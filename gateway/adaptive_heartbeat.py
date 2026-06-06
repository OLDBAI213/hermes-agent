"""
Adaptive heartbeat probe for Hermes gateway adapters.

Monitors adapter liveness with a dynamically adjusting interval:
- Stable connections → interval increases (save resources)
- Failing probes → interval decreases (more sensitive)
- 3 consecutive failures → trigger DISCONNECT callback

Data sources (Phase 0):
  - adapter._last_inbound_ts / _last_outbound_ts (base.py)
  - adapter._ws_last_pong_ts (feishu.py _bridge_ws_ping_pong)
  - GatewayMetrics singleton counters/gauges

Phase 1 module — depends on Phase 0 infrastructure.
"""

from __future__ import annotations

import asyncio
import logging
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Coroutine, Dict, Optional

from .metrics import GatewayMetrics

logger = logging.getLogger(__name__)


class HeartbeatStatus(str, Enum):
    """Current state of the heartbeat probe for an adapter."""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    FAILING = "failing"
    DISCONNECTED = "disconnected"


@dataclass
class HeartbeatConfig:
    """Tunable parameters for adaptive heartbeat."""
    min_interval: float = 30.0       # 最小探测间隔（秒）
    max_interval: float = 300.0      # 最大探测间隔（秒）
    initial_interval: float = 60.0   # 初始探测间隔（秒）
    upscale_factor: float = 1.2       # 稳定上调系数（连续 stable_count 次稳定后 ×1.2）
    downscale_factor: float = 0.5     # 失败下调系数（每次失败 ÷2）
    stable_count_threshold: int = 5  # 连续稳定 N 次后上调间隔
    fail_threshold: int = 3           # 连续失败 N 次后触发 DISCONNECT
    inbound_stale_seconds: float = 300.0  # 入站消息超过 N 秒视为 stale
    outbound_stale_seconds: float = 600.0 # 出站消息超过 N 秒视为 stale


@dataclass
class HeartbeatState:
    """Per-adapter heartbeat state."""
    adapter_id: str
    platform: str
    status: HeartbeatStatus = HeartbeatStatus.HEALTHY
    interval: float = 60.0
    consecutive_stable: int = 0
    consecutive_failures: int = 0
    total_probes: int = 0
    total_failures: int = 0
    last_probe_ts: float = 0.0
    last_success_ts: float = 0.0
    last_failure_ts: float = 0.0
    last_failure_reason: str = ""


