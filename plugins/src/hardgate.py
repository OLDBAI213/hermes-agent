"""硬门检查器 —— pre-call / post-call 两道关卡。

pre-call：hg_002（sqlmap 参数）/ hg_003（提交）/ hg_004（admin 破坏）/ hg_005（越权目标）
post-call：hg_001（响应含他人 PII）
"""
from __future__ import annotations

import fnmatch
from pathlib import Path

try:
    import yaml as _yaml

    def _load_yaml(path: Path) -> list[dict]:
        with path.open(encoding="utf-8") as f:
            return _yaml.safe_load(f) or []

except ImportError:
    import json

    def _load_yaml(path: Path) -> list[dict]:  # type: ignore[misc]
        jp = path.with_suffix(".json")
        if jp.exists():
            return json.loads(jp.read_text(encoding="utf-8"))
        return []


_RULES_PATH = Path(__file__).parent / "hardgate.yaml"
_RULES: list[dict] | None = None


def _rules() -> list[dict]:
    global _RULES
    if _RULES is None:
        _RULES = _load_yaml(_RULES_PATH) if _RULES_PATH.exists() else []
    return _RULES


def _reload() -> None:
    global _RULES
    _RULES = None


def check_pre(
    *,
    tool: str | None = None,
    method: str | None = None,
    path: str | None = None,
    args: list[str] | None = None,
    target: str | None = None,
    scope: list[str] | None = None,
) -> dict:
    """pre-call 硬门检查：hg_002 / hg_003 / hg_004 / hg_005。

    返回 {"status": "ok"} 或 {"status": "blocked", "rule_id": ..., "action": ..., ...}
    """
    effective_scope = scope if scope else ["*"]
    args = args or []

    for rule in _rules():
        for trigger in rule.get("triggers", []):
            kind = trigger.get("kind", "")

            # hg_002: sqlmap + dangerous args
            if trigger.get("tool") == "sqlmap" and tool == "sqlmap":
                if any(a in args for a in trigger.get("args_contain", [])):
                    return _blocked(rule)

            # hg_003: platform.submit (tool 字段是列表)
            if isinstance(trigger.get("tool"), list) and tool in trigger["tool"]:
                return _blocked(rule)

            # hg_004: POST /admin/...
            t_method = trigger.get("method")
            if t_method and method and t_method.upper() == method.upper() and path:
                if any(path.startswith(p) for p in trigger.get("path_matches", [])):
                    return _blocked(rule)

            # hg_005: target not in scope
            if kind == "target_not_in_scope" and target:
                if not _in_scope(target, effective_scope):
                    return _blocked(rule)

    return {"status": "ok"}


def check_post(*, response_text: str = "") -> dict:
    """post-call 硬门检查：hg_001（响应含他人 PII）。

    P0 仅做简单字段名匹配；P3 接浏览器时再精细化。
    """
    pii_fields = ["id_card", "real_name"]
    if any(f in response_text for f in pii_fields):
        for rule in _rules():
            if rule.get("id") == "hg_001_other_user_pii":
                return _blocked(rule)
    return {"status": "ok"}


def _in_scope(target: str, scope: list[str]) -> bool:
    if "*" in scope:
        return True
    clean = target.lstrip("https://").lstrip("http://").split("/")[0].split(":")[0]
    for pattern in scope:
        if fnmatch.fnmatch(clean, pattern) or fnmatch.fnmatch(target, pattern):
            return True
        bare = pattern.lstrip("*.")
        if clean == bare or clean.endswith("." + bare):
            return True
    return False


def _blocked(rule: dict) -> dict:
    return {
        "status": "blocked",
        "rule_id": rule.get("id", "unknown"),
        "action": rule.get("action", "ask_oldbai"),
        "description": rule.get("description", ""),
        "reason": rule.get("reason", ""),
    }