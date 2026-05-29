from __future__ import annotations

from pathlib import Path

from plugins.src import health


def test_run_health_writes_report(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path))
    monkeypatch.setattr(
        health,
        "_security_tools_report",
        lambda: {
            "root": {"path": "tools", "exists": True, "is_dir": True},
            "tools": {
                "subfinder": {"available": True, "path": "subfinder"},
                "httpx": {"available": True, "path": "httpx"},
                "naabu": {"available": False, "path": None},
                "katana": {"available": True, "path": "katana"},
                "nuclei": {"available": True, "path": "nuclei"},
                "ffuf": {"available": True, "path": "ffuf"},
            },
        },
    )
    monkeypatch.setattr(
        health,
        "_browser_report",
        lambda _home: {
            "configured_cdp_url": "http://localhost:9444",
            "url_file_cdp_url": "http://localhost:9444",
            "recommended_cdp_url": "http://localhost:9444",
            "cdp_urls_match_recommendation": True,
            "any_cdp_reachable": True,
            "reachable_urls": ["http://localhost:9444"],
            "probes": [],
            "structure": {
                "ok": True,
                "target_url": "about:blank",
                "title": "",
                "ready_state": "complete",
                "text_length": 0,
                "links": 0,
                "forms": 0,
                "inputs": 0,
                "buttons": 0,
                "clickable": 0,
                "accessibility_nodes": 3,
                "error": None,
            },
            "chrome": {"path": "chrome", "exists": True, "is_dir": False},
            "edge": {"path": "edge", "exists": False, "is_dir": False},
            "profiles": {"recommended_src_main": {"exists": True}},
        },
    )
    monkeypatch.setattr(
        health,
        "_network_report",
        lambda: {
            "dns_ok": True,
            "https_ok": True,
            "dns": {},
            "https": {},
            "proxy_env": {},
            "no_proxy_has_localhost": True,
        },
    )
    monkeypatch.setattr(
        health,
        "_display_report",
        lambda _dir=None: {
            "screen": {"available": True, "width": 1920, "height": 1080, "remote_session": False, "error": None},
            "chrome_render": {"ok": True, "artifact": "render.png", "bytes": 1234, "error": None},
            "display_ok": True,
        },
    )
    monkeypatch.setattr(
        health,
        "_android_report",
        lambda _dir=None: {
            "sdk_root": {"path": "sdk", "exists": True, "is_dir": True},
            "adb": {"path": "adb", "exists": True, "is_dir": False, "version": "adb", "devices_stdout": "", "connected_devices": ["emulator-5554"]},
            "emulator": {"path": "emulator", "exists": True, "is_dir": False, "avds": ["root_avd"], "root_avd_present": True},
            "screen": {"ok": True, "artifact": "android.png", "bytes": 1234, "error": None},
            "ui_dump": {"ok": True, "xml": "window.xml", "json": "window-summary.json", "nodes": 5, "clickable": 2, "error": None},
            "java": {"path": "java", "exists": True, "is_dir": False},
        },
    )

    report = health.run_health(write_report=True)

    assert report["status"] == "ready"
    assert report["usable_now"] == {
        "bulk_collection": True,
        "external_network": True,
        "local_display": True,
        "logged_in_browser": True,
        "browser_structured_page": True,
        "browser_interaction_map": True,
        "android_base": True,
        "android_display": True,
        "android_ui_tree": True,
        "task_storage": True,
    }
    assert report["capabilities"]["browser_logged_in_cdp"]["live_callable_by_hermes"] is True
    assert report["capabilities"]["browser_logged_in_cdp"]["good_to_use"] is True
    assert report["capabilities"]["browser_structured_page"]["good_to_use"] is True
    assert report["capabilities"]["browser_interaction_map"]["good_to_use"] is True
    assert report["capabilities"]["android_screen"]["good_to_use"] is True
    assert report["capabilities"]["android_ui_tree"]["good_to_use"] is True
    assert Path(report["report_files"]["json"]).exists()
    assert Path(report["report_files"]["markdown"]).exists()


def test_run_health_reports_degraded_without_browser(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path))
    monkeypatch.setattr(
        health,
        "_security_tools_report",
        lambda: {
            "root": {"path": "tools", "exists": True, "is_dir": True},
            "tools": {
                "subfinder": {"available": True, "path": "subfinder"},
                "httpx": {"available": True, "path": "httpx"},
                "naabu": {"available": True, "path": "naabu"},
                "katana": {"available": True, "path": "katana"},
                "nuclei": {"available": True, "path": "nuclei"},
                "ffuf": {"available": True, "path": "ffuf"},
            },
        },
    )
    monkeypatch.setattr(
        health,
        "_browser_report",
        lambda _home: {
            "configured_cdp_url": "http://localhost:9333",
            "url_file_cdp_url": "http://localhost:9333",
            "recommended_cdp_url": "http://localhost:9444",
            "cdp_urls_match_recommendation": False,
            "any_cdp_reachable": False,
            "reachable_urls": [],
            "probes": [],
            "structure": {
                "ok": False,
                "target_url": None,
                "title": None,
                "ready_state": None,
                "text_length": 0,
                "links": 0,
                "forms": 0,
                "inputs": 0,
                "buttons": 0,
                "clickable": 0,
                "accessibility_nodes": 0,
                "error": "CDP connection refused",
            },
            "chrome": {"path": "chrome", "exists": True, "is_dir": False},
            "edge": {"path": "edge", "exists": False, "is_dir": False},
            "profiles": {"recommended_src_main": {"exists": False}},
        },
    )
    monkeypatch.setattr(
        health,
        "_network_report",
        lambda: {
            "dns_ok": True,
            "https_ok": True,
            "dns": {},
            "https": {},
            "proxy_env": {},
            "no_proxy_has_localhost": True,
        },
    )
    monkeypatch.setattr(
        health,
        "_display_report",
        lambda _dir=None: {
            "screen": {"available": True, "width": 1920, "height": 1080, "remote_session": False, "error": None},
            "chrome_render": {"ok": True, "artifact": "render.png", "bytes": 1234, "error": None},
            "display_ok": True,
        },
    )
    monkeypatch.setattr(
        health,
        "_android_report",
        lambda _dir=None: {
            "sdk_root": {"path": "sdk", "exists": True, "is_dir": True},
            "adb": {"path": "adb", "exists": True, "is_dir": False, "version": "adb", "devices_stdout": "", "connected_devices": []},
            "emulator": {"path": "emulator", "exists": True, "is_dir": False, "avds": ["root_avd"], "root_avd_present": True},
            "screen": {"ok": False, "artifact": None, "bytes": 0, "error": "no connected android device"},
            "ui_dump": {"ok": False, "xml": None, "json": None, "nodes": 0, "clickable": 0, "error": "no connected android device"},
            "java": {"path": "java", "exists": True, "is_dir": False},
        },
    )

    report = health.run_health()

    assert report["status"] == "degraded"
    assert report["usable_now"]["logged_in_browser"] is False
    assert report["usable_now"]["browser_interaction_map"] is False
    assert report["browser"]["cdp_urls_match_recommendation"] is False
    assert report["capabilities"]["browser_logged_in_cdp"]["call_path_exists"] is True
    assert report["capabilities"]["browser_logged_in_cdp"]["live_callable_by_hermes"] is False
    assert report["capabilities"]["browser_structured_page"]["live_callable_by_hermes"] is False
    assert report["capabilities"]["browser_interaction_map"]["live_callable_by_hermes"] is False
    assert "CDP 没连上" in report["capabilities"]["browser_logged_in_cdp"]["blocker"]
