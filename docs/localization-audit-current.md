# Localization Audit Current

- Generated: 2026-05-21 12:52:24 +08:00
- Scope: all
- Repo: E:\AI\hermes\hermes-agent
- HERMES_HOME: E:\AI\hermes

## Summary

| Category | Count |
| --- | ---: |
| could_review | 3781 |
| mixed_review | 195 |
| must_review | 50 |
| skip_tech | 1028 |

## must_review

| Scope | File | Line | Reason | Text |
| --- | --- | ---: | --- | --- |
| feishu | gateway\platforms\feishu_comment.py | 263 | literal display field | Returns ``{"title": "...", "url": "...", "doc_type": "..."}`` or empty dict. |
| feishu | gateway\platforms\feishu.py | 639 | literal display field | return [[{"tag": "md", "text": ""}]] |
| feishu | gateway\platforms\feishu.py | 692 | user-facing field | title = _normalize_feishu_text(str(resolved.get("title", "")).strip()) |
| feishu | gateway\platforms\feishu.py | 775 | user-facing field | label = str(element.get("text", href) or "").strip() |
| feishu | gateway\platforms\feishu.py | 783 | user-facing field | placeholder = str(element.get("user_id", "")).strip() |
| feishu | gateway\platforms\feishu.py | 819 | user-facing field | label = str(element.get("text", "")).strip() or str(element.get("emoji_type", "")).strip() |
| feishu | gateway\platforms\feishu.py | 1161 | user-facing field | title = header.get("title") |
| feishu | gateway\platforms\feishu.py | 1278 | user-facing field | name = str(getattr(mention, "name", "") or "").strip() |
| feishu | gateway\platforms\feishu.py | 1737 | Feishu error/response | self._set_fatal_error("feishu_app_lock", message, retryable=False) |
| feishu | gateway\platforms\feishu.py | 1748 | Feishu error/response | self._set_fatal_error("feishu_connect_error", message, retryable=True) |
| feishu | gateway\platforms\feishu.py | 2042 | literal display field | {"tag": "markdown", "content": f"{prompt}{default_hint}"}, |
| feishu | gateway\platforms\feishu.py | 2096 | literal display field | "title": {"content": f"{icon} {label}", "tag": "plain_text"}, |
| feishu | gateway\platforms\feishu.py | 2394 | user-facing field | message = getattr(event, "message", None) |
| feishu | gateway\platforms\feishu.py | 2496 | user-facing field | message = getattr(event, "message", None) |
| feishu | gateway\platforms\feishu.py | 2525 | user-facing field | message = getattr(event, "message", None) |
| feishu | gateway\platforms\feishu.py | 3336 | Feishu error/response | return _web_json_response({"challenge": payload.get("challenge", "")}) |
| feishu | gateway\platforms\feishu.py | 3378 | Feishu error/response | return _web_json_response({"code": 0, "msg": "ok"}) |
| feishu | gateway\platforms\feishu.py | 4022 | user-facing field | placeholder = normalized.metadata.get("placeholder_text") if isinstance(normalized.metadata, dict) else None |
| feishu | gateway\platforms\feishu.py | 4950 | user-facing output | print(".", end="", flush=True) |
| feishu | gateway\platforms\feishu.py | 4972 | user-facing field | error = res.get("error", "") |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 231 | TUI status/output | turnController.pushActivity(String(r.warning), 'warn') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 308 | user-facing field | status: state.status === 'starting agent…' ? 'ready' : state.status, |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 388 | TUI status/output | turnController.pushActivity(line, 'info') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 458 | TUI status/output | setStatus('gateway startup timeout') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 688 | user-facing field | status: normalizeSubagentStatus(ev.payload.status, 'completed'), |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 712 | TUI status/output | setStatus('ready') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 727 | TUI status/output | turnController.pushActivity(message, 'error') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 731 | TUI status/output | setStatus('setup required') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 737 | TUI status/output | setStatus('ready') |
| tui | ui-tui\src\app\slash\commands\session.ts | 181 | TUI status/output | ctx.transcript.sys(`${prefix}${r.summary.headline}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 184 | TUI status/output | ctx.transcript.sys(` ${r.summary.token_line}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 188 | TUI status/output | ctx.transcript.sys(` ${r.summary.note}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 287 | TUI status/output | ctx.transcript.sys(` ${line}`) |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 151 | user-facing field | status: normalizeSubagentStatus(o.status, 'completed'), |
| tui | ui-tui\src\app\turnController.ts | 47 | user-facing field | status === 'pending' \|\| status === 'in_progress' \|\| status === 'completed' \|\| status === 'cancelled' |
| tui | ui-tui\src\app\turnController.ts | 387 | TUI status/output | pushActivity(text: string, tone: ActivityItem['tone'] = 'info', replaceLabel?: string) { |
| tui | ui-tui\src\app\uiStore.ts | 25 | user-facing field | status: 'summoning hermes…', |
| tui | ui-tui\src\app\useComposerState.ts | 144 | TUI JSX literal | }: Omit<PasteEvent, 'hotkey'>): Promise<null \| { cursor: number; value: string }> => { |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 154 | user-facing field | status: info?.version ? 'ready' : 'starting agent…', |
| tui | ui-tui\src\components\agentsOverlay.tsx | 471 | user-facing field | name="subtree" |
| tui | ui-tui\src\components\agentsOverlay.tsx | 484 | user-facing field | name="tokens" |
| tui | ui-tui\src\components\agentsOverlay.tsx | 497 | user-facing field | name="cost" |
| tui | ui-tui\src\components\agentsOverlay.tsx | 837 | TUI JSX literal | const interrupt = (id: string) => gw.request<SubagentInterruptResponse>('subagent.interrupt', { subagent_id: id }) |
| tui | ui-tui\src\components\textInput.tsx | 361 | TUI JSX literal | ): value is Promise<PasteResult> => !!value && typeof (value as PromiseLike<PasteResult>).then === 'function' |
| tui | ui-tui\src\lib\todo.ts | 6 | user-facing field | status === 'completed' ? '[x]' : status === 'cancelled' ? '[-]' : status === 'in_progress' ? '[>]' : '[ ]' |
| tui | ui-tui\src\lib\todo.ts | 9 | user-facing field | status === 'in_progress' ? 'active' : status === 'pending' ? 'body' : 'dim' |
| tui | ui-tui\src\theme.ts | 256 | user-facing field | name: 'Hermes Agent', |
| tui | ui-tui\src\theme.ts | 628 | user-facing field | label: c('ui_label') ?? d.color.label, |
| tui | ui-tui\src\theme.ts | 630 | user-facing field | error: c('ui_error') ?? d.color.error, |
| tui | ui-tui\src\types.ts | 11 | user-facing field | status: 'cancelled' \| 'completed' \| 'in_progress' \| 'pending' |

## mixed_review

| Scope | File | Line | Reason | Text |
| --- | --- | ---: | --- | --- |
| feishu | gateway\platforms\feishu_comment_rules.py | 306 | user-facing output | print(f" 启用: {cfg.enabled}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 307 | user-facing output | print(f" 策略: {cfg.policy}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 308 | user-facing output | print(f" 允许来源: {sorted(cfg.allow_from) if cfg.allow_from else '[]'}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 311 | user-facing output | print(f"文档规则 ({len(cfg.documents)}):") |
| feishu | gateway\platforms\feishu_comment_rules.py | 320 | user-facing output | print(f" [{key}] {', '.join(parts) if parts else '（空，继承全部）'}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 325 | user-facing output | print(f"已配对用户 ({len(approved)}):") |
| feishu | gateway\platforms\feishu_comment_rules.py | 328 | user-facing output | print(f" {uid} (批准时间={ts})") |
| feishu | gateway\platforms\feishu_comment_rules.py | 335 | user-facing output | print(f"错误: doc_key 必须是 'fileType:fileToken'，当前是 '{doc_key}'") |
| feishu | gateway\platforms\feishu_comment_rules.py | 340 | user-facing output | print(f"文档: {doc_key}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 341 | user-facing output | print(f"用户: {user_open_id}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 343 | user-facing output | print(f" 启用: {rule.enabled}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 344 | user-facing output | print(f" 策略: {rule.policy}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 345 | user-facing output | print(f" 允许来源: {sorted(rule.allow_from) if rule.allow_from else '[]'}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 346 | user-facing output | print(f" 匹配来源: {rule.match_source}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 347 | user-facing output | print(f"结果: {'允许' if allowed else '拒绝'}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 386 | user-facing output | print("用法: check <fileType:fileToken> <user_open_id>") |
| feishu | gateway\platforms\feishu_comment_rules.py | 392 | user-facing output | print("用法: pairing <add\|remove\|list> [args]") |
| feishu | gateway\platforms\feishu_comment_rules.py | 397 | user-facing output | print("用法: pairing add <user_open_id>") |
| feishu | gateway\platforms\feishu_comment_rules.py | 400 | user-facing output | print(f"已添加: {args[2]}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 402 | user-facing output | print(f"已在允许列表: {args[2]}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 405 | user-facing output | print("用法: pairing remove <user_open_id>") |
| feishu | gateway\platforms\feishu_comment_rules.py | 408 | user-facing output | print(f"已移除: {args[2]}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 410 | user-facing output | print(f"不在允许列表: {args[2]}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 416 | user-facing output | print(f" {uid} 批准时间={meta.get('approved_at', '?')}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 418 | user-facing output | print(f"未知 pairing 子命令: {sub}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 421 | user-facing output | print(f"未知命令: {cmd}\n") |
| feishu | gateway\platforms\feishu.py | 594 | literal display field | "title": {"tag": "plain_text", "content": "Hermes · 飞书"}, |
| feishu | gateway\platforms\feishu.py | 617 | literal display field | "title": {"tag": "plain_text", "content": "📌 运行状态"}, |
| feishu | gateway\platforms\feishu.py | 1747 | user-facing field | message = f"飞书启动失败: {exc}" |
| feishu | gateway\platforms\feishu.py | 1979 | literal display field | "title": {"content": "⚠️ 需要确认命令", "tag": "plain_text"}, |
| feishu | gateway\platforms\feishu.py | 1985 | literal display field | "content": f"```\n{cmd_preview}\n```\n**原因:** {description}", |
| feishu | gateway\platforms\feishu.py | 2038 | literal display field | "title": {"content": "⚕ 更新需要你确认", "tag": "plain_text"}, |
| feishu | gateway\platforms\feishu.py | 2102 | literal display field | "content": f"{icon} **{label}**，操作者: {user_name}", |
| feishu | gateway\platforms\feishu.py | 2110 | user-facing field | label = "是" if yes else "否" |
| feishu | gateway\platforms\feishu.py | 2114 | literal display field | "title": {"content": f"{'✅' if yes else '❌'} 已回复更新确认: {label}", "tag": "plain_text"}, |
| feishu | gateway\platforms\feishu.py | 2118 | literal display field | {"tag": "markdown", "content": f"由 **{user_name}** 回复"}, |
| feishu | gateway\platforms\feishu.py | 3320 | Feishu error/response | return _web_json_response({"code": 400, "msg": "请求体读取失败"}, status=400) |
| feishu | gateway\platforms\feishu.py | 3345 | Feishu error/response | return _web_response(status=401, text="verification token 无效") |
| feishu | gateway\platforms\feishu.py | 3356 | Feishu error/response | return _web_json_response({"code": 400, "msg": "暂不支持加密 webhook 请求体"}, status=400) |
| feishu | gateway\platforms\feishu.py | 4522 | user-facing output | raise RuntimeError("未安装 websockets，websocket 模式不可用") |
| feishu | gateway\platforms\feishu.py | 4548 | user-facing output | raise RuntimeError("未安装 aiohttp，webhook 模式不可用") |
| feishu | gateway\platforms\feishu.py | 4948 | user-facing output | print(" 正在获取配置结果...", end="", flush=True) |
| feishu | gateway\platforms\feishu.py | 5145 | user-facing output | print(" 提示: 安装 qrcode 后，下次可直接在这里显示可扫描二维码") |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\plugin.yaml | 3 | user-facing field | description: "把 lark-cli 接入 Hermes，提供个人飞书文档、消息、任务、日程、Markdown 和多维表格工具。" |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 195 | TUI status/output | sys(`启动图片附加失败: ${rpcErrorMessage(e)}`) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 234 | TUI status/output | .catch((e: unknown) => turnController.pushActivity(`命令目录不可用: ${rpcErrorMessage(e)}`, 'info')) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 459 | TUI status/output | turnController.pushActivity(`网关启动超时${trace} · 使用 /logs 查看`, 'error') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 489 | TUI status/output | turnController.pushActivity('检测到协议噪声 · 可用 /logs 查看', 'info') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 493 | TUI status/output | turnController.pushActivity(`协议噪声: ${String(ev.payload.preview).slice(0, 120)}`, 'info') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 519 | TUI status/output | turnController.pushTrail(`起草 ${ev.payload.name}…`) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 573 | TUI status/output | setStatus('需要 sudo 密码') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 586 | TUI status/output | sys(`[后台 ${ev.payload.task_id}] ${ev.payload.text}`) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 736 | TUI status/output | sys(`错误: ${message}`) |
| tui | ui-tui\src\app\createSlashHandler.ts | 34 | TUI status/output | sys(`错误: ${rpcErrorMessage(e)}`) |
| tui | ui-tui\src\app\createSlashHandler.ts | 70 | TUI status/output | sys(`命令不明确: ${matches.slice(0, 6).join(', ')}${matches.length > 6 ? ', …' : ''}`) |
| tui | ui-tui\src\app\createSlashHandler.ts | 99 | TUI status/output | return sys('错误: command.dispatch 返回无效') |
| tui | ui-tui\src\app\createSlashHandler.ts | 111 | TUI status/output | sys(`⚡ 正在加载技能: ${d.name}`) |
| tui | ui-tui\src\app\createSlashHandler.ts | 113 | TUI status/output | return d.message?.trim() ? send(d.message) : sys(`/${parsed.name}: 技能载荷缺少消息`) |
| tui | ui-tui\src\app\createSlashHandler.ts | 120 | TUI status/output | return d.message?.trim() ? send(d.message) : sys(`/${parsed.name}: 消息为空`) |
| tui | ui-tui\src\app\setupHandoff.ts | 20 | TUI status/output | transcript.sys(`正在启动 \`hermes ${args.join(' ')}\`…`) |
| tui | ui-tui\src\app\setupHandoff.ts | 30 | TUI status/output | transcript.sys(`启动 Hermes 失败: ${result.error}`) |
| tui | ui-tui\src\app\setupHandoff.ts | 37 | TUI status/output | transcript.sys(`hermes ${args[0]} 退出，代码 ${result.code}`) |
| tui | ui-tui\src\app\slash\commands\core.ts | 107 | user-facing field | help: '退出 Hermes', |
| tui | ui-tui\src\app\slash\commands\core.ts | 125 | user-facing field | help: '切换鼠标/滚轮跟踪 [on\|off\|toggle]', |
| tui | ui-tui\src\app\slash\commands\core.ts | 132 | TUI status/output | return ctx.transcript.sys('用法: /mouse [on\|off\|toggle]') |
| tui | ui-tui\src\app\slash\commands\core.ts | 138 | TUI status/output | queueMicrotask(() => ctx.transcript.sys(`鼠标跟踪 ${next ? '开启' : '关闭'}`)) |
| tui | ui-tui\src\app\slash\commands\core.ts | 228 | TUI status/output | ctx.transcript.sys(current ? `标题: ${current}` : '尚未设置标题') |
| tui | ui-tui\src\app\slash\commands\core.ts | 237 | TUI status/output | return ctx.transcript.sys('用法: /title <会话标题>') |
| tui | ui-tui\src\app\slash\commands\core.ts | 246 | TUI status/output | ctx.transcript.sys(`会话标题已设置: ${next}${suffix}`) |
| tui | ui-tui\src\app\slash\commands\core.ts | 260 | TUI status/output | return ctx.transcript.sys('用法: /compact [on\|off\|toggle]') |
| tui | ui-tui\src\app\slash\commands\core.ts | 266 | TUI status/output | queueMicrotask(() => ctx.transcript.sys(`紧凑模式 ${next ? '开启' : '关闭'}`)) |
| tui | ui-tui\src\app\slash\commands\core.ts | 292 | TUI status/output | transcript.sys(`过程细节: ${detailsModeLabel(mode)}${overrides ? ` (${overrides})` : ''}`) |
| tui | ui-tui\src\app\slash\commands\core.ts | 294 | TUI status/output | .catch(() => !ctx.stale() && transcript.sys(`过程细节: ${detailsModeLabel(ui.detailsMode)}`)) |
| tui | ui-tui\src\app\slash\commands\core.ts | 315 | TUI status/output | transcript.sys(`过程细节 ${detailsSectionLabel(first)}: ${mode ? detailsModeLabel(mode) : '重置'}`) |
| tui | ui-tui\src\app\slash\commands\core.ts | 330 | TUI status/output | transcript.sys(`过程细节: ${detailsModeLabel(next)}`) |
| tui | ui-tui\src\app\slash\commands\core.ts | 348 | TUI status/output | ctx.transcript.sys('用法: /fortune [random\|daily]') |
| tui | ui-tui\src\app\slash\commands\core.ts | 362 | TUI status/output | return sys(`已复制 ${text.length} 个字符`) |
| tui | ui-tui\src\app\slash\commands\core.ts | 371 | TUI status/output | return sys('用法: /copy [number]') |
| tui | ui-tui\src\app\slash\commands\core.ts | 396 | TUI status/output | sys(`复制失败: ${String(error)}`) |
| tui | ui-tui\src\app\slash\commands\core.ts | 405 | TUI status/output | run: (arg, ctx) => (arg ? ctx.transcript.sys('用法: /paste') : ctx.composer.paste()) |
| tui | ui-tui\src\app\slash\commands\core.ts | 415 | TUI status/output | return ctx.transcript.sys('用法: /terminal-setup [auto\|vscode\|cursor\|windsurf]') |
| tui | ui-tui\src\app\slash\commands\core.ts | 437 | TUI status/output | ctx.transcript.sys(`终端设置失败: ${String(error)}`) |
| tui | ui-tui\src\app\slash\commands\core.ts | 449 | TUI status/output | text ? ctx.transcript.page(text, '日志') : ctx.transcript.sys('没有网关日志') |
| tui | ui-tui\src\app\slash\commands\core.ts | 504 | TUI status/output | ctx.transcript.sys(`对话已保存到: ${file}`) |
| tui | ui-tui\src\app\slash\commands\core.ts | 516 | user-facing field | help: '状态栏位置 (on\|off\|top\|bottom)', |
| tui | ui-tui\src\app\slash\commands\core.ts | 532 | TUI status/output | return ctx.transcript.sys('用法: /statusbar [on\|off\|top\|bottom\|toggle]') |
| tui | ui-tui\src\app\slash\commands\core.ts | 538 | TUI status/output | queueMicrotask(() => ctx.transcript.sys(`状态栏 ${next === 'off' ? '关闭' : next === 'bottom' ? '底部' : '顶部'}`)) |
| tui | ui-tui\src\app\slash\commands\core.ts | 547 | TUI status/output | return ctx.transcript.sys(`队列中有 ${ctx.composer.queueRef.current.length} 条消息`) |
| tui | ui-tui\src\app\slash\commands\core.ts | 551 | TUI status/output | ctx.transcript.sys(`已加入队列: "${arg.slice(0, 50)}${arg.length > 50 ? '…' : ''}"`) |
| tui | ui-tui\src\app\slash\commands\core.ts | 562 | TUI status/output | return ctx.transcript.sys('用法: /steer <提示词>') |
| tui | ui-tui\src\app\slash\commands\core.ts | 605 | TUI status/output | ctx.transcript.sys(`已撤销 ${r.removed} 条消息`) |
| tui | ui-tui\src\app\slash\commands\debug.ts | 11 | TUI status/output | ctx.transcript.sys(`正在写入堆快照（堆 ${formatBytes(heapUsed)} · 常驻内存 ${formatBytes(rss)}）…`) |
| tui | ui-tui\src\app\slash\commands\debug.ts | 19 | TUI status/output | return ctx.transcript.sys(`堆快照失败: ${r.error ?? '未知错误'}`) |
| tui | ui-tui\src\app\slash\commands\debug.ts | 22 | TUI status/output | ctx.transcript.sys(`堆快照: ${r.heapPath}`) |
| tui | ui-tui\src\app\slash\commands\debug.ts | 23 | TUI status/output | ctx.transcript.sys(`诊断: ${r.diagPath}`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 74 | TUI status/output | ctx.transcript.sys(`已停止 ${killed} 个后台进程`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 104 | TUI status/output | ctx.transcript.sys(r.message \|\| '/reload-mcp 需要确认') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 131 | TUI status/output | ctx.transcript.sys(`已重载 .env（更新 ${n} 个变量）`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 155 | TUI status/output | ctx.transcript.sys(`正在检查 Chromium 系浏览器远程调试: ${url}...`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 182 | TUI status/output | ctx.transcript.sys(`端点: ${r.url \|\| '（url 不可用）'}`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 235 | TUI status/output | return ctx.transcript.sys('用法: /rollback diff <检查点>') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 267 | TUI status/output | return ctx.transcript.sys(`回滚失败: ${r.error \|\| r.message \|\| '未知错误'}`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 272 | TUI status/output | ctx.transcript.sys(`回滚已恢复 ${target}: ${detail}`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 299 | TUI status/output | ctx.transcript.sys(`派生任务 · ${r?.paused ? '已暂停' : '已恢复'}`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 320 | user-facing field | help: '回放已完成的派生树 · `/replay [N\|last\|list\|load <path>]`', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 362 | TUI status/output | return ctx.transcript.sys('用法: /replay load <路径>') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 386 | TUI status/output | return ctx.transcript.sys('当前会话还没有已完成的派生树 · 可试 /replay list') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 395 | TUI status/output | return ctx.transcript.sys(`回放: 序号超出范围 1..${history.length} · 磁盘记录用 /replay list`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 406 | user-facing field | help: '对比两个已完成派生树 · `/replay-diff <baseline> <candidate>`（序号来自 /replay list 或历史 N）', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 412 | TUI status/output | return ctx.transcript.sys('用法: /replay-diff <基线> <候选> （例如 /replay-diff 1 2 对比最近两个）') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 432 | TUI status/output | return ctx.transcript.sys(`回放对比: 无法解析序号 · 当前历史有 ${history.length} 条`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 528 | TUI status/output | return sys('用法: /skills inspect <名称>') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 537 | TUI status/output | return sys(`未知技能: ${query}`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 562 | TUI status/output | return sys('用法: /skills search <关键词>') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 571 | TUI status/output | return sys(`没有结果: ${query}`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 587 | TUI status/output | sys(`正在安装 ${query}…`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 592 | TUI status/output | sys(r.installed ? `已安装 ${r.name ?? query}` : '安装失败') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 604 | TUI status/output | return sys('用法: /skills browse [页码] （页码必须是正数）') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 615 | TUI status/output | return sys(`第 ${pageNum} 页没有技能${r.total ? `（共 ${r.total}）` : ''}`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 678 | TUI status/output | ctx.transcript.sys(`用法: /tools ${subcommand} <名称> [名称 ...]`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 679 | TUI status/output | ctx.transcript.sys(`内置工具集: /tools ${subcommand} web`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 695 | TUI status/output | ctx.transcript.sys(`${subcommand === 'disable' ? '已禁用' : '已启用'}: ${r.changed.join(', ')}`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 699 | TUI status/output | ctx.transcript.sys(`未知工具集: ${r.unknown.join(', ')}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 55 | TUI status/output | return ctx.transcript.sys('/background <提示词>') |
| tui | ui-tui\src\app\slash\commands\session.ts | 65 | TUI status/output | ctx.transcript.sys(`后台任务 ${r.task_id} 已启动`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 91 | TUI status/output | ctx.transcript.sys(`模型 → ${r.value}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 146 | TUI status/output | ctx.transcript.sys(`人格: ${r.value \|\| '默认'}${r.history_reset ? ' · 对话已清空' : ''}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 224 | TUI status/output | ctx.transcript.sys(`已创建分支 → ${r.title ?? ''}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 231 | user-facing field | help: '语音模式：[on\|off\|tts\|status]', |
| tui | ui-tui\src\app\slash\commands\session.ts | 274 | TUI status/output | ctx.transcript.sys(` 模式: ${onOffLabel(r.enabled)}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 276 | TUI status/output | ctx.transcript.sys(` 录音键: ${recordKeyLabel}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 304 | TUI status/output | ctx.transcript.sys(`语音模式已开启${tts}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 305 | TUI status/output | ctx.transcript.sys(` ${recordKeyLabel} 开始/停止录音`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 306 | TUI status/output | ctx.transcript.sys(' /voice tts 切换语音朗读') |
| tui | ui-tui\src\app\slash\commands\session.ts | 307 | TUI status/output | ctx.transcript.sys(' /voice off 关闭语音模式') |
| tui | ui-tui\src\app\slash\commands\session.ts | 323 | TUI status/output | .then(ctx.guarded<ConfigGetValueResponse>(r => ctx.transcript.sys(`皮肤: ${r.value \|\| '默认'}`))) |
| tui | ui-tui\src\app\slash\commands\session.ts | 328 | TUI status/output | .then(ctx.guarded<ConfigSetResponse>(r => r.value && ctx.transcript.sys(`皮肤 → ${r.value}`))) |
| tui | ui-tui\src\app\slash\commands\session.ts | 333 | user-facing field | help: '选择忙碌指示器：kaomoji（默认）、emoji、unicode（盲文）或 ascii', |
| tui | ui-tui\src\app\slash\commands\session.ts | 363 | TUI status/output | ctx.transcript.sys(`指示器 → ${r.value}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 370 | user-facing field | help: '切换 yolo 模式（当前会话审批策略）', |
| tui | ui-tui\src\app\slash\commands\session.ts | 375 | TUI status/output | .then(ctx.guarded<ConfigSetResponse>(r => ctx.transcript.sys(`yolo ${r.value === '1' ? '开启' : '关闭'}`))) |
| tui | ui-tui\src\app\slash\commands\session.ts | 390 | TUI status/output | ctx.transcript.sys(`推理: ${reasoningValueLabel(r.value)} · 思考 ${reasoningDisplayLabel(r.display)}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 417 | TUI status/output | ctx.transcript.sys(`推理: ${reasoningValueLabel(r.value)}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 424 | user-facing field | help: '切换快速模式 [normal\|fast\|status\|on\|off\|toggle]', |
| tui | ui-tui\src\app\slash\commands\session.ts | 431 | TUI status/output | return ctx.transcript.sys('用法: /fast [normal\|fast\|status\|on\|off\|toggle]') |
| tui | ui-tui\src\app\slash\commands\session.ts | 439 | TUI status/output | ctx.transcript.sys(`快速模式: ${r.value === 'fast' ? '快速' : '普通'}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 450 | TUI status/output | ctx.transcript.sys(`快速模式: ${next === 'fast' ? '快速' : '普通'}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 468 | user-facing field | help: '控制忙碌时回车行为 [queue\|steer\|interrupt\|status]', |
| tui | ui-tui\src\app\slash\commands\session.ts | 475 | TUI status/output | return ctx.transcript.sys('用法: /busy [queue\|steer\|interrupt\|status]') |
| tui | ui-tui\src\app\slash\commands\session.ts | 485 | TUI status/output | ctx.transcript.sys(`忙碌输入模式: ${label}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 497 | TUI status/output | ctx.transcript.sys(`忙碌输入模式: ${label}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 510 | TUI status/output | .then(ctx.guarded<ConfigSetResponse>(r => r.value && ctx.transcript.sys(`详细输出: ${r.value}`))) |
| tui | ui-tui\src\app\slash\commands\setup.ts | 9 | user-facing field | help: '运行完整设置向导（启动 `hermes setup`）', |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 115 | user-facing field | label: r.label \|\| `${normalised.length} 个子代理`, |
| tui | ui-tui\src\app\useInputHandlers.ts | 137 | TUI status/output | .then(r => r && (patchOverlayState({ sudo: null }), actions.sys('sudo 已取消'))) |
| tui | ui-tui\src\app\useInputHandlers.ts | 226 | TUI status/output | return actions.sys('语音模式未开启，可用 /voice on 开启') |
| tui | ui-tui\src\app\useInputHandlers.ts | 251 | TUI status/output | actions.sys(`语音错误: ${e.message}`) |
| tui | ui-tui\src\app\useInputHandlers.ts | 519 | TUI status/output | actions.sys(err instanceof Error ? `打开编辑器失败: ${err.message}` : '打开编辑器失败') |
| tui | ui-tui\src\app\useInputHandlers.ts | 526 | TUI status/output | return void actions.sys('yolo 需要一个活动会话') |
| tui | ui-tui\src\app\useInputHandlers.ts | 533 | TUI status/output | return actions.sys('yolo 开启') |
| tui | ui-tui\src\app\useInputHandlers.ts | 537 | TUI status/output | return actions.sys('yolo 关闭') |
| tui | ui-tui\src\app\useInputHandlers.ts | 541 | TUI status/output | actions.sys('yolo 切换失败') |
| tui | ui-tui\src\app\useMainApp.ts | 331 | TUI status/output | sys(`警告: ${warning}`) |
| tui | ui-tui\src\app\useMainApp.ts | 355 | TUI status/output | sys(`错误: ${method} 返回无效`) |
| tui | ui-tui\src\app\useMainApp.ts | 357 | TUI status/output | sys(`错误: ${rpcErrorMessage(e)}`) |
| tui | ui-tui\src\app\useMainApp.ts | 491 | TUI status/output | return sys(`📎 已从剪贴板附加图片 #${r.count}${meta ? ` · ${meta}` : ''}`) |
| tui | ui-tui\src\app\useMainApp.ts | 612 | TUI status/output | turnController.pushActivity('网关已退出 · 可用 /logs 查看', 'error') |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 163 | TUI status/output | sys(`警告: ${info.credential_warning}`) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 167 | TUI status/output | sys(`警告: ${info.config_warning}`) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 186 | TUI status/output | sys(`会话标题已设置: ${nextTitle}${suffix}`) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 194 | TUI status/output | sys(`警告: 会话标题设置失败: ${message}`) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 221 | TUI status/output | sys('错误: session.resume 返回无效') |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 242 | TUI status/output | sys(`错误: ${e.message}`) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 257 | TUI status/output | sys(`请先中断当前回合，再尝试${what}`) |
| tui | ui-tui\src\app\useSubmission.ts | 115 | TUI status/output | return sys(`已排队: "${submitText.slice(0, 50)}${submitText.length > 50 ? '…' : ''}"`) |
| tui | ui-tui\src\app\useSubmission.ts | 118 | TUI status/output | sys(`错误: ${e.message}`) |
| tui | ui-tui\src\app\useSubmission.ts | 141 | TUI status/output | turnController.pushActivity(`检测到文件: ${r.name}`) |
| tui | ui-tui\src\app\useSubmission.ts | 161 | TUI status/output | return sys('错误: shell.exec 返回无效') |
| tui | ui-tui\src\app\useSubmission.ts | 171 | TUI status/output | sys(`退出码 ${r.code}`) |
| tui | ui-tui\src\app\useSubmission.ts | 174 | TUI status/output | .catch((e: Error) => sys(`错误: ${e.message}`)) |
| tui | ui-tui\src\components\modelPicker.tsx | 277 | TUI JSX literal | <OverlayHint t={t}>Esc/q 取消</OverlayHint> |
| tui | ui-tui\src\components\modelPicker.tsx | 286 | TUI JSX literal | <OverlayHint t={t}>Esc/q 取消</OverlayHint> |
| tui | ui-tui\src\components\modelPicker.tsx | 329 | TUI JSX literal | <OverlayHint t={t}>Enter 保存 · Ctrl+U 清空 · Esc 返回</OverlayHint> |
| tui | ui-tui\src\components\modelPicker.tsx | 357 | TUI JSX literal | <OverlayHint t={t}>y/Enter 确认 · n/Esc 取消</OverlayHint> |
| tui | ui-tui\src\components\sessionPicker.tsx | 152 | TUI JSX literal | <OverlayHint t={t}>Esc/q 取消</OverlayHint> |
| tui | ui-tui\src\components\sessionPicker.tsx | 161 | TUI JSX literal | <OverlayHint t={t}>Esc/q 取消</OverlayHint> |
| tui | ui-tui\src\components\skillsHub.tsx | 189 | TUI JSX literal | <OverlayHint t={t}>Esc/q 取消</OverlayHint> |
| tui | ui-tui\src\components\skillsHub.tsx | 198 | TUI JSX literal | <OverlayHint t={t}>Esc/q 取消</OverlayHint> |
| tui | ui-tui\src\components\skillsHub.tsx | 294 | TUI JSX literal | <OverlayHint t={t}>i 重新检查 · x 重新安装 · Enter/Esc 返回 · q 关闭</OverlayHint> |
| tui | ui-tui\src\lib\terminalParity.ts | 46 | user-facing field | message: `检测到 ${ctx.vscodeLike} 终端 · 运行 /terminal-setup 可改善 Cmd+Enter / 撤销体验` |
| tui | ui-tui\src\lib\terminalSetup.ts | 305 | user-facing field | message: `无法确定 ${meta.label} 的设置路径。` |
| tui | ui-tui\src\lib\terminalSetup.ts | 336 | user-facing field | message: `读取 ${meta.label} 快捷键失败: ${error}` |
| tui | ui-tui\src\lib\terminalSetup.ts | 369 | user-facing field | message: `${meta.label} 终端快捷键已配置。` |
| tui | ui-tui\src\lib\terminalSetup.ts | 382 | user-facing field | message: `已在 ${keybindingsFile} 添加 ${added} 条 ${meta.label} 终端快捷键` |
| tui | ui-tui\src\lib\terminalSetup.ts | 387 | user-facing field | message: `配置 ${meta.label} 终端快捷键失败: ${error}` |

## could_review

| Scope | File | Line | Reason | Text |
| --- | --- | ---: | --- | --- |
| feishu | gateway\display_config.py | 3 | English string, visibility unknown | Provides ``resolve_display_setting()`` — the single entry-point for reading |
| feishu | gateway\display_config.py | 7 | English string, visibility unknown | 1. ``display.platforms.<platform>.<key>`` — explicit per-platform user override |
| feishu | gateway\display_config.py | 8 | English string, visibility unknown | 2. ``display.<key>`` — global user setting |
| feishu | gateway\display_config.py | 9 | English string, visibility unknown | 3. ``_PLATFORM_DEFAULTS[<platform>][<key>]`` — built-in sensible default |
| feishu | gateway\display_config.py | 10 | English string, visibility unknown | 4. ``_GLOBAL_DEFAULTS[<key>]`` — built-in global default |
| feishu | gateway\display_config.py | 13 | English string, visibility unknown | top-level ``streaming`` config unless ``display.platforms.<platform>.streaming`` |
| feishu | gateway\display_config.py | 16 | English string, visibility unknown | Backward compatibility: ``display.tool_progress_overrides`` is still read as a |
| feishu | gateway\display_config.py | 17 | English string, visibility unknown | fallback for ``tool_progress`` when no ``display.platforms`` entry exists. A |
| feishu | gateway\display_config.py | 19 | English string, visibility unknown | ``display.platforms`` structure. |
| feishu | gateway\display_config.py | 34 | English string, visibility unknown | "tool_progress": "all", |
| feishu | gateway\display_config.py | 35 | English string, visibility unknown | "show_reasoning": False, |
| feishu | gateway\display_config.py | 36 | English string, visibility unknown | "tool_preview_length": 0, |
| feishu | gateway\display_config.py | 37 | English string, visibility unknown | "streaming": None, # None = follow top-level streaming config |
| feishu | gateway\display_config.py | 38 | English string, visibility unknown | # When true, delete tool-progress / "Still working..." / status bubbles |
| feishu | gateway\display_config.py | 43 | English string, visibility unknown | "cleanup_progress": False, |
| feishu | gateway\display_config.py | 55 | English string, visibility unknown | "tool_progress": "all", |
| feishu | gateway\display_config.py | 56 | English string, visibility unknown | "show_reasoning": False, |
| feishu | gateway\display_config.py | 57 | English string, visibility unknown | "tool_preview_length": 40, |
| feishu | gateway\display_config.py | 58 | English string, visibility unknown | "streaming": None, # follow global |
| feishu | gateway\display_config.py | 62 | English string, visibility unknown | "tool_progress": "new", |
| feishu | gateway\display_config.py | 63 | English string, visibility unknown | "show_reasoning": False, |
| feishu | gateway\display_config.py | 64 | English string, visibility unknown | "tool_preview_length": 40, |
| feishu | gateway\display_config.py | 65 | English string, visibility unknown | "streaming": None, |
| feishu | gateway\display_config.py | 69 | English string, visibility unknown | "tool_progress": "off", |
| feishu | gateway\display_config.py | 70 | English string, visibility unknown | "show_reasoning": False, |
| feishu | gateway\display_config.py | 71 | English string, visibility unknown | "tool_preview_length": 40, |
| feishu | gateway\display_config.py | 72 | English string, visibility unknown | "streaming": False, |
| feishu | gateway\display_config.py | 76 | English string, visibility unknown | "tool_progress": "off", |
| feishu | gateway\display_config.py | 77 | English string, visibility unknown | "show_reasoning": False, |
| feishu | gateway\display_config.py | 78 | English string, visibility unknown | "tool_preview_length": 0, |
| feishu | gateway\display_config.py | 79 | English string, visibility unknown | "streaming": False, |
| feishu | gateway\display_config.py | 89 | English string, visibility unknown | # "new"/"all" spam permanent lines in channels (hermes-agent#14663). |
| feishu | gateway\display_config.py | 91 | English string, visibility unknown | "mattermost": _TIER_MEDIUM, |
| feishu | gateway\display_config.py | 92 | English string, visibility unknown | "matrix": _TIER_MEDIUM, |
| feishu | gateway\display_config.py | 96 | English string, visibility unknown | "signal": _TIER_LOW, |
| feishu | gateway\display_config.py | 97 | English string, visibility unknown | "whatsapp": _TIER_MEDIUM, # Baileys bridge supports /edit |
| feishu | gateway\display_config.py | 98 | English string, visibility unknown | "bluebubbles": _TIER_LOW, |
| feishu | gateway\display_config.py | 99 | English string, visibility unknown | "weixin": _TIER_LOW, |
| feishu | gateway\display_config.py | 100 | English string, visibility unknown | "wecom": _TIER_LOW, |
| feishu | gateway\display_config.py | 101 | English string, visibility unknown | "wecom_callback": _TIER_LOW, |
| feishu | gateway\display_config.py | 102 | English string, visibility unknown | "dingtalk": _TIER_LOW, |
| feishu | gateway\display_config.py | 105 | English string, visibility unknown | "email": _TIER_MINIMAL, |
| feishu | gateway\display_config.py | 106 | English string, visibility unknown | "sms": _TIER_MINIMAL, |
| feishu | gateway\display_config.py | 107 | English string, visibility unknown | "webhook": _TIER_MINIMAL, |
| feishu | gateway\display_config.py | 108 | English string, visibility unknown | "homeassistant": _TIER_MINIMAL, |
| feishu | gateway\display_config.py | 109 | English string, visibility unknown | "api_server": {**_TIER_HIGH, "tool_preview_length": 0}, |
| feishu | gateway\display_config.py | 130 | English string, visibility unknown | ``_platform_config_key(source.platform)`` from gateway/run.py. |
| feishu | gateway\display_config.py | 132 | English string, visibility unknown | Display setting name (e.g. ``"tool_progress"``, ``"show_reasoning"``). |
| feishu | gateway\display_config.py | 140 | English string, visibility unknown | display_cfg = user_config.get("display") or {} |
| feishu | gateway\display_config.py | 143 | English string, visibility unknown | platforms = display_cfg.get("platforms") or {} |
| feishu | gateway\display_config.py | 151 | English string, visibility unknown | if setting == "tool_progress": |
| feishu | gateway\display_config.py | 152 | English string, visibility unknown | legacy = display_cfg.get("tool_progress_overrides") |
| feishu | gateway\display_config.py | 161 | English string, visibility unknown | if setting != "streaming": |
| feishu | gateway\display_config.py | 187 | English string, visibility unknown | if setting == "tool_progress": |
| feishu | gateway\display_config.py | 189 | English string, visibility unknown | return "off" |
| feishu | gateway\display_config.py | 191 | English string, visibility unknown | return "all" |
| feishu | gateway\display_config.py | 193 | English string, visibility unknown | if setting in {"show_reasoning", "streaming"}: |
| feishu | gateway\display_config.py | 195 | English string, visibility unknown | return value.lower() in {"true", "1", "yes", "on"} |
| feishu | gateway\display_config.py | 197 | English string, visibility unknown | if setting == "cleanup_progress": |
| feishu | gateway\display_config.py | 199 | English string, visibility unknown | return value.lower() in {"true", "1", "yes", "on"} |
| feishu | gateway\display_config.py | 201 | English string, visibility unknown | if setting == "tool_preview_length": |
| feishu | gateway\platforms\feishu_comment_rules.py | 39 | English string, visibility unknown | _VALID_POLICIES = ("allowlist", "pairing") |
| feishu | gateway\platforms\feishu_comment_rules.py | 44 | English string, visibility unknown | """Per-document rule. ``None`` means 'inherit from lower tier'.""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 52 | English string, visibility unknown | """Top-level comment access config.""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 54 | English string, visibility unknown | policy: str = "pairing" |
| feishu | gateway\platforms\feishu_comment_rules.py | 61 | English string, visibility unknown | """Fully resolved rule after field-by-field fallback.""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 65 | English string, visibility unknown | match_source: str # e.g. "exact:docx:xxx" \| "wildcard" \| "top" \| "default" |
| feishu | gateway\platforms\feishu_comment_rules.py | 73 | English string, visibility unknown | """Generic mtime-based file cache. ``stat()`` per access, re-read only on change.""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 93 | English string, visibility unknown | with open(self._path, "r", encoding="utf-8") as f: |
| feishu | gateway\platforms\feishu_comment_rules.py | 115 | English string, visibility unknown | """Parse a list of strings into a frozenset; return None if key absent.""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 124 | English string, visibility unknown | enabled = raw.get("enabled") |
| feishu | gateway\platforms\feishu_comment_rules.py | 127 | English string, visibility unknown | policy = raw.get("policy") |
| feishu | gateway\platforms\feishu_comment_rules.py | 132 | English string, visibility unknown | allow_from = _parse_frozenset(raw.get("allow_from")) |
| feishu | gateway\platforms\feishu_comment_rules.py | 137 | English string, visibility unknown | """Load comment rules from disk (mtime-cached).""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 143 | English string, visibility unknown | raw_docs = raw.get("documents", {}) |
| feishu | gateway\platforms\feishu_comment_rules.py | 149 | English string, visibility unknown | policy = str(raw.get("policy", "pairing")).strip().lower() |
| feishu | gateway\platforms\feishu_comment_rules.py | 151 | English string, visibility unknown | policy = "pairing" |
| feishu | gateway\platforms\feishu_comment_rules.py | 154 | English string, visibility unknown | enabled=raw.get("enabled", True), |
| feishu | gateway\platforms\feishu_comment_rules.py | 156 | English string, visibility unknown | allow_from=_parse_frozenset(raw.get("allow_from")) or frozenset(), |
| feishu | gateway\platforms\feishu_comment_rules.py | 166 | English string, visibility unknown | """Check if any document rule key starts with 'wiki:'.""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 167 | English string, visibility unknown | return any(k.startswith("wiki:") for k in cfg.documents) |
| feishu | gateway\platforms\feishu_comment_rules.py | 176 | English string, visibility unknown | """Resolve effective rule: exact doc → wiki key → wildcard → top-level → defaults.""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 177 | English string, visibility unknown | exact_key = f"{file_type}:{file_token}" |
| feishu | gateway\platforms\feishu_comment_rules.py | 180 | English string, visibility unknown | exact_src = f"exact:{exact_key}" |
| feishu | gateway\platforms\feishu_comment_rules.py | 182 | English string, visibility unknown | wiki_key = f"wiki:{wiki_token}" |
| feishu | gateway\platforms\feishu_comment_rules.py | 184 | English string, visibility unknown | exact_src = f"exact:{wiki_key}" |
| feishu | gateway\platforms\feishu_comment_rules.py | 192 | English string, visibility unknown | layers.append((wildcard, "wildcard")) |
| feishu | gateway\platforms\feishu_comment_rules.py | 199 | English string, visibility unknown | return getattr(cfg, field_name), "top" |
| feishu | gateway\platforms\feishu_comment_rules.py | 201 | English string, visibility unknown | enabled, en_src = _pick("enabled") |
| feishu | gateway\platforms\feishu_comment_rules.py | 202 | English string, visibility unknown | policy, pol_src = _pick("policy") |
| feishu | gateway\platforms\feishu_comment_rules.py | 203 | English string, visibility unknown | allow_from, _ = _pick("allow_from") |
| feishu | gateway\platforms\feishu_comment_rules.py | 206 | English string, visibility unknown | priority_order = {"exact": 0, "wildcard": 1, "top": 2} |
| feishu | gateway\platforms\feishu_comment_rules.py | 225 | English string, visibility unknown | """Return set of approved user open_ids (mtime-cached).""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 227 | English string, visibility unknown | approved = data.get("approved", {}) |
| feishu | gateway\platforms\feishu_comment_rules.py | 238 | English string, visibility unknown | with open(tmp, "w", encoding="utf-8") as f: |
| feishu | gateway\platforms\feishu_comment_rules.py | 247 | English string, visibility unknown | """Add a user to the pairing-approved list. Returns True if newly added.""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 249 | English string, visibility unknown | approved = data.get("approved", {}) |
| feishu | gateway\platforms\feishu_comment_rules.py | 254 | English string, visibility unknown | approved[user_open_id] = {"approved_at": time.time()} |
| feishu | gateway\platforms\feishu_comment_rules.py | 255 | English string, visibility unknown | data["approved"] = approved |
| feishu | gateway\platforms\feishu_comment_rules.py | 261 | English string, visibility unknown | """Remove a user from the pairing-approved list. Returns True if removed.""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 263 | English string, visibility unknown | approved = data.get("approved", {}) |
| feishu | gateway\platforms\feishu_comment_rules.py | 269 | English string, visibility unknown | data["approved"] = approved |
| feishu | gateway\platforms\feishu_comment_rules.py | 275 | English string, visibility unknown | """Return the approved dict {user_open_id: {approved_at: ...}}.""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 277 | English string, visibility unknown | approved = data.get("approved", {}) |
| feishu | gateway\platforms\feishu_comment_rules.py | 286 | English string, visibility unknown | """Check if user passes the resolved rule's policy gate.""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 289 | English string, visibility unknown | if rule.policy == "pairing": |
| feishu | gateway\platforms\feishu_comment_rules.py | 315 | English string, visibility unknown | parts.append(f"enabled={rule.enabled}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 317 | English string, visibility unknown | parts.append(f"policy={rule.policy}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 319 | English string, visibility unknown | parts.append(f"allow_from={sorted(rule.allow_from)}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 327 | English string, visibility unknown | ts = meta.get("approved_at", 0) |
| feishu | gateway\platforms\feishu_comment_rules.py | 360 | mixed Chinese and English, visibility unknown | "用法: python -m gateway.platforms.feishu_comment_rules <command> [args]\n" |
| feishu | gateway\platforms\feishu_comment_rules.py | 363 | mixed Chinese and English, visibility unknown | " status 显示规则配置和配对状态\n" |
| feishu | gateway\platforms\feishu_comment_rules.py | 364 | mixed Chinese and English, visibility unknown | " check <fileType:token> <user> 模拟访问检查\n" |
| feishu | gateway\platforms\feishu_comment_rules.py | 365 | mixed Chinese and English, visibility unknown | " pairing add <user_open_id> 添加已配对用户\n" |
| feishu | gateway\platforms\feishu_comment_rules.py | 366 | mixed Chinese and English, visibility unknown | " pairing remove <user_open_id> 移除已配对用户\n" |
| feishu | gateway\platforms\feishu_comment_rules.py | 367 | mixed Chinese and English, visibility unknown | " pairing list 列出已配对用户\n" |
| feishu | gateway\platforms\feishu_comment_rules.py | 381 | English string, visibility unknown | if cmd == "status": |
| feishu | gateway\platforms\feishu_comment_rules.py | 384 | English string, visibility unknown | elif cmd == "check": |
| feishu | gateway\platforms\feishu_comment_rules.py | 390 | English string, visibility unknown | elif cmd == "pairing": |
| feishu | gateway\platforms\feishu_comment_rules.py | 395 | English string, visibility unknown | if sub == "add": |
| feishu | gateway\platforms\feishu_comment_rules.py | 403 | English string, visibility unknown | elif sub == "remove": |
| feishu | gateway\platforms\feishu_comment_rules.py | 411 | English string, visibility unknown | elif sub == "list": |
| feishu | gateway\platforms\feishu_comment_rules.py | 427 | English string, visibility unknown | if __name__ == "__main__": |
| feishu | gateway\platforms\feishu_comment.py | 4 | English string, visibility unknown | Processes ``drive.notice.comment_add_v1`` events and interacts with the |
| feishu | gateway\platforms\feishu_comment.py | 38 | English string, visibility unknown | """Build a lark_oapi BaseRequest.""" |
| feishu | gateway\platforms\feishu_comment.py | 68 | English string, visibility unknown | code = getattr(response, "code", None) |
| feishu | gateway\platforms\feishu_comment.py | 69 | English string, visibility unknown | msg = getattr(response, "msg", "") |
| feishu | gateway\platforms\feishu_comment.py | 72 | English string, visibility unknown | raw = getattr(response, "raw", None) |
| feishu | gateway\platforms\feishu_comment.py | 73 | English string, visibility unknown | if raw and hasattr(raw, "content"): |
| feishu | gateway\platforms\feishu_comment.py | 76 | English string, visibility unknown | data = body_json.get("data", {}) |
| feishu | gateway\platforms\feishu_comment.py | 80 | English string, visibility unknown | resp_data = getattr(response, "data", None) |
| feishu | gateway\platforms\feishu_comment.py | 83 | English string, visibility unknown | elif resp_data and hasattr(resp_data, "__dict__"): |
| feishu | gateway\platforms\feishu_comment.py | 87 | English string, visibility unknown | method, uri, code, msg, list(data.keys()) if data else "empty") |
| feishu | gateway\platforms\feishu_comment.py | 90 | English string, visibility unknown | raw = getattr(response, "raw", None) |
| feishu | gateway\platforms\feishu_comment.py | 92 | English string, visibility unknown | if raw and hasattr(raw, "content"): |
| feishu | gateway\platforms\feishu_comment.py | 104 | English string, visibility unknown | """Extract structured fields from a ``drive.notice.comment_add_v1`` payload. |
| feishu | gateway\platforms\feishu_comment.py | 106 | English string, visibility unknown | *data* may be a ``CustomizedEvent`` (WebSocket) whose ``.event`` is a dict, |
| feishu | gateway\platforms\feishu_comment.py | 109 | English string, visibility unknown | Returns a flat dict with the relevant fields, or ``None`` when the |
| feishu | gateway\platforms\feishu_comment.py | 113 | English string, visibility unknown | event = getattr(data, "event", None) |
| feishu | gateway\platforms\feishu_comment.py | 119 | English string, visibility unknown | vars(event) if hasattr(event, "__dict__") else {} |
| feishu | gateway\platforms\feishu_comment.py | 123 | English string, visibility unknown | notice_meta = evt.get("notice_meta") or {} |
| feishu | gateway\platforms\feishu_comment.py | 125 | English string, visibility unknown | notice_meta = vars(notice_meta) if hasattr(notice_meta, "__dict__") else {} |
| feishu | gateway\platforms\feishu_comment.py | 127 | English string, visibility unknown | from_user = notice_meta.get("from_user_id") or {} |
| feishu | gateway\platforms\feishu_comment.py | 129 | English string, visibility unknown | from_user = vars(from_user) if hasattr(from_user, "__dict__") else {} |
| feishu | gateway\platforms\feishu_comment.py | 131 | English string, visibility unknown | to_user = notice_meta.get("to_user_id") or {} |
| feishu | gateway\platforms\feishu_comment.py | 133 | English string, visibility unknown | to_user = vars(to_user) if hasattr(to_user, "__dict__") else {} |
| feishu | gateway\platforms\feishu_comment.py | 136 | English string, visibility unknown | "event_id": str(evt.get("event_id") or ""), |
| feishu | gateway\platforms\feishu_comment.py | 137 | English string, visibility unknown | "comment_id": str(evt.get("comment_id") or ""), |
| feishu | gateway\platforms\feishu_comment.py | 138 | English string, visibility unknown | "reply_id": str(evt.get("reply_id") or ""), |
| feishu | gateway\platforms\feishu_comment.py | 139 | English string, visibility unknown | "is_mentioned": bool(evt.get("is_mentioned")), |
| feishu | gateway\platforms\feishu_comment.py | 140 | English string, visibility unknown | "timestamp": str(evt.get("timestamp") or ""), |
| feishu | gateway\platforms\feishu_comment.py | 141 | English string, visibility unknown | "file_token": str(notice_meta.get("file_token") or ""), |
| feishu | gateway\platforms\feishu_comment.py | 142 | English string, visibility unknown | "file_type": str(notice_meta.get("file_type") or ""), |
| feishu | gateway\platforms\feishu_comment.py | 143 | English string, visibility unknown | "notice_type": str(notice_meta.get("notice_type") or ""), |
| feishu | gateway\platforms\feishu_comment.py | 144 | English string, visibility unknown | "from_open_id": str(from_user.get("open_id") or ""), |
| feishu | gateway\platforms\feishu_comment.py | 145 | English string, visibility unknown | "to_open_id": str(to_user.get("open_id") or ""), |
| feishu | gateway\platforms\feishu_comment.py | 153 | English string, visibility unknown | _REACTION_URI = "/open-apis/drive/v2/files/:file_token/comments/reaction" |
| feishu | gateway\platforms\feishu_comment.py | 166 | English string, visibility unknown | Uses the Drive v2 ``update_reaction`` endpoint:: |
| feishu | gateway\platforms\feishu_comment.py | 170 | English string, visibility unknown | Returns ``True`` on success, ``False`` on failure (errors are logged). |
| feishu | gateway\platforms\feishu_comment.py | 179 | English string, visibility unknown | "action": "add", |
| feishu | gateway\platforms\feishu_comment.py | 180 | English string, visibility unknown | "reply_id": reply_id, |
| feishu | gateway\platforms\feishu_comment.py | 181 | English string, visibility unknown | "reaction_type": reaction_type, |
| feishu | gateway\platforms\feishu_comment.py | 186 | English string, visibility unknown | paths={"file_token": file_token}, |
| feishu | gateway\platforms\feishu_comment.py | 187 | English string, visibility unknown | queries=[("file_type", file_type)], |
| feishu | gateway\platforms\feishu_comment.py | 200 | English string, visibility unknown | "file=%s:%s reply=%s", |
| feishu | gateway\platforms\feishu_comment.py | 219 | English string, visibility unknown | "action": "delete", |
| feishu | gateway\platforms\feishu_comment.py | 220 | English string, visibility unknown | "reply_id": reply_id, |
| feishu | gateway\platforms\feishu_comment.py | 221 | English string, visibility unknown | "reaction_type": reaction_type, |
| feishu | gateway\platforms\feishu_comment.py | 226 | English string, visibility unknown | paths={"file_token": file_token}, |
| feishu | gateway\platforms\feishu_comment.py | 227 | English string, visibility unknown | queries=[("file_type", file_type)], |
| feishu | gateway\platforms\feishu_comment.py | 240 | English string, visibility unknown | "file=%s:%s reply=%s", |
| feishu | gateway\platforms\feishu_comment.py | 250 | English string, visibility unknown | _BATCH_QUERY_META_URI = "/open-apis/drive/v1/metas/batch_query" |
| feishu | gateway\platforms\feishu_comment.py | 251 | English string, visibility unknown | _BATCH_QUERY_COMMENT_URI = "/open-apis/drive/v1/files/:file_token/comments/batch_query" |
| feishu | gateway\platforms\feishu_comment.py | 252 | English string, visibility unknown | _LIST_COMMENTS_URI = "/open-apis/drive/v1/files/:file_token/comments" |
| feishu | gateway\platforms\feishu_comment.py | 253 | English string, visibility unknown | _LIST_REPLIES_URI = "/open-apis/drive/v1/files/:file_token/comments/:comment_id/replies" |
| feishu | gateway\platforms\feishu_comment.py | 254 | English string, visibility unknown | _REPLY_COMMENT_URI = "/open-apis/drive/v1/files/:file_token/comments/:comment_id/replies" |
| feishu | gateway\platforms\feishu_comment.py | 255 | English string, visibility unknown | _ADD_COMMENT_URI = "/open-apis/drive/v1/files/:file_token/new_comments" |
| feishu | gateway\platforms\feishu_comment.py | 266 | English string, visibility unknown | "request_docs": [{"doc_token": file_token, "doc_type": file_type}], |
| feishu | gateway\platforms\feishu_comment.py | 267 | English string, visibility unknown | "with_url": True, |
| feishu | gateway\platforms\feishu_comment.py | 277 | English string, visibility unknown | metas = data.get("metas", []) |
| feishu | gateway\platforms\feishu_comment.py | 282 | English string, visibility unknown | if isinstance(data.get("metas"), dict): |
| feishu | gateway\platforms\feishu_comment.py | 283 | English string, visibility unknown | meta = data["metas"].get(file_token, {}) |
| feishu | gateway\platforms\feishu_comment.py | 291 | English string, visibility unknown | "title": meta.get("title", ""), |
| feishu | gateway\platforms\feishu_comment.py | 292 | English string, visibility unknown | "url": meta.get("url", ""), |
| feishu | gateway\platforms\feishu_comment.py | 293 | English string, visibility unknown | "doc_type": meta.get("doc_type", file_type), |
| feishu | gateway\platforms\feishu_comment.py | 295 | English string, visibility unknown | logger.info("[Feishu-Comment] query_document_meta: title=%s url=%s", |
| feishu | gateway\platforms\feishu_comment.py | 296 | English string, visibility unknown | result["title"], result["url"][:80] if result["url"] else "") |
| feishu | gateway\platforms\feishu_comment.py | 311 | English string, visibility unknown | Returns the comment dict with fields like ``is_whole``, ``quote``, |
| feishu | gateway\platforms\feishu_comment.py | 312 | English string, visibility unknown | ``reply_list``, etc. Empty dict on failure. |
| feishu | gateway\platforms\feishu_comment.py | 319 | English string, visibility unknown | paths={"file_token": file_token}, |
| feishu | gateway\platforms\feishu_comment.py | 321 | English string, visibility unknown | ("file_type", file_type), |
| feishu | gateway\platforms\feishu_comment.py | 322 | English string, visibility unknown | ("user_id_type", "open_id"), |
| feishu | gateway\platforms\feishu_comment.py | 324 | English string, visibility unknown | body={"comment_ids": [comment_id]}, |
| feishu | gateway\platforms\feishu_comment.py | 341 | English string, visibility unknown | # Response: {"items": [{"comment_id": "...", ...}]} |
| feishu | gateway\platforms\feishu_comment.py | 342 | English string, visibility unknown | items = data.get("items", []) |
| feishu | gateway\platforms\feishu_comment.py | 347 | English string, visibility unknown | item.get("is_whole"), |
| feishu | gateway\platforms\feishu_comment.py | 348 | English string, visibility unknown | (item.get("quote", "") or "")[:60], |
| feishu | gateway\platforms\feishu_comment.py | 349 | English string, visibility unknown | len(item.get("reply_list", {}).get("replies", [])) if isinstance(item.get("reply_list"), dict) else "?") |
| feishu | gateway\platforms\feishu_comment.py | 358 | English string, visibility unknown | """List all whole-document comments (paginated, up to 500).""" |
| feishu | gateway\platforms\feishu_comment.py | 365 | English string, visibility unknown | ("file_type", file_type), |
| feishu | gateway\platforms\feishu_comment.py | 366 | English string, visibility unknown | ("is_whole", "true"), |
| feishu | gateway\platforms\feishu_comment.py | 367 | English string, visibility unknown | ("page_size", "100"), |
| feishu | gateway\platforms\feishu_comment.py | 368 | English string, visibility unknown | ("user_id_type", "open_id"), |
| feishu | gateway\platforms\feishu_comment.py | 371 | English string, visibility unknown | queries.append(("page_token", page_token)) |
| feishu | gateway\platforms\feishu_comment.py | 375 | English string, visibility unknown | paths={"file_token": file_token}, |
| feishu | gateway\platforms\feishu_comment.py | 382 | English string, visibility unknown | items = data.get("items", []) |
| feishu | gateway\platforms\feishu_comment.py | 388 | English string, visibility unknown | if not data.get("has_more"): |
| feishu | gateway\platforms\feishu_comment.py | 390 | English string, visibility unknown | page_token = data.get("page_token", "") |
| feishu | gateway\platforms\feishu_comment.py | 416 | English string, visibility unknown | ("file_type", file_type), |
| feishu | gateway\platforms\feishu_comment.py | 417 | English string, visibility unknown | ("page_size", "100"), |
| feishu | gateway\platforms\feishu_comment.py | 418 | English string, visibility unknown | ("user_id_type", "open_id"), |
| feishu | gateway\platforms\feishu_comment.py | 421 | English string, visibility unknown | queries.append(("page_token", page_token)) |
| feishu | gateway\platforms\feishu_comment.py | 425 | English string, visibility unknown | paths={"file_token": file_token, "comment_id": comment_id}, |
| feishu | gateway\platforms\feishu_comment.py | 433 | English string, visibility unknown | items = data.get("items", []) |
| feishu | gateway\platforms\feishu_comment.py | 437 | English string, visibility unknown | if not data.get("has_more"): |
| feishu | gateway\platforms\feishu_comment.py | 439 | English string, visibility unknown | page_token = data.get("page_token", "") |
| feishu | gateway\platforms\feishu_comment.py | 446 | English string, visibility unknown | found = any(r.get("reply_id") == expect_reply_id for r in all_replies) |
| feishu | gateway\platforms\feishu_comment.py | 467 | English string, visibility unknown | return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") |
| feishu | gateway\platforms\feishu_comment.py | 475 | English string, visibility unknown | Returns ``(success, code)``. |
| feishu | gateway\platforms\feishu_comment.py | 478 | English string, visibility unknown | logger.info("[Feishu-Comment] reply_to_comment: comment_id=%s text=%s", |
| feishu | gateway\platforms\feishu_comment.py | 481 | English string, visibility unknown | "content": { |
| feishu | gateway\platforms\feishu_comment.py | 482 | English string, visibility unknown | "elements": [ |
| feishu | gateway\platforms\feishu_comment.py | 483 | English string, visibility unknown | {"type": "text_run", "text_run": {"text": text}}, |
| feishu | gateway\platforms\feishu_comment.py | 490 | English string, visibility unknown | paths={"file_token": file_token, "comment_id": comment_id}, |
| feishu | gateway\platforms\feishu_comment.py | 491 | English string, visibility unknown | queries=[("file_type", file_type)], |
| feishu | gateway\platforms\feishu_comment.py | 509 | English string, visibility unknown | Returns ``True`` on success. |
| feishu | gateway\platforms\feishu_comment.py | 512 | English string, visibility unknown | logger.info("[Feishu-Comment] add_whole_comment: file_token=%s text=%s", |
| feishu | gateway\platforms\feishu_comment.py | 515 | English string, visibility unknown | "file_type": file_type, |
| feishu | gateway\platforms\feishu_comment.py | 516 | English string, visibility unknown | "reply_elements": [ |
| feishu | gateway\platforms\feishu_comment.py | 517 | English string, visibility unknown | {"type": "text", "text": text}, |
| feishu | gateway\platforms\feishu_comment.py | 523 | English string, visibility unknown | paths={"file_token": file_token}, |
| feishu | gateway\platforms\feishu_comment.py | 537 | English string, visibility unknown | """Split text into chunks for delivery, preferring line breaks.""" |
| feishu | gateway\platforms\feishu_comment.py | 603 | English string, visibility unknown | """Extract plain text from a comment reply's content structure.""" |
| feishu | gateway\platforms\feishu_comment.py | 604 | English string, visibility unknown | content = reply.get("content", {}) |
| feishu | gateway\platforms\feishu_comment.py | 611 | English string, visibility unknown | elements = content.get("elements", []) |
| feishu | gateway\platforms\feishu_comment.py | 614 | English string, visibility unknown | if elem.get("type") == "text_run": |
| feishu | gateway\platforms\feishu_comment.py | 615 | English string, visibility unknown | text_run = elem.get("text_run", {}) |
| feishu | gateway\platforms\feishu_comment.py | 616 | English string, visibility unknown | parts.append(text_run.get("text", "")) |
| feishu | gateway\platforms\feishu_comment.py | 617 | English string, visibility unknown | elif elem.get("type") == "docs_link": |
| feishu | gateway\platforms\feishu_comment.py | 618 | English string, visibility unknown | docs_link = elem.get("docs_link", {}) |
| feishu | gateway\platforms\feishu_comment.py | 619 | English string, visibility unknown | parts.append(docs_link.get("url", "")) |
| feishu | gateway\platforms\feishu_comment.py | 620 | English string, visibility unknown | elif elem.get("type") == "person": |
| feishu | gateway\platforms\feishu_comment.py | 621 | English string, visibility unknown | person = elem.get("person", {}) |
| feishu | gateway\platforms\feishu_comment.py | 635 | English string, visibility unknown | """Extract semantic text from a reply, stripping self @mentions and extra whitespace.""" |
| feishu | gateway\platforms\feishu_comment.py | 636 | English string, visibility unknown | content = reply.get("content", {}) |
| feishu | gateway\platforms\feishu_comment.py | 643 | English string, visibility unknown | elements = content.get("elements", []) |
| feishu | gateway\platforms\feishu_comment.py | 646 | English string, visibility unknown | if elem.get("type") == "person": |
| feishu | gateway\platforms\feishu_comment.py | 647 | English string, visibility unknown | person = elem.get("person", {}) |
| feishu | gateway\platforms\feishu_comment.py | 652 | English string, visibility unknown | parts.append(f"@{uid}") |
| feishu | gateway\platforms\feishu_comment.py | 653 | English string, visibility unknown | elif elem.get("type") == "text_run": |
| feishu | gateway\platforms\feishu_comment.py | 654 | English string, visibility unknown | text_run = elem.get("text_run", {}) |
| feishu | gateway\platforms\feishu_comment.py | 655 | English string, visibility unknown | parts.append(text_run.get("text", "")) |
| feishu | gateway\platforms\feishu_comment.py | 656 | English string, visibility unknown | elif elem.get("type") == "docs_link": |
| feishu | gateway\platforms\feishu_comment.py | 657 | English string, visibility unknown | docs_link = elem.get("docs_link", {}) |
| feishu | gateway\platforms\feishu_comment.py | 658 | English string, visibility unknown | parts.append(docs_link.get("url", "")) |
| feishu | gateway\platforms\feishu_comment.py | 659 | English string, visibility unknown | return " ".join("".join(parts).split()).strip() |
| feishu | gateway\platforms\feishu_comment.py | 671 | English string, visibility unknown | r"/(?P<doc_type>wiki\|doc\|docx\|sheet\|sheets\|slides\|mindnote\|bitable\|base\|file)" |
| feishu | gateway\platforms\feishu_comment.py | 672 | English string, visibility unknown | r"/(?P<token>[A-Za-z0-9_-]{10,40})" |
| feishu | gateway\platforms\feishu_comment.py | 675 | English string, visibility unknown | _WIKI_GET_NODE_URI = "/open-apis/wiki/v2/spaces/get_node" |
| feishu | gateway\platforms\feishu_comment.py | 681 | English string, visibility unknown | Returns list of ``{"url": "...", "doc_type": "...", "token": "..."}`` dicts. |
| feishu | gateway\platforms\feishu_comment.py | 686 | English string, visibility unknown | content = reply.get("content", {}) |
| feishu | gateway\platforms\feishu_comment.py | 692 | English string, visibility unknown | for elem in content.get("elements", []): |
| feishu | gateway\platforms\feishu_comment.py | 693 | English string, visibility unknown | if elem.get("type") not in {"docs_link", "link"}: |
| feishu | gateway\platforms\feishu_comment.py | 695 | English string, visibility unknown | link_data = elem.get("docs_link") or elem.get("link") or {} |
| feishu | gateway\platforms\feishu_comment.py | 696 | English string, visibility unknown | url = link_data.get("url", "") |
| feishu | gateway\platforms\feishu_comment.py | 702 | English string, visibility unknown | doc_type = m.group("doc_type") |
| feishu | gateway\platforms\feishu_comment.py | 703 | English string, visibility unknown | token = m.group("token") |
| feishu | gateway\platforms\feishu_comment.py | 707 | English string, visibility unknown | links.append({"url": url, "doc_type": doc_type, "token": token}) |
| feishu | gateway\platforms\feishu_comment.py | 721 | English string, visibility unknown | queries=[("token", obj_token), ("obj_type", obj_type)], |
| feishu | gateway\platforms\feishu_comment.py | 724 | English string, visibility unknown | node = data.get("node", {}) |
| feishu | gateway\platforms\feishu_comment.py | 725 | English string, visibility unknown | wiki_token = node.get("node_token", "") |
| feishu | gateway\platforms\feishu_comment.py | 738 | English string, visibility unknown | Mutates entries in *links* in-place: replaces ``doc_type`` and ``token`` |
| feishu | gateway\platforms\feishu_comment.py | 741 | English string, visibility unknown | wiki_links = [l for l in links if l["doc_type"] == "wiki"] |
| feishu | gateway\platforms\feishu_comment.py | 746 | English string, visibility unknown | wiki_token = link["token"] |
| feishu | gateway\platforms\feishu_comment.py | 749 | English string, visibility unknown | queries=[("token", wiki_token)], |
| feishu | gateway\platforms\feishu_comment.py | 752 | English string, visibility unknown | node = data.get("node", {}) |
| feishu | gateway\platforms\feishu_comment.py | 753 | English string, visibility unknown | resolved_type = node.get("obj_type", "") |
| feishu | gateway\platforms\feishu_comment.py | 754 | English string, visibility unknown | resolved_token = node.get("obj_token", "") |
| feishu | gateway\platforms\feishu_comment.py | 760 | English string, visibility unknown | link["resolved_type"] = resolved_type |
| feishu | gateway\platforms\feishu_comment.py | 761 | English string, visibility unknown | link["resolved_token"] = resolved_token |
| feishu | gateway\platforms\feishu_comment.py | 763 | English string, visibility unknown | logger.warning("[Feishu-Comment] Wiki resolve returned empty: %s", wiki_token) |
| feishu | gateway\platforms\feishu_comment.py | 773 | English string, visibility unknown | """Format resolved document links for prompt embedding.""" |
| feishu | gateway\platforms\feishu_comment.py | 776 | English string, visibility unknown | lines = ["", "Referenced documents in comments:"] |
| feishu | gateway\platforms\feishu_comment.py | 778 | English string, visibility unknown | rtype = link.get("resolved_type", link["doc_type"]) |
| feishu | gateway\platforms\feishu_comment.py | 779 | English string, visibility unknown | rtoken = link.get("resolved_token", link["token"]) |
| feishu | gateway\platforms\feishu_comment.py | 781 | English string, visibility unknown | suffix = " (same as current document)" if is_current else "" |
| feishu | gateway\platforms\feishu_comment.py | 782 | English string, visibility unknown | lines.append(f"- {rtype}:{rtoken}{suffix} ({link['url'][:80]})") |
| feishu | gateway\platforms\feishu_comment.py | 796 | English string, visibility unknown | """Truncate text for prompt embedding.""" |
| feishu | gateway\platforms\feishu_comment.py | 878 | English string, visibility unknown | Do not show your reasoning process. Do not start with "I will", "Let me", or "I'll first". |
| feishu | gateway\platforms\feishu_comment.py | 899 | English string, visibility unknown | """Build the prompt for a local (quoted-text) comment.""" |
| feishu | gateway\platforms\feishu_comment.py | 903 | English string, visibility unknown | f'The user added a reply in "{doc_title}".', |
| feishu | gateway\platforms\feishu_comment.py | 904 | English string, visibility unknown | f'Current user comment text: "{_truncate(target_reply_text)}"', |
| feishu | gateway\platforms\feishu_comment.py | 905 | English string, visibility unknown | f'Original comment text: "{_truncate(root_comment_text)}"', |
| feishu | gateway\platforms\feishu_comment.py | 906 | English string, visibility unknown | f'Quoted content: "{_truncate(quote_text, 500)}"', |
| feishu | gateway\platforms\feishu_comment.py | 907 | English string, visibility unknown | "This comment mentioned you (@mention is for routing, not task content).", |
| feishu | gateway\platforms\feishu_comment.py | 908 | English string, visibility unknown | f"Document link: {doc_url}", |
| feishu | gateway\platforms\feishu_comment.py | 909 | English string, visibility unknown | "Current commented document:", |
| feishu | gateway\platforms\feishu_comment.py | 910 | English string, visibility unknown | f"- file_type={file_type}", |
| feishu | gateway\platforms\feishu_comment.py | 911 | English string, visibility unknown | f"- file_token={file_token}", |
| feishu | gateway\platforms\feishu_comment.py | 912 | English string, visibility unknown | f"- comment_id={comment_id}", |
| feishu | gateway\platforms\feishu_comment.py | 914 | English string, visibility unknown | f"Current comment card timeline ({len(selected)}/{len(timeline)} entries):", |
| feishu | gateway\platforms\feishu_comment.py | 942 | English string, visibility unknown | """Build the prompt for a whole-document comment.""" |
| feishu | gateway\platforms\feishu_comment.py | 946 | English string, visibility unknown | f'The user added a comment in "{doc_title}".', |
| feishu | gateway\platforms\feishu_comment.py | 947 | English string, visibility unknown | f'Current user comment text: "{_truncate(comment_text)}"', |
| feishu | gateway\platforms\feishu_comment.py | 948 | English string, visibility unknown | "This is a whole-document comment.", |
| feishu | gateway\platforms\feishu_comment.py | 949 | English string, visibility unknown | "This comment mentioned you (@mention is for routing, not task content).", |
| feishu | gateway\platforms\feishu_comment.py | 950 | English string, visibility unknown | f"Document link: {doc_url}", |
| feishu | gateway\platforms\feishu_comment.py | 951 | English string, visibility unknown | "Current commented document:", |
| feishu | gateway\platforms\feishu_comment.py | 952 | English string, visibility unknown | f"- file_type={file_type}", |
| feishu | gateway\platforms\feishu_comment.py | 953 | English string, visibility unknown | f"- file_token={file_token}", |
| feishu | gateway\platforms\feishu_comment.py | 955 | English string, visibility unknown | f"Whole-document comment timeline ({len(selected)}/{len(timeline)} entries):", |
| feishu | gateway\platforms\feishu_comment.py | 1007 | English string, visibility unknown | _session_cache: Dict[str, Dict] = {} # key -> {"messages": [...], "last_access": float} |
| feishu | gateway\platforms\feishu_comment.py | 1011 | English string, visibility unknown | return f"comment-doc:{file_type}:{file_token}" |
| feishu | gateway\platforms\feishu_comment.py | 1015 | English string, visibility unknown | """Load conversation history for a document session.""" |
| feishu | gateway\platforms\feishu_comment.py | 1021 | English string, visibility unknown | if _time.time() - entry["last_access"] > _SESSION_TTL_S: |
| feishu | gateway\platforms\feishu_comment.py | 1025 | English string, visibility unknown | entry["last_access"] = _time.time() |
| feishu | gateway\platforms\feishu_comment.py | 1026 | English string, visibility unknown | return list(entry["messages"]) |
| feishu | gateway\platforms\feishu_comment.py | 1030 | English string, visibility unknown | """Save conversation history for a document session (keeps last N messages).""" |
| feishu | gateway\platforms\feishu_comment.py | 1034 | English string, visibility unknown | if m.get("role") in {"user", "assistant"} and m.get("content") |
| feishu | gateway\platforms\feishu_comment.py | 1041 | English string, visibility unknown | "messages": cleaned, |
| feishu | gateway\platforms\feishu_comment.py | 1042 | English string, visibility unknown | "last_access": _time.time(), |
| feishu | gateway\platforms\feishu_comment.py | 1076 | English string, visibility unknown | base_url=runtime_kwargs.get("base_url"), |
| feishu | gateway\platforms\feishu_comment.py | 1077 | English string, visibility unknown | api_key=runtime_kwargs.get("api_key"), |
| feishu | gateway\platforms\feishu_comment.py | 1079 | English string, visibility unknown | api_mode=runtime_kwargs.get("api_mode"), |
| feishu | gateway\platforms\feishu_comment.py | 1080 | English string, visibility unknown | credential_pool=runtime_kwargs.get("credential_pool"), |
| feishu | gateway\platforms\feishu_comment.py | 1085 | English string, visibility unknown | enabled_toolsets=["feishu_doc", "feishu_drive"], |
| feishu | gateway\platforms\feishu_comment.py | 1090 | English string, visibility unknown | response = (result.get("final_response") or "").strip() |
| feishu | gateway\platforms\feishu_comment.py | 1091 | English string, visibility unknown | api_calls = result.get("api_calls", 0) |
| feishu | gateway\platforms\feishu_comment.py | 1097 | English string, visibility unknown | new_messages = result.get("messages", []) |
| feishu | gateway\platforms\feishu_comment.py | 1117 | English string, visibility unknown | _ALLOWED_NOTICE_TYPES = {"add_comment", "add_reply"} |
| feishu | gateway\platforms\feishu_comment.py | 1139 | English string, visibility unknown | file_token = parsed["file_token"] |
| feishu | gateway\platforms\feishu_comment.py | 1140 | English string, visibility unknown | file_type = parsed["file_type"] |
| feishu | gateway\platforms\feishu_comment.py | 1141 | English string, visibility unknown | comment_id = parsed["comment_id"] |
| feishu | gateway\platforms\feishu_comment.py | 1142 | English string, visibility unknown | reply_id = parsed["reply_id"] |
| feishu | gateway\platforms\feishu_comment.py | 1143 | English string, visibility unknown | from_open_id = parsed["from_open_id"] |
| feishu | gateway\platforms\feishu_comment.py | 1144 | English string, visibility unknown | to_open_id = parsed["to_open_id"] |
| feishu | gateway\platforms\feishu_comment.py | 1145 | English string, visibility unknown | notice_type = parsed["notice_type"] |
| feishu | gateway\platforms\feishu_comment.py | 1173 | English string, visibility unknown | if rule.match_source in {"wildcard", "top"} and has_wiki_keys(comments_cfg): |
| feishu | gateway\platforms\feishu_comment.py | 1207 | mixed Chinese and English, visibility unknown | doc_title = doc_meta.get("title", "未命名文档") |
| feishu | gateway\platforms\feishu_comment.py | 1208 | English string, visibility unknown | doc_url = doc_meta.get("url", "") |
| feishu | gateway\platforms\feishu_comment.py | 1209 | English string, visibility unknown | is_whole = bool(comment_detail.get("is_whole")) |
| feishu | gateway\platforms\feishu_comment.py | 1212 | English string, visibility unknown | "[Feishu-Comment] Comment context: title=%s is_whole=%s", |
| feishu | gateway\platforms\feishu_comment.py | 1228 | English string, visibility unknown | reply_list = wc.get("reply_list", {}) |
| feishu | gateway\platforms\feishu_comment.py | 1234 | English string, visibility unknown | replies = reply_list.get("replies", []) |
| feishu | gateway\platforms\feishu_comment.py | 1254 | English string, visibility unknown | logger.info("[Feishu-Comment] Whole timeline: %d entries, current_idx=%d, self_idx=%d, text=%s", |
| feishu | gateway\platforms\feishu_comment.py | 1256 | English string, visibility unknown | current_text[:80] if current_text else "(empty)") |
| feishu | gateway\platforms\feishu_comment.py | 1261 | English string, visibility unknown | rl = wc.get("reply_list", {}) |
| feishu | gateway\platforms\feishu_comment.py | 1267 | English string, visibility unknown | all_raw_replies.extend(rl.get("replies", [])) |
| feishu | gateway\platforms\feishu_comment.py | 1294 | English string, visibility unknown | quote_text = comment_detail.get("quote", "") |
| feishu | gateway\platforms\feishu_comment.py | 1307 | English string, visibility unknown | rid = r.get("reply_id", "") |
| feishu | gateway\platforms\feishu_comment.py | 1321 | English string, visibility unknown | quote_text[:60] if quote_text else "(empty)", |
| feishu | gateway\platforms\feishu_comment.py | 1322 | English string, visibility unknown | root_text[:60] if root_text else "(empty)", |
| feishu | gateway\platforms\feishu_comment.py | 1323 | English string, visibility unknown | target_text[:60] if target_text else "(empty)") |
| feishu | gateway\platforms\feishu.py | 27 | English string, visibility unknown | requires the ``contact:user.employee_id:readonly`` |
| feishu | gateway\platforms\feishu.py | 35 | English string, visibility unknown | bot open_id — Returned by ``/bot/v3/info``. This is the bot's own |
| feishu | gateway\platforms\feishu.py | 37 | English string, visibility unknown | puts in ``mentions[].id.open_id`` when someone |
| feishu | gateway\platforms\feishu.py | 43 | English string, visibility unknown | Session-key participant isolation prefers ``union_id`` (via user_id_alt) |
| feishu | gateway\platforms\feishu.py | 140 | English string, visibility unknown | body=json.dumps(payload, ensure_ascii=False).encode("utf-8"), |
| feishu | gateway\platforms\feishu.py | 178 | English string, visibility unknown | _MENTION_RE = re.compile(r"@_user_\d+") |
| feishu | gateway\platforms\feishu.py | 185 | English string, visibility unknown | _IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"} |
| feishu | gateway\platforms\feishu.py | 186 | English string, visibility unknown | _AUDIO_EXTENSIONS = {".ogg", ".mp3", ".wav", ".m4a", ".aac", ".flac", ".opus", ".webm"} |
| feishu | gateway\platforms\feishu.py | 187 | English string, visibility unknown | _VIDEO_EXTENSIONS = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v", ".3gp"} |
| feishu | gateway\platforms\feishu.py | 189 | English string, visibility unknown | _FEISHU_IMAGE_UPLOAD_TYPE = "message" |
| feishu | gateway\platforms\feishu.py | 190 | English string, visibility unknown | _FEISHU_FILE_UPLOAD_TYPE = "stream" |
| feishu | gateway\platforms\feishu.py | 191 | English string, visibility unknown | _FEISHU_OPUS_UPLOAD_EXTENSIONS = {".ogg", ".opus"} |
| feishu | gateway\platforms\feishu.py | 192 | English string, visibility unknown | _FEISHU_MEDIA_UPLOAD_EXTENSIONS = {".mp4", ".mov", ".avi", ".m4v"} |
| feishu | gateway\platforms\feishu.py | 194 | English string, visibility unknown | ".pdf": "pdf", |
| feishu | gateway\platforms\feishu.py | 195 | English string, visibility unknown | ".doc": "doc", |
| feishu | gateway\platforms\feishu.py | 196 | English string, visibility unknown | ".docx": "doc", |
| feishu | gateway\platforms\feishu.py | 197 | English string, visibility unknown | ".xls": "xls", |
| feishu | gateway\platforms\feishu.py | 198 | English string, visibility unknown | ".xlsx": "xls", |
| feishu | gateway\platforms\feishu.py | 199 | English string, visibility unknown | ".ppt": "ppt", |
| feishu | gateway\platforms\feishu.py | 200 | English string, visibility unknown | ".pptx": "ppt", |
| feishu | gateway\platforms\feishu.py | 234 | English string, visibility unknown | "approve_once": "once", |
| feishu | gateway\platforms\feishu.py | 235 | English string, visibility unknown | "approve_session": "session", |
| feishu | gateway\platforms\feishu.py | 236 | English string, visibility unknown | "approve_always": "always", |
| feishu | gateway\platforms\feishu.py | 237 | English string, visibility unknown | "deny": "deny", |
| feishu | gateway\platforms\feishu.py | 240 | mixed Chinese and English, visibility unknown | "once": "已批准一次", |
| feishu | gateway\platforms\feishu.py | 241 | mixed Chinese and English, visibility unknown | "session": "本轮会话已批准", |
| feishu | gateway\platforms\feishu.py | 242 | mixed Chinese and English, visibility unknown | "always": "已永久批准", |
| feishu | gateway\platforms\feishu.py | 243 | mixed Chinese and English, visibility unknown | "deny": "已拒绝", |
| feishu | gateway\platforms\feishu.py | 252 | English string, visibility unknown | _FEISHU_REACTION_IN_PROGRESS = "Typing" |
| feishu | gateway\platforms\feishu.py | 253 | English string, visibility unknown | _FEISHU_REACTION_FAILURE = "CrossMark" |
| feishu | gateway\platforms\feishu.py | 268 | English string, visibility unknown | _REGISTRATION_PATH = "/oauth/v1/app/registration" |
| feishu | gateway\platforms\feishu.py | 287 | English string, visibility unknown | _MENTION_PLACEHOLDER_RE = re.compile(r"@_user_\d+") |
| feishu | gateway\platforms\feishu.py | 292 | English string, visibility unknown | "title", |
| feishu | gateway\platforms\feishu.py | 293 | English string, visibility unknown | "text", |
| feishu | gateway\platforms\feishu.py | 294 | English string, visibility unknown | "content", |
| feishu | gateway\platforms\feishu.py | 295 | English string, visibility unknown | "label", |
| feishu | gateway\platforms\feishu.py | 296 | English string, visibility unknown | "value", |
| feishu | gateway\platforms\feishu.py | 297 | English string, visibility unknown | "name", |
| feishu | gateway\platforms\feishu.py | 298 | English string, visibility unknown | "summary", |
| feishu | gateway\platforms\feishu.py | 299 | English string, visibility unknown | "subtitle", |
| feishu | gateway\platforms\feishu.py | 300 | English string, visibility unknown | "description", |
| feishu | gateway\platforms\feishu.py | 301 | English string, visibility unknown | "placeholder", |
| feishu | gateway\platforms\feishu.py | 302 | English string, visibility unknown | "hint", |
| feishu | gateway\platforms\feishu.py | 305 | English string, visibility unknown | "tag", |
| feishu | gateway\platforms\feishu.py | 306 | English string, visibility unknown | "type", |
| feishu | gateway\platforms\feishu.py | 307 | English string, visibility unknown | "msg_type", |
| feishu | gateway\platforms\feishu.py | 308 | English string, visibility unknown | "message_type", |
| feishu | gateway\platforms\feishu.py | 310 | English string, visibility unknown | "open_chat_id", |
| feishu | gateway\platforms\feishu.py | 311 | English string, visibility unknown | "share_chat_id", |
| feishu | gateway\platforms\feishu.py | 312 | English string, visibility unknown | "file_key", |
| feishu | gateway\platforms\feishu.py | 313 | English string, visibility unknown | "image_key", |
| feishu | gateway\platforms\feishu.py | 315 | English string, visibility unknown | "open_id", |
| feishu | gateway\platforms\feishu.py | 316 | English string, visibility unknown | "union_id", |
| feishu | gateway\platforms\feishu.py | 317 | English string, visibility unknown | "url", |
| feishu | gateway\platforms\feishu.py | 318 | English string, visibility unknown | "href", |
| feishu | gateway\platforms\feishu.py | 319 | English string, visibility unknown | "link", |
| feishu | gateway\platforms\feishu.py | 320 | English string, visibility unknown | "token", |
| feishu | gateway\platforms\feishu.py | 321 | English string, visibility unknown | "template", |
| feishu | gateway\platforms\feishu.py | 322 | English string, visibility unknown | "locale", |
| feishu | gateway\platforms\feishu.py | 330 | English string, visibility unknown | resource_type: str = "file" |
| feishu | gateway\platforms\feishu.py | 369 | English string, visibility unknown | preferred_message_type: str = "text" |
| feishu | gateway\platforms\feishu.py | 373 | English string, visibility unknown | relation_kind: str = "plain" |
| feishu | gateway\platforms\feishu.py | 410 | English string, visibility unknown | allow_bots: str = "none" # "none" \| "mentions" \| "all" |
| feishu | gateway\platforms\feishu.py | 412 | English string, visibility unknown | outbound_format: str = "auto" # "auto" \| "text" \| "post" \| "card" |
| feishu | gateway\platforms\feishu.py | 418 | English string, visibility unknown | """Per-group policy rule for controlling which users may interact with the bot.""" |
| feishu | gateway\platforms\feishu.py | 420 | English string, visibility unknown | policy: str # "open" \| "allowlist" \| "blacklist" \| "admin_only" \| "disabled" |
| feishu | gateway\platforms\feishu.py | 439 | English string, visibility unknown | "self_echo", |
| feishu | gateway\platforms\feishu.py | 440 | English string, visibility unknown | "self_ids_unknown", |
| feishu | gateway\platforms\feishu.py | 441 | English string, visibility unknown | "bots_disabled", |
| feishu | gateway\platforms\feishu.py | 442 | English string, visibility unknown | "bot_not_mentioned", |
| feishu | gateway\platforms\feishu.py | 443 | English string, visibility unknown | "group_policy_rejected", |
| feishu | gateway\platforms\feishu.py | 448 | English string, visibility unknown | # receive_v1 docs say {user, bot}; accept "app" defensively. |
| feishu | gateway\platforms\feishu.py | 449 | English string, visibility unknown | return getattr(sender, "sender_type", "") in {"bot", "app"} |
| feishu | gateway\platforms\feishu.py | 454 | English string, visibility unknown | sid = getattr(sender, "sender_id", None) |
| feishu | gateway\platforms\feishu.py | 459 | English string, visibility unknown | getattr(sid, "open_id", None), |
| feishu | gateway\platforms\feishu.py | 461 | English string, visibility unknown | getattr(sid, "union_id", None), |
| feishu | gateway\platforms\feishu.py | 477 | English string, visibility unknown | return value is True or value == 1 or value == "true" |
| feishu | gateway\platforms\feishu.py | 489 | English string, visibility unknown | body = f" {text} " if text.startswith("`") or text.endswith("`") else text |
| feishu | gateway\platforms\feishu.py | 490 | English string, visibility unknown | return f"{fence}{body}{fence}" |
| feishu | gateway\platforms\feishu.py | 494 | English string, visibility unknown | return language.strip().replace("\n", " ").replace("\r", " ") |
| feishu | gateway\platforms\feishu.py | 498 | English string, visibility unknown | text = str(element.get("text", "") or "") |
| feishu | gateway\platforms\feishu.py | 499 | English string, visibility unknown | style = element.get("style") |
| feishu | gateway\platforms\feishu.py | 502 | English string, visibility unknown | if _is_style_enabled(style_dict, "code"): |
| feishu | gateway\platforms\feishu.py | 508 | English string, visibility unknown | if _is_style_enabled(style_dict, "bold"): |
| feishu | gateway\platforms\feishu.py | 509 | English string, visibility unknown | rendered = f"**{rendered}**" |
| feishu | gateway\platforms\feishu.py | 510 | English string, visibility unknown | if _is_style_enabled(style_dict, "italic"): |
| feishu | gateway\platforms\feishu.py | 511 | English string, visibility unknown | rendered = f"*{rendered}*" |
| feishu | gateway\platforms\feishu.py | 512 | English string, visibility unknown | if _is_style_enabled(style_dict, "underline"): |
| feishu | gateway\platforms\feishu.py | 513 | English string, visibility unknown | rendered = f"<u>{rendered}</u>" |
| feishu | gateway\platforms\feishu.py | 514 | English string, visibility unknown | if _is_style_enabled(style_dict, "strikethrough"): |
| feishu | gateway\platforms\feishu.py | 515 | English string, visibility unknown | rendered = f"~~{rendered}~~" |
| feishu | gateway\platforms\feishu.py | 521 | English string, visibility unknown | str(element.get("language", "") or "") or str(element.get("lang", "") or "") |
| feishu | gateway\platforms\feishu.py | 524 | English string, visibility unknown | str(element.get("text", "") or "") or str(element.get("content", "") or "") |
| feishu | gateway\platforms\feishu.py | 526 | English string, visibility unknown | trailing_newline = "" if code.endswith("\n") else "\n" |
| feishu | gateway\platforms\feishu.py | 527 | English string, visibility unknown | return f"```{language}\n{code}{trailing_newline}```" |
| feishu | gateway\platforms\feishu.py | 539 | English string, visibility unknown | plain = _MARKDOWN_LINK_RE.sub(lambda m: f"{m.group(1)} ({m.group(2).strip()})", plain) |
| feishu | gateway\platforms\feishu.py | 549 | English string, visibility unknown | """Coerce value to int with optional default and minimum constraint.""" |
| feishu | gateway\platforms\feishu.py | 572 | English string, visibility unknown | "content": rows, |
| feishu | gateway\platforms\feishu.py | 588 | English string, visibility unknown | "config": { |
| feishu | gateway\platforms\feishu.py | 589 | English string, visibility unknown | "wide_screen_mode": True, |
| feishu | gateway\platforms\feishu.py | 590 | English string, visibility unknown | "enable_forward": True, |
| feishu | gateway\platforms\feishu.py | 592 | English string, visibility unknown | "header": { |
| feishu | gateway\platforms\feishu.py | 593 | English string, visibility unknown | "template": "blue", |
| feishu | gateway\platforms\feishu.py | 596 | English string, visibility unknown | "elements": [ |
| feishu | gateway\platforms\feishu.py | 598 | English string, visibility unknown | "tag": "markdown", |
| feishu | gateway\platforms\feishu.py | 599 | English string, visibility unknown | "content": content or " ", |
| feishu | gateway\platforms\feishu.py | 611 | English string, visibility unknown | "config": { |
| feishu | gateway\platforms\feishu.py | 612 | English string, visibility unknown | "wide_screen_mode": True, |
| feishu | gateway\platforms\feishu.py | 613 | English string, visibility unknown | "enable_forward": False, |
| feishu | gateway\platforms\feishu.py | 615 | English string, visibility unknown | "header": { |
| feishu | gateway\platforms\feishu.py | 616 | English string, visibility unknown | "template": "green", |
| feishu | gateway\platforms\feishu.py | 619 | English string, visibility unknown | "elements": [ |
| feishu | gateway\platforms\feishu.py | 621 | English string, visibility unknown | "tag": "markdown", |
| feishu | gateway\platforms\feishu.py | 622 | English string, visibility unknown | "content": content or " ", |
| feishu | gateway\platforms\feishu.py | 641 | English string, visibility unknown | return [[{"tag": "md", "text": content}]] |
| feishu | gateway\platforms\feishu.py | 653 | English string, visibility unknown | rows.append([{"tag": "md", "text": segment}]) |
| feishu | gateway\platforms\feishu.py | 676 | English string, visibility unknown | return rows or [[{"tag": "md", "text": content}]] |
| feishu | gateway\platforms\feishu.py | 696 | English string, visibility unknown | for row in resolved.get("content", []) or []: |
| feishu | gateway\platforms\feishu.py | 722 | English string, visibility unknown | wrapped = payload.get("post") |
| feishu | gateway\platforms\feishu.py | 750 | English string, visibility unknown | content = candidate.get("content") |
| feishu | gateway\platforms\feishu.py | 754 | English string, visibility unknown | "title": str(candidate.get("title", "") or ""), |
| feishu | gateway\platforms\feishu.py | 755 | English string, visibility unknown | "content": content, |
| feishu | gateway\platforms\feishu.py | 770 | English string, visibility unknown | tag = str(element.get("tag", "")).strip().lower() |
| feishu | gateway\platforms\feishu.py | 771 | English string, visibility unknown | if tag == "text": |
| feishu | gateway\platforms\feishu.py | 774 | English string, visibility unknown | href = str(element.get("href", "")).strip() |
| feishu | gateway\platforms\feishu.py | 779 | English string, visibility unknown | return f"[{escaped_label}]({href})" if href else escaped_label |
| feishu | gateway\platforms\feishu.py | 784 | English string, visibility unknown | if placeholder == "@_all": |
| feishu | gateway\platforms\feishu.py | 787 | English string, visibility unknown | if mentions_map is not None and "@_all" not in mentions_map: |
| feishu | gateway\platforms\feishu.py | 788 | English string, visibility unknown | mentions_map["@_all"] = FeishuMentionRef(is_all=True) |
| feishu | gateway\platforms\feishu.py | 789 | English string, visibility unknown | return "@all" |
| feishu | gateway\platforms\feishu.py | 794 | mixed Chinese and English, visibility unknown | display_name = str(element.get("user_name", "")).strip() or "用户" |
| feishu | gateway\platforms\feishu.py | 795 | English string, visibility unknown | return f"@{_escape_markdown_text(display_name)}" |
| feishu | gateway\platforms\feishu.py | 796 | English string, visibility unknown | if tag in {"img", "image"}: |
| feishu | gateway\platforms\feishu.py | 797 | English string, visibility unknown | image_key = str(element.get("image_key", "")).strip() |
| feishu | gateway\platforms\feishu.py | 800 | English string, visibility unknown | alt = str(element.get("text", "")).strip() or str(element.get("alt", "")).strip() |
| feishu | gateway\platforms\feishu.py | 802 | English string, visibility unknown | if tag in {"media", "file", "audio", "video"}: |
| feishu | gateway\platforms\feishu.py | 803 | English string, visibility unknown | file_key = str(element.get("file_key", "")).strip() |
| feishu | gateway\platforms\feishu.py | 805 | English string, visibility unknown | str(element.get("file_name", "")).strip() |
| feishu | gateway\platforms\feishu.py | 806 | English string, visibility unknown | or str(element.get("title", "")).strip() |
| feishu | gateway\platforms\feishu.py | 807 | English string, visibility unknown | or str(element.get("text", "")).strip() |
| feishu | gateway\platforms\feishu.py | 814 | English string, visibility unknown | resource_type=tag if tag in {"audio", "video"} else "file", |
| feishu | gateway\platforms\feishu.py | 818 | English string, visibility unknown | if tag in {"emotion", "emoji"}: |
| feishu | gateway\platforms\feishu.py | 820 | mixed Chinese and English, visibility unknown | return f":{_escape_markdown_text(label)}:" if label else "[表情]" |
| feishu | gateway\platforms\feishu.py | 823 | English string, visibility unknown | if tag in {"hr", "divider"}: |
| feishu | gateway\platforms\feishu.py | 825 | English string, visibility unknown | if tag == "code": |
| feishu | gateway\platforms\feishu.py | 826 | English string, visibility unknown | code = str(element.get("text", "") or "") or str(element.get("content", "") or "") |
| feishu | gateway\platforms\feishu.py | 828 | English string, visibility unknown | if tag in {"code_block", "pre"}: |
| feishu | gateway\platforms\feishu.py | 832 | English string, visibility unknown | for key in ("text", "title", "content", "children", "elements"): |
| feishu | gateway\platforms\feishu.py | 883 | English string, visibility unknown | if normalized_type == "text": |
| feishu | gateway\platforms\feishu.py | 884 | English string, visibility unknown | text = str(payload.get("text", "") or "") |
| feishu | gateway\platforms\feishu.py | 887 | English string, visibility unknown | if "@_all" in text and "@_all" not in mentions_map: |
| feishu | gateway\platforms\feishu.py | 888 | English string, visibility unknown | mentions_map["@_all"] = FeishuMentionRef(is_all=True) |
| feishu | gateway\platforms\feishu.py | 894 | English string, visibility unknown | if normalized_type == "post": |
| feishu | gateway\platforms\feishu.py | 904 | English string, visibility unknown | relation_kind="post", |
| feishu | gateway\platforms\feishu.py | 907 | English string, visibility unknown | if normalized_type == "image": |
| feishu | gateway\platforms\feishu.py | 908 | English string, visibility unknown | image_key = str(payload.get("image_key", "") or "").strip() |
| feishu | gateway\platforms\feishu.py | 910 | English string, visibility unknown | str(payload.get("text", "") or "") |
| feishu | gateway\platforms\feishu.py | 911 | English string, visibility unknown | or str(payload.get("alt", "") or "") |
| feishu | gateway\platforms\feishu.py | 918 | English string, visibility unknown | preferred_message_type="photo", |
| feishu | gateway\platforms\feishu.py | 920 | English string, visibility unknown | relation_kind="image", |
| feishu | gateway\platforms\feishu.py | 923 | English string, visibility unknown | if normalized_type in {"file", "audio", "media"}: |
| feishu | gateway\platforms\feishu.py | 929 | English string, visibility unknown | preferred_message_type="audio" if normalized_type == "audio" else "document", |
| feishu | gateway\platforms\feishu.py | 932 | English string, visibility unknown | metadata={"placeholder_text": placeholder}, |
| feishu | gateway\platforms\feishu.py | 935 | English string, visibility unknown | if normalized_type == "merge_forward": |
| feishu | gateway\platforms\feishu.py | 937 | English string, visibility unknown | if normalized_type == "share_chat": |
| feishu | gateway\platforms\feishu.py | 939 | English string, visibility unknown | if normalized_type in {"interactive", "card"}: |
| feishu | gateway\platforms\feishu.py | 949 | English string, visibility unknown | return {"text": raw_content} |
| feishu | gateway\platforms\feishu.py | 950 | English string, visibility unknown | return parsed if isinstance(parsed, dict) else {"content": parsed} |
| feishu | gateway\platforms\feishu.py | 955 | English string, visibility unknown | payload.get("title"), |
| feishu | gateway\platforms\feishu.py | 956 | English string, visibility unknown | payload.get("summary"), |
| feishu | gateway\platforms\feishu.py | 957 | English string, visibility unknown | payload.get("preview"), |
| feishu | gateway\platforms\feishu.py | 958 | English string, visibility unknown | _find_first_text(payload, keys=("title", "summary", "preview", "description")), |
| feishu | gateway\platforms\feishu.py | 967 | English string, visibility unknown | raw_type="merge_forward", |
| feishu | gateway\platforms\feishu.py | 969 | English string, visibility unknown | relation_kind="merge_forward", |
| feishu | gateway\platforms\feishu.py | 970 | English string, visibility unknown | metadata={"entry_count": len(entries), "title": title}, |
| feishu | gateway\platforms\feishu.py | 976 | English string, visibility unknown | payload.get("chat_name"), |
| feishu | gateway\platforms\feishu.py | 977 | English string, visibility unknown | payload.get("name"), |
| feishu | gateway\platforms\feishu.py | 978 | English string, visibility unknown | payload.get("title"), |
| feishu | gateway\platforms\feishu.py | 979 | English string, visibility unknown | _find_first_text(payload, keys=("chat_name", "name", "title")), |
| feishu | gateway\platforms\feishu.py | 983 | English string, visibility unknown | payload.get("open_chat_id"), |
| feishu | gateway\platforms\feishu.py | 984 | English string, visibility unknown | payload.get("share_chat_id"), |
| feishu | gateway\platforms\feishu.py | 988 | mixed Chinese and English, visibility unknown | lines.append(f"共享聊天: {chat_name}") |
| feishu | gateway\platforms\feishu.py | 992 | mixed Chinese and English, visibility unknown | lines.append(f"聊天 ID: {share_id}") |
| feishu | gateway\platforms\feishu.py | 995 | English string, visibility unknown | raw_type="share_chat", |
| feishu | gateway\platforms\feishu.py | 997 | English string, visibility unknown | relation_kind="share_chat", |
| feishu | gateway\platforms\feishu.py | 1003 | English string, visibility unknown | card_payload = payload.get("card") if isinstance(payload.get("card"), dict) else payload |
| feishu | gateway\platforms\feishu.py | 1006 | English string, visibility unknown | payload.get("title"), |
| feishu | gateway\platforms\feishu.py | 1007 | English string, visibility unknown | _find_first_text(card_payload, keys=("title", "summary", "subtitle")), |
| feishu | gateway\platforms\feishu.py | 1019 | English string, visibility unknown | lines.append(f"Actions: {', '.join(actions)}") |
| feishu | gateway\platforms\feishu.py | 1025 | English string, visibility unknown | relation_kind="interactive", |
| feishu | gateway\platforms\feishu.py | 1026 | English string, visibility unknown | metadata={"title": title, "actions": actions}, |
| feishu | gateway\platforms\feishu.py | 1037 | English string, visibility unknown | for key in ("messages", "items", "message_list", "records", "content"): |
| feishu | gateway\platforms\feishu.py | 1046 | English string, visibility unknown | entries.append(f"- {text}") |
| feishu | gateway\platforms\feishu.py | 1049 | English string, visibility unknown | item.get("sender_name"), |
| feishu | gateway\platforms\feishu.py | 1050 | English string, visibility unknown | item.get("user_name"), |
| feishu | gateway\platforms\feishu.py | 1051 | English string, visibility unknown | item.get("sender"), |
| feishu | gateway\platforms\feishu.py | 1052 | English string, visibility unknown | item.get("name"), |
| feishu | gateway\platforms\feishu.py | 1054 | English string, visibility unknown | nested_type = str(item.get("message_type", "") or item.get("msg_type", "")).strip().lower() |
| feishu | gateway\platforms\feishu.py | 1055 | English string, visibility unknown | if nested_type == "post": |
| feishu | gateway\platforms\feishu.py | 1056 | English string, visibility unknown | body = parse_feishu_post_payload(item.get("content") or item).text_content |
| feishu | gateway\platforms\feishu.py | 1059 | English string, visibility unknown | item.get("text"), |
| feishu | gateway\platforms\feishu.py | 1060 | English string, visibility unknown | item.get("summary"), |
| feishu | gateway\platforms\feishu.py | 1061 | English string, visibility unknown | item.get("preview"), |
| feishu | gateway\platforms\feishu.py | 1062 | English string, visibility unknown | item.get("content"), |
| feishu | gateway\platforms\feishu.py | 1063 | English string, visibility unknown | _find_first_text(item, keys=("text", "content", "summary", "preview", "title")), |
| feishu | gateway\platforms\feishu.py | 1067 | English string, visibility unknown | entries.append(f"- {sender}: {body}") |
| feishu | gateway\platforms\feishu.py | 1069 | English string, visibility unknown | entries.append(f"- {body}") |
| feishu | gateway\platforms\feishu.py | 1084 | English string, visibility unknown | tag = str(item.get("tag", "") or item.get("type", "")).strip().lower() |
| feishu | gateway\platforms\feishu.py | 1085 | English string, visibility unknown | if tag not in {"button", "select_static", "overflow", "date_picker", "picker"}: |
| feishu | gateway\platforms\feishu.py | 1088 | English string, visibility unknown | item.get("text"), |
| feishu | gateway\platforms\feishu.py | 1089 | English string, visibility unknown | item.get("name"), |
| feishu | gateway\platforms\feishu.py | 1090 | English string, visibility unknown | item.get("value"), |
| feishu | gateway\platforms\feishu.py | 1091 | English string, visibility unknown | _find_first_text(item, keys=("text", "content", "name", "value")), |
| feishu | gateway\platforms\feishu.py | 1109 | English string, visibility unknown | tag = str(value.get("tag", "") or value.get("type", "")).strip().lower() |
| feishu | gateway\platforms\feishu.py | 1111 | English string, visibility unknown | "plain_text", |
| feishu | gateway\platforms\feishu.py | 1112 | English string, visibility unknown | "lark_md", |
| feishu | gateway\platforms\feishu.py | 1113 | English string, visibility unknown | "markdown", |
| feishu | gateway\platforms\feishu.py | 1114 | English string, visibility unknown | "note", |
| feishu | gateway\platforms\feishu.py | 1115 | English string, visibility unknown | "div", |
| feishu | gateway\platforms\feishu.py | 1116 | English string, visibility unknown | "column_set", |
| feishu | gateway\platforms\feishu.py | 1117 | English string, visibility unknown | "column", |
| feishu | gateway\platforms\feishu.py | 1118 | English string, visibility unknown | "action", |
| feishu | gateway\platforms\feishu.py | 1119 | English string, visibility unknown | "button", |
| feishu | gateway\platforms\feishu.py | 1120 | English string, visibility unknown | "select_static", |
| feishu | gateway\platforms\feishu.py | 1121 | English string, visibility unknown | "date_picker", |
| feishu | gateway\platforms\feishu.py | 1140 | English string, visibility unknown | file_key = str(payload.get("file_key", "") or "").strip() |
| feishu | gateway\platforms\feishu.py | 1142 | English string, visibility unknown | payload.get("file_name"), |
| feishu | gateway\platforms\feishu.py | 1143 | English string, visibility unknown | payload.get("title"), |
| feishu | gateway\platforms\feishu.py | 1144 | English string, visibility unknown | payload.get("text"), |
| feishu | gateway\platforms\feishu.py | 1146 | English string, visibility unknown | effective_type = resource_type if resource_type in {"audio", "video"} else "file" |
| feishu | gateway\platforms\feishu.py | 1158 | English string, visibility unknown | header = payload.get("header") |
| feishu | gateway\platforms\feishu.py | 1163 | English string, visibility unknown | return _first_non_empty_text(title.get("content"), title.get("text"), title.get("name")) |
| feishu | gateway\platforms\feishu.py | 1212 | English string, visibility unknown | def _sub(match: "re.Match[str]") -> str: |
| feishu | gateway\platforms\feishu.py | 1218 | English string, visibility unknown | return f"@{name}" |
| feishu | gateway\platforms\feishu.py | 1221 | English string, visibility unknown | cleaned = cleaned.replace("@_all", "@all") |
| feishu | gateway\platforms\feishu.py | 1222 | English string, visibility unknown | cleaned = cleaned.replace("\r\n", "\n").replace("\r", "\n") |
| feishu | gateway\platforms\feishu.py | 1223 | English string, visibility unknown | cleaned = "\n".join(_WHITESPACE_RE.sub(" ", line).strip() for line in cleaned.split("\n")) |
| feishu | gateway\platforms\feishu.py | 1224 | English string, visibility unknown | cleaned = "\n".join(line for line in cleaned.split("\n") if line) |
| feishu | gateway\platforms\feishu.py | 1251 | English string, visibility unknown | id_type = str(getattr(mention, "id_type", "") or "").lower() |
| feishu | gateway\platforms\feishu.py | 1252 | English string, visibility unknown | if id_type == "open_id": |
| feishu | gateway\platforms\feishu.py | 1260 | English string, visibility unknown | str(getattr(mention_id, "open_id", "") or ""), |
| feishu | gateway\platforms\feishu.py | 1271 | English string, visibility unknown | key = str(getattr(mention, "key", "") or "") |
| feishu | gateway\platforms\feishu.py | 1274 | English string, visibility unknown | if key == "@_all": |
| feishu | gateway\platforms\feishu.py | 1298 | English string, visibility unknown | parts.append("@all") |
| feishu | gateway\platforms\feishu.py | 1300 | English string, visibility unknown | parts.append(f"{ref.name or 'unknown'} (open_id={ref.open_id})") |
| feishu | gateway\platforms\feishu.py | 1302 | English string, visibility unknown | parts.append(ref.name or "unknown") |
| feishu | gateway\platforms\feishu.py | 1303 | English string, visibility unknown | return f"[Mentioned: {', '.join(parts)}]" if parts else "" |
| feishu | gateway\platforms\feishu.py | 1312 | English string, visibility unknown | # mid-sentence references ("don't @Bot again") stay intact. |
| feishu | gateway\platforms\feishu.py | 1317 | English string, visibility unknown | f"@{ref.name or ref.open_id or 'user'}" |
| feishu | gateway\platforms\feishu.py | 1361 | English string, visibility unknown | original_configure = getattr(ws_client, "_configure", None) |
| feishu | gateway\platforms\feishu.py | 1365 | English string, visibility unknown | setattr(ws_client, "_reconnect_nonce", adapter._ws_reconnect_nonce) |
| feishu | gateway\platforms\feishu.py | 1366 | English string, visibility unknown | setattr(ws_client, "_reconnect_interval", adapter._ws_reconnect_interval) |
| feishu | gateway\platforms\feishu.py | 1368 | English string, visibility unknown | setattr(ws_client, "_ping_interval", adapter._ws_ping_interval) |
| feishu | gateway\platforms\feishu.py | 1373 | English string, visibility unknown | if adapter._ws_ping_interval is not None and "ping_interval" not in kwargs: |
| feishu | gateway\platforms\feishu.py | 1374 | English string, visibility unknown | kwargs["ping_interval"] = adapter._ws_ping_interval |
| feishu | gateway\platforms\feishu.py | 1375 | English string, visibility unknown | if adapter._ws_ping_timeout is not None and "ping_timeout" not in kwargs: |
| feishu | gateway\platforms\feishu.py | 1376 | English string, visibility unknown | kwargs["ping_timeout"] = adapter._ws_ping_timeout |
| feishu | gateway\platforms\feishu.py | 1388 | English string, visibility unknown | setattr(ws_client, "_configure", _configure_with_overrides) |
| feishu | gateway\platforms\feishu.py | 1397 | English string, visibility unknown | setattr(ws_client, "_configure", original_configure) |
| feishu | gateway\platforms\feishu.py | 1445 | English string, visibility unknown | "GetApplicationRequest": GetApplicationRequest, |
| feishu | gateway\platforms\feishu.py | 1446 | English string, visibility unknown | "CreateFileRequest": CreateFileRequest, |
| feishu | gateway\platforms\feishu.py | 1447 | English string, visibility unknown | "CreateFileRequestBody": CreateFileRequestBody, |
| feishu | gateway\platforms\feishu.py | 1448 | English string, visibility unknown | "CreateImageRequest": CreateImageRequest, |
| feishu | gateway\platforms\feishu.py | 1449 | English string, visibility unknown | "CreateImageRequestBody": CreateImageRequestBody, |
| feishu | gateway\platforms\feishu.py | 1450 | English string, visibility unknown | "CreateMessageRequest": CreateMessageRequest, |
| feishu | gateway\platforms\feishu.py | 1451 | English string, visibility unknown | "CreateMessageRequestBody": CreateMessageRequestBody, |
| feishu | gateway\platforms\feishu.py | 1452 | English string, visibility unknown | "GetChatRequest": GetChatRequest, |
| feishu | gateway\platforms\feishu.py | 1453 | English string, visibility unknown | "GetMessageRequest": GetMessageRequest, |
| feishu | gateway\platforms\feishu.py | 1454 | English string, visibility unknown | "GetMessageResourceRequest": GetMessageResourceRequest, |
| feishu | gateway\platforms\feishu.py | 1455 | English string, visibility unknown | "P2ImMessageMessageReadV1": P2ImMessageMessageReadV1, |
| feishu | gateway\platforms\feishu.py | 1456 | English string, visibility unknown | "ReplyMessageRequest": ReplyMessageRequest, |
| feishu | gateway\platforms\feishu.py | 1457 | English string, visibility unknown | "ReplyMessageRequestBody": ReplyMessageRequestBody, |
| feishu | gateway\platforms\feishu.py | 1458 | English string, visibility unknown | "UpdateMessageRequest": UpdateMessageRequest, |
| feishu | gateway\platforms\feishu.py | 1459 | English string, visibility unknown | "UpdateMessageRequestBody": UpdateMessageRequestBody, |
| feishu | gateway\platforms\feishu.py | 1460 | English string, visibility unknown | "AccessTokenType": AccessTokenType, |
| feishu | gateway\platforms\feishu.py | 1461 | English string, visibility unknown | "HttpMethod": HttpMethod, |
| feishu | gateway\platforms\feishu.py | 1464 | English string, visibility unknown | "BaseRequest": BaseRequest, |
| feishu | gateway\platforms\feishu.py | 1465 | English string, visibility unknown | "CallBackCard": CallBackCard, |
| feishu | gateway\platforms\feishu.py | 1466 | English string, visibility unknown | "P2CardActionTriggerResponse": P2CardActionTriggerResponse, |
| feishu | gateway\platforms\feishu.py | 1467 | English string, visibility unknown | "EventDispatcherHandler": EventDispatcherHandler, |
| feishu | gateway\platforms\feishu.py | 1468 | English string, visibility unknown | "FeishuWSClient": FeishuWSClient, |
| feishu | gateway\platforms\feishu.py | 1504 | English string, visibility unknown | self._dedup_state_path = get_hermes_home() / "feishu_seen_message_ids.json" |
| feishu | gateway\platforms\feishu.py | 1538 | English string, visibility unknown | self._pending_processing_reactions: "OrderedDict[str, str]" = OrderedDict() |
| feishu | gateway\platforms\feishu.py | 1544 | English string, visibility unknown | raw_group_rules = extra.get("group_rules", {}) |
| feishu | gateway\platforms\feishu.py | 1553 | English string, visibility unknown | if "require_mention" in rule_cfg: |
| feishu | gateway\platforms\feishu.py | 1554 | English string, visibility unknown | per_chat_require_mention = _to_boolean(rule_cfg.get("require_mention")) |
| feishu | gateway\platforms\feishu.py | 1556 | English string, visibility unknown | policy=str(rule_cfg.get("policy", "open")).strip().lower(), |
| feishu | gateway\platforms\feishu.py | 1557 | English string, visibility unknown | allowlist={str(u).strip() for u in rule_cfg.get("allowlist", []) if str(u).strip()}, |
| feishu | gateway\platforms\feishu.py | 1558 | English string, visibility unknown | blacklist={str(u).strip() for u in rule_cfg.get("blacklist", []) if str(u).strip()}, |
| feishu | gateway\platforms\feishu.py | 1563 | English string, visibility unknown | raw_admins = extra.get("admins", []) |
| feishu | gateway\platforms\feishu.py | 1567 | English string, visibility unknown | default_group_policy = str(extra.get("default_group_policy", "")).strip().lower() |
| feishu | gateway\platforms\feishu.py | 1572 | English string, visibility unknown | if allow_bots not in {"none", "mentions", "all"}: |
| feishu | gateway\platforms\feishu.py | 1577 | English string, visibility unknown | allow_bots = "none" |
| feishu | gateway\platforms\feishu.py | 1628 | English string, visibility unknown | ws_reconnect_nonce=_coerce_required_int(extra.get("ws_reconnect_nonce"), default=30, min_value=0), |
| feishu | gateway\platforms\feishu.py | 1629 | English string, visibility unknown | ws_reconnect_interval=_coerce_required_int(extra.get("ws_reconnect_interval"), default=120, min_value=1), |
| feishu | gateway\platforms\feishu.py | 1630 | English string, visibility unknown | ws_ping_interval=_coerce_int(extra.get("ws_ping_interval"), default=None, min_value=1), |
| feishu | gateway\platforms\feishu.py | 1631 | English string, visibility unknown | ws_ping_timeout=_coerce_int(extra.get("ws_ping_timeout"), default=None, min_value=1), |
| feishu | gateway\platforms\feishu.py | 1674 | English string, visibility unknown | if self._outbound_format not in {"auto", "text", "post", "card"}: |
| feishu | gateway\platforms\feishu.py | 1676 | English string, visibility unknown | self._outbound_format = "auto" |
| feishu | gateway\platforms\feishu.py | 1677 | English string, visibility unknown | self._card_mode = settings.card_mode or self._outbound_format == "card" |
| feishu | gateway\platforms\feishu.py | 1690 | English string, visibility unknown | lambda data: self._on_reaction_event("im.message.reaction.created_v1", data) |
| feishu | gateway\platforms\feishu.py | 1693 | English string, visibility unknown | lambda data: self._on_reaction_event("im.message.reaction.deleted_v1", data) |
| feishu | gateway\platforms\feishu.py | 1701 | English string, visibility unknown | "drive.notice.comment_add_v1", |
| feishu | gateway\platforms\feishu.py | 1715 | English string, visibility unknown | if self._connection_mode not in {"websocket", "webhook"}: |
| feishu | gateway\platforms\feishu.py | 1727 | English string, visibility unknown | metadata={"platform": self.platform.value}, |
| feishu | gateway\platforms\feishu.py | 1730 | English string, visibility unknown | owner_pid = existing.get("pid") if isinstance(existing, dict) else None |
| feishu | gateway\platforms\feishu.py | 1785 | English string, visibility unknown | logger.debug("[Feishu] Websocket thread exited with error: %s", exc, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 1814 | English string, visibility unknown | setattr(self._ws_client, "_auto_reconnect", False) |
| feishu | gateway\platforms\feishu.py | 1860 | English string, visibility unknown | if msg_type != "post" or not _POST_CONTENT_INVALID_RE.search(str(exc)): |
| feishu | gateway\platforms\feishu.py | 1865 | English string, visibility unknown | msg_type="text", |
| feishu | gateway\platforms\feishu.py | 1866 | English string, visibility unknown | payload=json.dumps({"text": _strip_markdown_to_plain_text(chunk)}, ensure_ascii=False), |
| feishu | gateway\platforms\feishu.py | 1871 | English string, visibility unknown | msg_type == "post" |
| feishu | gateway\platforms\feishu.py | 1873 | English string, visibility unknown | and _POST_CONTENT_INVALID_RE.search(str(getattr(response, "msg", "") or "")) |
| feishu | gateway\platforms\feishu.py | 1878 | English string, visibility unknown | msg_type="text", |
| feishu | gateway\platforms\feishu.py | 1879 | English string, visibility unknown | payload=json.dumps({"text": _strip_markdown_to_plain_text(chunk)}, ensure_ascii=False), |
| feishu | gateway\platforms\feishu.py | 1887 | English string, visibility unknown | logger.error("[Feishu] Send error: %s", exc, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 1909 | English string, visibility unknown | if not result.success and msg_type == "post" and _POST_CONTENT_INVALID_RE.search(result.error or ""): |
| feishu | gateway\platforms\feishu.py | 1912 | English string, visibility unknown | msg_type="text", |
| feishu | gateway\platforms\feishu.py | 1913 | English string, visibility unknown | content=json.dumps({"text": _strip_markdown_to_plain_text(content)}, ensure_ascii=False), |
| feishu | gateway\platforms\feishu.py | 1940 | English string, visibility unknown | msg_type="interactive", |
| feishu | gateway\platforms\feishu.py | 1947 | English string, visibility unknown | logger.error("[Feishu] Runtime footer card send error: %s", exc, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 1957 | English string, visibility unknown | The buttons carry ``hermes_action`` in their value dict so that |
| feishu | gateway\platforms\feishu.py | 1958 | English string, visibility unknown | ``_handle_card_action_event`` can intercept them and call |
| feishu | gateway\platforms\feishu.py | 1959 | English string, visibility unknown | ``resolve_gateway_approval()`` to unblock the waiting agent thread. |
| feishu | gateway\platforms\feishu.py | 1968 | English string, visibility unknown | def _btn(label: str, action_name: str, btn_type: str = "default") -> dict: |
| feishu | gateway\platforms\feishu.py | 1970 | English string, visibility unknown | "tag": "button", |
| feishu | gateway\platforms\feishu.py | 1971 | English string, visibility unknown | "text": {"tag": "plain_text", "content": label}, |
| feishu | gateway\platforms\feishu.py | 1972 | English string, visibility unknown | "type": btn_type, |
| feishu | gateway\platforms\feishu.py | 1973 | English string, visibility unknown | "value": {"hermes_action": action_name, "approval_id": approval_id}, |
| feishu | gateway\platforms\feishu.py | 1977 | English string, visibility unknown | "config": {"wide_screen_mode": True}, |
| feishu | gateway\platforms\feishu.py | 1978 | English string, visibility unknown | "header": { |
| feishu | gateway\platforms\feishu.py | 1980 | English string, visibility unknown | "template": "orange", |
| feishu | gateway\platforms\feishu.py | 1982 | English string, visibility unknown | "elements": [ |
| feishu | gateway\platforms\feishu.py | 1984 | English string, visibility unknown | "tag": "markdown", |
| feishu | gateway\platforms\feishu.py | 1988 | English string, visibility unknown | "tag": "action", |
| feishu | gateway\platforms\feishu.py | 1989 | English string, visibility unknown | "actions": [ |
| feishu | gateway\platforms\feishu.py | 1990 | mixed Chinese and English, visibility unknown | _btn("✅ 仅本次", "approve_once", "primary"), |
| feishu | gateway\platforms\feishu.py | 1991 | mixed Chinese and English, visibility unknown | _btn("✅ 本轮会话", "approve_session"), |
| feishu | gateway\platforms\feishu.py | 1992 | mixed Chinese and English, visibility unknown | _btn("✅ 永久允许", "approve_always"), |
| feishu | gateway\platforms\feishu.py | 1993 | mixed Chinese and English, visibility unknown | _btn("❌ 拒绝", "deny", "danger"), |
| feishu | gateway\platforms\feishu.py | 2002 | English string, visibility unknown | msg_type="interactive", |
| feishu | gateway\platforms\feishu.py | 2011 | English string, visibility unknown | "session_key": session_key, |
| feishu | gateway\platforms\feishu.py | 2022 | mixed Chinese and English, visibility unknown | default_hint = f"\n\n默认值: `{default}`" if default else "" |
| feishu | gateway\platforms\feishu.py | 2026 | English string, visibility unknown | "tag": "button", |
| feishu | gateway\platforms\feishu.py | 2027 | English string, visibility unknown | "text": {"tag": "plain_text", "content": label}, |
| feishu | gateway\platforms\feishu.py | 2028 | English string, visibility unknown | "type": btn_type, |
| feishu | gateway\platforms\feishu.py | 2029 | English string, visibility unknown | "value": { |
| feishu | gateway\platforms\feishu.py | 2030 | English string, visibility unknown | "hermes_update_prompt_action": answer, |
| feishu | gateway\platforms\feishu.py | 2031 | English string, visibility unknown | "update_prompt_id": prompt_id, |
| feishu | gateway\platforms\feishu.py | 2036 | English string, visibility unknown | "config": {"wide_screen_mode": True}, |
| feishu | gateway\platforms\feishu.py | 2037 | English string, visibility unknown | "header": { |
| feishu | gateway\platforms\feishu.py | 2039 | English string, visibility unknown | "template": "orange", |
| feishu | gateway\platforms\feishu.py | 2041 | English string, visibility unknown | "elements": [ |
| feishu | gateway\platforms\feishu.py | 2044 | English string, visibility unknown | "tag": "action", |
| feishu | gateway\platforms\feishu.py | 2045 | English string, visibility unknown | "actions": [ |
| feishu | gateway\platforms\feishu.py | 2046 | mixed Chinese and English, visibility unknown | _btn("✓ 是", "y", "primary"), |
| feishu | gateway\platforms\feishu.py | 2047 | mixed Chinese and English, visibility unknown | _btn("✗ 否", "n", "danger"), |
| feishu | gateway\platforms\feishu.py | 2058 | English string, visibility unknown | """Send an interactive update prompt with Yes/No buttons.""" |
| feishu | gateway\platforms\feishu.py | 2070 | English string, visibility unknown | msg_type="interactive", |
| feishu | gateway\platforms\feishu.py | 2079 | English string, visibility unknown | "session_key": session_key, |
| feishu | gateway\platforms\feishu.py | 2091 | English string, visibility unknown | icon = "❌" if choice == "deny" else "✅" |
| feishu | gateway\platforms\feishu.py | 2094 | English string, visibility unknown | "config": {"wide_screen_mode": True}, |
| feishu | gateway\platforms\feishu.py | 2095 | English string, visibility unknown | "header": { |
| feishu | gateway\platforms\feishu.py | 2097 | English string, visibility unknown | "template": "red" if choice == "deny" else "green", |
| feishu | gateway\platforms\feishu.py | 2099 | English string, visibility unknown | "elements": [ |
| feishu | gateway\platforms\feishu.py | 2101 | English string, visibility unknown | "tag": "markdown", |
| feishu | gateway\platforms\feishu.py | 2112 | English string, visibility unknown | "config": {"wide_screen_mode": True}, |
| feishu | gateway\platforms\feishu.py | 2113 | English string, visibility unknown | "header": { |
| feishu | gateway\platforms\feishu.py | 2115 | English string, visibility unknown | "template": "green" if yes else "red", |
| feishu | gateway\platforms\feishu.py | 2117 | English string, visibility unknown | "elements": [ |
| feishu | gateway\platforms\feishu.py | 2124 | English string, visibility unknown | response_path = get_hermes_home() / ".update_response" |
| feishu | gateway\platforms\feishu.py | 2125 | English string, visibility unknown | tmp_path = response_path.with_suffix(".tmp") |
| feishu | gateway\platforms\feishu.py | 2145 | English string, visibility unknown | outbound_message_type="audio", |
| feishu | gateway\platforms\feishu.py | 2184 | English string, visibility unknown | outbound_message_type="media", |
| feishu | gateway\platforms\feishu.py | 2200 | mixed Chinese and English, visibility unknown | return SendResult(success=False, error=f"图片文件不存在: {image_path}") |
| feishu | gateway\platforms\feishu.py | 2215 | English string, visibility unknown | image_key = self._extract_response_field(upload_response, "image_key") |
| feishu | gateway\platforms\feishu.py | 2220 | mixed Chinese and English, visibility unknown | override_error="飞书图片上传缺少 image_key", |
| feishu | gateway\platforms\feishu.py | 2226 | English string, visibility unknown | media_tag={"tag": "img", "image_key": image_key}, |
| feishu | gateway\platforms\feishu.py | 2230 | English string, visibility unknown | msg_type="post", |
| feishu | gateway\platforms\feishu.py | 2238 | English string, visibility unknown | msg_type="image", |
| feishu | gateway\platforms\feishu.py | 2239 | English string, visibility unknown | payload=json.dumps({"image_key": image_key}, ensure_ascii=False), |
| feishu | gateway\platforms\feishu.py | 2292 | English string, visibility unknown | default_ext=".gif", |
| feishu | gateway\platforms\feishu.py | 2293 | English string, visibility unknown | preferred_name="animation.gif", |
| feishu | gateway\platforms\feishu.py | 2319 | English string, visibility unknown | "type": "dm", |
| feishu | gateway\platforms\feishu.py | 2331 | English string, visibility unknown | if not response or getattr(response, "success", lambda: False)() is False: |
| feishu | gateway\platforms\feishu.py | 2332 | English string, visibility unknown | code = getattr(response, "code", "unknown") |
| feishu | gateway\platforms\feishu.py | 2333 | mixed Chinese and English, visibility unknown | msg = getattr(response, "msg", "会话查询失败") |
| feishu | gateway\platforms\feishu.py | 2337 | English string, visibility unknown | data = getattr(response, "data", None) |
| feishu | gateway\platforms\feishu.py | 2338 | English string, visibility unknown | raw_chat_type = str(getattr(data, "chat_type", "") or "").strip().lower() |
| feishu | gateway\platforms\feishu.py | 2342 | English string, visibility unknown | "type": self._map_chat_type(raw_chat_type), |
| feishu | gateway\platforms\feishu.py | 2343 | English string, visibility unknown | "raw_type": raw_chat_type or None, |
| feishu | gateway\platforms\feishu.py | 2393 | English string, visibility unknown | event = getattr(dropped, "event", None) |
| feishu | gateway\platforms\feishu.py | 2417 | English string, visibility unknown | Runs in a dedicated daemon thread. Polls ``_running`` and |
| feishu | gateway\platforms\feishu.py | 2418 | English string, visibility unknown | ``_loop_accepts_callbacks`` until events can be dispatched or the |
| feishu | gateway\platforms\feishu.py | 2420 | English string, visibility unknown | concurrent ``_on_message_event`` calls just append. |
| feishu | gateway\platforms\feishu.py | 2427 | English string, visibility unknown | if not getattr(self, "_running", True): |
| feishu | gateway\platforms\feishu.py | 2482 | English string, visibility unknown | "dropped %d queued inbound event(s)", |
| feishu | gateway\platforms\feishu.py | 2494 | English string, visibility unknown | """Shared inbound message handling for websocket and webhook transports.""" |
| feishu | gateway\platforms\feishu.py | 2495 | English string, visibility unknown | event = getattr(data, "event", None) |
| feishu | gateway\platforms\feishu.py | 2497 | English string, visibility unknown | sender = getattr(event, "sender", None) |
| feishu | gateway\platforms\feishu.py | 2498 | English string, visibility unknown | if not message or not sender or not getattr(sender, "sender_id", None): |
| feishu | gateway\platforms\feishu.py | 2512 | English string, visibility unknown | chat_type = getattr(message, "chat_type", "p2p") |
| feishu | gateway\platforms\feishu.py | 2516 | English string, visibility unknown | sender_id=getattr(sender, "sender_id", None), |
| feishu | gateway\platforms\feishu.py | 2523 | English string, visibility unknown | """Ignore read-receipt events that Hermes does not act on.""" |
| feishu | gateway\platforms\feishu.py | 2524 | English string, visibility unknown | event = getattr(data, "event", None) |
| feishu | gateway\platforms\feishu.py | 2530 | English string, visibility unknown | """Handle bot being added to a group chat.""" |
| feishu | gateway\platforms\feishu.py | 2531 | English string, visibility unknown | event = getattr(data, "event", None) |
| feishu | gateway\platforms\feishu.py | 2537 | English string, visibility unknown | """Handle bot being removed from a group chat.""" |
| feishu | gateway\platforms\feishu.py | 2538 | English string, visibility unknown | event = getattr(data, "event", None) |
| feishu | gateway\platforms\feishu.py | 2552 | English string, visibility unknown | Delegates to :mod:`gateway.platforms.feishu_comment` for parsing, |
| feishu | gateway\platforms\feishu.py | 2554 | English string, visibility unknown | ``run_coroutine_threadsafe`` pattern used by ``_on_message_event``. |
| feishu | gateway\platforms\feishu.py | 2568 | English string, visibility unknown | """Route user reactions on bot messages as synthetic text events.""" |
| feishu | gateway\platforms\feishu.py | 2569 | English string, visibility unknown | event = getattr(data, "event", None) |
| feishu | gateway\platforms\feishu.py | 2571 | English string, visibility unknown | operator_type = str(getattr(event, "operator_type", "") or "") |
| feishu | gateway\platforms\feishu.py | 2572 | English string, visibility unknown | reaction_type_obj = getattr(event, "reaction_type", None) |
| feishu | gateway\platforms\feishu.py | 2573 | English string, visibility unknown | emoji_type = str(getattr(reaction_type_obj, "emoji_type", "") or "") |
| feishu | gateway\platforms\feishu.py | 2587 | English string, visibility unknown | operator_type in {"bot", "app"} |
| feishu | gateway\platforms\feishu.py | 2590 | English string, visibility unknown | or bool(getattr(loop, "is_closed", lambda: False)()) |
| feishu | gateway\platforms\feishu.py | 2602 | English string, visibility unknown | For other card actions: delegates to ``_handle_card_action_event``. |
| feishu | gateway\platforms\feishu.py | 2609 | English string, visibility unknown | event = getattr(data, "event", None) |
| feishu | gateway\platforms\feishu.py | 2610 | English string, visibility unknown | action = getattr(event, "action", None) |
| feishu | gateway\platforms\feishu.py | 2611 | English string, visibility unknown | action_value = getattr(action, "value", {}) or {} |
| feishu | gateway\platforms\feishu.py | 2612 | English string, visibility unknown | hermes_action = action_value.get("hermes_action") if isinstance(action_value, dict) else None |
| feishu | gateway\platforms\feishu.py | 2614 | English string, visibility unknown | action_value.get("hermes_update_prompt_action") |
| feishu | gateway\platforms\feishu.py | 2634 | English string, visibility unknown | """Return True when the adapter loop can accept thread-safe submissions.""" |
| feishu | gateway\platforms\feishu.py | 2635 | English string, visibility unknown | return loop is not None and not bool(getattr(loop, "is_closed", lambda: False)()) |
| feishu | gateway\platforms\feishu.py | 2638 | English string, visibility unknown | """Schedule background work on the adapter loop with shared failure logging.""" |
| feishu | gateway\platforms\feishu.py | 2643 | English string, visibility unknown | log_message="[Feishu] Failed to schedule background callback work", |
| feishu | gateway\platforms\feishu.py | 2652 | English string, visibility unknown | """Return whether this card-action operator may answer gated prompts.""" |
| feishu | gateway\platforms\feishu.py | 2662 | English string, visibility unknown | """Schedule approval resolution and build the synchronous callback response.""" |
| feishu | gateway\platforms\feishu.py | 2663 | English string, visibility unknown | approval_id = action_value.get("approval_id") |
| feishu | gateway\platforms\feishu.py | 2667 | English string, visibility unknown | choice = _APPROVAL_CHOICE_MAP.get(action_value.get("hermes_action"), "deny") |
| feishu | gateway\platforms\feishu.py | 2669 | English string, visibility unknown | operator = getattr(event, "operator", None) |
| feishu | gateway\platforms\feishu.py | 2670 | English string, visibility unknown | open_id = str(getattr(operator, "open_id", "") or "") |
| feishu | gateway\platforms\feishu.py | 2681 | English string, visibility unknown | card.type = "raw" |
| feishu | gateway\platforms\feishu.py | 2687 | English string, visibility unknown | """Schedule update prompt resolution and build the synchronous callback response.""" |
| feishu | gateway\platforms\feishu.py | 2688 | English string, visibility unknown | prompt_id = action_value.get("update_prompt_id") |
| feishu | gateway\platforms\feishu.py | 2696 | English string, visibility unknown | answer = str(action_value.get("hermes_update_prompt_action", "") or "").strip().lower() |
| feishu | gateway\platforms\feishu.py | 2701 | English string, visibility unknown | operator = getattr(event, "operator", None) |
| feishu | gateway\platforms\feishu.py | 2702 | English string, visibility unknown | open_id = str(getattr(operator, "open_id", "") or "") |
| feishu | gateway\platforms\feishu.py | 2716 | English string, visibility unknown | card.type = "raw" |
| feishu | gateway\platforms\feishu.py | 2722 | English string, visibility unknown | """Pop approval state and unblock the waiting agent thread.""" |
| feishu | gateway\platforms\feishu.py | 2729 | English string, visibility unknown | count = resolve_gateway_approval(state["session_key"], choice) |
| feishu | gateway\platforms\feishu.py | 2732 | English string, visibility unknown | count, state["session_key"], choice, user_name, |
| feishu | gateway\platforms\feishu.py | 2738 | English string, visibility unknown | """Persist an update prompt answer for the detached update process.""" |
| feishu | gateway\platforms\feishu.py | 2747 | English string, visibility unknown | state["session_key"], answer, user_name, |
| feishu | gateway\platforms\feishu.py | 2753 | English string, visibility unknown | """Fetch the reacted-to message; if it was sent by this bot, emit a synthetic text event.""" |
| feishu | gateway\platforms\feishu.py | 2756 | English string, visibility unknown | event = getattr(data, "event", None) |
| feishu | gateway\platforms\feishu.py | 2765 | English string, visibility unknown | if not response or not getattr(response, "success", lambda: False)(): |
| feishu | gateway\platforms\feishu.py | 2767 | English string, visibility unknown | items = getattr(getattr(response, "data", None), "items", None) or [] |
| feishu | gateway\platforms\feishu.py | 2772 | English string, visibility unknown | # peer bots and us share sender_type="app" but differ on app_id. |
| feishu | gateway\platforms\feishu.py | 2773 | English string, visibility unknown | sender = getattr(msg, "sender", None) |
| feishu | gateway\platforms\feishu.py | 2777 | English string, visibility unknown | chat_type_raw = str(getattr(msg, "chat_type", "p2p") or "p2p") |
| feishu | gateway\platforms\feishu.py | 2785 | English string, visibility unknown | reaction_type_obj = getattr(event, "reaction_type", None) |
| feishu | gateway\platforms\feishu.py | 2788 | English string, visibility unknown | synthetic_text = f"reaction:{action}:{emoji_type}" |
| feishu | gateway\platforms\feishu.py | 2797 | English string, visibility unknown | user_name=sender_profile["user_name"], |
| feishu | gateway\platforms\feishu.py | 2799 | English string, visibility unknown | user_id_alt=sender_profile["user_id_alt"], |
| feishu | gateway\platforms\feishu.py | 2813 | English string, visibility unknown | """Return True if this card action token was already processed within the dedup window.""" |
| feishu | gateway\platforms\feishu.py | 2826 | English string, visibility unknown | event = getattr(data, "event", None) |
| feishu | gateway\platforms\feishu.py | 2827 | English string, visibility unknown | token = str(getattr(event, "token", "") or "") |
| feishu | gateway\platforms\feishu.py | 2832 | English string, visibility unknown | context = getattr(event, "context", None) |
| feishu | gateway\platforms\feishu.py | 2834 | English string, visibility unknown | operator = getattr(event, "operator", None) |
| feishu | gateway\platforms\feishu.py | 2835 | English string, visibility unknown | open_id = str(getattr(operator, "open_id", "") or "") |
| feishu | gateway\platforms\feishu.py | 2840 | English string, visibility unknown | action = getattr(event, "action", None) |
| feishu | gateway\platforms\feishu.py | 2841 | English string, visibility unknown | action_tag = str(getattr(action, "tag", "") or "button") |
| feishu | gateway\platforms\feishu.py | 2842 | English string, visibility unknown | action_value = getattr(action, "value", {}) or {} |
| feishu | gateway\platforms\feishu.py | 2844 | English string, visibility unknown | synthetic_text = f"/card {action_tag}" |
| feishu | gateway\platforms\feishu.py | 2847 | English string, visibility unknown | synthetic_text += f" {json.dumps(action_value, ensure_ascii=False)}" |
| feishu | gateway\platforms\feishu.py | 2857 | English string, visibility unknown | chat_type=self._resolve_source_chat_type(chat_info=chat_info, event_chat_type="group"), |
| feishu | gateway\platforms\feishu.py | 2859 | English string, visibility unknown | user_name=sender_profile["user_name"], |
| feishu | gateway\platforms\feishu.py | 2861 | English string, visibility unknown | user_id_alt=sender_profile["user_id_alt"], |
| feishu | gateway\platforms\feishu.py | 2879 | English string, visibility unknown | """Return (creating if needed) the per-chat asyncio.Lock for serial message processing.""" |
| feishu | gateway\platforms\feishu.py | 2906 | English string, visibility unknown | """Return the reaction_id on success, else None. The id is needed later for deletion.""" |
| feishu | gateway\platforms\feishu.py | 2916 | English string, visibility unknown | .reaction_type({"emoji_type": emoji_type}) |
| feishu | gateway\platforms\feishu.py | 2926 | English string, visibility unknown | if response and getattr(response, "success", lambda: False)(): |
| feishu | gateway\platforms\feishu.py | 2927 | English string, visibility unknown | data = getattr(response, "data", None) |
| feishu | gateway\platforms\feishu.py | 2928 | English string, visibility unknown | return getattr(data, "reaction_id", None) |
| feishu | gateway\platforms\feishu.py | 2933 | English string, visibility unknown | getattr(response, "code", None), |
| feishu | gateway\platforms\feishu.py | 2934 | English string, visibility unknown | getattr(response, "msg", None), |
| feishu | gateway\platforms\feishu.py | 2957 | English string, visibility unknown | if response and getattr(response, "success", lambda: False)(): |
| feishu | gateway\platforms\feishu.py | 2963 | English string, visibility unknown | getattr(response, "code", None), |
| feishu | gateway\platforms\feishu.py | 2964 | English string, visibility unknown | getattr(response, "msg", None), |
| feishu | gateway\platforms\feishu.py | 3007 | English string, visibility unknown | # Don't stack a second badge on top of a Typing we couldn't |
| feishu | gateway\platforms\feishu.py | 3008 | English string, visibility unknown | # remove — UI would read as both "working" and "done/failed" |
| feishu | gateway\platforms\feishu.py | 3035 | English string, visibility unknown | "over the last %.0fs", |
| feishu | gateway\platforms\feishu.py | 3047 | English string, visibility unknown | """Reset the anomaly counter for remote_ip after a successful request.""" |
| feishu | gateway\platforms\feishu.py | 3071 | English string, visibility unknown | # Guard runs post-strip so a pure "@Bot" message (stripped to "") is dropped. |
| feishu | gateway\platforms\feishu.py | 3079 | English string, visibility unknown | text = f"{hint}\n\n{text}" if text else hint |
| feishu | gateway\platforms\feishu.py | 3081 | English string, visibility unknown | thread_id = getattr(message, "thread_id", None) or getattr(message, "root_id", None) or None |
| feishu | gateway\platforms\feishu.py | 3083 | English string, visibility unknown | getattr(message, "parent_id", None) |
| feishu | gateway\platforms\feishu.py | 3084 | English string, visibility unknown | or getattr(message, "upper_message_id", None) |
| feishu | gateway\platforms\feishu.py | 3085 | English string, visibility unknown | or getattr(message, "root_id", None) |
| feishu | gateway\platforms\feishu.py | 3091 | English string, visibility unknown | getattr(sender_id, "open_id", None) |
| feishu | gateway\platforms\feishu.py | 3093 | English string, visibility unknown | or getattr(sender_id, "union_id", None) |
| feishu | gateway\platforms\feishu.py | 3094 | English string, visibility unknown | or "<unknown>" |
| feishu | gateway\platforms\feishu.py | 3097 | English string, visibility unknown | "[Feishu] Inbound %s message received: id=%s type=%s chat_id=%s sender=%s:%s text=%r media=%d", |
| feishu | gateway\platforms\feishu.py | 3098 | English string, visibility unknown | "dm" if chat_type == "p2p" else "group", |
| feishu | gateway\platforms\feishu.py | 3102 | English string, visibility unknown | "bot" if is_bot else "user", |
| feishu | gateway\platforms\feishu.py | 3116 | English string, visibility unknown | user_name=sender_profile["user_name"], |
| feishu | gateway\platforms\feishu.py | 3118 | English string, visibility unknown | user_id_alt=sender_profile["user_id_alt"], |
| feishu | gateway\platforms\feishu.py | 3160 | English string, visibility unknown | group_sessions_per_user=self.config.extra.get("group_sessions_per_user", True), |
| feishu | gateway\platforms\feishu.py | 3161 | English string, visibility unknown | thread_sessions_per_user=self.config.extra.get("thread_sessions_per_user", False), |
| feishu | gateway\platforms\feishu.py | 3163 | English string, visibility unknown | return f"{session_key}:media:{event.message_type.value}" |
| feishu | gateway\platforms\feishu.py | 3223 | English string, visibility unknown | ext = self._guess_remote_extension(image_url, default=".jpg") |
| feishu | gateway\platforms\feishu.py | 3243 | English string, visibility unknown | "User-Agent": "Mozilla/5.0 (compatible; HermesAgent/1.0)", |
| feishu | gateway\platforms\feishu.py | 3244 | English string, visibility unknown | "Accept": "*/*", |
| feishu | gateway\platforms\feishu.py | 3264 | English string, visibility unknown | ext = Path((url or "").split("?", 1)[0]).suffix.lower() |
| feishu | gateway\platforms\feishu.py | 3269 | English string, visibility unknown | candidate = Path((file_url or "").split("?", 1)[0]).name or default_name |
| feishu | gateway\platforms\feishu.py | 3272 | English string, visibility unknown | guessed = mimetypes.guess_extension((content_type or "").split(";", 1)[0].strip().lower() or "") or default_ext |
| feishu | gateway\platforms\feishu.py | 3273 | English string, visibility unknown | candidate = f"{candidate}{guessed}" |
| feishu | gateway\platforms\feishu.py | 3285 | English string, visibility unknown | remote_ip = (getattr(request, "remote", None) or "unknown") |
| feishu | gateway\platforms\feishu.py | 3288 | English string, visibility unknown | rate_key = f"{self._app_id}:{self._webhook_path}:{remote_ip}" |
| feishu | gateway\platforms\feishu.py | 3295 | English string, visibility unknown | headers = getattr(request, "headers", {}) or {} |
| feishu | gateway\platforms\feishu.py | 3303 | English string, visibility unknown | content_length = getattr(request, "content_length", None) |
| feishu | gateway\platforms\feishu.py | 3328 | English string, visibility unknown | payload = json.loads(body_bytes.decode("utf-8")) |
| feishu | gateway\platforms\feishu.py | 3335 | English string, visibility unknown | if payload.get("type") == "url_verification": |
| feishu | gateway\platforms\feishu.py | 3340 | English string, visibility unknown | header = payload.get("header") or {} |
| feishu | gateway\platforms\feishu.py | 3341 | English string, visibility unknown | incoming_token = str(header.get("token") or payload.get("token") or "") |
| feishu | gateway\platforms\feishu.py | 3344 | English string, visibility unknown | self._record_webhook_anomaly(remote_ip, "401-token") |
| feishu | gateway\platforms\feishu.py | 3350 | English string, visibility unknown | self._record_webhook_anomaly(remote_ip, "401-sig") |
| feishu | gateway\platforms\feishu.py | 3353 | English string, visibility unknown | if payload.get("encrypt"): |
| feishu | gateway\platforms\feishu.py | 3355 | English string, visibility unknown | self._record_webhook_anomaly(remote_ip, "400-encrypted") |
| feishu | gateway\platforms\feishu.py | 3393 | English string, visibility unknown | body_str = body_bytes.decode("utf-8", errors="replace") |
| feishu | gateway\platforms\feishu.py | 3394 | English string, visibility unknown | content = f"{timestamp}{nonce}{self._encrypt_key}{body_str}" |
| feishu | gateway\platforms\feishu.py | 3395 | English string, visibility unknown | computed = hashlib.sha256(content.encode("utf-8")).hexdigest() |
| feishu | gateway\platforms\feishu.py | 3404 | English string, visibility unknown | The rate_key is composed as "{app_id}:{path}:{remote_ip}" — matching openclaw's key |
| feishu | gateway\platforms\feishu.py | 3445 | English string, visibility unknown | group_sessions_per_user=self.config.extra.get("group_sessions_per_user", True), |
| feishu | gateway\platforms\feishu.py | 3446 | English string, visibility unknown | thread_sessions_per_user=self.config.extra.get("thread_sessions_per_user", False), |
| feishu | gateway\platforms\feishu.py | 3451 | English string, visibility unknown | """Only merge text events when reply/thread context is identical.""" |
| feishu | gateway\platforms\feishu.py | 3480 | English string, visibility unknown | next_text = f"{existing.text}\n{appended_text}" if existing.text and appended_text else (existing.text or appended_text) |
| feishu | gateway\platforms\feishu.py | 3526 | English string, visibility unknown | last_len = getattr(pending, "_last_chunk_len", 0) if pending else 0 |
| feishu | gateway\platforms\feishu.py | 3538 | English string, visibility unknown | """Dispatch the current text batch immediately.""" |
| feishu | gateway\platforms\feishu.py | 3557 | English string, visibility unknown | raw_content = getattr(message, "content", "") or "" |
| feishu | gateway\platforms\feishu.py | 3558 | English string, visibility unknown | raw_type = getattr(message, "message_type", "") or "" |
| feishu | gateway\platforms\feishu.py | 3565 | English string, visibility unknown | mentions=getattr(message, "mentions", None), |
| feishu | gateway\platforms\feishu.py | 3578 | English string, visibility unknown | and normalized.preferred_message_type in {"document", "audio"} |
| feishu | gateway\platforms\feishu.py | 3620 | English string, visibility unknown | if normalized.startswith("image/"): |
| feishu | gateway\platforms\feishu.py | 3622 | English string, visibility unknown | if normalized.startswith("audio/"): |
| feishu | gateway\platforms\feishu.py | 3624 | English string, visibility unknown | if normalized.startswith("video/"): |
| feishu | gateway\platforms\feishu.py | 3634 | English string, visibility unknown | if preferred == "photo": |
| feishu | gateway\platforms\feishu.py | 3636 | English string, visibility unknown | if preferred == "audio": |
| feishu | gateway\platforms\feishu.py | 3638 | English string, visibility unknown | if preferred == "document": |
| feishu | gateway\platforms\feishu.py | 3643 | English string, visibility unknown | if not cached_path or not media_type.startswith("text/"): |
| feishu | gateway\platforms\feishu.py | 3651 | English string, visibility unknown | content = Path(cached_path).read_text(encoding="utf-8") |
| feishu | gateway\platforms\feishu.py | 3653 | mixed Chinese and English, visibility unknown | return f"[文件内容: {display_name}]:\n{content}" |
| feishu | gateway\platforms\feishu.py | 3665 | English string, visibility unknown | resource_type="image", |
| feishu | gateway\platforms\feishu.py | 3672 | English string, visibility unknown | getattr(response, "code", "unknown"), |
| feishu | gateway\platforms\feishu.py | 3673 | English string, visibility unknown | getattr(response, "msg", "request failed"), |
| feishu | gateway\platforms\feishu.py | 3680 | English string, visibility unknown | filename = getattr(response, "file_name", None) or f"{image_key}.jpg" |
| feishu | gateway\platforms\feishu.py | 3681 | English string, visibility unknown | ext = self._guess_extension(filename, content_type, ".jpg", allowed=_IMAGE_EXTENSIONS) |
| feishu | gateway\platforms\feishu.py | 3701 | English string, visibility unknown | if resource_type in {"audio", "media"}: |
| feishu | gateway\platforms\feishu.py | 3702 | English string, visibility unknown | request_types.append("file") |
| feishu | gateway\platforms\feishu.py | 3718 | English string, visibility unknown | getattr(response, "code", "unknown"), |
| feishu | gateway\platforms\feishu.py | 3719 | English string, visibility unknown | getattr(response, "msg", "request failed"), |
| feishu | gateway\platforms\feishu.py | 3727 | English string, visibility unknown | response_filename = getattr(response, "file_name", None) or "" |
| feishu | gateway\platforms\feishu.py | 3728 | English string, visibility unknown | filename = response_filename or fallback_filename or f"{request_type}_{file_key}" |
| feishu | gateway\platforms\feishu.py | 3734 | English string, visibility unknown | if media_type.startswith("image/"): |
| feishu | gateway\platforms\feishu.py | 3735 | English string, visibility unknown | ext = self._guess_extension(filename, content_type, ".jpg", allowed=_IMAGE_EXTENSIONS) |
| feishu | gateway\platforms\feishu.py | 3740 | English string, visibility unknown | if request_type == "audio" or media_type.startswith("audio/"): |
| feishu | gateway\platforms\feishu.py | 3741 | English string, visibility unknown | ext = self._guess_extension(filename, content_type, ".ogg", allowed=_AUDIO_EXTENSIONS) |
| feishu | gateway\platforms\feishu.py | 3744 | English string, visibility unknown | return cached_path, (media_type or f"audio/{ext.lstrip('.') or 'ogg'}") |
| feishu | gateway\platforms\feishu.py | 3746 | English string, visibility unknown | if media_type.startswith("video/"): |
| feishu | gateway\platforms\feishu.py | 3748 | English string, visibility unknown | filename = f"{filename}.mp4" |
| feishu | gateway\platforms\feishu.py | 3754 | English string, visibility unknown | filename = f"{filename}{_DOCUMENT_MIME_TO_EXT[media_type]}" |
| feishu | gateway\platforms\feishu.py | 3773 | English string, visibility unknown | file_obj = getattr(response, "file", None) |
| feishu | gateway\platforms\feishu.py | 3776 | English string, visibility unknown | if hasattr(file_obj, "getvalue"): |
| feishu | gateway\platforms\feishu.py | 3782 | English string, visibility unknown | raw = getattr(response, "raw", None) |
| feishu | gateway\platforms\feishu.py | 3783 | English string, visibility unknown | headers = getattr(raw, "headers", {}) or {} |
| feishu | gateway\platforms\feishu.py | 3784 | English string, visibility unknown | return str(headers.get(name, headers.get(name.lower(), "")) or "").split(";", 1)[0].strip().lower() |
| feishu | gateway\platforms\feishu.py | 3791 | English string, visibility unknown | guessed = mimetypes.guess_extension((content_type or "").split(";", 1)[0].strip().lower() or "") |
| feishu | gateway\platforms\feishu.py | 3798 | English string, visibility unknown | normalized = (content_type or "").split(";", 1)[0].strip().lower() |
| feishu | gateway\platforms\feishu.py | 3820 | English string, visibility unknown | return f"video/{ext.lstrip('.')}" |
| feishu | gateway\platforms\feishu.py | 3822 | English string, visibility unknown | return f"audio/{ext.lstrip('.')}" |
| feishu | gateway\platforms\feishu.py | 3832 | English string, visibility unknown | if "topic" in normalized or "thread" in normalized or "forum" in normalized: |
| feishu | gateway\platforms\feishu.py | 3833 | English string, visibility unknown | return "forum" |
| feishu | gateway\platforms\feishu.py | 3834 | English string, visibility unknown | if normalized == "group": |
| feishu | gateway\platforms\feishu.py | 3835 | English string, visibility unknown | return "group" |
| feishu | gateway\platforms\feishu.py | 3840 | English string, visibility unknown | resolved = str(chat_info.get("type") or "").strip().lower() |
| feishu | gateway\platforms\feishu.py | 3841 | English string, visibility unknown | if resolved in {"group", "forum"}: |
| feishu | gateway\platforms\feishu.py | 3845 | English string, visibility unknown | return "group" |
| feishu | gateway\platforms\feishu.py | 3859 | English string, visibility unknown | ``user_id_alt`` carries the union_id (developer-scoped, stable across |
| feishu | gateway\platforms\feishu.py | 3864 | English string, visibility unknown | open_id = getattr(sender_id, "open_id", None) or None |
| feishu | gateway\platforms\feishu.py | 3866 | English string, visibility unknown | union_id = getattr(sender_id, "union_id", None) or None |
| feishu | gateway\platforms\feishu.py | 3876 | English string, visibility unknown | "user_name": display_name, |
| feishu | gateway\platforms\feishu.py | 3877 | English string, visibility unknown | "user_id_alt": union_id, |
| feishu | gateway\platforms\feishu.py | 3910 | English string, visibility unknown | return cached_name or None # "" cached means "known nameless" |
| feishu | gateway\platforms\feishu.py | 3923 | English string, visibility unknown | id_type = "open_id" |
| feishu | gateway\platforms\feishu.py | 3925 | English string, visibility unknown | id_type = "union_id" |
| feishu | gateway\platforms\feishu.py | 3932 | English string, visibility unknown | user = getattr(getattr(response, "data", None), "user", None) |
| feishu | gateway\platforms\feishu.py | 3934 | English string, visibility unknown | getattr(user, "name", None) |
| feishu | gateway\platforms\feishu.py | 3935 | English string, visibility unknown | or getattr(user, "display_name", None) |
| feishu | gateway\platforms\feishu.py | 3936 | English string, visibility unknown | or getattr(user, "nickname", None) |
| feishu | gateway\platforms\feishu.py | 3937 | English string, visibility unknown | or getattr(user, "en_name", None) |
| feishu | gateway\platforms\feishu.py | 3955 | English string, visibility unknown | .uri("/open-apis/bot/v3/bots/basic_batch") |
| feishu | gateway\platforms\feishu.py | 3956 | English string, visibility unknown | .queries([("bot_ids", oid) for oid in bot_ids]) |
| feishu | gateway\platforms\feishu.py | 3961 | English string, visibility unknown | content = getattr(getattr(resp, "raw", None), "content", None) |
| feishu | gateway\platforms\feishu.py | 3965 | English string, visibility unknown | if payload.get("code") != 0: |
| feishu | gateway\platforms\feishu.py | 3967 | English string, visibility unknown | bots = (payload.get("data") or {}).get("bots") or {} |
| feishu | gateway\platforms\feishu.py | 3969 | English string, visibility unknown | oid: str(info.get("name") or "").strip() |
| feishu | gateway\platforms\feishu.py | 3985 | English string, visibility unknown | if not response or getattr(response, "success", lambda: False)() is False: |
| feishu | gateway\platforms\feishu.py | 3986 | English string, visibility unknown | code = getattr(response, "code", "unknown") |
| feishu | gateway\platforms\feishu.py | 3987 | mixed Chinese and English, visibility unknown | msg = getattr(response, "msg", "消息查询失败") |
| feishu | gateway\platforms\feishu.py | 3990 | English string, visibility unknown | items = getattr(getattr(response, "data", None), "items", None) or [] |
| feishu | gateway\platforms\feishu.py | 3992 | English string, visibility unknown | body = getattr(parent, "body", None) |
| feishu | gateway\platforms\feishu.py | 3993 | English string, visibility unknown | msg_type = getattr(parent, "msg_type", "") or "" |
| feishu | gateway\platforms\feishu.py | 3994 | English string, visibility unknown | raw_content = getattr(body, "content", "") or "" |
| feishu | gateway\platforms\feishu.py | 3995 | English string, visibility unknown | parent_mentions = getattr(parent, "mentions", None) if parent else None |
| feishu | gateway\platforms\feishu.py | 4028 | English string, visibility unknown | if normalized_ext in {".jpg", ".jpeg"}: |
| feishu | gateway\platforms\feishu.py | 4029 | English string, visibility unknown | return "image/jpeg" |
| feishu | gateway\platforms\feishu.py | 4030 | English string, visibility unknown | return f"image/{normalized_ext.lstrip('.') or 'jpeg'}" |
| feishu | gateway\platforms\feishu.py | 4047 | English string, visibility unknown | is_group = getattr(message, "chat_type", "p2p") != "p2p" |
| feishu | gateway\platforms\feishu.py | 4054 | English string, visibility unknown | return "self_echo" |
| feishu | gateway\platforms\feishu.py | 4058 | English string, visibility unknown | if mode != "mentions" and mode != "all": |
| feishu | gateway\platforms\feishu.py | 4059 | English string, visibility unknown | return "bots_disabled" |
| feishu | gateway\platforms\feishu.py | 4062 | English string, visibility unknown | return "self_ids_unknown" |
| feishu | gateway\platforms\feishu.py | 4065 | English string, visibility unknown | if mode == "mentions" and not require_mention and not self._mentions_self(message): |
| feishu | gateway\platforms\feishu.py | 4066 | English string, visibility unknown | return "bot_not_mentioned" |
| feishu | gateway\platforms\feishu.py | 4074 | English string, visibility unknown | return "group_policy_rejected" |
| feishu | gateway\platforms\feishu.py | 4076 | English string, visibility unknown | return "group_policy_rejected" |
| feishu | gateway\platforms\feishu.py | 4094 | English string, visibility unknown | """Per-group policy gate for non-DM traffic.""" |
| feishu | gateway\platforms\feishu.py | 4095 | English string, visibility unknown | sender_open_id = getattr(sender_id, "open_id", None) |
| feishu | gateway\platforms\feishu.py | 4114 | English string, visibility unknown | if policy == "disabled": |
| feishu | gateway\platforms\feishu.py | 4116 | English string, visibility unknown | if policy == "open": |
| feishu | gateway\platforms\feishu.py | 4118 | English string, visibility unknown | if policy == "admin_only": |
| feishu | gateway\platforms\feishu.py | 4123 | English string, visibility unknown | if policy == "allowlist": |
| feishu | gateway\platforms\feishu.py | 4125 | English string, visibility unknown | if policy == "blacklist": |
| feishu | gateway\platforms\feishu.py | 4134 | English string, visibility unknown | raw_content = getattr(message, "content", "") or "" |
| feishu | gateway\platforms\feishu.py | 4135 | English string, visibility unknown | if "@_all" in raw_content: |
| feishu | gateway\platforms\feishu.py | 4137 | English string, visibility unknown | mentions = getattr(message, "mentions", None) or [] |
| feishu | gateway\platforms\feishu.py | 4141 | English string, visibility unknown | message_type=getattr(message, "message_type", "") or "", |
| feishu | gateway\platforms\feishu.py | 4143 | English string, visibility unknown | mentions=getattr(message, "mentions", None), |
| feishu | gateway\platforms\feishu.py | 4154 | English string, visibility unknown | mention_open_id = (getattr(mention_id, "open_id", None) or "").strip() |
| feishu | gateway\platforms\feishu.py | 4156 | English string, visibility unknown | mention_name = (getattr(mention, "name", None) or "").strip() |
| feishu | gateway\platforms\feishu.py | 4185 | English string, visibility unknown | Populates ``_bot_open_id`` and ``_bot_name`` from /open-apis/bot/v3/info |
| feishu | gateway\platforms\feishu.py | 4189 | English string, visibility unknown | application info endpoint for ``_bot_name`` only when the first probe |
| feishu | gateway\platforms\feishu.py | 4202 | English string, visibility unknown | .uri("/open-apis/bot/v3/info") |
| feishu | gateway\platforms\feishu.py | 4207 | English string, visibility unknown | content = getattr(getattr(resp, "raw", None), "content", None) |
| feishu | gateway\platforms\feishu.py | 4211 | English string, visibility unknown | open_id = (parsed.get("bot_open_id") or "").strip() |
| feishu | gateway\platforms\feishu.py | 4212 | English string, visibility unknown | bot_name = (parsed.get("bot_name") or "").strip() |
| feishu | gateway\platforms\feishu.py | 4240 | English string, visibility unknown | code = getattr(response, "code", None) |
| feishu | gateway\platforms\feishu.py | 4244 | English string, visibility unknown | "Grant admin:app.info:readonly or application:application:self_manage " |
| feishu | gateway\platforms\feishu.py | 4245 | English string, visibility unknown | "so group @mention gating can resolve the bot name precisely." |
| feishu | gateway\platforms\feishu.py | 4248 | English string, visibility unknown | app = getattr(getattr(response, "data", None), "app", None) |
| feishu | gateway\platforms\feishu.py | 4249 | English string, visibility unknown | app_name = (getattr(app, "app_name", None) or "").strip() |
| feishu | gateway\platforms\feishu.py | 4261 | English string, visibility unknown | payload = json.loads(self._dedup_state_path.read_text(encoding="utf-8")) |
| feishu | gateway\platforms\feishu.py | 4267 | English string, visibility unknown | seen_data = payload.get("message_ids", {}) if isinstance(payload, dict) else {} |
| feishu | gateway\platforms\feishu.py | 4300 | English string, visibility unknown | payload = {"message_ids": {k: self._seen_message_ids[k] for k in recent if k in self._seen_message_ids}} |
| feishu | gateway\platforms\feishu.py | 4327 | English string, visibility unknown | return "interactive", _build_markdown_card_payload(content) |
| feishu | gateway\platforms\feishu.py | 4328 | English string, visibility unknown | if self._outbound_format == "text": |
| feishu | gateway\platforms\feishu.py | 4329 | English string, visibility unknown | text_payload = {"text": content} |
| feishu | gateway\platforms\feishu.py | 4330 | English string, visibility unknown | return "text", json.dumps(text_payload, ensure_ascii=False) |
| feishu | gateway\platforms\feishu.py | 4331 | English string, visibility unknown | if self._outbound_format == "post": |
| feishu | gateway\platforms\feishu.py | 4332 | English string, visibility unknown | return "post", _build_markdown_post_payload(content) |
| feishu | gateway\platforms\feishu.py | 4337 | English string, visibility unknown | text_payload = {"text": content} |
| feishu | gateway\platforms\feishu.py | 4338 | English string, visibility unknown | return "text", json.dumps(text_payload, ensure_ascii=False) |
| feishu | gateway\platforms\feishu.py | 4340 | English string, visibility unknown | return "post", _build_markdown_post_payload(content) |
| feishu | gateway\platforms\feishu.py | 4341 | English string, visibility unknown | text_payload = {"text": content} |
| feishu | gateway\platforms\feishu.py | 4342 | English string, visibility unknown | return "text", json.dumps(text_payload, ensure_ascii=False) |
| feishu | gateway\platforms\feishu.py | 4353 | English string, visibility unknown | outbound_message_type: str = "file", |
| feishu | gateway\platforms\feishu.py | 4358 | mixed Chinese and English, visibility unknown | return SendResult(success=False, error=f"文件不存在: {file_path}") |
| feishu | gateway\platforms\feishu.py | 4374 | English string, visibility unknown | file_key = self._extract_response_field(upload_response, "file_key") |
| feishu | gateway\platforms\feishu.py | 4379 | mixed Chinese and English, visibility unknown | override_error="飞书文件上传缺少 file_key", |
| feishu | gateway\platforms\feishu.py | 4384 | English string, visibility unknown | "tag": "media", |
| feishu | gateway\platforms\feishu.py | 4385 | English string, visibility unknown | "file_key": file_key, |
| feishu | gateway\platforms\feishu.py | 4386 | English string, visibility unknown | "file_name": display_name, |
| feishu | gateway\platforms\feishu.py | 4390 | English string, visibility unknown | msg_type="post", |
| feishu | gateway\platforms\feishu.py | 4399 | English string, visibility unknown | payload=json.dumps({"file_key": file_key}, ensure_ascii=False), |
| feishu | gateway\platforms\feishu.py | 4418 | English string, visibility unknown | if not effective_reply_to and metadata and metadata.get("thread_id"): |
| feishu | gateway\platforms\feishu.py | 4419 | English string, visibility unknown | effective_reply_to = metadata.get("reply_to_message_id") |
| feishu | gateway\platforms\feishu.py | 4420 | English string, visibility unknown | reply_in_thread = bool((metadata or {}).get("thread_id")) |
| feishu | gateway\platforms\feishu.py | 4434 | English string, visibility unknown | _thread_id = (metadata or {}).get("thread_id") |
| feishu | gateway\platforms\feishu.py | 4442 | English string, visibility unknown | request = self._build_create_message_request("thread_id", body) |
| feishu | gateway\platforms\feishu.py | 4452 | English string, visibility unknown | receive_id_type = "open_id" |
| feishu | gateway\platforms\feishu.py | 4460 | English string, visibility unknown | return bool(response and getattr(response, "success", lambda: False)()) |
| feishu | gateway\platforms\feishu.py | 4466 | English string, visibility unknown | data = getattr(response, "data", None) |
| feishu | gateway\platforms\feishu.py | 4478 | English string, visibility unknown | code = getattr(response, "code", "unknown") |
| feishu | gateway\platforms\feishu.py | 4479 | English string, visibility unknown | msg = getattr(response, "msg", default_message) |
| feishu | gateway\platforms\feishu.py | 4480 | English string, visibility unknown | return SendResult(success=False, error=f"[{code}] {msg}", raw_response=response) |
| feishu | gateway\platforms\feishu.py | 4498 | English string, visibility unknown | if self._connection_mode == "websocket": |
| feishu | gateway\platforms\feishu.py | 4595 | English string, visibility unknown | code = getattr(response, "code", None) |
| feishu | gateway\platforms\feishu.py | 4597 | English string, visibility unknown | if (metadata or {}).get("thread_id"): |
| feishu | gateway\platforms\feishu.py | 4600 | English string, visibility unknown | "skipping top-level fallback to avoid creating a new topic", |
| feishu | gateway\platforms\feishu.py | 4602 | English string, visibility unknown | (metadata or {}).get("thread_id"), |
| feishu | gateway\platforms\feishu.py | 4608 | English string, visibility unknown | "falling back to new message in chat %s", |
| feishu | gateway\platforms\feishu.py | 4624 | English string, visibility unknown | if msg_type == "post" and _POST_CONTENT_INVALID_RE.search(str(exc)): |
| feishu | gateway\platforms\feishu.py | 4656 | English string, visibility unknown | if "GetChatRequest" in globals(): |
| feishu | gateway\platforms\feishu.py | 4662 | English string, visibility unknown | if "GetMessageRequest" in globals(): |
| feishu | gateway\platforms\feishu.py | 4668 | English string, visibility unknown | if "GetMessageResourceRequest" in globals(): |
| feishu | gateway\platforms\feishu.py | 4680 | English string, visibility unknown | if "GetApplicationRequest" in globals(): |
| feishu | gateway\platforms\feishu.py | 4691 | English string, visibility unknown | if "ReplyMessageRequestBody" in globals(): |
| feishu | gateway\platforms\feishu.py | 4709 | English string, visibility unknown | if "ReplyMessageRequest" in globals(): |
| feishu | gateway\platforms\feishu.py | 4720 | English string, visibility unknown | if "UpdateMessageRequestBody" in globals(): |
| feishu | gateway\platforms\feishu.py | 4731 | English string, visibility unknown | if "UpdateMessageRequest" in globals(): |
| feishu | gateway\platforms\feishu.py | 4742 | English string, visibility unknown | if "CreateMessageRequestBody" in globals(): |
| feishu | gateway\platforms\feishu.py | 4760 | English string, visibility unknown | if "CreateMessageRequest" in globals(): |
| feishu | gateway\platforms\feishu.py | 4771 | English string, visibility unknown | if "CreateImageRequestBody" in globals(): |
| feishu | gateway\platforms\feishu.py | 4782 | English string, visibility unknown | if "CreateImageRequest" in globals(): |
| feishu | gateway\platforms\feishu.py | 4788 | English string, visibility unknown | if "CreateFileRequestBody" in globals(): |
| feishu | gateway\platforms\feishu.py | 4800 | English string, visibility unknown | if "CreateFileRequest" in globals(): |
| feishu | gateway\platforms\feishu.py | 4809 | English string, visibility unknown | content = payload.setdefault("zh_cn", {}).setdefault("content", []) |
| feishu | gateway\platforms\feishu.py | 4822 | English string, visibility unknown | return "opus", "audio" |
| feishu | gateway\platforms\feishu.py | 4825 | English string, visibility unknown | return "mp4", "media" |
| feishu | gateway\platforms\feishu.py | 4828 | English string, visibility unknown | return _FEISHU_DOC_UPLOAD_TYPES[ext], "file" |
| feishu | gateway\platforms\feishu.py | 4830 | English string, visibility unknown | if requested_message_type == "file": |
| feishu | gateway\platforms\feishu.py | 4831 | English string, visibility unknown | return _FEISHU_FILE_UPLOAD_TYPE, "file" |
| feishu | gateway\platforms\feishu.py | 4833 | English string, visibility unknown | return _FEISHU_FILE_UPLOAD_TYPE, "file" |
| feishu | gateway\platforms\feishu.py | 4841 | English string, visibility unknown | # Called by `hermes gateway setup` via _setup_feishu() in hermes_cli/gateway.py. |
| feishu | gateway\platforms\feishu.py | 4860 | English string, visibility unknown | url = f"{base_url}{_REGISTRATION_PATH}" |
| feishu | gateway\platforms\feishu.py | 4861 | English string, visibility unknown | data = urlencode(body).encode("utf-8") |
| feishu | gateway\platforms\feishu.py | 4865 | English string, visibility unknown | return json.loads(resp.read().decode("utf-8")) |
| feishu | gateway\platforms\feishu.py | 4870 | English string, visibility unknown | return json.loads(body_bytes.decode("utf-8")) |
| feishu | gateway\platforms\feishu.py | 4882 | English string, visibility unknown | res = _post_registration(base_url, {"action": "init"}) |
| feishu | gateway\platforms\feishu.py | 4883 | English string, visibility unknown | methods = res.get("supported_auth_methods") or [] |
| feishu | gateway\platforms\feishu.py | 4884 | English string, visibility unknown | if "client_secret" not in methods: |
| feishu | gateway\platforms\feishu.py | 4887 | English string, visibility unknown | f"Supported: {methods}" |
| feishu | gateway\platforms\feishu.py | 4892 | English string, visibility unknown | """Start the device-code flow. Returns device_code, qr_url, user_code, interval, expire_in.""" |
| feishu | gateway\platforms\feishu.py | 4895 | English string, visibility unknown | "action": "begin", |
| feishu | gateway\platforms\feishu.py | 4896 | English string, visibility unknown | "archetype": "PersonalAgent", |
| feishu | gateway\platforms\feishu.py | 4897 | English string, visibility unknown | "auth_method": "client_secret", |
| feishu | gateway\platforms\feishu.py | 4898 | English string, visibility unknown | "request_user_info": "open_id", |
| feishu | gateway\platforms\feishu.py | 4900 | English string, visibility unknown | device_code = res.get("device_code") |
| feishu | gateway\platforms\feishu.py | 4903 | English string, visibility unknown | qr_url = res.get("verification_uri_complete", "") |
| feishu | gateway\platforms\feishu.py | 4905 | English string, visibility unknown | qr_url += "&from=hermes&tp=hermes" |
| feishu | gateway\platforms\feishu.py | 4907 | English string, visibility unknown | qr_url += "?from=hermes&tp=hermes" |
| feishu | gateway\platforms\feishu.py | 4909 | English string, visibility unknown | "device_code": device_code, |
| feishu | gateway\platforms\feishu.py | 4910 | English string, visibility unknown | "qr_url": qr_url, |
| feishu | gateway\platforms\feishu.py | 4911 | English string, visibility unknown | "user_code": res.get("user_code", ""), |
| feishu | gateway\platforms\feishu.py | 4912 | English string, visibility unknown | "interval": res.get("interval") or 5, |
| feishu | gateway\platforms\feishu.py | 4913 | English string, visibility unknown | "expire_in": res.get("expire_in") or 600, |
| feishu | gateway\platforms\feishu.py | 4938 | English string, visibility unknown | "action": "poll", |
| feishu | gateway\platforms\feishu.py | 4939 | English string, visibility unknown | "device_code": device_code, |
| feishu | gateway\platforms\feishu.py | 4940 | English string, visibility unknown | "tp": "ob_app", |
| feishu | gateway\platforms\feishu.py | 4953 | English string, visibility unknown | user_info = res.get("user_info") or {} |
| feishu | gateway\platforms\feishu.py | 4954 | English string, visibility unknown | tenant_brand = user_info.get("tenant_brand") |
| feishu | gateway\platforms\feishu.py | 4961 | English string, visibility unknown | if res.get("client_id") and res.get("client_secret"): |
| feishu | gateway\platforms\feishu.py | 4965 | English string, visibility unknown | "app_id": res["client_id"], |
| feishu | gateway\platforms\feishu.py | 4966 | English string, visibility unknown | "app_secret": res["client_secret"], |
| feishu | gateway\platforms\feishu.py | 4967 | English string, visibility unknown | "domain": current_domain, |
| feishu | gateway\platforms\feishu.py | 4968 | English string, visibility unknown | "open_id": user_info.get("open_id"), |
| feishu | gateway\platforms\feishu.py | 4973 | English string, visibility unknown | if error in {"access_denied", "expired_token"}: |
| feishu | gateway\platforms\feishu.py | 4995 | English string, visibility unknown | """Try to render a QR code in the terminal. Returns True if successful.""" |
| feishu | gateway\platforms\feishu.py | 5012 | English string, visibility unknown | Returns {"bot_name": ..., "bot_open_id": ...} on success, None on failure. |
| feishu | gateway\platforms\feishu.py | 5014 | English string, visibility unknown | Note: ``bot_open_id`` here is the bot's app-scoped open_id — the same ID |
| feishu | gateway\platforms\feishu.py | 5037 | English string, visibility unknown | if data.get("code") != 0: |
| feishu | gateway\platforms\feishu.py | 5039 | English string, visibility unknown | bot = data.get("bot") or data.get("data", {}).get("bot") or {} |
| feishu | gateway\platforms\feishu.py | 5041 | English string, visibility unknown | "bot_name": bot.get("app_name") or bot.get("bot_name"), |
| feishu | gateway\platforms\feishu.py | 5042 | English string, visibility unknown | "bot_open_id": bot.get("open_id"), |
| feishu | gateway\platforms\feishu.py | 5053 | English string, visibility unknown | .uri("/open-apis/bot/v3/info") |
| feishu | gateway\platforms\feishu.py | 5058 | English string, visibility unknown | content = getattr(getattr(resp, "raw", None), "content", None) |
| feishu | gateway\platforms\feishu.py | 5071 | English string, visibility unknown | token_data = json.dumps({"app_id": app_id, "app_secret": app_secret}).encode("utf-8") |
| feishu | gateway\platforms\feishu.py | 5073 | English string, visibility unknown | f"{base_url}/open-apis/auth/v3/tenant_access_token/internal", |
| feishu | gateway\platforms\feishu.py | 5078 | English string, visibility unknown | token_res = json.loads(resp.read().decode("utf-8")) |
| feishu | gateway\platforms\feishu.py | 5080 | English string, visibility unknown | access_token = token_res.get("tenant_access_token") |
| feishu | gateway\platforms\feishu.py | 5085 | English string, visibility unknown | f"{base_url}/open-apis/bot/v3/info", |
| feishu | gateway\platforms\feishu.py | 5092 | English string, visibility unknown | bot_res = json.loads(resp.read().decode("utf-8")) |
| feishu | gateway\platforms\feishu.py | 5110 | English string, visibility unknown | "app_id": str, |
| feishu | gateway\platforms\feishu.py | 5111 | English string, visibility unknown | "app_secret": str, |
| feishu | gateway\platforms\feishu.py | 5113 | English string, visibility unknown | "open_id": str \| None, |
| feishu | gateway\platforms\feishu.py | 5114 | English string, visibility unknown | "bot_name": str \| None, |
| feishu | gateway\platforms\feishu.py | 5115 | English string, visibility unknown | "bot_open_id": str \| None, |
| feishu | gateway\platforms\feishu.py | 5133 | English string, visibility unknown | """Run init → begin → poll → probe. Raises on network/protocol errors.""" |
| feishu | gateway\platforms\feishu.py | 5140 | English string, visibility unknown | qr_url = begin["qr_url"] |
| feishu | gateway\platforms\feishu.py | 5149 | English string, visibility unknown | device_code=begin["device_code"], |
| feishu | gateway\platforms\feishu.py | 5150 | English string, visibility unknown | interval=begin["interval"], |
| feishu | gateway\platforms\feishu.py | 5151 | English string, visibility unknown | expire_in=min(begin["expire_in"], timeout_seconds), |
| feishu | gateway\platforms\feishu.py | 5158 | English string, visibility unknown | bot_info = probe_bot(result["app_id"], result["app_secret"], result["domain"]) |
| feishu | gateway\platforms\feishu.py | 5160 | English string, visibility unknown | result["bot_name"] = bot_info.get("bot_name") |
| feishu | gateway\platforms\feishu.py | 5161 | English string, visibility unknown | result["bot_open_id"] = bot_info.get("bot_open_id") |
| feishu | gateway\platforms\feishu.py | 5163 | English string, visibility unknown | result["bot_name"] = None |
| feishu | gateway\platforms\feishu.py | 5164 | English string, visibility unknown | result["bot_open_id"] = None |
| feishu | gateway\runtime_footer.py | 7 | English string, visibility unknown | Config (``~/.hermes/config.yaml``):: |
| feishu | gateway\runtime_footer.py | 15 | English string, visibility unknown | Per-platform overrides live under ``display.platforms.<platform>.runtime_footer``. |
| feishu | gateway\runtime_footer.py | 19 | English string, visibility unknown | The footer is appended to the final response text in ``gateway/run.py`` right |
| feishu | gateway\runtime_footer.py | 24 | English string, visibility unknown | ``send_trailing_footer()``. |
| feishu | gateway\runtime_footer.py | 35 | English string, visibility unknown | _DELIVERY_MODES = {"inline", "status_card"} |
| feishu | gateway\runtime_footer.py | 58 | English string, visibility unknown | if os.name == "nt" and raw.startswith("/") and not raw.startswith("//"): |
| feishu | gateway\runtime_footer.py | 70 | English string, visibility unknown | return "~/" + rel.replace("\\", "/") |
| feishu | gateway\runtime_footer.py | 94 | English string, visibility unknown | if str(style or "").lower() in {"zh", "zh_detailed", "detailed_zh"}: |
| feishu | gateway\runtime_footer.py | 95 | English string, visibility unknown | return f"{label} {value}" |
| feishu | gateway\runtime_footer.py | 100 | English string, visibility unknown | delivery = str(value or "inline").strip().lower().replace("-", "_") |
| feishu | gateway\runtime_footer.py | 101 | English string, visibility unknown | return delivery if delivery in _DELIVERY_MODES else "inline" |
| feishu | gateway\runtime_footer.py | 112 | English string, visibility unknown | 2. ``display.runtime_footer`` |
| feishu | gateway\runtime_footer.py | 113 | English string, visibility unknown | 3. ``display.platforms.<platform_key>.runtime_footer`` |
| feishu | gateway\runtime_footer.py | 115 | English string, visibility unknown | resolved = {"enabled": False, "fields": list(_DEFAULT_FIELDS), "style": "compact", "delivery": "inline"} |
| feishu | gateway\runtime_footer.py | 116 | English string, visibility unknown | cfg = (user_config or {}).get("display") or {} |
| feishu | gateway\runtime_footer.py | 118 | English string, visibility unknown | global_cfg = cfg.get("runtime_footer") |
| feishu | gateway\runtime_footer.py | 120 | English string, visibility unknown | if "enabled" in global_cfg: |
| feishu | gateway\runtime_footer.py | 121 | English string, visibility unknown | resolved["enabled"] = bool(global_cfg.get("enabled")) |
| feishu | gateway\runtime_footer.py | 122 | English string, visibility unknown | if isinstance(global_cfg.get("fields"), list) and global_cfg["fields"]: |
| feishu | gateway\runtime_footer.py | 123 | English string, visibility unknown | resolved["fields"] = [str(f) for f in global_cfg["fields"]] |
| feishu | gateway\runtime_footer.py | 124 | English string, visibility unknown | if global_cfg.get("style") is not None: |
| feishu | gateway\runtime_footer.py | 125 | English string, visibility unknown | resolved["style"] = str(global_cfg.get("style")) |
| feishu | gateway\runtime_footer.py | 126 | English string, visibility unknown | if global_cfg.get("delivery") is not None: |
| feishu | gateway\runtime_footer.py | 127 | English string, visibility unknown | resolved["delivery"] = _normalize_delivery(global_cfg.get("delivery")) |
| feishu | gateway\runtime_footer.py | 130 | English string, visibility unknown | platforms = cfg.get("platforms") or {} |
| feishu | gateway\runtime_footer.py | 133 | English string, visibility unknown | plat_footer = plat_cfg.get("runtime_footer") |
| feishu | gateway\runtime_footer.py | 135 | English string, visibility unknown | if "enabled" in plat_footer: |
| feishu | gateway\runtime_footer.py | 136 | English string, visibility unknown | resolved["enabled"] = bool(plat_footer.get("enabled")) |
| feishu | gateway\runtime_footer.py | 137 | English string, visibility unknown | if isinstance(plat_footer.get("fields"), list) and plat_footer["fields"]: |
| feishu | gateway\runtime_footer.py | 138 | English string, visibility unknown | resolved["fields"] = [str(f) for f in plat_footer["fields"]] |
| feishu | gateway\runtime_footer.py | 139 | English string, visibility unknown | if plat_footer.get("style") is not None: |
| feishu | gateway\runtime_footer.py | 140 | English string, visibility unknown | resolved["style"] = str(plat_footer.get("style")) |
| feishu | gateway\runtime_footer.py | 141 | English string, visibility unknown | if plat_footer.get("delivery") is not None: |
| feishu | gateway\runtime_footer.py | 142 | English string, visibility unknown | resolved["delivery"] = _normalize_delivery(plat_footer.get("delivery")) |
| feishu | gateway\runtime_footer.py | 157 | English string, visibility unknown | """Render the footer line, or return "" if no fields have data. |
| feishu | gateway\runtime_footer.py | 173 | English string, visibility unknown | elif field in {"context", "context_pct"}: |
| feishu | gateway\runtime_footer.py | 176 | mixed Chinese and English, visibility unknown | parts.append(_labeled("上下文", f"{pct}%", style)) |
| feishu | gateway\runtime_footer.py | 177 | English string, visibility unknown | elif field == "cwd": |
| feishu | gateway\runtime_footer.py | 200 | English string, visibility unknown | Returns the rendered footer plus delivery metadata. ``line`` is empty when |
| feishu | gateway\runtime_footer.py | 204 | English string, visibility unknown | if not cfg.get("enabled"): |
| feishu | gateway\runtime_footer.py | 205 | English string, visibility unknown | return {"delivery": cfg.get("delivery") or "inline", "line": "", "style": cfg.get("style") or "compact"} |
| feishu | gateway\runtime_footer.py | 212 | English string, visibility unknown | fields=cfg.get("fields") or _DEFAULT_FIELDS, |
| feishu | gateway\runtime_footer.py | 213 | English string, visibility unknown | style=str(cfg.get("style") or "compact"), |
| feishu | gateway\runtime_footer.py | 216 | English string, visibility unknown | "delivery": _normalize_delivery(cfg.get("delivery")), |
| feishu | gateway\runtime_footer.py | 217 | English string, visibility unknown | "line": line, |
| feishu | gateway\runtime_footer.py | 218 | English string, visibility unknown | "style": str(cfg.get("style") or "compact"), |
| feishu | gateway\runtime_footer.py | 232 | English string, visibility unknown | """Backward-compatible text-only footer entry point.""" |
| feishu | gateway\runtime_footer.py | 242 | English string, visibility unknown | ).get("line") |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 45 | English string, visibility unknown | "powershell", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 46 | English string, visibility unknown | "-NoProfile", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 47 | English string, visibility unknown | "-ExecutionPolicy", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 48 | English string, visibility unknown | "Bypass", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 49 | English string, visibility unknown | "-File", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 68 | English string, visibility unknown | encoding="utf-8", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 69 | English string, visibility unknown | errors="replace", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 74 | English string, visibility unknown | return {"ok": False, "error": str(exc), "args": args} |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 80 | English string, visibility unknown | "returncode": proc.returncode, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 81 | English string, visibility unknown | "args": args, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 85 | English string, visibility unknown | payload["data"] = json.loads(stdout) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 87 | English string, visibility unknown | payload["stdout"] = stdout |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 89 | English string, visibility unknown | payload["stderr"] = stderr |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 104 | English string, visibility unknown | def _identity(args: dict[str, Any], default: str = "user") -> str: |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 105 | English string, visibility unknown | value = str(_value(args, "identity", default)).strip() |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 106 | English string, visibility unknown | return value if value in {"user", "bot"} else default |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 123 | English string, visibility unknown | options.extend(["--format", "json"]) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 135 | English string, visibility unknown | doctor = _run(["doctor"]) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 136 | English string, visibility unknown | auth = _run(["auth", "status"]) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 137 | English string, visibility unknown | return _json({"lark_cli": _find_lark_cli(), "doctor": doctor, "auth_status": auth}) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 141 | English string, visibility unknown | query = _value(args, "query", "") |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 142 | English string, visibility unknown | options = ["docs", "+search", "--as", _identity(args), "--query", query] |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 143 | English string, visibility unknown | _add(options, "--page-size", _value(args, "page_size", 10)) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 144 | English string, visibility unknown | _add(options, "--page-token", _value(args, "page_token")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 145 | English string, visibility unknown | _add(options, "--filter", _value(args, "filter")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 152 | English string, visibility unknown | "docs", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 153 | English string, visibility unknown | "+fetch", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 155 | English string, visibility unknown | _identity(args, "user"), |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 156 | English string, visibility unknown | "--api-version", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 157 | English string, visibility unknown | str(_value(args, "api_version", "v2")), |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 159 | English string, visibility unknown | _add(options, "--doc", _value(args, "doc")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 160 | English string, visibility unknown | _add(options, "--limit", _value(args, "limit")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 161 | English string, visibility unknown | _add(options, "--offset", _value(args, "offset")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 167 | English string, visibility unknown | options = ["markdown", "+fetch", "--as", _identity(args)] |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 168 | English string, visibility unknown | _add(options, "--file-token", _value(args, "file_token")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 169 | English string, visibility unknown | _add(options, "--output", _value(args, "output")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 170 | English string, visibility unknown | _add_bool(options, "--overwrite", _value(args, "overwrite", False)) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 176 | English string, visibility unknown | options = ["markdown", "+create", "--as", _identity(args)] |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 177 | English string, visibility unknown | _add(options, "--name", _value(args, "name")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 178 | English string, visibility unknown | _add(options, "--content", _value(args, "content")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 179 | English string, visibility unknown | _add(options, "--file", _value(args, "file")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 180 | English string, visibility unknown | _add(options, "--folder-token", _value(args, "folder_token")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 181 | English string, visibility unknown | _add_bool(options, "--dry-run", _value(args, "dry_run", False)) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 187 | English string, visibility unknown | options = ["im", "+messages-search", "--as", "user"] |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 188 | English string, visibility unknown | _add(options, "--query", _value(args, "query")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 190 | English string, visibility unknown | _add(options, "--chat-type", _value(args, "chat_type")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 191 | English string, visibility unknown | _add(options, "--sender", _value(args, "sender")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 192 | English string, visibility unknown | _add(options, "--sender-type", _value(args, "sender_type")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 193 | English string, visibility unknown | _add(options, "--start", _value(args, "start")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 194 | English string, visibility unknown | _add(options, "--end", _value(args, "end")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 195 | English string, visibility unknown | _add(options, "--page-size", _value(args, "page_size", 20)) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 196 | English string, visibility unknown | _add_bool(options, "--page-all", _value(args, "page_all", False)) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 197 | English string, visibility unknown | _add_bool(options, "--is-at-me", _value(args, "is_at_me", False)) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 203 | English string, visibility unknown | options = ["im", "+messages-mget", "--as", _identity(args)] |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 204 | English string, visibility unknown | _add(options, "--message-ids", _comma(_value(args, "message_ids", ""))) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 210 | English string, visibility unknown | options = ["im", "+chat-messages-list", "--as", _identity(args)] |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 213 | English string, visibility unknown | _add(options, "--start", _value(args, "start")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 214 | English string, visibility unknown | _add(options, "--end", _value(args, "end")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 215 | English string, visibility unknown | _add(options, "--sort", _value(args, "sort", "desc")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 216 | English string, visibility unknown | _add(options, "--page-size", _value(args, "page_size", 50)) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 217 | English string, visibility unknown | _add(options, "--page-token", _value(args, "page_token")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 223 | English string, visibility unknown | options = ["task", "+get-my-tasks", "--as", "user"] |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 224 | English string, visibility unknown | _add(options, "--query", _value(args, "query")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 225 | English string, visibility unknown | _add(options, "--created_at", _value(args, "created_at")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 226 | English string, visibility unknown | _add(options, "--due-start", _value(args, "due_start")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 227 | English string, visibility unknown | _add(options, "--due-end", _value(args, "due_end")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 228 | English string, visibility unknown | if "complete" in args: |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 229 | English string, visibility unknown | _add_bool(options, "--complete", args.get("complete")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 230 | English string, visibility unknown | _add_bool(options, "--page-all", _value(args, "page_all", True)) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 236 | English string, visibility unknown | options = ["task", "+create", "--as", _identity(args)] |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 237 | English string, visibility unknown | _add(options, "--summary", _value(args, "summary")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 238 | English string, visibility unknown | _add(options, "--description", _value(args, "description")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 239 | English string, visibility unknown | _add(options, "--due", _value(args, "due")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 240 | English string, visibility unknown | _add(options, "--assignee", _value(args, "assignee")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 241 | English string, visibility unknown | _add(options, "--follower", _value(args, "follower")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 242 | English string, visibility unknown | _add(options, "--tasklist-id", _value(args, "tasklist_id")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 243 | English string, visibility unknown | _add(options, "--idempotency-key", _value(args, "idempotency_key")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 244 | English string, visibility unknown | _add_bool(options, "--dry-run", _value(args, "dry_run", False)) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 250 | English string, visibility unknown | options = ["calendar", "+agenda", "--as", _identity(args)] |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 251 | English string, visibility unknown | _add(options, "--calendar-id", _value(args, "calendar_id")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 252 | English string, visibility unknown | _add(options, "--start", _value(args, "start")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 253 | English string, visibility unknown | _add(options, "--end", _value(args, "end")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 259 | English string, visibility unknown | options = ["base", "+data-query", "--as", _identity(args)] |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 260 | English string, visibility unknown | _add(options, "--base-token", _value(args, "base_token")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 261 | English string, visibility unknown | _add(options, "--dsl", _value(args, "dsl")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 268 | English string, visibility unknown | "name": name, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 269 | English string, visibility unknown | "description": description, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 270 | English string, visibility unknown | "parameters": { |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 271 | English string, visibility unknown | "type": "object", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 272 | English string, visibility unknown | "properties": properties, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 273 | English string, visibility unknown | "required": required or [], |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 286 | English string, visibility unknown | "lark_cli_doctor", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 293 | English string, visibility unknown | "lark_docs_search", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 296 | English string, visibility unknown | ["query"], |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 300 | English string, visibility unknown | "lark_docs_fetch", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 303 | English string, visibility unknown | ["doc"], |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 307 | English string, visibility unknown | "lark_markdown_fetch", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 308 | mixed Chinese and English, visibility unknown | "按 token 获取飞书云文档 Markdown 文件。", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 310 | English string, visibility unknown | ["file_token"], |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 314 | English string, visibility unknown | "lark_markdown_create", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 315 | mixed Chinese and English, visibility unknown | "在飞书云空间创建 Markdown 文件。", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 321 | English string, visibility unknown | "lark_messages_search", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 328 | English string, visibility unknown | "lark_messages_get", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 331 | English string, visibility unknown | ["message_ids"], |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 335 | English string, visibility unknown | "lark_chat_messages_list", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 342 | English string, visibility unknown | "lark_tasks_list", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 349 | English string, visibility unknown | "lark_task_create", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 352 | English string, visibility unknown | ["summary"], |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 356 | English string, visibility unknown | "lark_calendar_agenda", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 363 | English string, visibility unknown | "lark_base_query", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 366 | English string, visibility unknown | ["base_token", "dsl"], |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 374 | English string, visibility unknown | "lark_base_query": "🗃️", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 375 | English string, visibility unknown | "lark_calendar_agenda": "📅", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 376 | English string, visibility unknown | "lark_chat_messages_list": "💬", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 377 | English string, visibility unknown | "lark_cli_doctor": "🩺", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 378 | English string, visibility unknown | "lark_docs_fetch": "📄", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 379 | English string, visibility unknown | "lark_docs_search": "🔎", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 380 | English string, visibility unknown | "lark_markdown_create": "✍️", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 381 | English string, visibility unknown | "lark_markdown_fetch": "📝", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 382 | English string, visibility unknown | "lark_messages_get": "📨", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 383 | English string, visibility unknown | "lark_messages_search": "🔎", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 384 | English string, visibility unknown | "lark_task_create": "✅", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 385 | English string, visibility unknown | "lark_tasks_list": "📋", |
| tui | ui-tui\src\app.tsx | 1 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\app.tsx | 3 | English string, visibility unknown | import { GatewayProvider } from './app/gatewayContext.js' |
| tui | ui-tui\src\app.tsx | 4 | English string, visibility unknown | import { $uiState } from './app/uiStore.js' |
| tui | ui-tui\src\app.tsx | 5 | English string, visibility unknown | import { useMainApp } from './app/useMainApp.js' |
| tui | ui-tui\src\app.tsx | 6 | English string, visibility unknown | import { AppLayout } from './components/appLayout.js' |
| tui | ui-tui\src\app.tsx | 7 | English string, visibility unknown | import type { GatewayClient } from './gatewayClient.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 11 | English string, visibility unknown | } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 12 | English string, visibility unknown | import { rpcErrorMessage } from '../lib/rpc.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 13 | English string, visibility unknown | import { topLevelSubagents } from '../lib/subagentTree.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 14 | English string, visibility unknown | import { formatToolCall, stripAnsi } from '../lib/text.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 15 | English string, visibility unknown | import { fromSkin } from '../theme.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 16 | English string, visibility unknown | import type { Msg, SubagentProgress, SubagentStatus } from '../types.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 18 | English string, visibility unknown | import { applyDelegationStatus, getDelegationState } from './delegationStore.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 19 | English string, visibility unknown | import type { GatewayEventHandlerContext } from './interfaces.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 20 | English string, visibility unknown | import { patchOverlayState } from './overlayStore.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 21 | English string, visibility unknown | import { turnController } from './turnController.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 22 | English string, visibility unknown | import { getUiState, patchUiState } from './uiStore.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 26 | English string, visibility unknown | const statusFromBusy = () => (getUiState().busy ? 'running…' : 'ready') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 60 | English string, visibility unknown | 'completed', |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 61 | English string, visibility unknown | 'error', |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 62 | English string, visibility unknown | 'failed', |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 63 | English string, visibility unknown | 'interrupted', |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 64 | English string, visibility unknown | 'queued', |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 65 | English string, visibility unknown | 'running', |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 66 | English string, visibility unknown | 'timeout' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 70 | English string, visibility unknown | if (typeof status !== 'string') { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 109 | mixed Chinese and English, visibility unknown | const label = top.length ? top.join(' · ') : `${subagents.length} 个子代理` |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 111 | English string, visibility unknown | await rpc('spawn_tree.save', { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 136 | English string, visibility unknown | rpc<DelegationStatusResponse>('delegation.status', {}) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 204 | English string, visibility unknown | // otherwise a stale `subagent.start` / `spawn_requested` can clobber a |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 206 | English string, visibility unknown | const isTerminalStatus = (s: SubagentProgress['status']) => |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 207 | English string, visibility unknown | s === 'completed' \|\| s === 'error' \|\| s === 'failed' \|\| s === 'interrupted' \|\| s === 'timeout' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 209 | English string, visibility unknown | const keepTerminalElseRunning = (s: SubagentProgress['status']) => (isTerminalStatus(s) ? s : 'running') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 216 | English string, visibility unknown | rpc<CommandsCatalogResponse>('commands.catalog', {}) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 237 | English string, visibility unknown | patchUiState({ status: 'resuming…' }) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 244 | English string, visibility unknown | // Opt-in: when `display.tui_auto_resume_recent` is true, look up |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 247 | English string, visibility unknown | // `hermes --tui` muscle memory and addresses the audit's "session |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 250 | English string, visibility unknown | rpc<ConfigFullResponse>('config.get', { key: 'full' }) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 253 | English string, visibility unknown | patchUiState({ status: 'forging session…' }) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 260 | English string, visibility unknown | return rpc<SessionMostRecentResponse>('session.most_recent', {}).then(r => { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 264 | English string, visibility unknown | patchUiState({ status: 'resuming most recent…' }) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 271 | English string, visibility unknown | patchUiState({ status: 'forging session…' }) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 277 | English string, visibility unknown | patchUiState({ status: 'forging session…' }) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 291 | English string, visibility unknown | case 'gateway.ready': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 296 | English string, visibility unknown | case 'skin.changed': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 302 | English string, visibility unknown | case 'session.info': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 312 | English string, visibility unknown | setHistoryItems(prev => prev.map(m => (m.kind === 'intro' ? { ...m, info } : m))) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 317 | English string, visibility unknown | case 'thinking.delta': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 332 | English string, visibility unknown | case 'message.start': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 336 | English string, visibility unknown | case 'status.update': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 343 | English string, visibility unknown | if (p.kind === 'goal') { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 352 | English string, visibility unknown | : 'ready' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 362 | English string, visibility unknown | if (p.kind === 'compressing') { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 368 | English string, visibility unknown | if (!p.kind \|\| p.kind === 'status') { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 376 | English string, visibility unknown | p.kind === 'error' ? 'error' : p.kind === 'warn' \|\| p.kind === 'approval' ? 'warn' : 'info' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 385 | English string, visibility unknown | case 'gateway.stderr': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 393 | English string, visibility unknown | case 'browser.progress': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 403 | English string, visibility unknown | case 'voice.status': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 408 | English string, visibility unknown | if (state === 'listening') { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 411 | English string, visibility unknown | } else if (state === 'transcribing') { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 422 | English string, visibility unknown | case 'voice.transcript': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 454 | English string, visibility unknown | case 'gateway.start_timeout': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 456 | English string, visibility unknown | const trace = python \|\| cwd ? ` · ${String(python \|\| '')} ${String(cwd \|\| '')}`.trim() : '' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 462 | English string, visibility unknown | // "wrong python", "missing dep", and "config parse failure" |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 466 | English string, visibility unknown | // 120-char clip used for `gateway.stderr` activity entries. |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 483 | English string, visibility unknown | case 'gateway.protocol_error': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 498 | English string, visibility unknown | case 'reasoning.delta': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 505 | English string, visibility unknown | case 'reasoning.available': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 510 | English string, visibility unknown | case 'tool.progress': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 517 | English string, visibility unknown | case 'tool.generating': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 524 | English string, visibility unknown | case 'tool.start': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 526 | English string, visibility unknown | turnController.recordToolStart(ev.payload.tool_id, ev.payload.name ?? 'tool', ev.payload.context ?? '') |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 529 | English string, visibility unknown | case 'tool.complete': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 555 | English string, visibility unknown | case 'clarify.request': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 562 | English string, visibility unknown | case 'approval.request': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 571 | English string, visibility unknown | case 'sudo.request': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 577 | English string, visibility unknown | case 'secret.request': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 584 | English string, visibility unknown | case 'background.complete': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 591 | English string, visibility unknown | case 'review.summary': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 606 | English string, visibility unknown | case 'subagent.spawn_requested': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 609 | English string, visibility unknown | turnController.upsertSubagent(ev.payload, c => (isTerminalStatus(c.status) ? {} : { status: 'queued' })) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 621 | English string, visibility unknown | case 'subagent.start': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 622 | English string, visibility unknown | turnController.upsertSubagent(ev.payload, c => (isTerminalStatus(c.status) ? {} : { status: 'running' })) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 625 | English string, visibility unknown | case 'subagent.thinking': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 646 | English string, visibility unknown | case 'subagent.tool': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 648 | English string, visibility unknown | ev.payload.tool_name ?? 'delegate_task', |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 664 | English string, visibility unknown | case 'subagent.progress': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 683 | English string, visibility unknown | case 'subagent.complete': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 696 | English string, visibility unknown | case 'message.delta': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 700 | English string, visibility unknown | case 'message.complete': { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 704 | English string, visibility unknown | const msgs: Msg[] = finalMessages.length ? finalMessages : [{ role: 'assistant', text: finalText }] |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 721 | English string, visibility unknown | case 'error': |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 725 | English string, visibility unknown | const message = String(ev.payload?.message \|\| 'unknown error') |
| tui | ui-tui\src\app\createSlashHandler.ts | 1 | English string, visibility unknown | import { parseSlashCommand } from '../domain/slash.js' |
| tui | ui-tui\src\app\createSlashHandler.ts | 2 | English string, visibility unknown | import type { SlashExecResponse } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\createSlashHandler.ts | 3 | English string, visibility unknown | import { asCommandDispatch, rpcErrorMessage } from '../lib/rpc.js' |
| tui | ui-tui\src\app\createSlashHandler.ts | 5 | English string, visibility unknown | import type { SlashHandlerContext } from './interfaces.js' |
| tui | ui-tui\src\app\createSlashHandler.ts | 6 | English string, visibility unknown | import { findSlashCommand } from './slash/registry.js' |
| tui | ui-tui\src\app\createSlashHandler.ts | 7 | English string, visibility unknown | import type { SlashRunCtx } from './slash/types.js' |
| tui | ui-tui\src\app\createSlashHandler.ts | 8 | English string, visibility unknown | import { getUiState } from './uiStore.js' |
| tui | ui-tui\src\app\createSlashHandler.ts | 20 | English string, visibility unknown | const argTail = parsed.arg ? ` ${parsed.arg}` : '' |
| tui | ui-tui\src\app\createSlashHandler.ts | 49 | English string, visibility unknown | const needle = `/${parsed.name}`.toLowerCase() |
| tui | ui-tui\src\app\createSlashHandler.ts | 54 | English string, visibility unknown | return handler(`${exact}${argTail}`) |
| tui | ui-tui\src\app\createSlashHandler.ts | 66 | English string, visibility unknown | return handler(`${matches[0]}${argTail}`) |
| tui | ui-tui\src\app\createSlashHandler.ts | 83 | mixed Chinese and English, visibility unknown | const body = r?.output \|\| `/${parsed.name}: 没有输出` |
| tui | ui-tui\src\app\createSlashHandler.ts | 84 | mixed Chinese and English, visibility unknown | const text = r?.warning ? `警告: ${r.warning}\n${body}` : body |
| tui | ui-tui\src\app\createSlashHandler.ts | 102 | English string, visibility unknown | if (d.type === 'exec' \|\| d.type === 'plugin') { |
| tui | ui-tui\src\app\createSlashHandler.ts | 106 | English string, visibility unknown | if (d.type === 'alias') { |
| tui | ui-tui\src\app\createSlashHandler.ts | 107 | English string, visibility unknown | return handler(`/${d.target}${argTail}`) |
| tui | ui-tui\src\app\createSlashHandler.ts | 110 | English string, visibility unknown | if (d.type === 'skill') { |
| tui | ui-tui\src\app\createSlashHandler.ts | 116 | English string, visibility unknown | if (d.type === 'send') { |
| tui | ui-tui\src\app\delegationStore.ts | 1 | English string, visibility unknown | import { atom } from 'nanostores' |
| tui | ui-tui\src\app\delegationStore.ts | 3 | English string, visibility unknown | import type { DelegationStatusResponse } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\delegationStore.ts | 39 | English string, visibility unknown | // `defaultOpen` prop. |
| tui | ui-tui\src\app\delegationStore.ts | 64 | English string, visibility unknown | if (typeof r.max_spawn_depth === 'number') { |
| tui | ui-tui\src\app\delegationStore.ts | 68 | English string, visibility unknown | if (typeof r.max_concurrent_children === 'number') { |
| tui | ui-tui\src\app\delegationStore.ts | 72 | English string, visibility unknown | if (typeof r.paused === 'boolean') { |
| tui | ui-tui\src\app\gatewayContext.tsx | 1 | English string, visibility unknown | import { createContext, useContext } from 'react' |
| tui | ui-tui\src\app\gatewayContext.tsx | 3 | English string, visibility unknown | import type { GatewayProviderProps, GatewayServices } from './interfaces.js' |
| tui | ui-tui\src\app\gatewayContext.tsx | 15 | English string, visibility unknown | throw new Error('GatewayContext missing') |
| tui | ui-tui\src\app\inputSelectionStore.ts | 1 | English string, visibility unknown | import { atom } from 'nanostores' |
| tui | ui-tui\src\app\interfaces.ts | 1 | English string, visibility unknown | import type { ScrollBoxHandle } from '@hermes/ink' |
| tui | ui-tui\src\app\interfaces.ts | 2 | English string, visibility unknown | import type { MutableRefObject, ReactNode, RefObject, SetStateAction } from 'react' |
| tui | ui-tui\src\app\interfaces.ts | 4 | English string, visibility unknown | import type { PasteEvent } from '../components/textInput.js' |
| tui | ui-tui\src\app\interfaces.ts | 5 | English string, visibility unknown | import type { GatewayClient } from '../gatewayClient.js' |
| tui | ui-tui\src\app\interfaces.ts | 6 | English string, visibility unknown | import type { ImageAttachResponse } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\interfaces.ts | 7 | English string, visibility unknown | import type { ParsedVoiceRecordKey } from '../lib/platform.js' |
| tui | ui-tui\src\app\interfaces.ts | 8 | English string, visibility unknown | import type { RpcResult } from '../lib/rpc.js' |
| tui | ui-tui\src\app\interfaces.ts | 9 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\app\interfaces.ts | 23 | English string, visibility unknown | } from '../types.js' |
| tui | ui-tui\src\app\interfaces.ts | 24 | English string, visibility unknown | import type { TuiModulesState } from './tuiModules.js' |
| tui | ui-tui\src\app\interfaces.ts | 30 | English string, visibility unknown | export type StatusBarMode = 'bottom' \| 'off' \| 'top' |
| tui | ui-tui\src\app\interfaces.ts | 32 | English string, visibility unknown | export type BusyInputMode = 'interrupt' \| 'queue' \| 'steer' |
| tui | ui-tui\src\app\interfaces.ts | 36 | English string, visibility unknown | // line — `useConfigSync` (validation) and `session.ts` (slash arg |
| tui | ui-tui\src\app\interfaces.ts | 43 | English string, visibility unknown | captureScrolledRows: (firstRow: number, lastRow: number, side: 'above' \| 'below') => void |
| tui | ui-tui\src\app\overlayStore.ts | 1 | English string, visibility unknown | import { atom, computed } from 'nanostores' |
| tui | ui-tui\src\app\overlayStore.ts | 3 | English string, visibility unknown | import type { OverlayState } from './interfaces.js' |
| tui | ui-tui\src\app\overlayStore.ts | 30 | English string, visibility unknown | $overlayState.set(typeof next === 'function' ? next($overlayState.get()) : { ...$overlayState.get(), ...next }) |
| tui | ui-tui\src\app\overlayStore.ts | 40 | English string, visibility unknown | * every turn completion / interrupt; the old "reset everything" behaviour |
| tui | ui-tui\src\app\scroll.ts | 1 | English string, visibility unknown | import type { ScrollBoxHandle } from '@hermes/ink' |
| tui | ui-tui\src\app\scroll.ts | 3 | English string, visibility unknown | import type { SelectionApi } from './interfaces.js' |
| tui | ui-tui\src\app\scroll.ts | 62 | English string, visibility unknown | selection.captureScrolledRows(top, top + actual - 1, 'above') |
| tui | ui-tui\src\app\scroll.ts | 64 | English string, visibility unknown | selection.captureScrolledRows(bottom + actual + 1, bottom, 'below') |
| tui | ui-tui\src\app\setupHandoff.ts | 1 | English string, visibility unknown | import type { RunExternalProcess } from '@hermes/ink' |
| tui | ui-tui\src\app\setupHandoff.ts | 3 | English string, visibility unknown | import type { SetupStatusResponse } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\setupHandoff.ts | 4 | English string, visibility unknown | import type { LaunchResult } from '../lib/externalCli.js' |
| tui | ui-tui\src\app\setupHandoff.ts | 6 | English string, visibility unknown | import type { SlashHandlerContext } from './interfaces.js' |
| tui | ui-tui\src\app\setupHandoff.ts | 7 | English string, visibility unknown | import { patchUiState } from './uiStore.js' |
| tui | ui-tui\src\app\setupHandoff.ts | 11 | English string, visibility unknown | ctx: Pick<SlashHandlerContext, 'gateway' \| 'session' \| 'transcript'> |
| tui | ui-tui\src\app\setupHandoff.ts | 21 | English string, visibility unknown | patchUiState({ status: 'setup running…' }) |
| tui | ui-tui\src\app\setupHandoff.ts | 31 | English string, visibility unknown | patchUiState({ status: 'setup required' }) |
| tui | ui-tui\src\app\setupHandoff.ts | 38 | English string, visibility unknown | patchUiState({ status: 'setup required' }) |
| tui | ui-tui\src\app\setupHandoff.ts | 43 | English string, visibility unknown | const setup = await gateway.rpc<SetupStatusResponse>('setup.status', {}) |
| tui | ui-tui\src\app\setupHandoff.ts | 47 | English string, visibility unknown | patchUiState({ status: 'setup required' }) |
| tui | ui-tui\src\app\slash\commands\core.ts | 1 | English string, visibility unknown | import { forceRedraw } from '@hermes/ink' |
| tui | ui-tui\src\app\slash\commands\core.ts | 4 | English string, visibility unknown | import { dailyFortune, randomFortune } from '../../../content/fortunes.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 15 | English string, visibility unknown | } from '../../../gatewayTypes.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 16 | English string, visibility unknown | import { writeClipboardText } from '../../../lib/clipboard.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 17 | English string, visibility unknown | import { writeOsc52Clipboard } from '../../../lib/osc52.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 18 | English string, visibility unknown | import { configureDetectedTerminalKeybindings, configureTerminalKeybindings } from '../../../lib/terminalSetup.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 19 | English string, visibility unknown | import type { Msg, PanelSection } from '../../../types.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 20 | English string, visibility unknown | import type { StatusBarMode } from '../../interfaces.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 21 | English string, visibility unknown | import { patchOverlayState } from '../../overlayStore.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 22 | English string, visibility unknown | import { patchUiState } from '../../uiStore.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 23 | English string, visibility unknown | import type { SlashCommand } from '../types.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 36 | English string, visibility unknown | if (mode === 'off') { |
| tui | ui-tui\src\app\slash\commands\core.ts | 40 | English string, visibility unknown | if (mode === 'toggle') { |
| tui | ui-tui\src\app\slash\commands\core.ts | 51 | mixed Chinese and English, visibility unknown | '用法: /details [hidden\|collapsed\|expanded\|cycle] 或 /details <section> [hidden\|collapsed\|expanded\|reset]' |
| tui | ui-tui\src\app\slash\commands\core.ts | 83 | mixed Chinese and English, visibility unknown | sections.push({ text: `${ctx.local.catalog.skillCount} 个技能命令可用 — 输入 /skills 浏览` }) |
| tui | ui-tui\src\app\slash\commands\core.ts | 89 | mixed Chinese and English, visibility unknown | ['/details [hidden\|collapsed\|expanded\|cycle]', '设置全局过程细节显示模式'], |
| tui | ui-tui\src\app\slash\commands\core.ts | 91 | English string, visibility unknown | '/details <section> [hidden\|collapsed\|expanded\|reset]', |
| tui | ui-tui\src\app\slash\commands\core.ts | 94 | mixed Chinese and English, visibility unknown | ['/fortune [random\|daily]', '显示随机或每日本地提示'] |
| tui | ui-tui\src\app\slash\commands\core.ts | 106 | English string, visibility unknown | aliases: ['exit', 'q'], |
| tui | ui-tui\src\app\slash\commands\core.ts | 117 | English string, visibility unknown | // Exit code 42 signals the Python wrapper to exec `hermes update`. |
| tui | ui-tui\src\app\slash\commands\core.ts | 124 | English string, visibility unknown | aliases: ['scroll'], |
| tui | ui-tui\src\app\slash\commands\core.ts | 136 | English string, visibility unknown | ctx.gateway.rpc<ConfigSetResponse>('config.set', { key: 'mouse', value: next ? 'on' : 'off' }).catch(() => {}) |
| tui | ui-tui\src\app\slash\commands\core.ts | 143 | English string, visibility unknown | aliases: ['new'], |
| tui | ui-tui\src\app\slash\commands\core.ts | 151 | English string, visibility unknown | const isNew = cmd.startsWith('/new') |
| tui | ui-tui\src\app\slash\commands\core.ts | 155 | English string, visibility unknown | patchUiState({ status: 'forging session…' }) |
| tui | ui-tui\src\app\slash\commands\core.ts | 264 | English string, visibility unknown | ctx.gateway.rpc<ConfigSetResponse>('config.set', { key: 'compact', value: next ? 'on' : 'off' }).catch(() => {}) |
| tui | ui-tui\src\app\slash\commands\core.ts | 271 | English string, visibility unknown | aliases: ['detail'], |
| tui | ui-tui\src\app\slash\commands\core.ts | 279 | English string, visibility unknown | .rpc<ConfigGetValueResponse>('config.get', { key: 'details_mode' }) |
| tui | ui-tui\src\app\slash\commands\core.ts | 289 | English string, visibility unknown | .map(s => `${detailsSectionLabel(s)}=${detailsModeLabel(ui.sections[s]!)}`) |
| tui | ui-tui\src\app\slash\commands\core.ts | 313 | English string, visibility unknown | .rpc<ConfigSetResponse>('config.set', { key: `details_mode.${first}`, value: mode ?? '' }) |
| tui | ui-tui\src\app\slash\commands\core.ts | 329 | English string, visibility unknown | gateway.rpc<ConfigSetResponse>('config.set', { key: 'details_mode', value: next }).catch(() => {}) |
| tui | ui-tui\src\app\slash\commands\core.ts | 340 | English string, visibility unknown | if (!arg \|\| key === 'random') { |
| tui | ui-tui\src\app\slash\commands\core.ts | 344 | English string, visibility unknown | if (['daily', 'stable', 'today'].includes(key)) { |
| tui | ui-tui\src\app\slash\commands\core.ts | 374 | English string, visibility unknown | const all = ctx.local.getHistoryItems().filter(m => m.role === 'assistant') |
| tui | ui-tui\src\app\slash\commands\core.ts | 414 | English string, visibility unknown | if (target && !['auto', 'cursor', 'vscode', 'windsurf'].includes(target)) { |
| tui | ui-tui\src\app\slash\commands\core.ts | 419 | English string, visibility unknown | !target \|\| target === 'auto' |
| tui | ui-tui\src\app\slash\commands\core.ts | 421 | English string, visibility unknown | : configureTerminalKeybindings(target as 'cursor' \| 'vscode' \| 'windsurf') |
| tui | ui-tui\src\app\slash\commands\core.ts | 460 | English string, visibility unknown | // transcript so `/history` actually reflects what the user just did. |
| tui | ui-tui\src\app\slash\commands\core.ts | 461 | English string, visibility unknown | const items = ctx.local.getHistoryItems().filter(m => m.role === 'user' \|\| m.role === 'assistant') |
| tui | ui-tui\src\app\slash\commands\core.ts | 470 | mixed Chinese and English, visibility unknown | const tag = m.role === 'user' ? `你 #${i + 1}` : `Hermes #${i + 1}` |
| tui | ui-tui\src\app\slash\commands\core.ts | 471 | mixed Chinese and English, visibility unknown | const body = m.text.trim() \|\| (m.tools?.length ? `(${m.tools.length} 次工具调用)` : '（空）') |
| tui | ui-tui\src\app\slash\commands\core.ts | 472 | English string, visibility unknown | const clipped = body.length > preview ? `${body.slice(0, preview).trimEnd()}…` : body |
| tui | ui-tui\src\app\slash\commands\core.ts | 474 | English string, visibility unknown | return `[${tag}]\n${clipped}` |
| tui | ui-tui\src\app\slash\commands\core.ts | 487 | English string, visibility unknown | .some(m => m.role === 'user' \|\| m.role === 'assistant' \|\| m.role === 'tool') |
| tui | ui-tui\src\app\slash\commands\core.ts | 520 | English string, visibility unknown | const toggle: StatusBarMode = ctx.ui.statusBar === 'off' ? 'top' : 'off' |
| tui | ui-tui\src\app\slash\commands\core.ts | 523 | English string, visibility unknown | !mode \|\| mode === 'toggle' |
| tui | ui-tui\src\app\slash\commands\core.ts | 525 | English string, visibility unknown | : mode === 'on' \|\| mode === 'top' |
| tui | ui-tui\src\app\slash\commands\core.ts | 526 | English string, visibility unknown | ? 'top' |
| tui | ui-tui\src\app\slash\commands\core.ts | 527 | English string, visibility unknown | : mode === 'off' \|\| mode === 'bottom' |
| tui | ui-tui\src\app\slash\commands\core.ts | 536 | English string, visibility unknown | ctx.gateway.rpc<ConfigSetResponse>('config.set', { key: 'statusbar', value: next }).catch(() => {}) |
| tui | ui-tui\src\app\slash\commands\core.ts | 565 | English string, visibility unknown | // If the agent isn't running, fall back to the queue so the user's |
| tui | ui-tui\src\app\slash\commands\core.ts | 570 | mixed Chinese and English, visibility unknown | `当前没有运行中的回合 — 已排队到下一轮: "${payload.slice(0, 50)}${payload.length > 50 ? '…' : ''}"` |
| tui | ui-tui\src\app\slash\commands\core.ts | 577 | English string, visibility unknown | .rpc<SessionSteerResponse>('session.steer', { session_id: ctx.sid, text: payload }) |
| tui | ui-tui\src\app\slash\commands\core.ts | 580 | English string, visibility unknown | if (r?.status === 'queued') { |
| tui | ui-tui\src\app\slash\commands\core.ts | 582 | mixed Chinese and English, visibility unknown | `插入消息已排队 — 会在下一次工具调用后送达: "${payload.slice(0, 50)}${payload.length > 50 ? '…' : ''}"` |
| tui | ui-tui\src\app\slash\commands\debug.ts | 1 | English string, visibility unknown | import { formatBytes, performHeapDump } from '../../../lib/memory.js' |
| tui | ui-tui\src\app\slash\commands\debug.ts | 2 | English string, visibility unknown | import type { SlashCommand } from '../types.js' |
| tui | ui-tui\src\app\slash\commands\debug.ts | 13 | English string, visibility unknown | void performHeapDump('manual').then(r => { |
| tui | ui-tui\src\app\slash\commands\debug.ts | 42 | mixed Chinese and English, visibility unknown | ['运行时长', `${process.uptime().toFixed(0)}s`] |
| tui | ui-tui\src\app\slash\commands\ops.ts | 15 | English string, visibility unknown | } from '../../../gatewayTypes.js' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 16 | English string, visibility unknown | import type { PanelSection } from '../../../types.js' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 17 | English string, visibility unknown | import { applyDelegationStatus, getDelegationState } from '../../delegationStore.js' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 18 | English string, visibility unknown | import { patchOverlayState } from '../../overlayStore.js' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 19 | English string, visibility unknown | import { getSpawnHistory, pushDiskSnapshot, setDiffPair, type SpawnSnapshot } from '../../spawnHistoryStore.js' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 20 | English string, visibility unknown | import type { SlashCommand } from '../types.js' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 70 | English string, visibility unknown | .rpc<ProcessStopResponse>('process.stop', {}) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 82 | English string, visibility unknown | aliases: ['reload_mcp'], |
| tui | ui-tui\src\app\slash\commands\ops.ts | 86 | English string, visibility unknown | // Parse arg: `now` / `always` skip the confirmation gate. |
| tui | ui-tui\src\app\slash\commands\ops.ts | 87 | English string, visibility unknown | // `always` additionally persists approvals.mcp_reload_confirm=false. |
| tui | ui-tui\src\app\slash\commands\ops.ts | 92 | English string, visibility unknown | if (a === 'now' \|\| a === 'approve' \|\| a === 'once' \|\| a === 'yes') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 94 | English string, visibility unknown | } else if (a === 'always') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 100 | English string, visibility unknown | .rpc<ReloadMcpResponse>('reload.mcp', params) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 103 | English string, visibility unknown | if (r.status === 'confirm_required') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 107 | English string, visibility unknown | if (r.status === 'reloaded') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 127 | English string, visibility unknown | .rpc<ReloadEnvResponse>('reload.env', {}) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 142 | English string, visibility unknown | const [rawAction = 'status', ...rest] = arg.trim().split(/\s+/).filter(Boolean) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 145 | English string, visibility unknown | if (!['connect', 'disconnect', 'status'].includes(action)) { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 147 | mixed Chinese and English, visibility unknown | '用法: /browser [connect\|disconnect\|status] [url] · 持久配置: 在 config.yaml 设置 browser.cdp_url' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 168 | English string, visibility unknown | if (action === 'status') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 171 | mixed Chinese and English, visibility unknown | ? `浏览器已连接: ${r.url \|\| '（url 不可用）'}` |
| tui | ui-tui\src\app\slash\commands\ops.ts | 172 | mixed Chinese and English, visibility unknown | : '浏览器未连接（可用 /browser connect <url>，或在 config.yaml 设置 browser.cdp_url）' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 176 | English string, visibility unknown | if (action === 'disconnect') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 203 | English string, visibility unknown | if (!trimmed \|\| lower === 'list' \|\| lower === 'ls') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 221 | English string, visibility unknown | `${idx + 1}. ${c.hash.slice(0, 10)}`, |
| tui | ui-tui\src\app\slash\commands\ops.ts | 231 | English string, visibility unknown | if (lower === 'diff') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 248 | English string, visibility unknown | const text = [r.stat \|\| '', body].filter(Boolean).join('\n\n') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 259 | English string, visibility unknown | .rpc<RollbackRestoreResponse>('rollback.restore', { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 270 | English string, visibility unknown | const target = filePath \|\| 'workspace' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 284 | English string, visibility unknown | aliases: ['tasks'], |
| tui | ui-tui\src\app\slash\commands\ops.ts | 293 | English string, visibility unknown | if (sub === 'pause' \|\| sub === 'resume' \|\| sub === 'unpause') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 294 | English string, visibility unknown | const paused = sub === 'pause' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 296 | English string, visibility unknown | .request<DelegationPauseResponse>('delegation.pause', { paused }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 306 | English string, visibility unknown | if (sub === 'status') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 309 | mixed Chinese and English, visibility unknown | `派生任务 · ${d.paused ? '已暂停' : '运行中'} · 限制 d${d.maxSpawnDepth ?? '?'}/${d.maxConcurrentChildren ?? '?'}` |
| tui | ui-tui\src\app\slash\commands\ops.ts | 328 | English string, visibility unknown | if (lower === 'list' \|\| lower === 'ls') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 330 | English string, visibility unknown | .rpc<SpawnTreeListResponse>('spawn_tree.list', { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 344 | mixed Chinese and English, visibility unknown | const label = e.label \|\| `${e.count} 个派生任务` |
| tui | ui-tui\src\app\slash\commands\ops.ts | 346 | English string, visibility unknown | return [`${ts} · ${e.count}×`, `${label}\n ${e.path}`] |
| tui | ui-tui\src\app\slash\commands\ops.ts | 358 | English string, visibility unknown | if (lower.startsWith('load ')) { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 366 | English string, visibility unknown | .rpc<SpawnTreeLoadResponse>('spawn_tree.load', { path }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 391 | English string, visibility unknown | if (raw && lower !== 'last') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 441 | English string, visibility unknown | aliases: ['reload_skills'], |
| tui | ui-tui\src\app\slash\commands\ops.ts | 446 | English string, visibility unknown | .rpc<SkillsReloadResponse>('skills.reload', {}) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 451 | English string, visibility unknown | .rpc<CommandsCatalogResponse>('commands.catalog', {}) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 496 | mixed Chinese and English, visibility unknown | const body = r?.output \|\| '/skills: 没有输出' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 497 | mixed Chinese and English, visibility unknown | const formatted = r?.warning ? `警告: ${r.warning}\n${body}` : body |
| tui | ui-tui\src\app\slash\commands\ops.ts | 505 | English string, visibility unknown | if (sub === 'list') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 506 | English string, visibility unknown | rpc<SkillsListResponse>('skills.manage', { action: 'list' }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 526 | English string, visibility unknown | if (sub === 'inspect') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 531 | English string, visibility unknown | rpc<SkillsInspectResponse>('skills.manage', { action: 'inspect', query }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 542 | mixed Chinese and English, visibility unknown | ['分类', String(info.category ?? '')], |
| tui | ui-tui\src\app\slash\commands\ops.ts | 543 | mixed Chinese and English, visibility unknown | ['路径', String(info.path ?? '')] |
| tui | ui-tui\src\app\slash\commands\ops.ts | 560 | English string, visibility unknown | if (sub === 'search') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 565 | English string, visibility unknown | rpc<SkillsSearchResponse>('skills.manage', { action: 'search', query }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 574 | mixed Chinese and English, visibility unknown | panel(`搜索: ${query}`, [{ rows: results.map(s => [s.name, s.description ?? '']) }]) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 582 | English string, visibility unknown | if (sub === 'install') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 589 | English string, visibility unknown | rpc<SkillsInstallResponse>('skills.manage', { action: 'install', query }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 600 | English string, visibility unknown | if (sub === 'browse') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 609 | English string, visibility unknown | rpc<SkillsBrowseResponse>('skills.manage', { action: 'browse', page: pageNum }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 619 | English string, visibility unknown | s.trust ? `${s.name} · ${s.trust}` : s.name, |
| tui | ui-tui\src\app\slash\commands\ops.ts | 626 | mixed Chinese and English, visibility unknown | footer.push(`第 ${r.page}/${r.total_pages} 页`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 630 | mixed Chinese and English, visibility unknown | footer.push(`共 ${r.total} 个技能`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 634 | mixed Chinese and English, visibility unknown | footer.push(`/skills browse ${r.page + 1} 查看更多`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 637 | mixed Chinese and English, visibility unknown | panel(`浏览技能${pageNum > 1 ? ` - 第 ${pageNum} 页` : ''}`, [ |
| tui | ui-tui\src\app\slash\commands\ops.ts | 658 | English string, visibility unknown | if (subcommand !== 'disable' && subcommand !== 'enable') { |
| tui | ui-tui\src\app\slash\commands\ops.ts | 666 | mixed Chinese and English, visibility unknown | const body = r?.output \|\| '/tools: 没有输出' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 667 | mixed Chinese and English, visibility unknown | const text = r?.warning ? `警告: ${r.warning}\n${body}` : body |
| tui | ui-tui\src\app\slash\commands\session.ts | 1 | English string, visibility unknown | import { attachedImageNotice, introMsg, toTranscriptMessages } from '../../../domain/messages.js' |
| tui | ui-tui\src\app\slash\commands\session.ts | 12 | English string, visibility unknown | } from '../../../gatewayTypes.js' |
| tui | ui-tui\src\app\slash\commands\session.ts | 13 | English string, visibility unknown | import { formatVoiceRecordKey, parseVoiceRecordKey } from '../../../lib/platform.js' |
| tui | ui-tui\src\app\slash\commands\session.ts | 14 | English string, visibility unknown | import { fmtK } from '../../../lib/text.js' |
| tui | ui-tui\src\app\slash\commands\session.ts | 15 | English string, visibility unknown | import type { PanelSection } from '../../../types.js' |
| tui | ui-tui\src\app\slash\commands\session.ts | 17 | English string, visibility unknown | import { patchOverlayState } from '../../overlayStore.js' |
| tui | ui-tui\src\app\slash\commands\session.ts | 18 | English string, visibility unknown | import { patchUiState } from '../../uiStore.js' |
| tui | ui-tui\src\app\slash\commands\session.ts | 19 | English string, visibility unknown | import type { SlashCommand } from '../types.js' |
| tui | ui-tui\src\app\slash\commands\session.ts | 29 | mixed Chinese and English, visibility unknown | value === 'show' ? '显示' : value === 'hide' ? '隐藏' : value \|\| '隐藏' |
| tui | ui-tui\src\app\slash\commands\session.ts | 32 | mixed Chinese and English, visibility unknown | value === 'show' ? '显示思考' : value === 'hide' ? '隐藏思考' : value \|\| '默认' |
| tui | ui-tui\src\app\slash\commands\session.ts | 50 | English string, visibility unknown | aliases: ['bg', 'btw'], |
| tui | ui-tui\src\app\slash\commands\session.ts | 58 | English string, visibility unknown | ctx.gateway.rpc<BackgroundStartResponse>('prompt.background', { session_id: ctx.sid, text: arg }).then( |
| tui | ui-tui\src\app\slash\commands\session.ts | 158 | English string, visibility unknown | .rpc<SessionCompressResponse>('session.compress', { |
| tui | ui-tui\src\app\slash\commands\session.ts | 199 | mixed Chinese and English, visibility unknown | `已压缩 ${r.removed} 条消息${r.usage?.total ? ` · ${fmtK(r.usage.total)} 令牌` : ''}` |
| tui | ui-tui\src\app\slash\commands\session.ts | 208 | English string, visibility unknown | aliases: ['fork'], |
| tui | ui-tui\src\app\slash\commands\session.ts | 237 | English string, visibility unknown | normalized === 'on' \|\| normalized === 'off' \|\| normalized === 'tts' \|\| normalized === 'status' |
| tui | ui-tui\src\app\slash\commands\session.ts | 239 | English string, visibility unknown | : 'status' |
| tui | ui-tui\src\app\slash\commands\session.ts | 241 | English string, visibility unknown | ctx.gateway.rpc<VoiceToggleResponse>('voice.toggle', { action }).then( |
| tui | ui-tui\src\app\slash\commands\session.ts | 245 | English string, visibility unknown | // Render the configured record key (config.yaml ``voice.record_key``) |
| tui | ui-tui\src\app\slash\commands\session.ts | 246 | English string, visibility unknown | // instead of hardcoded "Ctrl+B" — the gateway response carries the |
| tui | ui-tui\src\app\slash\commands\session.ts | 253 | English string, visibility unknown | // the next ``mtime`` poll (~5s). Parse once, push into state so |
| tui | ui-tui\src\app\slash\commands\session.ts | 254 | English string, visibility unknown | // ``useInputHandlers()`` picks up the new binding immediately. |
| tui | ui-tui\src\app\slash\commands\session.ts | 257 | English string, visibility unknown | // carries ``record_key`` — otherwise an older gateway (or a future |
| tui | ui-tui\src\app\slash\commands\session.ts | 267 | English string, visibility unknown | const recordKeyLabel = formatVoiceRecordKey(parsed ?? parseVoiceRecordKey('ctrl+b')) |
| tui | ui-tui\src\app\slash\commands\session.ts | 272 | English string, visibility unknown | if (action === 'status') { |
| tui | ui-tui\src\app\slash\commands\session.ts | 295 | English string, visibility unknown | if (action === 'tts') { |
| tui | ui-tui\src\app\slash\commands\session.ts | 322 | English string, visibility unknown | .rpc<ConfigGetValueResponse>('config.get', { key: 'skin' }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 327 | English string, visibility unknown | .rpc<ConfigSetResponse>('config.set', { key: 'skin', value: arg }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 341 | English string, visibility unknown | .rpc<ConfigGetValueResponse>('config.get', { key: 'indicator' }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 353 | English string, visibility unknown | ctx.gateway.rpc<ConfigSetResponse>('config.set', { key: 'indicator', value }).then( |
| tui | ui-tui\src\app\slash\commands\session.ts | 385 | English string, visibility unknown | .rpc<ConfigGetValueResponse>('config.get', { key: 'reasoning' }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 403 | English string, visibility unknown | if (r.value === 'hide') { |
| tui | ui-tui\src\app\slash\commands\session.ts | 406 | English string, visibility unknown | sections: { ...state.sections, thinking: 'hidden' }, |
| tui | ui-tui\src\app\slash\commands\session.ts | 409 | English string, visibility unknown | } else if (r.value === 'show') { |
| tui | ui-tui\src\app\slash\commands\session.ts | 412 | English string, visibility unknown | sections: { ...state.sections, thinking: 'expanded' }, |
| tui | ui-tui\src\app\slash\commands\session.ts | 428 | English string, visibility unknown | const valid = new Set(['', 'status', 'normal', 'fast', 'on', 'off', 'toggle']) |
| tui | ui-tui\src\app\slash\commands\session.ts | 434 | English string, visibility unknown | if (!mode \|\| mode === 'status') { |
| tui | ui-tui\src\app\slash\commands\session.ts | 449 | English string, visibility unknown | const next = r.value === 'fast' ? 'fast' : 'normal' |
| tui | ui-tui\src\app\slash\commands\session.ts | 456 | English string, visibility unknown | fast: next === 'fast', |
| tui | ui-tui\src\app\slash\commands\session.ts | 457 | English string, visibility unknown | service_tier: next === 'fast' ? 'priority' : '' |
| tui | ui-tui\src\app\slash\commands\session.ts | 472 | English string, visibility unknown | const valid = new Set(['', 'status', 'queue', 'steer', 'interrupt']) |
| tui | ui-tui\src\app\slash\commands\session.ts | 478 | English string, visibility unknown | if (!mode \|\| mode === 'status') { |
| tui | ui-tui\src\app\slash\commands\session.ts | 480 | English string, visibility unknown | .rpc<ConfigGetValueResponse>('config.get', { key: 'busy' }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 483 | English string, visibility unknown | const current = r.value \|\| 'interrupt' |
| tui | ui-tui\src\app\slash\commands\session.ts | 484 | mixed Chinese and English, visibility unknown | const label = current === 'queue' ? '排队' : current === 'steer' ? '转向' : '打断' |
| tui | ui-tui\src\app\slash\commands\session.ts | 492 | English string, visibility unknown | .rpc<ConfigSetResponse>('config.set', { key: 'busy', value: mode }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 496 | mixed Chinese and English, visibility unknown | const label = next === 'queue' ? '排队' : next === 'steer' ? '转向' : '打断' |
| tui | ui-tui\src\app\slash\commands\session.ts | 534 | English string, visibility unknown | const cost = r.cost_usd != null ? `${r.cost_status === 'estimated' ? '~' : ''}$${r.cost_usd.toFixed(4)}` : null |
| tui | ui-tui\src\app\slash\commands\session.ts | 553 | mixed Chinese and English, visibility unknown | sections.push({ text: `上下文: ${f(r.context_used)} / ${f(r.context_max)} (${r.context_percent}%)` }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 557 | mixed Chinese and English, visibility unknown | sections.push({ text: `压缩次数: ${r.compressions}` }) |
| tui | ui-tui\src\app\slash\commands\setup.ts | 1 | English string, visibility unknown | import { withInkSuspended } from '@hermes/ink' |
| tui | ui-tui\src\app\slash\commands\setup.ts | 3 | English string, visibility unknown | import { launchHermesCommand } from '../../../lib/externalCli.js' |
| tui | ui-tui\src\app\slash\commands\setup.ts | 4 | English string, visibility unknown | import { runExternalSetup } from '../../setupHandoff.js' |
| tui | ui-tui\src\app\slash\commands\setup.ts | 5 | English string, visibility unknown | import type { SlashCommand } from '../types.js' |
| tui | ui-tui\src\app\slash\commands\setup.ts | 13 | English string, visibility unknown | args: ['setup', ...arg.split(/\s+/).filter(Boolean)], |
| tui | ui-tui\src\app\slash\registry.ts | 1 | English string, visibility unknown | import { coreCommands } from './commands/core.js' |
| tui | ui-tui\src\app\slash\registry.ts | 2 | English string, visibility unknown | import { debugCommands } from './commands/debug.js' |
| tui | ui-tui\src\app\slash\registry.ts | 3 | English string, visibility unknown | import { opsCommands } from './commands/ops.js' |
| tui | ui-tui\src\app\slash\registry.ts | 4 | English string, visibility unknown | import { sessionCommands } from './commands/session.js' |
| tui | ui-tui\src\app\slash\registry.ts | 5 | English string, visibility unknown | import { setupCommands } from './commands/setup.js' |
| tui | ui-tui\src\app\slash\registry.ts | 6 | English string, visibility unknown | import type { SlashCommand } from './types.js' |
| tui | ui-tui\src\app\slash\types.ts | 1 | English string, visibility unknown | import type { MutableRefObject } from 'react' |
| tui | ui-tui\src\app\slash\types.ts | 3 | English string, visibility unknown | import type { SlashHandlerContext, UiState } from '../interfaces.js' |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 1 | English string, visibility unknown | import { atom } from 'nanostores' |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 3 | English string, visibility unknown | import type { SpawnTreeLoadResponse } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 4 | English string, visibility unknown | import type { SubagentProgress, SubagentStatus } from '../types.js' |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 25 | English string, visibility unknown | 'completed', |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 26 | English string, visibility unknown | 'error', |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 27 | English string, visibility unknown | 'failed', |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 28 | English string, visibility unknown | 'interrupted', |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 29 | English string, visibility unknown | 'queued', |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 30 | English string, visibility unknown | 'running', |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 31 | English string, visibility unknown | 'timeout' |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 35 | English string, visibility unknown | if (typeof status !== 'string') { |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 76 | English string, visibility unknown | id: `snap-${now.toString(36)}`, |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 91 | English string, visibility unknown | .map(s => s.goal \|\| 'subagent') |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 94 | mixed Chinese and English, visibility unknown | return top \|\| `${subagents.length} 个子代理` |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 114 | English string, visibility unknown | id: `disk-${path}`, |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 128 | English string, visibility unknown | const s = (v: unknown) => (typeof v === 'string' ? v : undefined) |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 129 | English string, visibility unknown | const n = (v: unknown) => (typeof v === 'number' ? v : undefined) |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 135 | English string, visibility unknown | depth: typeof o.depth === 'number' ? o.depth : 0, |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 139 | English string, visibility unknown | goal: s(o.goal) ?? 'subagent', |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 140 | English string, visibility unknown | id: s(o.id) ?? `sa-${Math.random().toString(36).slice(2, 8)}`, |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 141 | English string, visibility unknown | index: typeof o.index === 'number' ? o.index : 0, |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 145 | English string, visibility unknown | notes: (arr<string>(o.notes) ?? []).filter(x => typeof x === 'string'), |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 146 | English string, visibility unknown | outputTail: arr(o.outputTail) as SubagentProgress['outputTail'], |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 153 | English string, visibility unknown | taskCount: typeof o.taskCount === 'number' ? o.taskCount : 1, |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 154 | English string, visibility unknown | thinking: (arr<string>(o.thinking) ?? []).filter(x => typeof x === 'string'), |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 155 | English string, visibility unknown | toolCount: typeof o.toolCount === 'number' ? o.toolCount : 0, |
| tui | ui-tui\src\app\spawnHistoryStore.ts | 156 | English string, visibility unknown | tools: (arr<string>(o.tools) ?? []).filter(x => typeof x === 'string'), |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 1 | English string, visibility unknown | import type { TuiModulesState } from './tuiModules.js' |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 2 | English string, visibility unknown | import type { TuiSlotId } from './tuiSlots.js' |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 5 | English string, visibility unknown | export type TuiModuleSurface = 'dock' \| 'inline' \| 'status' \| 'future' |
| tui | ui-tui\src\app\tuiModules.ts | 1 | English string, visibility unknown | import { isTuiSlotId, type TuiSlotId } from './tuiSlots.js' |
| tui | ui-tui\src\app\tuiModules.ts | 3 | English string, visibility unknown | export type TuiModulePosition = 'auto' \| 'bottom' \| 'side' \| 'status' \| 'top' |
| tui | ui-tui\src\app\tuiModules.ts | 4 | English string, visibility unknown | export type TuiModuleCompactMode = boolean \| 'auto' |
| tui | ui-tui\src\app\tuiModules.ts | 71 | English string, visibility unknown | 'activity-scan': 'activityScan', |
| tui | ui-tui\src\app\tuiModules.ts | 74 | English string, visibility unknown | 'character-panel': 'characterPanel', |
| tui | ui-tui\src\app\tuiModules.ts | 77 | English string, visibility unknown | 'monitor-panel': 'monitorPanel', |
| tui | ui-tui\src\app\tuiModules.ts | 80 | English string, visibility unknown | 'status-meter': 'statusMeter', |
| tui | ui-tui\src\app\tuiModules.ts | 83 | English string, visibility unknown | 'task-panel': 'taskPanel' |
| tui | ui-tui\src\app\tuiModules.ts | 97 | English string, visibility unknown | const value = typeof raw === 'string' ? raw.trim().toLowerCase() : '' |
| tui | ui-tui\src\app\tuiModules.ts | 103 | English string, visibility unknown | const value = typeof raw === 'number' ? raw : typeof raw === 'string' ? Number(raw) : Number.NaN |
| tui | ui-tui\src\app\tuiModules.ts | 109 | English string, visibility unknown | const value = typeof raw === 'number' ? raw : typeof raw === 'string' ? Number(raw) : Number.NaN |
| tui | ui-tui\src\app\tuiModules.ts | 115 | English string, visibility unknown | if (typeof raw === 'boolean' \|\| raw === 'auto') { |
| tui | ui-tui\src\app\tuiModules.ts | 119 | English string, visibility unknown | if (typeof raw !== 'string') { |
| tui | ui-tui\src\app\tuiModules.ts | 125 | English string, visibility unknown | if (value === 'auto') { |
| tui | ui-tui\src\app\tuiModules.ts | 126 | English string, visibility unknown | return 'auto' |
| tui | ui-tui\src\app\tuiModules.ts | 129 | English string, visibility unknown | if (value === 'true') { |
| tui | ui-tui\src\app\tuiModules.ts | 133 | English string, visibility unknown | if (value === 'false') { |
| tui | ui-tui\src\app\tuiModules.ts | 145 | English string, visibility unknown | if (position === 'auto') { |
| tui | ui-tui\src\app\tuiModules.ts | 149 | English string, visibility unknown | if (position === 'top') { |
| tui | ui-tui\src\app\tuiModules.ts | 150 | English string, visibility unknown | return 'intro.hero' |
| tui | ui-tui\src\app\tuiModules.ts | 153 | English string, visibility unknown | if (position === 'side') { |
| tui | ui-tui\src\app\tuiModules.ts | 154 | English string, visibility unknown | return 'side.right' |
| tui | ui-tui\src\app\tuiModules.ts | 157 | English string, visibility unknown | if (position === 'bottom') { |
| tui | ui-tui\src\app\tuiModules.ts | 158 | English string, visibility unknown | return currentKey === 'taskPanel' ? 'transcript.afterUser' : 'composer.dock' |
| tui | ui-tui\src\app\tuiModules.ts | 161 | English string, visibility unknown | if (currentKey === 'activityScan') { |
| tui | ui-tui\src\app\tuiModules.ts | 162 | English string, visibility unknown | return 'status.left' |
| tui | ui-tui\src\app\tuiModules.ts | 165 | English string, visibility unknown | if (currentKey === 'statusMeter') { |
| tui | ui-tui\src\app\tuiModules.ts | 166 | English string, visibility unknown | return 'status.center' |
| tui | ui-tui\src\app\tuiModules.ts | 169 | English string, visibility unknown | return 'status.right' |
| tui | ui-tui\src\app\tuiModules.ts | 182 | English string, visibility unknown | if (!raw \|\| typeof raw !== 'object' \|\| Array.isArray(raw)) { |
| tui | ui-tui\src\app\tuiModules.ts | 195 | English string, visibility unknown | if (typeof rawValue === 'boolean') { |
| tui | ui-tui\src\app\tuiModules.ts | 201 | English string, visibility unknown | if (!rawValue \|\| typeof rawValue !== 'object' \|\| Array.isArray(rawValue)) { |
| tui | ui-tui\src\app\tuiModules.ts | 206 | English string, visibility unknown | const enabled = typeof cfg.enabled === 'boolean' ? cfg.enabled : current.enabled |
| tui | ui-tui\src\app\tuiSlots.ts | 2 | English string, visibility unknown | 'intro.hero', |
| tui | ui-tui\src\app\tuiSlots.ts | 3 | English string, visibility unknown | 'status.left', |
| tui | ui-tui\src\app\tuiSlots.ts | 4 | English string, visibility unknown | 'status.center', |
| tui | ui-tui\src\app\tuiSlots.ts | 5 | English string, visibility unknown | 'status.right', |
| tui | ui-tui\src\app\tuiSlots.ts | 6 | English string, visibility unknown | 'transcript.afterUser', |
| tui | ui-tui\src\app\tuiSlots.ts | 7 | English string, visibility unknown | 'composer.dock', |
| tui | ui-tui\src\app\tuiSlots.ts | 8 | English string, visibility unknown | 'side.right', |
| tui | ui-tui\src\app\tuiSlots.ts | 9 | English string, visibility unknown | 'overlay' |
| tui | ui-tui\src\app\turnController.ts | 7 | English string, visibility unknown | } from '../config/timing.js' |
| tui | ui-tui\src\app\turnController.ts | 8 | English string, visibility unknown | import type { SessionInterruptResponse, SubagentEventPayload } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\turnController.ts | 9 | English string, visibility unknown | import { appendToolShelfMessage, isToolShelfMessage } from '../lib/liveProgress.js' |
| tui | ui-tui\src\app\turnController.ts | 10 | English string, visibility unknown | import { hasReasoningTag, splitReasoning } from '../lib/reasoning.js' |
| tui | ui-tui\src\app\turnController.ts | 18 | English string, visibility unknown | } from '../lib/text.js' |
| tui | ui-tui\src\app\turnController.ts | 19 | English string, visibility unknown | import type { ActiveTool, ActivityItem, Msg, SubagentProgress, TodoItem } from '../types.js' |
| tui | ui-tui\src\app\turnController.ts | 21 | English string, visibility unknown | import { resetFlowOverlays } from './overlayStore.js' |
| tui | ui-tui\src\app\turnController.ts | 22 | English string, visibility unknown | import { pushSnapshot } from './spawnHistoryStore.js' |
| tui | ui-tui\src\app\turnController.ts | 23 | English string, visibility unknown | import { archiveDoneTodos, getTurnState, patchTurnState, resetTurnState } from './turnStore.js' |
| tui | ui-tui\src\app\turnController.ts | 24 | English string, visibility unknown | import { getUiState, patchUiState } from './uiStore.js' |
| tui | ui-tui\src\app\turnController.ts | 35 | English string, visibility unknown | if (msg.kind !== 'diff') { |
| tui | ui-tui\src\app\turnController.ts | 39 | English string, visibility unknown | const m = msg.text.match(/^```diff\n([\s\S]*?)\n```$/) |
| tui | ui-tui\src\app\turnController.ts | 46 | English string, visibility unknown | const isTodoStatus = (status: unknown): status is TodoItem['status'] => |
| tui | ui-tui\src\app\turnController.ts | 56 | English string, visibility unknown | if (!item \|\| typeof item !== 'object') { |
| tui | ui-tui\src\app\turnController.ts | 77 | English string, visibility unknown | segments.filter(msg => msg.role === 'assistant' && msg.kind !== 'diff').map(msg => msg.text) |
| tui | ui-tui\src\app\turnController.ts | 196 | English string, visibility unknown | // appears in both `turn.streamSegments` and the transcript for one frame. |
| tui | ui-tui\src\app\turnController.ts | 207 | English string, visibility unknown | // `partial` or pending tools, fold them into a single assistant message; |
| tui | ui-tui\src\app\turnController.ts | 209 | English string, visibility unknown | // turn was cancelled, even when only prior `segments` were preserved. |
| tui | ui-tui\src\app\turnController.ts | 213 | mixed Chinese and English, visibility unknown | text: partial ? `${partial}\n\n*[已中断]*` : '*[已中断]*', |
| tui | ui-tui\src\app\turnController.ts | 220 | English string, visibility unknown | patchUiState({ status: 'interrupted' }) |
| tui | ui-tui\src\app\turnController.ts | 225 | English string, visibility unknown | patchUiState({ status: 'ready' }) |
| tui | ui-tui\src\app\turnController.ts | 281 | English string, visibility unknown | : { reasoning: '', text: '' } |
| tui | ui-tui\src\app\turnController.ts | 291 | English string, visibility unknown | role: split.text ? 'assistant' : 'system', |
| tui | ui-tui\src\app\turnController.ts | 293 | English string, visibility unknown | ...(!split.text && { kind: 'trail' as const }), |
| tui | ui-tui\src\app\turnController.ts | 355 | English string, visibility unknown | // leading "┊ review diff" header written by `_emit_inline_diff` for the |
| tui | ui-tui\src\app\turnController.ts | 371 | English string, visibility unknown | const block = `\`\`\`diff\n${stripped}\n\`\`\`` |
| tui | ui-tui\src\app\turnController.ts | 382 | English string, visibility unknown | { kind: 'diff', role: 'assistant', text: block, ...(tools.length && { tools }) } |
| tui | ui-tui\src\app\turnController.ts | 435 | English string, visibility unknown | // (`payload.rendered`) is for terminals that can't. Prioritising |
| tui | ui-tui\src\app\turnController.ts | 436 | English string, visibility unknown | // `rendered` here garbles output whenever a user opts into |
| tui | ui-tui\src\app\turnController.ts | 444 | English string, visibility unknown | const savedReasoning = [existingReasoning, existingReasoning ? '' : split.reasoning].filter(Boolean).join('\n\n') |
| tui | ui-tui\src\app\turnController.ts | 459 | English string, visibility unknown | // reply. Without this, a closing "here's the diff …" message would |
| tui | ui-tui\src\app\turnController.ts | 461 | English string, visibility unknown | // with `kind: 'diff'` emitted by pushInlineDiffSegment — real |
| tui | ui-tui\src\app\turnController.ts | 495 | English string, visibility unknown | finalMessages.push({ role: 'assistant', text: finalText }) |
| tui | ui-tui\src\app\turnController.ts | 537 | English string, visibility unknown | // `display.final_response_markdown: render`. |
| tui | ui-tui\src\app\turnController.ts | 622 | English string, visibility unknown | const name = done?.name ?? fallbackName ?? 'tool' |
| tui | ui-tui\src\app\turnController.ts | 688 | English string, visibility unknown | const sample = `${name} ${context}`.trim() |
| tui | ui-tui\src\app\turnController.ts | 768 | English string, visibility unknown | const id = p.subagent_id \|\| `sa:${p.task_index}:${p.goal \|\| 'subagent'}` |
| tui | ui-tui\src\app\turnController.ts | 775 | English string, visibility unknown | // subagent into turn.subagents and block the "finished" title on the |
| tui | ui-tui\src\app\turnController.ts | 776 | English string, visibility unknown | // /agents overlay. When `createIfMissing` is false we drop silently. |
| tui | ui-tui\src\app\turnController.ts | 805 | English string, visibility unknown | tool: String(e.tool ?? 'tool') |
| tui | ui-tui\src\app\turnStore.ts | 1 | English string, visibility unknown | import { atom } from 'nanostores' |
| tui | ui-tui\src\app\turnStore.ts | 2 | English string, visibility unknown | import { useSyncExternalStore } from 'react' |
| tui | ui-tui\src\app\turnStore.ts | 4 | English string, visibility unknown | import { isTodoDone } from '../lib/liveProgress.js' |
| tui | ui-tui\src\app\turnStore.ts | 5 | English string, visibility unknown | import type { ActiveTool, ActivityItem, Msg, SubagentProgress, TodoItem } from '../types.js' |
| tui | ui-tui\src\app\turnStore.ts | 39 | English string, visibility unknown | $turnState.set(typeof next === 'function' ? next($turnState.get()) : { ...$turnState.get(), ...next }) |
| tui | ui-tui\src\app\uiStore.ts | 1 | English string, visibility unknown | import { atom, computed } from 'nanostores' |
| tui | ui-tui\src\app\uiStore.ts | 8 | English string, visibility unknown | import { buildDefaultTuiModules } from './tuiModules.js' |
| tui | ui-tui\src\app\uiStore.ts | 41 | English string, visibility unknown | $uiState.set(typeof next === 'function' ? next($uiState.get()) : { ...$uiState.get(), ...next }) |
| tui | ui-tui\src\app\useComposerState.ts | 1 | English string, visibility unknown | import { spawnSync } from 'node:child_process' |
| tui | ui-tui\src\app\useComposerState.ts | 2 | English string, visibility unknown | import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs' |
| tui | ui-tui\src\app\useComposerState.ts | 3 | English string, visibility unknown | import { tmpdir } from 'node:os' |
| tui | ui-tui\src\app\useComposerState.ts | 4 | English string, visibility unknown | import { join } from 'node:path' |
| tui | ui-tui\src\app\useComposerState.ts | 6 | English string, visibility unknown | import { useStdin, withInkSuspended } from '@hermes/ink' |
| tui | ui-tui\src\app\useComposerState.ts | 7 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\app\useComposerState.ts | 8 | English string, visibility unknown | import { useCallback, useMemo, useState } from 'react' |
| tui | ui-tui\src\app\useComposerState.ts | 10 | English string, visibility unknown | import type { PasteEvent } from '../components/textInput.js' |
| tui | ui-tui\src\app\useComposerState.ts | 12 | English string, visibility unknown | import type { ImageAttachResponse, InputDetectDropResponse } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\useComposerState.ts | 13 | English string, visibility unknown | import { useCompletion } from '../hooks/useCompletion.js' |
| tui | ui-tui\src\app\useComposerState.ts | 14 | English string, visibility unknown | import { useInputHistory } from '../hooks/useInputHistory.js' |
| tui | ui-tui\src\app\useComposerState.ts | 15 | English string, visibility unknown | import { useQueue } from '../hooks/useQueue.js' |
| tui | ui-tui\src\app\useComposerState.ts | 16 | English string, visibility unknown | import { isUsableClipboardText, readClipboardText } from '../lib/clipboard.js' |
| tui | ui-tui\src\app\useComposerState.ts | 17 | English string, visibility unknown | import { resolveEditor } from '../lib/editor.js' |
| tui | ui-tui\src\app\useComposerState.ts | 18 | English string, visibility unknown | import { readOsc52Clipboard } from '../lib/osc52.js' |
| tui | ui-tui\src\app\useComposerState.ts | 19 | English string, visibility unknown | import { isRemoteShellSession } from '../lib/terminalSetup.js' |
| tui | ui-tui\src\app\useComposerState.ts | 20 | English string, visibility unknown | import { pasteTokenLabel, stripTrailingPasteNewlines } from '../lib/text.js' |
| tui | ui-tui\src\app\useComposerState.ts | 22 | English string, visibility unknown | import type { MaybePromise, PasteSnippet, UseComposerStateOptions, UseComposerStateResult } from './interfaces.js' |
| tui | ui-tui\src\app\useComposerState.ts | 23 | English string, visibility unknown | import { $isBlocked } from './overlayStore.js' |
| tui | ui-tui\src\app\useComposerState.ts | 24 | English string, visibility unknown | import { getUiState } from './uiStore.js' |
| tui | ui-tui\src\app\useComposerState.ts | 52 | English string, visibility unknown | const insert = `${lead}${text}${tail}` |
| tui | ui-tui\src\app\useComposerState.ts | 75 | English string, visibility unknown | trimmed.startsWith('file://') \|\| |
| tui | ui-tui\src\app\useComposerState.ts | 90 | English string, visibility unknown | // false positives on short strings like "/api" or "/help" which would trigger |
| tui | ui-tui\src\app\useComposerState.ts | 95 | English string, visibility unknown | return rest.includes('/') \|\| rest.includes('.') |
| tui | ui-tui\src\app\useComposerState.ts | 159 | English string, visibility unknown | const attached = await gw.request<ImageAttachResponse>('image.attach', { |
| tui | ui-tui\src\app\useComposerState.ts | 179 | English string, visibility unknown | const dropped = await gw.request<InputDetectDropResponse>('input.detect_drop', { |
| tui | ui-tui\src\app\useComposerState.ts | 207 | English string, visibility unknown | .request<{ path?: string }>('paste.collapse', { text: cleanedText }) |
| tui | ui-tui\src\app\useComposerState.ts | 268 | English string, visibility unknown | const dir = mkdtempSync(join(tmpdir(), 'hermes-')) |
| tui | ui-tui\src\app\useComposerState.ts | 269 | English string, visibility unknown | const file = join(dir, 'prompt.md') |
| tui | ui-tui\src\app\useComposerState.ts | 277 | English string, visibility unknown | exitCode = spawnSync(cmd!, [...args, file], { stdio: 'inherit' }).status |
| tui | ui-tui\src\app\useComposerState.ts | 285 | English string, visibility unknown | const text = readFileSync(file, 'utf8').trimEnd() |
| tui | ui-tui\src\app\useConfigSync.ts | 1 | English string, visibility unknown | import { useEffect, useRef } from 'react' |
| tui | ui-tui\src\app\useConfigSync.ts | 3 | English string, visibility unknown | import { resolveDetailsMode, resolveSections } from '../domain/details.js' |
| tui | ui-tui\src\app\useConfigSync.ts | 4 | English string, visibility unknown | import type { GatewayClient } from '../gatewayClient.js' |
| tui | ui-tui\src\app\useConfigSync.ts | 9 | English string, visibility unknown | } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\useConfigSync.ts | 14 | English string, visibility unknown | } from '../lib/platform.js' |
| tui | ui-tui\src\app\useConfigSync.ts | 15 | English string, visibility unknown | import { asRpcResult } from '../lib/rpc.js' |
| tui | ui-tui\src\app\useConfigSync.ts | 23 | English string, visibility unknown | } from './interfaces.js' |
| tui | ui-tui\src\app\useConfigSync.ts | 24 | English string, visibility unknown | import { normalizeTuiModules } from './tuiModules.js' |
| tui | ui-tui\src\app\useConfigSync.ts | 25 | English string, visibility unknown | import { turnController } from './turnController.js' |
| tui | ui-tui\src\app\useConfigSync.ts | 26 | English string, visibility unknown | import { patchUiState } from './uiStore.js' |
| tui | ui-tui\src\app\useConfigSync.ts | 41 | English string, visibility unknown | // (`hermes_cli/config.py`) is `interrupt`. Rationale: in a full-screen |
| tui | ui-tui\src\app\useConfigSync.ts | 44 | English string, visibility unknown | // `display.busy_input_mode: interrupt` (or `steer`) explicitly to |
| tui | ui-tui\src\app\useConfigSync.ts | 50 | English string, visibility unknown | if (typeof raw !== 'string') { |
| tui | ui-tui\src\app\useConfigSync.ts | 62 | English string, visibility unknown | if (typeof raw !== 'string') { |
| tui | ui-tui\src\app\useConfigSync.ts | 75 | English string, visibility unknown | const raw = hasOwn(display, 'mouse_tracking') ? display.mouse_tracking : display.tui_mouse |
| tui | ui-tui\src\app\useConfigSync.ts | 104 | English string, visibility unknown | /** Fetch ``config.get full`` and fan the result through ``applyDisplay``. |
| tui | ui-tui\src\app\useConfigSync.ts | 116 | English string, visibility unknown | const cfg = await quietRpc<ConfigFullResponse>(gw, 'config.get', { key: 'full' }) |
| tui | ui-tui\src\app\useConfigSync.ts | 132 | English string, visibility unknown | // config payload. ``quietRpc()`` collapses failures to ``null``; if we |
| tui | ui-tui\src\app\useConfigSync.ts | 136 | English string, visibility unknown | // ``mtimeRef`` before this call, so staying silent on null preserves |
| tui | ui-tui\src\app\useConfigSync.ts | 179 | English string, visibility unknown | quietRpc<ConfigMtimeResponse>(gw, 'config.get', { key: 'mtime' }).then(r => { |
| tui | ui-tui\src\app\useConfigSync.ts | 191 | English string, visibility unknown | quietRpc<ConfigMtimeResponse>(gw, 'config.get', { key: 'mtime' }).then(r => { |
| tui | ui-tui\src\app\useInputHandlers.ts | 1 | English string, visibility unknown | import { forceRedraw, useInput } from '@hermes/ink' |
| tui | ui-tui\src\app\useInputHandlers.ts | 2 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\app\useInputHandlers.ts | 3 | English string, visibility unknown | import { useEffect, useRef } from 'react' |
| tui | ui-tui\src\app\useInputHandlers.ts | 12 | English string, visibility unknown | } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\useInputHandlers.ts | 13 | English string, visibility unknown | import { isAction, isCopyShortcut, isMac, isVoiceToggleKey } from '../lib/platform.js' |
| tui | ui-tui\src\app\useInputHandlers.ts | 14 | English string, visibility unknown | import { computePrecisionWheelStep, initPrecisionWheel } from '../lib/precisionWheel.js' |
| tui | ui-tui\src\app\useInputHandlers.ts | 15 | English string, visibility unknown | import { computeWheelStep, initWheelAccelForHost } from '../lib/wheelAccel.js' |
| tui | ui-tui\src\app\useInputHandlers.ts | 17 | English string, visibility unknown | import { getInputSelection } from './inputSelectionStore.js' |
| tui | ui-tui\src\app\useInputHandlers.ts | 18 | English string, visibility unknown | import type { InputHandlerContext, InputHandlerResult } from './interfaces.js' |
| tui | ui-tui\src\app\useInputHandlers.ts | 19 | English string, visibility unknown | import { $isBlocked, $overlayState, patchOverlayState } from './overlayStore.js' |
| tui | ui-tui\src\app\useInputHandlers.ts | 20 | English string, visibility unknown | import { turnController } from './turnController.js' |
| tui | ui-tui\src\app\useInputHandlers.ts | 21 | English string, visibility unknown | import { patchTurnState } from './turnStore.js' |
| tui | ui-tui\src\app\useInputHandlers.ts | 22 | English string, visibility unknown | import { getUiState } from './uiStore.js' |
| tui | ui-tui\src\app\useInputHandlers.ts | 27 | English string, visibility unknown | * Approval / clarify / confirm overlays mount their own `useInput` handlers |
| tui | ui-tui\src\app\useInputHandlers.ts | 65 | English string, visibility unknown | voice: Pick<InputHandlerContext['voice'], 'setProcessing' \| 'setRecording'>, |
| tui | ui-tui\src\app\useInputHandlers.ts | 68 | English string, visibility unknown | if (!starting \|\| response?.status === 'recording') { |
| tui | ui-tui\src\app\useInputHandlers.ts | 74 | English string, visibility unknown | if (response?.status === 'busy') { |
| tui | ui-tui\src\app\useInputHandlers.ts | 131 | English string, visibility unknown | .then(r => r && (patchOverlayState({ approval: null }), patchTurnState({ outcome: 'denied' }))) |
| tui | ui-tui\src\app\useInputHandlers.ts | 136 | English string, visibility unknown | .rpc<SudoRespondResponse>('sudo.respond', { password: '', request_id: overlay.sudo.requestId }) |
| tui | ui-tui\src\app\useInputHandlers.ts | 142 | English string, visibility unknown | .rpc<SecretRespondResponse>('secret.respond', { request_id: overlay.secret.requestId, value: '' }) |
| tui | ui-tui\src\app\useInputHandlers.ts | 230 | English string, visibility unknown | const action = starting ? 'start' : 'stop' |
| tui | ui-tui\src\app\useInputHandlers.ts | 287 | English string, visibility unknown | const move = (delta: number \| 'top' \| 'bottom') => |
| tui | ui-tui\src\app\useInputHandlers.ts | 295 | English string, visibility unknown | const step = delta === 'top' ? -lines.length : delta === 'bottom' ? lines.length : delta |
| tui | ui-tui\src\app\useInputHandlers.ts | 314 | English string, visibility unknown | return move('top') |
| tui | ui-tui\src\app\useInputHandlers.ts | 318 | English string, visibility unknown | return move('bottom') |
| tui | ui-tui\src\app\useInputHandlers.ts | 331 | English string, visibility unknown | // to `max` so the offset matches what the line/page-back handlers |
| tui | ui-tui\src\app\useInputHandlers.ts | 420 | English string, visibility unknown | // explicitly promises "Esc cancel", so honoring it takes priority over the |
| tui | ui-tui\src\app\useInputHandlers.ts | 517 | English string, visibility unknown | if (ch.toLowerCase() === 'g' && (isAction(key, ch, 'g') \|\| key.meta)) { |
| tui | ui-tui\src\app\useInputHandlers.ts | 551 | English string, visibility unknown | cState.input.startsWith('/') && row.text.startsWith('/') && cState.compReplace > 0 |
| tui | ui-tui\src\app\useLongRunToolCharms.ts | 1 | English string, visibility unknown | import { useEffect, useRef } from 'react' |
| tui | ui-tui\src\app\useLongRunToolCharms.ts | 4 | English string, visibility unknown | import { pick, toolTrailLabel } from '../lib/text.js' |
| tui | ui-tui\src\app\useLongRunToolCharms.ts | 6 | English string, visibility unknown | import { turnController } from './turnController.js' |
| tui | ui-tui\src\app\useLongRunToolCharms.ts | 7 | English string, visibility unknown | import { useTurnSelector } from './turnStore.js' |
| tui | ui-tui\src\app\useLongRunToolCharms.ts | 8 | English string, visibility unknown | import { getUiState } from './uiStore.js' |
| tui | ui-tui\src\app\useMainApp.ts | 1 | English string, visibility unknown | import { useApp, useHasSelection, useSelection, useStdout, useTerminalTitle, type ScrollBoxHandle } from '@hermes/ink' |
| tui | ui-tui\src\app\useMainApp.ts | 2 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\app\useMainApp.ts | 3 | English string, visibility unknown | import { useCallback, useEffect, useMemo, useRef, useState } from 'react' |
| tui | ui-tui\src\app\useMainApp.ts | 8 | English string, visibility unknown | import { attachedImageNotice, imageTokenMeta } from '../domain/messages.js' |
| tui | ui-tui\src\app\useMainApp.ts | 9 | English string, visibility unknown | import { fmtCwdBranch, shortCwd } from '../domain/paths.js' |
| tui | ui-tui\src\app\useMainApp.ts | 10 | English string, visibility unknown | import { type GatewayClient } from '../gatewayClient.js' |
| tui | ui-tui\src\app\useMainApp.ts | 16 | English string, visibility unknown | } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\useMainApp.ts | 17 | English string, visibility unknown | import { useGitBranch } from '../hooks/useGitBranch.js' |
| tui | ui-tui\src\app\useMainApp.ts | 18 | English string, visibility unknown | import { useVirtualHistory } from '../hooks/useVirtualHistory.js' |
| tui | ui-tui\src\app\useMainApp.ts | 19 | English string, visibility unknown | import { composerPromptWidth } from '../lib/inputMetrics.js' |
| tui | ui-tui\src\app\useMainApp.ts | 20 | English string, visibility unknown | import { appendTranscriptMessage } from '../lib/messages.js' |
| tui | ui-tui\src\app\useMainApp.ts | 22 | English string, visibility unknown | import { asRpcResult, rpcErrorMessage } from '../lib/rpc.js' |
| tui | ui-tui\src\app\useMainApp.ts | 23 | English string, visibility unknown | import { terminalParityHints } from '../lib/terminalParity.js' |
| tui | ui-tui\src\app\useMainApp.ts | 24 | English string, visibility unknown | import { buildToolTrailLine, sameToolTrailGroup, toolTrailLabel } from '../lib/text.js' |
| tui | ui-tui\src\app\useMainApp.ts | 25 | English string, visibility unknown | import { estimatedMsgHeight, messageHeightKey } from '../lib/virtualHeights.js' |
| tui | ui-tui\src\app\useMainApp.ts | 26 | English string, visibility unknown | import type { Msg, PanelSection, SlashCatalog } from '../types.js' |
| tui | ui-tui\src\app\useMainApp.ts | 28 | English string, visibility unknown | import { createGatewayEventHandler } from './createGatewayEventHandler.js' |
| tui | ui-tui\src\app\useMainApp.ts | 29 | English string, visibility unknown | import { createSlashHandler } from './createSlashHandler.js' |
| tui | ui-tui\src\app\useMainApp.ts | 30 | English string, visibility unknown | import { getInputSelection } from './inputSelectionStore.js' |
| tui | ui-tui\src\app\useMainApp.ts | 31 | English string, visibility unknown | import { type GatewayRpc, type TranscriptRow } from './interfaces.js' |
| tui | ui-tui\src\app\useMainApp.ts | 32 | English string, visibility unknown | import { $overlayState, patchOverlayState } from './overlayStore.js' |
| tui | ui-tui\src\app\useMainApp.ts | 33 | English string, visibility unknown | import { scrollWithSelectionBy } from './scroll.js' |
| tui | ui-tui\src\app\useMainApp.ts | 34 | English string, visibility unknown | import { turnController } from './turnController.js' |
| tui | ui-tui\src\app\useMainApp.ts | 35 | English string, visibility unknown | import { patchTurnState, useTurnSelector } from './turnStore.js' |
| tui | ui-tui\src\app\useMainApp.ts | 36 | English string, visibility unknown | import { $uiState, getUiState, patchUiState } from './uiStore.js' |
| tui | ui-tui\src\app\useMainApp.ts | 37 | English string, visibility unknown | import { useComposerState } from './useComposerState.js' |
| tui | ui-tui\src\app\useMainApp.ts | 38 | English string, visibility unknown | import { useConfigSync } from './useConfigSync.js' |
| tui | ui-tui\src\app\useMainApp.ts | 39 | English string, visibility unknown | import { useInputHandlers } from './useInputHandlers.js' |
| tui | ui-tui\src\app\useMainApp.ts | 40 | English string, visibility unknown | import { useLongRunToolCharms } from './useLongRunToolCharms.js' |
| tui | ui-tui\src\app\useMainApp.ts | 41 | English string, visibility unknown | import { useSessionLifecycle } from './useSessionLifecycle.js' |
| tui | ui-tui\src\app\useMainApp.ts | 42 | English string, visibility unknown | import { useSubmission } from './useSubmission.js' |
| tui | ui-tui\src\app\useMainApp.ts | 58 | English string, visibility unknown | if (status === 'ready') { |
| tui | ui-tui\src\app\useMainApp.ts | 62 | English string, visibility unknown | if (status.startsWith('error')) { |
| tui | ui-tui\src\app\useMainApp.ts | 66 | English string, visibility unknown | if (status === 'interrupted') { |
| tui | ui-tui\src\app\useMainApp.ts | 85 | English string, visibility unknown | stdout.on('resize', sync) |
| tui | ui-tui\src\app\useMainApp.ts | 92 | English string, visibility unknown | stdout.off('resize', sync) |
| tui | ui-tui\src\app\useMainApp.ts | 100 | English string, visibility unknown | const [historyItems, setHistoryItems] = useState<Msg[]>(() => [{ kind: 'intro', role: 'system', text: '' }]) |
| tui | ui-tui\src\app\useMainApp.ts | 205 | English string, visibility unknown | const empty = !historyItems.some(msg => msg.kind !== 'intro') |
| tui | ui-tui\src\app\useMainApp.ts | 229 | English string, visibility unknown | const next = `${messageHeightKey(msg)}:${++msgIdSeqRef.current}` |
| tui | ui-tui\src\app\useMainApp.ts | 242 | English string, visibility unknown | const thinking = sectionMode('thinking', ui.detailsMode, ui.sections, ui.detailsModeCommandOverride) |
| tui | ui-tui\src\app\useMainApp.ts | 243 | English string, visibility unknown | const tools = sectionMode('tools', ui.detailsMode, ui.sections, ui.detailsModeCommandOverride) |
| tui | ui-tui\src\app\useMainApp.ts | 245 | English string, visibility unknown | return `${thinking}:${tools}` |
| tui | ui-tui\src\app\useMainApp.ts | 248 | English string, visibility unknown | const detailsVisible = detailsLayoutKey !== 'hidden:hidden' |
| tui | ui-tui\src\app\useMainApp.ts | 250 | English string, visibility unknown | const heightCacheKey = `${ui.sid ?? 'draft'}:${cols}:${userPromptWidth}:${ui.compact ? '1' : '0'}:${detailsLayoutKey}` |
| tui | ui-tui\src\app\useMainApp.ts | 270 | English string, visibility unknown | const firstUserIdx = useMemo(() => virtualRows.findIndex(r => r.msg.role === 'user'), [virtualRows]) |
| tui | ui-tui\src\app\useMainApp.ts | 278 | English string, visibility unknown | withSeparator: virtualRows[index]!.msg.role === 'user' && firstUserIdx >= 0 && index > firstUserIdx |
| tui | ui-tui\src\app\useMainApp.ts | 313 | English string, visibility unknown | const sys = useCallback((text: string) => appendMessage({ role: 'system', text }), [appendMessage]) |
| tui | ui-tui\src\app\useMainApp.ts | 322 | English string, visibility unknown | appendMessage({ kind: 'panel', panelData: { sections, title }, role: 'system', text: '' }), |
| tui | ui-tui\src\app\useMainApp.ts | 330 | English string, visibility unknown | if (typeof warning === 'string' && warning) { |
| tui | ui-tui\src\app\useMainApp.ts | 372 | English string, visibility unknown | // alive (stdin listener keeps the event loop open), so the process.on('exit') |
| tui | ui-tui\src\app\useMainApp.ts | 411 | English string, visibility unknown | // Tab title: `⚠` waiting on approval/sudo/secret/clarify, `⏳` busy, `✓` idle. |
| tui | ui-tui\src\app\useMainApp.ts | 414 | English string, visibility unknown | const marker = overlay.approval \|\| overlay.sudo \|\| overlay.secret \|\| overlay.clarify ? '⚠' : ui.busy ? '⏳' : '✓' |
| tui | ui-tui\src\app\useMainApp.ts | 435 | English string, visibility unknown | stdout.on('resize', onResize) |
| tui | ui-tui\src\app\useMainApp.ts | 439 | English string, visibility unknown | stdout.off('resize', onResize) |
| tui | ui-tui\src\app\useMainApp.ts | 451 | English string, visibility unknown | const label = toolTrailLabel('clarify') |
| tui | ui-tui\src\app\useMainApp.ts | 456 | English string, visibility unknown | rpc<ClarifyRespondResponse>('clarify.respond', { answer, request_id: clarify.requestId }).then(r => { |
| tui | ui-tui\src\app\useMainApp.ts | 467 | English string, visibility unknown | tools: [buildToolTrailLine('clarify', clarify.question)] |
| tui | ui-tui\src\app\useMainApp.ts | 469 | English string, visibility unknown | appendMessage({ role: 'user', text: answer }) |
| tui | ui-tui\src\app\useMainApp.ts | 470 | English string, visibility unknown | patchUiState({ status: 'running…' }) |
| tui | ui-tui\src\app\useMainApp.ts | 520 | English string, visibility unknown | // `!sleep` / a failed turn was running would stay stuck forever. |
| tui | ui-tui\src\app\useMainApp.ts | 534 | English string, visibility unknown | patchUiState({ busy: true, status: 'running…' }) |
| tui | ui-tui\src\app\useMainApp.ts | 611 | English string, visibility unknown | patchUiState({ busy: false, sid: null, status: 'gateway exited' }) |
| tui | ui-tui\src\app\useMainApp.ts | 616 | English string, visibility unknown | gw.on('event', handler) |
| tui | ui-tui\src\app\useMainApp.ts | 617 | English string, visibility unknown | gw.on('exit', exitHandler) |
| tui | ui-tui\src\app\useMainApp.ts | 622 | English string, visibility unknown | gw.off('event', handler) |
| tui | ui-tui\src\app\useMainApp.ts | 623 | English string, visibility unknown | gw.off('exit', exitHandler) |
| tui | ui-tui\src\app\useMainApp.ts | 691 | English string, visibility unknown | patchTurnState({ outcome: choice === 'deny' ? 'denied' : `approved (${choice})` }) |
| tui | ui-tui\src\app\useMainApp.ts | 692 | English string, visibility unknown | patchUiState({ status: 'running…' }) |
| tui | ui-tui\src\app\useMainApp.ts | 703 | English string, visibility unknown | return respondWith('sudo.respond', { password: pw, request_id: overlay.sudo.requestId }, () => { |
| tui | ui-tui\src\app\useMainApp.ts | 705 | English string, visibility unknown | patchUiState({ status: 'running…' }) |
| tui | ui-tui\src\app\useMainApp.ts | 717 | English string, visibility unknown | return respondWith('secret.respond', { request_id: overlay.secret.requestId, value }, () => { |
| tui | ui-tui\src\app\useMainApp.ts | 719 | English string, visibility unknown | patchUiState({ status: 'running…' }) |
| tui | ui-tui\src\app\useMainApp.ts | 737 | English string, visibility unknown | s => sectionMode(s, ui.detailsMode, ui.sections, ui.detailsModeCommandOverride) !== 'hidden' |
| tui | ui-tui\src\app\useMainApp.ts | 740 | English string, visibility unknown | sectionMode('thinking', ui.detailsMode, ui.sections, ui.detailsModeCommandOverride) !== 'hidden' |
| tui | ui-tui\src\app\useMainApp.ts | 742 | English string, visibility unknown | sectionMode('tools', ui.detailsMode, ui.sections, ui.detailsModeCommandOverride) !== 'hidden' |
| tui | ui-tui\src\app\useMainApp.ts | 744 | English string, visibility unknown | sectionMode('activity', ui.detailsMode, ui.sections, ui.detailsModeCommandOverride) !== 'hidden' |
| tui | ui-tui\src\app\useMainApp.ts | 756 | English string, visibility unknown | if (segment.kind === 'trail' && !segment.text) { |
| tui | ui-tui\src\app\useMainApp.ts | 775 | English string, visibility unknown | : state.activity.some(item => item.tone !== 'info') |
| tui | ui-tui\src\app\useMainApp.ts | 828 | mixed Chinese and English, visibility unknown | voiceLabel: voiceRecording ? '🎙 录音中' : voiceProcessing ? '📝 转写中' : voiceEnabled ? '🎧 语音开' : '' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 1 | English string, visibility unknown | import { writeFileSync } from 'node:fs' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 3 | English string, visibility unknown | import type { ScrollBoxHandle } from '@hermes/ink' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 4 | English string, visibility unknown | import { evictInkCaches } from '@hermes/ink' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 5 | English string, visibility unknown | import { useCallback, type RefObject } from 'react' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 8 | English string, visibility unknown | import { introMsg, toTranscriptMessages } from '../domain/messages.js' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 10 | English string, visibility unknown | import { type GatewayClient } from '../gatewayClient.js' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 17 | English string, visibility unknown | } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 18 | English string, visibility unknown | import { asRpcResult } from '../lib/rpc.js' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 19 | English string, visibility unknown | import type { Msg, PanelSection, SessionInfo, Usage } from '../types.js' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 21 | English string, visibility unknown | import type { ComposerActions, GatewayRpc, StateSetter } from './interfaces.js' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 22 | English string, visibility unknown | import { patchOverlayState } from './overlayStore.js' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 23 | English string, visibility unknown | import { turnController } from './turnController.js' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 24 | English string, visibility unknown | import { patchTurnState } from './turnStore.js' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 25 | English string, visibility unknown | import { getUiState, patchUiState } from './uiStore.js' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 44 | English string, visibility unknown | while (q.at(-1)?.role === 'assistant' \|\| q.at(-1)?.role === 'tool') { |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 48 | English string, visibility unknown | if (q.at(-1)?.role === 'user') { |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 105 | English string, visibility unknown | evictInkCaches('half') |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 127 | English string, visibility unknown | const setup = await rpc<SetupStatusResponse>('setup.status', {}) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 131 | English string, visibility unknown | patchUiState({ status: 'setup required' }) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 138 | English string, visibility unknown | const r = await rpc<SessionCreateResponse>('session.create', { cols: colsRef.current }) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 141 | English string, visibility unknown | return patchUiState({ status: 'ready' }) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 175 | English string, visibility unknown | rpc<SessionTitleResponse>('session.title', { |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 204 | English string, visibility unknown | patchUiState({ status: 'resuming…' }) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 206 | English string, visibility unknown | rpc<SetupStatusResponse>('setup.status', {}).then(setup => { |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 209 | English string, visibility unknown | patchUiState({ status: 'setup required' }) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 223 | English string, visibility unknown | return patchUiState({ status: 'ready' }) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 243 | English string, visibility unknown | patchUiState({ status: 'ready' }) |
| tui | ui-tui\src\app\useSubmission.ts | 1 | English string, visibility unknown | import { type MutableRefObject, useCallback, useEffect, useRef } from 'react' |
| tui | ui-tui\src\app\useSubmission.ts | 4 | English string, visibility unknown | import { attachedImageNotice } from '../domain/messages.js' |
| tui | ui-tui\src\app\useSubmission.ts | 5 | English string, visibility unknown | import { looksLikeSlashCommand } from '../domain/slash.js' |
| tui | ui-tui\src\app\useSubmission.ts | 6 | English string, visibility unknown | import type { GatewayClient } from '../gatewayClient.js' |
| tui | ui-tui\src\app\useSubmission.ts | 12 | English string, visibility unknown | } from '../gatewayTypes.js' |
| tui | ui-tui\src\app\useSubmission.ts | 13 | English string, visibility unknown | import { asRpcResult } from '../lib/rpc.js' |
| tui | ui-tui\src\app\useSubmission.ts | 16 | English string, visibility unknown | import type { Msg } from '../types.js' |
| tui | ui-tui\src\app\useSubmission.ts | 18 | English string, visibility unknown | import type { ComposerActions, ComposerRefs, ComposerState, PasteSnippet } from './interfaces.js' |
| tui | ui-tui\src\app\useSubmission.ts | 19 | English string, visibility unknown | import { turnController } from './turnController.js' |
| tui | ui-tui\src\app\useSubmission.ts | 20 | English string, visibility unknown | import { getUiState, patchUiState } from './uiStore.js' |
| tui | ui-tui\src\app\useSubmission.ts | 103 | English string, visibility unknown | appendMessage({ role: 'user', text: displayText }) |
| tui | ui-tui\src\app\useSubmission.ts | 106 | English string, visibility unknown | patchUiState({ busy: true, status: 'running…' }) |
| tui | ui-tui\src\app\useSubmission.ts | 110 | English string, visibility unknown | gw.request<PromptSubmitResponse>('prompt.submit', { session_id: sid, text: submitText }).catch((e: Error) => { |
| tui | ui-tui\src\app\useSubmission.ts | 113 | English string, visibility unknown | patchUiState({ busy: true, status: 'queued for next turn' }) |
| tui | ui-tui\src\app\useSubmission.ts | 119 | English string, visibility unknown | patchUiState({ busy: false, status: 'ready' }) |
| tui | ui-tui\src\app\useSubmission.ts | 153 | English string, visibility unknown | appendMessage({ role: 'user', text: `!${cmd}` }) |
| tui | ui-tui\src\app\useSubmission.ts | 154 | English string, visibility unknown | patchUiState({ busy: true, status: 'running…' }) |
| tui | ui-tui\src\app\useSubmission.ts | 156 | English string, visibility unknown | gw.request<ShellExecResponse>('shell.exec', { command: cmd }) |
| tui | ui-tui\src\app\useSubmission.ts | 175 | English string, visibility unknown | .finally(() => patchUiState({ busy: false, status: 'ready' })) |
| tui | ui-tui\src\app\useSubmission.ts | 182 | English string, visibility unknown | patchUiState({ status: 'interpolating…' }) |
| tui | ui-tui\src\app\useSubmission.ts | 188 | English string, visibility unknown | .request<ShellExecResponse>('shell.exec', { command: m[1]! }) |
| tui | ui-tui\src\app\useSubmission.ts | 194 | English string, visibility unknown | .catch(() => '(error)') |
| tui | ui-tui\src\app\useSubmission.ts | 219 | English string, visibility unknown | // - 'queue' (legacy): append to queueRef; drains on busy → false |
| tui | ui-tui\src\app\useSubmission.ts | 220 | English string, visibility unknown | // - 'steer' : inject into the current turn via session.steer; falls |
| tui | ui-tui\src\app\useSubmission.ts | 223 | English string, visibility unknown | // - 'interrupt' (default): cancel the in-flight turn, then send the |
| tui | ui-tui\src\app\useSubmission.ts | 226 | English string, visibility unknown | // `opts.fallbackToFront` controls whether a steer fallback re-inserts |
| tui | ui-tui\src\app\useSubmission.ts | 245 | English string, visibility unknown | if (mode === 'queue') { |
| tui | ui-tui\src\app\useSubmission.ts | 249 | English string, visibility unknown | if (mode === 'steer' && live.sid) { |
| tui | ui-tui\src\app\useSubmission.ts | 250 | English string, visibility unknown | gw.request<SessionSteerResponse>('session.steer', { session_id: live.sid, text: full }) |
| tui | ui-tui\src\app\useSubmission.ts | 254 | English string, visibility unknown | if (r?.status !== 'queued') { |
| tui | ui-tui\src\app\useSubmission.ts | 263 | English string, visibility unknown | // 'interrupt' (default): tear down the current turn, then send. |
| tui | ui-tui\src\app\useSubmission.ts | 264 | English string, visibility unknown | // `interruptTurn` fires `session.interrupt` without awaiting; if |
| tui | ui-tui\src\app\useSubmission.ts | 265 | English string, visibility unknown | // the gateway is still mid-response when `prompt.submit` lands, |
| tui | ui-tui\src\app\useSubmission.ts | 266 | English string, visibility unknown | // `send()`'s catch path re-queues with a "queued: ..." sys note |
| tui | ui-tui\src\app\useSubmission.ts | 267 | English string, visibility unknown | // (`isSessionBusyError`) — so a lost race degrades to queue |
| tui | ui-tui\src\app\useSubmission.ts | 291 | English string, visibility unknown | appendMessage({ kind: 'slash', role: 'system', text: full }) |
| tui | ui-tui\src\app\useSubmission.ts | 329 | English string, visibility unknown | // 'interrupt' / 'steer' should reach the live turn instead of |
| tui | ui-tui\src\app\useSubmission.ts | 332 | English string, visibility unknown | if (getUiState().busyInputMode === 'queue') { |
| tui | ui-tui\src\app\useSubmission.ts | 367 | English string, visibility unknown | const text = value.startsWith('/') && row.text.startsWith('/') ? row.text.slice(1) : row.text |
| tui | ui-tui\src\banner.ts | 1 | English string, visibility unknown | import type { ThemeColors } from './theme.js' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1 | English string, visibility unknown | import { Box, NoSelect, ScrollBox, type ScrollBoxHandle, Text, useInput, useStdout } from '@hermes/ink' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 2 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 3 | English string, visibility unknown | import { type ReactNode, type RefObject, useEffect, useMemo, useRef, useState } from 'react' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 10 | English string, visibility unknown | } from '../app/delegationStore.js' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 11 | English string, visibility unknown | import { patchOverlayState } from '../app/overlayStore.js' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 12 | English string, visibility unknown | import { $spawnDiff, $spawnHistory, clearDiffPair, type SpawnSnapshot } from '../app/spawnHistoryStore.js' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 13 | English string, visibility unknown | import { useTurnSelector } from '../app/turnStore.js' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 14 | English string, visibility unknown | import type { GatewayClient } from '../gatewayClient.js' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 15 | English string, visibility unknown | import type { DelegationPauseResponse, DelegationStatusResponse, SubagentInterruptResponse } from '../gatewayTypes.js' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 16 | English string, visibility unknown | import { asRpcResult } from '../lib/rpc.js' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 31 | English string, visibility unknown | } from '../lib/subagentTree.js' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 32 | English string, visibility unknown | import { compactPreview } from '../lib/text.js' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 33 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 34 | English string, visibility unknown | import type { SubagentNode, SubagentProgress } from '../types.js' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 38 | English string, visibility unknown | type SortMode = 'depth-first' \| 'duration-desc' \| 'status' \| 'tools-desc' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 39 | English string, visibility unknown | type FilterMode = 'all' \| 'failed' \| 'leaf' \| 'running' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 40 | English string, visibility unknown | type Status = SubagentProgress['status'] |
| tui | ui-tui\src\components\agentsOverlay.tsx | 46 | mixed Chinese and English, visibility unknown | 'depth-first': '派生顺序', |
| tui | ui-tui\src\components\agentsOverlay.tsx | 47 | mixed Chinese and English, visibility unknown | 'duration-desc': '最慢', |
| tui | ui-tui\src\components\agentsOverlay.tsx | 49 | mixed Chinese and English, visibility unknown | 'tools-desc': '最忙' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 67 | mixed Chinese and English, visibility unknown | 'subtree tokens': '子树令牌', |
| tui | ui-tui\src\components\agentsOverlay.tsx | 86 | English string, visibility unknown | 'depth-first': (a, b) => a.item.depth - b.item.depth \|\| a.item.index - b.item.index, |
| tui | ui-tui\src\components\agentsOverlay.tsx | 87 | English string, visibility unknown | 'tools-desc': (a, b) => b.aggregate.totalTools - a.aggregate.totalTools, |
| tui | ui-tui\src\components\agentsOverlay.tsx | 88 | English string, visibility unknown | 'duration-desc': (a, b) => b.aggregate.totalDuration - a.aggregate.totalDuration, |
| tui | ui-tui\src\components\agentsOverlay.tsx | 95 | English string, visibility unknown | running: n => n.item.status === 'running' \|\| n.item.status === 'queued', |
| tui | ui-tui\src\components\agentsOverlay.tsx | 97 | English string, visibility unknown | n.item.status === 'error' \|\| |
| tui | ui-tui\src\components\agentsOverlay.tsx | 98 | English string, visibility unknown | n.item.status === 'failed' \|\| |
| tui | ui-tui\src\components\agentsOverlay.tsx | 99 | English string, visibility unknown | n.item.status === 'interrupted' \|\| |
| tui | ui-tui\src\components\agentsOverlay.tsx | 100 | English string, visibility unknown | n.item.status === 'timeout' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 137 | English string, visibility unknown | if (item.startedAt != null && (item.status === 'running' \|\| item.status === 'queued')) { |
| tui | ui-tui\src\components\agentsOverlay.tsx | 172 | English string, visibility unknown | return `${labels[name] ?? name}: ${fmt(a)} → ${fmt(b)} (${sign}${fmt(Math.abs(d)) \|\| '0'})` |
| tui | ui-tui\src\components\agentsOverlay.tsx | 177 | English string, visibility unknown | /** Polled on parent `tick` so accordions can resize the thumb without a scroll event. */ |
| tui | ui-tui\src\components\agentsOverlay.tsx | 207 | English string, visibility unknown | const vBar = (n: number) => (n > 0 ? `${'│\n'.repeat(n - 1)}│` : '') |
| tui | ui-tui\src\components\agentsOverlay.tsx | 208 | English string, visibility unknown | const thumbBody = `${'┃\n'.repeat(Math.max(0, thumb - 1))}┃` |
| tui | ui-tui\src\components\agentsOverlay.tsx | 222 | English string, visibility unknown | flexDirection="column" |
| tui | ui-tui\src\components\agentsOverlay.tsx | 299 | English string, visibility unknown | // 5-col id gutter (" 12 ") so the bar doesn't press against the id. |
| tui | ui-tui\src\components\agentsOverlay.tsx | 313 | English string, visibility unknown | return ' '.repeat(s) + '█'.repeat(fill) + ' '.repeat(Math.max(0, barWidth - s - fill)) |
| tui | ui-tui\src\components\agentsOverlay.tsx | 335 | English string, visibility unknown | const label = pos === 0 ? '0' : secs >= 1 ? `${Math.round(secs)}s` : `${secs.toFixed(1)}s` |
| tui | ui-tui\src\components\agentsOverlay.tsx | 346 | English string, visibility unknown | spans.length > maxRows ? ` (${startIdx + 1}-${Math.min(spans.length, startIdx + maxRows)}/${spans.length})` : '' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 349 | English string, visibility unknown | <Box flexDirection="column" marginBottom={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 364 | English string, visibility unknown | <Text key={node.item.id} wrap="truncate-end"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 414 | English string, visibility unknown | <Box flexDirection="column" marginTop={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 419 | English string, visibility unknown | {typeof count === 'number' ? ` (${count})` : ''} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 423 | English string, visibility unknown | {open ? <Box flexDirection="column">{children}</Box> : null} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 430 | English string, visibility unknown | <Text wrap="truncate-end"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 459 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 460 | English string, visibility unknown | <Text bold color={t.color.text} wrap="wrap"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 465 | English string, visibility unknown | <Box flexDirection="column" marginTop={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 466 | English string, visibility unknown | <Field name="depth" t={t} value={`${item.depth} · ${statusLabel(item.status)}`} /> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 468 | English string, visibility unknown | {item.toolsets?.length ? <Field name="toolsets" t={t} value={item.toolsets.join(', ')} /> : null} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 469 | mixed Chinese and English, visibility unknown | <Field name="tools" t={t} value={`${item.toolCount ?? 0}（子树 ${agg.totalTools}）`} /> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 473 | mixed Chinese and English, visibility unknown | value={`${agg.descendantCount} 个代理 · d${agg.maxDepthFromHere} · ⚡${agg.activeCount}`} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 475 | English string, visibility unknown | {item.durationSeconds ? <Field name="elapsed" t={t} value={fmtDur(item.durationSeconds)} /> : null} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 476 | English string, visibility unknown | {item.iteration != null ? <Field name="iteration" t={t} value={String(item.iteration)} /> : null} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 477 | English string, visibility unknown | {item.apiCalls ? <Field name="api calls" t={t} value={String(item.apiCalls)} /> : null} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 489 | mixed Chinese and English, visibility unknown | {item.reasoningTokens ? ` · ${fmtTokens(item.reasoningTokens)} 推理` : ''} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 502 | mixed Chinese and English, visibility unknown | {subtreeCost >= 0.01 ? ` · 子树 +${fmtCost(subtreeCost)}` : ''} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 508 | English string, visibility unknown | {subtreeTokens > 0 ? <Field name="subtree tokens" t={t} value={`+${fmtTokens(subtreeTokens)}`} /> : null} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 515 | English string, visibility unknown | <Text color={t.color.statusGood} key={`w-${i}`} wrap="truncate-end"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 521 | English string, visibility unknown | <Text color={t.color.text} key={`r-${i}`} wrap="truncate-end"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 533 | English string, visibility unknown | <Text color={t.color.text} key={i} wrap="wrap"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 543 | English string, visibility unknown | <Text color={entry.isError ? t.color.error : t.color.text} key={i} wrap="wrap"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 556 | English string, visibility unknown | <Text color={t.color.text} key={i} wrap="wrap"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 565 | English string, visibility unknown | <Text color={t.color.text} wrap="wrap"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 595 | English string, visibility unknown | const toolsCount = node.aggregate.totalTools > 0 ? ` ·🛠${node.aggregate.totalTools}` : '' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 596 | English string, visibility unknown | const kids = node.children.length ? ` ·${node.children.length}↓` : '' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 597 | English string, visibility unknown | const line = node.item.status === 'running' ? node.item.tools.at(-1) : undefined |
| tui | ui-tui\src\components\agentsOverlay.tsx | 600 | English string, visibility unknown | const trailing = toolShort ? ` · ${compactPreview(toolShort, 14)}` : '' |
| tui | ui-tui\src\components\agentsOverlay.tsx | 604 | English string, visibility unknown | <Text bold={active} color={fg} inverse={active} wrap="truncate-end"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 633 | English string, visibility unknown | <Box flexDirection="column" width={width}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 638 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 643 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 648 | English string, visibility unknown | <Box flexDirection="column" marginTop={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 655 | English string, visibility unknown | <Text color={t.color.muted} key={s.id} wrap="truncate-end"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 691 | English string, visibility unknown | <Box flexDirection="column" flexGrow={1} paddingX={1} paddingY={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 692 | English string, visibility unknown | <Box flexDirection="column" marginBottom={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 699 | English string, visibility unknown | <Box flexDirection="row" marginBottom={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 705 | English string, visibility unknown | <Box flexDirection="column" marginTop={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 711 | English string, visibility unknown | {diffMetricLine('agents', aTotals.descendantCount, bTotals.descendantCount, round)} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 713 | English string, visibility unknown | <Text color={t.color.text}>{diffMetricLine('tools', aTotals.totalTools, bTotals.totalTools, round)}</Text> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 715 | English string, visibility unknown | {diffMetricLine('depth', aTotals.maxDepthFromHere, bTotals.maxDepthFromHere, round)} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 718 | English string, visibility unknown | {diffMetricLine('duration', aTotals.totalDuration, bTotals.totalDuration, n => `${n.toFixed(1)}s`)} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 720 | English string, visibility unknown | <Text color={t.color.text}>{diffMetricLine('tokens', sumTokens(aTotals), sumTokens(bTotals), fmtTokens)}</Text> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 721 | English string, visibility unknown | <Text color={t.color.text}>{diffMetricLine('cost', aTotals.costUsd, bTotals.costUsd, dollars)}</Text> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 742 | English string, visibility unknown | const [sort, setSort] = useState<SortMode>('depth-first') |
| tui | ui-tui\src\components\agentsOverlay.tsx | 743 | English string, visibility unknown | const [filter, setFilter] = useState<FilterMode>('all') |
| tui | ui-tui\src\components\agentsOverlay.tsx | 749 | English string, visibility unknown | const [mode, setMode] = useState<'detail' \| 'list'>('list') |
| tui | ui-tui\src\components\agentsOverlay.tsx | 758 | English string, visibility unknown | // a one-frame "no subagents" flash while the auto-follow effect fires. |
| tui | ui-tui\src\components\agentsOverlay.tsx | 798 | English string, visibility unknown | // "had live subagents" → "live empty" while in live mode. |
| tui | ui-tui\src\components\agentsOverlay.tsx | 816 | English string, visibility unknown | gw.request<DelegationStatusResponse>('delegation.status', {}) |
| tui | ui-tui\src\components\agentsOverlay.tsx | 853 | mixed Chinese and English, visibility unknown | setFlash(`正在终止子树 · ${ids.length} 个节点`) |
| tui | ui-tui\src\components\agentsOverlay.tsx | 858 | English string, visibility unknown | gw.request<DelegationPauseResponse>('delegation.pause', { paused: !delegation.paused }) |
| tui | ui-tui\src\components\agentsOverlay.tsx | 873 | mixed Chinese and English, visibility unknown | setFlash(next === 0 ? '当前实时轮次' : `回放 · ${next}/${history.length}`) |
| tui | ui-tui\src\components\agentsOverlay.tsx | 896 | English string, visibility unknown | return mode === 'detail' ? setMode('list') : closeWithCleanup() |
| tui | ui-tui\src\components\agentsOverlay.tsx | 920 | English string, visibility unknown | if (mode === 'detail') { |
| tui | ui-tui\src\components\agentsOverlay.tsx | 922 | English string, visibility unknown | return setMode('list') |
| tui | ui-tui\src\components\agentsOverlay.tsx | 962 | English string, visibility unknown | return setMode('detail') |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1006 | mixed Chinese and English, visibility unknown | ? `限制 d${delegation.maxSpawnDepth}/${delegation.maxConcurrentChildren ?? '?'}` |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1011 | mixed Chinese and English, visibility unknown | ? `${historyIndex > 0 ? `回放 ${historyIndex}/${history.length}` : '上一轮'} · 完成于 ${new Date( |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1014 | mixed Chinese and English, visibility unknown | : `派生树${delegation.paused ? ' · ⏸ 已暂停' : ''}` |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1016 | English string, visibility unknown | const metaLine = [formatSummary(totals), spark, capsLabel, mix ? `· ${mix}` : ''].filter(Boolean).join(' ') |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1020 | mixed Chinese and English, visibility unknown | : ` · x 终止 · X 子树 · p ${delegation.paused ? '恢复' : '暂停'}` |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1029 | English string, visibility unknown | <Box alignItems="stretch" flexDirection="column" flexGrow={1} paddingX={1} paddingY={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1030 | English string, visibility unknown | <Box flexDirection="column" marginBottom={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1031 | English string, visibility unknown | <Text wrap="truncate-end"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1045 | English string, visibility unknown | <Box flexDirection="column" flexGrow={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1048 | English string, visibility unknown | ) : mode === 'list' ? ( |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1049 | English string, visibility unknown | <Box flexDirection="column" flexGrow={1} flexShrink={1} minHeight={0}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1052 | English string, visibility unknown | <Box flexDirection="column" flexGrow={0} flexShrink={0} overflow="hidden"> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1067 | English string, visibility unknown | <Box flexDirection="row" flexGrow={1} flexShrink={1} minHeight={0}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1068 | English string, visibility unknown | <ScrollBox flexDirection="column" flexGrow={1} flexShrink={1} ref={detailScrollRef}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1069 | English string, visibility unknown | <Box flexDirection="column" paddingBottom={4} paddingRight={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1080 | English string, visibility unknown | <Box flexDirection="column" marginTop={1}> |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1083 | English string, visibility unknown | {mode === 'list' ? ( |
| tui | ui-tui\src\components\agentsOverlay.tsx | 1087 | mixed Chinese and English, visibility unknown | {history.length > 0 ? ` · [ / ] 历史 ${historyIndex}/${history.length}` : ''} |
| tui | ui-tui\src\components\appChrome.tsx | 1 | English string, visibility unknown | import { Box, type ScrollBoxHandle, Text } from '@hermes/ink' |
| tui | ui-tui\src\components\appChrome.tsx | 2 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\components\appChrome.tsx | 3 | English string, visibility unknown | import { type ReactNode, type RefObject, useEffect, useMemo, useRef, useState } from 'react' |
| tui | ui-tui\src\components\appChrome.tsx | 4 | English string, visibility unknown | import unicodeSpinners from 'unicode-animations' |
| tui | ui-tui\src\components\appChrome.tsx | 6 | English string, visibility unknown | import { $delegationState } from '../app/delegationStore.js' |
| tui | ui-tui\src\components\appChrome.tsx | 7 | English string, visibility unknown | import type { IndicatorStyle } from '../app/interfaces.js' |
| tui | ui-tui\src\components\appChrome.tsx | 8 | English string, visibility unknown | import type { TuiModulesState } from '../app/tuiModules.js' |
| tui | ui-tui\src\components\appChrome.tsx | 9 | English string, visibility unknown | import { useTurnSelector } from '../app/turnStore.js' |
| tui | ui-tui\src\components\appChrome.tsx | 10 | English string, visibility unknown | import { $uiState } from '../app/uiStore.js' |
| tui | ui-tui\src\components\appChrome.tsx | 13 | English string, visibility unknown | import { fmtDuration } from '../domain/messages.js' |
| tui | ui-tui\src\components\appChrome.tsx | 14 | English string, visibility unknown | import { stickyPromptFromViewport } from '../domain/viewport.js' |
| tui | ui-tui\src\components\appChrome.tsx | 15 | English string, visibility unknown | import { buildSubagentTree, treeTotals, widthByDepth } from '../lib/subagentTree.js' |
| tui | ui-tui\src\components\appChrome.tsx | 16 | English string, visibility unknown | import { fmtK } from '../lib/text.js' |
| tui | ui-tui\src\components\appChrome.tsx | 17 | English string, visibility unknown | import { useScrollbarSnapshot, useViewportSnapshot } from '../lib/viewportStore.js' |
| tui | ui-tui\src\components\appChrome.tsx | 18 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\appChrome.tsx | 19 | English string, visibility unknown | import type { Msg, Usage } from '../types.js' |
| tui | ui-tui\src\components\appChrome.tsx | 31 | English string, visibility unknown | // Compact alternates for the `emoji` and `ascii` indicator styles. |
| tui | ui-tui\src\components\appChrome.tsx | 44 | English string, visibility unknown | // glyph + duration. Lets `unicode` stay minimal while the other |
| tui | ui-tui\src\components\appChrome.tsx | 51 | English string, visibility unknown | if (style === 'kaomoji') { |
| tui | ui-tui\src\components\appChrome.tsx | 58 | English string, visibility unknown | if (style === 'emoji') { |
| tui | ui-tui\src\components\appChrome.tsx | 66 | English string, visibility unknown | if (style === 'ascii') { |
| tui | ui-tui\src\components\appChrome.tsx | 74 | English string, visibility unknown | // 'unicode' — braille spinner (fixed 1-col). Authored interval is |
| tui | ui-tui\src\components\appChrome.tsx | 94 | English string, visibility unknown | // `/indicator` switch re-arms the interval (and skips the verb timer |
| tui | ui-tui\src\components\appChrome.tsx | 95 | English string, visibility unknown | // for verb-less styles like `unicode`) without leaving the previous |
| tui | ui-tui\src\components\appChrome.tsx | 102 | English string, visibility unknown | // Verb timer is gated on `showVerb` — `unicode` style hides the verb |
| tui | ui-tui\src\components\appChrome.tsx | 103 | English string, visibility unknown | // entirely, so cycling `verbTick` would be an avoidable re-render. |
| tui | ui-tui\src\components\appChrome.tsx | 118 | English string, visibility unknown | const verbSegment = showVerb ? ` ${padVerb(verb, verbPadWidth)}` : '' |
| tui | ui-tui\src\components\appChrome.tsx | 120 | English string, visibility unknown | // verb segment is hidden (e.g. `unicode` spinner style). When the verb |
| tui | ui-tui\src\components\appChrome.tsx | 123 | English string, visibility unknown | const durationSegment = startedAt ? ` · ${fmtDuration(now - startedAt)}` : '' |
| tui | ui-tui\src\components\appChrome.tsx | 158 | English string, visibility unknown | return '█'.repeat(filled) + '░'.repeat(w - filled) |
| tui | ui-tui\src\components\appChrome.tsx | 192 | English string, visibility unknown | // `max_concurrent_children` is a per-parent cap, not a global one. |
| tui | ui-tui\src\components\appChrome.tsx | 193 | English string, visibility unknown | // `activeCount` sums every running agent across the tree and would |
| tui | ui-tui\src\components\appChrome.tsx | 196 | English string, visibility unknown | // single parent's slot budget". |
| tui | ui-tui\src\components\appChrome.tsx | 211 | English string, visibility unknown | const depthLabel = maxDepth ? `${depth}/${maxDepth}` : `${depth}` |
| tui | ui-tui\src\components\appChrome.tsx | 212 | mixed Chinese and English, visibility unknown | pieces.push(`🌿 层${depthLabel}`) |
| tui | ui-tui\src\components\appChrome.tsx | 216 | English string, visibility unknown | // the total active count for context. `W/cap` triggers the warn, |
| tui | ui-tui\src\components\appChrome.tsx | 219 | English string, visibility unknown | const widthLabel = maxConc ? `${widestLevel}/${maxConc}` : `${widestLevel}` |
| tui | ui-tui\src\components\appChrome.tsx | 220 | English string, visibility unknown | const suffix = extra > 0 ? `+${extra}` : '' |
| tui | ui-tui\src\components\appChrome.tsx | 221 | English string, visibility unknown | pieces.push(`⚡${widthLabel}${suffix}`) |
| tui | ui-tui\src\components\appChrome.tsx | 236 | mixed Chinese and English, visibility unknown | 'forging session…': '正在创建会话…', |
| tui | ui-tui\src\components\appChrome.tsx | 237 | mixed Chinese and English, visibility unknown | 'gateway exited': '网关已退出', |
| tui | ui-tui\src\components\appChrome.tsx | 238 | mixed Chinese and English, visibility unknown | 'gateway startup timeout': '网关启动超时', |
| tui | ui-tui\src\components\appChrome.tsx | 239 | mixed Chinese and English, visibility unknown | 'interpolating…': '正在插入命令输出…', |
| tui | ui-tui\src\components\appChrome.tsx | 240 | mixed Chinese and English, visibility unknown | 'protocol warning': '协议警告', |
| tui | ui-tui\src\components\appChrome.tsx | 242 | mixed Chinese and English, visibility unknown | 'queued for next turn': '已排队到下一轮', |
| tui | ui-tui\src\components\appChrome.tsx | 245 | mixed Chinese and English, visibility unknown | 'resuming most recent…': '正在恢复最近会话…', |
| tui | ui-tui\src\components\appChrome.tsx | 246 | mixed Chinese and English, visibility unknown | 'resuming…': '正在恢复…', |
| tui | ui-tui\src\components\appChrome.tsx | 247 | mixed Chinese and English, visibility unknown | 'running…': '运行中…', |
| tui | ui-tui\src\components\appChrome.tsx | 248 | mixed Chinese and English, visibility unknown | 'setup required': '需要设置', |
| tui | ui-tui\src\components\appChrome.tsx | 249 | mixed Chinese and English, visibility unknown | 'setup running…': '正在设置…', |
| tui | ui-tui\src\components\appChrome.tsx | 250 | mixed Chinese and English, visibility unknown | 'starting agent…': '正在启动助手…', |
| tui | ui-tui\src\components\appChrome.tsx | 251 | mixed Chinese and English, visibility unknown | 'summoning hermes…': '正在启动 Hermes…', |
| tui | ui-tui\src\components\appChrome.tsx | 252 | mixed Chinese and English, visibility unknown | 'waiting for input…': '等待输入…', |
| tui | ui-tui\src\components\appChrome.tsx | 253 | mixed Chinese and English, visibility unknown | 'approval needed': '需要确认', |
| tui | ui-tui\src\components\appChrome.tsx | 254 | mixed Chinese and English, visibility unknown | 'sudo password needed': '需要 sudo 密码', |
| tui | ui-tui\src\components\appChrome.tsx | 255 | mixed Chinese and English, visibility unknown | 'secret input needed': '需要输入密钥', |
| tui | ui-tui\src\components\appChrome.tsx | 256 | mixed Chinese and English, visibility unknown | '✓ goal complete': '✓ 目标完成', |
| tui | ui-tui\src\components\appChrome.tsx | 257 | mixed Chinese and English, visibility unknown | '↻ goal continuing': '↻ 目标继续', |
| tui | ui-tui\src\components\appChrome.tsx | 258 | mixed Chinese and English, visibility unknown | '⏸ goal paused': '⏸ 目标暂停' |
| tui | ui-tui\src\components\appChrome.tsx | 268 | mixed Chinese and English, visibility unknown | return status.startsWith('error') ? status.replace(/^error/, '错误') : status |
| tui | ui-tui\src\components\appChrome.tsx | 276 | English string, visibility unknown | return value && value !== 'medium' && value !== 'normal' && value !== 'default' ? value : '' |
| tui | ui-tui\src\components\appChrome.tsx | 293 | mixed Chinese and English, visibility unknown | label.includes('录音') ? t.color.error : label.includes('转写') ? t.color.warn : t.color.statusFg |
| tui | ui-tui\src\components\appChrome.tsx | 342 | English string, visibility unknown | ? `${fmtK(usage.context_used ?? 0)}/${fmtK(usage.context_max)}` |
| tui | ui-tui\src\components\appChrome.tsx | 344 | mixed Chinese and English, visibility unknown | ? `${fmtK(usage.total)} 令牌` |
| tui | ui-tui\src\components\appChrome.tsx | 351 | English string, visibility unknown | const cwdDisplay = `📁 ${cwdLabel}` |
| tui | ui-tui\src\components\appChrome.tsx | 365 | English string, visibility unknown | const showActivityScan = activityScan.enabled && activityScan.slot === 'status.left' && cols >= activityScan.minCols |
| tui | ui-tui\src\components\appChrome.tsx | 366 | English string, visibility unknown | const showStatusMeter = statusMeter.enabled && statusMeter.slot === 'status.center' && cols >= statusMeter.minCols |
| tui | ui-tui\src\components\appChrome.tsx | 371 | English string, visibility unknown | <Text color={t.color.border} wrap="truncate-end"> |
| tui | ui-tui\src\components\appChrome.tsx | 386 | English string, visibility unknown | <Text color={t.color.statusDim} wrap="truncate-end"> |
| tui | ui-tui\src\components\appChrome.tsx | 395 | English string, visibility unknown | <Text color={barColor}> {pct != null ? `${pct}%` : ''}</Text> |
| tui | ui-tui\src\components\appChrome.tsx | 414 | English string, visibility unknown | {showStatusMeter && typeof usage.compressions === 'number' && usage.compressions > 0 ? ( |
| tui | ui-tui\src\components\appChrome.tsx | 424 | English string, visibility unknown | {showStatusMeter && showCost && typeof usage.cost_usd === 'number' ? ( |
| tui | ui-tui\src\components\appChrome.tsx | 434 | English string, visibility unknown | <Text wrap="truncate-end"> |
| tui | ui-tui\src\components\appChrome.tsx | 448 | English string, visibility unknown | alignSelf="flex-start" |
| tui | ui-tui\src\components\appChrome.tsx | 450 | English string, visibility unknown | borderStyle="double" |
| tui | ui-tui\src\components\appChrome.tsx | 451 | English string, visibility unknown | flexDirection="column" |
| tui | ui-tui\src\components\appChrome.tsx | 498 | English string, visibility unknown | flexDirection="column" |
| tui | ui-tui\src\components\appChrome.tsx | 520 | English string, visibility unknown | {' \n'.repeat(Math.max(0, vp - 1))}{' '} |
| tui | ui-tui\src\components\appChrome.tsx | 526 | English string, visibility unknown | {`${'│\n'.repeat(Math.max(0, thumbTop - 1))}${thumbTop > 0 ? '│' : ''}`} |
| tui | ui-tui\src\components\appChrome.tsx | 530 | English string, visibility unknown | <Text color={thumbColor}>{`${'┃\n'.repeat(Math.max(0, thumb - 1))}${thumb > 0 ? '┃' : ''}`}</Text> |
| tui | ui-tui\src\components\appChrome.tsx | 534 | English string, visibility unknown | {`${'│\n'.repeat(Math.max(0, vp - thumbTop - thumb - 1))}${vp - thumbTop - thumb > 0 ? '│' : ''}`} |
| tui | ui-tui\src\components\appLayout.tsx | 1 | English string, visibility unknown | import { AlternateScreen, Box, NoSelect, ScrollBox, Text } from '@hermes/ink' |
| tui | ui-tui\src\components\appLayout.tsx | 2 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\components\appLayout.tsx | 3 | English string, visibility unknown | import { Fragment, memo, useMemo, useRef } from 'react' |
| tui | ui-tui\src\components\appLayout.tsx | 5 | English string, visibility unknown | import { useGateway } from '../app/gatewayContext.js' |
| tui | ui-tui\src\components\appLayout.tsx | 6 | English string, visibility unknown | import type { AppLayoutProps } from '../app/interfaces.js' |
| tui | ui-tui\src\components\appLayout.tsx | 7 | English string, visibility unknown | import { $isBlocked, $overlayState, patchOverlayState } from '../app/overlayStore.js' |
| tui | ui-tui\src\components\appLayout.tsx | 8 | English string, visibility unknown | import { $uiState } from '../app/uiStore.js' |
| tui | ui-tui\src\components\appLayout.tsx | 16 | English string, visibility unknown | } from '../lib/inputMetrics.js' |
| tui | ui-tui\src\components\appLayout.tsx | 17 | English string, visibility unknown | import { PerfPane } from '../lib/perfPane.js' |
| tui | ui-tui\src\components\appLayout.tsx | 18 | English string, visibility unknown | import { composerPromptText } from '../lib/prompt.js' |
| tui | ui-tui\src\components\appLayout.tsx | 20 | English string, visibility unknown | import { AgentsOverlay } from './agentsOverlay.js' |
| tui | ui-tui\src\components\appLayout.tsx | 21 | English string, visibility unknown | import { GoodVibesHeart, StatusRule, StickyPromptTracker, TranscriptScrollbar } from './appChrome.js' |
| tui | ui-tui\src\components\appLayout.tsx | 22 | English string, visibility unknown | import { FloatingOverlays, PromptZone } from './appOverlays.js' |
| tui | ui-tui\src\components\appLayout.tsx | 23 | English string, visibility unknown | import { Banner, Panel, SessionPanel } from './branding.js' |
| tui | ui-tui\src\components\appLayout.tsx | 24 | English string, visibility unknown | import { FpsOverlay } from './fpsOverlay.js' |
| tui | ui-tui\src\components\appLayout.tsx | 25 | English string, visibility unknown | import { HelpHint } from './helpHint.js' |
| tui | ui-tui\src\components\appLayout.tsx | 26 | English string, visibility unknown | import { MessageLine } from './messageLine.js' |
| tui | ui-tui\src\components\appLayout.tsx | 27 | English string, visibility unknown | import { QueuedMessages } from './queuedMessages.js' |
| tui | ui-tui\src\components\appLayout.tsx | 28 | English string, visibility unknown | import { LiveTodoPanel, StreamingAssistant } from './streamingAssistant.js' |
| tui | ui-tui\src\components\appLayout.tsx | 29 | English string, visibility unknown | import { TextInput, type TextInputMouseApi } from './textInput.js' |
| tui | ui-tui\src\components\appLayout.tsx | 30 | English string, visibility unknown | import { TuiModuleDock } from './tuiModuleDock.js' |
| tui | ui-tui\src\components\appLayout.tsx | 62 | English string, visibility unknown | }: Pick<AppLayoutProps, 'actions' \| 'composer' \| 'progress' \| 'transcript'>) { |
| tui | ui-tui\src\components\appLayout.tsx | 72 | English string, visibility unknown | if (items[i].role === 'user') { |
| tui | ui-tui\src\components\appLayout.tsx | 85 | English string, visibility unknown | () => transcript.historyItems.findIndex(m => m.role === 'user'), |
| tui | ui-tui\src\components\appLayout.tsx | 92 | English string, visibility unknown | characterPanel.enabled && characterPanel.slot === 'intro.hero' && composer.cols >= characterPanel.minCols |
| tui | ui-tui\src\components\appLayout.tsx | 97 | English string, visibility unknown | taskPanel.enabled && taskPanel.slot === 'transcript.afterUser' && composer.cols >= taskPanel.minCols |
| tui | ui-tui\src\components\appLayout.tsx | 102 | English string, visibility unknown | flexDirection="column" |
| tui | ui-tui\src\components\appLayout.tsx | 113 | English string, visibility unknown | <Box flexDirection="column" paddingX={1}> |
| tui | ui-tui\src\components\appLayout.tsx | 117 | English string, visibility unknown | <Box flexDirection="column" key={row.key} ref={transcript.virtualHistory.measureRef(row.key)}> |
| tui | ui-tui\src\components\appLayout.tsx | 118 | English string, visibility unknown | {row.msg.role === 'user' && firstUserIdx >= 0 && row.index > firstUserIdx && ( |
| tui | ui-tui\src\components\appLayout.tsx | 124 | English string, visibility unknown | {row.msg.kind === 'intro' ? ( |
| tui | ui-tui\src\components\appLayout.tsx | 125 | English string, visibility unknown | <Box flexDirection="column" paddingTop={1}> |
| tui | ui-tui\src\components\appLayout.tsx | 137 | English string, visibility unknown | ) : row.msg.kind === 'panel' && row.msg.panelData ? ( |
| tui | ui-tui\src\components\appLayout.tsx | 186 | English string, visibility unknown | }: Pick<AppLayoutProps, 'actions' \| 'composer' \| 'status'>) { |
| tui | ui-tui\src\components\appLayout.tsx | 233 | English string, visibility unknown | flexDirection="column" |
| tui | ui-tui\src\components\appLayout.tsx | 259 | English string, visibility unknown | <Text color={ui.theme.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\appLayout.tsx | 268 | English string, visibility unknown | <StatusRulePane at="top" composer={composer} status={status} /> |
| tui | ui-tui\src\components\appLayout.tsx | 270 | English string, visibility unknown | <Box flexDirection="column" marginTop={ui.statusBar === 'top' ? 0 : 1} position="relative"> |
| tui | ui-tui\src\components\appLayout.tsx | 302 | English string, visibility unknown | position="relative" |
| tui | ui-tui\src\components\appLayout.tsx | 329 | English string, visibility unknown | <Box position="absolute" right={0}> |
| tui | ui-tui\src\components\appLayout.tsx | 339 | English string, visibility unknown | <StatusRulePane at="bottom" composer={composer} status={status} /> |
| tui | ui-tui\src\components\appLayout.tsx | 363 | English string, visibility unknown | }: Pick<AppLayoutProps, 'composer' \| 'status'> & { at: 'bottom' \| 'top' }) { |
| tui | ui-tui\src\components\appLayout.tsx | 371 | English string, visibility unknown | <Box marginTop={at === 'top' ? 1 : 0}> |
| tui | ui-tui\src\components\appLayout.tsx | 378 | English string, visibility unknown | modelFast={ui.info?.fast \|\| ui.info?.service_tier === 'priority'} |
| tui | ui-tui\src\components\appLayout.tsx | 413 | English string, visibility unknown | <Box flexDirection="column" flexGrow={1}> |
| tui | ui-tui\src\components\appLayout.tsx | 414 | English string, visibility unknown | <Box flexDirection="row" flexGrow={1}> |
| tui | ui-tui\src\components\appLayout.tsx | 416 | English string, visibility unknown | <PerfPane id="agents"> |
| tui | ui-tui\src\components\appLayout.tsx | 420 | English string, visibility unknown | <PerfPane id="transcript"> |
| tui | ui-tui\src\components\appLayout.tsx | 428 | English string, visibility unknown | <PerfPane id="prompt"> |
| tui | ui-tui\src\components\appLayout.tsx | 438 | English string, visibility unknown | <PerfPane id="composer"> |
| tui | ui-tui\src\components\appLayout.tsx | 443 | English string, visibility unknown | <Box flexShrink={0} justifyContent="flex-end" paddingRight={1}> |
| tui | ui-tui\src\components\appOverlays.tsx | 1 | English string, visibility unknown | import { Box, Text } from '@hermes/ink' |
| tui | ui-tui\src\components\appOverlays.tsx | 2 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\components\appOverlays.tsx | 4 | English string, visibility unknown | import { useGateway } from '../app/gatewayContext.js' |
| tui | ui-tui\src\components\appOverlays.tsx | 5 | English string, visibility unknown | import type { AppOverlaysProps } from '../app/interfaces.js' |
| tui | ui-tui\src\components\appOverlays.tsx | 6 | English string, visibility unknown | import { $overlayState, patchOverlayState } from '../app/overlayStore.js' |
| tui | ui-tui\src\components\appOverlays.tsx | 7 | English string, visibility unknown | import { $uiSessionId, $uiTheme } from '../app/uiStore.js' |
| tui | ui-tui\src\components\appOverlays.tsx | 9 | English string, visibility unknown | import { FloatBox } from './appChrome.js' |
| tui | ui-tui\src\components\appOverlays.tsx | 10 | English string, visibility unknown | import { MaskedPrompt } from './maskedPrompt.js' |
| tui | ui-tui\src\components\appOverlays.tsx | 11 | English string, visibility unknown | import { ModelPicker } from './modelPicker.js' |
| tui | ui-tui\src\components\appOverlays.tsx | 12 | English string, visibility unknown | import { OverlayHint } from './overlayControls.js' |
| tui | ui-tui\src\components\appOverlays.tsx | 13 | English string, visibility unknown | import { ApprovalPrompt, ClarifyPrompt, ConfirmPrompt } from './prompts.js' |
| tui | ui-tui\src\components\appOverlays.tsx | 14 | English string, visibility unknown | import { SessionPicker } from './sessionPicker.js' |
| tui | ui-tui\src\components\appOverlays.tsx | 15 | English string, visibility unknown | import { SkillsHub } from './skillsHub.js' |
| tui | ui-tui\src\components\appOverlays.tsx | 25 | English string, visibility unknown | }: Pick<AppOverlaysProps, 'cols' \| 'onApprovalChoice' \| 'onClarifyAnswer' \| 'onSecretSubmit' \| 'onSudoSubmit'>) { |
| tui | ui-tui\src\components\appOverlays.tsx | 31 | English string, visibility unknown | <Box flexDirection="column" flexShrink={0} paddingX={1} paddingY={1}> |
| tui | ui-tui\src\components\appOverlays.tsx | 48 | English string, visibility unknown | <Box flexDirection="column" flexShrink={0} paddingX={1} paddingY={1}> |
| tui | ui-tui\src\components\appOverlays.tsx | 56 | English string, visibility unknown | <Box flexDirection="column" flexShrink={0} paddingX={1} paddingY={1}> |
| tui | ui-tui\src\components\appOverlays.tsx | 70 | English string, visibility unknown | <Box flexDirection="column" flexShrink={0} paddingX={1} paddingY={1}> |
| tui | ui-tui\src\components\appOverlays.tsx | 71 | English string, visibility unknown | <MaskedPrompt cols={cols} icon="🔐" label="sudo password required" onSubmit={onSudoSubmit} t={theme} /> |
| tui | ui-tui\src\components\appOverlays.tsx | 78 | English string, visibility unknown | <Box flexDirection="column" flexShrink={0} paddingX={1} paddingY={1}> |
| tui | ui-tui\src\components\appOverlays.tsx | 84 | English string, visibility unknown | sub={`for ${overlay.secret.envVar}`} |
| tui | ui-tui\src\components\appOverlays.tsx | 101 | English string, visibility unknown | }: Pick<AppOverlaysProps, 'cols' \| 'compIdx' \| 'completions' \| 'onModelSelect' \| 'onPickerSelect' \| 'pagerPageSize'>) { |
| tui | ui-tui\src\components\appOverlays.tsx | 121 | English string, visibility unknown | <Box alignItems="flex-start" bottom="100%" flexDirection="column" left={0} position="absolute" right={0}> |
| tui | ui-tui\src\components\appOverlays.tsx | 153 | English string, visibility unknown | <Box flexDirection="column" paddingX={1} paddingY={1}> |
| tui | ui-tui\src\components\appOverlays.tsx | 155 | English string, visibility unknown | <Box justifyContent="center" marginBottom={1}> |
| tui | ui-tui\src\components\appOverlays.tsx | 169 | mixed Chinese and English, visibility unknown | ? `↑↓/jk 行 · Enter/Space/PgDn 翻页 · b/PgUp 返回 · g/G 首尾 · Esc/q 关闭 (${Math.min(overlay.pager.offset + pagerPageSize, overlay.pager.lines.length)}/${overlay.pager.lines.length})` |
| tui | ui-tui\src\components\appOverlays.tsx | 170 | mixed Chinese and English, visibility unknown | : `已到底 · ↑↓/jk · b/PgUp 返回 · g 回顶部 · Esc/q 关闭 (${overlay.pager.lines.length} 行)`} |
| tui | ui-tui\src\components\appOverlays.tsx | 179 | English string, visibility unknown | <Box flexDirection="column" width={Math.max(28, cols - 6)}> |
| tui | ui-tui\src\components\appOverlays.tsx | 186 | English string, visibility unknown | flexDirection="row" |
| tui | ui-tui\src\components\appOverlays.tsx | 187 | English string, visibility unknown | key={`${start + i}:${item.text}:${item.display}:${item.meta ?? ''}`} |
| tui | ui-tui\src\components\branding.tsx | 1 | English string, visibility unknown | import { Box, Text, useStdout } from '@hermes/ink' |
| tui | ui-tui\src\components\branding.tsx | 2 | English string, visibility unknown | import { useEffect, useMemo, useState } from 'react' |
| tui | ui-tui\src\components\branding.tsx | 3 | English string, visibility unknown | import unicodeSpinners from 'unicode-animations' |
| tui | ui-tui\src\components\branding.tsx | 6 | English string, visibility unknown | import { flat } from '../lib/text.js' |
| tui | ui-tui\src\components\branding.tsx | 7 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\branding.tsx | 8 | English string, visibility unknown | import type { PanelSection, SessionInfo } from '../types.js' |
| tui | ui-tui\src\components\branding.tsx | 25 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate"> |
| tui | ui-tui\src\components\branding.tsx | 48 | English string, visibility unknown | <Box flexDirection="column" marginBottom={1}> |
| tui | ui-tui\src\components\branding.tsx | 104 | English string, visibility unknown | {typeof count === 'number' ? ( |
| tui | ui-tui\src\components\branding.tsx | 126 | English string, visibility unknown | const strip = (s: string) => (s.endsWith('_tools') ? s.slice(0, -6) : s) |
| tui | ui-tui\src\components\branding.tsx | 139 | English string, visibility unknown | const next = line ? `${line}, ${item}` : item |
| tui | ui-tui\src\components\branding.tsx | 142 | English string, visibility unknown | return line ? `${line}, …+${items.length - shown}` : `${item}, …` |
| tui | ui-tui\src\components\branding.tsx | 168 | English string, visibility unknown | <Text key={k} wrap="truncate"> |
| tui | ui-tui\src\components\branding.tsx | 191 | English string, visibility unknown | <Text key={k} wrap="truncate"> |
| tui | ui-tui\src\components\branding.tsx | 207 | English string, visibility unknown | <Text key={s.name} wrap="truncate"> |
| tui | ui-tui\src\components\branding.tsx | 208 | English string, visibility unknown | <Text color={t.color.muted}>{` ${s.name} `}</Text> |
| tui | ui-tui\src\components\branding.tsx | 209 | English string, visibility unknown | <Text color={t.color.muted}>{`[${s.transport}]`}</Text> |
| tui | ui-tui\src\components\branding.tsx | 239 | English string, visibility unknown | <Box borderColor={t.color.border} borderStyle="round" marginBottom={1} paddingX={2} paddingY={1}> |
| tui | ui-tui\src\components\branding.tsx | 241 | English string, visibility unknown | <Box flexDirection="column" marginRight={2} width={leftW}> |
| tui | ui-tui\src\components\branding.tsx | 250 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\branding.tsx | 263 | English string, visibility unknown | <Box flexDirection="column" width={w}> |
| tui | ui-tui\src\components\branding.tsx | 264 | English string, visibility unknown | <Box justifyContent="center" marginBottom={1}> |
| tui | ui-tui\src\components\branding.tsx | 267 | English string, visibility unknown | {info.version ? ` v${info.version}` : ''} |
| tui | ui-tui\src\components\branding.tsx | 268 | English string, visibility unknown | {info.release_date ? ` (${info.release_date})` : ''} |
| tui | ui-tui\src\components\branding.tsx | 273 | English string, visibility unknown | <Box flexDirection="column" marginTop={1}> |
| tui | ui-tui\src\components\branding.tsx | 278 | mixed Chinese and English, visibility unknown | suffix={toolEntries.length > 0 ? `共 ${toolEntries.length} 个工具集` : undefined} |
| tui | ui-tui\src\components\branding.tsx | 286 | English string, visibility unknown | <Box flexDirection="column" marginTop={1}> |
| tui | ui-tui\src\components\branding.tsx | 291 | mixed Chinese and English, visibility unknown | suffix={skillsCatCount > 0 ? `共 ${skillsCatCount} 个分类` : undefined} |
| tui | ui-tui\src\components\branding.tsx | 300 | English string, visibility unknown | <Box flexDirection="column" marginTop={1}> |
| tui | ui-tui\src\components\branding.tsx | 304 | mixed Chinese and English, visibility unknown | suffix={`— ${sysPromptLen.toLocaleString()} 字符`} |
| tui | ui-tui\src\components\branding.tsx | 314 | English string, visibility unknown | <Box flexDirection="column" marginTop={1}> |
| tui | ui-tui\src\components\branding.tsx | 337 | English string, visibility unknown | {typeof info.update_behind === 'number' && info.update_behind > 0 && ( |
| tui | ui-tui\src\components\branding.tsx | 345 | English string, visibility unknown | {info.update_command \|\| 'hermes update'} |
| tui | ui-tui\src\components\branding.tsx | 360 | English string, visibility unknown | <Box borderColor={t.color.border} borderStyle="round" flexDirection="column" paddingX={2} paddingY={1}> |
| tui | ui-tui\src\components\branding.tsx | 361 | English string, visibility unknown | <Box justifyContent="center" marginBottom={1}> |
| tui | ui-tui\src\components\branding.tsx | 368 | English string, visibility unknown | <Box flexDirection="column" key={si} marginTop={si > 0 ? 1 : 0}> |
| tui | ui-tui\src\components\branding.tsx | 376 | English string, visibility unknown | <Text key={ri} wrap="truncate"> |
| tui | ui-tui\src\components\branding.tsx | 383 | English string, visibility unknown | <Text color={t.color.text} key={ii} wrap="truncate"> |
| tui | ui-tui\src\components\fpsOverlay.tsx | 3 | English string, visibility unknown | import { Text } from '@hermes/ink' |
| tui | ui-tui\src\components\fpsOverlay.tsx | 4 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\components\fpsOverlay.tsx | 7 | English string, visibility unknown | import { $fpsState } from '../lib/fpsStore.js' |
| tui | ui-tui\src\components\fpsOverlay.tsx | 8 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\helpHint.tsx | 1 | English string, visibility unknown | import { Box, Text } from '@hermes/ink' |
| tui | ui-tui\src\components\helpHint.tsx | 4 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\helpHint.tsx | 7 | mixed Chinese and English, visibility unknown | ['/help', '查看完整命令和快捷键'], |
| tui | ui-tui\src\components\helpHint.tsx | 8 | mixed Chinese and English, visibility unknown | ['/clear', '开始新会话'], |
| tui | ui-tui\src\components\helpHint.tsx | 9 | mixed Chinese and English, visibility unknown | ['/resume', '继续历史会话'], |
| tui | ui-tui\src\components\helpHint.tsx | 10 | mixed Chinese and English, visibility unknown | ['/details', '控制过程细节显示'], |
| tui | ui-tui\src\components\helpHint.tsx | 11 | mixed Chinese and English, visibility unknown | ['/copy', '复制选区或最近回复'], |
| tui | ui-tui\src\components\helpHint.tsx | 12 | mixed Chinese and English, visibility unknown | ['/quit', '退出 Hermes'] |
| tui | ui-tui\src\components\helpHint.tsx | 26 | English string, visibility unknown | <Box alignItems="flex-start" bottom="100%" flexDirection="column" left={0} position="absolute" right={0}> |
| tui | ui-tui\src\components\helpHint.tsx | 28 | English string, visibility unknown | alignSelf="flex-start" |
| tui | ui-tui\src\components\helpHint.tsx | 30 | English string, visibility unknown | borderStyle="round" |
| tui | ui-tui\src\components\helpHint.tsx | 31 | English string, visibility unknown | flexDirection="column" |
| tui | ui-tui\src\components\helpHint.tsx | 41 | mixed Chinese and English, visibility unknown | {' · 输入 /help 查看完整面板 · Backspace 关闭'} |
| tui | ui-tui\src\components\markdown.tsx | 1 | English string, visibility unknown | import { Box, Link, stringWidth, Text } from '@hermes/ink' |
| tui | ui-tui\src\components\markdown.tsx | 2 | English string, visibility unknown | import { Fragment, memo, type ReactNode, useMemo } from 'react' |
| tui | ui-tui\src\components\markdown.tsx | 4 | English string, visibility unknown | import { ensureEmojiPresentation } from '../lib/emoji.js' |
| tui | ui-tui\src\components\markdown.tsx | 5 | English string, visibility unknown | import { normalizeExternalUrl, urlSlugTitleLabel, useLinkTitle } from '../lib/externalLink.js' |
| tui | ui-tui\src\components\markdown.tsx | 7 | English string, visibility unknown | import { highlightLine, isHighlightable } from '../lib/syntax.js' |
| tui | ui-tui\src\components\markdown.tsx | 8 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\markdown.tsx | 10 | English string, visibility unknown | // `\boxed{X}` regions in `texToUnicode` output are marked with the |
| tui | ui-tui\src\components\markdown.tsx | 12 | English string, visibility unknown | // boxed segment with `inverse + bold` so it reads as a highlighter-pen |
| tui | ui-tui\src\components\markdown.tsx | 13 | English string, visibility unknown | // emphasis on top of whatever color the parent `<Text>` is using (the |
| tui | ui-tui\src\components\markdown.tsx | 80 | English string, visibility unknown | // Display math openers: `$$ ... $$` (TeX) and `\[ ... \]` (LaTeX). The |
| tui | ui-tui\src\components\markdown.tsx | 82 | English string, visibility unknown | // trimmed line — `startsWith('$$')` used to fire on prose like |
| tui | ui-tui\src\components\markdown.tsx | 83 | English string, visibility unknown | // `$$x+y$$ followed by more`, opening a block that never closed because the |
| tui | ui-tui\src\components\markdown.tsx | 94 | English string, visibility unknown | // so `**` must come before `*`, `__` before `_`, etc. Each pattern owns its |
| tui | ui-tui\src\components\markdown.tsx | 99 | English string, visibility unknown | // doesn't pair up the first `~` with the next one on the line and swallow |
| tui | ui-tui\src\components\markdown.tsx | 102 | English string, visibility unknown | // Inline math (`$x$` and `\(x\)`) takes precedence over emphasis at the |
| tui | ui-tui\src\components\markdown.tsx | 105 | English string, visibility unknown | // `$P=a*b*c$` renders as math instead of having `*b*` corrupted into |
| tui | ui-tui\src\components\markdown.tsx | 106 | English string, visibility unknown | // italics. Single-character minimums and "no space adjacent to delimiter" |
| tui | ui-tui\src\components\markdown.tsx | 112 | English string, visibility unknown | `<((?:https?:\\/\\/\|mailto:)[^>\\s]+\|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,})>`, // 5 autolink |
| tui | ui-tui\src\components\markdown.tsx | 151 | English string, visibility unknown | raw.startsWith('mailto:') \|\| raw.startsWith('http') \|\| !raw.includes('@') ? raw : `mailto:${raw}` |
| tui | ui-tui\src\components\markdown.tsx | 154 | English string, visibility unknown | url.startsWith('mailto:') ? url.replace(/^mailto:/, '') : /^https?:\/\//i.test(url) ? urlSlugTitleLabel(url) : url |
| tui | ui-tui\src\components\markdown.tsx | 193 | English string, visibility unknown | .replace(/!\[(.*?)\]\(((?:[^\s()]\|\([^\s()]*\))+?)\)/g, '[image: $1] $2') |
| tui | ui-tui\src\components\markdown.tsx | 305 | English string, visibility unknown | const segmenter = typeof Intl !== 'undefined' && 'Segmenter' in Intl |
| tui | ui-tui\src\components\markdown.tsx | 306 | English string, visibility unknown | ? new (Intl as any).Segmenter(undefined, { granularity: 'grapheme' }) |
| tui | ui-tui\src\components\markdown.tsx | 314 | English string, visibility unknown | // Word-wrap plain text to fit within `width` display columns. |
| tui | ui-tui\src\components\markdown.tsx | 358 | English string, visibility unknown | const sep = columnWidths.map(w => '─'.repeat(Math.max(1, w))).join(' ') |
| tui | ui-tui\src\components\markdown.tsx | 380 | English string, visibility unknown | wrap="truncate-end" |
| tui | ui-tui\src\components\markdown.tsx | 385 | English string, visibility unknown | <Text color={t.color.muted} dimColor wrap="truncate-end">{sep}</Text> |
| tui | ui-tui\src\components\markdown.tsx | 394 | English string, visibility unknown | type LineEntry = { text: string; kind: 'header' \| 'separator' \| 'body' } |
| tui | ui-tui\src\components\markdown.tsx | 421 | English string, visibility unknown | const kind = ri === 0 ? 'header' as const : 'body' as const |
| tui | ui-tui\src\components\markdown.tsx | 426 | English string, visibility unknown | allEntries.push({ text: sep, kind: 'separator' }) |
| tui | ui-tui\src\components\markdown.tsx | 444 | English string, visibility unknown | <Text bold color={t.color.accent} wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 464 | English string, visibility unknown | const label = stripInlineMarkup(header) \|\| `Col ${ci + 1}` |
| tui | ui-tui\src\components\markdown.tsx | 466 | English string, visibility unknown | <Text key={ci} wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 483 | English string, visibility unknown | bold={entry.kind === 'header'} |
| tui | ui-tui\src\components\markdown.tsx | 484 | English string, visibility unknown | color={entry.kind === 'header' ? t.color.accent : entry.kind === 'separator' ? t.color.muted : undefined} |
| tui | ui-tui\src\components\markdown.tsx | 485 | English string, visibility unknown | dimColor={entry.kind === 'separator'} |
| tui | ui-tui\src\components\markdown.tsx | 487 | English string, visibility unknown | wrap="truncate-end" |
| tui | ui-tui\src\components\markdown.tsx | 536 | English string, visibility unknown | // `$...$` math (and other inline tokens) inside a `**bolded |
| tui | ui-tui\src\components\markdown.tsx | 538 | English string, visibility unknown | // this the inner content is dropped into a single `<Text bold>` |
| tui | ui-tui\src\components\markdown.tsx | 586 | English string, visibility unknown | // Inline math is run through `texToUnicode` (Greek letters, ℕℤℚℝ, |
| tui | ui-tui\src\components\markdown.tsx | 589 | English string, visibility unknown | // so without italic readers can't tell `\mathbb{R}` (math) from a |
| tui | ui-tui\src\components\markdown.tsx | 590 | English string, visibility unknown | // hyperlinked word. Anything `texToUnicode` doesn't recognise is |
| tui | ui-tui\src\components\markdown.tsx | 607 | English string, visibility unknown | return <Text wrap="wrap-trim">{parts.length ? parts : text}</Text> |
| tui | ui-tui\src\components\markdown.tsx | 651 | English string, visibility unknown | const cacheKey = `${compact ? '1' : '0'}\|${cols ?? ''}\|${text}` |
| tui | ui-tui\src\components\markdown.tsx | 665 | English string, visibility unknown | if (nodes.length && prevKind !== 'blank') { |
| tui | ui-tui\src\components\markdown.tsx | 666 | English string, visibility unknown | nodes.push(<Text key={`gap-${nodes.length}`}> </Text>) |
| tui | ui-tui\src\components\markdown.tsx | 667 | English string, visibility unknown | prevKind = 'blank' |
| tui | ui-tui\src\components\markdown.tsx | 671 | English string, visibility unknown | const start = (kind: Exclude<Kind, null \| 'blank'>) => { |
| tui | ui-tui\src\components\markdown.tsx | 672 | English string, visibility unknown | if (prevKind && prevKind !== 'blank' && prevKind !== kind) { |
| tui | ui-tui\src\components\markdown.tsx | 702 | English string, visibility unknown | start('paragraph') |
| tui | ui-tui\src\components\markdown.tsx | 704 | English string, visibility unknown | <Text color={t.color.muted} key={key} wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 707 | English string, visibility unknown | <Link url={/^(?:\/\|[a-z]:[\\/])/i.test(media) ? `file://${media}` : media}> |
| tui | ui-tui\src\components\markdown.tsx | 741 | English string, visibility unknown | if (['md', 'markdown'].includes(lang)) { |
| tui | ui-tui\src\components\markdown.tsx | 742 | English string, visibility unknown | start('paragraph') |
| tui | ui-tui\src\components\markdown.tsx | 748 | English string, visibility unknown | start('code') |
| tui | ui-tui\src\components\markdown.tsx | 750 | English string, visibility unknown | const isDiff = lang === 'diff' |
| tui | ui-tui\src\components\markdown.tsx | 754 | English string, visibility unknown | <Box flexDirection="column" key={key} paddingLeft={2}> |
| tui | ui-tui\src\components\markdown.tsx | 812 | English string, visibility unknown | start('code') |
| tui | ui-tui\src\components\markdown.tsx | 814 | English string, visibility unknown | <Box flexDirection="column" key={key} paddingLeft={2}> |
| tui | ui-tui\src\components\markdown.tsx | 837 | English string, visibility unknown | start('paragraph') |
| tui | ui-tui\src\components\markdown.tsx | 858 | English string, visibility unknown | start('code') |
| tui | ui-tui\src\components\markdown.tsx | 860 | English string, visibility unknown | <Box flexDirection="column" key={key} paddingLeft={2}> |
| tui | ui-tui\src\components\markdown.tsx | 876 | English string, visibility unknown | start('heading') |
| tui | ui-tui\src\components\markdown.tsx | 878 | English string, visibility unknown | <Text bold color={t.color.accent} key={key} wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 888 | English string, visibility unknown | start('heading') |
| tui | ui-tui\src\components\markdown.tsx | 890 | English string, visibility unknown | <Text bold color={t.color.accent} key={key} wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 900 | English string, visibility unknown | start('rule') |
| tui | ui-tui\src\components\markdown.tsx | 914 | English string, visibility unknown | start('list') |
| tui | ui-tui\src\components\markdown.tsx | 916 | English string, visibility unknown | <Text color={t.color.muted} key={key} wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 924 | English string, visibility unknown | <Box key={`${key}-cont-${i}`} paddingLeft={2}> |
| tui | ui-tui\src\components\markdown.tsx | 925 | English string, visibility unknown | <Text color={t.color.muted} wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 937 | English string, visibility unknown | start('list') |
| tui | ui-tui\src\components\markdown.tsx | 939 | English string, visibility unknown | <Text bold key={key} wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 953 | English string, visibility unknown | <Text key={`${key}-def-${i}`} wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 967 | English string, visibility unknown | start('list') |
| tui | ui-tui\src\components\markdown.tsx | 974 | English string, visibility unknown | <Text wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 988 | English string, visibility unknown | start('list') |
| tui | ui-tui\src\components\markdown.tsx | 991 | English string, visibility unknown | <Text wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 1003 | English string, visibility unknown | start('quote') |
| tui | ui-tui\src\components\markdown.tsx | 1015 | English string, visibility unknown | <Box flexDirection="column" key={key}> |
| tui | ui-tui\src\components\markdown.tsx | 1018 | English string, visibility unknown | <Text color={t.color.muted} wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 1030 | English string, visibility unknown | start('table') |
| tui | ui-tui\src\components\markdown.tsx | 1052 | English string, visibility unknown | start('paragraph') |
| tui | ui-tui\src\components\markdown.tsx | 1054 | English string, visibility unknown | <Text color={t.color.muted} key={key} wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 1064 | English string, visibility unknown | start('paragraph') |
| tui | ui-tui\src\components\markdown.tsx | 1066 | English string, visibility unknown | <Text color={t.color.muted} key={key} wrap="wrap-trim"> |
| tui | ui-tui\src\components\markdown.tsx | 1075 | English string, visibility unknown | if (line.includes('\|') && line.trim().startsWith('\|')) { |
| tui | ui-tui\src\components\markdown.tsx | 1076 | English string, visibility unknown | start('table') |
| tui | ui-tui\src\components\markdown.tsx | 1097 | English string, visibility unknown | start('paragraph') |
| tui | ui-tui\src\components\markdown.tsx | 1107 | English string, visibility unknown | return <Box flexDirection="column">{nodes}</Box> |
| tui | ui-tui\src\components\markdown.tsx | 1112 | English string, visibility unknown | type Kind = 'blank' \| 'code' \| 'heading' \| 'list' \| 'paragraph' \| 'quote' \| 'rule' \| 'table' \| null |
| tui | ui-tui\src\components\maskedPrompt.tsx | 1 | English string, visibility unknown | import { Box, Text } from '@hermes/ink' |
| tui | ui-tui\src\components\maskedPrompt.tsx | 2 | English string, visibility unknown | import { useState } from 'react' |
| tui | ui-tui\src\components\maskedPrompt.tsx | 4 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\maskedPrompt.tsx | 6 | English string, visibility unknown | import { TextInput } from './textInput.js' |
| tui | ui-tui\src\components\maskedPrompt.tsx | 12 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\messageLine.tsx | 1 | English string, visibility unknown | import { Ansi, Box, NoSelect, Text } from '@hermes/ink' |
| tui | ui-tui\src\components\messageLine.tsx | 2 | English string, visibility unknown | import { memo, useState } from 'react' |
| tui | ui-tui\src\components\messageLine.tsx | 5 | English string, visibility unknown | import { sectionMode } from '../domain/details.js' |
| tui | ui-tui\src\components\messageLine.tsx | 6 | English string, visibility unknown | import { userDisplay } from '../domain/messages.js' |
| tui | ui-tui\src\components\messageLine.tsx | 8 | English string, visibility unknown | import { transcriptBodyWidth, transcriptGutterWidth } from '../lib/inputMetrics.js' |
| tui | ui-tui\src\components\messageLine.tsx | 16 | English string, visibility unknown | } from '../lib/text.js' |
| tui | ui-tui\src\components\messageLine.tsx | 17 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\messageLine.tsx | 18 | English string, visibility unknown | import type { ActiveTool, DetailsMode, Msg, SectionVisibility } from '../types.js' |
| tui | ui-tui\src\components\messageLine.tsx | 20 | English string, visibility unknown | import { Md } from './markdown.js' |
| tui | ui-tui\src\components\messageLine.tsx | 21 | English string, visibility unknown | import { StreamingMd } from './streamingMarkdown.js' |
| tui | ui-tui\src\components\messageLine.tsx | 22 | English string, visibility unknown | import { ToolTrail } from './thinking.js' |
| tui | ui-tui\src\components\messageLine.tsx | 23 | English string, visibility unknown | import { TodoPanel } from './todoPanel.js' |
| tui | ui-tui\src\components\messageLine.tsx | 31 | English string, visibility unknown | detailsMode = 'collapsed', |
| tui | ui-tui\src\components\messageLine.tsx | 41 | English string, visibility unknown | // sections only — never on the global mode. A `trail` message feeds Tool |
| tui | ui-tui\src\components\messageLine.tsx | 44 | English string, visibility unknown | // `thinking` (expanded by default) keep an empty wrapper alive when only |
| tui | ui-tui\src\components\messageLine.tsx | 45 | English string, visibility unknown | // `tools` is hidden — exactly the empty-Box bug Copilot caught. |
| tui | ui-tui\src\components\messageLine.tsx | 46 | English string, visibility unknown | const thinkingMode = sectionMode('thinking', detailsMode, sections, detailsModeCommandOverride) |
| tui | ui-tui\src\components\messageLine.tsx | 47 | English string, visibility unknown | const toolsMode = sectionMode('tools', detailsMode, sections, detailsModeCommandOverride) |
| tui | ui-tui\src\components\messageLine.tsx | 48 | English string, visibility unknown | const activityMode = sectionMode('activity', detailsMode, sections, detailsModeCommandOverride) |
| tui | ui-tui\src\components\messageLine.tsx | 55 | English string, visibility unknown | if (msg.kind === 'trail' && msg.todos?.length) { |
| tui | ui-tui\src\components\messageLine.tsx | 66 | English string, visibility unknown | if (msg.kind === 'trail' && (msg.tools?.length \|\| tools.length \|\| thinking)) { |
| tui | ui-tui\src\components\messageLine.tsx | 67 | English string, visibility unknown | return thinkingMode !== 'hidden' \|\| toolsMode !== 'hidden' \|\| activityMode !== 'hidden' ? ( |
| tui | ui-tui\src\components\messageLine.tsx | 68 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\messageLine.tsx | 84 | English string, visibility unknown | if (msg.role === 'tool') { |
| tui | ui-tui\src\components\messageLine.tsx | 91 | English string, visibility unknown | <Box alignSelf="flex-start" borderColor={t.color.muted} borderStyle="round" marginLeft={3} paddingX={1}> |
| tui | ui-tui\src\components\messageLine.tsx | 93 | English string, visibility unknown | <Text wrap="truncate-end"> |
| tui | ui-tui\src\components\messageLine.tsx | 97 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\messageLine.tsx | 109 | English string, visibility unknown | (toolsMode !== 'hidden' && Boolean(msg.tools?.length)) \|\| (thinkingMode !== 'hidden' && Boolean(thinking)) |
| tui | ui-tui\src\components\messageLine.tsx | 112 | English string, visibility unknown | if (msg.kind === 'slash') { |
| tui | ui-tui\src\components\messageLine.tsx | 120 | mixed Chinese and English, visibility unknown | const firstLine = (msg.text.split('\n')[0] ?? '').trim().slice(0, 120) \|\| '（系统消息）' |
| tui | ui-tui\src\components\messageLine.tsx | 123 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\messageLine.tsx | 137 | English string, visibility unknown | if (msg.role !== 'user' && hasAnsi(msg.text)) { |
| tui | ui-tui\src\components\messageLine.tsx | 141 | English string, visibility unknown | if (msg.role === 'assistant') { |
| tui | ui-tui\src\components\messageLine.tsx | 174 | English string, visibility unknown | const isDiffSegment = msg.kind === 'diff' |
| tui | ui-tui\src\components\messageLine.tsx | 178 | English string, visibility unknown | flexDirection="column" |
| tui | ui-tui\src\components\messageLine.tsx | 179 | English string, visibility unknown | marginBottom={msg.role === 'user' \|\| isDiffSegment ? 1 : 0} |
| tui | ui-tui\src\components\messageLine.tsx | 180 | English string, visibility unknown | marginTop={msg.role === 'user' \|\| msg.kind === 'slash' \|\| isDiffSegment ? 1 : 0} |
| tui | ui-tui\src\components\messageLine.tsx | 183 | English string, visibility unknown | <Box flexDirection="column" marginBottom={1}> |
| tui | ui-tui\src\components\messageLine.tsx | 199 | English string, visibility unknown | <Text bold={msg.role === 'user'} color={prefix}> |
| tui | ui-tui\src\components\modelPicker.tsx | 1 | English string, visibility unknown | import { Box, Text, useInput, useStdout } from '@hermes/ink' |
| tui | ui-tui\src\components\modelPicker.tsx | 2 | English string, visibility unknown | import { useEffect, useMemo, useState } from 'react' |
| tui | ui-tui\src\components\modelPicker.tsx | 4 | English string, visibility unknown | import { providerDisplayNames } from '../domain/providers.js' |
| tui | ui-tui\src\components\modelPicker.tsx | 6 | English string, visibility unknown | import type { GatewayClient } from '../gatewayClient.js' |
| tui | ui-tui\src\components\modelPicker.tsx | 7 | English string, visibility unknown | import type { ModelOptionProvider, ModelOptionsResponse } from '../gatewayTypes.js' |
| tui | ui-tui\src\components\modelPicker.tsx | 8 | English string, visibility unknown | import { asRpcResult, rpcErrorMessage } from '../lib/rpc.js' |
| tui | ui-tui\src\components\modelPicker.tsx | 9 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\modelPicker.tsx | 11 | English string, visibility unknown | import { OverlayHint, useOverlayKeys, windowItems } from './overlayControls.js' |
| tui | ui-tui\src\components\modelPicker.tsx | 93 | English string, visibility unknown | if (stage === 'key') { |
| tui | ui-tui\src\components\modelPicker.tsx | 158 | English string, visibility unknown | if (stage === 'disconnect') { |
| tui | ui-tui\src\components\modelPicker.tsx | 178 | mixed Chinese and English, visibility unknown | ? { ...p, authenticated: false, models: [], total_models: 0, warning: p.key_env ? `粘贴 ${p.key_env} 后启用` : '运行 `hermes model` 配置' } |
| tui | ui-tui\src\components\modelPicker.tsx | 229 | English string, visibility unknown | setStage('key') |
| tui | ui-tui\src\components\modelPicker.tsx | 263 | English string, visibility unknown | setStage('disconnect') |
| tui | ui-tui\src\components\modelPicker.tsx | 275 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\modelPicker.tsx | 284 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\modelPicker.tsx | 293 | English string, visibility unknown | const masked = keyInput ? '•'.repeat(Math.min(keyInput.length, 40)) : '' |
| tui | ui-tui\src\components\modelPicker.tsx | 296 | English string, visibility unknown | <Box flexDirection="column" width={width}> |
| tui | ui-tui\src\components\modelPicker.tsx | 297 | English string, visibility unknown | <Text bold color={t.color.accent} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 301 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 305 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> </Text> |
| tui | ui-tui\src\components\modelPicker.tsx | 307 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 311 | English string, visibility unknown | <Text color={t.color.accent} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 312 | mixed Chinese and English, visibility unknown | {' '}{masked \|\| '（空）'}{keySaving ? '' : '▎'} |
| tui | ui-tui\src\components\modelPicker.tsx | 315 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> </Text> |
| tui | ui-tui\src\components\modelPicker.tsx | 318 | English string, visibility unknown | <Text color={t.color.label} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 322 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 326 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> </Text> |
| tui | ui-tui\src\components\modelPicker.tsx | 337 | English string, visibility unknown | <Box flexDirection="column" width={width}> |
| tui | ui-tui\src\components\modelPicker.tsx | 338 | English string, visibility unknown | <Text bold color={t.color.accent} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 342 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> </Text> |
| tui | ui-tui\src\components\modelPicker.tsx | 344 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 348 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 352 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> </Text> |
| tui | ui-tui\src\components\modelPicker.tsx | 355 | mixed Chinese and English, visibility unknown | <Text color={t.color.muted} wrap="truncate-end">正在断开…</Text> |
| tui | ui-tui\src\components\modelPicker.tsx | 367 | English string, visibility unknown | const authMark = p.authenticated === false ? '○' : p.is_current ? '*' : '●' |
| tui | ui-tui\src\components\modelPicker.tsx | 370 | mixed Chinese and English, visibility unknown | ? (p.auth_type === 'api_key' ? '（无密钥）' : '（需要设置）') |
| tui | ui-tui\src\components\modelPicker.tsx | 371 | mixed Chinese and English, visibility unknown | : `${modelCount} 个模型` |
| tui | ui-tui\src\components\modelPicker.tsx | 373 | English string, visibility unknown | return `${authMark} ${names[i]} · ${suffix}` |
| tui | ui-tui\src\components\modelPicker.tsx | 380 | English string, visibility unknown | <Box flexDirection="column" width={width}> |
| tui | ui-tui\src\components\modelPicker.tsx | 381 | English string, visibility unknown | <Text bold color={t.color.accent} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 385 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 389 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 392 | English string, visibility unknown | <Text color={t.color.label} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 395 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 396 | mixed Chinese and English, visibility unknown | {offset > 0 ? ` ↑ 还有 ${offset} 项` : ' '} |
| tui | ui-tui\src\components\modelPicker.tsx | 410 | English string, visibility unknown | key={providers[idx]?.slug ?? `row-${idx}`} |
| tui | ui-tui\src\components\modelPicker.tsx | 411 | English string, visibility unknown | wrap="truncate-end" |
| tui | ui-tui\src\components\modelPicker.tsx | 417 | English string, visibility unknown | <Text color={t.color.muted} key={`pad-${i}`} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 423 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 427 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 439 | English string, visibility unknown | <Box flexDirection="column" width={width}> |
| tui | ui-tui\src\components\modelPicker.tsx | 440 | English string, visibility unknown | <Text bold color={t.color.accent} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 444 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 447 | English string, visibility unknown | <Text color={t.color.label} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 450 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 451 | mixed Chinese and English, visibility unknown | {offset > 0 ? ` ↑ 还有 ${offset} 项` : ' '} |
| tui | ui-tui\src\components\modelPicker.tsx | 460 | English string, visibility unknown | <Text color={t.color.muted} key="empty" wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 464 | English string, visibility unknown | <Text color={t.color.muted} key={`pad-${i}`} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 470 | English string, visibility unknown | const prefix = modelIdx === idx ? '▸ ' : row === currentModel ? '* ' : ' ' |
| tui | ui-tui\src\components\modelPicker.tsx | 478 | English string, visibility unknown | wrap="truncate-end" |
| tui | ui-tui\src\components\modelPicker.tsx | 486 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 490 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\modelPicker.tsx | 494 | mixed Chinese and English, visibility unknown | {models.length ? '↑/↓ 选择 · Enter 切换 · Esc 返回 · q 关闭' : 'Enter/Esc 返回 · q 关闭'} |
| tui | ui-tui\src\components\moduleSlot.tsx | 1 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\components\moduleSlot.tsx | 2 | English string, visibility unknown | import { Fragment } from 'react' |
| tui | ui-tui\src\components\moduleSlot.tsx | 4 | English string, visibility unknown | import { visibleModulesForSlot } from '../app/tuiModuleRegistry.js' |
| tui | ui-tui\src\components\moduleSlot.tsx | 5 | English string, visibility unknown | import type { TuiSlotId } from '../app/tuiSlots.js' |
| tui | ui-tui\src\components\moduleSlot.tsx | 6 | English string, visibility unknown | import { $uiState } from '../app/uiStore.js' |
| tui | ui-tui\src\components\moduleSlot.tsx | 8 | English string, visibility unknown | import { MonitorPanel } from './monitorPanel.js' |
| tui | ui-tui\src\components\moduleSlot.tsx | 17 | English string, visibility unknown | if (module.id === 'monitorPanel') { |
| tui | ui-tui\src\components\monitorPanel.tsx | 1 | English string, visibility unknown | import { Box, Text } from '@hermes/ink' |
| tui | ui-tui\src\components\monitorPanel.tsx | 2 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\components\monitorPanel.tsx | 4 | English string, visibility unknown | import { useTurnSelector } from '../app/turnStore.js' |
| tui | ui-tui\src\components\monitorPanel.tsx | 5 | English string, visibility unknown | import { $uiState } from '../app/uiStore.js' |
| tui | ui-tui\src\components\monitorPanel.tsx | 6 | English string, visibility unknown | import { fmtK } from '../lib/text.js' |
| tui | ui-tui\src\components\monitorPanel.tsx | 11 | English string, visibility unknown | const activeTodos = todos.filter(todo => todo.status !== 'completed').length |
| tui | ui-tui\src\components\monitorPanel.tsx | 12 | English string, visibility unknown | const ctx = ui.usage.context_percent == null ? '--' : `${ui.usage.context_percent}%` |
| tui | ui-tui\src\components\monitorPanel.tsx | 16 | English string, visibility unknown | <Box borderColor={ui.theme.color.statusDim} borderStyle="round" flexDirection="column" marginBottom={1} paddingX={1}> |
| tui | ui-tui\src\components\monitorPanel.tsx | 17 | English string, visibility unknown | <Text wrap="truncate-end"> |
| tui | ui-tui\src\components\monitorPanel.tsx | 28 | English string, visibility unknown | <Text color={ui.theme.color.statusDim} wrap="truncate-end"> |
| tui | ui-tui\src\components\overlayControls.tsx | 1 | English string, visibility unknown | import { Text, useInput } from '@hermes/ink' |
| tui | ui-tui\src\components\overlayControls.tsx | 3 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\overlayControls.tsx | 23 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\prompts.tsx | 1 | English string, visibility unknown | import { Box, Text, useInput } from '@hermes/ink' |
| tui | ui-tui\src\components\prompts.tsx | 2 | English string, visibility unknown | import { useState } from 'react' |
| tui | ui-tui\src\components\prompts.tsx | 4 | English string, visibility unknown | import { isMac } from '../lib/platform.js' |
| tui | ui-tui\src\components\prompts.tsx | 5 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\prompts.tsx | 6 | English string, visibility unknown | import type { ApprovalReq, ClarifyReq, ConfirmReq } from '../types.js' |
| tui | ui-tui\src\components\prompts.tsx | 8 | English string, visibility unknown | import { TextInput } from './textInput.js' |
| tui | ui-tui\src\components\prompts.tsx | 23 | English string, visibility unknown | \| { kind: 'move'; delta: -1 \| 1 } |
| tui | ui-tui\src\components\prompts.tsx | 24 | English string, visibility unknown | \| { kind: 'noop' } |
| tui | ui-tui\src\components\prompts.tsx | 39 | English string, visibility unknown | return { kind: 'choose', choice: 'deny' } |
| tui | ui-tui\src\components\prompts.tsx | 53 | English string, visibility unknown | return { kind: 'move', delta: -1 } |
| tui | ui-tui\src\components\prompts.tsx | 57 | English string, visibility unknown | return { kind: 'move', delta: 1 } |
| tui | ui-tui\src\components\prompts.tsx | 60 | English string, visibility unknown | return { kind: 'noop' } |
| tui | ui-tui\src\components\prompts.tsx | 69 | English string, visibility unknown | if (action.kind === 'choose') { |
| tui | ui-tui\src\components\prompts.tsx | 71 | English string, visibility unknown | } else if (action.kind === 'move') { |
| tui | ui-tui\src\components\prompts.tsx | 81 | English string, visibility unknown | <Box borderColor={t.color.warn} borderStyle="double" flexDirection="column" paddingX={1}> |
| tui | ui-tui\src\components\prompts.tsx | 86 | English string, visibility unknown | <Box flexDirection="column" paddingLeft={1}> |
| tui | ui-tui\src\components\prompts.tsx | 88 | English string, visibility unknown | <Text color={t.color.text} key={i} wrap="truncate-end"> |
| tui | ui-tui\src\components\prompts.tsx | 161 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\prompts.tsx | 171 | mixed Chinese and English, visibility unknown | {isMac ? 'Cmd+C 复制 · Cmd+V 粘贴 · Ctrl+C 取消' : 'Ctrl+C 取消'} |
| tui | ui-tui\src\components\prompts.tsx | 178 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\prompts.tsx | 201 | English string, visibility unknown | if (key.escape \|\| (key.ctrl && lower === 'c') \|\| lower === 'n') { |
| tui | ui-tui\src\components\prompts.tsx | 230 | English string, visibility unknown | <Box borderColor={accent} borderStyle="double" flexDirection="column" paddingX={1}> |
| tui | ui-tui\src\components\prompts.tsx | 237 | English string, visibility unknown | <Text color={t.color.text} wrap="truncate-end"> |
| tui | ui-tui\src\components\queuedMessages.tsx | 1 | English string, visibility unknown | import { Box, Text } from '@hermes/ink' |
| tui | ui-tui\src\components\queuedMessages.tsx | 3 | English string, visibility unknown | import { compactPreview } from '../lib/text.js' |
| tui | ui-tui\src\components\queuedMessages.tsx | 4 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\queuedMessages.tsx | 25 | English string, visibility unknown | <Box flexDirection="column" marginTop={1}> |
| tui | ui-tui\src\components\queuedMessages.tsx | 28 | mixed Chinese and English, visibility unknown | queueEditIdx !== null ? ` · 正在编辑 ${queueEditIdx + 1} · Ctrl+X 删除 · Esc 取消` : '' |
| tui | ui-tui\src\components\queuedMessages.tsx | 44 | English string, visibility unknown | <Text color={active ? t.color.accent : t.color.muted} dimColor key={`${idx}-${item.slice(0, 16)}`}> |
| tui | ui-tui\src\components\sessionPicker.tsx | 1 | English string, visibility unknown | import { Box, Text, useInput, useStdout } from '@hermes/ink' |
| tui | ui-tui\src\components\sessionPicker.tsx | 2 | English string, visibility unknown | import { useEffect, useState } from 'react' |
| tui | ui-tui\src\components\sessionPicker.tsx | 4 | English string, visibility unknown | import type { GatewayClient } from '../gatewayClient.js' |
| tui | ui-tui\src\components\sessionPicker.tsx | 5 | English string, visibility unknown | import type { SessionDeleteResponse, SessionListItem, SessionListResponse } from '../gatewayTypes.js' |
| tui | ui-tui\src\components\sessionPicker.tsx | 6 | English string, visibility unknown | import { asRpcResult, rpcErrorMessage } from '../lib/rpc.js' |
| tui | ui-tui\src\components\sessionPicker.tsx | 7 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\sessionPicker.tsx | 9 | English string, visibility unknown | import { OverlayHint, useOverlayKeys, windowOffset } from './overlayControls.js' |
| tui | ui-tui\src\components\sessionPicker.tsx | 26 | mixed Chinese and English, visibility unknown | return `${Math.floor(d)} 天前` |
| tui | ui-tui\src\components\sessionPicker.tsx | 34 | English string, visibility unknown | // When non-null, the user pressed `d` on this index and we're waiting for |
| tui | ui-tui\src\components\sessionPicker.tsx | 45 | English string, visibility unknown | gw.request<SessionListResponse>('session.list', { limit: 200 }) |
| tui | ui-tui\src\components\sessionPicker.tsx | 50 | mixed Chinese and English, visibility unknown | setErr('无效响应: session.list') |
| tui | ui-tui\src\components\sessionPicker.tsx | 79 | mixed Chinese and English, visibility unknown | setErr('无效响应: session.delete') |
| tui | ui-tui\src\components\sessionPicker.tsx | 150 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\sessionPicker.tsx | 159 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\sessionPicker.tsx | 169 | English string, visibility unknown | <Box flexDirection="column" width={width}> |
| tui | ui-tui\src\components\sessionPicker.tsx | 195 | mixed Chinese and English, visibility unknown | ({s.message_count} 条消息, {age(s.started_at)}, {s.source \|\| 'tui'}) |
| tui | ui-tui\src\components\sessionPicker.tsx | 203 | English string, visibility unknown | wrap="truncate-end" |
| tui | ui-tui\src\components\sessionPicker.tsx | 205 | mixed Chinese and English, visibility unknown | {pendingDelete ? '再次按 d 删除' : s.title \|\| s.preview \|\| '（未命名）'} |
| tui | ui-tui\src\components\skillsHub.tsx | 1 | English string, visibility unknown | import { Box, Text, useInput, useStdout } from '@hermes/ink' |
| tui | ui-tui\src\components\skillsHub.tsx | 2 | English string, visibility unknown | import { useEffect, useState } from 'react' |
| tui | ui-tui\src\components\skillsHub.tsx | 4 | English string, visibility unknown | import type { GatewayClient } from '../gatewayClient.js' |
| tui | ui-tui\src\components\skillsHub.tsx | 5 | English string, visibility unknown | import { rpcErrorMessage } from '../lib/rpc.js' |
| tui | ui-tui\src\components\skillsHub.tsx | 6 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\skillsHub.tsx | 8 | English string, visibility unknown | import { OverlayHint, useOverlayKeys, windowItems, windowOffset } from './overlayControls.js' |
| tui | ui-tui\src\components\skillsHub.tsx | 19 | English string, visibility unknown | const [stage, setStage] = useState<'actions' \| 'category' \| 'skill'>('category') |
| tui | ui-tui\src\components\skillsHub.tsx | 29 | English string, visibility unknown | gw.request<{ skills?: Record<string, string[]> }>('skills.manage', { action: 'list' }) |
| tui | ui-tui\src\components\skillsHub.tsx | 46 | English string, visibility unknown | if (stage === 'actions') { |
| tui | ui-tui\src\components\skillsHub.tsx | 47 | English string, visibility unknown | setStage('skill') |
| tui | ui-tui\src\components\skillsHub.tsx | 54 | English string, visibility unknown | if (stage === 'skill') { |
| tui | ui-tui\src\components\skillsHub.tsx | 55 | English string, visibility unknown | setStage('category') |
| tui | ui-tui\src\components\skillsHub.tsx | 70 | English string, visibility unknown | gw.request<{ info?: SkillInfo }>('skills.manage', { action: 'inspect', query: name }) |
| tui | ui-tui\src\components\skillsHub.tsx | 79 | English string, visibility unknown | gw.request<{ installed?: boolean; name?: string }>('skills.manage', { action: 'install', query: name }) |
| tui | ui-tui\src\components\skillsHub.tsx | 90 | English string, visibility unknown | if (stage === 'actions') { |
| tui | ui-tui\src\components\skillsHub.tsx | 92 | English string, visibility unknown | setStage('skill') |
| tui | ui-tui\src\components\skillsHub.tsx | 112 | English string, visibility unknown | const count = stage === 'category' ? cats.length : skills.length |
| tui | ui-tui\src\components\skillsHub.tsx | 113 | English string, visibility unknown | const sel = stage === 'category' ? catIdx : skillIdx |
| tui | ui-tui\src\components\skillsHub.tsx | 114 | English string, visibility unknown | const setSel = stage === 'category' ? setCatIdx : setSkillIdx |
| tui | ui-tui\src\components\skillsHub.tsx | 129 | English string, visibility unknown | if (stage === 'category') { |
| tui | ui-tui\src\components\skillsHub.tsx | 138 | English string, visibility unknown | setStage('skill') |
| tui | ui-tui\src\components\skillsHub.tsx | 146 | English string, visibility unknown | setStage('actions') |
| tui | ui-tui\src\components\skillsHub.tsx | 158 | English string, visibility unknown | if (stage === 'category') { |
| tui | ui-tui\src\components\skillsHub.tsx | 165 | English string, visibility unknown | setStage('skill') |
| tui | ui-tui\src\components\skillsHub.tsx | 175 | English string, visibility unknown | setStage('actions') |
| tui | ui-tui\src\components\skillsHub.tsx | 185 | English string, visibility unknown | if (err && stage === 'category') { |
| tui | ui-tui\src\components\skillsHub.tsx | 187 | English string, visibility unknown | <Box flexDirection="column" width={width}> |
| tui | ui-tui\src\components\skillsHub.tsx | 196 | English string, visibility unknown | <Box flexDirection="column" width={width}> |
| tui | ui-tui\src\components\skillsHub.tsx | 203 | English string, visibility unknown | if (stage === 'category') { |
| tui | ui-tui\src\components\skillsHub.tsx | 204 | mixed Chinese and English, visibility unknown | const rows = cats.map(c => `${c} · ${skillsByCat[c]?.length ?? 0} 个技能`) |
| tui | ui-tui\src\components\skillsHub.tsx | 208 | English string, visibility unknown | <Box flexDirection="column" width={width}> |
| tui | ui-tui\src\components\skillsHub.tsx | 225 | English string, visibility unknown | wrap="truncate-end" |
| tui | ui-tui\src\components\skillsHub.tsx | 241 | English string, visibility unknown | if (stage === 'skill') { |
| tui | ui-tui\src\components\skillsHub.tsx | 245 | English string, visibility unknown | <Box flexDirection="column" width={width}> |
| tui | ui-tui\src\components\skillsHub.tsx | 263 | English string, visibility unknown | wrap="truncate-end" |
| tui | ui-tui\src\components\skillsHub.tsx | 275 | mixed Chinese and English, visibility unknown | {skills.length ? '↑/↓ 选择 · Enter 打开 · 1-9,0 快选 · Esc 返回 · q 关闭' : 'Esc 返回 · q 关闭'} |
| tui | ui-tui\src\components\skillsHub.tsx | 282 | English string, visibility unknown | <Box flexDirection="column" width={width}> |
| tui | ui-tui\src\components\streamingAssistant.tsx | 1 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\components\streamingAssistant.tsx | 2 | English string, visibility unknown | import { memo } from 'react' |
| tui | ui-tui\src\components\streamingAssistant.tsx | 4 | English string, visibility unknown | import type { AppLayoutProgressProps } from '../app/interfaces.js' |
| tui | ui-tui\src\components\streamingAssistant.tsx | 5 | English string, visibility unknown | import { toggleTodoCollapsed, useTurnSelector } from '../app/turnStore.js' |
| tui | ui-tui\src\components\streamingAssistant.tsx | 6 | English string, visibility unknown | import { $uiState } from '../app/uiStore.js' |
| tui | ui-tui\src\components\streamingAssistant.tsx | 7 | English string, visibility unknown | import { appendToolShelfMessage } from '../lib/liveProgress.js' |
| tui | ui-tui\src\components\streamingAssistant.tsx | 8 | English string, visibility unknown | import type { DetailsMode, Msg, SectionVisibility } from '../types.js' |
| tui | ui-tui\src\components\streamingAssistant.tsx | 10 | English string, visibility unknown | import { MessageLine } from './messageLine.js' |
| tui | ui-tui\src\components\streamingAssistant.tsx | 11 | English string, visibility unknown | import { TodoPanel } from './todoPanel.js' |
| tui | ui-tui\src\components\streamingAssistant.tsx | 43 | English string, visibility unknown | key={`seg:${i}`} |
| tui | ui-tui\src\components\streamingAssistant.tsx | 56 | English string, visibility unknown | msg={{ kind: 'trail', role: 'system', text: '' }} |
| tui | ui-tui\src\components\streamingAssistant.tsx | 86 | English string, visibility unknown | msg={{ kind: 'trail', role: 'system', text: '', tools: streamPendingTools }} |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 7 | English string, visibility unknown | // This splits `text` at the last stable top-level block boundary (blank |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 23 | English string, visibility unknown | // container in messageLine.tsx is a default `flexDirection: 'row'` Box |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 26 | English string, visibility unknown | // streaming" rendering bug. Wrapping in a flexDirection="column" Box |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 31 | English string, visibility unknown | import { Box } from '@hermes/ink' |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 32 | English string, visibility unknown | import { memo, useRef } from 'react' |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 34 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 36 | English string, visibility unknown | import { Md } from './markdown.js' |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 44 | English string, visibility unknown | // produces zero net toggles; that's `len >= 4` plus `endsDollar`. |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 51 | English string, visibility unknown | // is frozen, so prematurely deciding "this `$$` is just prose" would |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 162 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\textInput.tsx | 1 | English string, visibility unknown | import type { InputEvent, Key } from '@hermes/ink' |
| tui | ui-tui\src\components\textInput.tsx | 2 | English string, visibility unknown | import * as Ink from '@hermes/ink' |
| tui | ui-tui\src\components\textInput.tsx | 3 | English string, visibility unknown | import { type MutableRefObject, useEffect, useMemo, useRef, useState } from 'react' |
| tui | ui-tui\src\components\textInput.tsx | 5 | English string, visibility unknown | import { setInputSelection } from '../app/inputSelectionStore.js' |
| tui | ui-tui\src\components\textInput.tsx | 6 | English string, visibility unknown | import { readClipboardText, writeClipboardText } from '../lib/clipboard.js' |
| tui | ui-tui\src\components\textInput.tsx | 7 | English string, visibility unknown | import { cursorLayout, offsetFromPosition } from '../lib/inputMetrics.js' |
| tui | ui-tui\src\components\textInput.tsx | 15 | English string, visibility unknown | } from '../lib/platform.js' |
| tui | ui-tui\src\components\textInput.tsx | 42 | English string, visibility unknown | const seg = () => (_seg ??= new Intl.Segmenter(undefined, { granularity: 'grapheme' })) |
| tui | ui-tui\src\components\textInput.tsx | 150 | English string, visibility unknown | * column offset from the current line's start. Returns `null` when the cursor |
| tui | ui-tui\src\components\textInput.tsx | 193 | English string, visibility unknown | * - `text.length` matches the number of grapheme clusters (no combining |
| tui | ui-tui\src\components\textInput.tsx | 253 | English string, visibility unknown | * contract — values like `'hello '` will return `true` even though |
| tui | ui-tui\src\components\textInput.tsx | 255 | English string, visibility unknown | * composer's `canFastBackspace` helper) always pass `columns`; |
| tui | ui-tui\src\components\textInput.tsx | 256 | English string, visibility unknown | * `columns` is optional only so unit tests of the pre-wrap shape |
| tui | ui-tui\src\components\textInput.tsx | 275 | English string, visibility unknown | // caret's physical column would be at (or past) the terminal's right |
| tui | ui-tui\src\components\textInput.tsx | 277 | English string, visibility unknown | // "\b \b" can't represent the physical move back across that wrap. |
| tui | ui-tui\src\components\textInput.tsx | 279 | English string, visibility unknown | // We check `column === 0` for the "wrap-ansi broke onto a new line" |
| tui | ui-tui\src\components\textInput.tsx | 312 | English string, visibility unknown | out += invert(index === pos && segment !== '\n' ? segment : ' ') |
| tui | ui-tui\src\components\textInput.tsx | 347 | English string, visibility unknown | ee.prependListener('input', h) |
| tui | ui-tui\src\components\textInput.tsx | 350 | English string, visibility unknown | ee.removeListener('input', h) |
| tui | ui-tui\src\components\textInput.tsx | 394 | English string, visibility unknown | const lineWidthRef = useRef(stringWidth(value.includes('\n') ? value.slice(value.lastIndexOf('\n') + 1) : value)) |
| tui | ui-tui\src\components\textInput.tsx | 416 | English string, visibility unknown | // Read `curRef.current` (always up-to-date) rather than the `cur` |
| tui | ui-tui\src\components\textInput.tsx | 417 | English string, visibility unknown | // React state. The fast-echo path defers the React `setCur` by 16ms |
| tui | ui-tui\src\components\textInput.tsx | 420 | English string, visibility unknown | // `cur` state here, the layout effect inside `useDeclaredCursor` |
| tui | ui-tui\src\components\textInput.tsx | 422 | English string, visibility unknown | // bump from `noteCursorAdvance(...)`. `cur` is still in scope and |
| tui | ui-tui\src\components\textInput.tsx | 485 | English string, visibility unknown | lineWidthRef.current = stringWidth(value.includes('\n') ? value.slice(value.lastIndexOf('\n') + 1) : value) |
| tui | ui-tui\src\components\textInput.tsx | 625 | English string, visibility unknown | nextLineWidth ?? stringWidth(next.includes('\n') ? next.slice(next.lastIndexOf('\n') + 1) : next) |
| tui | ui-tui\src\components\textInput.tsx | 748 | English string, visibility unknown | const cleaned = text.replace(/\r\n/g, '\n').replace(/\r/g, '\n') |
| tui | ui-tui\src\components\textInput.tsx | 900 | English string, visibility unknown | const actionHome = k.home \|\| (!isMac && mod && inp === 'a') \|\| isMacActionFallback(k, inp, 'a') |
| tui | ui-tui\src\components\textInput.tsx | 901 | English string, visibility unknown | const actionEnd = k.end \|\| (mod && inp === 'e') \|\| isMacActionFallback(k, inp, 'e') |
| tui | ui-tui\src\components\textInput.tsx | 902 | English string, visibility unknown | const actionDeleteToStart = (mod && inp === 'u') \|\| isMacActionFallback(k, inp, 'u') |
| tui | ui-tui\src\components\textInput.tsx | 903 | English string, visibility unknown | const actionKillToEnd = (mod && inp === 'k') \|\| isMacActionFallback(k, inp, 'k') |
| tui | ui-tui\src\components\textInput.tsx | 904 | English string, visibility unknown | const actionDeleteWord = (mod && inp === 'w') \|\| isMacActionFallback(k, inp, 'w') |
| tui | ui-tui\src\components\textInput.tsx | 912 | English string, visibility unknown | if ((mod && inp === 'y') \|\| (mod && k.shift && inp === 'z')) { |
| tui | ui-tui\src\components\textInput.tsx | 1111 | English string, visibility unknown | if (decision.action === 'copy') { |
| tui | ui-tui\src\components\textInput.tsx | 1152 | English string, visibility unknown | <Text wrap="wrap">{rendered}</Text> |
| tui | ui-tui\src\components\textInput.tsx | 1188 | English string, visibility unknown | \| { action: 'copy'; text: string } |
| tui | ui-tui\src\components\textInput.tsx | 1189 | English string, visibility unknown | \| { action: 'paste' } |
| tui | ui-tui\src\components\textInput.tsx | 1199 | English string, visibility unknown | * Callers pass the already-normalized range from `selRange()` (start <= end, |
| tui | ui-tui\src\components\textInput.tsx | 1209 | English string, visibility unknown | return { action: 'copy', text } |
| tui | ui-tui\src\components\textInput.tsx | 1212 | English string, visibility unknown | return { action: 'paste' } |
| tui | ui-tui\src\components\themed.tsx | 1 | English string, visibility unknown | import { Text } from '@hermes/ink' |
| tui | ui-tui\src\components\themed.tsx | 2 | English string, visibility unknown | import { useStore } from '@nanostores/react' |
| tui | ui-tui\src\components\themed.tsx | 3 | English string, visibility unknown | import type { ReactNode } from 'react' |
| tui | ui-tui\src\components\themed.tsx | 5 | English string, visibility unknown | import { $uiState } from '../app/uiStore.js' |
| tui | ui-tui\src\components\themed.tsx | 6 | English string, visibility unknown | import type { ThemeColors } from '../theme.js' |
| tui | ui-tui\src\components\themed.tsx | 29 | English string, visibility unknown | wrap?: 'end' \| 'middle' \| 'truncate' \| 'truncate-end' \| 'truncate-middle' \| 'truncate-start' \| 'wrap' \| 'wrap-trim' |
| tui | ui-tui\src\components\thinking.tsx | 1 | English string, visibility unknown | import { Box, NoSelect, Text } from '@hermes/ink' |
| tui | ui-tui\src\components\thinking.tsx | 2 | English string, visibility unknown | import { memo, type ReactNode, useEffect, useMemo, useState } from 'react' |
| tui | ui-tui\src\components\thinking.tsx | 3 | English string, visibility unknown | import spinners, { type BrailleSpinnerName } from 'unicode-animations' |
| tui | ui-tui\src\components\thinking.tsx | 6 | English string, visibility unknown | import { sectionMode } from '../domain/details.js' |
| tui | ui-tui\src\components\thinking.tsx | 17 | English string, visibility unknown | } from '../lib/subagentTree.js' |
| tui | ui-tui\src\components\thinking.tsx | 31 | English string, visibility unknown | } from '../lib/text.js' |
| tui | ui-tui\src\components\thinking.tsx | 32 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\thinking.tsx | 41 | English string, visibility unknown | } from '../types.js' |
| tui | ui-tui\src\components\thinking.tsx | 49 | English string, visibility unknown | return sec < 10 ? `${sec.toFixed(1)}s` : `${Math.round(sec)}s` |
| tui | ui-tui\src\components\thinking.tsx | 64 | English string, visibility unknown | type TreeBranch = 'mid' \| 'last' |
| tui | ui-tui\src\components\thinking.tsx | 67 | English string, visibility unknown | const nextTreeRails = (rails: TreeRails, branch: TreeBranch) => [...rails, branch === 'mid'] |
| tui | ui-tui\src\components\thinking.tsx | 70 | English string, visibility unknown | `${rails.map(on => (on ? '│ ' : ' ')).join('')}${branch === 'mid' ? '├─ ' : '└─ '}` |
| tui | ui-tui\src\components\thinking.tsx | 98 | English string, visibility unknown | <Box flexDirection="column" flexGrow={1}> |
| tui | ui-tui\src\components\thinking.tsx | 112 | English string, visibility unknown | wrap = 'wrap-trim' |
| tui | ui-tui\src\components\thinking.tsx | 120 | English string, visibility unknown | wrap?: 'truncate-end' \| 'wrap' \| 'wrap-trim' |
| tui | ui-tui\src\components\thinking.tsx | 159 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\thinking.tsx | 168 | English string, visibility unknown | export function Spinner({ color, variant = 'think' }: { color: string; variant?: 'think' \| 'tool' }) { |
| tui | ui-tui\src\components\thinking.tsx | 198 | English string, visibility unknown | branch = 'last', |
| tui | ui-tui\src\components\thinking.tsx | 253 | English string, visibility unknown | tone = 'dim' |
| tui | ui-tui\src\components\thinking.tsx | 261 | English string, visibility unknown | tone?: 'dim' \| 'error' \| 'warn' |
| tui | ui-tui\src\components\thinking.tsx | 263 | English string, visibility unknown | const color = tone === 'error' ? t.color.error : tone === 'warn' ? t.color.warn : t.color.muted |
| tui | ui-tui\src\components\thinking.tsx | 267 | English string, visibility unknown | <Text color={color} dim={tone === 'dim'}> |
| tui | ui-tui\src\components\thinking.tsx | 270 | English string, visibility unknown | {typeof count === 'number' ? ` (${count})` : ''} |
| tui | ui-tui\src\components\thinking.tsx | 287 | English string, visibility unknown | // fade into the chrome — only "hot" branches draw the eye. |
| tui | ui-tui\src\components\thinking.tsx | 343 | English string, visibility unknown | const statusTone: 'dim' \| 'error' \| 'warn' = |
| tui | ui-tui\src\components\thinking.tsx | 344 | English string, visibility unknown | item.status === 'error' \|\| item.status === 'failed' |
| tui | ui-tui\src\components\thinking.tsx | 345 | English string, visibility unknown | ? 'error' |
| tui | ui-tui\src\components\thinking.tsx | 346 | English string, visibility unknown | : item.status === 'interrupted' \|\| item.status === 'timeout' |
| tui | ui-tui\src\components\thinking.tsx | 347 | English string, visibility unknown | ? 'warn' |
| tui | ui-tui\src\components\thinking.tsx | 348 | English string, visibility unknown | : 'dim' |
| tui | ui-tui\src\components\thinking.tsx | 350 | English string, visibility unknown | const prefix = item.taskCount > 1 ? `[${item.index + 1}/${item.taskCount}] ` : '' |
| tui | ui-tui\src\components\thinking.tsx | 351 | mixed Chinese and English, visibility unknown | const goalLabel = item.goal \|\| `派生任务 ${item.index + 1}` |
| tui | ui-tui\src\components\thinking.tsx | 352 | English string, visibility unknown | const title = `${prefix}${open ? goalLabel : compactPreview(goalLabel, 60)}` |
| tui | ui-tui\src\components\thinking.tsx | 353 | English string, visibility unknown | const summary = compactPreview((item.summary \|\| '').replace(/\s+/g, ' ').trim(), 72) |
| tui | ui-tui\src\components\thinking.tsx | 369 | mixed Chinese and English, visibility unknown | rollupBits.push(`${localTools} 工具`) |
| tui | ui-tui\src\components\thinking.tsx | 375 | mixed Chinese and English, visibility unknown | rollupBits.push(`${fmtTokens(localTokens)} 令牌`) |
| tui | ui-tui\src\components\thinking.tsx | 387 | English string, visibility unknown | rollupBits.push(`⎘${filesLocal}`) |
| tui | ui-tui\src\components\thinking.tsx | 391 | mixed Chinese and English, visibility unknown | rollupBits.push(`${aggregate.descendantCount} 下级`) |
| tui | ui-tui\src\components\thinking.tsx | 394 | mixed Chinese and English, visibility unknown | rollupBits.push(`+${subtreeTools} 工具`) |
| tui | ui-tui\src\components\thinking.tsx | 400 | mixed Chinese and English, visibility unknown | rollupBits.push(`+${fmtCost(subCost)} 下级`) |
| tui | ui-tui\src\components\thinking.tsx | 403 | English string, visibility unknown | if (aggregate.activeCount > 0 && item.status !== 'running') { |
| tui | ui-tui\src\components\thinking.tsx | 404 | English string, visibility unknown | rollupBits.push(`⚡${aggregate.activeCount}`) |
| tui | ui-tui\src\components\thinking.tsx | 415 | English string, visibility unknown | const noteColor = statusTone === 'error' ? t.color.error : statusTone === 'warn' ? t.color.warn : t.color.muted |
| tui | ui-tui\src\components\thinking.tsx | 445 | English string, visibility unknown | active={item.status === 'running'} |
| tui | ui-tui\src\components\thinking.tsx | 446 | English string, visibility unknown | branch="last" |
| tui | ui-tui\src\components\thinking.tsx | 447 | English string, visibility unknown | mode="full" |
| tui | ui-tui\src\components\thinking.tsx | 450 | English string, visibility unknown | streaming={item.status === 'running'} |
| tui | ui-tui\src\components\thinking.tsx | 477 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\thinking.tsx | 480 | English string, visibility unknown | branch={index === item.tools.length - 1 ? 'last' : 'mid'} |
| tui | ui-tui\src\components\thinking.tsx | 488 | English string, visibility unknown | key={`${item.id}-tool-${index}`} |
| tui | ui-tui\src\components\thinking.tsx | 519 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\thinking.tsx | 522 | English string, visibility unknown | branch={index === noteRows.length - 1 ? 'last' : 'mid'} |
| tui | ui-tui\src\components\thinking.tsx | 525 | English string, visibility unknown | dimColor={statusTone === 'dim'} |
| tui | ui-tui\src\components\thinking.tsx | 526 | English string, visibility unknown | key={`${item.id}-note-${index}`} |
| tui | ui-tui\src\components\thinking.tsx | 551 | mixed Chinese and English, visibility unknown | suffix={`第 ${item.depth + 1} 层 · 共 ${aggregate.descendantCount}`} |
| tui | ui-tui\src\components\thinking.tsx | 559 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\thinking.tsx | 562 | English string, visibility unknown | branch={i === children.length - 1 ? 'last' : 'mid'} |
| tui | ui-tui\src\components\thinking.tsx | 576 | English string, visibility unknown | // Heatmap: amber→error gradient on the stem when this branch is "hot" |
| tui | ui-tui\src\components\thinking.tsx | 614 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\thinking.tsx | 617 | English string, visibility unknown | branch={index === sections.length - 1 ? 'last' : 'mid'} |
| tui | ui-tui\src\components\thinking.tsx | 619 | English string, visibility unknown | key={`${item.id}-${section.key}`} |
| tui | ui-tui\src\components\thinking.tsx | 637 | English string, visibility unknown | branch = 'last', |
| tui | ui-tui\src\components\thinking.tsx | 638 | English string, visibility unknown | mode = 'truncated', |
| tui | ui-tui\src\components\thinking.tsx | 656 | English string, visibility unknown | return mode === 'full' ? boundedLiveRenderText(localized) : localized |
| tui | ui-tui\src\components\thinking.tsx | 659 | English string, visibility unknown | const lines = useMemo(() => preview.split('\n').map(line => line.replace(/\t/g, ' ')), [preview]) |
| tui | ui-tui\src\components\thinking.tsx | 667 | English string, visibility unknown | <Box flexDirection="column" flexGrow={1}> |
| tui | ui-tui\src\components\thinking.tsx | 669 | English string, visibility unknown | mode === 'full' ? ( |
| tui | ui-tui\src\components\thinking.tsx | 671 | English string, visibility unknown | <Text color={t.color.muted} key={index} wrap="wrap-trim"> |
| tui | ui-tui\src\components\thinking.tsx | 679 | English string, visibility unknown | <Text color={t.color.muted} wrap="truncate-end"> |
| tui | ui-tui\src\components\thinking.tsx | 708 | English string, visibility unknown | detailsMode = 'collapsed', |
| tui | ui-tui\src\components\thinking.tsx | 740 | English string, visibility unknown | thinking: sectionMode('thinking', detailsMode, sections, commandOverride), |
| tui | ui-tui\src\components\thinking.tsx | 741 | English string, visibility unknown | tools: sectionMode('tools', detailsMode, sections, commandOverride), |
| tui | ui-tui\src\components\thinking.tsx | 742 | English string, visibility unknown | subagents: sectionMode('subagents', detailsMode, sections, commandOverride), |
| tui | ui-tui\src\components\thinking.tsx | 743 | English string, visibility unknown | activity: sectionMode('activity', detailsMode, sections, commandOverride) |
| tui | ui-tui\src\components\thinking.tsx | 753 | English string, visibility unknown | // `visible.X === 'expanded'` at render time — that locks the panel open |
| tui | ui-tui\src\components\thinking.tsx | 756 | English string, visibility unknown | const [openThinking, setOpenThinking] = useState(visible.thinking === 'expanded') |
| tui | ui-tui\src\components\thinking.tsx | 757 | English string, visibility unknown | const [openTools, setOpenTools] = useState(visible.tools === 'expanded') |
| tui | ui-tui\src\components\thinking.tsx | 758 | English string, visibility unknown | const [openSubagents, setOpenSubagents] = useState(visible.subagents === 'expanded') |
| tui | ui-tui\src\components\thinking.tsx | 759 | English string, visibility unknown | const [deepSubagents, setDeepSubagents] = useState(visible.subagents === 'expanded') |
| tui | ui-tui\src\components\thinking.tsx | 760 | English string, visibility unknown | const [openMeta, setOpenMeta] = useState(visible.activity === 'expanded') |
| tui | ui-tui\src\components\thinking.tsx | 763 | English string, visibility unknown | if (!tools.length \|\| (visible.tools !== 'expanded' && !openTools)) { |
| tui | ui-tui\src\components\thinking.tsx | 773 | English string, visibility unknown | setOpenThinking(visible.thinking === 'expanded') |
| tui | ui-tui\src\components\thinking.tsx | 774 | English string, visibility unknown | setOpenTools(visible.tools === 'expanded') |
| tui | ui-tui\src\components\thinking.tsx | 775 | English string, visibility unknown | setOpenSubagents(visible.subagents === 'expanded') |
| tui | ui-tui\src\components\thinking.tsx | 776 | English string, visibility unknown | setOpenMeta(visible.activity === 'expanded') |
| tui | ui-tui\src\components\thinking.tsx | 835 | mixed Chinese and English, visibility unknown | if (line.startsWith('起草 ') \|\| line.startsWith('drafting ')) { |
| tui | ui-tui\src\components\thinking.tsx | 846 | mixed Chinese and English, visibility unknown | details: [{ color: t.color.muted, content: '正在准备...', dimColor: true, key: `tr-${i}-d` }], |
| tui | ui-tui\src\components\thinking.tsx | 855 | mixed Chinese and English, visibility unknown | if (line === '分析工具输出…' \|\| line === 'analyzing tool output…') { |
| tui | ui-tui\src\components\thinking.tsx | 862 | mixed Chinese and English, visibility unknown | <Spinner color={t.color.accent} variant="think" /> 正在分析工具输出… |
| tui | ui-tui\src\components\thinking.tsx | 886 | English string, visibility unknown | <Spinner color={t.color.accent} variant="tool" /> {label} |
| tui | ui-tui\src\components\thinking.tsx | 887 | English string, visibility unknown | {tool.startedAt ? ` (${fmtElapsed(now - tool.startedAt)})` : ''} |
| tui | ui-tui\src\components\thinking.tsx | 894 | English string, visibility unknown | const glyph = item.tone === 'error' ? '✗' : item.tone === 'warn' ? '!' : '·' |
| tui | ui-tui\src\components\thinking.tsx | 895 | English string, visibility unknown | const color = item.tone === 'error' ? t.color.error : item.tone === 'warn' ? t.color.warn : t.color.muted |
| tui | ui-tui\src\components\thinking.tsx | 896 | English string, visibility unknown | meta.push({ color, content: `${glyph} ${item.text}`, dimColor: item.tone === 'info', key: `a-${item.id}` }) |
| tui | ui-tui\src\components\thinking.tsx | 912 | mixed Chinese and English, visibility unknown | const thinkingTokensLabel = tokenCount > 0 ? `~${fmtK(tokenCount)} 令牌` : null |
| tui | ui-tui\src\components\thinking.tsx | 914 | mixed Chinese and English, visibility unknown | const toolTokensLabel = toolTokens !== undefined && toolTokens > 0 ? `~${fmtK(toolTokens)} 令牌` : undefined |
| tui | ui-tui\src\components\thinking.tsx | 916 | mixed Chinese and English, visibility unknown | const totalTokensLabel = tokenCount > 0 && toolTokenCount > 0 ? `~${fmtK(totalTokenCount)} 总计` : null |
| tui | ui-tui\src\components\thinking.tsx | 917 | mixed Chinese and English, visibility unknown | const delegateGroups = groups.filter(g => g.label.startsWith('Delegate Task') \|\| g.label.startsWith('派生任务')) |
| tui | ui-tui\src\components\thinking.tsx | 939 | English string, visibility unknown | // resolved to hidden — that way `details_mode: hidden` + `sections.tools: |
| tui | ui-tui\src\components\thinking.tsx | 945 | English string, visibility unknown | visible.thinking === 'hidden' && |
| tui | ui-tui\src\components\thinking.tsx | 946 | English string, visibility unknown | visible.tools === 'hidden' && |
| tui | ui-tui\src\components\thinking.tsx | 947 | English string, visibility unknown | visible.subagents === 'hidden' && |
| tui | ui-tui\src\components\thinking.tsx | 948 | English string, visibility unknown | visible.activity === 'hidden' |
| tui | ui-tui\src\components\thinking.tsx | 951 | English string, visibility unknown | const alerts = activity.filter(i => i.tone !== 'info').slice(-2) |
| tui | ui-tui\src\components\thinking.tsx | 954 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\thinking.tsx | 956 | English string, visibility unknown | <Text color={i.tone === 'error' ? t.color.error : t.color.warn} key={`ha-${i.id}`}> |
| tui | ui-tui\src\components\thinking.tsx | 957 | English string, visibility unknown | {i.tone === 'error' ? '✗' : '!'} {i.text} |
| tui | ui-tui\src\components\thinking.tsx | 970 | English string, visibility unknown | if (visible.thinking !== 'hidden') { |
| tui | ui-tui\src\components\thinking.tsx | 974 | English string, visibility unknown | if (visible.tools !== 'hidden') { |
| tui | ui-tui\src\components\thinking.tsx | 978 | English string, visibility unknown | if (visible.subagents !== 'hidden') { |
| tui | ui-tui\src\components\thinking.tsx | 983 | English string, visibility unknown | if (visible.activity !== 'hidden') { |
| tui | ui-tui\src\components\thinking.tsx | 988 | English string, visibility unknown | const metaTone: 'dim' \| 'error' \| 'warn' = activity.some(i => i.tone === 'error') |
| tui | ui-tui\src\components\thinking.tsx | 989 | English string, visibility unknown | ? 'error' |
| tui | ui-tui\src\components\thinking.tsx | 990 | English string, visibility unknown | : activity.some(i => i.tone === 'warn') |
| tui | ui-tui\src\components\thinking.tsx | 991 | English string, visibility unknown | ? 'warn' |
| tui | ui-tui\src\components\thinking.tsx | 992 | English string, visibility unknown | : 'dim' |
| tui | ui-tui\src\components\thinking.tsx | 995 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\thinking.tsx | 998 | English string, visibility unknown | branch={index === spawnTree.length - 1 ? 'last' : 'mid'} |
| tui | ui-tui\src\components\thinking.tsx | 999 | English string, visibility unknown | expanded={visible.subagents === 'expanded' \|\| deepSubagents} |
| tui | ui-tui\src\components\thinking.tsx | 1017 | English string, visibility unknown | if (hasThinking && visible.thinking !== 'hidden') { |
| tui | ui-tui\src\components\thinking.tsx | 1054 | English string, visibility unknown | branch="last" |
| tui | ui-tui\src\components\thinking.tsx | 1055 | English string, visibility unknown | mode="full" |
| tui | ui-tui\src\components\thinking.tsx | 1065 | English string, visibility unknown | if (hasTools && visible.tools !== 'hidden') { |
| tui | ui-tui\src\components\thinking.tsx | 1086 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\thinking.tsx | 1088 | English string, visibility unknown | const branch: TreeBranch = index === groups.length - 1 ? 'last' : 'mid' |
| tui | ui-tui\src\components\thinking.tsx | 1093 | English string, visibility unknown | <Box flexDirection="column" key={group.key}> |
| tui | ui-tui\src\components\thinking.tsx | 1110 | English string, visibility unknown | branch={detailIndex === group.details.length - 1 && !hasInlineSubagents ? 'last' : 'mid'} |
| tui | ui-tui\src\components\thinking.tsx | 1125 | English string, visibility unknown | if (hasSubagents && !inlineDelegateKey && visible.subagents !== 'hidden') { |
| tui | ui-tui\src\components\thinking.tsx | 1127 | English string, visibility unknown | // opening the subtree. `/agents` opens the full-screen audit overlay. |
| tui | ui-tui\src\components\thinking.tsx | 1128 | English string, visibility unknown | const suffix = spawnSpark ? `${spawnSummaryLabel} ${spawnSpark} (/agents)` : `${spawnSummaryLabel} (/agents)` |
| tui | ui-tui\src\components\thinking.tsx | 1155 | English string, visibility unknown | if (hasMeta && visible.activity !== 'hidden') { |
| tui | ui-tui\src\components\thinking.tsx | 1176 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\thinking.tsx | 1179 | English string, visibility unknown | branch={index === meta.length - 1 ? 'last' : 'mid'} |
| tui | ui-tui\src\components\thinking.tsx | 1196 | English string, visibility unknown | <Box flexDirection="column"> |
| tui | ui-tui\src\components\thinking.tsx | 1199 | English string, visibility unknown | branch={index === topCount - 1 ? 'last' : 'mid'} |
| tui | ui-tui\src\components\thinking.tsx | 1210 | English string, visibility unknown | branch="last" |
| tui | ui-tui\src\components\todoPanel.tsx | 1 | English string, visibility unknown | import { Box, Text } from '@hermes/ink' |
| tui | ui-tui\src\components\todoPanel.tsx | 2 | English string, visibility unknown | import { memo, useState } from 'react' |
| tui | ui-tui\src\components\todoPanel.tsx | 4 | English string, visibility unknown | import { countPendingTodos } from '../lib/liveProgress.js' |
| tui | ui-tui\src\components\todoPanel.tsx | 5 | English string, visibility unknown | import { todoGlyph, todoTone } from '../lib/todo.js' |
| tui | ui-tui\src\components\todoPanel.tsx | 6 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\components\todoPanel.tsx | 7 | English string, visibility unknown | import type { TodoItem } from '../types.js' |
| tui | ui-tui\src\components\todoPanel.tsx | 9 | English string, visibility unknown | const rowColor = (t: Theme, status: TodoItem['status']) => { |
| tui | ui-tui\src\components\todoPanel.tsx | 12 | English string, visibility unknown | return tone === 'active' ? t.color.text : tone === 'body' ? t.color.statusFg : t.color.muted |
| tui | ui-tui\src\components\todoPanel.tsx | 34 | English string, visibility unknown | const isControlled = typeof collapsed === 'boolean' |
| tui | ui-tui\src\components\todoPanel.tsx | 53 | English string, visibility unknown | const done = todos.filter(todo => todo.status === 'completed').length |
| tui | ui-tui\src\components\todoPanel.tsx | 57 | English string, visibility unknown | <Box flexDirection="column" marginBottom={1}> |
| tui | ui-tui\src\components\todoPanel.tsx | 77 | English string, visibility unknown | <Box flexDirection="column" marginLeft={2}> |
| tui | ui-tui\src\components\todoPanel.tsx | 83 | English string, visibility unknown | <Text color={color} dim={tone === 'dim'} key={todo.id}> |
| tui | ui-tui\src\components\tuiModuleDock.tsx | 1 | English string, visibility unknown | import { ModuleSlot } from './moduleSlot.js' |
| tui | ui-tui\src\components\tuiModuleDock.tsx | 4 | English string, visibility unknown | return <ModuleSlot cols={cols} slot="composer.dock" /> |
| tui | ui-tui\src\config\env.ts | 1 | English string, visibility unknown | import { isTermuxTuiMode } from '../lib/termux.js' |
| tui | ui-tui\src\content\fortunes.ts | 8 | mixed Chinese and English, visibility unknown | '需要的 helper 多半已经在代码库里', |
| tui | ui-tui\src\content\fortunes.ts | 17 | mixed Chinese and English, visibility unknown | '稀有掉落：diff 自己就能说明问题' |
| tui | ui-tui\src\content\fortunes.ts | 26 | English string, visibility unknown | return `${rare ? '🌟' : '🔮'} ${bag[n % bag.length]}` |
| tui | ui-tui\src\content\fortunes.ts | 30 | English string, visibility unknown | export const dailyFortune = (seed: null \| string) => fromScore(hash(`${seed \|\| 'anon'}\|${new Date().toDateString()}`)) |
| tui | ui-tui\src\content\hotkeys.ts | 1 | English string, visibility unknown | import { isMac, isRemoteShell } from '../lib/platform.js' |
| tui | ui-tui\src\content\hotkeys.ts | 3 | English string, visibility unknown | const action = isMac ? 'Cmd' : 'Ctrl' |
| tui | ui-tui\src\content\hotkeys.ts | 4 | English string, visibility unknown | const paste = isMac ? 'Cmd' : 'Alt' |
| tui | ui-tui\src\content\hotkeys.ts | 8 | mixed Chinese and English, visibility unknown | ['Cmd+C', '复制选区'], |
| tui | ui-tui\src\content\hotkeys.ts | 9 | mixed Chinese and English, visibility unknown | ['Ctrl+C', '中断 / 清空草稿 / 退出'] |
| tui | ui-tui\src\content\hotkeys.ts | 13 | mixed Chinese and English, visibility unknown | ['Cmd+C', '终端转发时复制选区'], |
| tui | ui-tui\src\content\hotkeys.ts | 14 | mixed Chinese and English, visibility unknown | ['Ctrl+C', '复制选区 / 中断 / 清空草稿 / 退出'] |
| tui | ui-tui\src\content\hotkeys.ts | 16 | mixed Chinese and English, visibility unknown | : [['Ctrl+C', '复制选区 / 中断 / 清空草稿 / 退出']] |
| tui | ui-tui\src\content\hotkeys.ts | 23 | mixed Chinese and English, visibility unknown | [paste + '+V / /paste', '粘贴文本；/paste 附加剪贴板图片'], |
| tui | ui-tui\src\content\hotkeys.ts | 24 | mixed Chinese and English, visibility unknown | ['Tab', '应用补全'], |
| tui | ui-tui\src\content\hotkeys.ts | 26 | mixed Chinese and English, visibility unknown | ['Ctrl+X', '删除正在编辑的队列消息（Esc 取消编辑）'], |
| tui | ui-tui\src\content\hotkeys.ts | 28 | mixed Chinese and English, visibility unknown | [action + '+Z / ' + action + '+Y', '撤销 / 重做输入编辑'], |
| tui | ui-tui\src\content\hotkeys.ts | 32 | mixed Chinese and English, visibility unknown | ['Home/End', '行首 / 行尾'], |
| tui | ui-tui\src\content\hotkeys.ts | 33 | mixed Chinese and English, visibility unknown | ['Shift+Enter / Alt+Enter', '插入换行'], |
| tui | ui-tui\src\content\hotkeys.ts | 34 | mixed Chinese and English, visibility unknown | ['\\+Enter', '多行续写（兜底）'], |
| tui | ui-tui\src\content\hotkeys.ts | 35 | mixed Chinese and English, visibility unknown | ['!<cmd>', '运行 shell 命令（例如 !ls, !git status）'], |
| tui | ui-tui\src\content\hotkeys.ts | 36 | mixed Chinese and English, visibility unknown | ['{!<cmd>}', '把 shell 输出插入到输入中（例如 "branch is {!git branch --show-current}"）'] |
| tui | ui-tui\src\content\placeholders.ts | 1 | English string, visibility unknown | import { pick } from '../lib/text.js' |
| tui | ui-tui\src\content\placeholders.ts | 8 | mixed Chinese and English, visibility unknown | '输入 "/help" 查看命令', |
| tui | ui-tui\src\content\placeholders.ts | 9 | mixed Chinese and English, visibility unknown | '试试："修复 lint 错误"', |
| tui | ui-tui\src\content\setup.ts | 1 | English string, visibility unknown | import type { PanelSection } from '../types.js' |
| tui | ui-tui\src\content\setup.ts | 12 | mixed Chinese and English, visibility unknown | ['/setup', '在当前界面运行首次设置向导'], |
| tui | ui-tui\src\content\setup.ts | 13 | mixed Chinese and English, visibility unknown | ['Ctrl+C', '退出后手动运行 `hermes setup`'] |
| tui | ui-tui\src\domain\details.ts | 1 | English string, visibility unknown | import type { DetailsMode, SectionName, SectionVisibility } from '../types.js' |
| tui | ui-tui\src\domain\details.ts | 21 | English string, visibility unknown | // Opt out of any of these with `display.sections.<name>` in config.yaml |
| tui | ui-tui\src\domain\details.ts | 22 | English string, visibility unknown | // or at runtime via `/details <name> collapsed\|hidden`. |
| tui | ui-tui\src\domain\details.ts | 52 | English string, visibility unknown | raw && typeof raw === 'object' && !Array.isArray(raw) |
| tui | ui-tui\src\domain\details.ts | 63 | English string, visibility unknown | // The `commandOverride` flag is set for in-session `/details <mode>` changes. |
| tui | ui-tui\src\domain\messages.ts | 2 | English string, visibility unknown | import { buildToolTrailLine, fmtK } from '../lib/text.js' |
| tui | ui-tui\src\domain\messages.ts | 3 | English string, visibility unknown | import type { Msg, SessionInfo } from '../types.js' |
| tui | ui-tui\src\domain\messages.ts | 5 | English string, visibility unknown | export const introMsg = (info: SessionInfo): Msg => ({ info, kind: 'intro', role: 'system', text: '' }) |
| tui | ui-tui\src\domain\messages.ts | 10 | mixed Chinese and English, visibility unknown | return [width && height ? `${width}x${height}` : '', (t ?? 0) > 0 ? `~${fmtK(t!)} 令牌` : ''] |
| tui | ui-tui\src\domain\messages.ts | 17 | mixed Chinese and English, visibility unknown | const label = info?.name ? `📎 已附加图片: ${info.name}` : '📎 已附加图片' |
| tui | ui-tui\src\domain\messages.ts | 19 | English string, visibility unknown | return `${label}${meta ? ` · ${meta}` : ''}` |
| tui | ui-tui\src\domain\messages.ts | 27 | English string, visibility unknown | const first = text.split('\n')[0]?.trim() ?? '' |
| tui | ui-tui\src\domain\messages.ts | 31 | mixed Chinese and English, visibility unknown | return `${prefix \|\| '（消息）'} [长消息]` |
| tui | ui-tui\src\domain\messages.ts | 43 | English string, visibility unknown | if (!row \|\| typeof row !== 'object') { |
| tui | ui-tui\src\domain\messages.ts | 49 | English string, visibility unknown | if (role === 'tool') { |
| tui | ui-tui\src\domain\messages.ts | 50 | English string, visibility unknown | pending.push(buildToolTrailLine(name ?? 'tool', context ?? '')) |
| tui | ui-tui\src\domain\messages.ts | 55 | English string, visibility unknown | if (typeof text !== 'string' \|\| !text.trim()) { |
| tui | ui-tui\src\domain\messages.ts | 59 | English string, visibility unknown | if (role === 'assistant') { |
| tui | ui-tui\src\domain\messages.ts | 62 | English string, visibility unknown | } else if (role === 'user' \|\| role === 'system') { |
| tui | ui-tui\src\domain\paths.ts | 3 | English string, visibility unknown | const p = h && cwd.startsWith(h) ? `~${cwd.slice(h.length)}` : cwd |
| tui | ui-tui\src\domain\paths.ts | 5 | English string, visibility unknown | return p.length <= max ? p : `…${p.slice(-(max - 1))}` |
| tui | ui-tui\src\domain\paths.ts | 13 | English string, visibility unknown | const tag = ` (${branch.length > 16 ? `…${branch.slice(-15)}` : branch})` |
| tui | ui-tui\src\domain\paths.ts | 15 | English string, visibility unknown | return `${shortCwd(cwd, Math.max(8, max - tag.length))}${tag}` |
| tui | ui-tui\src\domain\providers.ts | 9 | English string, visibility unknown | (counts.get(p.name) ?? 0) > 1 && p.slug && p.slug !== p.name ? `${p.name} (${p.slug})` : p.name |
| tui | ui-tui\src\domain\roles.ts | 1 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\domain\roles.ts | 2 | English string, visibility unknown | import type { Role } from '../types.js' |
| tui | ui-tui\src\domain\roles.ts | 6 | English string, visibility unknown | system: t => ({ body: '', glyph: '·', prefix: t.color.muted }), |
| tui | ui-tui\src\domain\usage.ts | 1 | English string, visibility unknown | import type { Usage } from '../types.js' |
| tui | ui-tui\src\domain\viewport.ts | 1 | English string, visibility unknown | import type { Msg } from '../types.js' |
| tui | ui-tui\src\domain\viewport.ts | 3 | English string, visibility unknown | import { userDisplay } from './messages.js' |
| tui | ui-tui\src\domain\viewport.ts | 35 | English string, visibility unknown | if (messages[i]?.role === 'user') { |
| tui | ui-tui\src\domain\viewport.ts | 41 | English string, visibility unknown | if (messages[i]?.role !== 'user') { |
| tui | ui-tui\src\entry.tsx | 4 | English string, visibility unknown | import './lib/forceTruecolor.js' |
| tui | ui-tui\src\entry.tsx | 6 | English string, visibility unknown | import type { FrameEvent } from '@hermes/ink' |
| tui | ui-tui\src\entry.tsx | 9 | English string, visibility unknown | import { GatewayClient } from './gatewayClient.js' |
| tui | ui-tui\src\entry.tsx | 10 | English string, visibility unknown | import { setupGracefulExit } from './lib/gracefulExit.js' |
| tui | ui-tui\src\entry.tsx | 11 | English string, visibility unknown | import { formatBytes, type HeapDumpResult, performHeapDump } from './lib/memory.js' |
| tui | ui-tui\src\entry.tsx | 12 | English string, visibility unknown | import { type MemorySnapshot, startMemoryMonitor } from './lib/memoryMonitor.js' |
| tui | ui-tui\src\entry.tsx | 13 | English string, visibility unknown | import { openExternalUrl } from './lib/openExternalUrl.js' |
| tui | ui-tui\src\entry.tsx | 14 | English string, visibility unknown | import { resetTerminalModes } from './lib/terminalModes.js' |
| tui | ui-tui\src\entry.tsx | 39 | mixed Chinese and English, visibility unknown | `hermes-tui: 内存 ${snap.level}（${formatBytes(snap.heapUsed)}）— 自动堆快照 → ${dump?.heapPath ?? '失败'}\n` |
| tui | ui-tui\src\entry.tsx | 50 | English string, visibility unknown | const message = err instanceof Error ? `${err.name}: ${err.message}` : String(err) |
| tui | ui-tui\src\entry.tsx | 52 | mixed Chinese and English, visibility unknown | process.stderr.write(`hermes-tui ${scope} 错误: ${message.slice(0, 2000)}\n`) |
| tui | ui-tui\src\entry.tsx | 56 | mixed Chinese and English, visibility unknown | process.stderr.write(`hermes-tui: 收到 ${signal}\n`) |
| tui | ui-tui\src\entry.tsx | 64 | mixed Chinese and English, visibility unknown | process.stderr.write('hermes-tui: 为避免内存耗尽已退出；重启后恢复\n') |
| tui | ui-tui\src\entry.tsx | 71 | English string, visibility unknown | void performHeapDump('manual') |
| tui | ui-tui\src\entry.tsx | 74 | English string, visibility unknown | process.on('beforeExit', () => stopMemoryMonitor()) |
| tui | ui-tui\src\entry.tsx | 77 | English string, visibility unknown | import('@hermes/ink'), |
| tui | ui-tui\src\entry.tsx | 78 | English string, visibility unknown | import('./app.js'), |
| tui | ui-tui\src\entry.tsx | 79 | English string, visibility unknown | import('./lib/perfPane.js'), |
| tui | ui-tui\src\entry.tsx | 80 | English string, visibility unknown | import('./lib/fpsStore.js') |
| tui | ui-tui\src\gatewayClient.ts | 1 | English string, visibility unknown | import { type ChildProcess, spawn } from 'node:child_process' |
| tui | ui-tui\src\gatewayClient.ts | 2 | English string, visibility unknown | import { EventEmitter } from 'node:events' |
| tui | ui-tui\src\gatewayClient.ts | 3 | English string, visibility unknown | import { existsSync } from 'node:fs' |
| tui | ui-tui\src\gatewayClient.ts | 4 | English string, visibility unknown | import { delimiter, resolve } from 'node:path' |
| tui | ui-tui\src\gatewayClient.ts | 5 | English string, visibility unknown | import { createInterface } from 'node:readline' |
| tui | ui-tui\src\gatewayClient.ts | 7 | English string, visibility unknown | import type { GatewayEvent } from './gatewayTypes.js' |
| tui | ui-tui\src\gatewayClient.ts | 8 | English string, visibility unknown | import { CircularBuffer } from './lib/circularBuffer.js' |
| tui | ui-tui\src\gatewayClient.ts | 46 | English string, visibility unknown | venv && resolve(venv, 'bin/python'), |
| tui | ui-tui\src\gatewayClient.ts | 47 | English string, visibility unknown | venv && resolve(venv, 'Scripts/python.exe'), |
| tui | ui-tui\src\gatewayClient.ts | 48 | English string, visibility unknown | resolve(root, '.venv/bin/python'), |
| tui | ui-tui\src\gatewayClient.ts | 49 | English string, visibility unknown | resolve(root, '.venv/bin/python3'), |
| tui | ui-tui\src\gatewayClient.ts | 50 | English string, visibility unknown | resolve(root, 'venv/bin/python'), |
| tui | ui-tui\src\gatewayClient.ts | 51 | English string, visibility unknown | resolve(root, 'venv/bin/python3') |
| tui | ui-tui\src\gatewayClient.ts | 54 | English string, visibility unknown | return hit \|\| (process.platform === 'win32' ? 'python' : 'python3') |
| tui | ui-tui\src\gatewayClient.ts | 58 | English string, visibility unknown | value && typeof value === 'object' && !Array.isArray(value) && typeof (value as { type?: unknown }).type === 'string' |
| tui | ui-tui\src\gatewayClient.ts | 69 | English string, visibility unknown | if (typeof raw === 'string') { |
| tui | ui-tui\src\gatewayClient.ts | 84 | English string, visibility unknown | // Matches `<scheme>://user:pass@host…` style user-info segments in |
| tui | ui-tui\src\gatewayClient.ts | 86 | English string, visibility unknown | // Used by the `redactUrl` fallback so embedded credentials are |
| tui | ui-tui\src\gatewayClient.ts | 92 | English string, visibility unknown | // `gateway.start_timeout` payload, so always strip the query string and any |
| tui | ui-tui\src\gatewayClient.ts | 104 | English string, visibility unknown | return `${url.protocol}//${userInfo}${url.host}${url.pathname}${query}` |
| tui | ui-tui\src\gatewayClient.ts | 112 | English string, visibility unknown | return queryIdx >= 0 ? `${noUserInfo.slice(0, queryIdx)}?***` : noUserInfo |
| tui | ui-tui\src\gatewayClient.ts | 150 | English string, visibility unknown | if (ev.type === 'gateway.ready') { |
| tui | ui-tui\src\gatewayClient.ts | 160 | English string, visibility unknown | return void this.emit('event', ev) |
| tui | ui-tui\src\gatewayClient.ts | 185 | English string, visibility unknown | // implementations dispatch the 'close' event after a microtask hop, |
| tui | ui-tui\src\gatewayClient.ts | 186 | English string, visibility unknown | // so by the time the handler runs `this.ws` should already be null |
| tui | ui-tui\src\gatewayClient.ts | 205 | English string, visibility unknown | // never fire `rejectPending`, leaving callers hanging on promises |
| tui | ui-tui\src\gatewayClient.ts | 207 | English string, visibility unknown | this.rejectPending(new Error('gateway restarting')) |
| tui | ui-tui\src\gatewayClient.ts | 225 | English string, visibility unknown | // event so users can tell apart "wrong python", "missing dep", |
| tui | ui-tui\src\gatewayClient.ts | 226 | English string, visibility unknown | // and "config parse failure" from one glance instead of having |
| tui | ui-tui\src\gatewayClient.ts | 227 | English string, visibility unknown | // to dig through `/logs`. Capped to keep the activity feed |
| tui | ui-tui\src\gatewayClient.ts | 231 | English string, visibility unknown | this.pushLog(`[startup] timed out waiting for gateway.ready (python=${python}, cwd=${cwd})`) |
| tui | ui-tui\src\gatewayClient.ts | 242 | English string, visibility unknown | this.rejectPending(new Error(reason \|\| `gateway exited${code === null ? '' : ` (${code})`}`)) |
| tui | ui-tui\src\gatewayClient.ts | 245 | English string, visibility unknown | this.emit('exit', code) |
| tui | ui-tui\src\gatewayClient.ts | 258 | English string, visibility unknown | if (typeof WebSocket === 'undefined') { |
| tui | ui-tui\src\gatewayClient.ts | 259 | English string, visibility unknown | this.pushLog(`[sidecar] WebSocket unavailable; skipping mirror to ${redactUrl(this.sidecarUrl)}`) |
| tui | ui-tui\src\gatewayClient.ts | 267 | English string, visibility unknown | ws.addEventListener('close', () => { |
| tui | ui-tui\src\gatewayClient.ts | 272 | English string, visibility unknown | ws.addEventListener('error', () => { |
| tui | ui-tui\src\gatewayClient.ts | 273 | English string, visibility unknown | this.pushLog('[sidecar] mirror connection error') |
| tui | ui-tui\src\gatewayClient.ts | 276 | English string, visibility unknown | this.pushLog(`[sidecar] failed to connect ${redactUrl(this.sidecarUrl)} (constructor error)`) |
| tui | ui-tui\src\gatewayClient.ts | 305 | English string, visibility unknown | if (frame.method === 'event') { |
| tui | ui-tui\src\gatewayClient.ts | 313 | English string, visibility unknown | this.pushLog(`[protocol] malformed websocket frame: ${preview}`) |
| tui | ui-tui\src\gatewayClient.ts | 314 | English string, visibility unknown | this.publish({ type: 'gateway.protocol_error', payload: { preview } }) |
| tui | ui-tui\src\gatewayClient.ts | 326 | English string, visibility unknown | this.proc = spawn(python, ['-m', 'tui_gateway.entry'], { cwd, env, stdio: ['pipe', 'pipe', 'pipe'] }) |
| tui | ui-tui\src\gatewayClient.ts | 329 | English string, visibility unknown | this.stdoutRl.on('line', raw => { |
| tui | ui-tui\src\gatewayClient.ts | 335 | English string, visibility unknown | this.pushLog(`[protocol] malformed stdout: ${preview}`) |
| tui | ui-tui\src\gatewayClient.ts | 336 | English string, visibility unknown | this.publish({ type: 'gateway.protocol_error', payload: { preview } }) |
| tui | ui-tui\src\gatewayClient.ts | 341 | English string, visibility unknown | this.stderrRl.on('line', raw => { |
| tui | ui-tui\src\gatewayClient.ts | 349 | English string, visibility unknown | this.publish({ type: 'gateway.stderr', payload: { line } }) |
| tui | ui-tui\src\gatewayClient.ts | 353 | English string, visibility unknown | this.proc.on('error', err => { |
| tui | ui-tui\src\gatewayClient.ts | 359 | English string, visibility unknown | const line = `[spawn] ${err.message}` |
| tui | ui-tui\src\gatewayClient.ts | 362 | English string, visibility unknown | this.publish({ type: 'gateway.stderr', payload: { line } }) |
| tui | ui-tui\src\gatewayClient.ts | 363 | English string, visibility unknown | // Detach the reference up front so the late `exit` event for |
| tui | ui-tui\src\gatewayClient.ts | 365 | English string, visibility unknown | // 'exit' twice). Then run the full teardown — clears the |
| tui | ui-tui\src\gatewayClient.ts | 367 | English string, visibility unknown | // `gateway.start_timeout`, rejects pending RPCs, and emits or |
| tui | ui-tui\src\gatewayClient.ts | 368 | English string, visibility unknown | // queues a single `exit`. |
| tui | ui-tui\src\gatewayClient.ts | 370 | English string, visibility unknown | this.handleTransportExit(1, `gateway error: ${err.message}`) |
| tui | ui-tui\src\gatewayClient.ts | 372 | English string, visibility unknown | this.proc.on('exit', code => { |
| tui | ui-tui\src\gatewayClient.ts | 373 | English string, visibility unknown | // start() can replace `this.proc` while an old child is still |
| tui | ui-tui\src\gatewayClient.ts | 386 | English string, visibility unknown | this.startReadyTimer('websocket', safeAttachUrl) |
| tui | ui-tui\src\gatewayClient.ts | 388 | English string, visibility unknown | if (typeof WebSocket === 'undefined') { |
| tui | ui-tui\src\gatewayClient.ts | 392 | English string, visibility unknown | this.publish({ type: 'gateway.stderr', payload: { line } }) |
| tui | ui-tui\src\gatewayClient.ts | 393 | English string, visibility unknown | this.handleTransportExit(1, 'gateway websocket unavailable') |
| tui | ui-tui\src\gatewayClient.ts | 405 | English string, visibility unknown | 'open', |
| tui | ui-tui\src\gatewayClient.ts | 418 | English string, visibility unknown | 'error', |
| tui | ui-tui\src\gatewayClient.ts | 421 | English string, visibility unknown | this.pushLog('[startup] gateway websocket connect error') |
| tui | ui-tui\src\gatewayClient.ts | 423 | English string, visibility unknown | reject(new Error('gateway websocket connection failed')) |
| tui | ui-tui\src\gatewayClient.ts | 429 | English string, visibility unknown | 'close', |
| tui | ui-tui\src\gatewayClient.ts | 433 | English string, visibility unknown | reject(new Error(`gateway websocket closed (${ev.code}) during connect`)) |
| tui | ui-tui\src\gatewayClient.ts | 449 | English string, visibility unknown | ws.addEventListener('message', ev => this.handleWebSocketFrame(ev.data)) |
| tui | ui-tui\src\gatewayClient.ts | 450 | English string, visibility unknown | ws.addEventListener('close', ev => { |
| tui | ui-tui\src\gatewayClient.ts | 452 | English string, visibility unknown | // replaced — start() / closeGatewaySocket() can swap `this.ws` |
| tui | ui-tui\src\gatewayClient.ts | 462 | English string, visibility unknown | this.handleTransportExit(ev.code, `gateway websocket closed${ev.code ? ` (${ev.code})` : ''}`) |
| tui | ui-tui\src\gatewayClient.ts | 464 | English string, visibility unknown | ws.addEventListener('error', () => { |
| tui | ui-tui\src\gatewayClient.ts | 465 | English string, visibility unknown | const line = '[gateway] websocket transport error' |
| tui | ui-tui\src\gatewayClient.ts | 468 | English string, visibility unknown | this.publish({ type: 'gateway.stderr', payload: { line } }) |
| tui | ui-tui\src\gatewayClient.ts | 471 | English string, visibility unknown | this.pushLog(`[startup] failed to connect websocket gateway ${safeAttachUrl} (constructor error)`) |
| tui | ui-tui\src\gatewayClient.ts | 472 | English string, visibility unknown | this.handleTransportExit(1, 'gateway websocket startup failed') |
| tui | ui-tui\src\gatewayClient.ts | 510 | English string, visibility unknown | if (msg.method === 'event') { |
| tui | ui-tui\src\gatewayClient.ts | 522 | mixed Chinese and English, visibility unknown | return new Error(typeof err?.message === 'string' ? err.message : '请求失败') |
| tui | ui-tui\src\gatewayClient.ts | 549 | English string, visibility unknown | // Arrow class-field — stable identity, so `setTimeout(this.onTimeout, …, id)` |
| tui | ui-tui\src\gatewayClient.ts | 556 | English string, visibility unknown | p.reject(new Error(`timeout: ${p.method}`)) |
| tui | ui-tui\src\gatewayClient.ts | 564 | English string, visibility unknown | this.emit('event', ev) |
| tui | ui-tui\src\gatewayClient.ts | 571 | English string, visibility unknown | this.emit('exit', code) |
| tui | ui-tui\src\gatewayClient.ts | 581 | English string, visibility unknown | throw new Error('gateway not running') |
| tui | ui-tui\src\gatewayClient.ts | 597 | English string, visibility unknown | throw new Error(`gateway not connected: ${method}`) |
| tui | ui-tui\src\gatewayClient.ts | 607 | English string, visibility unknown | const id = `r${++this.reqId}` |
| tui | ui-tui\src\gatewayClient.ts | 642 | English string, visibility unknown | // tears down the old Python child. Merely closing `this.ws` |
| tui | ui-tui\src\gatewayClient.ts | 644 | English string, visibility unknown | this.rejectPending(new Error('gateway attach url changed')) |
| tui | ui-tui\src\gatewayClient.ts | 656 | English string, visibility unknown | return Promise.reject(new Error('gateway not running')) |
| tui | ui-tui\src\gatewayClient.ts | 659 | English string, visibility unknown | const id = `r${++this.reqId}` |
| tui | ui-tui\src\gatewayClient.ts | 694 | English string, visibility unknown | // The ws 'close' handler is identity-gated on `this.ws === ws` |
| tui | ui-tui\src\gatewayClient.ts | 695 | English string, visibility unknown | // and we just nulled `this.ws`, so it will short-circuit and |
| tui | ui-tui\src\gatewayClient.ts | 698 | English string, visibility unknown | this.rejectPending(new Error('gateway closed')) |
| tui | ui-tui\src\gatewayTypes.ts | 1 | English string, visibility unknown | import type { SessionInfo, SlashCategory, SubagentStatus, Usage } from './types.js' |
| tui | ui-tui\src\gatewayTypes.ts | 23 | English string, visibility unknown | role: 'assistant' \| 'system' \| 'tool' \| 'user' |
| tui | ui-tui\src\gatewayTypes.ts | 49 | English string, visibility unknown | \| { output?: string; type: 'exec' \| 'plugin' } |
| tui | ui-tui\src\gatewayTypes.ts | 50 | English string, visibility unknown | \| { target: string; type: 'alias' } |
| tui | ui-tui\src\gatewayTypes.ts | 51 | English string, visibility unknown | \| { message?: string; name: string; type: 'skill' } |
| tui | ui-tui\src\gatewayTypes.ts | 52 | English string, visibility unknown | \| { message: string; notice?: string; type: 'send' } |
| tui | ui-tui\src\gatewayTypes.ts | 73 | English string, visibility unknown | // `normalizeIndicatorStyle` falls back to 'kaomoji' for those — but the |
| tui | ui-tui\src\gatewayTypes.ts | 74 | English string, visibility unknown | // wire type is documented as `string` so consumers don't get a false |
| tui | ui-tui\src\gatewayTypes.ts | 78 | English string, visibility unknown | tui_statusbar?: 'bottom' \| 'off' \| 'on' \| 'top' \| boolean |
| tui | ui-tui\src\gatewayTypes.ts | 82 | English string, visibility unknown | // Raw `yaml.safe_load()` value from config; may be non-string if hand-edited. |
| tui | ui-tui\src\gatewayTypes.ts | 174 | English string, visibility unknown | cost_status?: 'estimated' \| 'exact' |
| tui | ui-tui\src\gatewayTypes.ts | 217 | English string, visibility unknown | status?: 'queued' \| 'rejected' |
| tui | ui-tui\src\gatewayTypes.ts | 301 | English string, visibility unknown | status?: 'busy' \| 'recording' \| 'stopped' |
| tui | ui-tui\src\gatewayTypes.ts | 473 | English string, visibility unknown | payload?: { level?: 'info' \| 'warn' \| 'error'; message?: string } |
| tui | ui-tui\src\gatewayTypes.ts | 509 | English string, visibility unknown | \| { payload: { command: string; description: string }; session_id?: string; type: 'approval.request' } |
| tui | ui-tui\src\gatewayTypes.ts | 512 | English string, visibility unknown | \| { payload: { task_id: string; text: string }; session_id?: string; type: 'background.complete' } |
| tui | ui-tui\src\hooks\useCompletion.ts | 1 | English string, visibility unknown | import { useEffect, useRef, useState } from 'react' |
| tui | ui-tui\src\hooks\useCompletion.ts | 3 | English string, visibility unknown | import type { CompletionItem } from '../app/interfaces.js' |
| tui | ui-tui\src\hooks\useCompletion.ts | 4 | English string, visibility unknown | import { looksLikeSlashCommand } from '../domain/slash.js' |
| tui | ui-tui\src\hooks\useCompletion.ts | 5 | English string, visibility unknown | import type { GatewayClient } from '../gatewayClient.js' |
| tui | ui-tui\src\hooks\useCompletion.ts | 6 | English string, visibility unknown | import type { CompletionResponse } from '../gatewayTypes.js' |
| tui | ui-tui\src\hooks\useCompletion.ts | 7 | English string, visibility unknown | import { asRpcResult } from '../lib/rpc.js' |
| tui | ui-tui\src\hooks\useCompletion.ts | 14 | English string, visibility unknown | \| { method: 'complete.path'; params: { word: string }; replaceFrom: number } |
| tui | ui-tui\src\hooks\useCompletion.ts | 15 | English string, visibility unknown | \| { method: 'complete.slash'; params: { text: string }; replaceFrom: number } |
| tui | ui-tui\src\hooks\useCompletion.ts | 31 | English string, visibility unknown | return { method: 'complete.slash', params: { text: input }, replaceFrom: 1 } |
| tui | ui-tui\src\hooks\useCompletion.ts | 89 | English string, visibility unknown | setCompReplace(request.method === 'complete.slash' ? (r?.replace_from ?? 1) : request.replaceFrom) |
| tui | ui-tui\src\hooks\useCompletion.ts | 99 | English string, visibility unknown | display: 'completion unavailable', |
| tui | ui-tui\src\hooks\useCompletion.ts | 100 | English string, visibility unknown | meta: e instanceof Error && e.message ? e.message : 'unavailable' |
| tui | ui-tui\src\hooks\useGitBranch.ts | 1 | English string, visibility unknown | import { execFile } from 'node:child_process' |
| tui | ui-tui\src\hooks\useGitBranch.ts | 2 | English string, visibility unknown | import { promisify } from 'node:util' |
| tui | ui-tui\src\hooks\useGitBranch.ts | 4 | English string, visibility unknown | import { useEffect, useState } from 'react' |
| tui | ui-tui\src\hooks\useInputHistory.ts | 1 | English string, visibility unknown | import { useRef, useState } from 'react' |
| tui | ui-tui\src\hooks\useInputHistory.ts | 3 | English string, visibility unknown | import * as inputHistory from '../lib/history.js' |
| tui | ui-tui\src\hooks\useQueue.ts | 1 | English string, visibility unknown | import { useCallback, useRef, useState } from 'react' |
| tui | ui-tui\src\hooks\useQueue.ts | 3 | English string, visibility unknown | // Mutates `arr` in place; returned reference is the same input array, kept |
| tui | ui-tui\src\hooks\useQueue.ts | 4 | English string, visibility unknown | // so callers can chain. Use `Array.prototype.toSpliced` if you need a copy. |
| tui | ui-tui\src\hooks\useVirtualHistory.ts | 1 | English string, visibility unknown | import type { ScrollBoxHandle } from '@hermes/ink' |
| tui | ui-tui\src\hooks\useVirtualHistory.ts | 11 | English string, visibility unknown | } from 'react' |
| tui | ui-tui\src\hooks\useVirtualHistory.ts | 33 | English string, visibility unknown | // wheel ticks that don't cross a bin short-circuit React's commit entirely; |
| tui | ui-tui\src\hooks\useVirtualHistory.ts | 40 | English string, visibility unknown | // doesn't poison the scaled cache; render #2's useLayoutEffect captures |
| tui | ui-tui\src\hooks\useVirtualHistory.ts | 381 | English string, visibility unknown | // the user feels "stuck before bottom". effStart stays deferred so scroll- |
| tui | ui-tui\src\lib\circularBuffer.ts | 8 | English string, visibility unknown | throw new RangeError(`CircularBuffer capacity must be a positive integer, got ${capacity}`) |
| tui | ui-tui\src\lib\clipboard.ts | 1 | English string, visibility unknown | import { execFile, spawn } from 'node:child_process' |
| tui | ui-tui\src\lib\clipboard.ts | 2 | English string, visibility unknown | import { promisify } from 'node:util' |
| tui | ui-tui\src\lib\clipboard.ts | 25 | English string, visibility unknown | if (isControl \|\| ch === '\ufffd') { |
| tui | ui-tui\src\lib\clipboard.ts | 37 | English string, visibility unknown | if (platform === 'darwin') { |
| tui | ui-tui\src\lib\clipboard.ts | 38 | English string, visibility unknown | return [{ cmd: 'pbpaste', args: [] }] |
| tui | ui-tui\src\lib\clipboard.ts | 41 | English string, visibility unknown | if (platform === 'win32') { |
| tui | ui-tui\src\lib\clipboard.ts | 52 | English string, visibility unknown | attempts.push({ cmd: 'wl-paste', args: ['--type', 'text'] }) |
| tui | ui-tui\src\lib\clipboard.ts | 55 | English string, visibility unknown | attempts.push({ cmd: 'xclip', args: ['-selection', 'clipboard', '-out'] }) |
| tui | ui-tui\src\lib\clipboard.ts | 83 | English string, visibility unknown | if (typeof result.stdout === 'string') { |
| tui | ui-tui\src\lib\clipboard.ts | 98 | English string, visibility unknown | if (platform === 'darwin') { |
| tui | ui-tui\src\lib\clipboard.ts | 99 | English string, visibility unknown | return [{ cmd: 'pbcopy', args: [] }] |
| tui | ui-tui\src\lib\clipboard.ts | 102 | English string, visibility unknown | if (platform === 'win32') { |
| tui | ui-tui\src\lib\clipboard.ts | 103 | English string, visibility unknown | return [{ cmd: 'powershell', args: ['-NoProfile', '-NonInteractive', '-Command', 'Set-Clipboard -Value $input'] }] |
| tui | ui-tui\src\lib\clipboard.ts | 111 | English string, visibility unknown | args: ['-NoProfile', '-NonInteractive', '-Command', 'Set-Clipboard -Value $input'] |
| tui | ui-tui\src\lib\clipboard.ts | 119 | English string, visibility unknown | attempts.push({ cmd: 'xclip', args: ['-selection', 'clipboard', '-in'] }) |
| tui | ui-tui\src\lib\clipboard.ts | 120 | English string, visibility unknown | attempts.push({ cmd: 'xsel', args: ['--clipboard', '--input'] }) |
| tui | ui-tui\src\lib\clipboard.ts | 150 | English string, visibility unknown | const child = start(cmd, [...args], { stdio: ['pipe', 'ignore', 'ignore'], windowsHide: true }) |
| tui | ui-tui\src\lib\clipboard.ts | 152 | English string, visibility unknown | child.once('error', () => resolve(false)) |
| tui | ui-tui\src\lib\clipboard.ts | 153 | English string, visibility unknown | child.once('close', code => resolve(code === 0)) |
| tui | ui-tui\src\lib\editor.ts | 1 | English string, visibility unknown | import { accessSync, constants } from 'node:fs' |
| tui | ui-tui\src\lib\editor.ts | 2 | English string, visibility unknown | import { delimiter, join } from 'node:path' |
| tui | ui-tui\src\lib\editor.ts | 26 | English string, visibility unknown | * 3. on Windows: `notepad.exe` |
| tui | ui-tui\src\lib\editor.ts | 39 | English string, visibility unknown | if (platform === 'win32') { |
| tui | ui-tui\src\lib\editor.ts | 40 | English string, visibility unknown | return ['notepad.exe'] |
| tui | ui-tui\src\lib\emoji.ts | 46 | English string, visibility unknown | out += text.slice(last, i + size) + '\uFE0F' |
| tui | ui-tui\src\lib\externalCli.ts | 1 | English string, visibility unknown | import { spawn } from 'node:child_process' |
| tui | ui-tui\src\lib\externalCli.ts | 12 | English string, visibility unknown | const child = spawn(resolveHermesBin(), args, { stdio: 'inherit' }) |
| tui | ui-tui\src\lib\externalCli.ts | 14 | English string, visibility unknown | child.on('error', err => resolve({ code: null, error: err.message })) |
| tui | ui-tui\src\lib\externalCli.ts | 15 | English string, visibility unknown | child.on('exit', code => resolve({ code })) |
| tui | ui-tui\src\lib\externalLink.ts | 1 | English string, visibility unknown | import { isIP } from 'node:net' |
| tui | ui-tui\src\lib\externalLink.ts | 3 | English string, visibility unknown | import { useEffect, useMemo, useState } from 'react' |
| tui | ui-tui\src\lib\externalLink.ts | 63 | English string, visibility unknown | const pathname = url.pathname === '/' ? '/' : url.pathname.replace(/\/+$/, '') \|\| '/' |
| tui | ui-tui\src\lib\externalLink.ts | 65 | English string, visibility unknown | return `${host}${pathname}${url.search \|\| ''}` |
| tui | ui-tui\src\lib\externalLink.ts | 84 | English string, visibility unknown | const path = url.pathname && url.pathname !== '/' ? url.pathname.replace(/\/$/, '') : '' |
| tui | ui-tui\src\lib\externalLink.ts | 86 | English string, visibility unknown | return `${host}${path}` |
| tui | ui-tui\src\lib\externalLink.ts | 182 | English string, visibility unknown | if (normalized === '::' \|\| normalized === '::1') { |
| tui | ui-tui\src\lib\externalLink.ts | 186 | English string, visibility unknown | if (normalized.startsWith('fc') \|\| normalized.startsWith('fd')) { |
| tui | ui-tui\src\lib\externalLink.ts | 190 | English string, visibility unknown | if (normalized.startsWith('fe8') \|\| normalized.startsWith('fe9') \|\| normalized.startsWith('fea') \|\| normalized.startsWith('feb')) { |
| tui | ui-tui\src\lib\externalLink.ts | 194 | English string, visibility unknown | if (normalized.startsWith('::ffff:')) { |
| tui | ui-tui\src\lib\externalLink.ts | 195 | English string, visibility unknown | return isPrivateIpv4(normalized.slice('::ffff:'.length)) |
| tui | ui-tui\src\lib\externalLink.ts | 202 | English string, visibility unknown | const withoutBrackets = value.replace(/^\[/, '').replace(/\]$/, '') |
| tui | ui-tui\src\lib\externalLink.ts | 257 | English string, visibility unknown | return raw ? decodeHtmlEntities(raw).replace(/\s+/g, ' ').trim() : '' |
| tui | ui-tui\src\lib\externalLink.ts | 337 | English string, visibility unknown | Accept: 'text/html,application/xhtml+xml;q=0.9,*/*;q=0.5', |
| tui | ui-tui\src\lib\externalLink.ts | 338 | English string, visibility unknown | 'Accept-Language': 'en-US,en;q=0.7', |
| tui | ui-tui\src\lib\forceTruecolor.ts | 28 | English string, visibility unknown | return colorTerm === 'truecolor' \|\| colorTerm === '24bit' \|\| forceColor === '3' |
| tui | ui-tui\src\lib\fpsStore.ts | 8 | English string, visibility unknown | import { atom } from 'nanostores' |
| tui | ui-tui\src\lib\gracefulExit.ts | 4 | English string, visibility unknown | onError?: (scope: 'uncaughtException' \| 'unhandledRejection', err: unknown) => void |
| tui | ui-tui\src\lib\gracefulExit.ts | 45 | English string, visibility unknown | process.on('uncaughtException', err => onError?.('uncaughtException', err)) |
| tui | ui-tui\src\lib\gracefulExit.ts | 46 | English string, visibility unknown | process.on('unhandledRejection', reason => onError?.('unhandledRejection', reason)) |
| tui | ui-tui\src\lib\history.ts | 1 | English string, visibility unknown | import { appendFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs' |
| tui | ui-tui\src\lib\history.ts | 2 | English string, visibility unknown | import { homedir } from 'node:os' |
| tui | ui-tui\src\lib\history.ts | 3 | English string, visibility unknown | import { join } from 'node:path' |
| tui | ui-tui\src\lib\history.ts | 7 | English string, visibility unknown | const file = join(dir, '.hermes_history') |
| tui | ui-tui\src\lib\history.ts | 26 | English string, visibility unknown | for (const line of readFileSync(file, 'utf8').split('\n')) { |
| tui | ui-tui\src\lib\history.ts | 71 | English string, visibility unknown | const ts = new Date().toISOString().replace('T', ' ').replace('Z', '') |
| tui | ui-tui\src\lib\history.ts | 78 | English string, visibility unknown | appendFileSync(file, `\n# ${ts}\n${encoded}\n`) |
| tui | ui-tui\src\lib\inputMetrics.ts | 1 | English string, visibility unknown | import { stringWidth, wrapAnsi } from '@hermes/ink' |
| tui | ui-tui\src\lib\inputMetrics.ts | 3 | English string, visibility unknown | import type { Role } from '../types.js' |
| tui | ui-tui\src\lib\inputMetrics.ts | 8 | English string, visibility unknown | const seg = () => (_seg ??= new Intl.Segmenter(undefined, { granularity: 'grapheme' })) |
| tui | ui-tui\src\lib\inputMetrics.ts | 31 | English string, visibility unknown | // composer's TextInput renders text via Ink's <Text wrap="wrap">, which |
| tui | ui-tui\src\lib\inputMetrics.ts | 52 | English string, visibility unknown | // literal '\n' from the input. Either way the next char in `wrapped` |
| tui | ui-tui\src\lib\inputMetrics.ts | 54 | English string, visibility unknown | // consume it (it doesn't appear in either line). Otherwise the '\n' |
| tui | ui-tui\src\lib\inputMetrics.ts | 67 | English string, visibility unknown | // Defensive sync check. wrap-ansi (with `hard: true, trim: false`, no |
| tui | ui-tui\src\lib\inputMetrics.ts | 70 | English string, visibility unknown | // options `wrapped[i]` should always equal `value[originalIdx]`. But |
| tui | ui-tui\src\lib\inputMetrics.ts | 73 | English string, visibility unknown | // they do, we'd slide `originalIdx` past the end of `value` and emit |
| tui | ui-tui\src\lib\inputMetrics.ts | 116 | English string, visibility unknown | * lays the value out (which uses `wrap-ansi`). Any divergence parks the |
| tui | ui-tui\src\lib\inputMetrics.ts | 118 | English string, visibility unknown | * "cursor drift past blank cells" bug. `visualLines` is sourced directly |
| tui | ui-tui\src\lib\inputMetrics.ts | 139 | English string, visibility unknown | // `column >= w` (the "trailing cursor-cell overflows" rule). With |
| tui | ui-tui\src\lib\inputMetrics.ts | 140 | English string, visibility unknown | // `visualLines` sourcing breaks from wrap-ansi, the line wrapping |
| tui | ui-tui\src\lib\inputMetrics.ts | 143 | English string, visibility unknown | // drift we're fixing, so we don't. |
| tui | ui-tui\src\lib\inputMetrics.ts | 177 | English string, visibility unknown | return role === 'user' ? composerPromptWidth(userPrompt) : 3 |
| tui | ui-tui\src\lib\liveProgress.ts | 1 | English string, visibility unknown | import type { Msg, TodoItem } from '../types.js' |
| tui | ui-tui\src\lib\liveProgress.ts | 4 | English string, visibility unknown | todos.filter(todo => todo.status === 'in_progress' \|\| todo.status === 'pending').length |
| tui | ui-tui\src\lib\liveProgress.ts | 7 | English string, visibility unknown | todos.length > 0 && todos.every(todo => todo.status === 'completed' \|\| todo.status === 'cancelled') |
| tui | ui-tui\src\lib\liveProgress.ts | 10 | English string, visibility unknown | Boolean(msg?.kind === 'trail' && !msg.text && !msg.thinking?.trim() && msg.tools?.length) |
| tui | ui-tui\src\lib\liveProgress.ts | 13 | English string, visibility unknown | Boolean(msg?.kind === 'trail' && !msg.text && (msg.thinking?.trim() \|\| msg.tools?.length)) |
| tui | ui-tui\src\lib\liveProgress.ts | 26 | English string, visibility unknown | if (msg.kind === 'intro' \|\| msg.kind === 'panel' \|\| msg.kind === 'diff') { |
| tui | ui-tui\src\lib\liveProgress.ts | 30 | English string, visibility unknown | if (msg.role && msg.role !== 'system') { |
| tui | ui-tui\src\lib\liveProgress.ts | 41 | English string, visibility unknown | const isToolCarryingTrail = (msg: Msg \| undefined) => Boolean(msg?.kind === 'trail' && !msg.text && msg.tools?.length) |
| tui | ui-tui\src\lib\mathUnicode.ts | 5 | English string, visibility unknown | // sub/superscripts, and `\frac{a}{b}` collapsed to `a/b`. |
| tui | ui-tui\src\lib\mathUnicode.ts | 9 | English string, visibility unknown | // verbatim (so a `\foo{bar}` we've never heard of still survives). |
| tui | ui-tui\src\lib\mathUnicode.ts | 13 | English string, visibility unknown | // • Longest-match-first ordering on commands so `\le` doesn't shadow |
| tui | ui-tui\src\lib\mathUnicode.ts | 14 | English string, visibility unknown | // `\leq`, `\sub` doesn't shadow `\subseteq`, etc. |
| tui | ui-tui\src\lib\mathUnicode.ts | 16 | English string, visibility unknown | // `\pix` (made-up command) doesn't get partially substituted as `π`. |
| tui | ui-tui\src\lib\mathUnicode.ts | 17 | English string, visibility unknown | // • `\mathbb{X}`, `\mathcal{X}`, `\mathfrak{X}` only handle a single |
| tui | ui-tui\src\lib\mathUnicode.ts | 18 | English string, visibility unknown | // letter argument — multi-letter `\mathbb{NN}` is rare and would |
| tui | ui-tui\src\lib\mathUnicode.ts | 22 | English string, visibility unknown | // LaTeX so we don't emit `ⁿ+¹` (which has no `+` superscript glyph |
| tui | ui-tui\src\lib\mathUnicode.ts | 27 | English string, visibility unknown | '\\alpha': 'α', |
| tui | ui-tui\src\lib\mathUnicode.ts | 28 | English string, visibility unknown | '\\beta': 'β', |
| tui | ui-tui\src\lib\mathUnicode.ts | 29 | English string, visibility unknown | '\\gamma': 'γ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 30 | English string, visibility unknown | '\\delta': 'δ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 31 | English string, visibility unknown | '\\epsilon': 'ε', |
| tui | ui-tui\src\lib\mathUnicode.ts | 32 | English string, visibility unknown | '\\varepsilon': 'ε', |
| tui | ui-tui\src\lib\mathUnicode.ts | 33 | English string, visibility unknown | '\\zeta': 'ζ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 34 | English string, visibility unknown | '\\eta': 'η', |
| tui | ui-tui\src\lib\mathUnicode.ts | 35 | English string, visibility unknown | '\\theta': 'θ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 36 | English string, visibility unknown | '\\vartheta': 'ϑ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 37 | English string, visibility unknown | '\\iota': 'ι', |
| tui | ui-tui\src\lib\mathUnicode.ts | 38 | English string, visibility unknown | '\\kappa': 'κ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 39 | English string, visibility unknown | '\\lambda': 'λ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 44 | English string, visibility unknown | '\\varpi': 'ϖ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 45 | English string, visibility unknown | '\\rho': 'ρ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 46 | English string, visibility unknown | '\\varrho': 'ϱ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 47 | English string, visibility unknown | '\\sigma': 'σ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 48 | English string, visibility unknown | '\\varsigma': 'ς', |
| tui | ui-tui\src\lib\mathUnicode.ts | 49 | English string, visibility unknown | '\\tau': 'τ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 50 | English string, visibility unknown | '\\upsilon': 'υ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 51 | English string, visibility unknown | '\\phi': 'φ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 52 | English string, visibility unknown | '\\varphi': 'φ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 53 | English string, visibility unknown | '\\chi': 'χ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 54 | English string, visibility unknown | '\\psi': 'ψ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 55 | English string, visibility unknown | '\\omega': 'ω', |
| tui | ui-tui\src\lib\mathUnicode.ts | 58 | English string, visibility unknown | '\\Gamma': 'Γ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 59 | English string, visibility unknown | '\\Delta': 'Δ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 60 | English string, visibility unknown | '\\Theta': 'Θ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 61 | English string, visibility unknown | '\\Lambda': 'Λ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 64 | English string, visibility unknown | '\\Sigma': 'Σ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 65 | English string, visibility unknown | '\\Upsilon': 'Υ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 66 | English string, visibility unknown | '\\Phi': 'Φ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 67 | English string, visibility unknown | '\\Psi': 'Ψ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 68 | English string, visibility unknown | '\\Omega': 'Ω', |
| tui | ui-tui\src\lib\mathUnicode.ts | 71 | English string, visibility unknown | '\\sum': '∑', |
| tui | ui-tui\src\lib\mathUnicode.ts | 72 | English string, visibility unknown | '\\prod': '∏', |
| tui | ui-tui\src\lib\mathUnicode.ts | 73 | English string, visibility unknown | '\\coprod': '∐', |
| tui | ui-tui\src\lib\mathUnicode.ts | 74 | English string, visibility unknown | '\\int': '∫', |
| tui | ui-tui\src\lib\mathUnicode.ts | 75 | English string, visibility unknown | '\\iint': '∬', |
| tui | ui-tui\src\lib\mathUnicode.ts | 76 | English string, visibility unknown | '\\iiint': '∭', |
| tui | ui-tui\src\lib\mathUnicode.ts | 77 | English string, visibility unknown | '\\oint': '∮', |
| tui | ui-tui\src\lib\mathUnicode.ts | 78 | English string, visibility unknown | '\\bigcup': '⋃', |
| tui | ui-tui\src\lib\mathUnicode.ts | 79 | English string, visibility unknown | '\\bigcap': '⋂', |
| tui | ui-tui\src\lib\mathUnicode.ts | 80 | English string, visibility unknown | '\\bigvee': '⋁', |
| tui | ui-tui\src\lib\mathUnicode.ts | 81 | English string, visibility unknown | '\\bigwedge': '⋀', |
| tui | ui-tui\src\lib\mathUnicode.ts | 82 | English string, visibility unknown | '\\bigoplus': '⨁', |
| tui | ui-tui\src\lib\mathUnicode.ts | 83 | English string, visibility unknown | '\\bigotimes': '⨂', |
| tui | ui-tui\src\lib\mathUnicode.ts | 86 | English string, visibility unknown | '\\partial': '∂', |
| tui | ui-tui\src\lib\mathUnicode.ts | 87 | English string, visibility unknown | '\\nabla': '∇', |
| tui | ui-tui\src\lib\mathUnicode.ts | 88 | English string, visibility unknown | '\\sqrt': '√', |
| tui | ui-tui\src\lib\mathUnicode.ts | 91 | English string, visibility unknown | '\\emptyset': '∅', |
| tui | ui-tui\src\lib\mathUnicode.ts | 92 | English string, visibility unknown | '\\varnothing': '∅', |
| tui | ui-tui\src\lib\mathUnicode.ts | 93 | English string, visibility unknown | '\\infty': '∞', |
| tui | ui-tui\src\lib\mathUnicode.ts | 95 | English string, visibility unknown | '\\notin': '∉', |
| tui | ui-tui\src\lib\mathUnicode.ts | 97 | English string, visibility unknown | '\\subset': '⊂', |
| tui | ui-tui\src\lib\mathUnicode.ts | 98 | English string, visibility unknown | '\\supset': '⊃', |
| tui | ui-tui\src\lib\mathUnicode.ts | 99 | English string, visibility unknown | '\\subseteq': '⊆', |
| tui | ui-tui\src\lib\mathUnicode.ts | 100 | English string, visibility unknown | '\\supseteq': '⊇', |
| tui | ui-tui\src\lib\mathUnicode.ts | 101 | English string, visibility unknown | '\\subsetneq': '⊊', |
| tui | ui-tui\src\lib\mathUnicode.ts | 102 | English string, visibility unknown | '\\supsetneq': '⊋', |
| tui | ui-tui\src\lib\mathUnicode.ts | 103 | English string, visibility unknown | '\\cup': '∪', |
| tui | ui-tui\src\lib\mathUnicode.ts | 104 | English string, visibility unknown | '\\cap': '∩', |
| tui | ui-tui\src\lib\mathUnicode.ts | 105 | English string, visibility unknown | '\\setminus': '∖', |
| tui | ui-tui\src\lib\mathUnicode.ts | 106 | English string, visibility unknown | '\\complement': '∁', |
| tui | ui-tui\src\lib\mathUnicode.ts | 109 | English string, visibility unknown | '\\forall': '∀', |
| tui | ui-tui\src\lib\mathUnicode.ts | 110 | English string, visibility unknown | '\\exists': '∃', |
| tui | ui-tui\src\lib\mathUnicode.ts | 111 | English string, visibility unknown | '\\nexists': '∄', |
| tui | ui-tui\src\lib\mathUnicode.ts | 112 | English string, visibility unknown | '\\land': '∧', |
| tui | ui-tui\src\lib\mathUnicode.ts | 113 | English string, visibility unknown | '\\lor': '∨', |
| tui | ui-tui\src\lib\mathUnicode.ts | 114 | English string, visibility unknown | '\\lnot': '¬', |
| tui | ui-tui\src\lib\mathUnicode.ts | 115 | English string, visibility unknown | '\\neg': '¬', |
| tui | ui-tui\src\lib\mathUnicode.ts | 116 | English string, visibility unknown | '\\therefore': '∴', |
| tui | ui-tui\src\lib\mathUnicode.ts | 117 | English string, visibility unknown | '\\because': '∵', |
| tui | ui-tui\src\lib\mathUnicode.ts | 121 | English string, visibility unknown | '\\leq': '≤', |
| tui | ui-tui\src\lib\mathUnicode.ts | 123 | English string, visibility unknown | '\\geq': '≥', |
| tui | ui-tui\src\lib\mathUnicode.ts | 125 | English string, visibility unknown | '\\neq': '≠', |
| tui | ui-tui\src\lib\mathUnicode.ts | 128 | English string, visibility unknown | '\\approx': '≈', |
| tui | ui-tui\src\lib\mathUnicode.ts | 129 | English string, visibility unknown | '\\equiv': '≡', |
| tui | ui-tui\src\lib\mathUnicode.ts | 130 | English string, visibility unknown | '\\cong': '≅', |
| tui | ui-tui\src\lib\mathUnicode.ts | 131 | English string, visibility unknown | '\\sim': '∼', |
| tui | ui-tui\src\lib\mathUnicode.ts | 132 | English string, visibility unknown | '\\simeq': '≃', |
| tui | ui-tui\src\lib\mathUnicode.ts | 133 | English string, visibility unknown | '\\propto': '∝', |
| tui | ui-tui\src\lib\mathUnicode.ts | 134 | English string, visibility unknown | '\\perp': '⊥', |
| tui | ui-tui\src\lib\mathUnicode.ts | 135 | English string, visibility unknown | '\\parallel': '∥', |
| tui | ui-tui\src\lib\mathUnicode.ts | 136 | English string, visibility unknown | '\\models': '⊨', |
| tui | ui-tui\src\lib\mathUnicode.ts | 137 | English string, visibility unknown | '\\vdash': '⊢', |
| tui | ui-tui\src\lib\mathUnicode.ts | 138 | English string, visibility unknown | '\\mid': '∣', |
| tui | ui-tui\src\lib\mathUnicode.ts | 139 | English string, visibility unknown | '\\nmid': '∤', |
| tui | ui-tui\src\lib\mathUnicode.ts | 140 | English string, visibility unknown | '\\divides': '∣', |
| tui | ui-tui\src\lib\mathUnicode.ts | 143 | English string, visibility unknown | '\\blacksquare': '■', |
| tui | ui-tui\src\lib\mathUnicode.ts | 144 | English string, visibility unknown | '\\square': '□', |
| tui | ui-tui\src\lib\mathUnicode.ts | 145 | English string, visibility unknown | '\\Box': '□', |
| tui | ui-tui\src\lib\mathUnicode.ts | 146 | English string, visibility unknown | '\\qed': '∎', |
| tui | ui-tui\src\lib\mathUnicode.ts | 147 | English string, visibility unknown | '\\bigstar': '★', |
| tui | ui-tui\src\lib\mathUnicode.ts | 149 | English string, visibility unknown | // Modular arithmetic — the `\pmod{p}` form (with arg) is handled below; |
| tui | ui-tui\src\lib\mathUnicode.ts | 150 | English string, visibility unknown | // the bare `\bmod` / `\mod` commands are simple text substitutions. |
| tui | ui-tui\src\lib\mathUnicode.ts | 151 | English string, visibility unknown | '\\bmod': 'mod', |
| tui | ui-tui\src\lib\mathUnicode.ts | 152 | English string, visibility unknown | '\\mod': 'mod', |
| tui | ui-tui\src\lib\mathUnicode.ts | 154 | English string, visibility unknown | // Brackets / fences (named delimiter commands; the `\left\X` / `\right\X` |
| tui | ui-tui\src\lib\mathUnicode.ts | 156 | English string, visibility unknown | '\\langle': '⟨', |
| tui | ui-tui\src\lib\mathUnicode.ts | 157 | English string, visibility unknown | '\\rangle': '⟩', |
| tui | ui-tui\src\lib\mathUnicode.ts | 158 | English string, visibility unknown | '\\lceil': '⌈', |
| tui | ui-tui\src\lib\mathUnicode.ts | 159 | English string, visibility unknown | '\\rceil': '⌉', |
| tui | ui-tui\src\lib\mathUnicode.ts | 160 | English string, visibility unknown | '\\lfloor': '⌊', |
| tui | ui-tui\src\lib\mathUnicode.ts | 161 | English string, visibility unknown | '\\rfloor': '⌋', |
| tui | ui-tui\src\lib\mathUnicode.ts | 166 | English string, visibility unknown | '\\rightarrow': '→', |
| tui | ui-tui\src\lib\mathUnicode.ts | 167 | English string, visibility unknown | '\\leftarrow': '←', |
| tui | ui-tui\src\lib\mathUnicode.ts | 168 | English string, visibility unknown | '\\leftrightarrow': '↔', |
| tui | ui-tui\src\lib\mathUnicode.ts | 169 | English string, visibility unknown | '\\Rightarrow': '⇒', |
| tui | ui-tui\src\lib\mathUnicode.ts | 170 | English string, visibility unknown | '\\Leftarrow': '⇐', |
| tui | ui-tui\src\lib\mathUnicode.ts | 171 | English string, visibility unknown | '\\Leftrightarrow': '⇔', |
| tui | ui-tui\src\lib\mathUnicode.ts | 172 | English string, visibility unknown | '\\implies': '⟹', |
| tui | ui-tui\src\lib\mathUnicode.ts | 173 | English string, visibility unknown | '\\impliedby': '⟸', |
| tui | ui-tui\src\lib\mathUnicode.ts | 174 | English string, visibility unknown | '\\iff': '⟺', |
| tui | ui-tui\src\lib\mathUnicode.ts | 175 | English string, visibility unknown | '\\mapsto': '↦', |
| tui | ui-tui\src\lib\mathUnicode.ts | 176 | English string, visibility unknown | '\\hookrightarrow': '↪', |
| tui | ui-tui\src\lib\mathUnicode.ts | 177 | English string, visibility unknown | '\\hookleftarrow': '↩', |
| tui | ui-tui\src\lib\mathUnicode.ts | 178 | English string, visibility unknown | '\\uparrow': '↑', |
| tui | ui-tui\src\lib\mathUnicode.ts | 179 | English string, visibility unknown | '\\downarrow': '↓', |
| tui | ui-tui\src\lib\mathUnicode.ts | 180 | English string, visibility unknown | '\\updownarrow': '↕', |
| tui | ui-tui\src\lib\mathUnicode.ts | 183 | English string, visibility unknown | '\\cdot': '⋅', |
| tui | ui-tui\src\lib\mathUnicode.ts | 184 | English string, visibility unknown | '\\cdots': '⋯', |
| tui | ui-tui\src\lib\mathUnicode.ts | 185 | English string, visibility unknown | '\\ldots': '…', |
| tui | ui-tui\src\lib\mathUnicode.ts | 186 | English string, visibility unknown | '\\dots': '…', |
| tui | ui-tui\src\lib\mathUnicode.ts | 187 | English string, visibility unknown | '\\dotsb': '…', |
| tui | ui-tui\src\lib\mathUnicode.ts | 188 | English string, visibility unknown | '\\dotsc': '…', |
| tui | ui-tui\src\lib\mathUnicode.ts | 189 | English string, visibility unknown | '\\vdots': '⋮', |
| tui | ui-tui\src\lib\mathUnicode.ts | 190 | English string, visibility unknown | '\\ddots': '⋱', |
| tui | ui-tui\src\lib\mathUnicode.ts | 191 | English string, visibility unknown | '\\times': '×', |
| tui | ui-tui\src\lib\mathUnicode.ts | 192 | English string, visibility unknown | '\\div': '÷', |
| tui | ui-tui\src\lib\mathUnicode.ts | 195 | English string, visibility unknown | '\\circ': '∘', |
| tui | ui-tui\src\lib\mathUnicode.ts | 196 | English string, visibility unknown | '\\bullet': '•', |
| tui | ui-tui\src\lib\mathUnicode.ts | 197 | English string, visibility unknown | '\\star': '⋆', |
| tui | ui-tui\src\lib\mathUnicode.ts | 198 | English string, visibility unknown | '\\ast': '∗', |
| tui | ui-tui\src\lib\mathUnicode.ts | 199 | English string, visibility unknown | '\\oplus': '⊕', |
| tui | ui-tui\src\lib\mathUnicode.ts | 200 | English string, visibility unknown | '\\ominus': '⊖', |
| tui | ui-tui\src\lib\mathUnicode.ts | 201 | English string, visibility unknown | '\\otimes': '⊗', |
| tui | ui-tui\src\lib\mathUnicode.ts | 202 | English string, visibility unknown | '\\odot': '⊙', |
| tui | ui-tui\src\lib\mathUnicode.ts | 203 | English string, visibility unknown | '\\diamond': '⋄', |
| tui | ui-tui\src\lib\mathUnicode.ts | 204 | English string, visibility unknown | '\\angle': '∠', |
| tui | ui-tui\src\lib\mathUnicode.ts | 205 | English string, visibility unknown | '\\triangle': '△', |
| tui | ui-tui\src\lib\mathUnicode.ts | 213 | English string, visibility unknown | '\\quad': ' ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 214 | English string, visibility unknown | '\\qquad': ' ', |
| tui | ui-tui\src\lib\mathUnicode.ts | 217 | English string, visibility unknown | '\\sin': 'sin', |
| tui | ui-tui\src\lib\mathUnicode.ts | 218 | English string, visibility unknown | '\\cos': 'cos', |
| tui | ui-tui\src\lib\mathUnicode.ts | 219 | English string, visibility unknown | '\\tan': 'tan', |
| tui | ui-tui\src\lib\mathUnicode.ts | 220 | English string, visibility unknown | '\\cot': 'cot', |
| tui | ui-tui\src\lib\mathUnicode.ts | 221 | English string, visibility unknown | '\\sec': 'sec', |
| tui | ui-tui\src\lib\mathUnicode.ts | 222 | English string, visibility unknown | '\\csc': 'csc', |
| tui | ui-tui\src\lib\mathUnicode.ts | 223 | English string, visibility unknown | '\\arcsin': 'arcsin', |
| tui | ui-tui\src\lib\mathUnicode.ts | 224 | English string, visibility unknown | '\\arccos': 'arccos', |
| tui | ui-tui\src\lib\mathUnicode.ts | 225 | English string, visibility unknown | '\\arctan': 'arctan', |
| tui | ui-tui\src\lib\mathUnicode.ts | 226 | English string, visibility unknown | '\\sinh': 'sinh', |
| tui | ui-tui\src\lib\mathUnicode.ts | 227 | English string, visibility unknown | '\\cosh': 'cosh', |
| tui | ui-tui\src\lib\mathUnicode.ts | 228 | English string, visibility unknown | '\\tanh': 'tanh', |
| tui | ui-tui\src\lib\mathUnicode.ts | 229 | English string, visibility unknown | '\\log': 'log', |
| tui | ui-tui\src\lib\mathUnicode.ts | 231 | English string, visibility unknown | '\\exp': 'exp', |
| tui | ui-tui\src\lib\mathUnicode.ts | 232 | English string, visibility unknown | '\\det': 'det', |
| tui | ui-tui\src\lib\mathUnicode.ts | 233 | English string, visibility unknown | '\\dim': 'dim', |
| tui | ui-tui\src\lib\mathUnicode.ts | 234 | English string, visibility unknown | '\\ker': 'ker', |
| tui | ui-tui\src\lib\mathUnicode.ts | 235 | English string, visibility unknown | '\\lim': 'lim', |
| tui | ui-tui\src\lib\mathUnicode.ts | 236 | English string, visibility unknown | '\\liminf': 'liminf', |
| tui | ui-tui\src\lib\mathUnicode.ts | 237 | English string, visibility unknown | '\\limsup': 'limsup', |
| tui | ui-tui\src\lib\mathUnicode.ts | 238 | English string, visibility unknown | '\\sup': 'sup', |
| tui | ui-tui\src\lib\mathUnicode.ts | 239 | English string, visibility unknown | '\\inf': 'inf', |
| tui | ui-tui\src\lib\mathUnicode.ts | 240 | English string, visibility unknown | '\\max': 'max', |
| tui | ui-tui\src\lib\mathUnicode.ts | 241 | English string, visibility unknown | '\\min': 'min', |
| tui | ui-tui\src\lib\mathUnicode.ts | 242 | English string, visibility unknown | '\\arg': 'arg', |
| tui | ui-tui\src\lib\mathUnicode.ts | 243 | English string, visibility unknown | '\\gcd': 'gcd', |
| tui | ui-tui\src\lib\mathUnicode.ts | 420 | English string, visibility unknown | // Sentinel control characters used to mark `\boxed` / `\fbox` regions in |
| tui | ui-tui\src\lib\mathUnicode.ts | 431 | English string, visibility unknown | // `\sum`) which need a `(?![A-Za-z])` lookahead so they don't partially |
| tui | ui-tui\src\lib\mathUnicode.ts | 432 | English string, visibility unknown | // match `\pix` or `\summa`, and one for punctuation-ending commands |
| tui | ui-tui\src\lib\mathUnicode.ts | 434 | English string, visibility unknown | // `\{p` would refuse to substitute because `p` is a letter. |
| tui | ui-tui\src\lib\mathUnicode.ts | 436 | English string, visibility unknown | // Longest commands first inside each group so `\leq` beats `\le`. |
| tui | ui-tui\src\lib\mathUnicode.ts | 485 | English string, visibility unknown | // far better than `^{∞}` in a terminal. Multi-char bodies that don't |
| tui | ui-tui\src\lib\mathUnicode.ts | 486 | English string, visibility unknown | // fully convert use parens (`e^(iπ)`) instead of braces (`e^{iπ}`) |
| tui | ui-tui\src\lib\mathUnicode.ts | 492 | English string, visibility unknown | return `${sigil}${trimmed}` |
| tui | ui-tui\src\lib\mathUnicode.ts | 495 | English string, visibility unknown | return `${sigil}(${trimmed})` |
| tui | ui-tui\src\lib\mathUnicode.ts | 499 | English string, visibility unknown | // `\{[^{}]*\}` regex this survives `\frac{\|t\|^{p-1}\|P(t)\|^p}{...}` where |
| tui | ui-tui\src\lib\mathUnicode.ts | 502 | English string, visibility unknown | // closing `}`. Returns null if there is no balanced brace at `start`. |
| tui | ui-tui\src\lib\mathUnicode.ts | 514 | English string, visibility unknown | // Skip escapes — `\{` and `\}` inside a body are literal braces and |
| tui | ui-tui\src\lib\mathUnicode.ts | 539 | English string, visibility unknown | // Replace every occurrence of `\command{arg}` using balanced-brace parsing |
| tui | ui-tui\src\lib\mathUnicode.ts | 540 | English string, visibility unknown | // (so `\boxed{x^{n+1}}` works where a `[^{}]*` regex would fail). The |
| tui | ui-tui\src\lib\mathUnicode.ts | 541 | English string, visibility unknown | // `render` callback receives the inner content already recursed-into, so |
| tui | ui-tui\src\lib\mathUnicode.ts | 542 | English string, visibility unknown | // `\boxed{\boxed{x}}` resolves outside-in cleanly. Unmatched `\command` |
| tui | ui-tui\src\lib\mathUnicode.ts | 570 | English string, visibility unknown | while (input[p] === ' ' \|\| input[p] === '\t') p++ |
| tui | ui-tui\src\lib\mathUnicode.ts | 587 | English string, visibility unknown | // Replace every `\frac{num}{den}` with `num/den` (parens around either |
| tui | ui-tui\src\lib\mathUnicode.ts | 589 | English string, visibility unknown | // fractions naturally: `\frac{1}{\frac{1}{x}}` collapses to `1/(1/x)` |
| tui | ui-tui\src\lib\mathUnicode.ts | 590 | English string, visibility unknown | // because we recurse into `den` before deciding whether to parenthesise. |
| tui | ui-tui\src\lib\mathUnicode.ts | 596 | English string, visibility unknown | const idx = input.indexOf('\\frac', i) |
| tui | ui-tui\src\lib\mathUnicode.ts | 606 | English string, visibility unknown | // `(?![A-Za-z])` — protect hypothetical commands like `\fraction`. |
| tui | ui-tui\src\lib\mathUnicode.ts | 617 | English string, visibility unknown | while (input[p] === ' ' \|\| input[p] === '\t') p++ |
| tui | ui-tui\src\lib\mathUnicode.ts | 629 | English string, visibility unknown | while (input[p] === ' ' \|\| input[p] === '\t') p++ |
| tui | ui-tui\src\lib\mathUnicode.ts | 639 | English string, visibility unknown | out += `${wrapForFrac(replaceFracs(num.content))}/${wrapForFrac(replaceFracs(den.content))}` |
| tui | ui-tui\src\lib\mathUnicode.ts | 646 | English string, visibility unknown | // Wrap multi-token expressions in parens so `\frac{a+b}{c}` becomes |
| tui | ui-tui\src\lib\mathUnicode.ts | 647 | English string, visibility unknown | // `(a+b)/c` rather than `a+b/c`. We wrap whenever inline `/` would |
| tui | ui-tui\src\lib\mathUnicode.ts | 648 | English string, visibility unknown | // change the meaning — that's any binary operator (`+`, `-`, `*`, `/`) |
| tui | ui-tui\src\lib\mathUnicode.ts | 649 | English string, visibility unknown | // or whitespace separating tokens. `*` and `/` matter because nested |
| tui | ui-tui\src\lib\mathUnicode.ts | 650 | English string, visibility unknown | // fractions and products like `\frac{a*b}{c}` and `\frac{1/x}{y}` would |
| tui | ui-tui\src\lib\mathUnicode.ts | 651 | English string, visibility unknown | // otherwise read as `a*b/c` (right-associative ambiguity) and `1/x/y`. |
| tui | ui-tui\src\lib\mathUnicode.ts | 652 | English string, visibility unknown | // Atomic factors like `n!`, `x^2`, `\sin x` don't trigger any of these |
| tui | ui-tui\src\lib\mathUnicode.ts | 666 | English string, visibility unknown | return `(${trimmed})` |
| tui | ui-tui\src\lib\mathUnicode.ts | 694 | English string, visibility unknown | // `\boxed{X}` / `\fbox{X}` highlight a final answer. Terminals can't |
| tui | ui-tui\src\lib\mathUnicode.ts | 698 | English string, visibility unknown | // video) to the bracketed region. This keeps `texToUnicode` pure-string |
| tui | ui-tui\src\lib\mathUnicode.ts | 705 | English string, visibility unknown | // `\xrightarrow{label}` / `\xleftarrow{label}` collapse to an arrow with |
| tui | ui-tui\src\lib\mathUnicode.ts | 707 | English string, visibility unknown | // we put it adjacent — `─label→` is the closest readable approximation. |
| tui | ui-tui\src\lib\mathUnicode.ts | 710 | English string, visibility unknown | s = s.replace(/\\xrightarrow\s*\{([^{}]*)\}/g, (_, label: string) => `─${label.trim()}→`) |
| tui | ui-tui\src\lib\mathUnicode.ts | 711 | English string, visibility unknown | s = s.replace(/\\xleftarrow\s*\{([^{}]*)\}/g, (_, label: string) => `←${label.trim()}─`) |
| tui | ui-tui\src\lib\mathUnicode.ts | 716 | English string, visibility unknown | // `\pmod{p}` → ` (mod p)` (LaTeX adds parens automatically); `\pod{p}` |
| tui | ui-tui\src\lib\mathUnicode.ts | 717 | English string, visibility unknown | // is a paren-less variant; `\tag{n}` is the equation-number annotation |
| tui | ui-tui\src\lib\mathUnicode.ts | 720 | English string, visibility unknown | // already in the source so we don't end up with `b (mod p)` (double |
| tui | ui-tui\src\lib\mathUnicode.ts | 721 | English string, visibility unknown | // space) when the user wrote `b \pmod{p}`. |
| tui | ui-tui\src\lib\mathUnicode.ts | 722 | English string, visibility unknown | s = s.replace(/\s*\\pmod\s*\{([^{}]*)\}/g, (_, p: string) => ` (mod ${p.trim()})`) |
| tui | ui-tui\src\lib\mathUnicode.ts | 723 | English string, visibility unknown | s = s.replace(/\s*\\pod\s*\{([^{}]*)\}/g, (_, p: string) => ` (${p.trim()})`) |
| tui | ui-tui\src\lib\mathUnicode.ts | 724 | English string, visibility unknown | s = s.replace(/\s*\\tag\s*\{([^{}]*)\}/g, (_, n: string) => ` (${n.trim()})`) |
| tui | ui-tui\src\lib\mathUnicode.ts | 726 | English string, visibility unknown | // `\big`, `\Big`, `\bigg`, `\Bigg` (with optional `l`/`r`/`m` suffix) |
| tui | ui-tui\src\lib\mathUnicode.ts | 727 | English string, visibility unknown | // are sizing wrappers analogous to `\left`/`\right` but without the |
| tui | ui-tui\src\lib\mathUnicode.ts | 729 | English string, visibility unknown | // follows. The trailing `(?![A-Za-z])` protects `\bigtriangleup` and |
| tui | ui-tui\src\lib\mathUnicode.ts | 737 | English string, visibility unknown | // `\displaystyle` in the output. |
| tui | ui-tui\src\lib\mathUnicode.ts | 740 | English string, visibility unknown | // `\left` and `\right` are sizing wrappers around any delimiter — bare |
| tui | ui-tui\src\lib\mathUnicode.ts | 741 | English string, visibility unknown | // (`\left(`), escaped (`\left\{`), or named (`\left\langle`). Strip the |
| tui | ui-tui\src\lib\mathUnicode.ts | 744 | English string, visibility unknown | // `.?` consumes `\left.` / `\right.` which mean "no delimiter". |
| tui | ui-tui\src\lib\mathUnicode.ts | 745 | English string, visibility unknown | // Lookahead `(?![A-Za-z])` keeps `\leftarrow` / `\leftrightarrow` safe. |
| tui | ui-tui\src\lib\mathUnicode.ts | 751 | English string, visibility unknown | // superscript (it can't — Unicode lacks one) or fall back to `^∞` |
| tui | ui-tui\src\lib\mathUnicode.ts | 755 | English string, visibility unknown | // is "open-brace then p"), so the letter pass's `(?![A-Za-z])` rule |
| tui | ui-tui\src\lib\mathUnicode.ts | 762 | English string, visibility unknown | // emit `(...)` and we don't want a second pass to greedily convert |
| tui | ui-tui\src\lib\memory.ts | 1 | English string, visibility unknown | import { createWriteStream } from 'node:fs' |
| tui | ui-tui\src\lib\memory.ts | 2 | English string, visibility unknown | import { mkdir, readdir, readFile, writeFile } from 'node:fs/promises' |
| tui | ui-tui\src\lib\memory.ts | 3 | English string, visibility unknown | import { homedir, tmpdir } from 'node:os' |
| tui | ui-tui\src\lib\memory.ts | 4 | English string, visibility unknown | import { join } from 'node:path' |
| tui | ui-tui\src\lib\memory.ts | 5 | English string, visibility unknown | import { pipeline } from 'node:stream/promises' |
| tui | ui-tui\src\lib\memory.ts | 6 | English string, visibility unknown | import { getHeapSnapshot, getHeapSpaceStatistics, getHeapStatistics } from 'node:v8' |
| tui | ui-tui\src\lib\memory.ts | 8 | English string, visibility unknown | export type MemoryTrigger = 'auto-critical' \| 'auto-high' \| 'manual' |
| tui | ui-tui\src\lib\memory.ts | 79 | English string, visibility unknown | const openFileDescriptors = await swallow(async () => (await readdir('/proc/self/fd')).length) |
| tui | ui-tui\src\lib\memory.ts | 80 | English string, visibility unknown | const smapsRollup = await swallow(() => readFile('/proc/self/smaps_rollup', 'utf8')) |
| tui | ui-tui\src\lib\memory.ts | 84 | English string, visibility unknown | // average of rss/uptime, which would report phantom "growth" for a stable process. |
| tui | ui-tui\src\lib\memory.ts | 91 | English string, visibility unknown | `${heapStats.number_of_detached_contexts} detached context(s) — possible component/closure leak`, |
| tui | ui-tui\src\lib\memory.ts | 92 | English string, visibility unknown | activeHandles > 100 && `${activeHandles} active handles — possible timer/socket leak`, |
| tui | ui-tui\src\lib\memory.ts | 93 | English string, visibility unknown | nativeMemory > usage.heapUsed && 'Native memory > heap — leak may be in native addons', |
| tui | ui-tui\src\lib\memory.ts | 94 | English string, visibility unknown | mbPerHour > 100 && `High memory growth rate: ${mbPerHour.toFixed(1)} MB/hour`, |
| tui | ui-tui\src\lib\memory.ts | 95 | English string, visibility unknown | openFileDescriptors && openFileDescriptors > 500 && `${openFileDescriptors} open FDs — possible file/socket leak` |
| tui | ui-tui\src\lib\memory.ts | 96 | English string, visibility unknown | ].filter((s): s is string => typeof s === 'string') |
| tui | ui-tui\src\lib\memory.ts | 105 | English string, visibility unknown | : 'No obvious leak indicators. Inspect heap snapshot for retained objects.' |
| tui | ui-tui\src\lib\memory.ts | 143 | English string, visibility unknown | export async function performHeapDump(trigger: MemoryTrigger = 'manual'): Promise<HeapDumpResult> { |
| tui | ui-tui\src\lib\memory.ts | 152 | English string, visibility unknown | const base = `hermes-${new Date().toISOString().replace(/[:.]/g, '-')}-${process.pid}-${trigger}` |
| tui | ui-tui\src\lib\memory.ts | 153 | English string, visibility unknown | const heapPath = join(dir, `${base}.heapsnapshot`) |
| tui | ui-tui\src\lib\memory.ts | 154 | English string, visibility unknown | const diagPath = join(dir, `${base}.diagnostics.json`) |
| tui | ui-tui\src\lib\memoryMonitor.ts | 1 | English string, visibility unknown | import { type HeapDumpResult, performHeapDump } from './memory.js' |
| tui | ui-tui\src\lib\memoryMonitor.ts | 3 | English string, visibility unknown | export type MemoryLevel = 'critical' \| 'high' \| 'normal' |
| tui | ui-tui\src\lib\memoryMonitor.ts | 21 | English string, visibility unknown | // Deferred @hermes/ink import: loading `@hermes/ink` at module top-level |
| tui | ui-tui\src\lib\memoryMonitor.ts | 25 | English string, visibility unknown | // cold `hermes --tui` launch. |
| tui | ui-tui\src\lib\memoryMonitor.ts | 27 | English string, visibility unknown | // evictInkCaches only runs inside `tick()`, which fires on a 10s timer and |
| tui | ui-tui\src\lib\memoryMonitor.ts | 33 | English string, visibility unknown | let _evictInkCaches: ((level: 'all' \| 'half') => unknown) \| null = null |
| tui | ui-tui\src\lib\memoryMonitor.ts | 34 | English string, visibility unknown | let _evictInkCachesPromise: Promise<(level: 'all' \| 'half') => unknown> \| null = null |
| tui | ui-tui\src\lib\memoryMonitor.ts | 36 | English string, visibility unknown | async function _ensureEvictInkCaches(): Promise<(level: 'all' \| 'half') => unknown> { |
| tui | ui-tui\src\lib\memoryMonitor.ts | 41 | English string, visibility unknown | _evictInkCachesPromise ??= import('@hermes/ink') |
| tui | ui-tui\src\lib\memoryMonitor.ts | 43 | English string, visibility unknown | _evictInkCaches = mod.evictInkCaches as (level: 'all' \| 'half') => unknown |
| tui | ui-tui\src\lib\memoryMonitor.ts | 62 | English string, visibility unknown | const dumped = new Set<Exclude<MemoryLevel, 'normal'>>() |
| tui | ui-tui\src\lib\memoryMonitor.ts | 63 | English string, visibility unknown | const inFlight = new Set<Exclude<MemoryLevel, 'normal'>>() |
| tui | ui-tui\src\lib\memoryMonitor.ts | 67 | English string, visibility unknown | const level: MemoryLevel = heapUsed >= criticalBytes ? 'critical' : heapUsed >= highBytes ? 'high' : 'normal' |
| tui | ui-tui\src\lib\memoryMonitor.ts | 69 | English string, visibility unknown | if (level === 'normal') { |
| tui | ui-tui\src\lib\memoryMonitor.ts | 80 | English string, visibility unknown | // Prune Ink content caches before dump/exit — half on 'high' (recoverable), |
| tui | ui-tui\src\lib\memoryMonitor.ts | 82 | English string, visibility unknown | // Deferred import keeps `@hermes/ink` off the cold-start critical path; |
| tui | ui-tui\src\lib\memoryMonitor.ts | 88 | English string, visibility unknown | evictInkCaches(level === 'critical' ? 'all' : 'half') |
| tui | ui-tui\src\lib\memoryMonitor.ts | 95 | English string, visibility unknown | const dump = await performHeapDump(level === 'critical' ? 'auto-critical' : 'auto-high').catch(() => null) |
| tui | ui-tui\src\lib\memoryMonitor.ts | 98 | English string, visibility unknown | ;(level === 'critical' ? onCritical : onHigh)?.(snap, dump) |
| tui | ui-tui\src\lib\messages.ts | 1 | English string, visibility unknown | import type { Msg, Role } from '../types.js' |
| tui | ui-tui\src\lib\messages.ts | 3 | English string, visibility unknown | import { appendToolShelfMessage } from './liveProgress.js' |
| tui | ui-tui\src\lib\openExternalUrl.ts | 1 | English string, visibility unknown | import { spawn, type SpawnOptions } from 'node:child_process' |
| tui | ui-tui\src\lib\openExternalUrl.ts | 2 | English string, visibility unknown | import { platform } from 'node:os' |
| tui | ui-tui\src\lib\openExternalUrl.ts | 7 | English string, visibility unknown | * Wired into the Ink instance via `onHyperlinkClick` in entry.tsx, so any |
| tui | ui-tui\src\lib\openExternalUrl.ts | 15 | English string, visibility unknown | * - http(s) only. Anything else (`file:`, `data:`, `javascript:`, etc.) is |
| tui | ui-tui\src\lib\openExternalUrl.ts | 23 | English string, visibility unknown | * Returns `true` if the spawn was attempted, `false` if the open could |
| tui | ui-tui\src\lib\openExternalUrl.ts | 26 | English string, visibility unknown | * (`openCommand` returned null), or (c) `spawn()` threw synchronously |
| tui | ui-tui\src\lib\openExternalUrl.ts | 27 | English string, visibility unknown | * before the child was created. Async failures after spawn (`'error'` |
| tui | ui-tui\src\lib\openExternalUrl.ts | 28 | English string, visibility unknown | * event because the binary couldn't exec) still return `true` because |
| tui | ui-tui\src\lib\openExternalUrl.ts | 53 | English string, visibility unknown | // Without `ignore` here, Chrome's stderr can land in the alt screen. |
| tui | ui-tui\src\lib\openExternalUrl.ts | 61 | English string, visibility unknown | // later as an 'error' event. Without a handler, an unhandled 'error' |
| tui | ui-tui\src\lib\openExternalUrl.ts | 64 | English string, visibility unknown | // consumer; we already returned `true` synchronously, so the user |
| tui | ui-tui\src\lib\openExternalUrl.ts | 67 | English string, visibility unknown | child.once('error', () => { |
| tui | ui-tui\src\lib\openExternalUrl.ts | 92 | English string, visibility unknown | if (!value \|\| typeof value !== 'string') { |
| tui | ui-tui\src\lib\openExternalUrl.ts | 107 | English string, visibility unknown | if (parsed.protocol !== 'http:' && parsed.protocol !== 'https:') { |
| tui | ui-tui\src\lib\openExternalUrl.ts | 113 | English string, visibility unknown | // to forward those to `open`. |
| tui | ui-tui\src\lib\openExternalUrl.ts | 124 | English string, visibility unknown | * Per-platform open command. We deliberately avoid `cmd.exe /c start` on |
| tui | ui-tui\src\lib\openExternalUrl.ts | 125 | English string, visibility unknown | * Windows even though it's the canonical example, because `start` is a cmd |
| tui | ui-tui\src\lib\openExternalUrl.ts | 129 | English string, visibility unknown | * allowlist's safety story and also breaks plain http(s) URLs with `&` in |
| tui | ui-tui\src\lib\openExternalUrl.ts | 130 | English string, visibility unknown | * query strings. `explorer.exe <url>` is the safe, non-shell alternative — |
| tui | ui-tui\src\lib\openExternalUrl.ts | 134 | English string, visibility unknown | * Returns null for platforms where we don't know a safe opener (e.g. `aix`, |
| tui | ui-tui\src\lib\openExternalUrl.ts | 135 | English string, visibility unknown | * `sunos`, `cygwin`). The caller's `if (!command) return false` path then |
| tui | ui-tui\src\lib\openExternalUrl.ts | 136 | English string, visibility unknown | * surfaces "no opener" instead of optimistically trying `xdg-open` on a |
| tui | ui-tui\src\lib\openExternalUrl.ts | 140 | English string, visibility unknown | if (platformId === 'darwin') { |
| tui | ui-tui\src\lib\openExternalUrl.ts | 141 | English string, visibility unknown | return { command: 'open', args: [] } |
| tui | ui-tui\src\lib\openExternalUrl.ts | 144 | English string, visibility unknown | if (platformId === 'win32') { |
| tui | ui-tui\src\lib\openExternalUrl.ts | 145 | English string, visibility unknown | return { command: 'explorer.exe', args: [] } |
| tui | ui-tui\src\lib\openExternalUrl.ts | 154 | English string, visibility unknown | return { command: 'xdg-open', args: [] } |
| tui | ui-tui\src\lib\osc52.ts | 7 | English string, visibility unknown | type OscResponse = { code: number; data: string; type: 'osc' } |
| tui | ui-tui\src\lib\osc52.ts | 40 | English string, visibility unknown | if ((selection !== 'c' && selection !== 'p') \|\| !payload \|\| payload === '?') { |
| tui | ui-tui\src\lib\osc52.ts | 45 | English string, visibility unknown | return Buffer.from(payload, 'base64').toString('utf8') |
| tui | ui-tui\src\lib\osc52.ts | 61 | English string, visibility unknown | return !!r && typeof r === 'object' && (r as OscResponse).type === 'osc' && (r as OscResponse).code === 52 |
| tui | ui-tui\src\lib\osc52.ts | 73 | English string, visibility unknown | process.stdout.write(`\x1b]52;c;${Buffer.from(s, 'utf8').toString('base64')}\x07`) |
| tui | ui-tui\src\lib\perfPane.tsx | 14 | English string, visibility unknown | import { appendFileSync, mkdirSync } from 'node:fs' |
| tui | ui-tui\src\lib\perfPane.tsx | 15 | English string, visibility unknown | import { homedir } from 'node:os' |
| tui | ui-tui\src\lib\perfPane.tsx | 16 | English string, visibility unknown | import { dirname, join } from 'node:path' |
| tui | ui-tui\src\lib\perfPane.tsx | 18 | English string, visibility unknown | import type { FrameEvent } from '@hermes/ink' |
| tui | ui-tui\src\lib\perfPane.tsx | 19 | English string, visibility unknown | import { scrollFastPathStats } from '@hermes/ink' |
| tui | ui-tui\src\lib\perfPane.tsx | 20 | English string, visibility unknown | import { Profiler, type ProfilerOnRenderCallback, type ReactNode } from 'react' |
| tui | ui-tui\src\lib\platform.ts | 3 | English string, visibility unknown | * On macOS the "action" modifier is Cmd. Modern terminals that support kitty |
| tui | ui-tui\src\lib\platform.ts | 4 | English string, visibility unknown | * keyboard protocol report Cmd as `key.super`; legacy terminals often surface it |
| tui | ui-tui\src\lib\platform.ts | 5 | English string, visibility unknown | * as `key.meta`. Some macOS terminals also translate Cmd+Left/Right/Backspace |
| tui | ui-tui\src\lib\platform.ts | 12 | English string, visibility unknown | export const isMac = process.platform === 'darwin' |
| tui | ui-tui\src\lib\platform.ts | 19 | English string, visibility unknown | * Accept raw Ctrl+<letter> as an action shortcut on macOS, where `isActionMod` |
| tui | ui-tui\src\lib\platform.ts | 54 | English string, visibility unknown | * Voice recording toggle key — configurable via ``voice.record_key`` in |
| tui | ui-tui\src\lib\platform.ts | 55 | English string, visibility unknown | * ``config.yaml`` (default ``ctrl+b``). |
| tui | ui-tui\src\lib\platform.ts | 61 | English string, visibility unknown | * Only the documented default (``ctrl+b``) additionally accepts the |
| tui | ui-tui\src\lib\platform.ts | 62 | English string, visibility unknown | * macOS action modifier (Cmd+B) — custom bindings like ``ctrl+o`` |
| tui | ui-tui\src\lib\platform.ts | 65 | English string, visibility unknown | export type VoiceRecordKeyMod = 'alt' \| 'ctrl' \| 'super' |
| tui | ui-tui\src\lib\platform.ts | 68 | English string, visibility unknown | * prompt_toolkit binding shape (``c-space``, ``c-enter``, etc.) so a |
| tui | ui-tui\src\lib\platform.ts | 69 | English string, visibility unknown | * config value like ``ctrl+space`` binds in both runtimes. */ |
| tui | ui-tui\src\lib\platform.ts | 70 | English string, visibility unknown | export type VoiceRecordKeyNamed = 'backspace' \| 'delete' \| 'enter' \| 'escape' \| 'space' \| 'tab' |
| tui | ui-tui\src\lib\platform.ts | 73 | English string, visibility unknown | /** Single character (``'b'``, ``'o'``) when ``named`` is undefined, |
| tui | ui-tui\src\lib\platform.ts | 74 | English string, visibility unknown | * otherwise the named-key token (``'space'``, ``'enter'``…). Kept as |
| tui | ui-tui\src\lib\platform.ts | 75 | English string, visibility unknown | * one field for back-compat with the v1 ``{ ch, mod, raw }`` shape. */ |
| tui | ui-tui\src\lib\platform.ts | 85 | English string, visibility unknown | raw: 'ctrl+b' |
| tui | ui-tui\src\lib\platform.ts | 90 | English string, visibility unknown | * ``meta`` / ``cmd`` / ``command`` are intentionally absent. |
| tui | ui-tui\src\lib\platform.ts | 91 | English string, visibility unknown | * hermes-ink sets ``key.meta`` for plain Alt/Option on every platform |
| tui | ui-tui\src\lib\platform.ts | 95 | English string, visibility unknown | * ``cmd+b`` would render as ``Cmd+B`` but silently fire on Alt+B, or |
| tui | ui-tui\src\lib\platform.ts | 99 | English string, visibility unknown | * the platform action modifier ``super`` / ``win``, which match the |
| tui | ui-tui\src\lib\platform.ts | 100 | English string, visibility unknown | * unambiguous ``key.super`` bit. macOS users on Terminal.app stick |
| tui | ui-tui\src\lib\platform.ts | 101 | English string, visibility unknown | * with the documented ``ctrl+b``. |
| tui | ui-tui\src\lib\platform.ts | 103 | English string, visibility unknown | * Cross-runtime parity: the ``ctrl`` / ``control`` / ``alt`` / ``option`` / |
| tui | ui-tui\src\lib\platform.ts | 105 | English string, visibility unknown | * (``hermes_cli/voice.py::normalize_voice_record_key_for_prompt_toolkit``) |
| tui | ui-tui\src\lib\platform.ts | 106 | English string, visibility unknown | * so one ``voice.record_key`` value binds the same shortcut in both |
| tui | ui-tui\src\lib\platform.ts | 107 | English string, visibility unknown | * runtimes (Copilot round-9 review on #19835). The ``super`` / |
| tui | ui-tui\src\lib\platform.ts | 124 | English string, visibility unknown | * Aliases mirror what prompt_toolkit accepts (``return`` ↔ ``enter``, |
| tui | ui-tui\src\lib\platform.ts | 142 | English string, visibility unknown | /** ``useInputHandlers()`` intercepts these unconditionally before the |
| tui | ui-tui\src\lib\platform.ts | 143 | English string, visibility unknown | * voice check runs, so a binding like ``ctrl+c`` (interrupt), |
| tui | ui-tui\src\lib\platform.ts | 144 | English string, visibility unknown | * ``ctrl+d`` (quit), or ``ctrl+l`` (clear screen) would be advertised |
| tui | ui-tui\src\lib\platform.ts | 150 | English string, visibility unknown | * queue-edit (``queueEditIdx !== null``), so the voice binding works |
| tui | ui-tui\src\lib\platform.ts | 156 | English string, visibility unknown | * ``isCopyShortcut`` / ``isAction`` in ``useInputHandlers()``: |
| tui | ui-tui\src\lib\platform.ts | 167 | English string, visibility unknown | /** On macOS ``isActionMod`` accepts ``key.meta`` as the action |
| tui | ui-tui\src\lib\platform.ts | 168 | English string, visibility unknown | * modifier — but hermes-ink reports Alt as ``key.meta`` on many |
| tui | ui-tui\src\lib\platform.ts | 169 | English string, visibility unknown | * terminals. So on darwin a configured ``alt+c`` / ``alt+d`` / ``alt+l`` |
| tui | ui-tui\src\lib\platform.ts | 170 | English string, visibility unknown | * gets swallowed by ``isCopyShortcut`` / ``isAction`` before the voice |
| tui | ui-tui\src\lib\platform.ts | 189 | English string, visibility unknown | /** Match an ink ``key`` event against a parsed named key. The ink runtime |
| tui | ui-tui\src\lib\platform.ts | 190 | English string, visibility unknown | * sets one boolean per named key; ``space`` is a printable char so it |
| tui | ui-tui\src\lib\platform.ts | 191 | English string, visibility unknown | * arrives as ``ch === ' '`` rather than a dedicated ``key.space`` flag. */ |
| tui | ui-tui\src\lib\platform.ts | 198 | English string, visibility unknown | case 'backspace': |
| tui | ui-tui\src\lib\platform.ts | 200 | English string, visibility unknown | case 'delete': |
| tui | ui-tui\src\lib\platform.ts | 202 | English string, visibility unknown | case 'enter': |
| tui | ui-tui\src\lib\platform.ts | 204 | English string, visibility unknown | case 'escape': |
| tui | ui-tui\src\lib\platform.ts | 206 | English string, visibility unknown | case 'space': |
| tui | ui-tui\src\lib\platform.ts | 208 | English string, visibility unknown | case 'tab': |
| tui | ui-tui\src\lib\platform.ts | 214 | English string, visibility unknown | * Parse a config-string voice record key like ``ctrl+b`` / ``alt+r`` / |
| tui | ui-tui\src\lib\platform.ts | 215 | English string, visibility unknown | * ``ctrl+space`` into ``{mod, ch, named?}``. Accepts single characters |
| tui | ui-tui\src\lib\platform.ts | 217 | English string, visibility unknown | * ``enter``/``return``, ``tab``, ``escape``/``esc``, ``backspace``, |
| tui | ui-tui\src\lib\platform.ts | 219 | English string, visibility unknown | * side via the ``c-<name>`` rewrite in ``cli.py``. |
| tui | ui-tui\src\lib\platform.ts | 222 | English string, visibility unknown | * ``config.get full`` — a hand-edited ``voice.record_key: 1`` or |
| tui | ui-tui\src\lib\platform.ts | 223 | English string, visibility unknown | * ``voice.record_key: true`` would otherwise crash ``.trim()`` on a |
| tui | ui-tui\src\lib\platform.ts | 229 | English string, visibility unknown | if (typeof raw !== 'string') { |
| tui | ui-tui\src\lib\platform.ts | 248 | English string, visibility unknown | // Reject multi-modifier chords (``ctrl+alt+r``, ``cmd+ctrl+b``) rather |
| tui | ui-tui\src\lib\platform.ts | 258 | English string, visibility unknown | // Require an explicit modifier. A bare ``o`` / ``space`` / ``escape`` |
| tui | ui-tui\src\lib\platform.ts | 269 | English string, visibility unknown | // Unknown modifier token (e.g. bare ``meta+b`` which is ambiguous on |
| tui | ui-tui\src\lib\platform.ts | 279 | English string, visibility unknown | // check — ``ctrl+c`` / ``ctrl+d`` / ``ctrl+l`` would never actually |
| tui | ui-tui\src\lib\platform.ts | 281 | English string, visibility unknown | if (mod === 'ctrl' && last.length === 1 && _RESERVED_CTRL_CHARS.has(last)) { |
| tui | ui-tui\src\lib\platform.ts | 285 | English string, visibility unknown | // Same for ``super+c`` / ``super+d`` / ``super+l`` / ``super+v`` on |
| tui | ui-tui\src\lib\platform.ts | 287 | English string, visibility unknown | // by ``isCopyShortcut`` / ``isAction`` / the TextInput paste layer |
| tui | ui-tui\src\lib\platform.ts | 291 | English string, visibility unknown | if (isMac && mod === 'super' && last.length === 1 && _RESERVED_SUPER_CHARS.has(last)) { |
| tui | ui-tui\src\lib\platform.ts | 295 | English string, visibility unknown | // On macOS hermes-ink reports Alt as ``key.meta``, which ``isActionMod`` |
| tui | ui-tui\src\lib\platform.ts | 296 | English string, visibility unknown | // accepts as the mac action modifier. So ``alt+c`` / ``alt+d`` / ``alt+l`` |
| tui | ui-tui\src\lib\platform.ts | 297 | English string, visibility unknown | // collide with copy / exit / clear in ``useInputHandlers()`` before the |
| tui | ui-tui\src\lib\platform.ts | 298 | English string, visibility unknown | // voice check. Reject at parse time on darwin only — non-mac ``alt+<letter>`` |
| tui | ui-tui\src\lib\platform.ts | 300 | English string, visibility unknown | if (isMac && mod === 'alt' && last.length === 1 && _RESERVED_ALT_CHARS_MAC.has(last)) { |
| tui | ui-tui\src\lib\platform.ts | 314 | English string, visibility unknown | // Unknown multi-character token (e.g. typo'd ``ctrl+spcae``) — fall back |
| tui | ui-tui\src\lib\platform.ts | 319 | English string, visibility unknown | /** Render a parsed key back as ``Ctrl+B`` / ``Ctrl+Space`` for status text. |
| tui | ui-tui\src\lib\platform.ts | 321 | English string, visibility unknown | * Platform-aware for the ``super`` modifier: renders ``Cmd`` on macOS and |
| tui | ui-tui\src\lib\platform.ts | 322 | English string, visibility unknown | * ``Super`` elsewhere. Previously rendered ``Cmd`` universally, which told |
| tui | ui-tui\src\lib\platform.ts | 327 | English string, visibility unknown | parsed.mod === 'super' ? (isMac ? 'Cmd' : 'Super') : parsed.mod[0].toUpperCase() + parsed.mod.slice(1) |
| tui | ui-tui\src\lib\platform.ts | 334 | English string, visibility unknown | return `${modLabel}+${keyLabel}` |
| tui | ui-tui\src\lib\platform.ts | 339 | English string, visibility unknown | * Compare on the parsed spec rather than ``raw`` so semantically-equal |
| tui | ui-tui\src\lib\platform.ts | 340 | English string, visibility unknown | * aliases (``control+b``, ``ctrl + b``) still get the macOS Cmd+B |
| tui | ui-tui\src\lib\platform.ts | 363 | English string, visibility unknown | // The parser rejects multi-modifier configs (``ctrl+shift+b`` etc.), |
| tui | ui-tui\src\lib\platform.ts | 365 | English string, visibility unknown | // ``ctrl+tab`` would also fire on Ctrl+Shift+Tab and ``alt+enter`` |
| tui | ui-tui\src\lib\platform.ts | 373 | English string, visibility unknown | case 'alt': |
| tui | ui-tui\src\lib\platform.ts | 374 | English string, visibility unknown | // Most terminals surface Alt as either ``alt`` or ``meta``; accept |
| tui | ui-tui\src\lib\platform.ts | 380 | English string, visibility unknown | // Bare Escape on hermes-ink can arrive as ``key.meta=true`` on some |
| tui | ui-tui\src\lib\platform.ts | 381 | English string, visibility unknown | // terminals, so a configured ``alt+escape`` must not match that shape; |
| tui | ui-tui\src\lib\platform.ts | 385 | English string, visibility unknown | case 'ctrl': |
| tui | ui-tui\src\lib\platform.ts | 388 | English string, visibility unknown | // ``ctrl+<key>`` (Copilot round-6 review on #19835). |
| tui | ui-tui\src\lib\platform.ts | 390 | English string, visibility unknown | // The documented default (``ctrl+b``) additionally accepts the |
| tui | ui-tui\src\lib\platform.ts | 391 | English string, visibility unknown | // explicit ``key.super`` bit on macOS for Cmd+B muscle memory — |
| tui | ui-tui\src\lib\platform.ts | 393 | English string, visibility unknown | // ``key.meta`` is hermes-ink's Alt signal and accepting it would |
| tui | ui-tui\src\lib\platform.ts | 400 | English string, visibility unknown | case 'super': |
| tui | ui-tui\src\lib\platform.ts | 401 | English string, visibility unknown | // Require the explicit ``key.super`` bit (kitty-style protocol) |
| tui | ui-tui\src\lib\platform.ts | 405 | English string, visibility unknown | // ``key.meta`` need a kitty-protocol terminal — see the |
| tui | ui-tui\src\lib\prompt.ts | 6 | English string, visibility unknown | if (profileName && !['default', 'custom'].includes(profileName)) { |
| tui | ui-tui\src\lib\prompt.ts | 7 | English string, visibility unknown | return `${profileName} ${prompt}` |
| tui | ui-tui\src\lib\reasoning.ts | 13 | English string, visibility unknown | const paired = new RegExp(`<${tag}>([\\s\\S]*?)</${tag}>\\s*`, 'gi') |
| tui | ui-tui\src\lib\reasoning.ts | 24 | English string, visibility unknown | const unclosed = new RegExp(`<${tag}>([\\s\\S]*)$`, 'i') |
| tui | ui-tui\src\lib\reasoning.ts | 44 | English string, visibility unknown | if (input.includes(`<${tag}>`)) { |
| tui | ui-tui\src\lib\rpc.ts | 1 | English string, visibility unknown | import type { CommandDispatchResponse } from '../gatewayTypes.js' |
| tui | ui-tui\src\lib\rpc.ts | 6 | English string, visibility unknown | !value \|\| typeof value !== 'object' \|\| Array.isArray(value) ? null : (value as T) |
| tui | ui-tui\src\lib\rpc.ts | 11 | English string, visibility unknown | if (!o \|\| typeof o.type !== 'string') { |
| tui | ui-tui\src\lib\rpc.ts | 17 | English string, visibility unknown | if (t === 'exec' \|\| t === 'plugin') { |
| tui | ui-tui\src\lib\rpc.ts | 18 | English string, visibility unknown | return { type: t, output: typeof o.output === 'string' ? o.output : undefined } |
| tui | ui-tui\src\lib\rpc.ts | 21 | English string, visibility unknown | if (t === 'alias' && typeof o.target === 'string') { |
| tui | ui-tui\src\lib\rpc.ts | 22 | English string, visibility unknown | return { type: 'alias', target: o.target } |
| tui | ui-tui\src\lib\rpc.ts | 25 | English string, visibility unknown | if (t === 'skill' && typeof o.name === 'string') { |
| tui | ui-tui\src\lib\rpc.ts | 26 | English string, visibility unknown | return { type: 'skill', name: o.name, message: typeof o.message === 'string' ? o.message : undefined } |
| tui | ui-tui\src\lib\rpc.ts | 29 | English string, visibility unknown | if (t === 'send' && typeof o.message === 'string') { |
| tui | ui-tui\src\lib\rpc.ts | 33 | English string, visibility unknown | notice: typeof o.notice === 'string' ? o.notice : undefined, |
| tui | ui-tui\src\lib\rpc.ts | 41 | mixed Chinese and English, visibility unknown | err instanceof Error && err.message ? err.message : typeof err === 'string' && err.trim() ? err : '请求失败' |
| tui | ui-tui\src\lib\subagentTree.ts | 1 | English string, visibility unknown | import type { SubagentAggregate, SubagentNode, SubagentProgress } from '../types.js' |
| tui | ui-tui\src\lib\subagentTree.ts | 8 | English string, visibility unknown | * Grouping is by `parentId`; a missing `parentId` (or one pointing at an |
| tui | ui-tui\src\lib\subagentTree.ts | 10 | English string, visibility unknown | * Children within a parent are sorted by `depth` then `index` — same key |
| tui | ui-tui\src\lib\subagentTree.ts | 11 | English string, visibility unknown | * used in `turnController.upsertSubagent`, so render order matches spawn |
| tui | ui-tui\src\lib\subagentTree.ts | 14 | English string, visibility unknown | * Older gateways omit `parentId`; every subagent is then a top-level node |
| tui | ui-tui\src\lib\subagentTree.ts | 54 | English string, visibility unknown | * `hotness` = tools per second across the subtree — a crude proxy for |
| tui | ui-tui\src\lib\subagentTree.ts | 55 | English string, visibility unknown | * "how much work is happening in this branch". Used to colour tree rails |
| tui | ui-tui\src\lib\subagentTree.ts | 200 | English string, visibility unknown | export function isRunning(item: Pick<SubagentProgress, 'status'>): boolean { |
| tui | ui-tui\src\lib\subagentTree.ts | 201 | English string, visibility unknown | return item.status === 'running' \|\| item.status === 'queued' |
| tui | ui-tui\src\lib\subagentTree.ts | 238 | mixed Chinese and English, visibility unknown | const pieces = [`🌿 层${Math.max(0, totals.maxDepthFromHere)}`] |
| tui | ui-tui\src\lib\subagentTree.ts | 239 | mixed Chinese and English, visibility unknown | pieces.push(`🧠 ${totals.descendantCount} 派生`) |
| tui | ui-tui\src\lib\subagentTree.ts | 242 | mixed Chinese and English, visibility unknown | pieces.push(`🛠 ${totals.totalTools} 工具`) |
| tui | ui-tui\src\lib\subagentTree.ts | 246 | English string, visibility unknown | pieces.push(`⏱ ${fmtDuration(totals.totalDuration)}`) |
| tui | ui-tui\src\lib\subagentTree.ts | 252 | mixed Chinese and English, visibility unknown | pieces.push(`🔢 ${fmtTokens(tokens)} 令牌`) |
| tui | ui-tui\src\lib\subagentTree.ts | 256 | English string, visibility unknown | pieces.push(`💵 ${fmtCost(totals.costUsd)}`) |
| tui | ui-tui\src\lib\subagentTree.ts | 260 | English string, visibility unknown | pieces.push(`⚡${totals.activeCount}`) |
| tui | ui-tui\src\lib\subagentTree.ts | 266 | English string, visibility unknown | /** Compact dollar amount: `$0.02`, `$1.34`, `$12.4` — never > 5 chars beyond the `$`. */ |
| tui | ui-tui\src\lib\subagentTree.ts | 277 | English string, visibility unknown | return `$${usd.toFixed(2)}` |
| tui | ui-tui\src\lib\subagentTree.ts | 280 | English string, visibility unknown | return `$${usd.toFixed(1)}` |
| tui | ui-tui\src\lib\subagentTree.ts | 294 | English string, visibility unknown | return `${(n / 1000).toFixed(1)}k` |
| tui | ui-tui\src\lib\subagentTree.ts | 297 | English string, visibility unknown | return `${Math.round(n / 1000)}k` |
| tui | ui-tui\src\lib\subagentTree.ts | 306 | English string, visibility unknown | return `${Math.max(0, Math.round(seconds))}s` |
| tui | ui-tui\src\lib\subagentTree.ts | 316 | English string, visibility unknown | * A subagent is top-level if it has no `parentId`, or its parent isn't in |
| tui | ui-tui\src\lib\subagentTree.ts | 318 | English string, visibility unknown | * `buildSubagentTree` uses — keep call sites consistent across the live |
| tui | ui-tui\src\lib\subagentTree.ts | 329 | English string, visibility unknown | * Higher hotness = "hotter" colour. Normalized against the tree's peak hotness |
| tui | ui-tui\src\lib\syntax.ts | 1 | English string, visibility unknown | import type { Theme } from '../theme.js' |
| tui | ui-tui\src\lib\syntax.ts | 46 | English string, visibility unknown | json: { comment: null, keywords: KW('true false null') }, |
| tui | ui-tui\src\lib\syntax.ts | 52 | English string, visibility unknown | yaml: { comment: '#', keywords: KW('true false null yes no on off') } |
| tui | ui-tui\src\lib\terminalModes.ts | 1 | English string, visibility unknown | import { writeSync } from 'node:fs' |
| tui | ui-tui\src\lib\terminalModes.ts | 24 | English string, visibility unknown | type ResettableStream = Pick<NodeJS.WriteStream, 'isTTY' \| 'write'> & { |
| tui | ui-tui\src\lib\terminalModes.ts | 33 | English string, visibility unknown | const fd = typeof stream.fd === 'number' ? stream.fd : stream === process.stdout ? 1 : undefined |
| tui | ui-tui\src\lib\terminalParity.ts | 6 | English string, visibility unknown | } from './terminalSetup.js' |
| tui | ui-tui\src\lib\terminalParity.ts | 11 | English string, visibility unknown | tone: 'info' \| 'warn' |
| tui | ui-tui\src\lib\terminalParity.ts | 18 | English string, visibility unknown | vscodeLike: null \| 'cursor' \| 'vscode' \| 'windsurf' |
| tui | ui-tui\src\lib\terminalParity.ts | 55 | mixed Chinese and English, visibility unknown | '检测到 Apple Terminal · 可用 /paste 处理纯图片剪贴板；如果 Cmd+←/→/⌫ 被改写，可试 Ctrl+A / Ctrl+E / Ctrl+U' |
| tui | ui-tui\src\lib\terminalSetup.ts | 1 | English string, visibility unknown | import { copyFile, mkdir, readFile, writeFile } from 'node:fs/promises' |
| tui | ui-tui\src\lib\terminalSetup.ts | 2 | English string, visibility unknown | import { homedir } from 'node:os' |
| tui | ui-tui\src\lib\terminalSetup.ts | 3 | English string, visibility unknown | import { posix, win32 } from 'node:path' |
| tui | ui-tui\src\lib\terminalSetup.ts | 5 | English string, visibility unknown | export type SupportedTerminal = 'cursor' \| 'vscode' \| 'windsurf' |
| tui | ui-tui\src\lib\terminalSetup.ts | 32 | English string, visibility unknown | vscode: { appName: 'Code', label: 'VS Code' }, |
| tui | ui-tui\src\lib\terminalSetup.ts | 33 | English string, visibility unknown | cursor: { appName: 'Cursor', label: 'Cursor' }, |
| tui | ui-tui\src\lib\terminalSetup.ts | 34 | English string, visibility unknown | windsurf: { appName: 'Windsurf', label: 'Windsurf' } |
| tui | ui-tui\src\lib\terminalSetup.ts | 38 | English string, visibility unknown | key: 'cmd+c', |
| tui | ui-tui\src\lib\terminalSetup.ts | 40 | English string, visibility unknown | when: 'terminalFocus && terminalTextSelected', |
| tui | ui-tui\src\lib\terminalSetup.ts | 46 | English string, visibility unknown | key: 'shift+enter', |
| tui | ui-tui\src\lib\terminalSetup.ts | 52 | English string, visibility unknown | key: 'ctrl+enter', |
| tui | ui-tui\src\lib\terminalSetup.ts | 58 | English string, visibility unknown | key: 'cmd+enter', |
| tui | ui-tui\src\lib\terminalSetup.ts | 64 | English string, visibility unknown | key: 'cmd+z', |
| tui | ui-tui\src\lib\terminalSetup.ts | 70 | English string, visibility unknown | key: 'shift+cmd+z', |
| tui | ui-tui\src\lib\terminalSetup.ts | 81 | English string, visibility unknown | platform === 'win32' ? win32.join(...parts) : posix.join(...parts) |
| tui | ui-tui\src\lib\terminalSetup.ts | 87 | English string, visibility unknown | return 'cursor' |
| tui | ui-tui\src\lib\terminalSetup.ts | 90 | English string, visibility unknown | if (askpass.includes('windsurf')) { |
| tui | ui-tui\src\lib\terminalSetup.ts | 91 | English string, visibility unknown | return 'windsurf' |
| tui | ui-tui\src\lib\terminalSetup.ts | 95 | English string, visibility unknown | return 'vscode' |
| tui | ui-tui\src\lib\terminalSetup.ts | 137 | English string, visibility unknown | if (ch === '/' && content[i + 1] === '/') { |
| tui | ui-tui\src\lib\terminalSetup.ts | 145 | English string, visibility unknown | if (ch === '/' && content[i + 1] === '*') { |
| tui | ui-tui\src\lib\terminalSetup.ts | 170 | English string, visibility unknown | if (platform === 'darwin') { |
| tui | ui-tui\src\lib\terminalSetup.ts | 171 | English string, visibility unknown | return joinForPlatform(platform, homeDir, 'Library', 'Application Support', appName, 'User') |
| tui | ui-tui\src\lib\terminalSetup.ts | 174 | English string, visibility unknown | if (platform === 'win32') { |
| tui | ui-tui\src\lib\terminalSetup.ts | 178 | English string, visibility unknown | return joinForPlatform(platform, homeDir, '.config', appName, 'User') |
| tui | ui-tui\src\lib\terminalSetup.ts | 182 | English string, visibility unknown | return typeof value === 'object' && value !== null |
| tui | ui-tui\src\lib\terminalSetup.ts | 256 | English string, visibility unknown | // VS Code allows multiple bindings on the same key as long as their `when` |
| tui | ui-tui\src\lib\terminalSetup.ts | 258 | English string, visibility unknown | // the bindings differ — e.g. existing `terminalFocus` cmd+c overlaps with |
| tui | ui-tui\src\lib\terminalSetup.ts | 259 | English string, visibility unknown | // our `terminalFocus && terminalTextSelected`, so the existing binding |
| tui | ui-tui\src\lib\terminalSetup.ts | 266 | English string, visibility unknown | if (!whensOverlap(existing.when ?? '', target.when ?? '')) { |
| tui | ui-tui\src\lib\terminalSetup.ts | 275 | English string, visibility unknown | await ops.copyFile(filePath, `${filePath}.backup.${stamp}`) |
| tui | ui-tui\src\lib\terminalSetup.ts | 309 | English string, visibility unknown | const keybindingsFile = joinForPlatform(platform, configDir, 'keybindings.json') |
| tui | ui-tui\src\lib\terminalSetup.ts | 318 | English string, visibility unknown | const content = await ops.readFile(keybindingsFile, 'utf8') |
| tui | ui-tui\src\lib\terminalSetup.ts | 351 | mixed Chinese and English, visibility unknown | `已有终端快捷键会与 ${keybindingsFile} 冲突: ` + conflicts.map(c => c.key).join(', ') |
| tui | ui-tui\src\lib\terminalSetup.ts | 434 | English string, visibility unknown | const content = await ops.readFile(joinForPlatform(platform, configDir, 'keybindings.json'), 'utf8') |
| tui | ui-tui\src\lib\text.ts | 5 | English string, visibility unknown | } from '../config/limits.js' |
| tui | ui-tui\src\lib\text.ts | 7 | English string, visibility unknown | import type { ThinkingMode } from '../types.js' |
| tui | ui-tui\src\lib\text.ts | 57 | English string, visibility unknown | .replace(/!\[(.*?)\]\(([^)\s]+)\)/g, '[image: $1]') |
| tui | ui-tui\src\lib\text.ts | 68 | English string, visibility unknown | .replace(/^\s*[-*+]\s+\[( \|x\|X)\]\s+/, (_m, checked: string) => `• [${checked.toLowerCase() === 'x' ? 'x' : ' '}] `) |
| tui | ui-tui\src\lib\text.ts | 77 | English string, visibility unknown | return !one ? '' : one.length > max ? one.slice(0, max - 1) + '…' : one |
| tui | ui-tui\src\lib\text.ts | 89 | English string, visibility unknown | : `${one.slice(0, head).trimEnd()}.. ${one.slice(-tail).trimStart()}` |
| tui | ui-tui\src\lib\text.ts | 96 | mixed Chinese and English, visibility unknown | return `[[ [${fmtK(lineCount)} 行] ]]` |
| tui | ui-tui\src\lib\text.ts | 99 | English string, visibility unknown | const [head = preview, tail = ''] = preview.split('.. ', 2) |
| tui | ui-tui\src\lib\text.ts | 102 | mixed Chinese and English, visibility unknown | ? `[[ ${head.trimEnd()}.. [${fmtK(lineCount)} 行] .. ${tail.trimStart()} ]]` |
| tui | ui-tui\src\lib\text.ts | 103 | mixed Chinese and English, visibility unknown | : `[[ ${preview} [${fmtK(lineCount)} 行] ]]` |
| tui | ui-tui\src\lib\text.ts | 110 | English string, visibility unknown | 'pondering', |
| tui | ui-tui\src\lib\text.ts | 111 | English string, visibility unknown | 'contemplating', |
| tui | ui-tui\src\lib\text.ts | 112 | English string, visibility unknown | 'musing', |
| tui | ui-tui\src\lib\text.ts | 113 | English string, visibility unknown | 'cogitating', |
| tui | ui-tui\src\lib\text.ts | 114 | English string, visibility unknown | 'ruminating', |
| tui | ui-tui\src\lib\text.ts | 115 | English string, visibility unknown | 'deliberating', |
| tui | ui-tui\src\lib\text.ts | 116 | English string, visibility unknown | 'mulling', |
| tui | ui-tui\src\lib\text.ts | 117 | English string, visibility unknown | 'reflecting', |
| tui | ui-tui\src\lib\text.ts | 118 | English string, visibility unknown | 'processing', |
| tui | ui-tui\src\lib\text.ts | 119 | English string, visibility unknown | 'reasoning', |
| tui | ui-tui\src\lib\text.ts | 120 | English string, visibility unknown | 'analyzing', |
| tui | ui-tui\src\lib\text.ts | 121 | English string, visibility unknown | 'computing', |
| tui | ui-tui\src\lib\text.ts | 122 | English string, visibility unknown | 'synthesizing', |
| tui | ui-tui\src\lib\text.ts | 123 | English string, visibility unknown | 'formulating', |
| tui | ui-tui\src\lib\text.ts | 124 | English string, visibility unknown | 'brainstorming' |
| tui | ui-tui\src\lib\text.ts | 133 | English string, visibility unknown | 'giu' |
| tui | ui-tui\src\lib\text.ts | 157 | mixed Chinese and English, visibility unknown | [/\btheir GitHub profile and repositories\b/gi, '他们的 GitHub 主页和仓库'], |
| tui | ui-tui\src\lib\text.ts | 159 | mixed Chinese and English, visibility unknown | [/\bwhat GitHub features and strategies\b/gi, '哪些 GitHub 功能和策略'], |
| tui | ui-tui\src\lib\text.ts | 189 | English string, visibility unknown | [/\bGitHub Actions\b/gi, 'GitHub Actions'], |
| tui | ui-tui\src\lib\text.ts | 190 | English string, visibility unknown | [/\bIssues\/Discussions\b/gi, 'Issues/Discussions'], |
| tui | ui-tui\src\lib\text.ts | 191 | English string, visibility unknown | [/\bReleases\b/gi, 'Releases'], |
| tui | ui-tui\src\lib\text.ts | 192 | English string, visibility unknown | [/\bGitHub Sponsors\b/gi, 'GitHub Sponsors'], |
| tui | ui-tui\src\lib\text.ts | 193 | English string, visibility unknown | [/\bGitHub Pages\b/gi, 'GitHub Pages'], |
| tui | ui-tui\src\lib\text.ts | 195 | English string, visibility unknown | [/\bGitHub Organizations\b/gi, 'GitHub Organizations'], |
| tui | ui-tui\src\lib\text.ts | 266 | mixed Chinese and English, visibility unknown | ? `[${labelPrefix}；已省略 ${fmtK(omittedLines)} 行 / ${fmtK(omittedChars)} 字符]\n` |
| tui | ui-tui\src\lib\text.ts | 267 | mixed Chinese and English, visibility unknown | : `[${labelPrefix}；已省略 ${fmtK(omittedChars)} 字符]\n` |
| tui | ui-tui\src\lib\text.ts | 269 | English string, visibility unknown | return `${label}${tail}` |
| tui | ui-tui\src\lib\text.ts | 303 | mixed Chinese and English, visibility unknown | lark_markdown_create: '新建飞书 Markdown', |
| tui | ui-tui\src\lib\text.ts | 304 | mixed Chinese and English, visibility unknown | lark_markdown_fetch: '读飞书 Markdown', |
| tui | ui-tui\src\lib\text.ts | 360 | English string, visibility unknown | return preview ? `${label}("${preview}")` : label |
| tui | ui-tui\src\lib\text.ts | 371 | English string, visibility unknown | const took = duration !== undefined ? ` (${duration.toFixed(1)}s)` : '' |
| tui | ui-tui\src\lib\text.ts | 373 | English string, visibility unknown | return `${formatToolCall(name, context)}${took}${detail ? ` :: ${detail}` : ''} ${error ? '✗' : '✓'}` |
| tui | ui-tui\src\lib\text.ts | 376 | English string, visibility unknown | export const isToolTrailResultLine = (line: string) => line.endsWith(' ✓') \|\| line.endsWith(' ✗') |
| tui | ui-tui\src\lib\text.ts | 409 | English string, visibility unknown | line.startsWith('drafting ') \|\| |
| tui | ui-tui\src\lib\text.ts | 410 | English string, visibility unknown | line === 'analyzing tool output…' |
| tui | ui-tui\src\lib\text.ts | 413 | English string, visibility unknown | entry === `${label} ✓` \|\| |
| tui | ui-tui\src\lib\text.ts | 414 | English string, visibility unknown | entry === `${label} ✗` \|\| |
| tui | ui-tui\src\lib\text.ts | 415 | English string, visibility unknown | entry.startsWith(`${label}(`) \|\| |
| tui | ui-tui\src\lib\text.ts | 416 | English string, visibility unknown | entry.startsWith(`${label} ::`) \|\| |
| tui | ui-tui\src\lib\text.ts | 417 | English string, visibility unknown | entry.startsWith(`${label}:`) |
| tui | ui-tui\src\lib\text.ts | 445 | English string, visibility unknown | rows += Math.ceil((`─ ${lang}`.length \|\| 1) / w) |
| tui | ui-tui\src\lib\todo.ts | 1 | English string, visibility unknown | import type { TodoItem } from '../types.js' |
| tui | ui-tui\src\lib\todo.ts | 3 | English string, visibility unknown | export type TodoTone = 'active' \| 'body' \| 'dim' |
| tui | ui-tui\src\lib\todo.ts | 5 | English string, visibility unknown | export const todoGlyph = (status: TodoItem['status']) => |
| tui | ui-tui\src\lib\todo.ts | 8 | English string, visibility unknown | export const todoTone = (status: TodoItem['status']): TodoTone => |
| tui | ui-tui\src\lib\viewportStore.ts | 1 | English string, visibility unknown | import type { ScrollBoxHandle } from '@hermes/ink' |
| tui | ui-tui\src\lib\viewportStore.ts | 2 | English string, visibility unknown | import type { RefObject } from 'react' |
| tui | ui-tui\src\lib\viewportStore.ts | 3 | English string, visibility unknown | import { useCallback, useMemo, useSyncExternalStore } from 'react' |
| tui | ui-tui\src\lib\viewportStore.ts | 64 | English string, visibility unknown | return `${v.atBottom ? 1 : 0}:${Math.ceil(v.top / 8) * 8}:${v.viewportHeight}:${Math.ceil(v.scrollHeight / 8) * 8}:${v.pending}` |
| tui | ui-tui\src\lib\viewportStore.ts | 84 | English string, visibility unknown | return `${v.top}:${v.viewportHeight}:${v.scrollHeight}` |
| tui | ui-tui\src\lib\viewportStore.ts | 95 | English string, visibility unknown | const [atBottom = '1', top = '0', viewportHeight = '0', scrollHeight = '0', pending = '0'] = key.split(':') |
| tui | ui-tui\src\lib\viewportStore.ts | 116 | English string, visibility unknown | const [top = '0', viewportHeight = '0', scrollHeight = '0'] = key.split(':') |
| tui | ui-tui\src\lib\virtualHeights.ts | 1 | English string, visibility unknown | import type { Msg } from '../types.js' |
| tui | ui-tui\src\lib\virtualHeights.ts | 3 | English string, visibility unknown | import { transcriptBodyWidth } from './inputMetrics.js' |
| tui | ui-tui\src\lib\virtualHeights.ts | 16 | English string, visibility unknown | const todoSig = msg.todos?.map(t => `${t.status}:${t.content}`).join('\u0001') ?? '' |
| tui | ui-tui\src\lib\virtualHeights.ts | 20 | English string, visibility unknown | .map(s => `${s.title ?? ''}:${s.text?.length ?? 0}:${s.items?.length ?? 0}:${s.rows?.length ?? 0}`) |
| tui | ui-tui\src\lib\virtualHeights.ts | 23 | English string, visibility unknown | const introSig = msg.kind === 'intro' ? (msg.info?.version ?? '') : '' |
| tui | ui-tui\src\lib\virtualHeights.ts | 28 | English string, visibility unknown | hashText([msg.text, msg.thinking ?? '', msg.tools?.join('\n') ?? '', todoSig, panelSig, introSig].join('\0')) |
| tui | ui-tui\src\lib\virtualHeights.ts | 83 | English string, visibility unknown | if (msg.kind === 'intro') { |
| tui | ui-tui\src\lib\virtualHeights.ts | 87 | English string, visibility unknown | if (msg.kind === 'panel') { |
| tui | ui-tui\src\lib\virtualHeights.ts | 91 | English string, visibility unknown | if (msg.kind === 'trail' && msg.todos?.length) { |
| tui | ui-tui\src\lib\virtualHeights.ts | 103 | English string, visibility unknown | if (!compact && msg.role === 'assistant') { |
| tui | ui-tui\src\lib\virtualHeights.ts | 116 | English string, visibility unknown | if (msg.role === 'user' \|\| msg.kind === 'diff') { |
| tui | ui-tui\src\lib\virtualHeights.ts | 118 | English string, visibility unknown | } else if (msg.kind === 'slash') { |
| tui | ui-tui\src\lib\virtualHeights.ts | 124 | English string, visibility unknown | // the caller to pass `withSeparator` only when it matches that gate. |
| tui | ui-tui\src\lib\wheelAccel.ts | 18 | English string, visibility unknown | import { isXtermJs } from '@hermes/ink' |
| tui | ui-tui\src\lib\wheelAccel.ts | 79 | English string, visibility unknown | /** Compute rows for one wheel event, mutating `state`. Returns 0 when a |
| tui | ui-tui\src\lib\wheelAccel.ts | 87 | English string, visibility unknown | // Idle disengage runs first so a pending bounce can't mask "user paused |
| tui | ui-tui\src\theme.ts | 103 | English string, visibility unknown | 'text', |
| tui | ui-tui\src\theme.ts | 104 | English string, visibility unknown | 'label', |
| tui | ui-tui\src\theme.ts | 106 | English string, visibility unknown | 'error', |
| tui | ui-tui\src\theme.ts | 107 | English string, visibility unknown | 'warn', |
| tui | ui-tui\src\theme.ts | 108 | English string, visibility unknown | 'prompt', |
| tui | ui-tui\src\theme.ts | 109 | English string, visibility unknown | 'statusFg', |
| tui | ui-tui\src\theme.ts | 110 | English string, visibility unknown | 'statusStrong', |
| tui | ui-tui\src\theme.ts | 111 | English string, visibility unknown | 'statusGood', |
| tui | ui-tui\src\theme.ts | 112 | English string, visibility unknown | 'statusWarn', |
| tui | ui-tui\src\theme.ts | 113 | English string, visibility unknown | 'statusBad', |
| tui | ui-tui\src\theme.ts | 114 | English string, visibility unknown | 'statusCritical', |
| tui | ui-tui\src\theme.ts | 115 | English string, visibility unknown | 'shellDollar' |
| tui | ui-tui\src\theme.ts | 250 | English string, visibility unknown | return `ansi256(${ansi})` |
| tui | ui-tui\src\theme.ts | 259 | mixed Chinese and English, visibility unknown | welcome: '输入任务，或用 /help 查看命令。', |
| tui | ui-tui\src\theme.ts | 285 | English string, visibility unknown | Array.isArray(raw) ? raw.filter((item): item is string => typeof item === 'string' && item.length > 0) : [] |
| tui | ui-tui\src\theme.ts | 290 | English string, visibility unknown | Array.isArray(item) && typeof item[0] === 'string' && typeof item[1] === 'string' |
| tui | ui-tui\src\theme.ts | 297 | English string, visibility unknown | if (!raw \|\| typeof raw !== 'object' \|\| Array.isArray(raw)) { |
| tui | ui-tui\src\theme.ts | 312 | English string, visibility unknown | if (!raw \|\| typeof raw !== 'object' \|\| Array.isArray(raw)) { |
| tui | ui-tui\src\theme.ts | 333 | English string, visibility unknown | // secondary" semantic. Field labels still use `label` (65%) which |
| tui | ui-tui\src\theme.ts | 341 | English string, visibility unknown | ok: '#4caf50', |
| tui | ui-tui\src\theme.ts | 343 | English string, visibility unknown | warn: '#ffa726', |
| tui | ui-tui\src\theme.ts | 346 | English string, visibility unknown | // sessionLabel/sessionBorder intentionally track the `dim` value — they |
| tui | ui-tui\src\theme.ts | 347 | English string, visibility unknown | // are "same role, same colour" by design. fromSkin's banner_dim fallback |
| tui | ui-tui\src\theme.ts | 356 | English string, visibility unknown | statusGood: '#8FBC8F', |
| tui | ui-tui\src\theme.ts | 362 | English string, visibility unknown | diffAdded: 'rgb(220,255,220)', |
| tui | ui-tui\src\theme.ts | 363 | English string, visibility unknown | diffRemoved: 'rgb(255,220,220)', |
| tui | ui-tui\src\theme.ts | 364 | English string, visibility unknown | diffAddedWord: 'rgb(36,138,61)', |
| tui | ui-tui\src\theme.ts | 365 | English string, visibility unknown | diffRemovedWord: 'rgb(207,34,46)', |
| tui | ui-tui\src\theme.ts | 366 | English string, visibility unknown | shellDollar: '#4dabf7' |
| tui | ui-tui\src\theme.ts | 411 | English string, visibility unknown | diffAdded: 'rgb(200,240,200)', |
| tui | ui-tui\src\theme.ts | 412 | English string, visibility unknown | diffRemoved: 'rgb(240,200,200)', |
| tui | ui-tui\src\theme.ts | 413 | English string, visibility unknown | diffAddedWord: 'rgb(27,94,32)', |
| tui | ui-tui\src\theme.ts | 414 | English string, visibility unknown | diffRemovedWord: 'rgb(183,28,28)', |
| tui | ui-tui\src\theme.ts | 443 | English string, visibility unknown | // non-hex character (e.g. `fffgff` would parse as `fff` and yield a |
| tui | ui-tui\src\theme.ts | 444 | English string, visibility unknown | // false-positive "white" reading), so reject anything that doesn't match |
| tui | ui-tui\src\theme.ts | 468 | English string, visibility unknown | // Rec. 709 luma — close enough for "is this background bright". |
| tui | ui-tui\src\theme.ts | 475 | English string, visibility unknown | // `0`/`false`/`no`/`off` → dark. Either explicit value wins |
| tui | ui-tui\src\theme.ts | 507 | English string, visibility unknown | if (themeFlag === 'light') { |
| tui | ui-tui\src\theme.ts | 511 | English string, visibility unknown | if (themeFlag === 'dark') { |
| tui | ui-tui\src\theme.ts | 524 | English string, visibility unknown | // Validate as a decimal integer before coercing — `Number('')` is 0, |
| tui | ui-tui\src\theme.ts | 555 | English string, visibility unknown | return termProgram === 'Apple_Terminal' && colorTerm !== 'truecolor' && colorTerm !== '24bit' && isLight |
| tui | ui-tui\src\theme.ts | 604 | English string, visibility unknown | const accent = c('ui_accent') ?? c('banner_accent') ?? d.color.accent |
| tui | ui-tui\src\theme.ts | 605 | English string, visibility unknown | const bannerAccent = c('banner_accent') ?? c('banner_title') ?? d.color.accent |
| tui | ui-tui\src\theme.ts | 606 | English string, visibility unknown | const muted = c('banner_dim') ?? d.color.muted |
| tui | ui-tui\src\theme.ts | 607 | English string, visibility unknown | const completionBg = c('completion_menu_bg') ?? d.color.completionBg |
| tui | ui-tui\src\theme.ts | 610 | English string, visibility unknown | c('completion_menu_current_bg') ?? |
| tui | ui-tui\src\theme.ts | 613 | English string, visibility unknown | const completionMetaBg = c('completion_menu_meta_bg') ?? completionBg |
| tui | ui-tui\src\theme.ts | 614 | English string, visibility unknown | const completionMetaCurrentBg = c('completion_menu_meta_current_bg') ?? completionCurrentBg |
| tui | ui-tui\src\theme.ts | 618 | English string, visibility unknown | primary: c('ui_primary') ?? c('banner_title') ?? d.color.primary, |
| tui | ui-tui\src\theme.ts | 620 | English string, visibility unknown | border: c('ui_border') ?? c('banner_border') ?? d.color.border, |
| tui | ui-tui\src\theme.ts | 621 | English string, visibility unknown | text: c('ui_text') ?? c('banner_text') ?? d.color.text, |
| tui | ui-tui\src\theme.ts | 631 | English string, visibility unknown | warn: c('ui_warn') ?? d.color.warn, |
| tui | ui-tui\src\theme.ts | 633 | English string, visibility unknown | prompt: c('prompt') ?? c('banner_text') ?? d.color.prompt, |
| tui | ui-tui\src\theme.ts | 634 | English string, visibility unknown | sessionLabel: c('session_label') ?? muted, |
| tui | ui-tui\src\theme.ts | 635 | English string, visibility unknown | sessionBorder: c('session_border') ?? muted, |
| tui | ui-tui\src\theme.ts | 637 | English string, visibility unknown | statusBg: c('status_bar_bg') ?? d.color.statusBg, |
| tui | ui-tui\src\theme.ts | 638 | English string, visibility unknown | statusFg: c('status_bar_text') ?? d.color.statusFg, |
| tui | ui-tui\src\theme.ts | 639 | English string, visibility unknown | statusStrong: c('status_bar_strong') ?? c('ui_primary') ?? d.color.statusStrong, |
| tui | ui-tui\src\theme.ts | 640 | English string, visibility unknown | statusDim: c('status_bar_dim') ?? c('banner_dim') ?? d.color.statusDim, |
| tui | ui-tui\src\theme.ts | 641 | English string, visibility unknown | statusGood: c('status_bar_good') ?? c('ui_ok') ?? d.color.statusGood, |
| tui | ui-tui\src\theme.ts | 642 | English string, visibility unknown | statusWarn: c('status_bar_warn') ?? c('ui_warn') ?? d.color.statusWarn, |
| tui | ui-tui\src\theme.ts | 643 | English string, visibility unknown | statusBad: c('status_bar_bad') ?? d.color.statusBad, |
| tui | ui-tui\src\theme.ts | 644 | English string, visibility unknown | statusCritical: c('status_bar_critical') ?? c('ui_error') ?? d.color.statusCritical, |
| tui | ui-tui\src\theme.ts | 645 | English string, visibility unknown | selectionBg: c('selection_bg') ?? c('completion_menu_current_bg') ?? (hasSkinColors ? completionCurrentBg : d.color.selectionBg), |
| tui | ui-tui\src\theme.ts | 651 | English string, visibility unknown | shellDollar: c('shell_dollar') ?? d.color.shellDollar |
| tui | ui-tui\src\types.ts | 17 | English string, visibility unknown | tone: 'error' \| 'info' \| 'warn' |
| tui | ui-tui\src\types.ts | 20 | English string, visibility unknown | export type SubagentStatus = 'completed' \| 'error' \| 'failed' \| 'interrupted' \| 'queued' \| 'running' \| 'timeout' |
| tui | ui-tui\src\types.ts | 113 | English string, visibility unknown | kind?: 'diff' \| 'intro' \| 'panel' \| 'slash' \| 'trail' |
| tui | ui-tui\src\types.ts | 126 | English string, visibility unknown | export type Role = 'assistant' \| 'system' \| 'tool' \| 'user' |
| tui | ui-tui\src\types.ts | 127 | English string, visibility unknown | export type DetailsMode = 'hidden' \| 'collapsed' \| 'expanded' |
| tui | ui-tui\src\types.ts | 128 | English string, visibility unknown | export type ThinkingMode = 'collapsed' \| 'truncated' \| 'full' |
| tui | ui-tui\src\types.ts | 131 | English string, visibility unknown | // at lookup time is: explicit `display.sections.<name>` → built-in |
| tui | ui-tui\src\types.ts | 133 | English string, visibility unknown | // expand `thinking`/`tools` and hide `activity`; `subagents` falls through |
| tui | ui-tui\src\types.ts | 135 | English string, visibility unknown | export type SectionName = 'thinking' \| 'tools' \| 'subagents' \| 'activity' |
| tui | ui-tui\src\types\hermes-ink.d.ts | 1 | English string, visibility unknown | import type * as React from 'react' |
| tui | ui-tui\src\types\hermes-ink.d.ts | 3 | English string, visibility unknown | declare module '@hermes/ink' { |
| tui | ui-tui\src\types\hermes-ink.d.ts | 58 | English string, visibility unknown | readonly reason: 'resize' \| 'offscreen' \| 'clear' |
| tui | ui-tui\src\types\hermes-ink.d.ts | 127 | English string, visibility unknown | export type EvictLevel = 'all' \| 'half' |
| tui | ui-tui\src\types\hermes-ink.d.ts | 155 | English string, visibility unknown | readonly captureScrolledRows: (firstRow: number, lastRow: number, side: 'above' \| 'below') => void |

## skip_tech

| Scope | File | Line | Reason | Text |
| --- | --- | ---: | --- | --- |
| feishu | gateway\display_config.py | 12 | technical/protocol line | Exception: ``display.streaming`` is CLI-only. Gateway streaming follows the |
| feishu | gateway\display_config.py | 84 | technical/protocol line | "telegram": {**_TIER_HIGH, "tool_progress": "new"}, |
| feishu | gateway\display_config.py | 85 | technical/protocol line | "discord": _TIER_HIGH, |
| feishu | gateway\display_config.py | 90 | technical/protocol line | "slack": {**_TIER_MEDIUM, "tool_progress": "off"}, |
| feishu | gateway\display_config.py | 93 | technical/protocol line | "feishu": _TIER_MEDIUM, |
| feishu | gateway\display_config.py | 129 | technical/protocol line | Platform config key (e.g. ``"telegram"``, ``"slack"``). Use |
| feishu | gateway\display_config.py | 186 | technical/protocol line | """Normalise YAML quirks (bare ``off`` → False in YAML 1.1).""" |
| feishu | gateway\platforms\feishu_comment_rules.py | 27 | technical/protocol line | # Uses the canonical ``get_hermes_home()`` helper (HERMES_HOME-aware and |
| feishu | gateway\platforms\feishu_comment_rules.py | 32 | technical/protocol line | RULES_FILE = get_hermes_home() / "feishu_comment_rules.json" |
| feishu | gateway\platforms\feishu_comment_rules.py | 33 | technical/protocol line | PAIRING_FILE = get_hermes_home() / "feishu_comment_pairing.json" |
| feishu | gateway\platforms\feishu_comment_rules.py | 98 | technical/protocol line | logger.warning("[Feishu-Rules] Failed to read %s, using empty config", self._path) |
| feishu | gateway\platforms\feishu_comment_rules.py | 237 | technical/protocol line | tmp = PAIRING_FILE.with_suffix(".tmp") |
| feishu | gateway\platforms\feishu_comment_rules.py | 300 | user-facing output | print(f"规则文件: {RULES_FILE}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 301 | user-facing output | print(f" 存在: {RULES_FILE.exists()}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 302 | user-facing output | print(f"配对文件: {PAIRING_FILE}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 303 | user-facing output | print(f" 存在: {PAIRING_FILE.exists()}") |
| feishu | gateway\platforms\feishu_comment_rules.py | 369 | mixed technical/protocol line | f"规则配置文件: {RULES_FILE}\n" |
| feishu | gateway\platforms\feishu_comment_rules.py | 370 | mixed technical/protocol line | " 可直接编辑这个 JSON 文件来配置策略和文档规则。\n" |
| feishu | gateway\platforms\feishu_comment.py | 6 | technical/protocol line | main ``feishu.py`` adapter does not grow further and comment-related |
| feishu | gateway\platforms\feishu_comment.py | 43 | technical/protocol line | http_method = HttpMethod.GET if method == "GET" else HttpMethod.POST |
| feishu | gateway\platforms\feishu_comment.py | 61 | technical/protocol line | """Execute a lark API request and return (code, msg, data_dict).""" |
| feishu | gateway\platforms\feishu_comment.py | 62 | technical/protocol line | logger.info("[Feishu-Comment] API >>> %s %s paths=%s queries=%s body=%s", |
| feishu | gateway\platforms\feishu_comment.py | 86 | technical/protocol line | logger.info("[Feishu-Comment] API <<< %s %s code=%s msg=%s data_keys=%s", |
| feishu | gateway\platforms\feishu_comment.py | 94 | technical/protocol line | logger.warning("[Feishu-Comment] API FAIL raw response: %s", raw_content) |
| feishu | gateway\platforms\feishu_comment.py | 107 | technical/protocol line | or a ``SimpleNamespace`` (Webhook) built from the full JSON body. |
| feishu | gateway\platforms\feishu_comment.py | 112 | technical/protocol line | logger.debug("[Feishu-Comment] parse_drive_comment_event: data type=%s", type(data).__name__) |
| feishu | gateway\platforms\feishu_comment.py | 115 | technical/protocol line | logger.debug("[Feishu-Comment] parse_drive_comment_event: no .event attribute, returning None") |
| feishu | gateway\platforms\feishu_comment.py | 121 | technical/protocol line | logger.debug("[Feishu-Comment] parse_drive_comment_event: evt keys=%s", list(evt.keys())) |
| feishu | gateway\platforms\feishu_comment.py | 175 | technical/protocol line | logger.error("[Feishu-Comment] lark_oapi not available") |
| feishu | gateway\platforms\feishu_comment.py | 185 | technical/protocol line | client, "POST", _REACTION_URI, |
| feishu | gateway\platforms\feishu_comment.py | 194 | technical/protocol line | "[Feishu-Comment] Reaction '%s' added: file=%s:%s reply=%s", |
| feishu | gateway\platforms\feishu_comment.py | 199 | technical/protocol line | "[Feishu-Comment] Reaction API failed: code=%s msg=%s " |
| feishu | gateway\platforms\feishu_comment.py | 225 | technical/protocol line | client, "POST", _REACTION_URI, |
| feishu | gateway\platforms\feishu_comment.py | 234 | technical/protocol line | "[Feishu-Comment] Reaction '%s' deleted: file=%s:%s reply=%s", |
| feishu | gateway\platforms\feishu_comment.py | 239 | technical/protocol line | "[Feishu-Comment] Reaction API failed: code=%s msg=%s " |
| feishu | gateway\platforms\feishu_comment.py | 269 | technical/protocol line | logger.debug("[Feishu-Comment] query_document_meta: file_token=%s file_type=%s", file_token, file_type) |
| feishu | gateway\platforms\feishu_comment.py | 271 | technical/protocol line | client, "POST", _BATCH_QUERY_META_URI, body=body, |
| feishu | gateway\platforms\feishu_comment.py | 274 | technical/protocol line | logger.warning("[Feishu-Comment] Meta batch_query failed: code=%s msg=%s", code, msg) |
| feishu | gateway\platforms\feishu_comment.py | 278 | technical/protocol line | logger.debug("[Feishu-Comment] query_document_meta: raw metas type=%s value=%s", |
| feishu | gateway\platforms\feishu_comment.py | 285 | technical/protocol line | logger.debug("[Feishu-Comment] query_document_meta: no metas found") |
| feishu | gateway\platforms\feishu_comment.py | 314 | technical/protocol line | logger.debug("[Feishu-Comment] batch_query_comment: file_token=%s comment_id=%s", file_token, comment_id) |
| feishu | gateway\platforms\feishu_comment.py | 318 | technical/protocol line | client, "POST", _BATCH_QUERY_COMMENT_URI, |
| feishu | gateway\platforms\feishu_comment.py | 330 | technical/protocol line | "[Feishu-Comment] batch_query_comment retry %d/%d: code=%s msg=%s", |
| feishu | gateway\platforms\feishu_comment.py | 336 | technical/protocol line | "[Feishu-Comment] batch_query_comment failed after %d attempts: code=%s msg=%s", |
| feishu | gateway\platforms\feishu_comment.py | 343 | technical/protocol line | logger.debug("[Feishu-Comment] batch_query_comment: got %d items", len(items) if isinstance(items, list) else 0) |
| feishu | gateway\platforms\feishu_comment.py | 346 | technical/protocol line | logger.info("[Feishu-Comment] batch_query_comment: is_whole=%s quote=%s reply_count=%s", |
| feishu | gateway\platforms\feishu_comment.py | 351 | technical/protocol line | logger.warning("[Feishu-Comment] batch_query_comment: empty items, raw data keys=%s", list(data.keys())) |
| feishu | gateway\platforms\feishu_comment.py | 359 | technical/protocol line | logger.debug("[Feishu-Comment] list_whole_comments: file_token=%s", file_token) |
| feishu | gateway\platforms\feishu_comment.py | 374 | technical/protocol line | client, "GET", _LIST_COMMENTS_URI, |
| feishu | gateway\platforms\feishu_comment.py | 379 | technical/protocol line | logger.warning("[Feishu-Comment] List whole comments failed: code=%s msg=%s", code, msg) |
| feishu | gateway\platforms\feishu_comment.py | 385 | technical/protocol line | logger.debug("[Feishu-Comment] list_whole_comments: page got %d items, total=%d", |
| feishu | gateway\platforms\feishu_comment.py | 394 | technical/protocol line | logger.info("[Feishu-Comment] list_whole_comments: total %d whole comments fetched", len(all_comments)) |
| feishu | gateway\platforms\feishu_comment.py | 407 | technical/protocol line | logger.debug("[Feishu-Comment] list_comment_replies: file_token=%s comment_id=%s", file_token, comment_id) |
| feishu | gateway\platforms\feishu_comment.py | 424 | technical/protocol line | client, "GET", _LIST_REPLIES_URI, |
| feishu | gateway\platforms\feishu_comment.py | 429 | technical/protocol line | logger.warning("[Feishu-Comment] List replies failed: code=%s msg=%s", code, msg) |
| feishu | gateway\platforms\feishu_comment.py | 451 | technical/protocol line | "[Feishu-Comment] list_comment_replies: reply_id=%s not found, retry %d/%d", |
| feishu | gateway\platforms\feishu_comment.py | 457 | technical/protocol line | "[Feishu-Comment] list_comment_replies: reply_id=%s not found after %d attempts", |
| feishu | gateway\platforms\feishu_comment.py | 461 | technical/protocol line | logger.info("[Feishu-Comment] list_comment_replies: total %d replies fetched", len(all_replies)) |
| feishu | gateway\platforms\feishu_comment.py | 466 | technical/protocol line | """Escape characters not allowed in Feishu comment text_run content.""" |
| feishu | gateway\platforms\feishu_comment.py | 489 | technical/protocol line | client, "POST", _REPLY_COMMENT_URI, |
| feishu | gateway\platforms\feishu_comment.py | 496 | technical/protocol line | "[Feishu-Comment] reply_to_comment FAILED: code=%s msg=%s comment_id=%s", |
| feishu | gateway\platforms\feishu_comment.py | 500 | technical/protocol line | logger.info("[Feishu-Comment] reply_to_comment OK: comment_id=%s", comment_id) |
| feishu | gateway\platforms\feishu_comment.py | 522 | technical/protocol line | client, "POST", _ADD_COMMENT_URI, |
| feishu | gateway\platforms\feishu_comment.py | 527 | technical/protocol line | logger.warning("[Feishu-Comment] add_whole_comment FAILED: code=%s msg=%s", code, msg) |
| feishu | gateway\platforms\feishu_comment.py | 529 | technical/protocol line | logger.info("[Feishu-Comment] add_whole_comment OK") |
| feishu | gateway\platforms\feishu_comment.py | 568 | technical/protocol line | logger.info("[Feishu-Comment] deliver_comment_reply: is_whole=%s comment_id=%s text_len=%d chunks=%d", |
| feishu | gateway\platforms\feishu_comment.py | 574 | technical/protocol line | logger.info("[Feishu-Comment] deliver_comment_reply: sending chunk %d/%d (%d chars)", |
| feishu | gateway\platforms\feishu_comment.py | 584 | technical/protocol line | logger.info("[Feishu-Comment] Reply not allowed (1069302), falling back to add_whole_comment") |
| feishu | gateway\platforms\feishu_comment.py | 622 | technical/protocol line | parts.append(f"@{person.get('user_id', 'unknown')}") |
| feishu | gateway\platforms\feishu_comment.py | 627 | technical/protocol line | """Extract user_id from a reply dict.""" |
| feishu | gateway\platforms\feishu_comment.py | 628 | technical/protocol line | user_id = reply.get("user_id", "") |
| feishu | gateway\platforms\feishu_comment.py | 630 | technical/protocol line | return user_id.get("open_id", "") or user_id.get("user_id", "") |
| feishu | gateway\platforms\feishu_comment.py | 648 | technical/protocol line | uid = person.get("user_id", "") |
| feishu | gateway\platforms\feishu_comment.py | 670 | technical/protocol line | r"(?:feishu\.cn\|larkoffice\.com\|larksuite\.com\|lark\.suite\.com)" |
| feishu | gateway\platforms\feishu_comment.py | 720 | technical/protocol line | client, "GET", _WIKI_GET_NODE_URI, |
| feishu | gateway\platforms\feishu_comment.py | 728 | technical/protocol line | logger.warning("[Feishu-Comment] Wiki reverse lookup failed: code=%s msg=%s obj=%s:%s", code, msg, obj_type, obj_token) |
| feishu | gateway\platforms\feishu_comment.py | 748 | technical/protocol line | client, "GET", _WIKI_GET_NODE_URI, |
| feishu | gateway\platforms\feishu_comment.py | 757 | technical/protocol line | "[Feishu-Comment] Wiki resolved: %s -> %s:%s", |
| feishu | gateway\platforms\feishu_comment.py | 765 | technical/protocol line | logger.warning("[Feishu-Comment] Wiki resolve failed: code=%s msg=%s token=%s", code, msg, wiki_token) |
| feishu | gateway\platforms\feishu_comment.py | 918 | technical/protocol line | marker = " <-- YOU" if is_self else "" |
| feishu | gateway\platforms\feishu_comment.py | 919 | technical/protocol line | lines.append(f"[{user_id}] {_truncate(text)}{marker}") |
| feishu | gateway\platforms\feishu_comment.py | 959 | technical/protocol line | marker = " <-- YOU" if is_self else "" |
| feishu | gateway\platforms\feishu_comment.py | 960 | technical/protocol line | lines.append(f"[{user_id}] {_truncate(text)}{marker}") |
| feishu | gateway\platforms\feishu_comment.py | 976 | technical/protocol line | """Resolve model and provider credentials, same as gateway message handling.""" |
| feishu | gateway\platforms\feishu_comment.py | 986 | technical/protocol line | if not model and runtime_kwargs.get("provider"): |
| feishu | gateway\platforms\feishu_comment.py | 989 | technical/protocol line | model = get_default_model_for_provider(runtime_kwargs["provider"]) |
| feishu | gateway\platforms\feishu_comment.py | 1023 | technical/protocol line | logger.info("[Feishu-Comment] Session expired: %s", key) |
| feishu | gateway\platforms\feishu_comment.py | 1044 | technical/protocol line | logger.info("[Feishu-Comment] Session saved: %s (%d messages)", key, len(cleaned)) |
| feishu | gateway\platforms\feishu_comment.py | 1057 | technical/protocol line | logger.info("[Feishu-Comment] _run_comment_agent: injecting lark client into tool thread-locals") |
| feishu | gateway\platforms\feishu_comment.py | 1065 | technical/protocol line | logger.info("[Feishu-Comment] _run_comment_agent: model=%s provider=%s base_url=%s", |
| feishu | gateway\platforms\feishu_comment.py | 1066 | technical/protocol line | model, runtime_kwargs.get("provider"), (runtime_kwargs.get("base_url") or "")[:50]) |
| feishu | gateway\platforms\feishu_comment.py | 1071 | technical/protocol line | logger.info("[Feishu-Comment] _run_comment_agent: loaded %d history messages from session %s", |
| feishu | gateway\platforms\feishu_comment.py | 1078 | technical/protocol line | provider=runtime_kwargs.get("provider"), |
| feishu | gateway\platforms\feishu_comment.py | 1087 | technical/protocol line | logger.info("[Feishu-Comment] _run_comment_agent: calling run_conversation (prompt=%d chars, history=%d)", |
| feishu | gateway\platforms\feishu_comment.py | 1092 | technical/protocol line | logger.info("[Feishu-Comment] _run_comment_agent: done api_calls=%d response_len=%d response=%s", |
| feishu | gateway\platforms\feishu_comment.py | 1103 | technical/protocol line | logger.exception("[Feishu-Comment] _run_comment_agent: agent failed: %s", e) |
| feishu | gateway\platforms\feishu_comment.py | 1114 | technical/protocol line | _NO_REPLY_SENTINEL = "NO_REPLY" |
| feishu | gateway\platforms\feishu_comment.py | 1132 | technical/protocol line | logger.info("[Feishu-Comment] ========== handle_drive_comment_event START ==========") |
| feishu | gateway\platforms\feishu_comment.py | 1135 | technical/protocol line | logger.warning("[Feishu-Comment] Dropping malformed drive comment event") |
| feishu | gateway\platforms\feishu_comment.py | 1137 | technical/protocol line | logger.info("[Feishu-Comment] [Step 0/5] Event parsed successfully") |
| feishu | gateway\platforms\feishu_comment.py | 1149 | technical/protocol line | logger.debug("[Feishu-Comment] Skipping self-authored event: from=%s", from_open_id) |
| feishu | gateway\platforms\feishu_comment.py | 1152 | technical/protocol line | logger.debug("[Feishu-Comment] Skipping event not addressed to self: to=%s", to_open_id or "(empty)") |
| feishu | gateway\platforms\feishu_comment.py | 1155 | technical/protocol line | logger.debug("[Feishu-Comment] Skipping notice_type=%s", notice_type) |
| feishu | gateway\platforms\feishu_comment.py | 1158 | technical/protocol line | logger.warning("[Feishu-Comment] Missing required fields, skipping") |
| feishu | gateway\platforms\feishu_comment.py | 1162 | technical/protocol line | "[Feishu-Comment] Event: notice=%s file=%s:%s comment=%s from=%s", |
| feishu | gateway\platforms\feishu_comment.py | 1179 | technical/protocol line | logger.info("[Feishu-Comment] Comments disabled for %s:%s, skipping", file_type, file_token) |
| feishu | gateway\platforms\feishu_comment.py | 1182 | technical/protocol line | logger.info("[Feishu-Comment] User %s denied (policy=%s, rule=%s)", from_open_id, rule.policy, rule.match_source) |
| feishu | gateway\platforms\feishu_comment.py | 1185 | technical/protocol line | logger.info("[Feishu-Comment] Access granted: user=%s policy=%s rule=%s", from_open_id, rule.policy, rule.match_source) |
| feishu | gateway\platforms\feishu_comment.py | 1198 | technical/protocol line | logger.info("[Feishu-Comment] [Step 2/5] Parallel fetch: doc meta + comment batch_query") |
| feishu | gateway\platforms\feishu_comment.py | 1217 | technical/protocol line | logger.info("[Feishu-Comment] [Step 3/5] Building timeline (is_whole=%s)", is_whole) |
| feishu | gateway\platforms\feishu_comment.py | 1220 | technical/protocol line | logger.info("[Feishu-Comment] Fetching whole-document comments for timeline...") |
| feishu | gateway\platforms\feishu_comment.py | 1288 | technical/protocol line | logger.info("[Feishu-Comment] Fetching comment thread replies...") |
| feishu | gateway\platforms\feishu_comment.py | 1319 | technical/protocol line | logger.info("[Feishu-Comment] Local timeline: %d entries, target_idx=%d, quote=%s root=%s target=%s", |
| feishu | gateway\platforms\feishu_comment.py | 1346 | technical/protocol line | logger.info("[Feishu-Comment] [Step 4/5] Prompt built (%d chars), running agent...", len(prompt)) |
| feishu | gateway\platforms\feishu_comment.py | 1347 | technical/protocol line | logger.debug("[Feishu-Comment] Full prompt:\n%s", prompt) |
| feishu | gateway\platforms\feishu_comment.py | 1358 | technical/protocol line | logger.info("[Feishu-Comment] Agent returned NO_REPLY, skipping delivery") |
| feishu | gateway\platforms\feishu_comment.py | 1360 | technical/protocol line | logger.info("[Feishu-Comment] Agent response (%d chars): %s", len(response), response[:200]) |
| feishu | gateway\platforms\feishu_comment.py | 1363 | technical/protocol line | logger.info("[Feishu-Comment] [Step 5/5] Delivering reply (is_whole=%s, comment_id=%s)", is_whole, comment_id) |
| feishu | gateway\platforms\feishu_comment.py | 1368 | technical/protocol line | logger.info("[Feishu-Comment] Reply delivered successfully") |
| feishu | gateway\platforms\feishu_comment.py | 1370 | technical/protocol line | logger.error("[Feishu-Comment] Failed to deliver reply") |
| feishu | gateway\platforms\feishu_comment.py | 1382 | technical/protocol line | logger.info("[Feishu-Comment] ========== handle_drive_comment_event END ==========") |
| feishu | gateway\platforms\feishu.py | 44 | technical/protocol line | over ``open_id`` (via user_id) so that sessions stay stable if the same |
| feishu | gateway\platforms\feishu.py | 180 | technical/protocol line | _POST_CONTENT_INVALID_RE = re.compile(r"content format of the post type is incorrect", re.IGNORECASE) |
| feishu | gateway\platforms\feishu.py | 209 | technical/protocol line | _FEISHU_APP_LOCK_SCOPE = "feishu-app-id" |
| feishu | gateway\platforms\feishu.py | 217 | technical/protocol line | _DEFAULT_WEBHOOK_PATH = "/feishu/webhook" |
| feishu | gateway\platforms\feishu.py | 261 | technical/protocol line | "feishu": "https://accounts.feishu.cn", |
| feishu | gateway\platforms\feishu.py | 262 | technical/protocol line | "lark": "https://accounts.larksuite.com", |
| feishu | gateway\platforms\feishu.py | 265 | technical/protocol line | "feishu": "https://open.feishu.cn", |
| feishu | gateway\platforms\feishu.py | 266 | technical/protocol line | "lark": "https://open.larksuite.com", |
| feishu | gateway\platforms\feishu.py | 309 | technical/protocol line | "chat_id", |
| feishu | gateway\platforms\feishu.py | 314 | technical/protocol line | "user_id", |
| feishu | gateway\platforms\feishu.py | 460 | technical/protocol line | getattr(sid, "user_id", None), |
| feishu | gateway\platforms\feishu.py | 608 | technical/protocol line | """Build a compact Feishu card for runtime metadata.""" |
| feishu | gateway\platforms\feishu.py | 781 | technical/protocol line | # Post <at>.user_id is a placeholder ("@_user_N" or "@_all"); look up |
| feishu | gateway\platforms\feishu.py | 801 | mixed technical/protocol line | return f"[图片: {alt}]" if alt else FALLBACK_IMAGE_TEXT |
| feishu | gateway\platforms\feishu.py | 817 | mixed technical/protocol line | return f"[附件: {file_name}]" if file_name else FALLBACK_ATTACHMENT_TEXT |
| feishu | gateway\platforms\feishu.py | 896 | technical/protocol line | # <at user_id="@_all">, so reading .values() after parsing is enough. |
| feishu | gateway\platforms\feishu.py | 982 | technical/protocol line | payload.get("chat_id"), |
| feishu | gateway\platforms\feishu.py | 998 | technical/protocol line | metadata={"chat_id": share_id, "chat_name": chat_name}, |
| feishu | gateway\platforms\feishu.py | 1152 | mixed technical/protocol line | return f"[附件: {normalized_name}]" if normalized_name else FALLBACK_ATTACHMENT_TEXT |
| feishu | gateway\platforms\feishu.py | 1254 | technical/protocol line | if id_type == "user_id": |
| feishu | gateway\platforms\feishu.py | 1261 | technical/protocol line | str(getattr(mention_id, "user_id", "") or ""), |
| feishu | gateway\platforms\feishu.py | 1352 | technical/protocol line | """Run the official Lark WS client in its own thread-local event loop.""" |
| feishu | gateway\platforms\feishu.py | 1370 | technical/protocol line | logger.debug("[Feishu] Failed to apply websocket runtime overrides", exc_info=True) |
| feishu | gateway\platforms\feishu.py | 1381 | user-facing output | raise RuntimeError("Feishu _configure_with_overrides called but original_configure is None") |
| feishu | gateway\platforms\feishu.py | 1417 | technical/protocol line | Lazy-installs lark-oapi via ``tools.lazy_deps.ensure("platform.feishu")`` |
| feishu | gateway\platforms\feishu.py | 1444 | technical/protocol line | "lark": lark, |
| feishu | gateway\platforms\feishu.py | 1462 | technical/protocol line | "FEISHU_DOMAIN": FEISHU_DOMAIN, |
| feishu | gateway\platforms\feishu.py | 1463 | technical/protocol line | "LARK_DOMAIN": LARK_DOMAIN, |
| feishu | gateway\platforms\feishu.py | 1469 | technical/protocol line | "FEISHU_AVAILABLE": True, |
| feishu | gateway\platforms\feishu.py | 1473 | technical/protocol line | return ensure_and_bind("platform.feishu", _import, globals(), prompt=False) |
| feishu | gateway\platforms\feishu.py | 1477 | technical/protocol line | """Feishu/Lark bot adapter.""" |
| feishu | gateway\platforms\feishu.py | 1571 | technical/protocol line | allow_bots = os.getenv("FEISHU_ALLOW_BOTS", "none").strip().lower() |
| feishu | gateway\platforms\feishu.py | 1574 | technical/protocol line | "[Feishu] Unknown allow_bots=%r, falling back to 'none'. Valid: none, mentions, all.", |
| feishu | gateway\platforms\feishu.py | 1580 | technical/protocol line | app_id=str(extra.get("app_id") or os.getenv("FEISHU_APP_ID", "")).strip(), |
| feishu | gateway\platforms\feishu.py | 1581 | technical/protocol line | app_secret=str(extra.get("app_secret") or os.getenv("FEISHU_APP_SECRET", "")).strip(), |
| feishu | gateway\platforms\feishu.py | 1582 | technical/protocol line | domain_name=str(extra.get("domain") or os.getenv("FEISHU_DOMAIN", "feishu")).strip().lower(), |
| feishu | gateway\platforms\feishu.py | 1584 | technical/protocol line | extra.get("connection_mode") or os.getenv("FEISHU_CONNECTION_MODE", "websocket") |
| feishu | gateway\platforms\feishu.py | 1586 | technical/protocol line | encrypt_key=os.getenv("FEISHU_ENCRYPT_KEY", "").strip(), |
| feishu | gateway\platforms\feishu.py | 1587 | technical/protocol line | verification_token=os.getenv("FEISHU_VERIFICATION_TOKEN", "").strip(), |
| feishu | gateway\platforms\feishu.py | 1588 | technical/protocol line | group_policy=os.getenv("FEISHU_GROUP_POLICY", "allowlist").strip().lower(), |
| feishu | gateway\platforms\feishu.py | 1591 | technical/protocol line | for item in os.getenv("FEISHU_ALLOWED_USERS", "").split(",") |
| feishu | gateway\platforms\feishu.py | 1594 | technical/protocol line | bot_open_id=os.getenv("FEISHU_BOT_OPEN_ID", "").strip(), |
| feishu | gateway\platforms\feishu.py | 1595 | technical/protocol line | bot_user_id=os.getenv("FEISHU_BOT_USER_ID", "").strip(), |
| feishu | gateway\platforms\feishu.py | 1596 | technical/protocol line | bot_name=os.getenv("FEISHU_BOT_NAME", "").strip(), |
| feishu | gateway\platforms\feishu.py | 1599 | technical/protocol line | int(os.getenv("HERMES_FEISHU_DEDUP_CACHE_SIZE", str(_DEFAULT_DEDUP_CACHE_SIZE))), |
| feishu | gateway\platforms\feishu.py | 1602 | technical/protocol line | os.getenv("HERMES_FEISHU_TEXT_BATCH_DELAY_SECONDS", str(_DEFAULT_TEXT_BATCH_DELAY_SECONDS)) |
| feishu | gateway\platforms\feishu.py | 1605 | technical/protocol line | os.getenv("HERMES_FEISHU_TEXT_BATCH_SPLIT_DELAY_SECONDS", "2.0") |
| feishu | gateway\platforms\feishu.py | 1609 | technical/protocol line | int(os.getenv("HERMES_FEISHU_TEXT_BATCH_MAX_MESSAGES", str(_DEFAULT_TEXT_BATCH_MAX_MESSAGES))), |
| feishu | gateway\platforms\feishu.py | 1613 | technical/protocol line | int(os.getenv("HERMES_FEISHU_TEXT_BATCH_MAX_CHARS", str(_DEFAULT_TEXT_BATCH_MAX_CHARS))), |
| feishu | gateway\platforms\feishu.py | 1616 | technical/protocol line | os.getenv("HERMES_FEISHU_MEDIA_BATCH_DELAY_SECONDS", str(_DEFAULT_MEDIA_BATCH_DELAY_SECONDS)) |
| feishu | gateway\platforms\feishu.py | 1619 | technical/protocol line | extra.get("webhook_host") or os.getenv("FEISHU_WEBHOOK_HOST", _DEFAULT_WEBHOOK_HOST) |
| feishu | gateway\platforms\feishu.py | 1622 | technical/protocol line | extra.get("webhook_port") or os.getenv("FEISHU_WEBHOOK_PORT", str(_DEFAULT_WEBHOOK_PORT)) |
| feishu | gateway\platforms\feishu.py | 1625 | technical/protocol line | str(extra.get("webhook_path") or os.getenv("FEISHU_WEBHOOK_PATH", _DEFAULT_WEBHOOK_PATH)).strip() |
| feishu | gateway\platforms\feishu.py | 1637 | technical/protocol line | extra.get("require_mention", os.getenv("FEISHU_REQUIRE_MENTION", "true")) |
| feishu | gateway\platforms\feishu.py | 1639 | technical/protocol line | outbound_format=str(extra.get("outbound_format") or os.getenv("HERMES_FEISHU_OUTBOUND_FORMAT", "auto")).strip().lower(), |
| feishu | gateway\platforms\feishu.py | 1640 | technical/protocol line | card_mode=_to_boolean(extra.get("card_mode", os.getenv("HERMES_FEISHU_CARD_MODE", "false"))), |
| feishu | gateway\platforms\feishu.py | 1675 | technical/protocol line | logger.warning("[Feishu] Unknown outbound_format=%r, falling back to auto", self._outbound_format) |
| feishu | gateway\platforms\feishu.py | 1708 | technical/protocol line | """Connect to Feishu/Lark.""" |
| feishu | gateway\platforms\feishu.py | 1710 | technical/protocol line | logger.error("[Feishu] lark-oapi not installed") |
| feishu | gateway\platforms\feishu.py | 1713 | technical/protocol line | logger.error("[Feishu] FEISHU_APP_ID or FEISHU_APP_SECRET not set") |
| feishu | gateway\platforms\feishu.py | 1717 | technical/protocol line | "[Feishu] Unsupported FEISHU_CONNECTION_MODE=%s. Supported modes: websocket, webhook.", |
| feishu | gateway\platforms\feishu.py | 1732 | technical/protocol line | "Another local Hermes gateway is already using this Feishu app_id" |
| feishu | gateway\platforms\feishu.py | 1733 | technical/protocol line | + (f" (PID {owner_pid})." if owner_pid else ".") |
| feishu | gateway\platforms\feishu.py | 1734 | technical/protocol line | + " Stop the other gateway before starting a second Feishu websocket client." |
| feishu | gateway\platforms\feishu.py | 1736 | technical/protocol line | logger.error("[Feishu] %s", message) |
| feishu | gateway\platforms\feishu.py | 1743 | technical/protocol line | logger.info("[Feishu] Connected in %s mode (%s)", self._connection_mode, self._domain_name) |
| feishu | gateway\platforms\feishu.py | 1749 | technical/protocol line | logger.error("[Feishu] Failed to connect: %s", exc, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 1753 | technical/protocol line | """Disconnect from Feishu/Lark.""" |
| feishu | gateway\platforms\feishu.py | 1763 | technical/protocol line | logger.debug("[Feishu] Cancelling websocket thread tasks and stopping loop") |
| feishu | gateway\platforms\feishu.py | 1767 | technical/protocol line | logger.debug("[Feishu] Found %d pending tasks in websocket thread", len(tasks)) |
| feishu | gateway\platforms\feishu.py | 1777 | technical/protocol line | logger.debug("[Feishu] Waiting for websocket thread to exit (timeout=10s)") |
| feishu | gateway\platforms\feishu.py | 1779 | technical/protocol line | logger.debug("[Feishu] Websocket thread exited cleanly") |
| feishu | gateway\platforms\feishu.py | 1781 | technical/protocol line | logger.warning("[Feishu] Websocket thread did not exit within 10s - may be stuck") |
| feishu | gateway\platforms\feishu.py | 1783 | technical/protocol line | logger.debug("[Feishu] Websocket thread cancelled during disconnect") |
| feishu | gateway\platforms\feishu.py | 1795 | technical/protocol line | logger.info("[Feishu] Disconnected") |
| feishu | gateway\platforms\feishu.py | 1840 | technical/protocol line | """Send a Feishu message.""" |
| feishu | gateway\platforms\feishu.py | 1862 | technical/protocol line | logger.warning("[Feishu] Invalid post payload rejected by API; falling back to plain text") |
| feishu | gateway\platforms\feishu.py | 1875 | technical/protocol line | logger.warning("[Feishu] Post payload rejected by API response; falling back to plain text") |
| feishu | gateway\platforms\feishu.py | 1898 | technical/protocol line | """Edit a previously sent Feishu text/post message.""" |
| feishu | gateway\platforms\feishu.py | 1910 | technical/protocol line | logger.warning("[Feishu] Invalid post update payload rejected by API; falling back to plain text") |
| feishu | gateway\platforms\feishu.py | 1922 | technical/protocol line | logger.error("[Feishu] Failed to edit message %s: %s", message_id, exc, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 1933 | technical/protocol line | """Send runtime metadata as a compact Feishu status card.""" |
| feishu | gateway\platforms\feishu.py | 2012 | technical/protocol line | "message_id": result.message_id or "", |
| feishu | gateway\platforms\feishu.py | 2013 | technical/protocol line | "chat_id": chat_id, |
| feishu | gateway\platforms\feishu.py | 2017 | technical/protocol line | logger.warning("[Feishu] send_exec_approval failed: %s", exc) |
| feishu | gateway\platforms\feishu.py | 2080 | technical/protocol line | "message_id": result.message_id or "", |
| feishu | gateway\platforms\feishu.py | 2081 | technical/protocol line | "chat_id": chat_id, |
| feishu | gateway\platforms\feishu.py | 2085 | technical/protocol line | logger.warning("[Feishu] send_update_prompt failed: %s", exc) |
| feishu | gateway\platforms\feishu.py | 2090 | technical/protocol line | """Build raw card JSON for a resolved approval action.""" |
| feishu | gateway\platforms\feishu.py | 2138 | technical/protocol line | """Send audio to Feishu as a file attachment plus optional caption.""" |
| feishu | gateway\platforms\feishu.py | 2158 | technical/protocol line | """Send a document/file attachment to Feishu.""" |
| feishu | gateway\platforms\feishu.py | 2177 | technical/protocol line | """Send a video file to Feishu.""" |
| feishu | gateway\platforms\feishu.py | 2196 | technical/protocol line | """Send a local image file to Feishu.""" |
| feishu | gateway\platforms\feishu.py | 2245 | technical/protocol line | logger.error("[Feishu] Failed to send image %s: %s", image_path, exc, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 2249 | technical/protocol line | """Feishu bot API does not expose a typing indicator.""" |
| feishu | gateway\platforms\feishu.py | 2260 | technical/protocol line | """Download a remote image then send it through the native Feishu image flow.""" |
| feishu | gateway\platforms\feishu.py | 2264 | technical/protocol line | logger.error("[Feishu] Failed to download image %s: %s", image_url, exc, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 2288 | technical/protocol line | """Feishu has no native GIF bubble; degrade to a downloadable file.""" |
| feishu | gateway\platforms\feishu.py | 2296 | technical/protocol line | logger.error("[Feishu] Failed to download animation %s: %s", animation_url, exc, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 2304 | technical/protocol line | degraded_caption = f"[GIF downgraded to file]\n{caption}" if caption else "[GIF downgraded to file]" |
| feishu | gateway\platforms\feishu.py | 2315 | technical/protocol line | """Return real chat metadata from Feishu when available.""" |
| feishu | gateway\platforms\feishu.py | 2317 | technical/protocol line | "chat_id": chat_id, |
| feishu | gateway\platforms\feishu.py | 2318 | technical/protocol line | "name": chat_id, |
| feishu | gateway\platforms\feishu.py | 2334 | technical/protocol line | logger.warning("[Feishu] Failed to get chat info for %s: [%s] %s", chat_id, code, msg) |
| feishu | gateway\platforms\feishu.py | 2340 | technical/protocol line | "chat_id": chat_id, |
| feishu | gateway\platforms\feishu.py | 2341 | technical/protocol line | "name": str(getattr(data, "name", None) or chat_id), |
| feishu | gateway\platforms\feishu.py | 2348 | technical/protocol line | logger.warning("[Feishu] Failed to get chat info for %s", chat_id, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 2352 | technical/protocol line | """Feishu text messages are plain text by default.""" |
| feishu | gateway\platforms\feishu.py | 2373 | user-facing field | name="feishu-pending-inbound-drainer", |
| feishu | gateway\platforms\feishu.py | 2395 | technical/protocol line | message_id = str(getattr(message, "message_id", "") or "unknown") |
| feishu | gateway\platforms\feishu.py | 2397 | technical/protocol line | message_id = "unknown" |
| feishu | gateway\platforms\feishu.py | 2399 | technical/protocol line | "[Feishu] Pending-inbound queue full (%d); dropped oldest event %s", |
| feishu | gateway\platforms\feishu.py | 2409 | technical/protocol line | "[Feishu] Queued inbound event for replay (loop not ready, queue depth=%d)", |
| feishu | gateway\platforms\feishu.py | 2435 | technical/protocol line | "[Feishu] Dropped %d queued inbound event(s) during shutdown", |
| feishu | gateway\platforms\feishu.py | 2465 | technical/protocol line | "[Feishu] Replayed %d queued inbound event(s)", |
| feishu | gateway\platforms\feishu.py | 2481 | technical/protocol line | "[Feishu] Adapter loop unavailable for %.0fs; " |
| feishu | gateway\platforms\feishu.py | 2499 | technical/protocol line | logger.debug("[Feishu] Dropping malformed inbound event: missing message/sender") |
| feishu | gateway\platforms\feishu.py | 2502 | technical/protocol line | message_id = getattr(message, "message_id", None) |
| feishu | gateway\platforms\feishu.py | 2504 | technical/protocol line | logger.debug("[Feishu] Dropping duplicate/missing message_id: %s", message_id) |
| feishu | gateway\platforms\feishu.py | 2509 | technical/protocol line | logger.debug("[Feishu] dropping inbound event: %s", reason) |
| feishu | gateway\platforms\feishu.py | 2526 | technical/protocol line | message_id = getattr(message, "message_id", None) or "" |
| feishu | gateway\platforms\feishu.py | 2527 | technical/protocol line | logger.debug("[Feishu] Ignoring message_read event: %s", message_id) |
| feishu | gateway\platforms\feishu.py | 2532 | technical/protocol line | chat_id = str(getattr(event, "chat_id", "") or "") |
| feishu | gateway\platforms\feishu.py | 2533 | technical/protocol line | logger.info("[Feishu] Bot added to chat: %s", chat_id) |
| feishu | gateway\platforms\feishu.py | 2539 | technical/protocol line | chat_id = str(getattr(event, "chat_id", "") or "") |
| feishu | gateway\platforms\feishu.py | 2540 | technical/protocol line | logger.info("[Feishu] Bot removed from chat: %s", chat_id) |
| feishu | gateway\platforms\feishu.py | 2544 | technical/protocol line | logger.debug("[Feishu] User entered P2P chat with bot") |
| feishu | gateway\platforms\feishu.py | 2547 | technical/protocol line | logger.debug("[Feishu] Message recalled by user") |
| feishu | gateway\platforms\feishu.py | 2560 | technical/protocol line | logger.warning("[Feishu] Dropping drive comment event before adapter loop is ready") |
| feishu | gateway\platforms\feishu.py | 2570 | technical/protocol line | message_id = str(getattr(event, "message_id", "") or "") |
| feishu | gateway\platforms\feishu.py | 2574 | technical/protocol line | action = "added" if "created" in event_type else "removed" |
| feishu | gateway\platforms\feishu.py | 2576 | technical/protocol line | "[Feishu] Reaction %s on message %s (operator_type=%s, emoji=%s)", |
| feishu | gateway\platforms\feishu.py | 2606 | technical/protocol line | logger.warning("[Feishu] Dropping card action before adapter loop is ready") |
| feishu | gateway\platforms\feishu.py | 2665 | technical/protocol line | logger.debug("[Feishu] Card action missing approval_id, ignoring") |
| feishu | gateway\platforms\feishu.py | 2690 | technical/protocol line | logger.debug("[Feishu] Card action missing update_prompt_id, ignoring") |
| feishu | gateway\platforms\feishu.py | 2693 | technical/protocol line | logger.debug("[Feishu] Update prompt %s already resolved or unknown", prompt_id) |
| feishu | gateway\platforms\feishu.py | 2698 | technical/protocol line | logger.debug("[Feishu] Card action has invalid update prompt answer=%r", answer) |
| feishu | gateway\platforms\feishu.py | 2704 | technical/protocol line | logger.warning("[Feishu] Unauthorized update prompt click by %s", open_id or "<unknown>") |
| feishu | gateway\platforms\feishu.py | 2725 | technical/protocol line | logger.debug("[Feishu] Approval %s already resolved or unknown", approval_id) |
| feishu | gateway\platforms\feishu.py | 2731 | technical/protocol line | "Feishu button resolved %d approval(s) for session %s (choice=%s, user=%s)", |
| feishu | gateway\platforms\feishu.py | 2735 | technical/protocol line | logger.error("Failed to resolve gateway approval from Feishu button: %s", exc) |
| feishu | gateway\platforms\feishu.py | 2741 | technical/protocol line | logger.debug("[Feishu] Update prompt %s already resolved or unknown", prompt_id) |
| feishu | gateway\platforms\feishu.py | 2746 | technical/protocol line | "Feishu update prompt resolved for session %s (answer=%s, user=%s)", |
| feishu | gateway\platforms\feishu.py | 2750 | technical/protocol line | logger.error("Failed to resolve Feishu update prompt: %s", exc) |
| feishu | gateway\platforms\feishu.py | 2757 | technical/protocol line | message_id = str(getattr(event, "message_id", "") or "") |
| feishu | gateway\platforms\feishu.py | 2776 | technical/protocol line | chat_id = str(getattr(msg, "chat_id", "") or "") |
| feishu | gateway\platforms\feishu.py | 2781 | technical/protocol line | logger.debug("[Feishu] Failed to fetch message for reaction routing", exc_info=True) |
| feishu | gateway\platforms\feishu.py | 2784 | technical/protocol line | user_id_obj = getattr(event, "user_id", None) |
| feishu | gateway\platforms\feishu.py | 2786 | technical/protocol line | emoji_type = str(getattr(reaction_type_obj, "emoji_type", "") or "UNKNOWN") |
| feishu | gateway\platforms\feishu.py | 2787 | technical/protocol line | action = "added" if "created" in event_type else "removed" |
| feishu | gateway\platforms\feishu.py | 2794 | technical/protocol line | chat_name=chat_info.get("name") or chat_id or "Feishu Chat", |
| feishu | gateway\platforms\feishu.py | 2796 | technical/protocol line | user_id=sender_profile["user_id"], |
| feishu | gateway\platforms\feishu.py | 2809 | technical/protocol line | logger.info("[Feishu] Routing reaction %s:%s on bot message %s as synthetic event", action, emoji_type, message_id) |
| feishu | gateway\platforms\feishu.py | 2825 | technical/protocol line | """Route Feishu interactive card button clicks as synthetic COMMAND events.""" |
| feishu | gateway\platforms\feishu.py | 2829 | technical/protocol line | logger.debug("[Feishu] Dropping duplicate card action token: %s", token) |
| feishu | gateway\platforms\feishu.py | 2833 | technical/protocol line | chat_id = str(getattr(context, "open_chat_id", "") or "") |
| feishu | gateway\platforms\feishu.py | 2837 | technical/protocol line | logger.debug("[Feishu] Card action missing chat_id or operator open_id, dropping") |
| feishu | gateway\platforms\feishu.py | 2856 | technical/protocol line | chat_name=chat_info.get("name") or chat_id or "Feishu Chat", |
| feishu | gateway\platforms\feishu.py | 2858 | technical/protocol line | user_id=sender_profile["user_id"], |
| feishu | gateway\platforms\feishu.py | 2871 | technical/protocol line | logger.info("[Feishu] Routing card action %r from %s in %s as synthetic command", action_tag, open_id, chat_id) |
| feishu | gateway\platforms\feishu.py | 2893 | technical/protocol line | chat_id = getattr(event.source, "chat_id", "") or "" if event.source else "" |
| feishu | gateway\platforms\feishu.py | 2903 | technical/protocol line | return os.getenv("FEISHU_REACTIONS", "true").strip().lower() not in {"false", "0", "no"} |
| feishu | gateway\platforms\feishu.py | 2930 | technical/protocol line | "[Feishu] Add reaction %s on %s rejected: code=%s msg=%s", |
| feishu | gateway\platforms\feishu.py | 2938 | technical/protocol line | "[Feishu] Add reaction %s on %s raised", |
| feishu | gateway\platforms\feishu.py | 2960 | technical/protocol line | "[Feishu] Remove reaction %s on %s rejected: code=%s msg=%s", |
| feishu | gateway\platforms\feishu.py | 2968 | technical/protocol line | "[Feishu] Remove reaction %s on %s raised", |
| feishu | gateway\platforms\feishu.py | 3034 | technical/protocol line | "[Feishu] Webhook anomaly: %d consecutive error responses (%s) from %s " |
| feishu | gateway\platforms\feishu.py | 3073 | technical/protocol line | logger.debug("[Feishu] Ignoring empty text message id=%s", message_id) |
| feishu | gateway\platforms\feishu.py | 3092 | technical/protocol line | or getattr(sender_id, "user_id", None) |
| feishu | gateway\platforms\feishu.py | 3101 | technical/protocol line | getattr(message, "chat_id", "") or "", |
| feishu | gateway\platforms\feishu.py | 3108 | technical/protocol line | chat_id = getattr(message, "chat_id", "") or "" |
| feishu | gateway\platforms\feishu.py | 3113 | technical/protocol line | chat_name=chat_info.get("name") or chat_id or "Feishu Chat", |
| feishu | gateway\platforms\feishu.py | 3115 | technical/protocol line | user_id=sender_profile["user_id"], |
| feishu | gateway\platforms\feishu.py | 3136 | technical/protocol line | """Apply Feishu-specific burst protection before entering the base adapter.""" |
| feishu | gateway\platforms\feishu.py | 3216 | technical/protocol line | "[Feishu] Flushing media batch %s with %d attachment(s)", |
| feishu | gateway\platforms\feishu.py | 3235 | user-facing output | raise ValueError(f"Blocked unsafe URL (SSRF protection): {file_url[:80]}") |
| feishu | gateway\platforms\feishu.py | 3251 | technical/protocol line | content_type_hdr = str(response.headers.get("Content-Type", "")) |
| feishu | gateway\platforms\feishu.py | 3290 | technical/protocol line | logger.warning("[Feishu] Webhook rate limit exceeded for %s", remote_ip) |
| feishu | gateway\platforms\feishu.py | 3296 | technical/protocol line | content_type = str(headers.get("Content-Type", "") or "").split(";")[0].strip().lower() |
| feishu | gateway\platforms\feishu.py | 3297 | technical/protocol line | if content_type and content_type != "application/json": |
| feishu | gateway\platforms\feishu.py | 3298 | technical/protocol line | logger.warning("[Feishu] Webhook rejected: unexpected Content-Type %r from %s", content_type, remote_ip) |
| feishu | gateway\platforms\feishu.py | 3305 | technical/protocol line | logger.warning("[Feishu] Webhook body too large (%d bytes) from %s", content_length, remote_ip) |
| feishu | gateway\platforms\feishu.py | 3315 | technical/protocol line | logger.warning("[Feishu] Webhook body read timed out after %ds from %s", _FEISHU_WEBHOOK_BODY_TIMEOUT_SECONDS, remote_ip) |
| feishu | gateway\platforms\feishu.py | 3323 | technical/protocol line | logger.warning("[Feishu] Webhook body exceeds limit (%d bytes) from %s", len(body_bytes), remote_ip) |
| feishu | gateway\platforms\feishu.py | 3331 | Feishu error/response | return _web_json_response({"code": 400, "msg": "无效 JSON"}, status=400) |
| feishu | gateway\platforms\feishu.py | 3343 | technical/protocol line | logger.warning("[Feishu] Webhook rejected: invalid verification token from %s", remote_ip) |
| feishu | gateway\platforms\feishu.py | 3349 | technical/protocol line | logger.warning("[Feishu] Webhook rejected: invalid signature from %s", remote_ip) |
| feishu | gateway\platforms\feishu.py | 3354 | technical/protocol line | logger.error("[Feishu] Encrypted webhook payloads are not supported by Hermes webhook mode") |
| feishu | gateway\platforms\feishu.py | 3360 | technical/protocol line | event_type = str((payload.get("header") or {}).get("event_type") or "") |
| feishu | gateway\platforms\feishu.py | 3362 | technical/protocol line | if event_type == "im.message.receive_v1": |
| feishu | gateway\platforms\feishu.py | 3364 | technical/protocol line | elif event_type == "im.message.message_read_v1": |
| feishu | gateway\platforms\feishu.py | 3366 | technical/protocol line | elif event_type == "im.chat.member.bot.added_v1": |
| feishu | gateway\platforms\feishu.py | 3368 | technical/protocol line | elif event_type == "im.chat.member.bot.deleted_v1": |
| feishu | gateway\platforms\feishu.py | 3370 | technical/protocol line | elif event_type in {"im.message.reaction.created_v1", "im.message.reaction.deleted_v1"}: |
| feishu | gateway\platforms\feishu.py | 3372 | technical/protocol line | elif event_type == "card.action.trigger": |
| feishu | gateway\platforms\feishu.py | 3374 | technical/protocol line | elif event_type == "drive.notice.comment_add_v1": |
| feishu | gateway\platforms\feishu.py | 3377 | technical/protocol line | logger.debug("[Feishu] Ignoring webhook event type: %s", event_type or "unknown") |
| feishu | gateway\platforms\feishu.py | 3387 | technical/protocol line | timestamp = str(headers.get("x-lark-request-timestamp", "") or "") |
| feishu | gateway\platforms\feishu.py | 3388 | technical/protocol line | nonce = str(headers.get("x-lark-request-nonce", "") or "") |
| feishu | gateway\platforms\feishu.py | 3389 | technical/protocol line | signature = str(headers.get("x-lark-signature", "") or "") |
| feishu | gateway\platforms\feishu.py | 3398 | technical/protocol line | logger.debug("[Feishu] Signature verification raised an exception", exc_info=True) |
| feishu | gateway\platforms\feishu.py | 3440 | technical/protocol line | """Return the session-scoped key used for Feishu text aggregation.""" |
| feishu | gateway\platforms\feishu.py | 3459 | technical/protocol line | """Debounce rapid Feishu text bursts into a single MessageEvent.""" |
| feishu | gateway\platforms\feishu.py | 3497 | technical/protocol line | """Reset the debounce timer for a pending Feishu text batch.""" |
| feishu | gateway\platforms\feishu.py | 3544 | technical/protocol line | "[Feishu] Flushing text batch %s (%d chars)", |
| feishu | gateway\platforms\feishu.py | 3559 | technical/protocol line | message_id = str(getattr(message, "message_id", "") or "") |
| feishu | gateway\platforms\feishu.py | 3560 | technical/protocol line | logger.info("[Feishu] Received raw message type=%s message_id=%s", raw_type, message_id) |
| feishu | gateway\platforms\feishu.py | 3649 | technical/protocol line | if ext not in {".txt", ".md"} and media_type not in {"text/plain", "text/markdown"}: |
| feishu | gateway\platforms\feishu.py | 3655 | technical/protocol line | logger.warning("[Feishu] Failed to inject text document content from %s", cached_path, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 3670 | technical/protocol line | "[Feishu] Failed to download image %s: %s %s", |
| feishu | gateway\platforms\feishu.py | 3679 | technical/protocol line | content_type = self._get_response_header(response, "Content-Type") |
| feishu | gateway\platforms\feishu.py | 3686 | technical/protocol line | logger.warning("[Feishu] Failed to cache image resource %s", image_key, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 3714 | technical/protocol line | "[Feishu] Resource download failed for %s/%s via type=%s: %s %s", |
| feishu | gateway\platforms\feishu.py | 3726 | technical/protocol line | content_type = self._get_response_header(response, "Content-Type") |
| feishu | gateway\platforms\feishu.py | 3737 | technical/protocol line | logger.info("[Feishu] Cached message image resource at %s", cached_path) |
| feishu | gateway\platforms\feishu.py | 3743 | technical/protocol line | logger.info("[Feishu] Cached message audio resource at %s", cached_path) |
| feishu | gateway\platforms\feishu.py | 3750 | technical/protocol line | logger.info("[Feishu] Cached message video resource at %s", cached_path) |
| feishu | gateway\platforms\feishu.py | 3756 | technical/protocol line | logger.info("[Feishu] Cached message document resource at %s", cached_path) |
| feishu | gateway\platforms\feishu.py | 3760 | technical/protocol line | "[Feishu] Failed to cache message resource %s/%s", |
| feishu | gateway\platforms\feishu.py | 3804 | technical/protocol line | return SUPPORTED_DOCUMENT_TYPES.get(ext, mimetypes.guess_type(filename or "")[0] or "application/octet-stream") |
| feishu | gateway\platforms\feishu.py | 3853 | technical/protocol line | """Map Feishu's three-tier user IDs onto Hermes' SessionSource fields. |
| feishu | gateway\platforms\feishu.py | 3855 | technical/protocol line | Preference order for the primary ``user_id`` field: |
| feishu | gateway\platforms\feishu.py | 3865 | technical/protocol line | user_id = getattr(sender_id, "user_id", None) or None |
| feishu | gateway\platforms\feishu.py | 3875 | technical/protocol line | "user_id": primary_id, |
| feishu | gateway\platforms\feishu.py | 3881 | technical/protocol line | """Return a cached sender name only while its TTL is still valid.""" |
| feishu | gateway\platforms\feishu.py | 3899 | technical/protocol line | """Bots divert to bot/basic_batch — contact API doesn't return bot names. |
| feishu | gateway\platforms\feishu.py | 3927 | technical/protocol line | id_type = "user_id" |
| feishu | gateway\platforms\feishu.py | 3945 | technical/protocol line | logger.debug("[Feishu] Failed to resolve sender name for %s", sender_id, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 3974 | technical/protocol line | logger.debug("[Feishu] Failed to fetch bot names for %s", bot_ids, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 3988 | technical/protocol line | logger.warning("[Feishu] Failed to fetch parent message %s: [%s] %s", message_id, code, msg) |
| feishu | gateway\platforms\feishu.py | 4004 | technical/protocol line | logger.warning("[Feishu] Failed to fetch parent message %s", message_id, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 4037 | technical/protocol line | logger.exception("[Feishu] Background inbound processing failed") |
| feishu | gateway\platforms\feishu.py | 4048 | technical/protocol line | chat_id = getattr(message, "chat_id", "") or "" |
| feishu | gateway\platforms\feishu.py | 4072 | technical/protocol line | getattr(sender, "sender_id", None), chat_id, is_bot=is_bot, |
| feishu | gateway\platforms\feishu.py | 4096 | technical/protocol line | sender_user_id = getattr(sender_id, "user_id", None) |
| feishu | gateway\platforms\feishu.py | 4155 | technical/protocol line | mention_user_id = (getattr(mention_id, "user_id", None) or "").strip() |
| feishu | gateway\platforms\feishu.py | 4216 | technical/protocol line | "[Feishu] FEISHU_BOT_OPEN_ID is stale; using /bot/v3/info open_id for group @mention gating." |
| feishu | gateway\platforms\feishu.py | 4222 | technical/protocol line | "[Feishu] FEISHU_BOT_NAME differs from /bot/v3/info; using hydrated bot name for group @mention gating." |
| feishu | gateway\platforms\feishu.py | 4227 | technical/protocol line | "[Feishu] /bot/v3/info probe failed during hydration", |
| feishu | gateway\platforms\feishu.py | 4243 | technical/protocol line | "[Feishu] Unable to hydrate bot name from application info. " |
| feishu | gateway\platforms\feishu.py | 4253 | technical/protocol line | logger.debug("[Feishu] Failed to hydrate bot name from application info", exc_info=True) |
| feishu | gateway\platforms\feishu.py | 4265 | technical/protocol line | logger.warning("[Feishu] Failed to load persisted dedup state from %s", self._dedup_state_path, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 4303 | technical/protocol line | logger.warning("[Feishu] Failed to persist dedup state to %s", self._dedup_state_path, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 4405 | technical/protocol line | logger.error("[Feishu] Failed to send file %s: %s", file_path, exc, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 4454 | technical/protocol line | receive_id_type = "chat_id" |
| feishu | gateway\platforms\feishu.py | 4487 | technical/protocol line | message_id=self._extract_response_field(response, "message_id"), |
| feishu | gateway\platforms\feishu.py | 4512 | technical/protocol line | "[Feishu] Connect attempt %d/%d failed; retrying in %ds: %s", |
| feishu | gateway\platforms\feishu.py | 4523 | technical/protocol line | domain = FEISHU_DOMAIN if self._domain_name != "lark" else LARK_DOMAIN |
| feishu | gateway\platforms\feishu.py | 4549 | technical/protocol line | domain = FEISHU_DOMAIN if self._domain_name != "lark" else LARK_DOMAIN |
| feishu | gateway\platforms\feishu.py | 4599 | technical/protocol line | "[Feishu] Reply to %s failed in thread %s (code %s — message withdrawn/missing); " |
| feishu | gateway\platforms\feishu.py | 4607 | technical/protocol line | "[Feishu] Reply to %s failed (code %s — message withdrawn/missing); " |
| feishu | gateway\platforms\feishu.py | 4630 | technical/protocol line | "[Feishu] Send attempt %d/%d failed for chat %s; retrying in %ds: %s", |
| feishu | gateway\platforms\feishu.py | 4646 | technical/protocol line | logger.warning("[Feishu] Failed to release app lock: %s", exc, exc_info=True) |
| feishu | gateway\platforms\feishu.py | 4846 | technical/protocol line | return _ONBOARD_ACCOUNTS_URLS.get(domain, _ONBOARD_ACCOUNTS_URLS["feishu"]) |
| feishu | gateway\platforms\feishu.py | 4850 | technical/protocol line | return _ONBOARD_OPEN_URLS.get(domain, _ONBOARD_OPEN_URLS["feishu"]) |
| feishu | gateway\platforms\feishu.py | 4862 | technical/protocol line | req = Request(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"}) |
| feishu | gateway\platforms\feishu.py | 4876 | technical/protocol line | def _init_registration(domain: str = "feishu") -> None: |
| feishu | gateway\platforms\feishu.py | 4886 | technical/protocol line | f"Feishu / Lark registration environment does not support client_secret auth. " |
| feishu | gateway\platforms\feishu.py | 4891 | technical/protocol line | def _begin_registration(domain: str = "feishu") -> dict: |
| feishu | gateway\platforms\feishu.py | 4902 | user-facing output | raise RuntimeError("Feishu / Lark registration did not return a device_code") |
| feishu | gateway\platforms\feishu.py | 4922 | technical/protocol line | domain: str = "feishu", |
| feishu | gateway\platforms\feishu.py | 4955 | technical/protocol line | if tenant_brand == "lark" and not domain_switched: |
| feishu | gateway\platforms\feishu.py | 4956 | technical/protocol line | current_domain = "lark" |
| feishu | gateway\platforms\feishu.py | 4976 | technical/protocol line | logger.warning("[Feishu onboard] Registration %s", error) |
| feishu | gateway\platforms\feishu.py | 4984 | technical/protocol line | logger.warning("[Feishu onboard] Poll timed out after %ds", expire_in) |
| feishu | gateway\platforms\feishu.py | 5023 | technical/protocol line | """Build a lark Client for the given credentials and domain.""" |
| feishu | gateway\platforms\feishu.py | 5024 | technical/protocol line | sdk_domain = LARK_DOMAIN if domain == "lark" else FEISHU_DOMAIN |
| feishu | gateway\platforms\feishu.py | 5047 | technical/protocol line | """Probe bot info using lark_oapi SDK.""" |
| feishu | gateway\platforms\feishu.py | 5063 | technical/protocol line | logger.debug("[Feishu onboard] SDK probe failed: %s", exc) |
| feishu | gateway\platforms\feishu.py | 5068 | technical/protocol line | """Fallback probe using raw HTTP (when lark_oapi is not installed).""" |
| feishu | gateway\platforms\feishu.py | 5075 | technical/protocol line | headers={"Content-Type": "application/json"}, |
| feishu | gateway\platforms\feishu.py | 5087 | technical/protocol line | "Authorization": f"Bearer {access_token}", |
| feishu | gateway\platforms\feishu.py | 5088 | technical/protocol line | "Content-Type": "application/json", |
| feishu | gateway\platforms\feishu.py | 5096 | technical/protocol line | logger.debug("[Feishu onboard] HTTP probe failed: %s", exc) |
| feishu | gateway\platforms\feishu.py | 5102 | technical/protocol line | initial_domain: str = "feishu", |
| feishu | gateway\platforms\feishu.py | 5112 | technical/protocol line | "domain": "feishu" \| "lark", |
| feishu | gateway\platforms\feishu.py | 5124 | technical/protocol line | logger.warning("[Feishu onboard] Registration failed: %s", exc) |
| feishu | gateway\platforms\feishu.py | 5134 | user-facing output | print(" 正在连接 Feishu / Lark...", end="", flush=True) |
| feishu | gateway\platforms\feishu.py | 5142 | user-facing output | print(f"\n 扫描上方二维码，或直接打开这个 URL:\n {qr_url}") |
| feishu | gateway\platforms\feishu.py | 5144 | user-facing output | print(f" 在手机 Feishu / Lark 中打开这个 URL:\n\n {qr_url}\n") |
| feishu | gateway\runtime_footer.py | 16 | technical/protocol line | Users can toggle the global setting with ``/footer on\|off`` from both the CLI |
| feishu | gateway\runtime_footer.py | 33 | technical/protocol line | _DEFAULT_FIELDS: tuple[str, ...] = ("model", "context_pct", "cwd") |
| feishu | gateway\runtime_footer.py | 39 | technical/protocol line | for key in ("HOME", "USERPROFILE"): |
| feishu | gateway\runtime_footer.py | 43 | technical/protocol line | home_drive = os.environ.get("HOMEDRIVE", "").strip() |
| feishu | gateway\runtime_footer.py | 44 | technical/protocol line | home_path = os.environ.get("HOMEPATH", "").strip() |
| feishu | gateway\runtime_footer.py | 54 | technical/protocol line | """Return *cwd* with ``$HOME`` collapsed to ``~``. Empty string if unset.""" |
| feishu | gateway\runtime_footer.py | 79 | technical/protocol line | """Drop ``vendor/`` prefix for readability (``openai/gpt-5.4`` → ``gpt-5.4``).""" |
| feishu | gateway\runtime_footer.py | 165 | technical/protocol line | if field == "model": |
| feishu | gateway\runtime_footer.py | 169 | technical/protocol line | elif field == "provider": |
| feishu | gateway\runtime_footer.py | 178 | technical/protocol line | rel = _home_relative_cwd(cwd or os.environ.get("TERMINAL_CWD", "")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 1 | technical/protocol line | """Hermes tools backed by the local lark-cli executable.""" |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 13 | technical/protocol line | TOOLSET = "lark_cli" |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 19 | technical/protocol line | configured = os.getenv("LARK_CLI_BIN") |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 22 | technical/protocol line | shutil.which("lark-cli.cmd"), |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 23 | technical/protocol line | shutil.which("lark-cli.exe"), |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 24 | technical/protocol line | shutil.which("lark-cli"), |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 25 | technical/protocol line | shutil.which("lark-cli.ps1"), |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 26 | technical/protocol line | r"G:\AI\npm-global\lark-cli.cmd", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 27 | technical/protocol line | r"G:\AI\npm-global\lark-cli.ps1", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 42 | user-facing output | raise RuntimeError("未找到 lark-cli。请安装 @larksuite/cli，或设置 LARK_CLI_BIN。") |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 189 | technical/protocol line | _add(options, "--chat-id", _value(args, "chat_id")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 211 | technical/protocol line | _add(options, "--chat-id", _value(args, "chat_id")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 212 | technical/protocol line | _add(options, "--user-id", _value(args, "user_id")) |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 278 | technical/protocol line | TEXT = {"type": "string"} |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 279 | literal display field | IDENTITY = {"type": "string", "enum": ["user", "bot"], "description": "使用的飞书身份。"} |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 280 | technical/protocol line | BOOL = {"type": "boolean"} |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 281 | technical/protocol line | INT = {"type": "integer"} |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 287 | mixed technical/protocol line | "检查 lark-cli 安装、绑定和登录状态。", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 295 | technical/protocol line | {"query": TEXT, "page_size": INT, "page_token": TEXT, "filter": {"type": "object"}, "identity": IDENTITY}, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 301 | mixed technical/protocol line | "按 URL 或 token 获取飞书文档内容。", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 302 | technical/protocol line | {"doc": TEXT, "api_version": {"type": "string", "enum": ["v1", "v2"]}, "limit": INT, "offset": INT, "identity": IDENTITY}, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 309 | technical/protocol line | {"file_token": TEXT, "output": TEXT, "overwrite": BOOL, "identity": IDENTITY}, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 316 | technical/protocol line | {"name": TEXT, "content": TEXT, "file": TEXT, "folder_token": TEXT, "dry_run": BOOL, "identity": IDENTITY}, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 323 | technical/protocol line | {"query": TEXT, "chat_id": TEXT, "chat_type": TEXT, "sender": TEXT, "sender_type": TEXT, "start": TEXT, "end": TEXT, "page_size": INT, "page_all": BOOL, "is_at_me": BOOL}, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 330 | technical/protocol line | {"message_ids": TEXT, "identity": IDENTITY}, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 337 | technical/protocol line | {"chat_id": TEXT, "user_id": TEXT, "start": TEXT, "end": TEXT, "sort": {"type": "string", "enum": ["asc", "desc"]}, "page_size": INT, "page_token": TEXT, "identity": IDENTITY}, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 344 | technical/protocol line | {"query": TEXT, "created_at": TEXT, "due_start": TEXT, "due_end": TEXT, "complete": BOOL, "page_all": BOOL}, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 351 | technical/protocol line | {"summary": TEXT, "description": TEXT, "due": TEXT, "assignee": TEXT, "follower": TEXT, "tasklist_id": TEXT, "idempotency_key": TEXT, "dry_run": BOOL, "identity": IDENTITY}, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 358 | technical/protocol line | {"calendar_id": TEXT, "start": TEXT, "end": TEXT, "identity": IDENTITY}, |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 364 | mixed technical/protocol line | "使用 lark-cli LiteQuery DSL 查询飞书多维表格。", |
| lark-cli | $HERMES_HOME\plugins\lark-cli-toolbox\__init__.py | 365 | technical/protocol line | {"base_token": TEXT, "dsl": TEXT, "identity": IDENTITY}, |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 1 | technical/protocol line | import { STARTUP_IMAGE, STARTUP_QUERY } from '../config/env.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 2 | technical/protocol line | import { STREAM_BATCH_MS } from '../config/timing.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 3 | technical/protocol line | import { buildSetupRequiredSections, SETUP_REQUIRED_TITLE } from '../content/setup.js' |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 114 | technical/protocol line | session_id: sessionId ?? 'default', |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 193 | technical/protocol line | await rpc('image.attach', { path: STARTUP_IMAGE, session_id: sid }) |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 246 | technical/protocol line | // forging a brand-new one. Mirrors classic CLI's `hermes -c` / |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 286 | technical/protocol line | if (ev.session_id && sid && ev.session_id !== sid && !ev.type.startsWith('gateway.')) { |
| tui | ui-tui\src\app\createGatewayEventHandler.ts | 477 | TUI status/output | turnController.pushActivity(line.slice(0, STDERR_LINE_CAP), 'error') |
| tui | ui-tui\src\app\createSlashHandler.ts | 77 | technical/protocol line | gw.request<SlashExecResponse>('slash.exec', { command: cmd.slice(1), session_id: sid }) |
| tui | ui-tui\src\app\createSlashHandler.ts | 90 | technical/protocol line | gw.request('command.dispatch', { arg: parsed.arg, name: parsed.name, session_id: sid }) |
| tui | ui-tui\src\app\delegationStore.ts | 6 | technical/protocol line | // Last known caps from `delegation.status` RPC. null until fetched. |
| tui | ui-tui\src\app\interfaces.ts | 38 | technical/protocol line | export const INDICATOR_STYLES = ['ascii', 'emoji', 'kaomoji', 'unicode'] as const |
| tui | ui-tui\src\app\interfaces.ts | 40 | technical/protocol line | export const DEFAULT_INDICATOR_STYLE: IndicatorStyle = 'kaomoji' |
| tui | ui-tui\src\app\slash\commands\core.ts | 3 | technical/protocol line | import { NO_CONFIRM_DESTRUCTIVE } from '../../../config/env.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 5 | technical/protocol line | import { HOTKEYS } from '../../../content/hotkeys.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 6 | technical/protocol line | import { isSectionName, nextDetailsMode, parseDetailsMode, SECTION_NAMES } from '../../../domain/details.js' |
| tui | ui-tui\src\app\slash\commands\core.ts | 47 | technical/protocol line | const RESET_WORDS = new Set(['reset', 'clear', 'default']) |
| tui | ui-tui\src\app\slash\commands\core.ts | 48 | technical/protocol line | const CYCLE_WORDS = new Set(['cycle', 'toggle']) |
| tui | ui-tui\src\app\slash\commands\core.ts | 53 | mixed technical/protocol line | const DETAILS_SECTION_USAGE = '用法: /details <section> [hidden\|collapsed\|expanded\|reset]' |
| tui | ui-tui\src\app\slash\commands\core.ts | 75 | user-facing field | name: 'help', |
| tui | ui-tui\src\app\slash\commands\core.ts | 96 | user-facing field | title: 'TUI' |
| tui | ui-tui\src\app\slash\commands\core.ts | 108 | user-facing field | name: 'quit', |
| tui | ui-tui\src\app\slash\commands\core.ts | 113 | user-facing field | help: '更新 Hermes Agent 到最新版（会退出 TUI）', |
| tui | ui-tui\src\app\slash\commands\core.ts | 114 | user-facing field | name: 'update', |
| tui | ui-tui\src\app\slash\commands\core.ts | 116 | TUI status/output | ctx.transcript.sys('正在退出 TUI 并运行更新...') |
| tui | ui-tui\src\app\slash\commands\core.ts | 126 | user-facing field | name: 'mouse', |
| tui | ui-tui\src\app\slash\commands\core.ts | 145 | user-facing field | name: 'clear', |
| tui | ui-tui\src\app\slash\commands\core.ts | 178 | user-facing field | name: 'redraw', |
| tui | ui-tui\src\app\slash\commands\core.ts | 187 | user-facing field | name: 'status', |
| tui | ui-tui\src\app\slash\commands\core.ts | 194 | technical/protocol line | .rpc<SessionStatusResponse>('session.status', { session_id: ctx.sid }) |
| tui | ui-tui\src\app\slash\commands\core.ts | 202 | user-facing field | name: 'resume', |
| tui | ui-tui\src\app\slash\commands\core.ts | 214 | user-facing field | name: 'title', |
| tui | ui-tui\src\app\slash\commands\core.ts | 224 | technical/protocol line | .rpc<SessionTitleResponse>('session.title', { session_id: ctx.sid }) |
| tui | ui-tui\src\app\slash\commands\core.ts | 241 | technical/protocol line | .rpc<SessionTitleResponse>('session.title', { session_id: ctx.sid, title }) |
| tui | ui-tui\src\app\slash\commands\core.ts | 255 | user-facing field | name: 'compact', |
| tui | ui-tui\src\app\slash\commands\core.ts | 273 | user-facing field | name: 'details', |
| tui | ui-tui\src\app\slash\commands\core.ts | 336 | user-facing field | name: 'fortune', |
| tui | ui-tui\src\app\slash\commands\core.ts | 354 | user-facing field | name: 'copy', |
| tui | ui-tui\src\app\slash\commands\core.ts | 365 | mixed technical/protocol line | '剪贴板复制失败 — 可尝试 HERMES_TUI_FORCE_OSC52=1 强制使用转义序列；HERMES_TUI_DEBUG_CLIPBOARD=1 查看详情' |
| tui | ui-tui\src\app\slash\commands\core.ts | 391 | TUI status/output | sys('已发送 OSC52 复制序列（需要终端支持）') |
| tui | ui-tui\src\app\slash\commands\core.ts | 404 | user-facing field | name: 'paste', |
| tui | ui-tui\src\app\slash\commands\core.ts | 409 | user-facing field | help: '配置 IDE 终端快捷键（多行 + 撤销/重做）', |
| tui | ui-tui\src\app\slash\commands\core.ts | 410 | user-facing field | name: 'terminal-setup', |
| tui | ui-tui\src\app\slash\commands\core.ts | 432 | TUI status/output | ctx.transcript.sys('请重启 IDE 终端，让新的快捷键生效') |
| tui | ui-tui\src\app\slash\commands\core.ts | 445 | user-facing field | name: 'logs', |
| tui | ui-tui\src\app\slash\commands\core.ts | 455 | user-facing field | name: 'history', |
| tui | ui-tui\src\app\slash\commands\core.ts | 457 | technical/protocol line | // The CLI-side `/history` runs in a detached slash-worker subprocess |
| tui | ui-tui\src\app\slash\commands\core.ts | 482 | user-facing field | help: '把当前对话记录保存为 JSON', |
| tui | ui-tui\src\app\slash\commands\core.ts | 483 | user-facing field | name: 'save', |
| tui | ui-tui\src\app\slash\commands\core.ts | 498 | technical/protocol line | .rpc<SessionSaveResponse>('session.save', { session_id: ctx.sid }) |
| tui | ui-tui\src\app\slash\commands\core.ts | 517 | user-facing field | name: 'statusbar', |
| tui | ui-tui\src\app\slash\commands\core.ts | 544 | user-facing field | name: 'queue', |
| tui | ui-tui\src\app\slash\commands\core.ts | 557 | user-facing field | name: 'steer', |
| tui | ui-tui\src\app\slash\commands\core.ts | 595 | user-facing field | name: 'undo', |
| tui | ui-tui\src\app\slash\commands\core.ts | 601 | technical/protocol line | ctx.gateway.rpc<SessionUndoResponse>('session.undo', { session_id: ctx.sid }).then( |
| tui | ui-tui\src\app\slash\commands\core.ts | 616 | user-facing field | name: 'retry', |
| tui | ui-tui\src\app\slash\commands\core.ts | 628 | technical/protocol line | ctx.gateway.rpc<SessionUndoResponse>('session.undo', { session_id: ctx.sid }).then( |
| tui | ui-tui\src\app\slash\commands\debug.ts | 6 | user-facing field | help: '写入 V8 堆快照和内存诊断（见 HERMES_HEAPDUMP_DIR）', |
| tui | ui-tui\src\app\slash\commands\debug.ts | 7 | user-facing field | name: 'heapdump', |
| tui | ui-tui\src\app\slash\commands\debug.ts | 30 | user-facing field | name: 'mem', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 67 | user-facing field | name: 'stop', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 83 | user-facing field | help: '重新加载当前会话的 MCP 服务（会提示缓存影响）', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 84 | user-facing field | name: 'reload-mcp', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 110 | mixed technical/protocol line | ? 'MCP 服务已重载 · 以后 /reload-mcp 不再需要确认' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 111 | mixed technical/protocol line | : 'MCP 服务已重载' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 123 | user-facing field | help: '把 ~/.hermes/.env 重新加载到当前网关（CLI 一致）', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 124 | user-facing field | name: 'reload', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 139 | user-facing field | help: '管理浏览器 CDP 连接 [connect\|disconnect\|status]', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 140 | user-facing field | name: 'browser', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 152 | technical/protocol line | const url = action === 'connect' ? rest.join(' ').trim() \|\| 'http://127.0.0.1:9222' : undefined |
| tui | ui-tui\src\app\slash\commands\ops.ts | 159 | technical/protocol line | .rpc<BrowserManageResponse>('browser.manage', { action, session_id: sid, ...(url && { url }) }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 181 | TUI status/output | ctx.transcript.sys('已通过 CDP 连接到正在运行的 Chromium 系浏览器') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 183 | TUI status/output | ctx.transcript.sys('下一次浏览器工具调用会使用这个 CDP 端点') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 193 | user-facing field | name: 'rollback', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 205 | technical/protocol line | .rpc<RollbackListResponse>('rollback.list', { session_id: ctx.sid }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 239 | technical/protocol line | .rpc<RollbackDiffResponse>('rollback.diff', { hash, session_id: ctx.sid }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 286 | user-facing field | name: 'agents', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 290 | technical/protocol line | // Stay compatible with the gateway `/agents [pause\|resume\|status]` CLI — |
| tui | ui-tui\src\app\slash\commands\ops.ts | 321 | user-facing field | name: 'replay', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 332 | technical/protocol line | session_id: ctx.sid ?? 'default' |
| tui | ui-tui\src\app\slash\commands\ops.ts | 407 | user-facing field | name: 'replay-diff', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 442 | user-facing field | help: '让当前 TUI 网关重新扫描已安装技能', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 443 | user-facing field | name: 'reload-skills', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 476 | user-facing field | name: 'skills', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 490 | technical/protocol line | .request<SlashExecResponse>('slash.exec', { command: cmd.slice(1), session_id: ctx.sid }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 584 | TUI status/output | return sys('用法: /skills install <名称或 URL>') |
| tui | ui-tui\src\app\slash\commands\ops.ts | 654 | user-facing field | name: 'tools', |
| tui | ui-tui\src\app\slash\commands\ops.ts | 660 | technical/protocol line | .request<SlashExecResponse>('slash.exec', { command: cmd.slice(1), session_id: ctx.sid }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 680 | TUI status/output | ctx.transcript.sys(`MCP 工具: /tools ${subcommand} github:create_issue`) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 686 | technical/protocol line | .rpc<ToolsConfigureResponse>('tools.configure', { action: subcommand, names, session_id: ctx.sid }) |
| tui | ui-tui\src\app\slash\commands\ops.ts | 703 | TUI status/output | ctx.transcript.sys(`缺少 MCP 服务: ${r.missing_servers.join(', ')}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 2 | technical/protocol line | import { TUI_SESSION_MODEL_FLAG } from '../../../domain/slash.js' |
| tui | ui-tui\src\app\slash\commands\session.ts | 16 | technical/protocol line | import { DEFAULT_INDICATOR_STYLE, INDICATOR_STYLES, type IndicatorStyle } from '../../interfaces.js' |
| tui | ui-tui\src\app\slash\commands\session.ts | 21 | technical/protocol line | const TUI_SESSION_MODEL_RE = new RegExp(`(?:^\|\\s)${TUI_SESSION_MODEL_FLAG}(?:\\s\|$)`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 22 | technical/protocol line | const TUI_SESSION_STRIP_RE = new RegExp(`\\s*${TUI_SESSION_MODEL_FLAG}\\b\\s*`, 'g') |
| tui | ui-tui\src\app\slash\commands\session.ts | 24 | technical/protocol line | const stripTuiSessionFlag = (trimmed: string) => trimmed.replace(TUI_SESSION_STRIP_RE, ' ').replace(/\s+/g, ' ').trim() |
| tui | ui-tui\src\app\slash\commands\session.ts | 52 | user-facing field | name: 'background', |
| tui | ui-tui\src\app\slash\commands\session.ts | 73 | user-facing field | name: 'model', |
| tui | ui-tui\src\app\slash\commands\session.ts | 84 | technical/protocol line | .rpc<ConfigSetResponse>('config.set', { key: 'model', session_id: ctx.sid, value: modelValueForConfigSet(arg) }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 105 | user-facing field | name: 'sessions', |
| tui | ui-tui\src\app\slash\commands\session.ts | 118 | user-facing field | name: 'image', |
| tui | ui-tui\src\app\slash\commands\session.ts | 120 | technical/protocol line | ctx.gateway.rpc<ImageAttachResponse>('image.attach', { path: arg, session_id: ctx.sid }).then( |
| tui | ui-tui\src\app\slash\commands\session.ts | 134 | user-facing field | name: 'personality', |
| tui | ui-tui\src\app\slash\commands\session.ts | 140 | technical/protocol line | ctx.gateway.rpc<ConfigSetResponse>('config.set', { key: 'personality', session_id: ctx.sid, value: arg }).then( |
| tui | ui-tui\src\app\slash\commands\session.ts | 155 | user-facing field | name: 'compress', |
| tui | ui-tui\src\app\slash\commands\session.ts | 210 | user-facing field | name: 'branch', |
| tui | ui-tui\src\app\slash\commands\session.ts | 214 | technical/protocol line | ctx.gateway.rpc<SessionBranchResponse>('session.branch', { name: arg, session_id: ctx.sid }).then( |
| tui | ui-tui\src\app\slash\commands\session.ts | 232 | user-facing field | name: 'voice', |
| tui | ui-tui\src\app\slash\commands\session.ts | 251 | technical/protocol line | // backend response WITHOUT updating the frontend ``voice.recordKey`` |
| tui | ui-tui\src\app\slash\commands\session.ts | 275 | TUI status/output | ctx.transcript.sys(` TTS: ${onOffLabel(r.tts)}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 278 | technical/protocol line | // CLI's "Requirements:" block — surfaces STT/audio setup issues |
| tui | ui-tui\src\app\slash\commands\session.ts | 279 | technical/protocol line | // so the user sees "STT provider: MISSING ..." instead of |
| tui | ui-tui\src\app\slash\commands\session.ts | 296 | TUI status/output | ctx.transcript.sys(`语音 TTS 已${r.tts ? '开启' : '关闭'}。`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 303 | mixed technical/protocol line | const tts = r.tts ? '（TTS 已开启）' : '' |
| tui | ui-tui\src\app\slash\commands\session.ts | 318 | user-facing field | name: 'skin', |
| tui | ui-tui\src\app\slash\commands\session.ts | 334 | user-facing field | name: 'indicator', |
| tui | ui-tui\src\app\slash\commands\session.ts | 335 | technical/protocol line | usage: `/indicator [${INDICATOR_STYLES.join('\|')}]`, |
| tui | ui-tui\src\app\slash\commands\session.ts | 344 | TUI status/output | ctx.transcript.sys(`指示器: ${r.value \|\| DEFAULT_INDICATOR_STYLE}`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 350 | TUI status/output | return ctx.transcript.sys(`用法: /indicator [${INDICATOR_STYLES.join('\|')}]`) |
| tui | ui-tui\src\app\slash\commands\session.ts | 371 | user-facing field | name: 'yolo', |
| tui | ui-tui\src\app\slash\commands\session.ts | 374 | technical/protocol line | .rpc<ConfigSetResponse>('config.set', { key: 'yolo', session_id: ctx.sid }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 381 | user-facing field | name: 'reasoning', |
| tui | ui-tui\src\app\slash\commands\session.ts | 396 | technical/protocol line | .rpc<ConfigSetResponse>('config.set', { key: 'reasoning', session_id: ctx.sid, value: arg }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 425 | user-facing field | name: 'fast', |
| tui | ui-tui\src\app\slash\commands\session.ts | 436 | technical/protocol line | .rpc<ConfigGetValueResponse>('config.get', { key: 'fast', session_id: ctx.sid }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 446 | technical/protocol line | .rpc<ConfigSetResponse>('config.set', { key: 'fast', session_id: ctx.sid, value: mode }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 469 | user-facing field | name: 'busy', |
| tui | ui-tui\src\app\slash\commands\session.ts | 506 | user-facing field | name: 'verbose', |
| tui | ui-tui\src\app\slash\commands\session.ts | 509 | technical/protocol line | .rpc<ConfigSetResponse>('config.set', { key: 'verbose', session_id: ctx.sid, value: arg \|\| 'cycle' }) |
| tui | ui-tui\src\app\slash\commands\session.ts | 516 | user-facing field | name: 'usage', |
| tui | ui-tui\src\app\slash\commands\session.ts | 518 | technical/protocol line | ctx.gateway.rpc<SessionUsageResponse>('session.usage', { session_id: ctx.sid }).then(r => { |
| tui | ui-tui\src\app\slash\commands\session.ts | 530 | TUI status/output | return ctx.transcript.sys('还没有 API 调用') |
| tui | ui-tui\src\app\slash\commands\session.ts | 537 | mixed technical/protocol line | ['模型', r.model ?? ''], |
| tui | ui-tui\src\app\slash\commands\session.ts | 543 | mixed technical/protocol line | ['API 调用', f(r.calls)] |
| tui | ui-tui\src\app\slash\commands\setup.ts | 10 | user-facing field | name: 'setup', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 16 | technical/protocol line | defaultSlot: 'status.left', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 17 | technical/protocol line | id: 'activityScan', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 18 | user-facing field | label: 'activity-scan', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 19 | technical/protocol line | surface: 'status' |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 22 | technical/protocol line | defaultSlot: 'intro.hero', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 23 | technical/protocol line | id: 'characterPanel', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 24 | user-facing field | label: 'character-panel', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 25 | technical/protocol line | surface: 'future' |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 28 | technical/protocol line | defaultSlot: 'composer.dock', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 29 | technical/protocol line | id: 'monitorPanel', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 30 | user-facing field | label: 'monitor-panel', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 31 | technical/protocol line | surface: 'dock' |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 34 | technical/protocol line | defaultSlot: 'status.center', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 35 | technical/protocol line | id: 'statusMeter', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 36 | user-facing field | label: 'status-meter', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 37 | technical/protocol line | surface: 'status' |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 40 | technical/protocol line | defaultSlot: 'transcript.afterUser', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 41 | technical/protocol line | id: 'taskPanel', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 42 | user-facing field | label: 'task-panel', |
| tui | ui-tui\src\app\tuiModuleRegistry.ts | 43 | technical/protocol line | surface: 'inline' |
| tui | ui-tui\src\app\tuiModules.ts | 27 | technical/protocol line | compact: 'auto', |
| tui | ui-tui\src\app\tuiModules.ts | 30 | technical/protocol line | position: 'status', |
| tui | ui-tui\src\app\tuiModules.ts | 32 | technical/protocol line | slot: 'status.left' |
| tui | ui-tui\src\app\tuiModules.ts | 35 | technical/protocol line | compact: 'auto', |
| tui | ui-tui\src\app\tuiModules.ts | 38 | technical/protocol line | position: 'top', |
| tui | ui-tui\src\app\tuiModules.ts | 40 | technical/protocol line | slot: 'intro.hero' |
| tui | ui-tui\src\app\tuiModules.ts | 43 | technical/protocol line | compact: 'auto', |
| tui | ui-tui\src\app\tuiModules.ts | 46 | technical/protocol line | position: 'bottom', |
| tui | ui-tui\src\app\tuiModules.ts | 48 | technical/protocol line | slot: 'composer.dock' |
| tui | ui-tui\src\app\tuiModules.ts | 51 | technical/protocol line | compact: 'auto', |
| tui | ui-tui\src\app\tuiModules.ts | 54 | technical/protocol line | position: 'status', |
| tui | ui-tui\src\app\tuiModules.ts | 56 | technical/protocol line | slot: 'status.center' |
| tui | ui-tui\src\app\tuiModules.ts | 59 | technical/protocol line | compact: 'auto', |
| tui | ui-tui\src\app\tuiModules.ts | 62 | technical/protocol line | position: 'bottom', |
| tui | ui-tui\src\app\tuiModules.ts | 64 | technical/protocol line | slot: 'transcript.afterUser' |
| tui | ui-tui\src\app\tuiModules.ts | 69 | technical/protocol line | activityScan: 'activityScan', |
| tui | ui-tui\src\app\tuiModules.ts | 70 | technical/protocol line | activity_scan: 'activityScan', |
| tui | ui-tui\src\app\tuiModules.ts | 72 | technical/protocol line | characterPanel: 'characterPanel', |
| tui | ui-tui\src\app\tuiModules.ts | 73 | technical/protocol line | character_panel: 'characterPanel', |
| tui | ui-tui\src\app\tuiModules.ts | 75 | technical/protocol line | monitorPanel: 'monitorPanel', |
| tui | ui-tui\src\app\tuiModules.ts | 76 | technical/protocol line | monitor_panel: 'monitorPanel', |
| tui | ui-tui\src\app\tuiModules.ts | 78 | technical/protocol line | statusMeter: 'statusMeter', |
| tui | ui-tui\src\app\tuiModules.ts | 79 | technical/protocol line | status_meter: 'statusMeter', |
| tui | ui-tui\src\app\tuiModules.ts | 81 | technical/protocol line | taskPanel: 'taskPanel', |
| tui | ui-tui\src\app\tuiModules.ts | 82 | technical/protocol line | task_panel: 'taskPanel', |
| tui | ui-tui\src\app\tuiModules.ts | 86 | technical/protocol line | const POSITIONS = new Set<TuiModulePosition>(['auto', 'bottom', 'side', 'status', 'top']) |
| tui | ui-tui\src\app\tuiSlots.ts | 17 | technical/protocol line | typeof value === 'string' && TUI_SLOT_SET.has(value) |
| tui | ui-tui\src\app\turnController.ts | 186 | technical/protocol line | gw.request<SessionInterruptResponse>('session.interrupt', { session_id: sid }).catch(() => {}) |
| tui | ui-tui\src\app\turnController.ts | 212 | technical/protocol line | role: 'assistant', |
| tui | ui-tui\src\app\turnController.ts | 246 | technical/protocol line | kind: 'trail', |
| tui | ui-tui\src\app\turnController.ts | 247 | technical/protocol line | role: 'system', |
| tui | ui-tui\src\app\turnController.ts | 336 | technical/protocol line | kind: 'trail', |
| tui | ui-tui\src\app\turnController.ts | 337 | technical/protocol line | role: 'system', |
| tui | ui-tui\src\app\turnController.ts | 437 | technical/protocol line | // `display.final_response_markdown: render` because raw ANSI escapes |
| tui | ui-tui\src\app\turnController.ts | 477 | technical/protocol line | kind: 'trail', |
| tui | ui-tui\src\app\turnController.ts | 478 | technical/protocol line | role: 'system', |
| tui | ui-tui\src\app\turnController.ts | 534 | technical/protocol line | // the entire buffer with `rendered` (an *incremental* Rich ANSI |
| tui | ui-tui\src\app\turnController.ts | 790 | user-facing field | status: 'running', |
| tui | ui-tui\src\app\turnStore.ts | 55 | technical/protocol line | kind: 'trail', |
| tui | ui-tui\src\app\turnStore.ts | 56 | technical/protocol line | role: 'system', |
| tui | ui-tui\src\app\uiStore.ts | 3 | technical/protocol line | import { MOUSE_TRACKING } from '../config/env.js' |
| tui | ui-tui\src\app\uiStore.ts | 4 | technical/protocol line | import { ZERO } from '../domain/usage.js' |
| tui | ui-tui\src\app\uiStore.ts | 5 | technical/protocol line | import { DEFAULT_THEME } from '../theme.js' |
| tui | ui-tui\src\app\uiStore.ts | 7 | technical/protocol line | import { DEFAULT_INDICATOR_STYLE, type UiState } from './interfaces.js' |
| tui | ui-tui\src\app\uiStore.ts | 13 | technical/protocol line | busyInputMode: 'queue', |
| tui | ui-tui\src\app\uiStore.ts | 15 | technical/protocol line | detailsMode: 'collapsed', |
| tui | ui-tui\src\app\uiStore.ts | 26 | technical/protocol line | statusBar: 'top', |
| tui | ui-tui\src\app\useComposerState.ts | 11 | technical/protocol line | import { LARGE_PASTE } from '../config/limits.js' |
| tui | ui-tui\src\app\useConfigSync.ts | 29 | technical/protocol line | bottom: 'bottom', |
| tui | ui-tui\src\app\useConfigSync.ts | 30 | technical/protocol line | off: 'off', |
| tui | ui-tui\src\app\useConfigSync.ts | 31 | technical/protocol line | on: 'top', |
| tui | ui-tui\src\app\useConfigSync.ts | 32 | technical/protocol line | top: 'top' |
| tui | ui-tui\src\app\useConfigSync.ts | 36 | technical/protocol line | raw === false ? 'off' : typeof raw === 'string' ? (STATUSBAR_ALIAS[raw.trim().toLowerCase()] ?? 'top') : 'top' |
| tui | ui-tui\src\app\useConfigSync.ts | 38 | technical/protocol line | const BUSY_MODES = new Set<BusyInputMode>(['interrupt', 'queue', 'steer']) |
| tui | ui-tui\src\app\useConfigSync.ts | 40 | technical/protocol line | // TUI defaults to `queue` even though the framework default |
| tui | ui-tui\src\app\useConfigSync.ts | 45 | technical/protocol line | // opt out per-config; CLI / messaging adapters keep their `interrupt` |
| tui | ui-tui\src\app\useConfigSync.ts | 47 | technical/protocol line | const TUI_BUSY_DEFAULT: BusyInputMode = 'queue' |
| tui | ui-tui\src\app\useConfigSync.ts | 71 | technical/protocol line | const FALSEY_MOUSE = new Set(['0', 'false', 'no', 'off']) |
| tui | ui-tui\src\app\useConfigSync.ts | 81 | technical/protocol line | return typeof raw === 'string' ? !FALSEY_MOUSE.has(raw.trim().toLowerCase()) : true |
| tui | ui-tui\src\app\useConfigSync.ts | 208 | technical/protocol line | quietRpc<ReloadMcpResponse>(gw, 'reload.mcp', { session_id: sid, confirm: true }).then( |
| tui | ui-tui\src\app\useConfigSync.ts | 209 | TUI status/output | r => r && turnController.pushActivity('MCP reloaded after config change') |
| tui | ui-tui\src\app\useInputHandlers.ts | 5 | technical/protocol line | import { TYPING_IDLE_MS } from '../config/timing.js' |
| tui | ui-tui\src\app\useInputHandlers.ts | 130 | technical/protocol line | .rpc<ApprovalRespondResponse>('approval.respond', { choice: 'deny', session_id: getUiState().sid }) |
| tui | ui-tui\src\app\useInputHandlers.ts | 243 | technical/protocol line | .rpc<VoiceRecordResponse>('voice.record', { action, session_id: getUiState().sid }) |
| tui | ui-tui\src\app\useInputHandlers.ts | 404 | technical/protocol line | // `delta < innerHeight` DECSTBM fast-path threshold. |
| tui | ui-tui\src\app\useInputHandlers.ts | 515 | technical/protocol line | // primary keystroke to "Find Next" before the TUI sees it; Alt+G |
| tui | ui-tui\src\app\useInputHandlers.ts | 531 | technical/protocol line | return void gateway.rpc<ConfigSetResponse>('config.set', { key: 'yolo', session_id: live.sid }).then(r => { |
| tui | ui-tui\src\app\useLongRunToolCharms.ts | 3 | technical/protocol line | import { LONG_RUN_CHARMS } from '../content/charms.js' |
| tui | ui-tui\src\app\useLongRunToolCharms.ts | 59 | mixed technical/protocol line | `${pick(LONG_RUN_CHARMS)} (${toolTrailLabel(tool.name)} · ${Math.round((now - tool.startedAt) / 1000)} 秒)` |
| tui | ui-tui\src\app\useMainApp.ts | 5 | technical/protocol line | import { STARTUP_RESUME_ID } from '../config/env.js' |
| tui | ui-tui\src\app\useMainApp.ts | 6 | technical/protocol line | import { MAX_HISTORY, WHEEL_SCROLL_STEP } from '../config/limits.js' |
| tui | ui-tui\src\app\useMainApp.ts | 7 | technical/protocol line | import { SECTION_NAMES, sectionMode } from '../domain/details.js' |
| tui | ui-tui\src\app\useMainApp.ts | 21 | technical/protocol line | import { DEFAULT_VOICE_RECORD_KEY, isMac, type ParsedVoiceRecordKey } from '../lib/platform.js' |
| tui | ui-tui\src\app\useMainApp.ts | 54 | technical/protocol line | return items[0]?.kind === 'intro' ? [items[0]!, ...items.slice(-(MAX_HISTORY - 1))] : items.slice(-MAX_HISTORY) |
| tui | ui-tui\src\app\useMainApp.ts | 418 | technical/protocol line | useTerminalTitle(model ? `${marker} ${model}${tabCwd ? ` · ${shortCwd(tabCwd, 24)}` : ''}` : 'Hermes') |
| tui | ui-tui\src\app\useMainApp.ts | 431 | technical/protocol line | void rpc<TerminalResizeResponse>('terminal.resize', { cols: stdout.columns ?? 80, session_id: ui.sid }) |
| tui | ui-tui\src\app\useMainApp.ts | 464 | technical/protocol line | kind: 'trail', |
| tui | ui-tui\src\app\useMainApp.ts | 465 | technical/protocol line | role: 'system', |
| tui | ui-tui\src\app\useMainApp.ts | 483 | technical/protocol line | rpc<ClipboardPasteResponse>('clipboard.paste', { session_id: getUiState().sid }).then(r => { |
| tui | ui-tui\src\app\useMainApp.ts | 689 | technical/protocol line | respondWith('approval.respond', { choice, session_id: ui.sid }, () => { |
| tui | ui-tui\src\app\useMainApp.ts | 727 | technical/protocol line | slashRef.current(`/model ${value}`) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 7 | technical/protocol line | import { buildSetupRequiredSections, SETUP_REQUIRED_TITLE } from '../content/setup.js' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 9 | technical/protocol line | import { ZERO } from '../domain/usage.js' |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 90 | technical/protocol line | targetSid ? rpc<SessionCloseResponse>('session.close', { session_id: targetSid }) : Promise.resolve(null), |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 216 | technical/protocol line | .request<SessionResumeResponse>('session.resume', { cols: colsRef.current, session_id: id }) |
| tui | ui-tui\src\app\useSessionLifecycle.ts | 236 | user-facing field | status: 'ready', |
| tui | ui-tui\src\app\useSubmission.ts | 3 | technical/protocol line | import { TYPING_IDLE_MS } from '../config/timing.js' |
| tui | ui-tui\src\app\useSubmission.ts | 14 | technical/protocol line | import { hasInterpolation, INTERPOLATION_RE } from '../protocol/interpolation.js' |
| tui | ui-tui\src\app\useSubmission.ts | 15 | technical/protocol line | import { PASTE_SNIPPET_RE } from '../protocol/paste.js' |
| tui | ui-tui\src\app\useSubmission.ts | 132 | technical/protocol line | gw.request<InputDetectDropResponse>('input.detect_drop', { session_id: sid, text }) |
| tui | ui-tui\src\app\useSubmission.ts | 218 | technical/protocol line | // Honors `display.busy_input_mode` from config.yaml (CLI parity): |
| tui | ui-tui\src\components\agentsOverlay.tsx | 42 | technical/protocol line | const SORT_ORDER: readonly SortMode[] = ['depth-first', 'tools-desc', 'duration-desc', 'status'] |
| tui | ui-tui\src\components\agentsOverlay.tsx | 43 | technical/protocol line | const FILTER_ORDER: readonly FilterMode[] = ['all', 'running', 'failed', 'leaf'] |
| tui | ui-tui\src\components\agentsOverlay.tsx | 60 | mixed technical/protocol line | 'api calls': 'API 调用', |
| tui | ui-tui\src\components\agentsOverlay.tsx | 467 | technical/protocol line | {item.model ? <Field name="model" t={t} value={item.model} /> : null} |
| tui | ui-tui\src\components\agentsOverlay.tsx | 994 | technical/protocol line | const key = it.model ? it.model.split('/').pop()! : 'inherit' |
| tui | ui-tui\src\components\appChrome.tsx | 11 | technical/protocol line | import { FACES } from '../content/faces.js' |
| tui | ui-tui\src\components\appChrome.tsx | 12 | technical/protocol line | import { VERBS } from '../content/verbs.js' |
| tui | ui-tui\src\components\appChrome.tsx | 27 | technical/protocol line | export const padVerb = (verb: string, width = VERB_PAD_LEN) => `${verb}…`.padEnd(width, ' ') |
| tui | ui-tui\src\components\appChrome.tsx | 290 | mixed technical/protocol line | [shortModelLabel(model), effortLabel(effort), fast ? '快速' : ''].filter(Boolean).join(' ') |
| tui | ui-tui\src\components\appLayout.tsx | 9 | technical/protocol line | import { INLINE_MODE, SHOW_FPS } from '../config/env.js' |
| tui | ui-tui\src\components\appLayout.tsx | 10 | technical/protocol line | import { PLACEHOLDER } from '../content/placeholders.js' |
| tui | ui-tui\src\components\appLayout.tsx | 323 | user-facing field | placeholder={composer.empty ? PLACEHOLDER : ui.busy ? 'Ctrl+C 中断…' : ''} |
| tui | ui-tui\src\components\branding.tsx | 5 | technical/protocol line | import { artWidth, caduceus, CADUCEUS_WIDTH, logo, LOGO_WIDTH } from '../banner.js' |
| tui | ui-tui\src\components\branding.tsx | 321 | user-facing field | title="MCP 服务器" |
| tui | ui-tui\src\components\branding.tsx | 332 | technical/protocol line | {info.mcp_servers?.length ? ` · ${info.mcp_servers.length} MCP` : ''} |
| tui | ui-tui\src\components\fpsOverlay.tsx | 6 | technical/protocol line | import { SHOW_FPS } from '../config/env.js' |
| tui | ui-tui\src\components\helpHint.tsx | 3 | technical/protocol line | import { HOTKEYS } from '../content/hotkeys.js' |
| tui | ui-tui\src\components\markdown.tsx | 6 | technical/protocol line | import { BOX_CLOSE, BOX_OPEN, texToUnicode } from '../lib/mathUnicode.js' |
| tui | ui-tui\src\components\markdown.tsx | 74 | technical/protocol line | const MD_DUNDER_IDENTIFIER_RE = `(?:${MD_IDENTIFIER_RE}__(?!\\w))` |
| tui | ui-tui\src\components\markdown.tsx | 75 | technical/protocol line | const MD_UNDERSCORE_BOLD_RE = `(?<!\\w)__(?!${MD_DUNDER_IDENTIFIER_RE})(.+?)__(?!\\w)` |
| tui | ui-tui\src\components\markdown.tsx | 89 | technical/protocol line | export const MEDIA_LINE_RE = /^\s*[`"']?MEDIA:\s*(\S+?)[`"']?\s*$/ |
| tui | ui-tui\src\components\markdown.tsx | 98 | technical/protocol line | // `thing ~! more ~?` from Kimi / Qwen / GLM (kaomoji-style decorators) |
| tui | ui-tui\src\components\markdown.tsx | 110 | technical/protocol line | `!\\[(.*?)\\]\\(${MD_URL_RE}\\)`, // 1,2 image |
| tui | ui-tui\src\components\markdown.tsx | 111 | technical/protocol line | `\\[(.+?)\\]\\(${MD_URL_RE}\\)`, // 3,4 link |
| tui | ui-tui\src\components\markdown.tsx | 123 | technical/protocol line | `(https?:\\/\\/[^\\s<]+)`, // 16 bare URL — wrapped so it owns its own |
| tui | ui-tui\src\components\markdown.tsx | 374 | technical/protocol line | <Box flexDirection="column" key={k} paddingLeft={TABLE_PADDING_LEFT}> |
| tui | ui-tui\src\components\markdown.tsx | 443 | technical/protocol line | <Box flexDirection="column" key={k} paddingLeft={TABLE_PADDING_LEFT}> |
| tui | ui-tui\src\components\markdown.tsx | 456 | technical/protocol line | <Box flexDirection="column" key={k} paddingLeft={TABLE_PADDING_LEFT}> |
| tui | ui-tui\src\components\markdown.tsx | 480 | technical/protocol line | <Box flexDirection="column" key={k} paddingLeft={TABLE_PADDING_LEFT}> |
| tui | ui-tui\src\components\markdown.tsx | 526 | technical/protocol line | // Code is the one wrap that does NOT recurse — inline `code` spans |
| tui | ui-tui\src\components\markdown.tsx | 577 | technical/protocol line | // so `see https://x.com/, which…` keeps the comma outside the link. |
| tui | ui-tui\src\components\messageLine.tsx | 4 | technical/protocol line | import { LONG_MSG } from '../config/limits.js' |
| tui | ui-tui\src\components\messageLine.tsx | 7 | technical/protocol line | import { ROLE } from '../domain/roles.js' |
| tui | ui-tui\src\components\messageLine.tsx | 52 | technical/protocol line | const systemIsLong = msg.role === 'system' && msg.text.length > SYSTEM_COLLAPSE_CHARS |
| tui | ui-tui\src\components\messageLine.tsx | 154 | technical/protocol line | if (msg.role === 'user' && msg.text.length > LONG_MSG && isPasteBackedText(msg.text)) { |
| tui | ui-tui\src\components\modelPicker.tsx | 5 | technical/protocol line | import { TUI_SESSION_MODEL_FLAG } from '../domain/slash.js' |
| tui | ui-tui\src\components\modelPicker.tsx | 17 | technical/protocol line | type Stage = 'provider' \| 'key' \| 'model' \| 'disconnect' |
| tui | ui-tui\src\components\modelPicker.tsx | 27 | technical/protocol line | const [stage, setStage] = useState<Stage>('provider') |
| tui | ui-tui\src\components\modelPicker.tsx | 34 | technical/protocol line | // to-fit with alignSelf="flex-start") doesn't resize as long provider / |
| tui | ui-tui\src\components\modelPicker.tsx | 35 | technical/protocol line | // model names scroll into view, and so `wrap="truncate-end"` on each row |
| tui | ui-tui\src\components\modelPicker.tsx | 40 | technical/protocol line | gw.request<ModelOptionsResponse>('model.options', sessionId ? { session_id: sessionId } : {}) |
| tui | ui-tui\src\components\modelPicker.tsx | 45 | mixed technical/protocol line | setErr('无效响应: model.options') |
| tui | ui-tui\src\components\modelPicker.tsx | 61 | technical/protocol line | setStage('provider') |
| tui | ui-tui\src\components\modelPicker.tsx | 76 | technical/protocol line | if (stage === 'model' \|\| stage === 'key' \|\| stage === 'disconnect') { |
| tui | ui-tui\src\components\modelPicker.tsx | 77 | technical/protocol line | setStage('provider') |
| tui | ui-tui\src\components\modelPicker.tsx | 105 | technical/protocol line | gw.request<{ provider?: ModelOptionProvider }>('model.save_key', { |
| tui | ui-tui\src\components\modelPicker.tsx | 126 | technical/protocol line | setStage('model') |
| tui | ui-tui\src\components\modelPicker.tsx | 161 | technical/protocol line | setStage('provider') |
| tui | ui-tui\src\components\modelPicker.tsx | 167 | technical/protocol line | gw.request<{ disconnected?: boolean }>('model.disconnect', { |
| tui | ui-tui\src\components\modelPicker.tsx | 185 | technical/protocol line | setStage('provider') |
| tui | ui-tui\src\components\modelPicker.tsx | 189 | technical/protocol line | setStage('provider') |
| tui | ui-tui\src\components\modelPicker.tsx | 196 | technical/protocol line | setStage('provider') |
| tui | ui-tui\src\components\modelPicker.tsx | 204 | technical/protocol line | const count = stage === 'provider' ? providers.length : models.length |
| tui | ui-tui\src\components\modelPicker.tsx | 205 | technical/protocol line | const sel = stage === 'provider' ? providerIdx : modelIdx |
| tui | ui-tui\src\components\modelPicker.tsx | 206 | technical/protocol line | const setSel = stage === 'provider' ? setProviderIdx : setModelIdx |
| tui | ui-tui\src\components\modelPicker.tsx | 221 | technical/protocol line | if (stage === 'provider') { |
| tui | ui-tui\src\components\modelPicker.tsx | 228 | technical/protocol line | if (provider.auth_type === 'api_key' && provider.key_env) { |
| tui | ui-tui\src\components\modelPicker.tsx | 238 | technical/protocol line | setStage('model') |
| tui | ui-tui\src\components\modelPicker.tsx | 247 | technical/protocol line | onSelect(`${model} --provider ${provider.slug}${persistGlobal ? ' --global' : ` ${TUI_SESSION_MODEL_FLAG}`}`) |
| tui | ui-tui\src\components\modelPicker.tsx | 249 | technical/protocol line | setStage('provider') |
| tui | ui-tui\src\components\modelPicker.tsx | 262 | technical/protocol line | if (ch.toLowerCase() === 'd' && stage === 'provider' && provider?.authenticated !== false) { |
| tui | ui-tui\src\components\modelPicker.tsx | 292 | technical/protocol line | if (stage === 'key' && provider) { |
| tui | ui-tui\src\components\modelPicker.tsx | 335 | technical/protocol line | if (stage === 'disconnect' && provider) { |
| tui | ui-tui\src\components\modelPicker.tsx | 364 | technical/protocol line | if (stage === 'provider') { |
| tui | ui-tui\src\components\modelPicker.tsx | 393 | mixed technical/protocol line | {provider?.warning ? `提醒: ${provider.warning}` : ' '} |
| tui | ui-tui\src\components\modelPicker.tsx | 424 | mixed technical/protocol line | {offset + VISIBLE < rows.length ? ` ↓ 还有 ${rows.length - offset - VISIBLE} 项` : ' '} |
| tui | ui-tui\src\components\modelPicker.tsx | 448 | mixed technical/protocol line | {provider?.warning ? `提醒: ${provider.warning}` : ' '} |
| tui | ui-tui\src\components\modelPicker.tsx | 477 | technical/protocol line | key={`${provider?.slug ?? 'prov'}:${idx}:${row}`} |
| tui | ui-tui\src\components\modelPicker.tsx | 487 | mixed technical/protocol line | {offset + VISIBLE < models.length ? ` ↓ 还有 ${models.length - offset - VISIBLE} 项` : ' '} |
| tui | ui-tui\src\components\prompts.tsx | 10 | technical/protocol line | const OPTS = ['once', 'session', 'always', 'deny'] as const |
| tui | ui-tui\src\components\prompts.tsx | 11 | mixed technical/protocol line | const LABELS = { always: '始终允许', deny: '拒绝', once: '允许一次', session: '本次会话允许' } as const |
| tui | ui-tui\src\components\prompts.tsx | 22 | technical/protocol line | \| { kind: 'choose'; choice: (typeof OPTS)[number] } |
| tui | ui-tui\src\components\prompts.tsx | 45 | technical/protocol line | return { kind: 'choose', choice: OPTS[n - 1]! } |
| tui | ui-tui\src\components\prompts.tsx | 49 | technical/protocol line | return { kind: 'choose', choice: OPTS[sel]! } |
| tui | ui-tui\src\components\sessionPicker.tsx | 74 | technical/protocol line | gw.request<SessionDeleteResponse>('session.delete', { session_id: target.id }) |
| tui | ui-tui\src\components\streamingAssistant.tsx | 71 | technical/protocol line | role: 'assistant', |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 38 | technical/protocol line | // Count ``` / ~~~ AND `$$` / `\[…\]` fence toggles in `s` up to `end`. Odd |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 43 | technical/protocol line | // don't double-count. A `$$x$$` line that opens AND closes on its own |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 46 | technical/protocol line | // NB: this is INTENTIONALLY more conservative than `markdown.tsx`'s |
| tui | ui-tui\src\components\streamingMarkdown.tsx | 104 | technical/protocol line | // Find the last "\n\n" boundary before `end` that is OUTSIDE a fenced code |
| tui | ui-tui\src\components\textInput.tsx | 29 | technical/protocol line | const INV = `${ESC}[7m` |
| tui | ui-tui\src\components\textInput.tsx | 30 | technical/protocol line | const INV_OFF = `${ESC}[27m` |
| tui | ui-tui\src\components\textInput.tsx | 31 | technical/protocol line | const DIM = `${ESC}[2m` |
| tui | ui-tui\src\components\textInput.tsx | 32 | technical/protocol line | const DIM_OFF = `${ESC}[22m` |
| tui | ui-tui\src\components\textInput.tsx | 33 | technical/protocol line | const FWD_DEL_RE = new RegExp(`${ESC}\\[3(?:[~$^]\|;)`) |
| tui | ui-tui\src\components\textInput.tsx | 35 | technical/protocol line | const BRACKET_PASTE = new RegExp(`${ESC}?\\[20[01]~`, 'g') |
| tui | ui-tui\src\components\textInput.tsx | 203 | technical/protocol line | * We deliberately do NOT just check `stringWidth(text) === text.length`: |
| tui | ui-tui\src\components\textInput.tsx | 243 | technical/protocol line | * When `columns` is supplied, ALSO rejects when the physical cursor |
| tui | ui-tui\src\components\textInput.tsx | 248 | technical/protocol line | * the previous visual line, desyncing both Ink's `displayCursor` model |
| tui | ui-tui\src\components\textInput.tsx | 251 | technical/protocol line | * When `columns` is OMITTED, the wrap-boundary check is skipped |
| tui | ui-tui\src\components\textInput.tsx | 280 | technical/protocol line | // case AND `column >= columns` for the "exact-fill, terminal auto-wraps" |
| tui | ui-tui\src\components\textInput.tsx | 301 | technical/protocol line | return (env.TERM_PROGRAM ?? '').trim() !== 'Apple_Terminal' |
| tui | ui-tui\src\components\textInput.tsx | 972 | technical/protocol line | // LEFT of where Ink last parked it. Tell Ink so its `displayCursor` |
| tui | ui-tui\src\components\textInput.tsx | 1021 | technical/protocol line | const text = inp.replace(BRACKET_PASTE, '').replace(/\r\n/g, '\n').replace(/\r/g, '\n') |
| tui | ui-tui\src\components\thinking.tsx | 5 | technical/protocol line | import { THINKING_COT_MAX } from '../config/limits.js' |
| tui | ui-tui\src\components\thinking.tsx | 43 | technical/protocol line | const THINK: BrailleSpinnerName[] = ['helix', 'breathe', 'orbit', 'dna', 'waverows', 'snake', 'pulse'] |
| tui | ui-tui\src\components\thinking.tsx | 44 | technical/protocol line | const TOOL: BrailleSpinnerName[] = ['cascade', 'scan', 'diagswipe', 'fillsweep', 'rain', 'columns', 'sparkle'] |
| tui | ui-tui\src\components\thinking.tsx | 170 | technical/protocol line | const raw = spinners[pick(variant === 'tool' ? TOOL : THINK)] |
| tui | ui-tui\src\components\thinking.tsx | 441 | technical/protocol line | key: 'thinking', |
| tui | ui-tui\src\components\thinking.tsx | 474 | technical/protocol line | key: 'tools', |
| tui | ui-tui\src\components\thinking.tsx | 516 | technical/protocol line | key: 'notes', |
| tui | ui-tui\src\components\thinking.tsx | 556 | technical/protocol line | key: 'subagents', |
| tui | ui-tui\src\components\thinking.tsx | 779 | technical/protocol line | const cot = useMemo(() => thinkingPreview(reasoning, 'full', THINKING_COT_MAX), [reasoning]) |
| tui | ui-tui\src\components\thinking.tsx | 1049 | technical/protocol line | key: 'thinking', |
| tui | ui-tui\src\components\thinking.tsx | 1083 | technical/protocol line | key: 'tools', |
| tui | ui-tui\src\components\thinking.tsx | 1149 | technical/protocol line | key: 'subagents', |
| tui | ui-tui\src\components\thinking.tsx | 1173 | technical/protocol line | key: 'meta', |
| tui | ui-tui\src\content\hotkeys.ts | 21 | mixed technical/protocol line | [action + '+G / Alt+G', '打开 $EDITOR（VSCode/Cursor 可用 Alt+G 兜底）'], |
| tui | ui-tui\src\content\setup.ts | 7 | mixed technical/protocol line | text: 'TUI 开始会话前，需要先配置一个模型服务商。' |
| tui | ui-tui\src\content\setup.ts | 11 | mixed technical/protocol line | ['/model', '在当前界面配置服务商和模型'], |
| tui | ui-tui\src\domain\details.ts | 3 | technical/protocol line | const MODES = ['hidden', 'collapsed', 'expanded'] as const |
| tui | ui-tui\src\domain\details.ts | 5 | technical/protocol line | export const SECTION_NAMES = ['thinking', 'tools', 'subagents', 'activity'] as const |
| tui | ui-tui\src\domain\details.ts | 24 | technical/protocol line | thinking: 'expanded', |
| tui | ui-tui\src\domain\details.ts | 25 | technical/protocol line | tools: 'expanded', |
| tui | ui-tui\src\domain\details.ts | 26 | technical/protocol line | activity: 'hidden' |
| tui | ui-tui\src\domain\details.ts | 30 | technical/protocol line | collapsed: 'collapsed', |
| tui | ui-tui\src\domain\details.ts | 31 | technical/protocol line | full: 'expanded', |
| tui | ui-tui\src\domain\details.ts | 32 | technical/protocol line | truncated: 'collapsed' |
| tui | ui-tui\src\domain\details.ts | 43 | technical/protocol line | typeof v === 'string' && (SECTION_NAMES as readonly string[]).includes(v) |
| tui | ui-tui\src\domain\details.ts | 46 | technical/protocol line | parseDetailsMode(d?.details_mode) ?? THINKING_FALLBACK[norm(d?.thinking_mode)] ?? 'collapsed' |
| tui | ui-tui\src\domain\messages.ts | 1 | technical/protocol line | import { LONG_MSG } from '../config/limits.js' |
| tui | ui-tui\src\domain\slash.ts | 1 | technical/protocol line | /** Appended to `/model` args from the TUI picker for session scope; stripped in `session` slash before `config.set`. */ |
| tui | ui-tui\src\domain\slash.ts | 2 | technical/protocol line | export const TUI_SESSION_MODEL_FLAG = '--tui-session' |
| tui | ui-tui\src\entry.tsx | 8 | technical/protocol line | import { TERMUX_TUI_MODE } from './config/env.js' |
| tui | ui-tui\src\entry.tsx | 17 | user-facing output | console.log('hermes-tui: 当前不是 TTY，无法启动交互界面') |
| tui | ui-tui\src\entry.tsx | 97 | technical/protocol line | // The TUI's mouse tracking captures click events before Terminal.app's |
| tui | ui-tui\src\entry.tsx | 98 | technical/protocol line | // own URL detection can fire, so without this hook clicks on `<Link>` |
| tui | ui-tui\src\gatewayClient.ts | 22 | technical/protocol line | line.length > MAX_LOG_LINE_BYTES ? `${line.slice(0, MAX_LOG_LINE_BYTES)}… [truncated ${line.length} bytes]` : line |
| tui | ui-tui\src\gatewayClient.ts | 85 | technical/protocol line | // otherwise-malformed URLs that the WHATWG `URL` parser can't accept. |
| tui | ui-tui\src\gatewayClient.ts | 107 | technical/protocol line | // `user:pass@` segment AND the query string so a malformed token |
| tui | ui-tui\src\gatewayClient.ts | 233 | technical/protocol line | type: 'gateway.start_timeout', |
| tui | ui-tui\src\gatewayClient.ts | 311 | technical/protocol line | const preview = text.trim().slice(0, MAX_LOG_PREVIEW) \|\| '(empty frame)' |
| tui | ui-tui\src\gatewayClient.ts | 324 | technical/protocol line | env.PYTHONPATH = pyPath ? `${root}${delimiter}${pyPath}` : root |
| tui | ui-tui\src\gatewayClient.ts | 333 | technical/protocol line | const preview = raw.trim().slice(0, MAX_LOG_PREVIEW) \|\| '(empty line)' |
| tui | ui-tui\src\gatewayClient.ts | 389 | technical/protocol line | const line = `[startup] WebSocket API unavailable; cannot attach to ${safeAttachUrl}` |
| tui | ui-tui\src\gatewayClient.ts | 675 | technical/protocol line | this.proc!.stdin!.write(JSON.stringify({ id, jsonrpc: '2.0', method, params }) + '\n') |
| tui | ui-tui\src\gatewayTypes.ts | 463 | technical/protocol line | \| { payload?: { skin?: GatewaySkin }; session_id?: string; type: 'gateway.ready' } |
| tui | ui-tui\src\gatewayTypes.ts | 464 | technical/protocol line | \| { payload?: GatewaySkin; session_id?: string; type: 'skin.changed' } |
| tui | ui-tui\src\gatewayTypes.ts | 465 | technical/protocol line | \| { payload: SessionInfo; session_id?: string; type: 'session.info' } |
| tui | ui-tui\src\gatewayTypes.ts | 466 | technical/protocol line | \| { payload?: { text?: string }; session_id?: string; type: 'thinking.delta' } |
| tui | ui-tui\src\gatewayTypes.ts | 467 | technical/protocol line | \| { payload?: undefined; session_id?: string; type: 'message.start' } |
| tui | ui-tui\src\gatewayTypes.ts | 468 | technical/protocol line | \| { payload?: { kind?: string; text?: string }; session_id?: string; type: 'status.update' } |
| tui | ui-tui\src\gatewayTypes.ts | 469 | technical/protocol line | \| { payload?: { state?: 'idle' \| 'listening' \| 'transcribing' }; session_id?: string; type: 'voice.status' } |
| tui | ui-tui\src\gatewayTypes.ts | 470 | technical/protocol line | \| { payload?: { no_speech_limit?: boolean; text?: string }; session_id?: string; type: 'voice.transcript' } |
| tui | ui-tui\src\gatewayTypes.ts | 471 | technical/protocol line | \| { payload: { line: string }; session_id?: string; type: 'gateway.stderr' } |
| tui | ui-tui\src\gatewayTypes.ts | 475 | technical/protocol line | type: 'browser.progress' |
| tui | ui-tui\src\gatewayTypes.ts | 480 | technical/protocol line | type: 'gateway.start_timeout' |
| tui | ui-tui\src\gatewayTypes.ts | 482 | technical/protocol line | \| { payload?: { preview?: string }; session_id?: string; type: 'gateway.protocol_error' } |
| tui | ui-tui\src\gatewayTypes.ts | 483 | technical/protocol line | \| { payload?: { text?: string }; session_id?: string; type: 'reasoning.delta' \| 'reasoning.available' } |
| tui | ui-tui\src\gatewayTypes.ts | 484 | technical/protocol line | \| { payload: { name?: string; preview?: string }; session_id?: string; type: 'tool.progress' } |
| tui | ui-tui\src\gatewayTypes.ts | 485 | technical/protocol line | \| { payload: { name?: string }; session_id?: string; type: 'tool.generating' } |
| tui | ui-tui\src\gatewayTypes.ts | 489 | technical/protocol line | type: 'tool.start' |
| tui | ui-tui\src\gatewayTypes.ts | 502 | technical/protocol line | type: 'tool.complete' |
| tui | ui-tui\src\gatewayTypes.ts | 507 | technical/protocol line | type: 'clarify.request' |
| tui | ui-tui\src\gatewayTypes.ts | 510 | technical/protocol line | \| { payload: { request_id: string }; session_id?: string; type: 'sudo.request' } |
| tui | ui-tui\src\gatewayTypes.ts | 511 | technical/protocol line | \| { payload: { env_var: string; prompt: string; request_id: string }; session_id?: string; type: 'secret.request' } |
| tui | ui-tui\src\gatewayTypes.ts | 513 | technical/protocol line | \| { payload?: { text?: string }; session_id?: string; type: 'review.summary' } |
| tui | ui-tui\src\gatewayTypes.ts | 514 | technical/protocol line | \| { payload: SubagentEventPayload; session_id?: string; type: 'subagent.spawn_requested' } |
| tui | ui-tui\src\gatewayTypes.ts | 515 | technical/protocol line | \| { payload: SubagentEventPayload; session_id?: string; type: 'subagent.start' } |
| tui | ui-tui\src\gatewayTypes.ts | 516 | technical/protocol line | \| { payload: SubagentEventPayload; session_id?: string; type: 'subagent.thinking' } |
| tui | ui-tui\src\gatewayTypes.ts | 517 | technical/protocol line | \| { payload: SubagentEventPayload; session_id?: string; type: 'subagent.tool' } |
| tui | ui-tui\src\gatewayTypes.ts | 518 | technical/protocol line | \| { payload: SubagentEventPayload; session_id?: string; type: 'subagent.progress' } |
| tui | ui-tui\src\gatewayTypes.ts | 519 | technical/protocol line | \| { payload: SubagentEventPayload; session_id?: string; type: 'subagent.complete' } |
| tui | ui-tui\src\gatewayTypes.ts | 520 | technical/protocol line | \| { payload: { rendered?: string; text?: string }; session_id?: string; type: 'message.delta' } |
| tui | ui-tui\src\gatewayTypes.ts | 524 | technical/protocol line | type: 'message.complete' |
| tui | ui-tui\src\gatewayTypes.ts | 526 | technical/protocol line | \| { payload?: { message?: string }; session_id?: string; type: 'error' } |
| tui | ui-tui\src\hooks\useCompletion.ts | 24 | technical/protocol line | // `/model` uses the two-step ModelPicker (real curated IDs). |
| tui | ui-tui\src\hooks\useCompletion.ts | 35 | technical/protocol line | method: 'complete.path', |
| tui | ui-tui\src\hooks\useGitBranch.ts | 15 | technical/protocol line | const { stdout } = await pexec('git', ['-C', cwd, 'rev-parse', '--abbrev-ref', 'HEAD'], { timeout: TIMEOUT_MS }) |
| tui | ui-tui\src\hooks\useGitBranch.ts | 18 | technical/protocol line | return !b \|\| b === 'HEAD' ? null : b |
| tui | ui-tui\src\lib\clipboard.ts | 6 | technical/protocol line | const POWERSHELL_ARGS = ['-NoProfile', '-NonInteractive', '-Command', 'Get-Clipboard -Raw'] as const |
| tui | ui-tui\src\lib\clipboard.ts | 42 | technical/protocol line | return [{ cmd: 'powershell', args: POWERSHELL_ARGS }] |
| tui | ui-tui\src\lib\clipboard.ts | 48 | technical/protocol line | attempts.push({ cmd: 'powershell.exe', args: POWERSHELL_ARGS }) |
| tui | ui-tui\src\lib\clipboard.ts | 78 | technical/protocol line | encoding: 'utf8', |
| tui | ui-tui\src\lib\clipboard.ts | 110 | technical/protocol line | cmd: 'powershell.exe', |
| tui | ui-tui\src\lib\clipboard.ts | 116 | technical/protocol line | attempts.push({ cmd: 'wl-copy', args: ['--type', 'text/plain'] }) |
| tui | ui-tui\src\lib\editor.ts | 6 | technical/protocol line | * prompt_toolkit's `Buffer.open_in_editor()` picker so the classic CLI and |
| tui | ui-tui\src\lib\editor.ts | 9 | technical/protocol line | const FALLBACKS = ['editor', 'nano', 'pico', 'vi', 'emacs'] |
| tui | ui-tui\src\lib\editor.ts | 24 | technical/protocol line | * 1. $VISUAL / $EDITOR, shell-tokenized so `EDITOR="code --wait"` works |
| tui | ui-tui\src\lib\externalCli.ts | 8 | technical/protocol line | const resolveHermesBin = () => process.env.HERMES_BIN?.trim() \|\| 'hermes' |
| tui | ui-tui\src\lib\externalLink.ts | 15 | technical/protocol line | 'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36' |
| tui | ui-tui\src\lib\externalLink.ts | 23 | technical/protocol line | const LOCAL_HOST_SUFFIXES = ['.corp', '.home', '.internal', '.lan', '.local', '.localdomain'] |
| tui | ui-tui\src\lib\externalLink.ts | 44 | technical/protocol line | return DOMAIN_RE.test(trimmed) ? `https://${trimmed}` : trimmed |
| tui | ui-tui\src\lib\externalLink.ts | 339 | technical/protocol line | 'User-Agent': TITLE_USER_AGENT |
| tui | ui-tui\src\lib\externalLink.ts | 341 | technical/protocol line | redirect: 'follow', |
| tui | ui-tui\src\lib\externalLink.ts | 349 | technical/protocol line | const contentType = response.headers.get('content-type') |
| tui | ui-tui\src\lib\forceTruecolor.ts | 15 | technical/protocol line | if (FALSE_RE.test(override) \|\| 'NO_COLOR' in env) { |
| tui | ui-tui\src\lib\forceTruecolor.ts | 22 | technical/protocol line | const isAppleTerminal = (env: NodeJS.ProcessEnv = process.env) => (env.TERM_PROGRAM ?? '').trim() === 'Apple_Terminal' |
| tui | ui-tui\src\lib\forceTruecolor.ts | 45 | technical/protocol line | process.env.COLORTERM = 'truecolor' |
| tui | ui-tui\src\lib\forceTruecolor.ts | 55 | technical/protocol line | if ((process.env.FORCE_COLOR ?? '').trim() === '3') { |
| tui | ui-tui\src\lib\fpsStore.ts | 10 | technical/protocol line | import { SHOW_FPS } from '../config/env.js' |
| tui | ui-tui\src\lib\gracefulExit.ts | 8 | technical/protocol line | const SIGNAL_EXIT_CODE: Record<'SIGHUP' \| 'SIGINT' \| 'SIGTERM', number> = { |
| tui | ui-tui\src\lib\gracefulExit.ts | 41 | technical/protocol line | for (const sig of ['SIGINT', 'SIGTERM', 'SIGHUP'] as const) { |
| tui | ui-tui\src\lib\history.ts | 6 | technical/protocol line | const dir = process.env.HERMES_HOME ?? join(homedir(), '.hermes') |
| tui | ui-tui\src\lib\inputMetrics.ts | 24 | technical/protocol line | // back to its original offset in `value`. wrap-ansi only INSERTS '\n' at wrap |
| tui | ui-tui\src\lib\inputMetrics.ts | 115 | technical/protocol line | * IMPORTANT: this MUST stay in lock-step with how Ink's `<Text wrap="wrap">` |
| tui | ui-tui\src\lib\mathUnicode.ts | 423 | technical/protocol line | // exported `BOX_RE` below. |
| tui | ui-tui\src\lib\mathUnicode.ts | 460 | technical/protocol line | const SYMBOL_LETTER_RE = new RegExp('(?:' + buildAlt(LETTER_CMDS) + ')(?![A-Za-z])', 'g') |
| tui | ui-tui\src\lib\mathUnicode.ts | 461 | technical/protocol line | const SYMBOL_PUNCT_RE = new RegExp('(?:' + buildAlt(PUNCT_CMDS) + ')', 'g') |
| tui | ui-tui\src\lib\mathUnicode.ts | 702 | technical/protocol line | s = replaceBracedCommand(s, '\\boxed', body => `${BOX_OPEN}${body.trim()}${BOX_CLOSE}`) |
| tui | ui-tui\src\lib\mathUnicode.ts | 703 | technical/protocol line | s = replaceBracedCommand(s, '\\fbox', body => `${BOX_OPEN}${body.trim()}${BOX_CLOSE}`) |
| tui | ui-tui\src\lib\mathUnicode.ts | 749 | technical/protocol line | // Run symbol substitution BEFORE scripts so a body like `^{\infty}` |
| tui | ui-tui\src\lib\mathUnicode.ts | 760 | technical/protocol line | // Bare `^c` / `_c` handles ONLY alphanumerics and `+`/`-`/`=`. Parens |
| tui | ui-tui\src\lib\memory.ts | 104 | technical/protocol line | ? `WARNING: ${potentialLeaks.length} potential leak indicator(s). See potentialLeaks.` |
| tui | ui-tui\src\lib\memory.ts | 148 | technical/protocol line | const dir = process.env.HERMES_HEAPDUMP_DIR?.trim() \|\| join(homedir() \|\| tmpdir(), '.hermes', 'heapdumps') |
| tui | ui-tui\src\lib\memory.ts | 173 | technical/protocol line | return `${value >= 100 ? value.toFixed(0) : value.toFixed(1)}${UNITS[exp]}` |
| tui | ui-tui\src\lib\memoryMonitor.ts | 81 | technical/protocol line | // full on 'critical' (post-dump RSS reduction, keeps user running). |
| tui | ui-tui\src\lib\openExternalUrl.ts | 8 | technical/protocol line | * mouse click on a `<Link>` cell (or a row containing a plain-text URL the |
| tui | ui-tui\src\lib\openExternalUrl.ts | 16 | technical/protocol line | * rejected — a hostile model could otherwise emit `<Link url="file:///">` |
| tui | ui-tui\src\lib\openExternalUrl.ts | 18 | technical/protocol line | * - Hostname is parsed via `URL`; only well-formed URLs are forwarded. |
| tui | ui-tui\src\lib\openExternalUrl.ts | 19 | technical/protocol line | * - Spawned via `child_process.spawn` with arg array (no shell), so a URL |
| tui | ui-tui\src\lib\openExternalUrl.ts | 24 | technical/protocol line | * not proceed — covers (a) URL rejected by `parseSafeUrl` (non-http(s), |
| tui | ui-tui\src\lib\openExternalUrl.ts | 30 | technical/protocol line | * so the TUI doesn't crash, and the user just doesn't see their browser |
| tui | ui-tui\src\lib\openExternalUrl.ts | 55 | technical/protocol line | stdio: 'ignore' |
| tui | ui-tui\src\lib\openExternalUrl.ts | 59 | technical/protocol line | // when the binary is missing (ENOENT on `xdg-open` / `explorer.exe`), |
| tui | ui-tui\src\lib\openExternalUrl.ts | 112 | technical/protocol line | // accepts URLs like 'http:///foo' on some Node versions; we don't want |
| tui | ui-tui\src\lib\openExternalUrl.ts | 132 | technical/protocol line | * through cmd. Linux/BSD use `xdg-open` directly with no shell wrapping. |
| tui | ui-tui\src\lib\openExternalUrl.ts | 151 | technical/protocol line | const XDG_OPEN_PLATFORMS = new Set(['linux', 'freebsd', 'openbsd', 'netbsd', 'dragonfly']) |
| tui | ui-tui\src\lib\osc52.ts | 3 | technical/protocol line | const ST = `${ESC}\\` |
| tui | ui-tui\src\lib\osc52.ts | 5 | technical/protocol line | export const OSC52_CLIPBOARD_QUERY = `${ESC}]52;c;?${BEL}` |
| tui | ui-tui\src\lib\osc52.ts | 15 | technical/protocol line | if (process.env['TMUX']) { |
| tui | ui-tui\src\lib\osc52.ts | 16 | technical/protocol line | return `${ESC}Ptmux;${sequence.split(ESC).join(ESC + ESC)}${ST}` |
| tui | ui-tui\src\lib\osc52.ts | 19 | technical/protocol line | if (process.env['STY']) { |
| tui | ui-tui\src\lib\osc52.ts | 20 | technical/protocol line | return `${ESC}P${sequence}${ST}` |
| tui | ui-tui\src\lib\perfPane.tsx | 8 | technical/protocol line | // override HERMES_DEV_PERF_LOG). Tagged { src: 'react' \| 'frame' } for jq. |
| tui | ui-tui\src\lib\perfPane.tsx | 24 | technical/protocol line | const LOG_PATH = process.env.HERMES_DEV_PERF_LOG?.trim() \|\| join(homedir(), '.hermes', 'perf.log') |
| tui | ui-tui\src\lib\perfPane.tsx | 40 | technical/protocol line | appendFileSync(LOG_PATH, `${JSON.stringify(row)}\n`) |
| tui | ui-tui\src\lib\perfPane.tsx | 59 | technical/protocol line | src: 'react', |
| tui | ui-tui\src\lib\perfPane.tsx | 100 | technical/protocol line | src: 'frame', |
| tui | ui-tui\src\lib\platform.ts | 59 | technical/protocol line | * when ``voice.record_key`` is e.g. ``ctrl+o`` the TUI binds Ctrl+O. |
| tui | ui-tui\src\lib\platform.ts | 84 | technical/protocol line | mod: 'ctrl', |
| tui | ui-tui\src\lib\platform.ts | 104 | technical/protocol line | * ``opt`` spellings are normalized identically in the classic CLI |
| tui | ui-tui\src\lib\platform.ts | 108 | technical/protocol line | * ``win`` / ``windows`` spellings are TUI-only — prompt_toolkit has no |
| tui | ui-tui\src\lib\platform.ts | 112 | technical/protocol line | alt: 'alt', |
| tui | ui-tui\src\lib\platform.ts | 113 | technical/protocol line | control: 'ctrl', |
| tui | ui-tui\src\lib\platform.ts | 114 | technical/protocol line | ctrl: 'ctrl', |
| tui | ui-tui\src\lib\platform.ts | 115 | technical/protocol line | option: 'alt', |
| tui | ui-tui\src\lib\platform.ts | 116 | technical/protocol line | opt: 'alt', |
| tui | ui-tui\src\lib\platform.ts | 117 | technical/protocol line | super: 'super', |
| tui | ui-tui\src\lib\platform.ts | 118 | technical/protocol line | win: 'super', |
| tui | ui-tui\src\lib\platform.ts | 119 | technical/protocol line | windows: 'super' |
| tui | ui-tui\src\lib\platform.ts | 125 | technical/protocol line | * ``esc`` ↔ ``escape``) so a config that round-trips through the CLI also |
| tui | ui-tui\src\lib\platform.ts | 128 | technical/protocol line | backspace: 'backspace', |
| tui | ui-tui\src\lib\platform.ts | 129 | technical/protocol line | bs: 'backspace', |
| tui | ui-tui\src\lib\platform.ts | 130 | technical/protocol line | del: 'delete', |
| tui | ui-tui\src\lib\platform.ts | 131 | technical/protocol line | delete: 'delete', |
| tui | ui-tui\src\lib\platform.ts | 132 | technical/protocol line | enter: 'enter', |
| tui | ui-tui\src\lib\platform.ts | 133 | technical/protocol line | esc: 'escape', |
| tui | ui-tui\src\lib\platform.ts | 134 | technical/protocol line | escape: 'escape', |
| tui | ui-tui\src\lib\platform.ts | 135 | technical/protocol line | ret: 'enter', |
| tui | ui-tui\src\lib\platform.ts | 136 | technical/protocol line | return: 'enter', |
| tui | ui-tui\src\lib\platform.ts | 137 | technical/protocol line | space: 'space', |
| tui | ui-tui\src\lib\platform.ts | 138 | technical/protocol line | spc: 'space', |
| tui | ui-tui\src\lib\platform.ts | 139 | technical/protocol line | tab: 'tab' |
| tui | ui-tui\src\lib\platform.ts | 149 | technical/protocol line | * ``ctrl+x`` is intentionally NOT here — it's only claimed during |
| tui | ui-tui\src\lib\platform.ts | 151 | technical/protocol line | * for most of the session and matches CLI parity for ``ctrl+<letter>`` |
| tui | ui-tui\src\lib\platform.ts | 163 | technical/protocol line | * at parse time so kitty/CSI-u ``super+<key>`` configs still work for |
| tui | ui-tui\src\lib\platform.ts | 216 | technical/protocol line | * AND the named tokens declared in ``_NAMED_KEY_ALIASES`` (``space``, |
| tui | ui-tui\src\lib\platform.ts | 218 | technical/protocol line | * ``delete``) — matching the keys prompt_toolkit accepts on the CLI |
| tui | ui-tui\src\lib\platform.ts | 221 | technical/protocol line | * Accepts ``unknown`` because the source is raw YAML via |
| tui | ui-tui\src\lib\platform.ts | 253 | technical/protocol line | // ``c-x`` / ``a-x`` rewrite in ``cli.py``, so this matches CLI parity. |
| tui | ui-tui\src\lib\platform.ts | 289 | technical/protocol line | // globals key off Ctrl (not Super), so kitty/CSI-u ``super+<letter>`` |
| tui | ui-tui\src\lib\platform.ts | 392 | technical/protocol line | // but ONLY ``key.super`` (kitty-style), never ``key.meta``, since |
| tui | ui-tui\src\lib\reasoning.ts | 1 | technical/protocol line | const TAGS = ['think', 'reasoning', 'thinking', 'thought', 'REASONING_SCRATCHPAD'] as const |
| tui | ui-tui\src\lib\rpc.ts | 31 | technical/protocol line | type: 'send', |
| tui | ui-tui\src\lib\subagentTree.ts | 3 | technical/protocol line | const ROOT_KEY = '__root__' |
| tui | ui-tui\src\lib\subagentTree.ts | 165 | technical/protocol line | * for "kill subtree" walks that fire one RPC per descendant. |
| tui | ui-tui\src\lib\syntax.ts | 61 | technical/protocol line | rs: 'rust', |
| tui | ui-tui\src\lib\syntax.ts | 65 | technical/protocol line | yml: 'yaml', |
| tui | ui-tui\src\lib\terminalParity.ts | 22 | technical/protocol line | const termProgram = env['TERM_PROGRAM'] ?? '' |
| tui | ui-tui\src\lib\terminalParity.ts | 25 | technical/protocol line | isAppleTerminal: termProgram === 'Apple_Terminal' \|\| !!env['TERM_SESSION_ID'], |
| tui | ui-tui\src\lib\terminalParity.ts | 27 | technical/protocol line | isTmux: !!env['TMUX'], |
| tui | ui-tui\src\lib\terminalParity.ts | 44 | technical/protocol line | key: 'ide-setup', |
| tui | ui-tui\src\lib\terminalParity.ts | 45 | technical/protocol line | tone: 'info', |
| tui | ui-tui\src\lib\terminalParity.ts | 52 | technical/protocol line | key: 'apple-terminal', |
| tui | ui-tui\src\lib\terminalParity.ts | 53 | technical/protocol line | tone: 'warn', |
| tui | ui-tui\src\lib\terminalParity.ts | 61 | technical/protocol line | key: 'tmux', |
| tui | ui-tui\src\lib\terminalParity.ts | 62 | technical/protocol line | tone: 'warn', |
| tui | ui-tui\src\lib\terminalParity.ts | 63 | user-facing field | message: '检测到 tmux · 剪贴板会优先使用 passthrough；开启 allow-passthrough 可提高 OSC52 稳定性' |
| tui | ui-tui\src\lib\terminalParity.ts | 69 | technical/protocol line | key: 'remote', |
| tui | ui-tui\src\lib\terminalParity.ts | 70 | technical/protocol line | tone: 'warn', |
| tui | ui-tui\src\lib\terminalParity.ts | 71 | user-facing field | message: '检测到 SSH 会话 · 文本剪贴板可通过 OSC52 桥接，图片剪贴板和本机截图路径仍取决于运行 Hermes 的机器' |
| tui | ui-tui\src\lib\terminalSetup.ts | 39 | technical/protocol line | command: 'workbench.action.terminal.sendSequence', |
| tui | ui-tui\src\lib\terminalSetup.ts | 47 | technical/protocol line | command: 'workbench.action.terminal.sendSequence', |
| tui | ui-tui\src\lib\terminalSetup.ts | 48 | technical/protocol line | when: 'terminalFocus', |
| tui | ui-tui\src\lib\terminalSetup.ts | 53 | technical/protocol line | command: 'workbench.action.terminal.sendSequence', |
| tui | ui-tui\src\lib\terminalSetup.ts | 54 | technical/protocol line | when: 'terminalFocus', |
| tui | ui-tui\src\lib\terminalSetup.ts | 59 | technical/protocol line | command: 'workbench.action.terminal.sendSequence', |
| tui | ui-tui\src\lib\terminalSetup.ts | 60 | technical/protocol line | when: 'terminalFocus', |
| tui | ui-tui\src\lib\terminalSetup.ts | 65 | technical/protocol line | command: 'workbench.action.terminal.sendSequence', |
| tui | ui-tui\src\lib\terminalSetup.ts | 66 | technical/protocol line | when: 'terminalFocus', |
| tui | ui-tui\src\lib\terminalSetup.ts | 71 | technical/protocol line | command: 'workbench.action.terminal.sendSequence', |
| tui | ui-tui\src\lib\terminalSetup.ts | 72 | technical/protocol line | when: 'terminalFocus', |
| tui | ui-tui\src\lib\terminalSetup.ts | 78 | technical/protocol line | platform === 'darwin' ? [MAC_COPY_BINDING, ...BASE_BINDINGS] : BASE_BINDINGS |
| tui | ui-tui\src\lib\terminalSetup.ts | 84 | technical/protocol line | const askpass = env['VSCODE_GIT_ASKPASS_MAIN']?.toLowerCase() ?? '' |
| tui | ui-tui\src\lib\terminalSetup.ts | 86 | technical/protocol line | if (env['CURSOR_TRACE_ID'] \|\| askpass.includes('cursor')) { |
| tui | ui-tui\src\lib\terminalSetup.ts | 94 | technical/protocol line | if (env['TERM_PROGRAM'] === 'vscode' \|\| env['VSCODE_GIT_IPC_HANDLE']) { |
| tui | ui-tui\src\lib\terminalSetup.ts | 161 | technical/protocol line | return Boolean(env['SSH_CONNECTION'] \|\| env['SSH_TTY'] \|\| env['SSH_CLIENT']) |
| tui | ui-tui\src\lib\terminalSetup.ts | 175 | technical/protocol line | return env['APPDATA'] ? joinForPlatform(platform, env['APPDATA'], appName, 'User') : null |
| tui | ui-tui\src\lib\terminalSetup.ts | 296 | user-facing field | message: `${meta.label} 终端快捷键设置必须在本机运行，不能在 SSH 会话内执行。` |
| tui | ui-tui\src\lib\terminalSetup.ts | 325 | user-facing field | message: `${meta.label} keybindings.json 不是 JSON 数组: ${keybindingsFile}` |
| tui | ui-tui\src\lib\terminalSetup.ts | 333 | technical/protocol line | if (code !== 'ENOENT') { |
| tui | ui-tui\src\lib\terminalSetup.ts | 377 | technical/protocol line | await ops.writeFile(keybindingsFile, `${JSON.stringify(keybindings, null, 2)}\n`, 'utf8') |
| tui | ui-tui\src\lib\terminalSetup.ts | 403 | user-facing field | message: '未检测到支持的 IDE 终端。支持: VS Code、Cursor、Windsurf。' |
| tui | ui-tui\src\lib\termux.ts | 1 | technical/protocol line | const TERMUX_PREFIX = '/data/data/com.termux/files/usr' |
| tui | ui-tui\src\lib\text.ts | 6 | technical/protocol line | import { VERBS } from '../content/verbs.js' |
| tui | ui-tui\src\lib\text.ts | 11 | technical/protocol line | const ANSI_CSI_RE = new RegExp(`${ESC}\\[[0-?]*[ -/]*[@-~]`, 'g') |
| tui | ui-tui\src\lib\text.ts | 12 | technical/protocol line | const ANSI_CSI_WITH_CMD_RE = new RegExp(`${ESC}\\[[0-?]*[ -/]*([@-~])`, 'g') |
| tui | ui-tui\src\lib\text.ts | 13 | technical/protocol line | const ANSI_INCOMPLETE_CSI_RE = new RegExp(`${ESC}\\[[0-?]*[ -/]*(?=${ESC}\|\\n\|$)`, 'g') |
| tui | ui-tui\src\lib\text.ts | 14 | technical/protocol line | const ANSI_OSC_RE = new RegExp(`${ESC}\\][\\s\\S]*?(?:${BEL}\|${ESC}\\\\)`, 'g') |
| tui | ui-tui\src\lib\text.ts | 15 | technical/protocol line | const ANSI_STRING_RE = new RegExp(`${ESC}[PX^_][\\s\\S]*?(?:${BEL}\|${ESC}\\\\)`, 'g') |
| tui | ui-tui\src\lib\text.ts | 16 | technical/protocol line | const ANSI_NON_CSI_ESC_SEQ_RE = new RegExp(`${ESC}(?!\\[\|\\]\|P\|X\|\\^\|_)[ -/]*[0-~]`, 'g') |
| tui | ui-tui\src\lib\text.ts | 17 | technical/protocol line | const ANSI_STRAY_ESC_RE = new RegExp(`${ESC}(?!\\[)[\\s\\S]?`, 'g') |
| tui | ui-tui\src\lib\text.ts | 37 | technical/protocol line | .replace(ANSI_CSI_WITH_CMD_RE, (seq, cmd: string) => (cmd === 'm' ? seq : '')) |
| tui | ui-tui\src\lib\text.ts | 83 | technical/protocol line | const one = s.replace(WS_RE, ' ').trim().replace(/\]\]/g, '] ]') |
| tui | ui-tui\src\lib\text.ts | 129 | technical/protocol line | const THINKING_STATUS_RE = new RegExp(`^(?:${THINKING_STATUS_PATTERN})\\.{0,3}$`, 'i') |
| tui | ui-tui\src\lib\text.ts | 132 | technical/protocol line | `(?:[^A-Za-z\\u3400-\\u9fff\n]+\\s*)?(?:${THINKING_STATUS_PATTERN})\\.{0,3}\\s*`, |
| tui | ui-tui\src\lib\text.ts | 149 | technical/protocol line | return !raw \|\| mode === 'collapsed' ? '' : mode === 'full' ? raw : compactPreview(raw.replace(WS_RE, ' '), max) |
| tui | ui-tui\src\lib\text.ts | 187 | mixed technical/protocol line | [/\bProfile README\b/gi, '主页 README'], |
| tui | ui-tui\src\lib\text.ts | 196 | technical/protocol line | [/\bGitHub API\b/gi, 'GitHub API'], |
| tui | ui-tui\src\lib\text.ts | 475 | technical/protocol line | const COMPACT_NUMBER = new Intl.NumberFormat('en-US', { maximumFractionDigits: 1, notation: 'compact' }) |
| tui | ui-tui\src\theme.ts | 118 | technical/protocol line | const ANSI_MUTED_FOREGROUNDS: readonly (keyof ThemeColors)[] = ['muted', 'sessionLabel', 'sessionBorder', 'statusDim'] |
| tui | ui-tui\src\theme.ts | 325 | technical/protocol line | primary: '#FFD700', |
| tui | ui-tui\src\theme.ts | 326 | technical/protocol line | accent: '#FFBF00', |
| tui | ui-tui\src\theme.ts | 328 | technical/protocol line | text: '#FFF8DC', |
| tui | ui-tui\src\theme.ts | 340 | user-facing field | label: '#DAA520', |
| tui | ui-tui\src\theme.ts | 345 | technical/protocol line | prompt: '#FFF8DC', |
| tui | ui-tui\src\theme.ts | 354 | technical/protocol line | statusStrong: '#FFD700', |
| tui | ui-tui\src\theme.ts | 357 | technical/protocol line | statusWarn: '#FFD700', |
| tui | ui-tui\src\theme.ts | 378 | technical/protocol line | // backgrounds. Same shape as DARK_THEME so `fromSkin` still layers on top |
| tui | ui-tui\src\theme.ts | 433 | technical/protocol line | const LIGHT_DEFAULT_TERM_PROGRAMS = new Set<string>(['Apple_Terminal']) |
| tui | ui-tui\src\theme.ts | 437 | technical/protocol line | // `HERMES_TUI_BACKGROUND` is intentionally generic so a future OSC11 |
| tui | ui-tui\src\theme.ts | 474 | technical/protocol line | // 1. `HERMES_TUI_LIGHT` boolean — `1`/`true`/`yes`/`on` → light; |
| tui | ui-tui\src\theme.ts | 477 | technical/protocol line | // 2. `HERMES_TUI_THEME` named override — `light` / `dark` win over |
| tui | ui-tui\src\theme.ts | 479 | technical/protocol line | // 3. `HERMES_TUI_BACKGROUND` hex hint (3- or 6-digit) — luminance |
| tui | ui-tui\src\theme.ts | 481 | technical/protocol line | // 4. `COLORFGBG` last field — XFCE / rxvt / Terminal.app emit |
| tui | ui-tui\src\theme.ts | 485 | technical/protocol line | // 5. `TERM_PROGRAM` light-default allow-list. |
| tui | ui-tui\src\theme.ts | 525 | technical/protocol line | // so a malformed `COLORFGBG='15;'` would otherwise look like an |
| tui | ui-tui\src\theme.ts | 574 | technical/protocol line | color[key] = `ansi256(${ANSI_MUTED_BUCKET})` |
| tui | ui-tui\src\types.ts | 132 | technical/protocol line | // SECTION_DEFAULTS → global `details_mode`. Today the built-in defaults |
