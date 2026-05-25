from hermes_cli.config import DEFAULT_CONFIG


def test_default_config_declares_tui_framework_defaults():
    display = DEFAULT_CONFIG["display"]

    assert display["tui_status_indicator"] == "kaomoji"
    assert display["tui_statusbar"] == "top"
    assert display["tui_modules"] == {
        "activity_scan": True,
        "character_panel": False,
        "monitor_panel": False,
        "status_meter": True,
        "task_panel": True,
    }
