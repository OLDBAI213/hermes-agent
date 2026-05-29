import { describe, expect, it } from 'vitest'

import { isBundledTuiEntry, runtimeFreshnessWarningFromStats } from '../app/runtimeFreshness.js'
import { formatToolCall, isTransientTrailLine, thinkingPreview } from '../lib/text.js'

const ENGLISH_REASONING_RE = /\b(?:Let me|I need to|I should|The path resolution is wrong|thinking|reasoning)\b/i

describe('TUI display contract', () => {
  it('renders common tool calls as Chinese UI labels instead of function-call text', () => {
    const samples = [
      ['cronjob', 'list', '⏰ 定时任务：查看列表'],
      ['cronjob', 'remove', '⏰ 定时任务：删除任务'],
      ['read_file', 'E:/AI/hermes/config.yaml', '📖 读取文件：E:/AI/hermes/config.yaml'],
      ['terminal', 'npm run build --prefix ui-tui', '💻 终端：命令 npm run build --prefix ui-tui'],
      ['browser_navigate', 'https://www.vulbox.com/my/vuln', '🌐 浏览器跳转：打开 https://www.vulbox.com/my/vuln'],
      ['browser_click', '@e55', '🖱️ 浏览器点击：点击 @e55'],
      ['search_files', 'TurnPhase', '🔎 搜索文件：关键词 TurnPhase']
    ] as const

    for (const [name, context, expected] of samples) {
      const label = formatToolCall(name, context)

      expect(label).toBe(expected)
      expect(label).not.toMatch(/\w+\("/)
      expect(label).not.toContain('("')
      expect(label).toContain('：')
    }
  })

  it('does not expose provider English reasoning prose in the thinking panel', () => {
    const samples = [
      'The path resolution is wrong. Let me fix the path and try again.',
      'Let me inspect the config first. I should check whether reasoning is enabled.',
      '**Planning tool execution**\nI can run tools.\n**Determining weather search parameters**'
    ]

    for (const sample of samples) {
      const preview = thinkingPreview(sample, 'full')

      expect(preview).not.toMatch(ENGLISH_REASONING_RE)
      expect(preview).toMatch(/[一-龥]/)
    }
  })

  it('keeps model wait/progress lines transient so the live trail does not pile up', () => {
    expect(isTransientTrailLine('模型：等待模型响应 #3…')).toBe(true)
    expect(isTransientTrailLine('模型：模型响应过慢 · 已等 90s · Ctrl+C 可中断')).toBe(true)
    expect(isTransientTrailLine('正在分析工具输出…')).toBe(true)
  })

  it('warns when a running bundled TUI is older than the rebuilt dist entry', () => {
    expect(isBundledTuiEntry('E:/AI/hermes/hermes-agent/ui-tui/dist/entry.js')).toBe(true)
    expect(
      runtimeFreshnessWarningFromStats({
        entryPath: 'E:/AI/hermes/hermes-agent/ui-tui/dist/entry.js',
        mtimeMs: 12_500,
        startedAtMs: 10_000
      })
    ).toContain('当前窗口仍在运行旧版本')
  })
})
