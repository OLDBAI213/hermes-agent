from __future__ import annotations

from pathlib import Path
import json

from plugins.src.facade import SrcSuite
from plugins.src import interaction_map
from plugins.src import status as src_status


def test_run_interaction_map_writes_report(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path))

    class FakeCdpPage:
        def __init__(self, _url):
            pass

        def snapshot(self, _url):
            return {
                "ok": True,
                "requested_url": "<current>",
                "final_url": "https://example.com/login",
                "title": "login",
                "ready_state": "complete",
                "text_length": 10,
                "controls": [
                    {
                        "tag": "button",
                        "text": "登录",
                        "type": "button",
                        "selector": "button.login",
                        "rect": {"x": 10, "y": 20, "width": 60, "height": 30},
                        "center": {"x": 40, "y": 35},
                        "region": "middle",
                        "visible": True,
                    }
                ],
                "top_right_candidates": [],
            }

    monkeypatch.setattr(interaction_map, "CdpPage", FakeCdpPage)

    report = interaction_map.run_interaction_map(write_report=True)

    assert report["success"] is True
    assert report["interaction_map"]["counts"]["buttons"] == 1
    assert Path(report["report_files"]["json"]).exists()


def test_srcsuite_browse_map_writes_task_journal(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path))

    def fake_run_interaction_map(*, url=None, cdp_url=None, write_report=False):
        return {
            "success": True,
            "page": {"final_url": url or "https://example.com"},
            "interaction_map": {
                "counts": {
                    "controls": 1,
                    "inputs": 0,
                    "buttons": 1,
                    "links": 0,
                    "icon_candidates": 0,
                    "top_right_candidates": 0,
                }
            },
            "report_files": {"json": str(tmp_path / "interaction-map.json")},
        }

    monkeypatch.setattr(interaction_map, "run_interaction_map", fake_run_interaction_map)

    suite = SrcSuite()
    created = suite.task.new(platform="crosscheck", scope=["https://example.com"])
    result = suite.browse.map(write_report=True)
    journal = Path(created["task_dir"]) / "journal.jsonl"
    events = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines()]

    assert result["success"] is True
    assert events[-1]["tool"] == "browse.map"
    assert events[-1]["status"] == "ok"
    assert events[-1]["output"]["counts"]["controls"] == 1


def test_srcsuite_status_summarizes_current_truth(monkeypatch):
    monkeypatch.setattr(
        src_status._health,
        "run_health",
        lambda write_report=False: {
            "success": True,
            "usable_now": {
                "external_network": True,
                "local_display": True,
                "browser_structured_page": True,
                "android_base": True,
                "android_ui_tree": True,
                "task_storage": True,
            },
            "browser": {
                "configured_cdp_url": "http://localhost:9444",
                "reachable_urls": ["http://localhost:9444"],
                "any_cdp_reachable": True,
            },
            "android": {
                "adb": {"connected_devices": ["emulator-5554"]},
                "ui_dump": {"clickable": 22},
            },
        },
    )
    monkeypatch.setattr(
        src_status._platform_smoke,
        "run_smoke",
        lambda write_report=False: {
            "success": True,
            "platforms": {
                "vulbox": {"assessment": {"login_state": "likely_logged_in"}},
                "butian": {"assessment": {"login_state": "login_required_or_unknown"}},
            },
        },
    )
    monkeypatch.setattr(
        src_status._interaction_map,
        "run_interaction_map",
        lambda write_report=False: {
            "success": True,
            "page": {"final_url": "https://www.vulbox.com/projects/list"},
            "interaction_map": {"counts": {"controls": 3, "top_right_candidates": 1}},
        },
    )

    report = SrcSuite().status()

    assert report["status"] == "ready"
    assert report["usable_now"]["browser_cdp_9444"] is True
    assert report["usable_now"]["vulbox_logged_in"] is True
    assert report["usable_now"]["butian_logged_in"] is False


def test_srcsuite_status_quick_mode_does_not_make_artifact_false_claims(monkeypatch):
    monkeypatch.setattr(
        src_status._health,
        "run_health",
        lambda write_report=False: {
            "success": False,
            "usable_now": {
                "external_network": True,
                "local_display": False,
                "browser_structured_page": True,
                "android_base": True,
                "android_ui_tree": False,
                "task_storage": True,
            },
            "display": {"chrome_render": {"ok": None, "error": "not run without report directory"}},
            "browser": {
                "configured_cdp_url": "http://localhost:9444",
                "reachable_urls": ["http://localhost:9444"],
                "any_cdp_reachable": True,
            },
            "android": {
                "adb": {"connected_devices": ["emulator-5554"]},
                "ui_dump": {"ok": None, "clickable": 0, "error": "not run without report directory"},
            },
        },
    )
    monkeypatch.setattr(
        src_status._platform_smoke,
        "run_smoke",
        lambda write_report=False: {
            "success": True,
            "platforms": {
                "vulbox": {"assessment": {"login_state": "likely_logged_in"}},
                "butian": {"assessment": {"login_state": "login_required_or_unknown"}},
            },
        },
    )
    monkeypatch.setattr(
        src_status._interaction_map,
        "run_interaction_map",
        lambda write_report=False: {
            "success": True,
            "page": {"final_url": "https://www.butian.net/"},
            "interaction_map": {"counts": {"controls": 58, "top_right_candidates": 8}},
        },
    )

    report = src_status.run_status(write_report=False)

    assert report["status"] == "ready"
    assert report["verification"]["mode"] == "quick_no_report"
    assert report["usable_now"]["display"] is None
    assert report["usable_now"]["android_ui_tree"] is None
    assert report["current_truth"]["android_clickable_nodes"] is None
    assert any("quick_no_report" in item for item in report["do_not_answer_from_memory"])
