"""
Self-heal audit logger.

Records every autonomous self-heal action as a structured JSONL line so
operators can later answer "what happened and why?".

Use cases:
1. Post-incident analysis — why did the gateway auto-reconnect at 03:14?
2. Trend detection — DLQ depth surging / frequent restarts → systemic issue
3. Compliance — what remediation actions did the system take?

Usage::

    from gateway.self_heal_audit import SelfHealAuditor

    auditor = SelfHealAuditor()
    auditor.log("auto_reconnect", "feishu",
                details={"reason": "ping_timeout", "attempt": 3},
                level="warning")

    recent = auditor.query(platform="feishu", limit=10)
    summary = auditor.get_summary(hours=24)
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

_DEFAULT_AUDIT_PATH = Path.home() / ".hermes" / "self_heal_audit.jsonl"


class SelfHealAuditor:
    """
    Append-only JSONL audit logger for self-heal operations.

    Thread-safe (uses file-level atomic appends).  The ``query()`` and
    ``get_summary()`` methods read the full file, so they are not intended
    for hot-path usage — only for /health/detailed and /gateway status.
    """

    def __init__(self, path: str | Path | None = None) -> None:
        if path is None:
            path = _DEFAULT_AUDIT_PATH
        elif isinstance(path, str):
            path = Path(path)
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def log(
        self,
        action: str,
        platform: str,
        details: dict[str, Any] | None = None,
        level: str = "info",
        human_action: bool = False,
    ) -> None:
        """
        Append an audit entry.

        Parameters
        ----------
        action:
            Descriptive verb: ``auto_reconnect``, ``degrade_l2``, etc.
        platform:
            Platform identifier: ``feishu``, ``qqbot``, ``telegram``, etc.
        details:
            Arbitrary context dict (reason, error codes, counts, …).
        level:
            ``info`` / ``warning`` / ``critical``.
        human_action:
            ``True`` when the action was triggered by a human command
            (e.g. ``/gateway restart feishu``).
        """
        entry: dict[str, Any] = {
            "ts": time.time(),
            "ts_iso": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()),
            "action": action,
            "platform": platform,
            "level": level,
            "human_action": human_action,
            "details": details or {},
        }
        try:
            with open(self.path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except OSError:
            # Audit logging must never crash the gateway
            pass

    def query(
        self,
        platform: str | None = None,
        action: str | None = None,
        since: float | None = None,
        limit: int = 50,
    ) -> list[dict[str, Any]]:
        """
        Search the audit log (newest-first).

        Parameters
        ----------
        platform:
            Filter by platform name.
        action:
            Filter by action name (exact match).
        since:
            Unix timestamp lower bound.
        limit:
            Max entries to return.
        """
        if not self.path.exists():
            return []
        try:
            lines = self.path.read_text(encoding="utf-8").strip().split("\n")
        except OSError:
            return []

        results: list[dict[str, Any]] = []
        for line in reversed(lines):
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except (json.JSONDecodeError, KeyError):
                continue
            if since and entry.get("ts", 0) < since:
                continue
            if platform and entry.get("platform") != platform:
                continue
            if action and entry.get("action") != action:
                continue
            results.append(entry)
            if len(results) >= limit:
                break
        return results

    def get_summary(self, hours: int = 24) -> dict[str, Any]:
        """
        Return aggregated stats for the last *hours* hours.

        Useful for ``/health/detailed`` and ``/gateway status``.
        """
        since = time.time() - hours * 3600
        logs = self.query(since=since, limit=10000)
        summary: dict[str, Any] = {
            "total_actions": len(logs),
            "auto_reconnects": 0,
            "degradations": 0,
            "supervisor_restarts": 0,
            "human_interventions": 0,
            "critical_events": 0,
            "by_platform": {},
        }
        for entry in logs:
            action = entry.get("action", "")
            plat = entry.get("platform", "unknown")
            if plat not in summary["by_platform"]:
                summary["by_platform"][plat] = 0
            summary["by_platform"][plat] += 1

            if action == "auto_reconnect" or "reconnect" in action:
                summary["auto_reconnects"] += 1
            elif "degrade" in action:
                summary["degradations"] += 1
            elif "restart" in action:
                summary["supervisor_restarts"] += 1
            if entry.get("human_action"):
                summary["human_interventions"] += 1
            if entry.get("level") == "critical":
                summary["critical_events"] += 1
        return summary
