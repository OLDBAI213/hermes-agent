"""Helpers for agent status events that are consumed by UI frontends."""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


def emit_tui_model_status(agent: Any, text: str, *, debug_context: str = "model status") -> bool:
    """Emit model progress only for the Ink TUI.

    Messaging gateways also wire ``status_callback`` for user-visible platform
    messages. Model wait/stream heartbeat events are live UI chrome, not chat
    replies, so they must not leak into Feishu/Telegram/Discord/etc.
    """

    if getattr(agent, "platform", "") != "tui":
        return False

    callback = getattr(agent, "status_callback", None)
    if callback is None:
        return False

    try:
        callback("model", text)
    except Exception:
        logger.debug("status_callback error for %s", debug_context, exc_info=True)
        return False

    return True
