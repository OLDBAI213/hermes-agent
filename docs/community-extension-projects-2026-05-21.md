# Hermes 社区扩展项目清单

日期：2026-05-21  
用途：整理当前已经做过、正在打磨、以及后续可拆成独立 GitHub 项目的 Hermes 扩展方向。  
原则：先把能直接给用户带来体验提升的项目打包；还没验证的方向只保留为候选，不提前承诺。

## 已发布

### `hermes-feishu-zh`

定位：Hermes 飞书中文增强包。

状态：已发布。

已包含或应保持的能力：

- 飞书消息中文显示。
- 图片、附件、富文本、合并转发、共享聊天等占位文案中文化。
- 飞书错误提示、连接提示、CLI 注册提示中文化。
- 飞书侧默认少展示推理过程，避免移动端刷屏。
- `post` 输出和状态卡显示优化。
- 后续可继续承载 `lark-cli` 个人工具箱，等能力变多后再拆。

后续维护重点：

- 跟随 Hermes 上游飞书插件变化做兼容。
- 每次升级后跑飞书显示验证。
- 保持安装、回滚、验证流程简单。

## 可立即整理成项目

### `hermes-tui-zh`

定位：Hermes TUI 中文体验增强包。

状态：已有本机实物，适合作为下一个项目。

当前可打包内容：

- TUI 可见英文中文化。
- 启动页、帮助、技能中心、命令提示中文化。
- 思考、工具、后台任务、子代理、目标状态等显示文案整理。
- 顶部状态栏瘦身：隐藏常驻路径、语言等低价值信息。
- 默认体验优化：思考/工具默认折叠，角色面板默认关闭。
- `/layout simple|workbench|debug` 布局预设。
- `simple`：最清爽日常对话。
- `workbench`：默认工作台，保留状态和待办，不显示拥挤侧栏。
- `debug`：排查问题时打开侧栏、监控、角色面板和展开细节。
- 汉化审查脚本和审查报告。

建议仓库结构：

```text
hermes-tui-zh/
├── install.ps1
├── verify.ps1
├── manifest.json
├── patches/
│   ├── tui-zh.replacements.json
│   ├── tui-layout-presets.patch
│   └── tui-display-defaults.patch
├── docs/
│   ├── README.md
│   ├── install.md
│   ├── upgrade.md
│   └── troubleshooting.md
└── tests/
    └── smoke.ps1
```

验收条件：

- `hermes --version` 正常。
- TUI 能启动。
- `/layout simple`、`/layout workbench`、`/layout debug` 都能切换。
- 重启后布局核心配置仍保留。
- 常见命令、技能中心、思考区、工具区没有明显英文残留。

### `hermes-layout-presets`

定位：Hermes TUI 布局预设包。

状态：不建议第一时间单独拆，先并入 `hermes-tui-zh`。

可拆条件：

- 后续出现更多布局，如 mobile、wide、focus、coding、review。
- 布局预设不再只服务中文化，而是成为通用 TUI 体验能力。
- 上游 Hermes 愿意接收布局机制，但不接收中文化内容。

当前处理建议：

- 先作为 `hermes-tui-zh` 的一个模块维护。
- 等布局预设稳定后，再考虑独立仓库。

## 第二阶段项目

### `hermes-continuity`

定位：Hermes 跨入口、跨上下文连续工作流。

状态：方向明确，但还没有完整产品级实现。

目标场景：

- 在家用 CLI。
- 出门用飞书。
- 回家后能从 CLI 接上飞书里的上下文。
- 电脑重启后能恢复当前任务状态。
- 不把用户逼着手动复制上下文。

应包含能力：

- 会话索引。
- 当前任务摘要。
- 最近上下文快照。
- CLI / 飞书入口共用同一套 Hermes 会话状态。
- `/resume` 或类似入口能恢复最近任务。
- 重要任务可生成 handoff。
- 重启后能明确告诉用户当前可恢复的会话。

第一版边界：

- 只支持个人单用户。
- 不做多人协作。
- 不做群聊同步。
- 不保证所有平台消息完全一致，只保证任务连续。

建议仓库结构：

```text
hermes-continuity/
├── install.ps1
├── verify.ps1
├── manifest.json
├── plugins/
│   └── continuity/
├── docs/
│   ├── README.md
│   ├── cli-to-feishu.md
│   ├── feishu-to-cli.md
│   └── recovery.md
└── tests/
    └── continuity-smoke.ps1
```

验收条件：

- CLI 创建的会话能被记录。
- 飞书入口能看到最近任务摘要。
- 重启后能列出可恢复会话。
- 恢复后不会丢模型、工具、飞书配置。

### `hermes-lark-cli-toolbox`

定位：Hermes 飞书个人生产力工具箱。

状态：可以先在 `hermes-feishu-zh` 内继续长，成熟后拆出。

适合能力：

- 飞书 IM：个人消息、搜索、附件下载。
- 飞书文档：创建、读取、整理、更新。
- 飞书表格：读写单元格、导出、追加数据。
- 飞书多维表格：表、字段、记录、视图。
- 飞书日历：日程、忙闲、提醒。
- 飞书任务：个人待办、任务拆分、状态同步。

第一版边界：

- 只服务个人 AI 助手场景。
- 不主打群管理、审批流、组织通讯录管理。
- 先做常用工作流封装，不追求覆盖所有 OpenAPI。

## 后续候选项目

### `hermes-browser-automation`

定位：Hermes 浏览器执行能力扩展。

状态：还没正式做，适合排在 TUI 和 continuity 后。

目标能力：

- 使用本机浏览器登录态。
- 打开网页、读取页面、点击、输入。
- 对常用网站形成可复用动作模板。
- 支持“查网页、整理、回填到飞书/文档”的个人工作流。

验收条件：

- 能稳定连接 Chrome 或内置 browser。
- 能读取真实页面正文。
- 能执行二级页面跳转。
- 能把结果返回 Hermes，而不是只停在浏览器操作。

### `hermes-xhs-cli`

定位：Hermes 小红书内容工作流。

状态：概念候选，暂不建议马上做。

可能能力：

- 搜索笔记。
- 读取笔记内容。
- 整理选题素材。
- 草稿辅助。
- 发布前检查。

风险：

- 平台规则和页面结构变化快。
- 自动化边界需要单独确认。
- 现在没有足够本机验证，不能作为近期主项目。

## 推荐推进顺序

1. `hermes-tui-zh`
   - 当前已有真实代码和验证结果。
   - 你每天会用，最容易发现问题。
   - 最适合作为 `hermes-feishu-zh` 后的第二个项目。

2. `hermes-continuity`
   - 这是“在家 CLI，出门飞书”的核心卖点。
   - 需要单独设计和验证，不能混在汉化项目里。

3. `hermes-lark-cli-toolbox`
   - 先随着 `hermes-feishu-zh` 继续增强。
   - 等命令和工作流稳定后再拆仓库。

4. `hermes-browser-automation`
   - 等核心入口和上下文稳定后再做。

5. `hermes-xhs-cli`
   - 先保留为候选，不作为近期主线。

## 当前结论

近期真正值得做成项目的只有两个：

- `hermes-tui-zh`
- `hermes-continuity`

`hermes-layout-presets` 先并进 `hermes-tui-zh`。  
`hermes-lark-cli-toolbox` 先并进 `hermes-feishu-zh`。  
`hermes-browser-automation` 和 `hermes-xhs-cli` 等核心体验稳定后再开。
