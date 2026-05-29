import types
from pathlib import Path

from tui_gateway import server


ROOT = Path(__file__).resolve().parents[1]


def test_tui_session_info_surfaces_display_health(monkeypatch):
    cfg = {
        "display": {
            "sections": {"thinking": "hidden", "tools": "hidden"},
            "show_reasoning": False,
        }
    }

    monkeypatch.setattr(server, "_load_cfg", lambda: cfg)
    monkeypatch.setattr(server, "_load_show_reasoning", lambda: False)
    monkeypatch.setattr(server, "_get_usage", lambda _agent: {})
    monkeypatch.setattr(server, "_current_profile_name", lambda: "default")

    info = server._session_info(types.SimpleNamespace(model="mimo-v2.5", service_tier="", tools=[]))

    assert info["show_reasoning"] is False
    assert "TUI 思考显示当前关闭" in info["config_warning"]
    assert "思考面板会被隐藏" in info["config_warning"]
    assert "工具调用面板会被隐藏" in info["config_warning"]


def test_tui_config_health_warning_is_chinese_and_actionable():
    warning = server._probe_config_health(
        {
            "agent": None,
            "display": {
                "personality": "warm",
                "sections": {"thinking": "hidden", "tools": "hidden"},
                "show_reasoning": False,
            },
        }
    )

    assert "config.yaml 存在空配置段" in warning
    assert "运行 `/reasoning show`" in warning
    assert "人格叠加会被跳过" in warning
    assert "empty section" not in warning
    assert "personality overlay will be skipped" not in warning


def test_conpty_smoke_has_real_slash_submission_guard():
    script = (ROOT / "scripts" / "tui_smoke_winpty.py").read_text(encoding="utf-8")

    assert "--slash-command" in script
    assert "--before-input-delay" in script
    assert 'rstrip() + " "' in script
    assert "completion" in script.lower()