class AdaptiveHeartbeat:
    """
    Per-adapter adaptive heartbeat manager.

    Usage::

        hb = AdaptiveHeartbeat()
        hb.register("feishu_main", "feishu")

        # In the main loop or a background task:
        await hb.tick_all(adapters_dict, on_disconnect=handle_disconnect)

    The tick_all method should be called periodically (e.g., every 10 seconds).
    It checks each registered adapter against its current interval and
    performs a liveness probe if the interval has elapsed.
    """

    def __init__(
        self,
        config: HeartbeatConfig | None = None,
        metrics: GatewayMetrics | None = None,
    ) -> None:
        self._config = config or HeartbeatConfig()
        self._metrics = metrics or GatewayMetrics()
        self._states: Dict[str, HeartbeatState] = {}
        self._lock = asyncio.Lock() if False else None  # 非异步上下文用 threading.Lock
        import threading
        self._lock = threading.Lock()

    def register(self, adapter_id: str, platform: str) -> HeartbeatState:
        """Register an adapter for heartbeat monitoring."""
        with self._lock:
            if adapter_id in self._states:
                return self._states[adapter_id]
            state = HeartbeatState(
                adapter_id=adapter_id,
                platform=platform,
                interval=self._config.initial_interval,
            )
            self._states[adapter_id] = state
            logger.info(
                "[heartbeat] 注册适配器 %s (%s)，初始间隔 %.0fs",
                adapter_id, platform, self._config.initial_interval,
            )
            return state

    def unregister(self, adapter_id: str) -> None:
        """Remove an adapter from heartbeat monitoring."""
        with self._lock:
            self._states.pop(adapter_id, None)

    def probe(self, adapter: Any) -> dict[str, Any]:
        """
        Perform a synchronous liveness probe on an adapter.

        Returns a dict with probe results:
          - alive (bool): whether the adapter appears alive
          - reason (str): human-readable explanation
          - inbound_stale (bool): no inbound messages for too long
          - outbound_stale (bool): no outbound messages for too long
          - seconds_since_inbound (float)
          - seconds_since_outbound (float)
          - seconds_since_pong (float | None): SDK ping/pong age
        """
        now = time.time()
        result: dict[str, Any] = {
            "alive": True,
            "reason": "正常",
            "inbound_stale": False,
            "outbound_stale": False,
            "seconds_since_inbound": float("inf"),
            "seconds_since_outbound": float("inf"),
            "seconds_since_pong": None,
        }

        # Check inbound activity
        last_inbound = getattr(adapter, "_last_inbound_ts", 0)
        if last_inbound > 0:
            since_inbound = now - last_inbound
            result["seconds_since_inbound"] = since_inbound
            if since_inbound > self._config.inbound_stale_seconds:
                result["inbound_stale"] = True
                result["alive"] = False
                result["reason"] = f"入站消息已停滞 {since_inbound:.0f}s"

        # Check outbound activity
        last_outbound = getattr(adapter, "_last_outbound_ts", 0)
        if last_outbound > 0:
            since_outbound = now - last_outbound
            result["seconds_since_outbound"] = since_outbound
            if since_outbound > self._config.outbound_stale_seconds:
                result["outbound_stale"] = True
                if result["alive"]:
                    result["alive"] = False
                    result["reason"] = f"出站消息已停滞 {since_outbound:.0f}s"

        # Check SDK ping/pong (feishu-specific)
        last_pong = getattr(adapter, "_ws_last_pong_ts", None)
        if last_pong is not None and last_pong > 0:
            since_pong = now - last_pong
            result["seconds_since_pong"] = since_pong
            # SDK pong 超过 2 分钟视为异常
            if since_pong > 120:
                if result["alive"]:
                    result["alive"] = False
                    result["reason"] = f"SDK pong 已停滞 {since_pong:.0f}s"

        # Check adapter fatal_error flag
        if getattr(adapter, "fatal_error", None):
            result["alive"] = False
            result["reason"] = f"适配器 fatal_error: {adapter.fatal_error}"

        return result

    def tick(
        self,
        adapter_id: str,
        adapter: Any,
        on_disconnect: Callable[[str, str], Coroutine[Any, Any, None]] | None = None,
    ) -> HeartbeatState:
        """
        Check if a heartbeat probe is due, and perform it if so.

        Returns the updated HeartbeatState.
        If on_disconnect is provided and fail_threshold is reached,
        the callback will be awaited (caller must run in async context).
        """
        now = time.time()
        with self._lock:
            state = self._states.get(adapter_id)
            if state is None:
                state = self.register(adapter_id, getattr(adapter, "platform_name", "unknown"))

            # Check if probe is due
            if now - state.last_probe_ts < state.interval:
                return state

            # Perform probe
            state.last_probe_ts = now
            state.total_probes += 1
            probe_result = self.probe(adapter)

            # Update metrics
            self._metrics.counter_inc(
                "heartbeat_probes_total",
                {"platform": state.platform, "adapter_id": adapter_id},
            )

            if probe_result["alive"]:
                # --- Success path ---
                state.consecutive_stable += 1
                state.consecutive_failures = 0
                state.last_success_ts = now
                state.status = HeartbeatStatus.HEALTHY

                # Check if we should upscale interval
                if state.consecutive_stable >= self._config.stable_count_threshold:
                    old_interval = state.interval
                    state.interval = min(
                        state.interval * self._config.upscale_factor,
                        self._config.max_interval,
                    )
                    state.consecutive_stable = 0
                    if state.interval != old_interval:
                        logger.info(
                            "[heartbeat] %s 连续 %d 次稳定，间隔 %.0fs → %.0fs",
                            adapter_id,
                            self._config.stable_count_threshold,
                            old_interval,
                            state.interval,
                        )

                self._metrics.gauge_set(
                    "heartbeat_interval_seconds",
                    state.interval,
                    {"platform": state.platform},
                )

            else:
                # --- Failure path ---
                state.consecutive_failures += 1
                state.consecutive_stable = 0
                state.total_failures += 1
                state.last_failure_ts = now
                state.last_failure_reason = probe_result["reason"]

                self._metrics.counter_inc(
                    "heartbeat_failures_total",
                    {"platform": state.platform, "adapter_id": adapter_id},
                )

                # Downscale interval for faster detection
                old_interval = state.interval
                state.interval = max(
                    state.interval * self._config.downscale_factor,
                    self._config.min_interval,
                )
                if state.interval != old_interval:
                    logger.warning(
                        "[heartbeat] %s 探测失败: %s，间隔 %.0fs → %.0fs",
                        adapter_id,
                        probe_result["reason"],
                        old_interval,
                        state.interval,
                    )

                # Update status based on failure count
                if state.consecutive_failures >= self._config.fail_threshold:
                    state.status = HeartbeatStatus.DISCONNECTED
                    logger.error(
                        "[heartbeat] %s 连续 %d 次失败，标记为 DISCONNECTED: %s",
                        adapter_id,
                        state.consecutive_failures,
                        probe_result["reason"],
                    )
                elif state.consecutive_failures >= 2:
                    state.status = HeartbeatStatus.FAILING
                else:
                    state.status = HeartbeatStatus.DEGRADED

                # Trigger disconnect callback if threshold reached
                if (
                    state.consecutive_failures >= self._config.fail_threshold
                    and on_disconnect is not None
                ):
                    try:
                        import asyncio
                        loop = asyncio.get_event_loop()
                        if loop.is_running():
                            asyncio.ensure_future(
                                on_disconnect(adapter_id, probe_result["reason"])
                            )
                        else:
                            loop.run_until_complete(
                                on_disconnect(adapter_id, probe_result["reason"])
                            )
                    except Exception:
                        logger.exception(
                            "[heartbeat] %s on_disconnect 回调异常", adapter_id
                        )

            return state

    def tick_all(
        self,
        adapters: Dict[str, Any],
        on_disconnect: Callable[[str, str], Coroutine[Any, Any, None]] | None = None,
    ) -> Dict[str, HeartbeatState]:
        """Tick all registered adapters. Returns updated states."""
        results = {}
        for adapter_id, adapter in adapters.items():
            try:
                results[adapter_id] = self.tick(adapter_id, adapter, on_disconnect)
            except Exception:
                logger.exception("[heartbeat] %s tick 异常", adapter_id)
        return results

    def get_state(self, adapter_id: str) -> HeartbeatState | None:
        """Get the current heartbeat state for an adapter."""
        with self._lock:
            return self._states.get(adapter_id)

    def get_all_states(self) -> Dict[str, HeartbeatState]:
        """Get heartbeat states for all registered adapters."""
        with self._lock:
            return dict(self._states)

    def snapshot(self) -> dict[str, Any]:
        """Export a snapshot for /health/detailed."""
        with self._lock:
            return {
                "adapters": {
                    aid: {
                        "platform": s.platform,
                        "status": s.status.value,
                        "interval": round(s.interval, 1),
                        "consecutive_stable": s.consecutive_stable,
                        "consecutive_failures": s.consecutive_failures,
                        "total_probes": s.total_probes,
                        "total_failures": s.total_failures,
                        "last_probe_ts": s.last_probe_ts,
                        "last_success_ts": s.last_success_ts,
                        "last_failure_ts": s.last_failure_ts,
                        "last_failure_reason": s.last_failure_reason,
                    }
                    for aid, s in self._states.items()
                }
            }
