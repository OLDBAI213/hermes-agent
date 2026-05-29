from __future__ import annotations

from pathlib import Path

from plugins.src import platform_smoke


def _page(*, url: str, text: str, kind: str = "public_projects") -> dict:
    return {
        "ok": True,
        "kind": kind,
        "requested_url": url,
        "final_url": url,
        "title": "page",
        "ready_state": "complete",
        "text_length": len(text),
        "text_sample": text,
        "counters": {"links": 3, "forms": 0, "inputs": 0, "buttons": 1, "clickable": 4},
        "links": [],
        "controls": [],
        "top_right_candidates": [],
        "forms": [],
        "accessibility_nodes": 3,
        "error": None,
    }


def test_build_interaction_map_includes_unlabeled_top_right_candidate():
    page = _page(url="https://example.com/login", text="登录")
    page["controls"] = [
        {
            "tag": "div",
            "text": "",
            "href": "",
            "id": "",
            "className": "qr-switch-corner",
            "role": "button",
            "type": "",
            "selector": "div.qr-switch-corner",
            "rect": {"x": 500, "y": 88, "width": 34, "height": 34},
            "center": {"x": 517, "y": 105},
            "region": "top-right",
            "visible": True,
            "unlabeled": True,
        }
    ]

    imap = platform_smoke.build_interaction_map(page)

    assert imap["counts"]["icon_candidates"] == 1
    assert imap["counts"]["top_right_candidates"] == 1
    assert imap["icon_candidates"][0]["selector"] == "div.qr-switch-corner"
    assert imap["icon_candidates"][0]["center"] == {"x": 517, "y": 105}


def test_build_interaction_map_includes_visual_top_right_candidate():
    page = _page(url="https://example.com/login", text="登录")
    page["top_right_candidates"] = [
        {
            "tag": "span",
            "text": "",
            "className": "login-type-switch",
            "selector": "span.login-type-switch",
            "rect": {"x": 700, "y": 18, "width": 42, "height": 42},
            "center": {"x": 721, "y": 39},
            "region": "top-right",
            "visible": True,
            "unlabeled": True,
        }
    ]

    imap = platform_smoke.build_interaction_map(page)

    assert imap["counts"]["top_right_candidates"] == 1
    assert imap["top_right_candidates"][0]["selector"] == "span.login-type-switch"


def test_cdp_page_retries_transient_windows_socket_error(monkeypatch):
    client = platform_smoke.CdpPage("http://localhost:9444")
    attempts = []

    class FakeConnection:
        pass

    def fake_connect(_url, open_timeout):
        attempts.append(open_timeout)
        if len(attempts) == 1:
            raise OSError("[WinError 10048] address already in use")
        return FakeConnection()

    monkeypatch.setattr(client, "_page_ws_url", lambda: "ws://127.0.0.1/devtools/page/1")
    monkeypatch.setattr(platform_smoke, "connect", fake_connect)

    assert isinstance(client._connect_page_ws(), FakeConnection)
    assert len(attempts) == 2


def test_assess_platform_distinguishes_logged_in_from_login_prompt():
    logged_in = platform_smoke.assess_platform(
        "vulbox",
        [
            _page(url="https://user.vulbox.com/projectHall/myProject", kind="account_projects", text="个人中心 我的项目 漏洞提交 项目大厅 赏金"),
        ],
    )
    login_required = platform_smoke.assess_platform(
        "vulbox",
        [
            _page(url="https://www.vulbox.com/account/login", kind="account_projects", text="登录 注册 项目大厅"),
        ],
    )

    assert logged_in["login_state"] == "likely_logged_in"
    assert logged_in["project_entry_readable"] is True
    assert login_required["login_state"] == "login_required_or_unknown"


def test_assess_platform_does_not_treat_public_project_page_as_protected_data():
    result = platform_smoke.assess_platform(
        "vulbox",
        [
            _page(url="https://www.vulbox.com/projects/list", kind="public_projects", text="项目大厅 赏金 个人中心 我的项目"),
            _page(url="https://user.vulbox.com/projectHall/myProject", kind="account_projects", text="个人中心 我的项目 漏洞提交 项目大厅"),
            _page(url="https://user.vulbox.com/dashboard/myvuln/project", kind="protected_my_vuln_projects", text=""),
        ],
    )

    assert result["login_state"] == "likely_logged_in"
    assert result["project_entry_readable"] is True
    assert result["protected_project_page_readable"] is False
    assert result["protected_project_data_readable"] is False
    assert result["protected_blocked_pages"][0]["kind"] == "protected_my_vuln_projects"


def test_assess_platform_marks_protected_project_data_readable_only_with_internal_signals():
    result = platform_smoke.assess_platform(
        "vulbox",
        [
            _page(url="https://user.vulbox.com/dashboard/myvuln/project", kind="protected_my_vuln_projects", text="我的漏洞 漏洞编号 项目名称 提交时间 待审核"),
        ],
    )

    assert result["protected_project_page_readable"] is True
    assert result["protected_project_data_readable"] is True
    assert "漏洞编号" in result["protected_project_signals"]


def test_render_markdown_exposes_protected_project_data_result():
    report = {
        "checked_at": "2026-05-27T00:00:00+00:00",
        "status": "ready",
        "cdp_url": "http://localhost:9444",
        "hard_gate": "readonly",
        "platforms": {
            "vulbox": {
                "assessment": {
                    "name": "漏洞盒子",
                    "structure_readable": True,
                    "project_entry_readable": True,
                    "protected_project_page_readable": True,
                    "protected_project_data_readable": False,
                    "protected_project_signals": [],
                    "login_state": "likely_logged_in",
                    "login_prompts": [],
                    "project_signals": ["项目大厅"],
                },
                "pages": [],
                "interaction_maps": [],
            }
        },
    }

    text = platform_smoke._render_markdown(report)

    assert "内部任务数据可读" in text
    assert "不能说已经找到项目数据" in text


def test_assess_platform_uses_machine_readable_login_container():
    page = _page(url="https://www.vulbox.com/projects/list", text="项目大厅 赏金", kind="account_projects")
    page["controls"] = [
        {
            "text": "",
            "className": "logined-wrapper",
            "selector": "div.header-right-wrapper > div.logined-wrapper > span.uname",
        }
    ]

    result = platform_smoke.assess_platform("vulbox", [page])

    assert result["login_state"] == "likely_logged_in"
    assert "logined-wrapper" in result["account_logged_in_signals"]


def test_run_smoke_writes_report(monkeypatch, tmp_path):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path))
    (tmp_path / "config.yaml").write_text("browser:\n  cdp_url: http://localhost:9444\n", encoding="utf-8")

    class FakeCdpPage:
        def __init__(self, _url):
            pass

        def snapshot(self, url):
            return _page(url=url, text="项目大厅 赏金 个人中心 我的项目 漏洞提交")

    monkeypatch.setattr(platform_smoke, "CdpPage", FakeCdpPage)

    report = platform_smoke.run_smoke(platforms=["vulbox"], write_report=True)

    assert report["status"] == "ready"
    assert report["platforms"]["vulbox"]["assessment"]["login_state"] == "likely_logged_in"
    assert Path(report["report_files"]["json"]).exists()
    assert Path(report["report_files"]["markdown"]).exists()
