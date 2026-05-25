"""Gateway command help rendering tests."""

import pytest

from gateway.config import Platform
from gateway.platforms.base import MessageEvent
from gateway.session import SessionSource


def _make_event(text: str, platform: Platform) -> MessageEvent:
    return MessageEvent(
        text=text,
        source=SessionSource(
            platform=platform,
            chat_id="chat-1",
            user_id="user-1",
            user_name="tester",
            chat_type="dm",
        ),
    )


def _make_runner():
    from gateway.run import GatewayRunner

    return object.__new__(GatewayRunner)


@pytest.mark.asyncio
async def test_help_sanitizes_slash_command_mentions_for_telegram(monkeypatch):
    """Telegram help output must not expose invalid uppercase/hyphenated slashes."""
    monkeypatch.setattr(
        "agent.skill_commands.get_skill_commands",
        lambda: {
            "/Linear": {"description": "Open Linear"},
            "/Custom-Thing": {"description": "Run a custom thing"},
        },
    )

    result = await _make_runner()._handle_help_command(
        _make_event("/help", Platform.TELEGRAM)
    )

    assert "`/linear`" in result
    assert "`/custom_thing`" in result
    assert "`/Linear`" not in result
    assert "`/Custom-Thing`" not in result


@pytest.mark.asyncio
async def test_commands_sanitizes_slash_command_mentions_for_telegram(monkeypatch):
    """Paginated Telegram /commands output uses Telegram-valid slash mentions."""
    monkeypatch.setattr(
        "agent.skill_commands.get_skill_commands",
        lambda: {"/Linear": {"description": "Open Linear"}},
    )

    result = await _make_runner()._handle_commands_command(
        _make_event("/commands 999", Platform.TELEGRAM)
    )

    assert "`/linear`" in result
    assert "`/Linear`" not in result


@pytest.mark.asyncio
async def test_help_keeps_non_telegram_slash_command_mentions_unchanged(monkeypatch):
    """Only Telegram needs slash mentions rewritten to Telegram command names."""
    monkeypatch.setattr(
        "agent.skill_commands.get_skill_commands",
        lambda: {"/Linear": {"description": "Open Linear"}},
    )

    result = await _make_runner()._handle_help_command(
        _make_event("/help", Platform.DISCORD)
    )

    assert "`/Linear`" in result


@pytest.mark.asyncio
async def test_feishu_zh_help_localizes_builtin_commands(monkeypatch):
    """Feishu Chinese mode should not expose the English built-in command registry."""
    import gateway.run as gateway_run

    monkeypatch.setattr(
        gateway_run,
        "_load_gateway_config",
        lambda: {"display": {"language": "zh", "gateway_locale": "zh"}},
    )

    result = await _make_runner()._handle_help_command(
        _make_event("/help", Platform.FEISHU)
    )

    assert "**会话：**" in result
    assert "`/status` -- 显示当前会话状态" in result
    assert "Show session info" not in result


@pytest.mark.asyncio
async def test_feishu_zh_commands_localizes_builtin_commands(monkeypatch):
    """Paginated Feishu /commands output should use Chinese built-in descriptions."""
    import gateway.run as gateway_run

    monkeypatch.setattr(
        gateway_run,
        "_load_gateway_config",
        lambda: {"display": {"language": "zh", "gateway_locale": "zh"}},
    )

    result = await _make_runner()._handle_commands_command(
        _make_event("/commands 1", Platform.FEISHU)
    )

    assert "**会话：**" in result
    assert "`/new [name]` -- 开始新会话" in result
    assert "Start a new session" not in result
