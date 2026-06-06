"""
Connection quality scorer for Hermes gateway adapters.

Computes a 0-100 quality score based on five dimensions:
  1. Heartbeat success rate (weight: 0.30)
  2. Message latency (weight: 0.20)
  3. Reconnect frequency (weight: 0.20)
  4. Error rate (weight: 0.15)
  5. Idle stability (weight: 0.15)

Thresholds:
  - >= 80: HEALTHY
  - >= 60: DEGRADED
  - >= 40: UNSTABLE (预防性重连)
  - <  40: CRITICAL (强制重连)

Phase 1 module — depends on Phase 0 GatewayMetrics.
"""

from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional

from .metrics import GatewayMetrics


class QualityLevel(str, Enum):
    """Connection quality classification."""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNSTABLE = "unstable"
    CRITICAL = "critical"


@dataclass
class QualityConfig:
    """Tunable parameters for quality scoring."""
    # Dimension weights (must sum to 1.0)
    weight_heartbeat: float = 0.30
    weight_latency: float = 0.20
    weight_reconnect: float = 0.20
    weight_error: float = 0.15
    weight_idle: float = 0.15

    # Thresholds
    threshold_healthy: float = 80.0
    threshold_degraded: float = 60.0
    threshold_unstable: float = 40.0

    # Latency scoring (ms)
    latency_good: float = 500.0      # <= 500ms: full score
    latency_bad: float = 5000.0      # >= 5s: zero score

    # Reconnect scoring
    reconnect_good: float = 1.0       # <= 1 次/小时: full score
    reconnect_bad: float = 5.0        # >= 5 次/小时: zero score

    # Error rate scoring
    error_good: float = 0.01          # <= 1%: full score
    error_bad: float = 0.20           # >= 20%: zero score

    # Idle stability
    idle_good_seconds: float = 3600.0  # <= 1h: full score
    idle_bad_seconds: float = 300.0    # <= 5min 无活动: zero score


@dataclass
class QualitySnapshot:
    """A point-in-time quality assessment for one adapter."""
    adapter_id: str
    platform: str
    score: float  # 0-100
    level: QualityLevel
    dimensions: Dict[str, float] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> dict[str, Any]:
        return {
            "adapter_id": self.adapter_id,
            "platform": self.platform,
            "score": round(self.score, 1),
            "level": self.level.value,
            "dimensions": {k: round(v, 2) for k, v in self.dimensions.items()},
            "timestamp": self.timestamp,
        }


