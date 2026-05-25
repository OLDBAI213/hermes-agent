"""Gateway runtime-metadata footer.

Renders a compact footer showing runtime state (model, provider, context %, cwd) and
appends it to the FINAL message of an agent turn when enabled.  Off by default
to keep replies minimal.

Config (``~/.hermes/config.yaml``)::

    display:
      runtime_footer:
        enabled: true                       # off by default
        fields: [model, provider, context]  # order shown; drop any to hide
        style: zh_detailed                  # optional: labeled Chinese output

Per-platform overrides live under ``display.platforms.<platform>.runtime_footer``.
Users can toggle the global setting with ``/footer on|off`` from both the CLI
and any gateway platform.

The footer is appended to the final response text in ``gateway/run.py`` right
before returning the response to the adapter send path — so it only lands on
the final message a user sees, not on tool-progress updates or streaming
partials.  When streaming is on and the final text has already been delivered
piecemeal, the footer is sent as a separate trailing message via
``send_trailing_footer()``.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Iterable, Optional

_DEFAULT_FIELDS: tuple[str, ...] = ("model", "context_pct", "cwd")
_SEP = " · "
_DELIVERY_MODES = {"inline", "status_card"}


def _env_home() -> str:
    for key in ("HOME", "USERPROFILE"):
        value = os.environ.get(key, "").strip()
        if value:
            return value
    home_drive = os.environ.get("HOMEDRIVE", "").strip()
    home_path = os.environ.get("HOMEPATH", "").strip()
    if home_drive and home_path:
        return home_drive + home_path
    try:
        return os.path.expanduser("~")
    except Exception:
        return ""


def _home_relative_cwd(cwd: str) -> str:
    """Return *cwd* with ``$HOME`` collapsed to ``~``.  Empty string if unset."""
    if not cwd:
        return ""
    raw = str(cwd).strip()
    if os.name == "nt" and raw.startswith("/") and not raw.startswith("//"):
        return raw
    try:
        home = _env_home()
        p = os.path.abspath(raw)
        if home:
            home_abs = os.path.abspath(home)
            try:
                if os.path.commonpath([p, home_abs]) == home_abs:
                    rel = os.path.relpath(p, home_abs)
                    if rel == ".":
                        return "~"
                    return "~/" + rel.replace("\\", "/")
            except ValueError:
                pass
        return p
    except Exception:
        return raw


def _model_short(model: Optional[str]) -> str:
    """Drop ``vendor/`` prefix for readability (``openai/gpt-5.4`` → ``gpt-5.4``)."""
    if not model:
        return ""
    return model.rsplit("/", 1)[-1]


def _provider_short(provider: Optional[str], model: Optional[str]) -> str:
    if provider:
        return provider
    if model and "/" in model:
        return model.split("/", 1)[0]
    return ""


def _labeled(label: str, value: str, style: str | None) -> str:
    if str(style or "").lower() in {"zh", "zh_detailed", "detailed_zh"}:
        return f"{label} {value}"
    return value


def _normalize_delivery(value: Any) -> str:
    delivery = str(value or "inline").strip().lower().replace("-", "_")
    return delivery if delivery in _DELIVERY_MODES else "inline"


def resolve_footer_config(
    user_config: dict[str, Any] | None,
    platform_key: str | None = None,
) -> dict[str, Any]:
    """Resolve effective runtime-footer config for *platform_key*.

    Merge order (later wins):
        1. Built-in defaults (enabled=False)
        2. ``display.runtime_footer``
        3. ``display.platforms.<platform_key>.runtime_footer``
    """
    resolved = {"enabled": False, "fields": list(_DEFAULT_FIELDS), "style": "compact", "delivery": "inline"}
    cfg = (user_config or {}).get("display") or {}

    global_cfg = cfg.get("runtime_footer")
    if isinstance(global_cfg, dict):
        if "enabled" in global_cfg:
            resolved["enabled"] = bool(global_cfg.get("enabled"))
        if isinstance(global_cfg.get("fields"), list) and global_cfg["fields"]:
            resolved["fields"] = [str(f) for f in global_cfg["fields"]]
        if global_cfg.get("style") is not None:
            resolved["style"] = str(global_cfg.get("style"))
        if global_cfg.get("delivery") is not None:
            resolved["delivery"] = _normalize_delivery(global_cfg.get("delivery"))

    if platform_key:
        platforms = cfg.get("platforms") or {}
        plat_cfg = platforms.get(platform_key)
        if isinstance(plat_cfg, dict):
            plat_footer = plat_cfg.get("runtime_footer")
            if isinstance(plat_footer, dict):
                if "enabled" in plat_footer:
                    resolved["enabled"] = bool(plat_footer.get("enabled"))
                if isinstance(plat_footer.get("fields"), list) and plat_footer["fields"]:
                    resolved["fields"] = [str(f) for f in plat_footer["fields"]]
                if plat_footer.get("style") is not None:
                    resolved["style"] = str(plat_footer.get("style"))
                if plat_footer.get("delivery") is not None:
                    resolved["delivery"] = _normalize_delivery(plat_footer.get("delivery"))

    return resolved


def format_runtime_footer(
    *,
    model: Optional[str],
    provider: Optional[str] = None,
    context_tokens: int,
    context_length: Optional[int],
    cwd: Optional[str] = None,
    fields: Iterable[str] = _DEFAULT_FIELDS,
    style: str | None = None,
) -> str:
    """Render the footer line, or return "" if no fields have data.

    Fields are skipped silently when their underlying data is missing — a
    partially-populated footer is better than a line with ``?%`` or empty slots.
    """
    parts: list[str] = []
    for field in fields:
        field = str(field).strip().lower()
        if field == "model":
            m = _model_short(model)
            if m:
                parts.append(_labeled("模型", m, style))
        elif field == "provider":
            p = _provider_short(provider, model)
            if p:
                parts.append(_labeled("服务", p, style))
        elif field in {"context", "context_pct"}:
            if context_length and context_length > 0 and context_tokens >= 0:
                pct = max(0, min(100, round((context_tokens / context_length) * 100)))
                parts.append(_labeled("上下文", f"{pct}%", style))
        elif field == "cwd":
            rel = _home_relative_cwd(cwd or os.environ.get("TERMINAL_CWD", ""))
            if rel:
                parts.append(_labeled("目录", rel, style))
        # Unknown field names are silently ignored.

    if not parts:
        return ""
    return _SEP.join(parts)


def build_footer(
    *,
    user_config: dict[str, Any] | None,
    platform_key: str | None,
    model: Optional[str],
    provider: Optional[str] = None,
    context_tokens: int,
    context_length: Optional[int],
    cwd: Optional[str] = None,
) -> dict[str, Any]:
    """Top-level entry point used by gateway/run.py.

    Returns the rendered footer plus delivery metadata. ``line`` is empty when
    disabled or when no requested fields have data.
    """
    cfg = resolve_footer_config(user_config, platform_key)
    if not cfg.get("enabled"):
        return {"delivery": cfg.get("delivery") or "inline", "line": "", "style": cfg.get("style") or "compact"}
    line = format_runtime_footer(
        model=model,
        provider=provider,
        context_tokens=context_tokens,
        context_length=context_length,
        cwd=cwd,
        fields=cfg.get("fields") or _DEFAULT_FIELDS,
        style=str(cfg.get("style") or "compact"),
    )
    return {
        "delivery": _normalize_delivery(cfg.get("delivery")),
        "line": line,
        "style": str(cfg.get("style") or "compact"),
    }


def build_footer_line(
    *,
    user_config: dict[str, Any] | None,
    platform_key: str | None,
    model: Optional[str],
    provider: Optional[str] = None,
    context_tokens: int,
    context_length: Optional[int],
    cwd: Optional[str] = None,
) -> str:
    """Backward-compatible text-only footer entry point."""
    return str(
        build_footer(
            user_config=user_config,
            platform_key=platform_key,
            model=model,
            provider=provider,
            context_tokens=context_tokens,
            context_length=context_length,
            cwd=cwd,
        ).get("line")
        or ""
    )
