# Hermes TUI / 飞书汉化交接

日期：2026-05-21  
继续目标：先保证 TUI 和飞书汉化可用，再考虑汉化包、发布包或扩展到其他平台。

## 当前状态

本轮已完成 TUI 与飞书入口的第一轮系统审查和修复。

2026-05-21 20:52 用户要求：Hermes TUI 先还原成官方原生，不再保留本地模板/皮肤实验。

已执行：

- 使用官方 `NousResearch/hermes-agent` `main.zip` 中的源码覆盖还原：
  - `ui-tui/`
  - `tui_gateway/`
- 已删除会影响或误导 TUI 使用的本地模板/皮肤：
  - `E:\AI\hermes\hermes-enhanced`
  - `E:\AI\hermes\skins\oldbai-*.yaml`
  - `G:\AI\research\tui-study` 下的 `vault` / `opencode` / `enhanced` TUI 模板与研究产物
  - `E:\AI\hermes\cache\hermes-agent-main*` 官方源码临时缓存
- 已清理 `E:\AI\hermes\config.yaml` 里的 TUI 自定义项：
  - `skin` 改回 `default`
  - `language` 改回 `en`
  - `busy_input_mode` 改回 `interrupt`
  - `streaming` 改回 `false`
  - 删除 `tui_modules`、`details_mode`、`sections`、`tui_statusbar` 等实验布局项
- 飞书配置保留，不随 TUI 还原一起回退。
- 当前后续本地项目产出统一放到：`E:\AI\github`。

还原验证：

- `ui-tui/` 和 `tui_gateway/` 源文件哈希与官方 zip 解压源码一致。
- `E:\AI\hermes\hermes-enhanced` 已不存在。
- `E:\AI\hermes\skins` 下已无 `oldbai-*.yaml`。
- `G:\AI\research\tui-study` 下已无 `vault` / `opencode` / `enhanced` / `template` / `oc-plugin` 相关条目。
- `E:\AI\hermes\cache` 下已无 `hermes-agent-main` 官方源码临时缓存。
- `npm --prefix ui-tui ci` 成功。
- `npm --prefix ui-tui run build` 成功，生成 `ui-tui/dist/entry.js`。
- TUI 入口相关 Python 测试：`13 passed`。
- `hermes --version` 正常：`Hermes Agent v0.14.0 (2026.5.16)`。

注意：

- `npm --prefix ui-tui run type-check` 在官方原生文件 `packages/hermes-ink/src/utils/execFileNoThrow.ts` 上报 TypeScript 类型错误；为保持 TUI 原生未改，没有为了通过检查修改官方源码。
- 如果后续要继续做 TUI 汉化或视觉方案，应另建项目放在 `E:\AI\github`，不要直接污染 `E:\AI\hermes\hermes-agent` 原生 TUI。

已建立审查机制：

- `scripts/audit-localization.ps1`
- `docs/localization-audit.md`
- `docs/localization-audit-current.md`
- `docs/localization-audit-findings.md`

历史记录：此前已处理过的 TUI 汉化项（当前已按用户要求还原为官方原生 TUI，不代表当前运行状态）：

- 启动输入跳过、默认图片提问、命令目录不可用。
- 语音连续模式提示、协议噪声提示、等待输入提示。
- 确认、sudo 密码、密钥输入等状态提示。
- 剪贴板图片、取消提示、忙碌状态、退出码显示。
- skill 相关加载、空消息、命令不明确、技能列表标题。
- 技能中心和 `/skills` 命令的普通说明词。
- 状态栏和 `/details` 帮助里的普通 `Agent` 说明词。
- 顶部状态栏瘦身：普通宽度隐藏路径；语音关闭不再显示，只在语音开启/录音/转写时显示。
- TUI 默认体验收敛：思考/工具默认折叠；启动页角色图默认关闭；启动页不再常驻显示工作路径；普通启动面板不再撑满整行。
- 可选模块文案统一：`monitorPanel` 改为“本轮概览”，移除开发占位文案；`deviceRail` 改为中文“状态侧栏”，不再显示 PIP-BOY 英文风格。
- TUI 配置兼容：`display.compact` 作为旧配置键会被 TUI 读取；`display.tui_compact` 仍然优先。
- 第二阶段视觉统一：待办区改成和思考/工具一致的树形标题与缩进；启动页小宽度 fallback 不再写死 `NOUS HERMES`；品牌副标题改为“本地 AI 工作台”。
- 新增 `/layout simple|workbench|debug`：`simple` 用于最清爽日常对话，`workbench` 作为默认工作台布局，`debug` 才打开侧栏、监控、角色面板和展开细节；模块开关会通过网关写回配置；本机 `E:\AI\hermes\config.yaml` 已切到 `workbench` 风格，默认关闭 `device_rail`。
- 后台任务、子代理数量、目标状态、顶部状态栏映射。

已处理的飞书显示文案：

- webhook HTTP 错误文本。
- 飞书消息解析占位：图片、附件、表情、富文本、合并转发、共享聊天、交互消息。
- 文件内容展示前缀、共享聊天详情、聊天 ID。
- 注册/连接 CLI 主要提示。
- `aiohttp` 缺失时的 webhook 模式提示。
- 飞书评论规则 CLI 常用输出。

已处理的飞书显示顺序：

