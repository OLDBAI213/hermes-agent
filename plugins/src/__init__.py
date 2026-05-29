"""SRC Suite — Hermes-facing SRC workflow facade."""

from __future__ import annotations

import json
from typing import Any

from .facade import SrcSuite

__all__ = ["SrcSuite", "register"]


def _handle_slash(raw_args: str = "") -> str:
    from . import status as _status

    subcommand = (raw_args or "status").strip().lower()
    if subcommand in {"", "status", "health"}:
        return json.dumps(_status.run_status(write_report=False), ensure_ascii=False, indent=2)
    if subcommand in {"full", "report"}:
        return json.dumps(_status.run_status(write_report=True), ensure_ascii=False, indent=2)
    return (
        "Usage: /src-suite [status|health|full|report]\n"
        "status/health runs the quick non-invasive health check; "
        "full/report also writes health artifacts."
    )


def register(ctx: Any) -> None:
    ctx.register_command(
        "src-suite",
        handler=_handle_slash,
        description="Check SRC Suite browser, Android, platform, and task-storage readiness.",
        args_hint="[status|health|full|report]",
    )
