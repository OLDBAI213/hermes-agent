import { statSync } from 'node:fs'
import { resolve } from 'node:path'

export const RUNTIME_FRESHNESS_POLL_MS = 15_000
export const RUNTIME_FRESHNESS_GRACE_MS = 2_000
export const runtimeStartedAtMs = Date.now()

const normalizePath = (path: string) => path.replace(/\\/g, '/')

export const isBundledTuiEntry = (entryPath?: string) =>
  Boolean(entryPath && normalizePath(resolve(entryPath)).endsWith('/dist/entry.js'))

export const runtimeFreshnessWarningFromStats = ({
  entryPath,
  graceMs = RUNTIME_FRESHNESS_GRACE_MS,
  mtimeMs,
  startedAtMs
}: {
  entryPath?: string
  graceMs?: number
  mtimeMs: number
  startedAtMs: number
}) => {
  if (!isBundledTuiEntry(entryPath)) {
    return ''
  }

  if (mtimeMs <= startedAtMs + graceMs) {
    return ''
  }

  return '检测到 TUI 已在后台重新构建，但当前窗口仍在运行旧版本；请重启 TUI 窗口加载最新显示修复。'
}

export const runtimeFreshnessWarning = (
  entryPath = process.argv[1],
  startedAtMs = runtimeStartedAtMs,
  env = process.env
) => {
  if (env.HERMES_TUI_DISABLE_STALE_WARN === '1') {
    return ''
  }

  if (!isBundledTuiEntry(entryPath)) {
    return ''
  }

  try {
    return runtimeFreshnessWarningFromStats({
      entryPath,
      mtimeMs: statSync(entryPath).mtimeMs,
      startedAtMs
    })
  } catch {
    return ''
  }
}
