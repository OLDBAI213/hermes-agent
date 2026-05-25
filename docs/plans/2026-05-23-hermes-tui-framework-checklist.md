# Goal

把 Hermes TUI 的可定制框架能力做成可验证的本地工程能力，而不是靠一次性提示词生成新壳。优先贴着现有 `ui-tui`、`tui_gateway`、`hermes_cli.skin_engine` 增量推进。

# Non-goals

- 不重写主聊天、输入框、滚动区、补全菜单或 JSON-RPC 通道。
- 不默认新增运行时依赖；只有现有能力无法覆盖并验证收益后才加库。
- 不直接改用户真实 `~/.hermes/config.yaml` 做验收；需要切换皮肤时用临时 `HERMES_HOME`。
- 不把 dashboard 另做一套聊天 UI；dashboard 继续嵌入真实 `hermes --tui`。

# Current hypothesis

当前最可靠路线是先做皮肤/ASCII 资产合同，再补 TUI 模块化入口，最后做布局和视觉验收。原因：仓库现有可用通道已经包括 `banner_logo`、`banner_hero`、`skin.changed`、`tui_status_indicator`，但当前源码里还没有可直接复用的 `tuiModuleRegistry` / `TuiSlotId` 文件，`display.tui_modules` 目前主要停在配置默认值。

# Framework decision

不要按“终极提示词”一次生成一个新 TUI 框架。正确做法是把现有 `hermes --tui` 变成可扩展框架：Python 继续负责配置、会话、工具、模型和 slash 命令；TypeScript/Ink 只负责屏幕、交互和可视模块。主聊天区、输入框、滚动区、补全菜单、JSON-RPC 通道是受保护核心，不重写。

框架分 5 层：

1. **配置合同层**：`display.tui_modules`、皮肤字段、状态栏字段是唯一入口；后端负责读写，前端负责归一化和渲染。配置必须支持旧 boolean 写法和新 object 写法。
2. **素材主题层**：皮肤提供颜色、品牌文案、`banner_logo`、`banner_hero`、指示器素材；组件只吃 `Theme.color` 和皮肤字段，不在组件里硬编码颜色系统。
3. **模块注册层**：每个模块必须有 `id`、`enabled`、`slot`、`priority`、`minCols` 和渲染组件。第一阶段先用固定渲染点，第二阶段再升级为 registry，避免一开始抽象过重。
4. **布局插槽层**：围绕主聊天区提供可插拔位置，例如 `status.left/right`、`message.user.after`、`assistant.activity`、`overlay`、未来的 `sidebar.left/right`。主流程不允许被模块截断。
5. **验收预览层**：所有皮肤和布局改动必须能用临时 `HERMES_HOME` 验收；先跑自动测试，再做真实 TUI 截图/录屏确认窄屏、宽屏、亮色终端。

推进顺序固定为：

1. **先稳合同**：配置读写、前端状态、模块开关、测试。
2. **再做素材**：主题包、ASCII/Braille/宽字符、预览样例。
3. **再做布局**：状态栏、活动流、任务面板、侧栏插槽。
4. **最后做生态**：主题导入导出、社区素材库、更多模块、国际化增强。

明确不做：

- 不把 dashboard 另写成第二套聊天 UI。
- 不引入新的 TUI 框架替换 Ink。
- 不把 ASCII 生成库作为运行时依赖。
- 不在没有真实截图验收的情况下声称视觉完成。

# Inventory

## Local project

- 主工程：`E:\AI\hermes\hermes-agent`
- TUI 前端：`ui-tui/src`
- TUI 后端：`tui_gateway`
- 皮肤系统：`hermes_cli/skin_engine.py`
- 配置默认值：`hermes_cli/config.py`
- 计划文件：`docs/plans/2026-05-23-hermes-tui-framework-checklist.md`

## Tools needed

- 搜索/定位：`rg`、PowerShell
- TypeScript 验证：`npm test`、`npm run type-check`、`npm run build`
- 局部 lint：`npx eslint <changed files>`
- Python 验证：`uv run python -m pytest -n0 --timeout-method=thread <target tests>`
- 可视验收：真实 `hermes --tui` 终端截图或录屏；必要时用 dashboard 的 `/chat` 做嵌入检查

## Existing libraries to use

- `React` + `Ink` / `@hermes/ink`
- `nanostores`
- `unicode-animations`
- `Vitest`
- `ESLint` / `TypeScript`
- Python stdlib + existing `skin_engine.py` YAML loader

## Libraries not needed yet

- 暂不引入 `@inkjs/ui`：现有控件和 `@hermes/ink` 已覆盖当前范围。
- 暂不引入 `i18next`：Hermes 已有 `display.language` 和本地化系统，先接现有机制。
- 暂不引入 ASCII 生成库作为运行时依赖：ASCII 资产先作为皮肤 YAML / 测试样例进入。
- 暂不引入新 TUI 框架：现有 `ui-tui` 是唯一主入口。

