from gateway.run import (
    _format_busy_session_ack_message,
    _format_busy_session_status_detail,
    _format_feishu_tool_failure_message,
    _format_feishu_verbose_tool_message,
    _format_inactivity_timeout_lines,
    _format_long_running_notice,
    _feishu_tool_emoji,
    _localize_feishu_background_review_message,
    _localize_feishu_guardrail_message,
    _localize_feishu_tool_progress_message,
    _zh_enabled_for_gateway,
)


def test_feishu_tool_progress_localizes_todo_preview():
    assert _localize_feishu_tool_progress_message('📋 todo: "planning 6 task(s)"') == '📋 待办: "规划 6 个任务"'
    assert _localize_feishu_tool_progress_message('📋 todo: "updating 3 task(s)"') == '📋 待办: "更新 3 个任务"'


def test_feishu_tool_progress_localizes_common_github_mcp_tools():
    assert (
        _localize_feishu_tool_progress_message('⚙️ mcp_github_get_file_contents: "README.md"')
        == '⚙️ 读取 GitHub 文件: "README.md"'
    )
    assert (
        _localize_feishu_tool_progress_message('⚙️ mcp_github_create_or_update_file: "README.md"')
        == '⚙️ 创建/更新 GitHub 文件: "README.md"'
    )
    assert (
        _localize_feishu_tool_progress_message('⚙️ mcp_github_create_repository: "hermes-tui-reverse-study"')
        == '⚙️ 创建 GitHub 仓库: "hermes-tui-reverse-study"'
    )


def test_feishu_tool_progress_localizes_delegate_without_preview():
    assert _localize_feishu_tool_progress_message("↗️ delegate_task...") == "↗️ 分派任务…"


def test_feishu_tool_progress_localizes_recent_tool_names_and_phrases():
    assert (
        _localize_feishu_tool_progress_message('📄 web_extract: "https://github.com/EverMind-AI/EverMind"')
        == '📄 网页提取: "https://github.com/EverMind-AI/EverMind"'
    )
    assert (
        _localize_feishu_tool_progress_message('🔧 tool: "EverMind EverOS long-term memory self-evolving agents"')
        == '🔧 调用工具: "EverMind EverOS long-term memory self-evolving agents"'
    )
    assert (
        _localize_feishu_tool_progress_message('🧩 task_analysis: "Deep study of EverMind-AI/EverOS. Focus on: architecture"')
        == '🧩 任务分析: "深入研究 EverMind-AI/EverOS。重点：architecture"'
    )
    assert _localize_feishu_tool_progress_message("🚨 Executing process (5 steps)") == "🧰 执行过程（5步）"


def test_feishu_tool_progress_localizes_multiline_tool_record():
    raw = "\n".join(
        [
            "🚨 Executing process (5 steps)",
            '📄 web_extract: "https://github.com/EverMind-AI/EverMind"',
            '🔧 Calling tool: "EverMind EverOS long-term memory self-evolving agents"',
            '🌐 web_search: "EverMind EverOS long-term memory self-evolving agents github 2026"',
            '🧩 delegate_task: "Deep study of EverMind-AI/EverOS. Focus on: architecture"',
        ]
    )

    localized = _localize_feishu_tool_progress_message(raw)

    assert "🧰 执行过程（5步）" in localized
    assert "📄 网页提取" in localized
    assert "🔧 调用工具" in localized
    assert "🌐 网页搜索" in localized
    assert "🧩 分派任务" in localized
    assert "web_extract" not in localized
    assert "web_search" not in localized
    assert "delegate_task" not in localized
    assert "Executing process" not in localized
    assert "Calling tool" not in localized


def test_feishu_process_tool_record_uses_screenshot_header_shape():
    assert (
        _localize_feishu_tool_progress_message('🤖 process: "Executing process (5 steps)"')
        == "🧰 执行过程（5步）"
    )
    assert (
        _localize_feishu_tool_progress_message('🚨 process: "Executing process (5 steps)"')
        == "🧰 执行过程（5步）"
    )


def test_feishu_process_step_count_is_dynamic():
    assert (
        _localize_feishu_tool_progress_message('🤖 process: "Executing process (12 steps)"')
        == "🧰 执行过程（12步）"
    )


def test_feishu_tool_record_localizes_unclosed_preview_line():
    localized = _localize_feishu_tool_progress_message(
        '🧩 delegate_task: "Deep study of EverMind-AI/EverOS '
        '(github.com/EverMind-AI/EverOS). Focus on:'
    )
    assert localized == (
        '🧩 分派任务: "深入研究 EverMind-AI/EverOS '
        '(github.com/EverMind-AI/EverOS)。重点：'
    )
    assert "delegate_task" not in localized
    assert "Deep study" not in localized
    assert "Focus on" not in localized


def test_feishu_tool_progress_has_stable_emoji_for_internal_events():
    assert _feishu_tool_emoji("process") == "🧰"
    assert _feishu_tool_emoji("tool") == "🔧"
    assert _feishu_tool_emoji("delegate_task") == "🧩"
    assert _feishu_tool_emoji("task_analysis") == "🧩"
    assert _feishu_tool_emoji("web_extract") == "📄"
    assert _feishu_tool_emoji("web_search") == "🌐"
    assert _feishu_tool_emoji("browser_snapshot") == "📸"
    assert _feishu_tool_emoji("browser_console") == "🖥️"
    assert _feishu_tool_emoji("unknown_tool", "⚙️") == "⚙️"


