"""
Lightweight built-in metrics collector for the Hermes gateway.

Provides Counter, Gauge, and Histogram metric types with label support.
Designed as a minimal data pipeline for ConnectionQualityScorer and
/health/detailed — no external dependencies (Prometheus/OTel).
Phase 3 may upgrade to an external exporter.
"""

from __future__ import annotations

import threading
import time
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class MetricPoint:
    """A single metric observation."""
    value: float
    timestamp: float = field(default_factory=time.time)
    labels: Dict[str, str] = field(default_factory=dict)


class GatewayMetrics:
    """
    Singleton metrics collector.

    Usage::

        metrics = GatewayMetrics()          # returns singleton
        metrics.counter_inc("adapter_inbound_total", {"platform": "feishu"})
        metrics.gauge_set("adapter_quality_score", 85.0, {"platform": "feishu"})
        metrics.histogram_observe("adapter_send_latency_ms", 42.5, {"platform": "feishu"})

        snapshot = metrics.snapshot()      # export all metrics
    """

    _instance: Optional["GatewayMetrics"] = None
    _lock = threading.Lock()

    def __new__(cls) -> "GatewayMetrics":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance._initialized = False
                    cls._instance = instance
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return
        self._initialized = True
        self._counters: Dict[str, int] = defaultdict(int)
        self._gauges: Dict[str, float] = {}
        self._histograms: Dict[str, List[float]] = defaultdict(list)
        self._events: List[dict] = []  # recent event log (capped at 1000)

    # ------------------------------------------------------------------
    # Counter — monotonically increasing integer
    # ------------------------------------------------------------------

    def counter_inc(self, name: str, labels: dict[str, str] | None = None, amount: int = 1) -> None:
        """Increment a counter by *amount* (default 1)."""
        key = self._make_key(name, labels)
        self._counters[key] += amount
        self._append_event("counter", name, amount, labels)

    def counter_get(self, name: str, labels: dict[str, str] | None = None) -> int:
        """Return current counter value."""
        return self._counters.get(self._make_key(name, labels), 0)

    # ------------------------------------------------------------------
    # Gauge — point-in-time float value
    # ------------------------------------------------------------------

    def gauge_set(self, name: str, value: float, labels: dict[str, str] | None = None) -> None:
        """Set a gauge to *value*."""
        self._gauges[self._make_key(name, labels)] = value

    def gauge_get(self, name: str, labels: dict[str, str] | None = None) -> float | None:
        """Return current gauge value, or ``None`` if unset."""
        return self._gauges.get(self._make_key(name, labels))

    # ------------------------------------------------------------------
    # Histogram — distribution of observations (latencies, sizes, etc.)
    # ------------------------------------------------------------------

    def histogram_observe(
        self,
        name: str,
        value: float,
        labels: dict[str, str] | None = None,
    ) -> None:
        """Record a single observation."""
        key = self._make_key(name, labels)
        bucket = self._histograms[key]
        bucket.append(value)
        # Cap at 500 observations to bound memory
        if len(bucket) > 500:
            del bucket[: len(bucket) - 500]

    def histogram_stats(
        self, name: str, labels: dict[str, str] | None = None
    ) -> dict[str, Any]:
        """Return p50 / p95 / p99 / avg / count for a histogram."""
        key = self._make_key(name, labels)
        return self._stats_for_values(self._histograms.get(key, []))

    # ------------------------------------------------------------------
    # Snapshot — export all metrics at once
    # ------------------------------------------------------------------

    def snapshot(self) -> dict[str, Any]:
        """
        Export a snapshot of all metrics.

        Used by ``/health/detailed`` and ``ConnectionQualityScorer``.
        """
        return {
            "counters": dict(self._counters),
            "gauges": dict(self._gauges),
            "histograms": {
                key: self._stats_for_values(values)
                for key, values in self._histograms.items()
            },
            "recent_events": self._events[-20:],
        }

    def snapshot_for_platform(self, platform: str) -> dict[str, Any]:
        """Export metrics filtered by *platform* label."""
        tag = f",platform={platform}"
        filtered_counters = {
            k: v for k, v in self._counters.items() if tag in k
        }
        filtered_gauges = {
            k: v for k, v in self._gauges.items() if tag in k
        }
        filtered_hist = {
            k: self._stats_for_values(v)
            for k, v in self._histograms.items()
            if tag in k
        }
        return {
            "counters": filtered_counters,
            "gauges": filtered_gauges,
            "histograms": filtered_hist,
        }

    # ------------------------------------------------------------------
    # Reset (primarily for tests)
    # ------------------------------------------------------------------

    def reset(self) -> None:
        """Clear all collected metrics."""
        self._counters.clear()
        self._gauges.clear()
        self._histograms.clear()
        self._events.clear()

    @classmethod
    def _reset_singleton(cls) -> None:
        """Reset the singleton entirely (for tests)."""
        with cls._lock:
            if cls._instance is not None:
                cls._instance.reset()
                cls._instance._initialized = False
                cls._instance = None

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _make_key(self, name: str, labels: dict[str, str] | None) -> str:
        if not labels:
            return name
        label_str = ",".join(f"{k}={v}" for k, v in sorted(labels.items()))
        return f"{name}{{{label_str}}}"

    def _append_event(
        self, event_type: str, name: str, value: Any, labels: dict[str, str] | None
    ) -> None:
        self._events.append({
            "type": event_type,
            "name": name,
            "value": value,
            "labels": labels or {},
            "ts": time.time(),
        })
        if len(self._events) > 1000:
            del self._events[: len(self._events) - 500]

    @staticmethod
    def _stats_for_values(values: list[float]) -> dict[str, Any]:
        if not values:
            return {"count": 0, "avg": 0, "p50": 0, "p95": 0, "p99": 0}
        sorted_v = sorted(values)
        n = len(sorted_v)
        return {
            "count": n,
            "avg": round(sum(sorted_v) / n, 2),
            "p50": sorted_v[n // 2],
            "p95": sorted_v[int(n * 0.95)] if n >= 20 else sorted_v[-1],
            "p99": sorted_v[int(n * 0.99)] if n >= 100 else sorted_v[-1],
        }
