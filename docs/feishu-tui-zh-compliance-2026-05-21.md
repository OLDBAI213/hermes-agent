# 飞书汉化包与 TUI 汉化对照检查

日期：2026-05-21  
对照对象：`OLDBAI213/hermes-feishu-zh` `main` 分支，版本 `0.2.0`。  
本机对象：`E:\AI\hermes` / `E:\AI\hermes\hermes-agent`。

## 结论

飞书侧：源码汉化基本符合已发布的 `hermes-feishu-zh`，但发布包 `stable.config.yaml` 的显示配置不符合当前实测期望。  
TUI 侧：此前符合 `hermes-tui-zh` 拆包方向；但 2026-05-21 20:52 用户要求先还原官方原生 TUI，当前本机 TUI 已不再保留这些汉化/布局实验。  
当前飞书配置已改回用户截图确认的原版顺序显示：收到消息后立即发状态气泡；正文/中间回复独立显示；本轮工具调用合并在同一个“执行过程”气泡里持续编辑；最后再发正式回复。不再把运行状态作为最终回复后的独立卡片发送。

## 飞书包对照

`hermes-feishu-zh` 当前要求：

- `display.language = zh`
- `display.gateway_locale = zh`
- `display.platforms.feishu.tool_progress = new`
- `display.platforms.feishu.show_reasoning = false`
- `platforms.feishu.enabled = true`
- `platforms.feishu.extra.outbound_format = post`
- `platforms.feishu.extra.card_mode = false`
- `plugins.enabled` 包含 `lark-cli-toolbox`

本机检查结果（2026-05-21 18:30 初查）：

- 源码汉化和插件配置基本匹配。
- `E:\AI\hermes\plugins\lark-cli-toolbox` 存在。
- `platform_toolsets.cli` 和 `platform_toolsets.feishu` 均包含 `lark_cli`。
- 飞书相关测试通过：`209 passed, 43 skipped`。

实测修正（2026-05-21 19:39）：

- 用户截图确认 `runtime_footer.delivery = status_card` 会破坏原版顺序显示。
- 已将本机配置改为：
  - `display.platforms.feishu.interim_assistant_messages = true`
  - `display.platforms.feishu.runtime_footer.enabled = false`
  - `display.platforms.feishu.runtime_footer.delivery = inline`
  - `display.platforms.feishu.tool_progress = new`
  - `display.platforms.feishu.cleanup_progress = false`
- 已重启 Gateway，PID: `11756`。

二次纠偏（2026-05-21 20:03）：

- 用户截图确认：状态气泡必须在 Feishu adapter 收到消息后立刻发出，不能等 `_run_agent` 初始化模型后再发。
- 已删除 `_run_agent` 中的延迟状态发送逻辑。
- 状态发送入口改为 `gateway/platforms/feishu.py::on_processing_start()`：
  - 第一行：`⌛ 已收到，正在思考...`
  - 后续多行：`模型:` / `服务商:` / `上下文:`
  - 服务商显示使用 `get_auth_provider_display_name()`，例如 `xiaomi` 显示为 `小米 MiMo`。
  - 上下文从 `sessions.json` 的 `last_prompt_tokens` 和 `model.context_length` 计算，格式为 `约 221K / 1M (21%)`。
- Feishu 的工具进度不再因为正文/中间消息落地而重开新气泡：
  - `GatewayStreamConsumer.on_new_message` 对 Feishu 不再注入 `__reset__`。
  - 同一轮工具调用应保留在一个“执行过程”气泡中编辑更新。
- 本机配置新增/确认：
  - `display.platforms.feishu.processing_start_message = true`
  - `display.platforms.feishu.tool_progress = new`
  - `display.platforms.feishu.runtime_footer.enabled = false`
- 已重启 Gateway，PID: `26544`。

源码替换对照：

- `feishu-card-zh.replacements.json` 共 77 条。
- 大部分替换已经应用。
- 7 条显示为 `MISSING`，原因是本机源码已经没有旧英文或代码结构已经变化，不是明确漏汉化：
  - `FALLBACK_EMOJI_TEXT = "[Emoji]"`
  - `Invalid JSON`
  - `Encrypted webhook body not supported`
  - `User:`
  - `Enabled:`
  - `Policy:`
  - `Unknown command`
- 增强显示补丁已具备核心能力：`outbound_format`、`card_mode`、`_build_markdown_card_payload()`、`_build_outbound_payload()` 都存在。
- 本机增强卡片标题已是 `Hermes · 飞书`，比发布包里的基础 `Hermes` 更贴近中文飞书场景。

判断：