- 状态气泡现在由 `gateway/platforms/feishu.py::on_processing_start()` 在收到消息后立即发送，不再放在 `_run_agent` 里等待模型初始化。
- 状态气泡按用户截图口径显示：
  - `⌛ 已收到，正在思考...`
  - `模型:`
  - `服务商:`
  - `上下文:`
- 工具执行过程保持一个状态气泡持续编辑更新；Feishu 不再因为中间正文消息触发 `__reset__` 后拆出多个“执行过程”气泡。
- 正式回复和中间正文仍然独立显示，不合并进状态气泡。

## 已验证

已通过：

```powershell
npm run type-check
npx vitest run src\__tests__\createSlashHandler.test.ts src\__tests__\createGatewayEventHandler.test.ts
E:\AI\hermes\hermes-agent\.venv\Scripts\python.exe -m pytest tests\gateway\test_feishu.py tests\gateway\test_feishu_comment.py tests\gateway\test_feishu_comment_rules.py -q -n0 --timeout=30 --timeout-method=thread
npm run build
.\scripts\audit-localization.ps1 -Scope all -Output docs\localization-audit-current.md
hermes --version
```

结果摘要：

- TUI type-check 通过。2026-05-21 继续时已重跑。
- TUI 相关测试：`93 passed`。
- 继续修复后补跑 `createSlashHandler`：`53 passed`。
- 新增技能中心汉化测试，补跑 `skillsHub + createSlashHandler`：`55 passed`。
- 继续补状态栏和 `/details` 帮助后，补跑 `createSlashHandler + statusBarTicker`：`56 passed`。
- 顶部状态栏瘦身后，补跑 `tuiSlotSmoke + statusBarTicker + useInputHandlers`：`17 passed`。
- TUI 默认体验收敛后，补跑 `details + tuiSlotSmoke + tuiModuleRegistry + useConfigSync + virtualHeights`：`65 passed`；`test_tui_display_defaults.py`：`1 passed`。
- 第二阶段视觉统一后，补跑 `details + tuiSlotSmoke + tuiModuleRegistry + useConfigSync + theme + todo`：`92 passed`，`type-check` 和 `build` 通过。
- 新增布局预设和模块持久化后，补跑 `createSlashHandler + details + tuiSlotSmoke + tuiModuleRegistry + useConfigSync + theme + todo`：`146 passed`；`test_tui_gateway_server.py`：`181 passed`；`type-check`、`eslint` 和 `build` 通过。
- 完整 TUI 测试：`823 passed, 3 skipped`。
- 飞书相关测试：`209 passed, 43 skipped`。
- 飞书显示二次纠偏后，补跑飞书/进度/页脚回归：`264 passed, 44 skipped`。
- 关键专项通过：
  - `test_feishu_keeps_one_progress_bubble_across_interim_messages`
  - `test_run_agent_feishu_progress_replies_inside_existing_thread`
- Feishu adapter 即时状态专项在当前环境因缺少 `lark_oapi` 按项目规则 skip；`gateway/platforms/feishu.py`、`gateway/run.py`、`gateway/display_config.py` 编译检查通过。
- TUI build 通过，生成 `ui-tui/dist/entry.js`。2026-05-21 继续时已重跑。
- 审查结果：`must_review 50`、`mixed_review 195`、`could_review 3781`、`skip_tech 1028`。
- TUI + 飞书旧目标英文精确扫描无残留。
- `hermes --version` 正常：`Hermes Agent v0.14.0`。

## 当前判断

剩余 `must_review` 不能直接等同于没汉化。当前剩余项主要是：

- 协议字段、配置键、事件名、JSON 字段、API 枚举值。
- 外部 payload 透传内容，例如用户原文、文件名、服务端返回摘要。
- 测试模拟输入和断言上下文。
- 内部状态值，它们已通过映射在界面层显示中文。

全局扫描还能看到 Discord、Slack、Telegram、QQBot、通用 webhook/API 的英文占位。这不是本轮 TUI/飞书入口问题；如果要做 Hermes 全平台中文化，需要单独开一轮。

## 入口状态

当前 PowerShell 会话里：

- `hermes` 是函数。
- `hermes` 和 `hermes tui` 都会走 `hermes.exe --tui`。
- 这个会话里没有识别到 `hermestui` 命令。

如果用户明天仍然看到 `hermestui`，需要在他的实际终端会话里重新查 alias/function/path，而不是只看当前 Codex 会话。

## 明天继续顺序

1. 先实际打开 TUI，按用户截图检查：顶部状态、思考区、技能/命令页、后台任务、图片粘贴提示。
2. 如果仍有英文，先用审查脚本定位，再按调用路径判断是否真实可见。
3. 复查飞书实际消息显示：普通消息、图片、附件、富文本、错误提示。
   - 飞书普通消息重点验收：收到后立刻出现状态气泡；本轮工具调用只占一个“执行过程”气泡；最终回复不带额外运行状态卡。
4. 如果当前 TUI/飞书都没问题，再决定是否扩展到其他平台英文占位。
5. 汉化包仍然先不做，等用户确认日常使用没问题后再封装。

## 注意

- 不要批量替换协议值、配置键、API 字段。
- 不要把外部平台原始内容强行翻译。
- 不要因为审查脚本报 `must_review` 就直接改，必须先判断是否面向用户可见。
- 当前仓库是用户本机工作区，`git status` 显示大量未跟踪文件，未要求提交前不要 stage/commit。
