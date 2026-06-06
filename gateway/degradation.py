"""
Five-level graceful degradation for Hermes gateway message sending.

Ensures user notifications are never silently dropped by providing
a fallback chain:

  L1: SDK/WS normal send (adapter.send())
  L2: HTTP REST API fallback (raw HTTP POST)
  L3: Persistent queue (local JSONL file, retry later)
  L4: Log-and-notify (write to audit log + best-effort alt channel)
  L5: Dead letter queue (final resort, human review required)

Phase 1 module — depends on Phase 0 FeishuTokenManager and self_heal_audit.
"""

from __future__ import annotations

import json
import logging
import os
import threading
import time
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from .self_heal_audit import SelfHealAuditor

logger = logging.getLogger(__name__)


class DegradationLevel(IntEnum):
    """Five degradation levels, ordered by severity."""
    L1_SDK = 1           # 正常 SDK/WS 发送
    L2_HTTP = 2          # HTTP REST API 回退
    L3_QUEUE = 3         # 持久化队列（稍后重试）
    L4_LOG = 4           # 审计日志 + 尽力通知
    L5_DEAD_LETTER = 5   # 死信队列（需人工介入）

    @property
    def label(self) -> str:
        labels = {
            1: "SDK 正常发送",
            2: "HTTP REST 回退",
            3: "持久化队列",
            4: "日志记录",
            5: "死信队列",
        }
        return labels[self]


@dataclass
class DegradationResult:
    """Result of a degradation attempt."""
    level: DegradationLevel
    success: bool
    message_id: str = ""
    error: str = ""
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> dict[str, Any]:
        return {
            "level": self.level.value,
            "level_label": self.level.label,
            "success": self.success,
            "message_id": self.message_id,
            "error": self.error,
            "timestamp": self.timestamp,
        }


@dataclass
class QueuedMessage:
    """A message waiting in the persistent queue (L3)."""
    message_id: str
    platform: str
    payload: dict[str, Any]
    created_at: float = field(default_factory=time.time)
    retry_count: int = 0
    last_retry_at: float = 0.0
    max_retries: int = 5


