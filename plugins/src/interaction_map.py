"""Generic machine-readable browser interaction map."""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .journal import runs_root
from .platform_smoke import CdpPage, _read_cdp_url, build_interaction_map


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def _clean(value: Any, *, limit: int = 160) -> str:
    text = " ".join(str(value or "").split())
    return text[:limit]


def run_interaction_map(
    *,
    url: str | None = None,
    cdp_url: str | None = None,
    write_report: bool = False,
) -> dict[str, Any]:
    cdp = cdp_url or _read_cdp_url(Path(os.environ.get("HERMES_HOME", "E:/AI/hermes")))
    page = CdpPage(cdp).snapshot(url)
    imap = build_interaction_map(page, limit=220) if page.get("ok") else {
        "counts": {
            "controls": 0,
            "inputs": 0,
            "buttons": 0,
            "links": 0,
            "icon_candidates": 0,
            "top_right_candidates": 0,
        },
        "inputs": [],
        "buttons": [],
        "links": [],
        "icon_candidates": [],
        "top_right_candidates": [],
    }
    report: dict[str, Any] = {
        "success": bool(page.get("ok")),
        "checked_at": _now(),
        "cdp_url": cdp,
        "page": {
            "ok": page.get("ok"),
            "requested_url": page.get("requested_url"),
            "final_url": page.get("final_url"),
            "title": page.get("title"),
            "ready_state": page.get("ready_state"),
            "text_length": page.get("text_length", 0),
            "error": page.get("error"),
        },
        "interaction_map": imap,
        "hard_gate": "只读交互地图；不点击、不输入、不提交。",
    }
    if write_report:
        report["report_files"] = _write_report(report)
    return report


def _write_report(report: dict[str, Any]) -> dict[str, str]:
    out_dir = runs_root() / f"interaction_map_{_stamp()}"
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "interaction-map.json"
    md_path = out_dir / "interaction-map.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(_render_markdown(report), encoding="utf-8")
    return {"dir": str(out_dir), "json": str(json_path), "markdown": str(md_path)}


def _action_line(action: dict[str, Any]) -> str:
    center = action.get("center") or {}
    rect = action.get("rect") or {}
    return (
        f"- {_clean(action.get('label'), limit=80)} "
        f"[{action.get('tag')}/{action.get('type') or action.get('role')}] "
        f"@ ({center.get('x')},{center.get('y')}) "
        f"{rect.get('width')}x{rect.get('height')}"
    )


def _render_markdown(report: dict[str, Any]) -> str:
    page = report["page"]
    imap = report["interaction_map"]
    counts = imap.get("counts") or {}
    lines = [
        "# Browser Interaction Map",
        "",
        f"- 时间: {report['checked_at']}",
        f"- CDP: {report['cdp_url']}",
        f"- URL: {page.get('final_url') or page.get('requested_url')}",
        f"- 标题: {_clean(page.get('title'), limit=120)}",
        f"- 状态: {'成功' if page.get('ok') else '失败'}",
        f"- 文本长度: {page.get('text_length', 0)}",
        f"- 控件/输入/按钮/链接/图标候选/右上角候选: {counts.get('controls', 0)}/{counts.get('inputs', 0)}/{counts.get('buttons', 0)}/{counts.get('links', 0)}/{counts.get('icon_candidates', 0)}/{counts.get('top_right_candidates', 0)}",
        f"- 区域分布: {json.dumps(imap.get('by_region') or {}, ensure_ascii=False)}",
        f"- 硬门: {report['hard_gate']}",
        "",
    ]
    for group, title in [
        ("inputs", "输入框"),
        ("buttons", "按钮"),
        ("links", "链接"),
        ("top_right_candidates", "右上角候选"),
        ("icon_candidates", "无文字/图标候选"),
    ]:
        actions = imap.get(group) or []
        lines += [f"## {title}", ""]
        if not actions:
            lines.append("- 无")
        for action in actions[:60]:
            lines.append(_action_line(action))
            if action.get("selector"):
                lines.append(f"  selector: `{action['selector']}`")
        lines.append("")
    return "\n".join(lines) + "\n"


def compact_report(report: dict[str, Any]) -> dict[str, Any]:
    imap = report.get("interaction_map") or {}
    return {
        "success": report.get("success"),
        "page": report.get("page"),
        "counts": imap.get("counts"),
        "by_region": imap.get("by_region"),
        "top_right_candidates": (imap.get("top_right_candidates") or [])[:10],
        "top_icon_candidates": (imap.get("icon_candidates") or [])[:10],
        "report_files": report.get("report_files"),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build a machine-readable browser interaction map.")
    parser.add_argument("--url", help="optional URL to navigate before scanning; omit to scan current page")
    parser.add_argument("--cdp-url", help="CDP url, default reads Hermes config")
    parser.add_argument("--write-report", action="store_true", help="write interaction-map.json/md under runs/src")
    parser.add_argument("--full", action="store_true", help="print full report instead of compact summary")
    args = parser.parse_args(argv)
    report = run_interaction_map(url=args.url, cdp_url=args.cdp_url, write_report=args.write_report)
    print(json.dumps(report if args.full else compact_report(report), ensure_ascii=False, indent=2))
    return 0 if report["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