## External projects to evaluate later

- `joeynyc/hermes-skins`：借鉴皮肤结构和 ASCII 资产风格，不直接并入。
- `H-Ali13381/hermes-theme-workshop`：借鉴主题生成流程，不直接绑定。
- `ASCIINova` / `Python art` / `TerminalTextEffects` / `braille-art`：只作为素材生成或灵感来源；不得变成 Hermes 运行时依赖，除非单独验证。
- `create-giggles-app` / `ink-cli-starter`：只作参考，不替换 Hermes TUI。

## Assets needed

- 皮肤 YAML 样例：至少 2 个，覆盖深色和浅色终端。
- `banner_logo` 样例：宽版、窄版 fallback 都要验收。
- `banner_hero` 样例：宽字符/Braille/纯 ASCII 至少各一类测试。
- 多色 rich markup 样例：同一行多个颜色片段。
- 忙碌指示器样例：现有 `ascii` / `unicode` / `emoji` / `kaomoji` 的兼容测试。

# Files under investigation

- `ui-tui/src/banner.ts`
- `ui-tui/src/components/branding.tsx`
- `ui-tui/src/theme.ts`
- `ui-tui/src/app/useConfigSync.ts`
- `ui-tui/src/app/interfaces.ts`
- `ui-tui/src/components/appLayout.tsx`
- `ui-tui/src/components/appChrome.tsx`
- `ui-tui/src/__tests__/banner.test.ts`
- `ui-tui/src/__tests__/theme.test.ts`
- `ui-tui/src/__tests__/useConfigSync.test.ts`
- `hermes_cli/skin_engine.py`
- `hermes_cli/config.py`
- `tui_gateway/server.py`
- `tui_gateway/entry.py`

# Implementation checklist

## 1. Skin and ASCII asset contract

- [x] Fix rich-markup banner parsing so one visual line can contain multiple color spans.
- [x] Measure banner width by terminal display cells, not JavaScript string length.
- [x] Add Python-side skin tests for `banner_logo` / `banner_hero` user YAML loading.
- [x] Add a safe sample skin asset fixture with wide-character and ASCII variants.
- [ ] Add a temp-`HERMES_HOME` smoke path for `/skin <name>` without touching the real user config.

## 2. TUI config and module surface

- [x] Confirm actual current state of `display.tui_modules` from config to frontend.
- [x] Add a minimal typed frontend contract for TUI module visibility.
- [x] Decide whether to implement slot registry now or first expose fixed extension points in `appLayout`.
- [x] Keep optional modules disabled unless explicitly enabled by config.
- [x] Test old boolean config and object config if object form is introduced.

## 3. Visible TUI surfaces

- [x] Keep main transcript, composer, scroll, and completion menu untouched unless required.
- [x] Add any new panel only through a narrow render point.
- [ ] Validate narrow terminal fallback: logo becomes text, side art hides or shrinks.
- [ ] Validate wide terminal view: banner/hero does not push input line out.

## 4. Theme and color behavior

- [x] Keep colors sourced from existing `Theme.color`, not hard-coded inside components.
- [ ] Verify light terminal handling with `HERMES_TUI_THEME=light`.
- [ ] Verify truecolor and non-truecolor behavior when skin colors are bright.
- [ ] Avoid one-off color systems outside `theme.ts` / `skin_engine.py`.

## 5. Validation

- [x] `npm test -- src/__tests__/banner.test.ts src/__tests__/theme.test.ts src/__tests__/useConfigSync.test.ts src/__tests__/tuiModules.test.ts`
- [x] `npm run type-check`
- [x] `npm run build`
- [x] `npx eslint <changed files>`
- [x] Targeted Python tests for skin/config changes.
- [x] Built TUI bundle starts safely in non-TTY smoke (`node dist\entry.js` exits with `hermes-tui: no TTY`).
- [ ] Real TUI visual smoke with temporary config and screenshot/capture.

# Open blockers

- Current `npm run lint` has unrelated existing errors across many files. For this track, use targeted lint on changed files unless the task is lint cleanup.
- Current full `npm test` has unrelated Windows/localization failures in existing suites (`editor`, `terminalSetup`, `terminalParity`, `subagentTree`, `messages`, `createGatewayEventHandler`, `cursorDriftRegression`). Targeted tests for this change pass.
- The remembered `tuiModuleRegistry` / `TuiSlotId` files are not present in the current `E:\AI\hermes\hermes-agent` checkout. Treat current filesystem as source of truth.
- External skin/theme repositories must be evaluated in isolated checkouts before any adoption.
