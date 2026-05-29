import { describe, expect, it } from 'vitest'

import { isBundledTuiEntry, runtimeFreshnessWarningFromStats } from '../app/runtimeFreshness.js'

describe('runtime freshness warning', () => {
  it('warns when the bundled TUI entry was rebuilt after this process started', () => {
    const warning = runtimeFreshnessWarningFromStats({
      entryPath: 'E:/AI/hermes/hermes-agent/ui-tui/dist/entry.js',
      mtimeMs: 12_500,
      startedAtMs: 10_000
    })

    expect(warning).toContain('当前窗口仍在运行旧版本')
    expect(warning).toContain('重启 TUI 窗口')
  })

  it('ignores dev/source entries and same-start builds', () => {
    expect(isBundledTuiEntry('E:/AI/hermes/hermes-agent/ui-tui/src/entry.tsx')).toBe(false)
    expect(
      runtimeFreshnessWarningFromStats({
        entryPath: 'E:/AI/hermes/hermes-agent/ui-tui/dist/entry.js',
        mtimeMs: 10_500,
        startedAtMs: 10_000
      })
    ).toBe('')
  })
})
