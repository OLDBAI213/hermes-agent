# Hermes 汉化审查机制

这个文件是本机汉化工作的准入门。以后继续改 TUI、飞书、插件显示之前，先审查，再修改，再验证。

## 审查顺序

1. 先跑扫描：
   ```powershell
   powershell -ExecutionPolicy Bypass -File scripts\audit-localization.ps1 -Scope all -Output docs\localization-audit-current.md
   ```
2. 先看 `must_review`，确认哪些是真正用户可见文案。
3. 再看 `could_review`，只处理有明确显示路径的内容。
4. 修改后必须重跑扫描和对应测试。
5. 没有扫描结果、没有测试结果、没有真实显示证据时，不能说“确认好了”。

## 必须汉化

- TUI 主界面能看到的标题、标签、按钮、提示、空状态、状态栏、错误、帮助、快捷键说明。
- `/help`、命令说明、命令结果、会话恢复、审批、权限、密钥、确认弹窗。
- Thinking / task frame / tool activity / todo / skills / setup / handoff 等工作流文案。
- 飞书消息正文、卡片标题、状态卡、错误提示、启动提示、运行状态、回退提示。
- `lark-cli-toolbox` 暴露给 Hermes/飞书用户看到的工具名、工具描述、doctor 结果摘要。

## 可以汉化但要验证

- 日志里同时会展示给用户看的错误摘要。
- slash command 描述。命令名本身不翻译，但说明可以翻译。
- accessibility label、tooltip、占位符。TUI 里如果实际不可见，可以低优先级处理。
- 测试快照里的英文。只有当它代表真实界面输出时才改。
- AI prompt / system prompt 片段。只有确认不会破坏模型行为、工具调用和协议格式时才改。

## 不该汉化

- 命令名、参数名、环境变量、配置键、JSON 字段、事件名、协议字段。
- API payload 的固定枚举值，例如 `post`、`text`、`interactive`、`message_type`。
- 文件路径、URL、包名、模块名、类名、函数名、测试名。
- provider/model 名称、token 名称、HTTP header、MIME type、正则表达式。
- 第三方品牌固定英文名。界面可显示 `飞书`，但代码协议里的 `feishu` / `lark` 不改。

## 验收门

- TUI：`npm run type-check`、`npx vitest run`、`npm run build` 至少通过一次。
- 飞书：`lark-cli doctor`、网关进程、`gateway_state.json`、近期 `gateway.log` 都要一致。
- 配置：`display.language = zh`、`display.gateway_locale = zh`、`feishu.outbound_format = post`。
- 插件：`lark-cli-toolbox` 在 `plugins.enabled` 中，且 doctor 明确说明 bot/user 哪个身份可用。
- 结论必须分层：能确认的说确认；缺用户登录、外部服务、真实消息截图的，要明确写成未完成或需复验。

## 当前重点范围

- `ui-tui/src`
- `gateway/platforms/feishu.py`
- `gateway/platforms/feishu_comment.py`
- `gateway/platforms/feishu_comment_rules.py`
- `gateway/runtime_footer.py`
- `gateway/display_config.py`
- `$HERMES_HOME/plugins/lark-cli-toolbox`
