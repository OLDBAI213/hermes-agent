"""Hermes-facing SRC status summary."""
from __future__ import annotations

import argparse
import json
from typing import Any

from . import health as _health
from . import interaction_map as _interaction_map
from . import platform_smoke as _platform_smoke


def _platform_login(platform_report: dict[str, Any], name: str) -> str:
    item = (platform_report.get("platforms") or {}).get(name) or {}
    assessment = item.get("assessment") or {}
    return str(assessment.get("login_state") or "unknown")


def _platform_assessment(platform_report: dict[str, Any], name: str) -> dict[str, Any]:
    item = (platform_report.get("platforms") or {}).get(name) or {}
    assessment = item.get("assessment") or {}
    return assessment if isinstance(assessment, dict) else {}


def run_status(*, write_report: bool = True) -> dict[str, Any]:
    """Return one compact truth source for Hermes before answering SRC tool status."""
    health = _health.run_health(write_report=write_report)
    platform = _platform_smoke.run_smoke(write_report=write_report)
    imap = _interaction_map.run_interaction_map(write_report=write_report)

    usable = health.get("usable_now") or {}
    browser = health.get("browser") or {}
    android = health.get("android") or {}
    display = health.get("display") or {}
    display_probe = display.get("chrome_render") or {}
    ui_probe = (android.get("ui_dump") or {})
    display_checked = display_probe.get("ok") is not None
    android_ui_checked = ui_probe.get("ok") is not None
    interaction_counts = (imap.get("interaction_map") or {}).get("counts") or {}
    report_files: dict[str, Any] = {
        "health": health.get("report_files"),
        "platform_smoke": platform.get("report_files"),
        "interaction_map": imap.get("report_files"),
    }

    vulbox_login = _platform_login(platform, "vulbox")
    butian_login = _platform_login(platform, "butian")
    vulbox_assessment = _platform_assessment(platform, "vulbox")
    cdp_reachable = bool(browser.get("any_cdp_reachable"))
    interaction_ok = bool(imap.get("success"))
    health_ok = bool(health.get("success"))
    if not write_report:
        # Artifact-dependent probes are intentionally skipped in quick mode.
        # Do not let skipped display/UI checks become false availability claims.
        health_ok = bool(
            usable.get("external_network")
            and usable.get("browser_structured_page")
            and usable.get("android_base")
            and usable.get("task_storage")
        )

    return {
        "success": bool(health_ok and platform.get("success") and interaction_ok),
        "status": "ready" if cdp_reachable and interaction_ok else "degraded",
        "hermes_use_this_first": True,
        "verification": {
            "mode": "complete_report" if write_report else "quick_no_report",
            "artifact_dependent_fields": [
                "usable_now.display",
                "usable_now.android_ui_tree",
                "current_truth.android_clickable_nodes",
            ],
            "rule": (
                "quick_no_report cannot mark display or Android UI unavailable; "
                "rerun complete status before reporting availability."
            ),
        },
        "usable_now": {
            "network": bool(usable.get("external_network")),
            "display": bool(usable.get("local_display")) if display_checked else None,
            "browser_cdp_9444": "http://localhost:9444" in (browser.get("reachable_urls") or []),
            "browser_structured_page": bool(usable.get("browser_structured_page")),
            "browser_interaction_map": interaction_ok,
            "vulbox_logged_in": vulbox_login == "likely_logged_in",
            "butian_logged_in": butian_login == "likely_logged_in",
            "android_avd": bool(usable.get("android_base")),
            "android_ui_tree": bool(usable.get("android_ui_tree")) if android_ui_checked else None,
            "task_storage": bool(usable.get("task_storage")),
        },
        "current_truth": {
            "cdp_url": browser.get("configured_cdp_url"),
            "reachable_cdp_urls": browser.get("reachable_urls") or [],
            "current_page": (imap.get("page") or {}).get("final_url"),
            "interaction_counts": interaction_counts,
            "vulbox_login_state": vulbox_login,
            "vulbox_protected_project_page_readable": vulbox_assessment.get("protected_project_page_readable"),
            "vulbox_protected_project_data_readable": vulbox_assessment.get("protected_project_data_readable"),
            "vulbox_protected_blocked_pages": vulbox_assessment.get("protected_blocked_pages") or [],
            "butian_login_state": butian_login,
            "android_devices": ((android.get("adb") or {}).get("connected_devices") or []),
            "android_clickable_nodes": ui_probe.get("clickable") if android_ui_checked else None,
        },
        "do_not_answer_from_memory": [
            "不要再凭旧结论说 9222/9333/9444 全不可用；先看 reachable_cdp_urls。",
            "不要要求老白开 9222；Hermes 当前标准端口是 9444。",
            "不要默认要求 1080/10809 代理；先看 network 结果。",
            "不要用 quick_no_report 里的 display=null 或 android_clickable_nodes=null 判定不可用。",
            "不要把没有生成报告导致的 0 个 UI 节点说成模拟器不可用。",
            "不要把截图当主判断；优先用 browser_interaction_map 和 android_ui_tree。",
            "不要把漏洞盒子 projects/list 或 projectHall/myProject 可读，说成 dashboard/myvuln/project 内部项目数据可读。",
            "如果 protected_project_page_readable/data_readable 为 false/null，只能说工具可用但内部任务页未验证可读。",
        ],
        "hard_gate": "只读状态检查；不点击、不输入、不提交、不绕过验证码/风控。",
        "report_files": report_files,
    }


def compact_report(report: dict[str, Any]) -> dict[str, Any]:
    return {
        "success": report.get("success"),
        "status": report.get("status"),
        "verification": report.get("verification"),
        "usable_now": report.get("usable_now"),
        "current_truth": report.get("current_truth"),
        "do_not_answer_from_memory": report.get("do_not_answer_from_memory"),
        "report_files": report.get("report_files"),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Summarize current SRC Suite status for Hermes.")
    parser.add_argument("--write-report", action="store_true", help="write underlying health/smoke/map reports; this is the default")
    parser.add_argument("--no-report", action="store_true", help="quick mode; artifact-dependent display/android fields are unknown")
    parser.add_argument("--full", action="store_true", help="print full underlying summary")
    args = parser.parse_args(argv)
    report = run_status(write_report=not args.no_report)
    print(json.dumps(report if args.full else compact_report(report), ensure_ascii=False, indent=2))
    return 0 if report["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
