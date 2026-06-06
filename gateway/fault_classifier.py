"""
Fault classifier for Hermes gateway adapter failures.

Classifies adapter errors into five fault types using pattern matching:
  - NETWORK:    网络连接问题 → 退避重连
  - AUTH:       认证/Token 问题 → 刷新 Token 后重连
  - RATE_LIMIT: 速率限制 → 等待后重试
  - SDK_BUG:    SDK 内部错误 → 完全重启 adapter
  - SERVER_DOWN: 远端服务不可用 → 暂停并通知
  - UNKNOWN:    无法分类 → 通用重连策略

Each fault type maps to a recommended self-healing strategy.

Phase 1 module — depends on Phase 0 FeishuTokenManager.
"""

from __future__ import annotations

import re
import time
import threading
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional


class FaultType(str, Enum):
    """Classified fault categories."""
    NETWORK = "network"
    AUTH = "auth"
    RATE_LIMIT = "rate_limit"
    SDK_BUG = "sdk_bug"
    SERVER_DOWN = "server_down"
    UNKNOWN = "unknown"


class HealingAction(str, Enum):
    """Recommended healing actions for each fault type."""
    BACKOFF_RECONNECT = "backoff_reconnect"      # 指数退避重连
    TOKEN_REFRESH_RECONNECT = "token_refresh_reconnect"  # 刷新 Token 后重连
    WAIT_RETRY = "wait_retry"                    # 等待一段时间后重试
    RESTART_ADAPTER = "restart_adapter"          # 完全重启 adapter
    PAUSE_NOTIFY = "pause_notify"                # 暂停并通知用户
    GENERIC_RECONNECT = "generic_reconnect"      # 通用重连


@dataclass
class FaultClassification:
    """Result of fault classification."""
    fault_type: FaultType
    confidence: float  # 0.0-1.0
    pattern_matched: str  # which regex pattern matched
    healing_action: HealingAction
    suggested_wait: float = 0.0  # seconds to wait before action
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> dict[str, Any]:
        return {
            "fault_type": self.fault_type.value,
            "confidence": round(self.confidence, 2),
            "pattern_matched": self.pattern_matched,
            "healing_action": self.healing_action.value,
            "suggested_wait": self.suggested_wait,
            "timestamp": self.timestamp,
        }


@dataclass
class PatternRule:
    """A single classification rule: regex → fault type + action."""
    pattern: re.Pattern
    fault_type: FaultType
    healing_action: HealingAction
    suggested_wait: float = 0.0
    confidence: float = 0.8