def test_feishu_tool_failure_message_is_chinese_and_compact():
    assert (
        _format_feishu_tool_failure_message(
            tool_name="web_extract",
            result_preview="Error executing tool 'web_extract': timed out while fetching page",
        )
        == "⚠️ 网页提取失败: timed out while fetching page"
    )
    assert (
        _format_feishu_tool_failure_message(
            tool_name="web_extract",
            result_preview='{"results":[{"url":"https://skillhub.cloud.tencent.com/skills/tencent-novnc-chromium-cdp","error":"request timeout"}]}',
        )
        == "⚠️ 网页提取失败: request timeout"
    )


def test_feishu_browser_tool_names_and_guardrail_are_chinese():
    assert _localize_feishu_tool_progress_message('📸 browser_snapshot: "compact"') == '📸 浏览器快照: "紧凑"'
    assert _localize_feishu_tool_progress_message('🖥️ browser_console: "console logs"') == '🖥️ 浏览器控制台: "控制台日志"'
    assert (
        _localize_feishu_guardrail_message("⚠️ Tool guardrail halted browser_snapshot: idempotent_no_progress_block")
        == "⚠️ 工具防重复已暂停 浏览器快照: 页面状态重复无进展"
    )
    assert (
        _localize_feishu_guardrail_message(
            "I stopped retrying browser_snapshot because it hit the tool-call guardrail "
            "(idempotent_no_progress_block) after 5 repeated non-progressing attempts. "
            "The last tool result explains the blocker; the next step is to change strategy instead of repeating the same call."
        )
        == "我已停止重复调用 浏览器快照，因为连续 5 次没有取得新进展（页面状态重复无进展）。上一条工具结果里有阻塞原因，下一步需要换方法，而不是继续重复同一个调用。"
    )


def test_feishu_background_review_message_is_chinese():
    assert (
        _localize_feishu_background_review_message("💾 Self-improvement review: Memory updated")
        == "💾 自我改进复盘: 记忆已更新"
    )
    assert (
        _localize_feishu_background_review_message("💾 Self-improvement review: User profile updated")
        == "💾 自我改进复盘: 用户画像已更新"
    )


def test_feishu_verbose_progress_compacts_terminal_args():
    assert _format_feishu_verbose_tool_message(
        emoji="$",
        tool_name="terminal",
        args={"command": "tail -50 /e/AI/hermes/logs/gateway.log 2>/dev/null", "cwd": "E:/AI/hermes"},
    ) == "$ 终端: 命令: tail -50 /e/AI/hermes/logs/gateway.log 2>/dev/null；目录: E:/AI/hermes"


def test_feishu_verbose_progress_compacts_send_message_args():
    assert _format_feishu_verbose_tool_message(
        emoji="📰",
        tool_name="send_message",
        args={"to": "feishu", "content": "MEDIA:C:\\Users\\Administrator\\AppData\\Local\\Temp\\avatar.png"},
    ) == "📰 发送消息: 发送到: feishu；内容: MEDIA:C:\\Users\\Administrator\\AppData\\Local\\Temp\\avatar.png"


def test_feishu_verbose_progress_localizes_web_extract_urls_arg():
    assert _format_feishu_verbose_tool_message(
        emoji="📄",
        tool_name="web_extract",
        args={"urls": ["https://github.com/EverMind-AI/EverMind"]},
    ) == '📄 网页提取: 链接: ["https://github.com/EverMind-AI/EverMind"]'


def test_feishu_long_running_notice_localizes_iteration_and_streaming_activity():
    assert _format_long_running_notice(
        elapsed_mins=4,
        iteration=9,
        max_iterations=90,
        activity_desc="receiving stream response",
        locale_zh=True,
    ) == "⏳ 仍在处理…（已用 4 分钟 — 第 9/90 轮，正在接收流式响应）"


def test_feishu_long_running_notice_localizes_waiting_provider_activity():
    assert _format_long_running_notice(
        elapsed_mins=6,
        iteration=25,
        max_iterations=90,
        activity_desc="waiting for provider response (streaming)",
        locale_zh=True,
    ) == "⏳ 仍在处理…（已用 6 分钟 — 第 25/90 轮，正在等待模型流式响应）"


def test_feishu_busy_ack_status_detail_is_chinese():
    detail = _format_busy_session_status_detail(
        summary={"api_call_count": 26, "max_iterations": 90, "current_tool": "terminal"},
        start_ts=100.0,
        now=460.0,
        locale_zh=True,
    )
    assert detail == "（已用 6 分钟，第 26/90 轮，正在运行: 终端）"
    assert _format_busy_session_ack_message(
        mode="steer",
        status_detail=detail,
        locale_zh=True,
    ) == "⏩ 已插入当前运行（已用 6 分钟，第 26/90 轮，正在运行: 终端）。你的消息会在下一次工具调用后送达。"


def test_feishu_inactivity_timeout_lines_are_chinese():
    lines = _format_inactivity_timeout_lines(
        timeout_mins=30,
        last_desc="waiting for provider response (streaming)",
        secs_ago=1800,
        current_tool=None,
        iteration=25,
        max_iterations=90,
        locale_zh=True,
    )
    joined = "\n".join(lines)
    assert "Agent 已连续 30 分钟没有工具调用或模型响应" in joined
    assert "上次活动: 正在等待模型流式响应" in joined
    assert "iteration" not in joined
    assert "Last activity" not in joined


def test_feishu_zh_enabled_from_display_gateway_locale():
    assert _zh_enabled_for_gateway({"display": {"gateway_locale": "zh"}}, "feishu") is True
    assert _zh_enabled_for_gateway({"display": {"platforms": {"feishu": {"language": "zh-CN"}}}}, "feishu") is True