class ConnectionQualityScorer:
    """
    Computes connection quality scores for adapters.

    Usage::

        scorer = ConnectionQualityScorer()
        snapshot = scorer.score("feishu_main", "feishu")
    """

    def __init__(
        self,
        config: QualityConfig | None = None,
        metrics: GatewayMetrics | None = None,
    ) -> None:
        self._config = config or QualityConfig()
        self._metrics = metrics or GatewayMetrics()
        self._lock = threading.Lock()
        # History per adapter: list of (timestamp, score) for trend analysis
        self._history: Dict[str, list[tuple[float, float]]] = {}
        self._history_max = 100  # keep last 100 scores per adapter

    def score(
        self,
        adapter_id: str,
        platform: str,
        heartbeat_state: dict[str, Any] | None = None,
        adapter: Any | None = None,
    ) -> QualitySnapshot:
        """
        Compute a quality score for the given adapter.

        Args:
            adapter_id: Unique adapter identifier.
            platform: Platform name (feishu, qq, etc.).
            heartbeat_state: Optional dict from AdaptiveHeartbeat.get_state().
                             If None, uses metrics data only.
            adapter: Optional adapter instance for direct attribute access.

        Returns:
            QualitySnapshot with score and level.
        """
        now = time.time()
        labels = {"platform": platform, "adapter_id": adapter_id}

        # 1. Heartbeat success rate (0-100)
        heartbeat_score = self._score_heartbeat(heartbeat_state, labels)

        # 2. Message latency (0-100)
        latency_score = self._score_latency(labels)

        # 3. Reconnect frequency (0-100)
        reconnect_score = self._score_reconnect(labels)

        # 4. Error rate (0-100)
        error_score = self._score_error(labels)

        # 5. Idle stability (0-100)
        idle_score = self._score_idle(adapter_id, adapter, labels)

        # Weighted composite
        composite = (
            heartbeat_score * self._config.weight_heartbeat
            + latency_score * self._config.weight_latency
            + reconnect_score * self._config.weight_reconnect
            + error_score * self._config.weight_error
            + idle_score * self._config.weight_idle
        )
        composite = max(0.0, min(100.0, composite))

        # Determine level
        if composite >= self._config.threshold_healthy:
            level = QualityLevel.HEALTHY
        elif composite >= self._config.threshold_degraded:
            level = QualityLevel.DEGRADED
        elif composite >= self._config.threshold_unstable:
            level = QualityLevel.UNSTABLE
        else:
            level = QualityLevel.CRITICAL

        snapshot = QualitySnapshot(
            adapter_id=adapter_id,
            platform=platform,
            score=composite,
            level=level,
            dimensions={
                "heartbeat": heartbeat_score,
                "latency": latency_score,
                "reconnect": reconnect_score,
                "error": error_score,
                "idle": idle_score,
            },
            timestamp=now,
        )

        # Store in history
        with self._lock:
            history = self._history.setdefault(adapter_id, [])
            history.append((now, composite))
            if len(history) > self._history_max:
                del history[: len(history) - self._history_max]

        # Update gauge
        self._metrics.gauge_set("adapter_quality_score", composite, labels)

        return snapshot

    def _score_heartbeat(
        self, state: dict[str, Any] | None, labels: dict[str, str]
    ) -> float:
        """Score based on heartbeat success rate."""
        if state is None:
            # Fall back to metrics counters
            probes = self._metrics.counter_get("heartbeat_probes_total", labels)
            failures = self._metrics.counter_get("heartbeat_failures_total", labels)
            if probes == 0:
                return 50.0  # 没有心跳数据时给中性分
            rate = 1.0 - (failures / probes)
            return rate * 100.0

        total = state.get("total_probes", 0)
        failures = state.get("total_failures", 0)
        if total == 0:
            return 50.0

        rate = 1.0 - (failures / total)

        # Penalize for recent failures
        consecutive = state.get("consecutive_failures", 0)
        if consecutive >= 3:
            rate *= 0.3
        elif consecutive >= 2:
            rate *= 0.6
        elif consecutive >= 1:
            rate *= 0.85

        return max(0.0, min(100.0, rate * 100.0))

    def _score_latency(self, labels: dict[str, str]) -> float:
        """Score based on send latency (lower is better)."""
        stats = self._metrics.histogram_stats("adapter_send_latency_ms", labels)
        avg = stats.get("avg", 0)

        if avg <= 0:
            return 70.0  # 没有延迟数据时给中等偏高（假设正常）

        if avg <= self._config.latency_good:
            return 100.0
        if avg >= self._config.latency_bad:
            return 0.0

        # Linear interpolation
        ratio = (avg - self._config.latency_good) / (
            self._config.latency_bad - self._config.latency_good
        )
        return max(0.0, min(100.0, (1.0 - ratio) * 100.0))

    def _score_reconnect(self, labels: dict[str, str]) -> float:
        """Score based on reconnect frequency (fewer is better)."""
        reconnects = self._metrics.counter_get("adapter_reconnects_total", labels)

        # Normalize to per-hour rate (approximate using uptime from first event)
        events = self._metrics.snapshot().get("recent_events", [])
        reconnect_events = [
            e for e in events
            if e.get("name") == "adapter_reconnects_total"
            and e.get("labels", {}).get("platform") == labels.get("platform")
        ]
        if not reconnect_events:
            return 80.0  # 没有重连记录时给高分

        # Simple: use raw count, capped
        if reconnects <= self._config.reconnect_good:
            return 100.0
        if reconnects >= self._config.reconnect_bad:
            return 0.0

        ratio = (reconnects - self._config.reconnect_good) / (
            self._config.reconnect_bad - self._config.reconnect_good
        )
        return max(0.0, min(100.0, (1.0 - ratio) * 100.0))

    def _score_error(self, labels: dict[str, str]) -> float:
        """Score based on error rate (lower is better)."""
        total_sends = self._metrics.counter_get("adapter_outbound_total", labels)
        failed_sends = self._metrics.counter_get("adapter_outbound_failed_total", labels)

        if total_sends == 0:
            return 80.0  # 没有发送记录时给高分

        error_rate = failed_sends / total_sends

        if error_rate <= self._config.error_good:
            return 100.0
        if error_rate >= self._config.error_bad:
            return 0.0

        ratio = (error_rate - self._config.error_good) / (
            self._config.error_bad - self._config.error_good
        )
        return max(0.0, min(100.0, (1.0 - ratio) * 100.0))

    def _score_idle(
        self,
        adapter_id: str,
        adapter: Any | None,
        labels: dict[str, str],
    ) -> float:
        """Score based on idle stability (longer idle = better, but not too long)."""
        now = time.time()
        last_activity = 0.0

        if adapter is not None:
            inbound = getattr(adapter, "_last_inbound_ts", 0)
            outbound = getattr(adapter, "_last_outbound_ts", 0)
            last_activity = max(inbound, outbound)

        if last_activity == 0:
            return 70.0  # 没有活动记录

        idle_seconds = now - last_activity

        # Being active is good; short idle is fine; long idle (no messages)
        # could mean a problem.
        if idle_seconds <= self._config.idle_bad_seconds:
            # Very recent activity — healthy
            return 100.0

        if idle_seconds >= self._config.idle_good_seconds:
            # Very long idle — could be a problem
            return 30.0

        # Linear interpolation between bad and good
        ratio = (idle_seconds - self._config.idle_bad_seconds) / (
            self._config.idle_good_seconds - self._config.idle_bad_seconds
        )
        return max(0.0, min(100.0, (1.0 - ratio) * 100.0))

    def get_history(self, adapter_id: str) -> list[tuple[float, float]]:
        """Get score history for an adapter: [(timestamp, score), ...]."""
        with self._lock:
            return list(self._history.get(adapter_id, []))

    def get_trend(self, adapter_id: str, window: int = 10) -> str:
        """
        Get score trend direction: 'improving', 'stable', 'declining', 'unknown'.

        Compares the average of the last `window` scores against the
        average of the `window` scores before that.
        """
        with self._lock:
            history = self._history.get(adapter_id, [])

        if len(history) < window * 2:
            return "unknown"

        recent_avg = sum(s for _, s in history[-window:]) / window
        prior_avg = sum(s for _, s in history[-(window * 2):-window]) / window

        diff = recent_avg - prior_avg
        if diff > 5:
            return "improving"
        elif diff < -5:
            return "declining"
        return "stable"

    def snapshot_all(self) -> dict[str, Any]:
        """Export all scores for /health/detailed."""
        with self._lock:
            return {
                "history_per_adapter": {
                    aid: [(ts, round(score, 1)) for ts, score in hist]
                    for aid, hist in self._history.items()
                }
            }