# Default pattern rules — ordered by specificity (most specific first)
DEFAULT_RULES: List[PatternRule] = [
    # --- AUTH (token/credential errors) ---
    PatternRule(
        pattern=re.compile(r"token.*(expired|invalid|revoked)", re.IGNORECASE),
        fault_type=FaultType.AUTH,
        healing_action=HealingAction.TOKEN_REFRESH_RECONNECT,
        suggested_wait=5.0,
        confidence=0.95,
    ),
    PatternRule(
        pattern=re.compile(r"(invalid|expired|revoked).*(token|credential|app_id|app_secret)", re.IGNORECASE),
        fault_type=FaultType.AUTH,
        healing_action=HealingAction.TOKEN_REFRESH_RECONNECT,
        suggested_wait=5.0,
        confidence=0.9,
    ),
    PatternRule(
        pattern=re.compile(r"99991668|99991663|99991664", re.IGNORECASE),
        # 飞书错误码: token expired / invalid
        fault_type=FaultType.AUTH,
        healing_action=HealingAction.TOKEN_REFRESH_RECONNECT,
        suggested_wait=5.0,
        confidence=0.95,
    ),
    PatternRule(
        pattern=re.compile(r"authentication.failed|unauthorized|forbidden", re.IGNORECASE),
        fault_type=FaultType.AUTH,
        healing_action=HealingAction.TOKEN_REFRESH_RECONNECT,
        suggested_wait=10.0,
        confidence=0.85,
    ),

    # --- RATE_LIMIT ---
    PatternRule(
        pattern=re.compile(r"rate.?limit|too.?many.?requests|throttl", re.IGNORECASE),
        fault_type=FaultType.RATE_LIMIT,
        healing_action=HealingAction.WAIT_RETRY,
        suggested_wait=60.0,
        confidence=0.9,
    ),
    PatternRule(
        pattern=re.compile(r"99991400|99991401|99991402|429", re.IGNORECASE),
        # 飞书/通用错误码: rate limit
        fault_type=FaultType.RATE_LIMIT,
        healing_action=HealingAction.WAIT_RETRY,
        suggested_wait=60.0,
        confidence=0.95,
    ),
    PatternRule(
        pattern=re.compile(r"quota.exceeded|request.limit", re.IGNORECASE),
        fault_type=FaultType.RATE_LIMIT,
        healing_action=HealingAction.WAIT_RETRY,
        suggested_wait=120.0,
        confidence=0.85,
    ),

    # --- SERVER_DOWN ---
    PatternRule(
        pattern=re.compile(r"502|503|504|service.unavailable|bad.gateway", re.IGNORECASE),
        fault_type=FaultType.SERVER_DOWN,
        healing_action=HealingAction.PAUSE_NOTIFY,
        suggested_wait=300.0,
        confidence=0.9,
    ),
    PatternRule(
        pattern=re.compile(r"99991696|99991697", re.IGNORECASE),
        # 飞书错误码: 服务不可用 / 内部错误
        fault_type=FaultType.SERVER_DOWN,
        healing_action=HealingAction.PAUSE_NOTIFY,
        suggested_wait=300.0,
        confidence=0.9,
    ),
    PatternRule(
        pattern=re.compile(r"server.*(down|unreachable|maintenance)", re.IGNORECASE),
        fault_type=FaultType.SERVER_DOWN,
        healing_action=HealingAction.PAUSE_NOTIFY,
        suggested_wait=300.0,
        confidence=0.8,
    ),

    # --- NETWORK ---
    PatternRule(
        pattern=re.compile(r"connection.*(refused|reset|timeout|lost|broken|closed)", re.IGNORECASE),
        fault_type=FaultType.NETWORK,
        healing_action=HealingAction.BACKOFF_RECONNECT,
        suggested_wait=30.0,
        confidence=0.9,
    ),
    PatternRule(
        pattern=re.compile(r"(timeout|timed.?out|eof|broken.pipe|socket.error)", re.IGNORECASE),
        fault_type=FaultType.NETWORK,
        healing_action=HealingAction.BACKOFF_RECONNECT,
        suggested_wait=30.0,
        confidence=0.85,
    ),
    PatternRule(
        pattern=re.compile(r"dns.*(fail|error|resolve)|name.or.service.not.known", re.IGNORECASE),
        fault_type=FaultType.NETWORK,
        healing_action=HealingAction.BACKOFF_RECONNECT,
        suggested_wait=60.0,
        confidence=0.9,
    ),
    PatternRule(
        pattern=re.compile(r"ssl|tls|certificate.*(error|fail|verify)", re.IGNORECASE),
        fault_type=FaultType.NETWORK,
        healing_action=HealingAction.BACKOFF_RECONNECT,
        suggested_wait=120.0,
        confidence=0.85,
    ),
    PatternRule(
        pattern=re.compile(r"network.*(unreachable|error|fail)", re.IGNORECASE),
        fault_type=FaultType.NETWORK,
        healing_action=HealingAction.BACKOFF_RECONNECT,
        suggested_wait=30.0,
        confidence=0.8,
    ),
    PatternRule(
        pattern=re.compile(r"websocket.*(closed|error|disconnect)", re.IGNORECASE),
        fault_type=FaultType.NETWORK,
        healing_action=HealingAction.BACKOFF_RECONNECT,
        suggested_wait=15.0,
        confidence=0.9,
    ),

    # --- SDK_BUG ---
    PatternRule(
        pattern=re.compile(r"TypeError|AttributeError|KeyError|ValueError|IndexError", re.IGNORECASE),
        fault_type=FaultType.SDK_BUG,
        healing_action=HealingAction.RESTART_ADAPTER,
        suggested_wait=5.0,
        confidence=0.7,
    ),
    PatternRule(
        pattern=re.compile(r"AssertionError|RuntimeError|RecursionError", re.IGNORECASE),
        fault_type=FaultType.SDK_BUG,
        healing_action=HealingAction.RESTART_ADAPTER,
        suggested_wait=5.0,
        confidence=0.75,
    ),
    PatternRule(
        pattern=re.compile(r"null.?pointer|null.?reference|nil", re.IGNORECASE),
        fault_type=FaultType.SDK_BUG,
        healing_action=HealingAction.RESTART_ADAPTER,
        suggested_wait=5.0,
        confidence=0.65,
    ),
]