- 飞书包源码汉化与本机实现基本一致。
- 飞书包的默认显示配置需要更新，不能继续默认启用 `runtime_footer.status_card`。
- 本机没有发现需要按发布包补回的飞书汉化缺口。
- 发布包下一版应恢复原版顺序显示，把运行状态卡作为可选项，而不是 stable 默认项。

## TUI 汉化检查

状态更新（2026-05-21 20:52）：

- 用户要求 Hermes TUI 先还原成官方原生。
- 已用官方 `NousResearch/hermes-agent` `main.zip` 中的 `ui-tui/`、`tui_gateway/` 覆盖本机对应目录。
- 已删除本地 TUI 模板/皮肤：
  - `E:\AI\hermes\hermes-enhanced`
  - `E:\AI\hermes\skins\oldbai-*.yaml`
  - `G:\AI\research\tui-study` 下的 `vault` / `opencode` / `enhanced` TUI 模板与研究产物
  - `E:\AI\hermes\cache\hermes-agent-main*` 官方源码临时缓存
- 已将 `E:\AI\hermes\config.yaml` 的 TUI 相关显示配置恢复为官方默认口径：
  - `skin: default`
  - `language: en`
  - `busy_input_mode: interrupt`
  - `streaming: false`
  - 删除 `tui_modules`、`details_mode`、`sections`、`tui_statusbar` 等实验布局项。
- 验证：`ui-tui/`、`tui_gateway/` 源文件哈希与官方 zip 一致；`npm --prefix ui-tui run build` 成功；TUI 入口相关 Python 测试 `13 passed`。
- 后续 TUI 汉化或视觉方案必须另建项目，放在 `E:\AI\github`，不要直接污染 `E:\AI\hermes\hermes-agent` 原生 TUI。

以下为还原前的历史检查记录，不代表当前运行状态。

已具备能力：

- 启动页、帮助、命令提示、技能中心中文化。
- 思考、工具、待办、后台任务、子代理、目标状态等核心可见区域中文化。
- 顶部状态栏中文状态映射完整，包括：
  - `ready` -> `就绪`
  - `running…` -> `运行中…`
  - `gateway startup timeout` -> `网关启动超时`
  - `setup required` -> `需要设置`
  - `summoning hermes…` -> `正在启动 Hermes…`
- 默认体验已收敛：
  - 思考/工具默认折叠。
  - 角色面板默认关闭。
  - 侧栏默认关闭。
  - 状态栏不再常驻显示路径和语言。
- `/layout simple|workbench|debug` 已实现，并能持久化模块开关。

审查脚本结果：

- `Scope tui`
- `must_review = 30`
- `mixed_review = 151`
- `could_review = 2540`
- `skip_tech = 628`

人工判断：

- `must_review` 里大部分是协议字段、内部状态值、类型字段或外部 payload 透传，不应直接翻译。
- 当前真正需要继续盯的不是“扫描数字清零”，而是实际 TUI 截图和日常交互里是否还有英文。
- 审查脚本仍有假阳性，后续应增加 allowlist 或分类规则，避免把内部字段误报成可见文案。

验证：

- TUI 相关测试通过：`146 passed`。
- 飞书/进度/页脚回归通过：`264 passed, 44 skipped`。
- 关键专项：
  - `test_feishu_keeps_one_progress_bubble_across_interim_messages`
  - `test_run_agent_feishu_progress_replies_inside_existing_thread`
- Feishu adapter 的即时状态测试在当前环境因缺少 `lark_oapi` 按项目规则 skip；相关实现已通过编译检查。

## 是否符合拆包标准

`hermes-feishu-zh`：

- 已符合。
- 当前本机实现和发布包对齐。
- 后续只需要把本机新增增强整理成版本更新候选。

`hermes-tui-zh`：

- 功能上基本符合。
- 还缺项目外壳：
  - `install.ps1`
  - `verify.ps1`
  - `manifest.json`
  - TUI 补丁文件
  - 回滚策略
  - README / install / troubleshooting 文档

## 下一步

1. 不再继续改飞书汉化，除非实际飞书消息截图出现英文。
2. 继续用 TUI 一轮，重点看：
   - 启动页。
   - `/help`。
   - `/skills`。
   - 思考/工具展开。
   - `/layout simple|workbench|debug`。
   - 错误、确认、回滚、浏览器、技能加载提示。
3. 若 TUI 体验确认没问题，再整理 `hermes-tui-zh` 项目外壳。
4. 审查脚本后续要升级：把协议字段、内部状态、类型名、外部 payload 透传从 `must_review` 中降级。