class FiveLevelDegradation:
    """
    Five-level message degradation manager.

    Usage::

        deg = FiveLevelDegradation(data_dir="/path/to/hermes/data")
        deg.register_http_fallback("feishu", my_http_send_fn)

        # When sending a message:
        result = deg.send_with_fallback(
            platform="feishu",
            adapter=adapter,
            message={"msg_type": "text", "content": {"text": "hello"}},
            message_id="msg_001",
        )

        # Retry queued messages (call periodically):
        await deg.retry_queue()
    """

    def __init__(
        self,
        data_dir: str | Path | None = None,
        audit: SelfHealAuditor | None = None,
        max_queue_size: int = 1000,
        retry_cooldown: float = 300.0,  # 队列消息重试冷却 5 分钟
    ) -> None:
        self._data_dir = Path(data_dir) if data_dir else Path.cwd() / "degradation"
        self._audit = audit
        self._max_queue_size = max_queue_size
        self._retry_cooldown = retry_cooldown
        self._lock = threading.Lock()

        # Per-platform HTTP fallback functions: platform -> callable(payload) -> bool
        self._http_fallbacks: Dict[str, Callable[[dict], bool]] = {}

        # Persistent queue storage
        self._queue_dir = self._data_dir / "queue"
        self._queue_dir.mkdir(parents=True, exist_ok=True)

        # Dead letter storage
        self._dead_letter_dir = self._data_dir / "dead_letters"
        self._dead_letter_dir.mkdir(parents=True, exist_ok=True)

        # In-memory queue index
        self._queue: Dict[str, QueuedMessage] = {}
        self._load_queue()

        # Statistics
        self._stats: Dict[str, Dict[str, int]] = {}  # platform -> {l1: n, l2: n, ...}

    def register_http_fallback(
        self, platform: str, fn: Callable[[dict], bool]
    ) -> None:
        """Register an HTTP fallback sender for a platform."""
        self._http_fallbacks[platform] = fn
        logger.info("[degradation] 注册 %s HTTP 回退发送器", platform)

    def send_with_fallback(
        self,
        platform: str,
        adapter: Any,
        message: dict[str, Any],
        message_id: str = "",
        context: str = "",
    ) -> DegradationResult:
        """
        Attempt to send a message, degrading through L1→L5 as needed.

        Args:
            platform: Target platform (feishu, qq, etc.)
            adapter: The platform adapter instance.
            message: The message payload to send.
            message_id: Optional unique ID for tracking.
            context: Optional context for logging.

        Returns:
            DegradationResult with the highest successful level.
        """
        message_id = message_id or f"msg_{int(time.time()*1000)}_{id(message)}"
        now = time.time()

        # Ensure stats dict exists
        if platform not in self._stats:
            self._stats[platform] = {}

        # --- L1: SDK/WS normal send ---
        try:
            result = adapter.send(message)
            if result and getattr(result, "success", True):
                self._record_stat(platform, "l1_success")
                logger.debug("[degradation] %s L1 发送成功: %s", platform, message_id)
                self._audit_log(
                    "send_success", platform, message_id,
                    {"level": 1, "context": context},
                )
                return DegradationResult(
                    level=DegradationLevel.L1_SDK,
                    success=True,
                    message_id=message_id,
                )
        except Exception as e:
            logger.warning(
                "[degradation] %s L1 发送失败: %s — %s",
                platform, message_id, e,
            )
        except:  # noqa: E722 — adapter.send() might raise anything
            logger.warning(
                "[degradation] %s L1 发送异常: %s",
                platform, message_id,
            )

        self._record_stat(platform, "l1_failure")

        # --- L2: HTTP REST API fallback ---
        http_fn = self._http_fallbacks.get(platform)
        if http_fn is not None:
            try:
                success = http_fn(message)
                if success:
                    self._record_stat(platform, "l2_success")
                    logger.info(
                        "[degradation] %s L2 HTTP 回退成功: %s", platform, message_id
                    )
                    self._audit_log(
                        "send_fallback", platform, message_id,
                        {"level": 2, "context": context},
                    )
                    return DegradationResult(
                        level=DegradationLevel.L2_HTTP,
                        success=True,
                        message_id=message_id,
                    )
            except Exception as e:
                logger.warning(
                    "[degradation] %s L2 HTTP 回退失败: %s — %s",
                    platform, message_id, e,
                )
            self._record_stat(platform, "l2_failure")
        else:
            logger.info(
                "[degradation] %s 未注册 HTTP 回退，跳过 L2", platform
            )

        # --- L3: Persistent queue ---
        queued = self._enqueue(
            QueuedMessage(
                message_id=message_id,
                platform=platform,
                payload=message,
            )
        )
        if queued:
            self._record_stat(platform, "l3_queue")
            logger.warning(
                "[degradation] %s L3 入队: %s（稍后重试）", platform, message_id
            )
            self._audit_log(
                "send_queued", platform, message_id,
                {"level": 3, "context": context},
            )
            return DegradationResult(
                level=DegradationLevel.L3_QUEUE,
                success=False,
                message_id=message_id,
                error="消息已持久化到队列，等待重试",
            )

        # --- L4: Audit log ---
        self._record_stat(platform, "l4_log")
        logger.error(
            "[degradation] %s L4 队列已满，消息仅记录到审计日志: %s | payload: %s",
            platform, message_id,
            json.dumps(message, ensure_ascii=False)[:200],
        )
        self._audit_log(
            "send_failed_log_only", platform, message_id,
            {"level": 4, "context": context, "payload_summary": str(message)[:200]},
        )
        return DegradationResult(
            level=DegradationLevel.L4_LOG,
            success=False,
            message_id=message_id,
            error="队列已满，消息仅记录到审计日志",
        )

    def retry_queue(
        self,
        adapters: Dict[str, Any] | None = None,
    ) -> List[DegradationResult]:
        """
        Attempt to send all queued messages.

        Called periodically (e.g., every 5 minutes) to drain the queue.
        Messages that still fail after max_retries are moved to dead letter.

        Args:
            adapters: Current active adapters dict {adapter_id: adapter}.
                     If None, only L2 (HTTP) retry is attempted.

        Returns:
            List of DegradationResult for attempted retries.
        """
        now = time.time()
        results = []

        with self._lock:
            to_remove = []
            for msg_id, qm in self._queue.items():
                # Check cooldown
                if now - qm.last_retry_at < self._retry_cooldown:
                    continue

                # Check max retries
                if qm.retry_count >= qm.max_retries:
                    self._move_to_dead_letter(qm)
                    to_remove.append(msg_id)
                    results.append(DegradationResult(
                        level=DegradationLevel.L5_DEAD_LETTER,
                        success=False,
                        message_id=msg_id,
                        error=f"超过最大重试次数 ({qm.max_retries})",
                    ))
                    continue

                # Attempt retry
                qm.retry_count += 1
                qm.last_retry_at = now
                success = False
                level_used = 3

                # Try adapter (L1) if available
                if adapters is not None:
                    adapter = adapters.get(qm.platform)
                    if adapter is not None:
                        try:
                            result = adapter.send(qm.payload)
                            if result and getattr(result, "success", True):
                                success = True
                                level_used = 1
                        except Exception:
                            pass

                # Try HTTP fallback (L2) if L1 failed
                if not success:
                    http_fn = self._http_fallbacks.get(qm.platform)
                    if http_fn is not None:
                        try:
                            success = http_fn(qm.payload)
                            if success:
                                level_used = 2
                        except Exception:
                            pass

                if success:
                    to_remove.append(msg_id)
                    self._remove_from_disk(msg_id)
                    self._record_stat(qm.platform, f"l{level_used}_retry_success")
                    logger.info(
                        "[degradation] %s 队列消息重试成功: %s (第 %d 次, L%d)",
                        qm.platform, msg_id, qm.retry_count, level_used,
                    )
                    self._audit_log(
                        "queue_retry_success", qm.platform, msg_id,
                        {"retry_count": qm.retry_count, "level": level_used},
                    )
                    results.append(DegradationResult(
                        level=DegradationLevel(level_used),
                        success=True,
                        message_id=msg_id,
                    ))
                else:
                    logger.warning(
                        "[degradation] %s 队列消息重试失败: %s (第 %d 次)",
                        qm.platform, msg_id, qm.retry_count,
                    )

            for msg_id in to_remove:
                self._queue.pop(msg_id, None)

        return results

    def get_queue_size(self, platform: str | None = None) -> int:
        """Get the number of messages in the persistent queue."""
        with self._lock:
            if platform is None:
                return len(self._queue)
            return sum(1 for qm in self._queue.values() if qm.platform == platform)

    def get_dead_letter_count(self, platform: str | None = None) -> int:
        """Get the number of dead letter messages."""
        count = 0
        for f in self._dead_letter_dir.glob("*.json"):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                if platform is None or data.get("platform") == platform:
                    count += 1
            except Exception:
                count += 1
        return count

    def get_stats(self) -> dict[str, Any]:
        """Export degradation statistics."""
        return {
            "per_platform": dict(self._stats),
            "queue_size": self.get_queue_size(),
            "dead_letter_count": self.get_dead_letter_count(),
        }

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _enqueue(self, qm: QueuedMessage) -> bool:
        """Add a message to the persistent queue. Returns False if full."""
        with self._lock:
            if len(self._queue) >= self._max_queue_size:
                return False
            self._queue[qm.message_id] = qm
            self._save_to_disk(qm)
            return True

    def _save_to_disk(self, qm: QueuedMessage) -> None:
        """Persist a queued message to disk."""
        path = self._queue_dir / f"{qm.message_id}.json"
        try:
            path.write_text(
                json.dumps({
                    "message_id": qm.message_id,
                    "platform": qm.platform,
                    "payload": qm.payload,
                    "created_at": qm.created_at,
                    "retry_count": qm.retry_count,
                    "last_retry_at": qm.last_retry_at,
                    "max_retries": qm.max_retries,
                }, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        except Exception:
            logger.exception("[degradation] 队列消息写入磁盘失败: %s", qm.message_id)

    def _remove_from_disk(self, message_id: str) -> None:
        """Remove a queued message from disk."""
        path = self._queue_dir / f"{message_id}.json"
        try:
            path.unlink(missing_ok=True)
        except Exception:
            pass

    def _load_queue(self) -> None:
        """Load queued messages from disk on startup."""
        count = 0
        for f in self._queue_dir.glob("*.json"):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                qm = QueuedMessage(
                    message_id=data["message_id"],
                    platform=data["platform"],
                    payload=data["payload"],
                    created_at=data.get("created_at", 0),
                    retry_count=data.get("retry_count", 0),
                    last_retry_at=data.get("last_retry_at", 0),
                    max_retries=data.get("max_retries", 5),
                )
                self._queue[qm.message_id] = qm
                count += 1
            except Exception:
                logger.exception("[degradation] 加载队列消息失败: %s", f)
        if count:
            logger.info("[degradation] 从磁盘加载了 %d 条队列消息", count)

    def _move_to_dead_letter(self, qm: QueuedMessage) -> None:
        """Move a message to the dead letter queue."""
        self._remove_from_disk(qm.message_id)
        path = self._dead_letter_dir / f"{qm.message_id}.json"
        try:
            path.write_text(
                json.dumps({
                    "message_id": qm.message_id,
                    "platform": qm.platform,
                    "payload": qm.payload,
                    "created_at": qm.created_at,
                    "retry_count": qm.retry_count,
                    "max_retries": qm.max_retries,
                    "dead_at": time.time(),
                }, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            logger.error(
                "[degradation] 消息移入死信队列: %s (platform=%s, retries=%d)",
                qm.message_id, qm.platform, qm.retry_count,
            )
            self._audit_log(
                "dead_letter", qm.platform, qm.message_id,
                {"retry_count": qm.retry_count},
            )
        except Exception:
            logger.exception("[degradation] 死信写入失败: %s", qm.message_id)

    def _record_stat(self, platform: str, key: str) -> None:
        """Record a degradation statistic."""
        if platform not in self._stats:
            self._stats[platform] = {}
        self._stats[platform][key] = self._stats[platform].get(key, 0) + 1

    def _audit_log(
        self,
        action: str,
        platform: str,
        message_id: str,
        details: dict[str, Any],
    ) -> None:
        """Log to the audit trail."""
        if self._audit is None:
            return
        try:
            self._audit.log({
                "action": action,
                "platform": platform,
                "message_id": message_id,
                **details,
            })
        except Exception:
            logger.exception("[degradation] 审计日志写入失败")