class FaultClassifier:
    """
    Classifies adapter errors and recommends healing actions.

    Usage::

        classifier = FaultClassifier()

        result = classifier.classify(
            error_message="Connection reset by peer",
            error_type="ConnectionError",
        )
        # result.fault_type == FaultType.NETWORK
        # result.healing_action == HealingAction.BACKOFF_RECONNECT
        # result.suggested_wait == 30.0

    Custom rules can be added with `add_rule()` or `add_rules()`.
    """

    def __init__(
        self,
        rules: List[PatternRule] | None = None,
    ) -> None:
        self._rules: List[PatternRule] = list(rules or DEFAULT_RULES)
        self._lock = threading.Lock()

        # Statistics
        self._classification_count: Dict[str, int] = {}

    def classify(
        self,
        error_message: str = "",
        error_type: str = "",
        context: str = "",
    ) -> FaultClassification:
        """
        Classify an error based on its message, type, and context.

        Searches through rules in order; first match wins.
        Returns a FaultClassification with the best match.
        """
        # Combine all text for matching
        combined = " ".join(filter(None, [error_message, error_type, context]))

        best_match: Optional[PatternRule] = None
        best_confidence = 0.0
        matched_pattern = ""

        with self._lock:
            for rule in self._rules:
                m = rule.pattern.search(combined)
                if m:
                    if rule.confidence > best_confidence:
                        best_match = rule
                        best_confidence = rule.confidence
                        matched_pattern = m.group(0)

        if best_match is not None:
            result = FaultClassification(
                fault_type=best_match.fault_type,
                confidence=best_confidence,
                pattern_matched=matched_pattern,
                healing_action=best_match.healing_action,
                suggested_wait=best_match.suggested_wait,
            )
        else:
            result = FaultClassification(
                fault_type=FaultType.UNKNOWN,
                confidence=0.3,
                pattern_matched="",
                healing_action=HealingAction.GENERIC_RECONNECT,
                suggested_wait=30.0,
            )

        # Record stats
        key = result.fault_type.value
        self._classification_count[key] = self._classification_count.get(key, 0) + 1

        return result

    def add_rule(self, rule: PatternRule, prepend: bool = False) -> None:
        """Add a custom classification rule."""
        with self._lock:
            if prepend:
                self._rules.insert(0, rule)
            else:
                self._rules.append(rule)

    def add_rules(self, rules: List[PatternRule], prepend: bool = False) -> None:
        """Add multiple classification rules."""
        with self._lock:
            if prepend:
                self._rules = rules + self._rules
            else:
                self._rules.extend(rules)

    def get_stats(self) -> Dict[str, Any]:
        """Export classification statistics."""
        return {
            "classifications": dict(self._classification_count),
            "total": sum(self._classification_count.values()),
            "rules_count": len(self._rules),
        }

    def reset_stats(self) -> None:
        """Reset classification statistics."""
        self._classification_count.clear()

    def suggest_action(
        self,
        fault_type: FaultType,
        consecutive_count: int = 1,
    ) -> dict[str, Any]:
        """
        Get a detailed healing action suggestion based on fault type
        and how many times it has occurred consecutively.

        Escalation:
        - 1 occurrence: normal action
        - 2 occurrences: longer wait
        - 3+ occurrences: escalated action
        """
        base_actions = {
            FaultType.NETWORK: HealingAction.BACKOFF_RECONNECT,
            FaultType.AUTH: HealingAction.TOKEN_REFRESH_RECONNECT,
            FaultType.RATE_LIMIT: HealingAction.WAIT_RETRY,
            FaultType.SDK_BUG: HealingAction.RESTART_ADAPTER,
            FaultType.SERVER_DOWN: HealingAction.PAUSE_NOTIFY,
            FaultType.UNKNOWN: HealingAction.GENERIC_RECONNECT,
        }

        base_wait = {
            FaultType.NETWORK: 30.0,
            FaultType.AUTH: 10.0,
            FaultType.RATE_LIMIT: 60.0,
            FaultType.SDK_BUG: 5.0,
            FaultType.SERVER_DOWN: 300.0,
            FaultType.UNKNOWN: 30.0,
        }

        action = base_actions.get(fault_type, HealingAction.GENERIC_RECONNECT)
        wait = base_wait.get(fault_type, 30.0)

        # Escalation
        if consecutive_count >= 3:
            if fault_type == FaultType.NETWORK:
                action = HealingAction.RESTART_ADAPTER
                wait = 10.0
            elif fault_type == FaultType.AUTH:
                action = HealingAction.PAUSE_NOTIFY
                wait = 60.0
            elif fault_type == FaultType.RATE_LIMIT:
                action = HealingAction.PAUSE_NOTIFY
                wait = 300.0
            elif fault_type == FaultType.SDK_BUG:
                action = HealingAction.PAUSE_NOTIFY
                wait = 60.0
            wait *= 2  # double the wait for escalation
        elif consecutive_count >= 2:
            wait *= 1.5  # 50% longer wait

        return {
            "fault_type": fault_type.value,
            "action": action.value,
            "suggested_wait": wait,
            "consecutive_count": consecutive_count,
            "escalated": consecutive_count >= 3,
        }
