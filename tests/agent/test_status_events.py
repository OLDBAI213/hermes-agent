from types import SimpleNamespace

from agent.status_events import emit_tui_model_status


def test_emit_tui_model_status_only_for_tui():
    events = []
    agent = SimpleNamespace(
        platform="feishu",
        status_callback=lambda kind, text: events.append((kind, text)),
    )

    assert emit_tui_model_status(agent, "等待响应 #20…") is False
    assert events == []

    agent.platform = "tui"

    assert emit_tui_model_status(agent, "等待响应 #20…") is True
    assert events == [("model", "等待响应 #20…")]


def test_emit_tui_model_status_ignores_missing_callback():
    agent = SimpleNamespace(platform="tui", status_callback=None)

    assert emit_tui_model_status(agent, "等待响应 #20…") is False


def test_emit_tui_model_status_swallows_callback_errors():
    def bad_callback(kind, text):
        raise RuntimeError("boom")

    agent = SimpleNamespace(platform="tui", status_callback=bad_callback)

    assert emit_tui_model_status(agent, "等待响应 #20…") is False
