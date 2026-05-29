"""SRC Suite workflow 运行器 —— 读 YAML DAG，顺序执行 facade 动词。

MVP 版：拓扑排序后顺序执行（无并发），步骤输出通过 ctx 传递给后续步骤。
模板格式：{{target}} | {{steps.<id>.<field>}}
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any, TYPE_CHECKING

try:
    import yaml as _yaml

    def _load_yaml(path: Path) -> dict:
        with path.open(encoding="utf-8") as f:
            return _yaml.safe_load(f) or {}

except ImportError:
    import json

    def _load_yaml(path: Path) -> dict:  # type: ignore[misc]
        return json.loads(path.read_text(encoding="utf-8"))

if TYPE_CHECKING:
    from .facade import SrcSuite

_FLOWS_DIR = Path(__file__).parent / "workflows"


def _resolve_param(value: Any, ctx: dict) -> Any:
    """模板变量解析；list/dict 引用直接返回原值（不转 str）。"""
    if not isinstance(value, str):
        return value
    # 纯模板引用 {{steps.X.Y}} → 直接返回原始值（可能是 list）
    if re.fullmatch(r"\{\{.+?\}\}", value.strip()):
        expr = value.strip()[2:-2].strip()
        if expr.startswith("steps."):
            parts = expr.split(".", 2)
            if len(parts) == 3:
                step_out = ctx.get("steps", {}).get(parts[1], {})
                return step_out.get(parts[2])
        if expr == "target":
            return ctx.get("target")
    # 字符串插值
    def _repl(m: re.Match) -> str:
        expr = m.group(1).strip()
        if expr == "target":
            return str(ctx.get("target", ""))
        if expr.startswith("steps."):
            parts = expr.split(".", 2)
            if len(parts) == 3:
                step_out = ctx.get("steps", {}).get(parts[1], {})
                val = step_out.get(parts[2], "")
                return str(val) if not isinstance(val, (list, dict)) else repr(val)
        return m.group(0)
    return re.sub(r"\{\{(.+?)\}\}", _repl, value)


def _topo_sort(steps: list[dict]) -> list[dict]:
    order: list[dict] = []
    done: set[str] = set()
    step_map = {s["id"]: s for s in steps}

    def _visit(step: dict) -> None:
        if step["id"] in done:
            return
        for dep in step.get("depends_on", []):
            if dep in step_map:
                _visit(step_map[dep])
        order.append(step)
        done.add(step["id"])

    for s in steps:
        _visit(s)
    return order


def run_flow(suite: "SrcSuite", flow_name: str, *, target: str, **extra: Any) -> dict:
    """执行指定 workflow DAG。

    返回 {"success": bool, "flow": ..., "steps": {id: result}, "summary": str}
    """
    flow_path = _FLOWS_DIR / f"{flow_name}.yaml"
    if not flow_path.exists():
        return {
            "success": False,
            "flow": flow_name,
            "steps": {},
            "summary": f"workflow 文件不存在：{flow_path}",
        }

    flow_def = _load_yaml(flow_path)
    ordered = _topo_sort(flow_def.get("steps", []))

    ctx: dict[str, Any] = {"target": target, "steps": {}, **extra}
    results: dict[str, dict] = {}
    j = suite.require_journal()

    j.write(
        phase="init",
        kind="decision",
        target=target,
        decision=f"启动 workflow: {flow_name}",
        input={"flow": flow_name, "target": target},
        next=[s["id"] for s in ordered],
    )

    for step in ordered:
        step_id = step["id"]
        verb_str = step["verb"]
        on_fail = step.get("on_fail", "skip")

        resolved = {k: _resolve_param(v, ctx) for k, v in step.get("params", {}).items()}

        ns_name, _, method_name = verb_str.partition(".")
        ns = getattr(suite, ns_name, None)
        method = getattr(ns, method_name, None) if ns else None

        if method is None:
            result: dict = {"success": False, "error": f"未知动词 {verb_str}"}
        else:
            try:
                result = method(**resolved)
            except Exception as exc:
                result = {"success": False, "error": str(exc)}

        results[step_id] = result
        ctx["steps"][step_id] = result

        if not result.get("success") and on_fail == "stop":
            j.write(
                phase="init", kind="decision", target=target,
                decision=f"workflow 中止：步骤 {step_id} 失败（on_fail=stop）",
                status="fail",
                err=result.get("error") or result.get("err"),
            )
            return {
                "success": False,
                "flow": flow_name,
                "steps": results,
                "summary": f"workflow {flow_name} 在步骤 {step_id} 中止",
            }

    hints = [s["next_hint"] for s in ordered if s.get("next_hint")]
    j.write(
        phase="init", kind="decision", target=target,
        decision=f"workflow {flow_name} 完成",
        status="ok",
        next=hints,
    )

    return {
        "success": True,
        "flow": flow_name,
        "steps": results,
        "summary": f"workflow {flow_name} 完成（{len(results)} 步）",
    }


def list_flows() -> list[str]:
    if not _FLOWS_DIR.exists():
        return []
    return [p.stem for p in sorted(_FLOWS_DIR.glob("*.yaml"))]