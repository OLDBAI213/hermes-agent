"""
Self-heal system configuration manager.

Externalizes all self-heal thresholds so tuning does not require code changes.
Configuration is stored as JSON at ``~/.hermes/self_heal_config.json`` and
supports hot-reload (5-second cooldown between file stat checks).

Usage::

    from gateway.self_heal_config import SelfHealConfig

    config = SelfHealConfig()
    min_interval = config.get("adaptive_heartbeat", "min_interval")  # → 30
    config.set("quality_scorer", "critical_threshold", value=45)
    config.save()  # persist to disk
"""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Default values — serve as the fallback when the JSON file is missing keys
# or entirely absent.
# ---------------------------------------------------------------------------

DEFAULT_CONFIG: dict[str, Any] = {
    "adaptive_heartbeat": {
        "min_interval": 30,          # seconds — minimum probe interval
        "max_interval": 300,         # seconds — maximum probe interval
        "initial_interval": 60,      # seconds — starting probe interval
        "stable_threshold": 5,       # consecutive stable probes to increase interval
        "fail_threshold": 3,         # consecutive failures to declare disconnect
        "up_factor": 1.2,            # multiplier on interval increase
        "down_factor": 0.5,          # multiplier on interval decrease
    },
    "quality_scorer": {
        "window_size": 60,           # seconds — sliding window for metrics
        "degraded_threshold": 60,    # score ≤ 60 → DEGRADED
        "critical_threshold": 40,     # score ≤ 40 → CRITICAL
        "healthy_threshold": 80,     # score ≥ 80 → HEALTHY
        "weights": {
            "heartbeat_success_rate": 0.30,
            "message_latency": 0.20,
            "reconnect_frequency": 0.20,
            "error_rate": 0.15,
            "idle_stability": 0.15,
        },
    },
    "degradation": {
        "max_queue_size": 1000,       # L3 persistent queue max length
        "dlq_max_size": 5000,         # L5 dead-letter queue max length
        "retry_delay_secs": 30,       # L3 queue retry interval
        "max_retries": 3,             # per-message max retry count
    },
    "supervisor": {
        "max_restarts": 3,            # restarts within window before escalation
        "window_seconds": 300,        # restart counting window
    },
    "feishu_token": {
        "refresh_ahead_secs": 300,    # refresh N seconds before expiry
        "max_refresh_retries": 3,     # consecutive refresh failure limit
    },
}


class SelfHealConfig:
    """
    Manages self-heal configuration with file-backed persistence and hot-reload.

    - Reads from ``~/.hermes/self_heal_config.json`` if present.
    - Missing keys fall back to ``DEFAULT_CONFIG``.
    - ``reload_if_changed()`` checks file mtime for hot-reload.
    """

    def __init__(self, config_path: str | Path | None = None) -> None:
        if config_path is None:
            config_path = Path.home() / ".hermes" / "self_heal_config.json"
        elif isinstance(config_path, str):
            config_path = Path(config_path)
        self.config_path = config_path
        self._config: dict[str, Any] = _deep_copy(DEFAULT_CONFIG)
        self._loaded_at: float = 0.0
        self._file_mtime: float = 0.0
        self.load()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def load(self) -> dict[str, Any]:
        """Load config from disk, merging with defaults."""
        self._config = _deep_copy(DEFAULT_CONFIG)
        if self.config_path.exists():
            try:
                raw = self.config_path.read_text(encoding="utf-8")
                user_config = json.loads(raw)
                self._file_mtime = self.config_path.stat().st_mtime
                _deep_merge(self._config, user_config)
                self._loaded_at = time.time()
                logger.debug("Self-heal config loaded from %s", self.config_path)
            except Exception:
                logger.warning(
                    "Failed to load self_heal_config from %s, using defaults",
                    self.config_path,
                    exc_info=True,
                )
        return self._config

    def save(self) -> None:
        """Persist current config to disk."""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        self.config_path.write_text(
            json.dumps(self._config, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        self._file_mtime = self.config_path.stat().st_mtime
        self._loaded_at = time.time()

    def get(self, *keys: str, default: Any = None) -> Any:
        """
        Dot-path access: ``config.get("adaptive_heartbeat", "min_interval")`` → 30
        """
        obj: Any = self._config
        for key in keys:
            if isinstance(obj, dict) and key in obj:
                obj = obj[key]
            else:
                return default
        return obj

    def set(self, *keys: str, value: Any) -> None:
        """
        Dot-path mutation (not auto-persisted). Call ``save()`` explicitly.
        """
        obj: Any = self._config
        for key in keys[:-1]:
            if key not in obj or not isinstance(obj[key], dict):
                obj[key] = {}
            obj = obj[key]
        obj[keys[-1]] = value

    def reload_if_changed(self) -> bool:
        """
        Hot-reload: returns ``True`` if the file was reloaded.

        Includes a 5-second cooldown to avoid excessive stat calls.
        """
        if not self.config_path.exists():
            return False
        now = time.time()
        if now - self._loaded_at < 5:
            return False
        try:
            if self.config_path.stat().st_mtime > self._file_mtime:
                self.load()
                return True
        except OSError:
            pass
        return False

    @property
    def raw(self) -> dict[str, Any]:
        """Return the full merged config dict (for inspection/debugging)."""
        return _deep_copy(self._config)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _deep_copy(src: dict[str, Any]) -> dict[str, Any]:
    """Cheap deep copy via json round-trip (safe for our flat/nested dict)."""
    return json.loads(json.dumps(src))


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> None:
    """Recursively merge *override* into *base* in-place."""
    for k, v in override.items():
        if k in base and isinstance(base[k], dict) and isinstance(v, dict):
            _deep_merge(base[k], v)
        else:
            base[k] = v
