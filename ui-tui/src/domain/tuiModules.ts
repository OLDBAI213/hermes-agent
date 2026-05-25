export interface TuiModuleConfig {
  compact?: boolean
  enabled: boolean
  minCols?: number
  position?: string
  priority?: number
  slot?: string
}

export type TuiModules = Record<string, TuiModuleConfig>

export const DEFAULT_TUI_MODULES: TuiModules = {
  activity_scan: { enabled: true },
  character_panel: { enabled: false },
  monitor_panel: { enabled: false },
  status_meter: { enabled: true },
  task_panel: { enabled: true }
}

const truthy = new Set(['1', 'true', 'yes', 'on'])
const falsey = new Set(['0', 'false', 'no', 'off'])

const normalizeEnabled = (raw: unknown, fallback = true): boolean => {
  if (raw === true || raw === 1) {
    return true
  }

  if (raw === false || raw === 0) {
    return false
  }

  if (typeof raw === 'string') {
    const value = raw.trim().toLowerCase()

    if (truthy.has(value)) {
      return true
    }

    if (falsey.has(value)) {
      return false
    }
  }

  return fallback
}

const normalizeNumber = (raw: unknown): number | undefined => {
  const value = typeof raw === 'number' ? raw : typeof raw === 'string' ? Number(raw.trim()) : Number.NaN

  return Number.isFinite(value) && value > 0 ? Math.floor(value) : undefined
}

export const normalizeTuiModuleConfig = (raw: unknown, fallback?: TuiModuleConfig): TuiModuleConfig => {
  if (typeof raw === 'boolean' || typeof raw === 'number' || typeof raw === 'string') {
    return { ...(fallback ?? {}), enabled: normalizeEnabled(raw, fallback?.enabled ?? true) }
  }

  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) {
    return { ...(fallback ?? {}), enabled: fallback?.enabled ?? true }
  }

  const source = raw as Record<string, unknown>
  const minCols = normalizeNumber(source.minCols ?? source.min_cols)
  const compact = typeof source.compact === 'boolean' ? source.compact : fallback?.compact
  const position = typeof source.position === 'string' ? source.position : fallback?.position
  const slot = typeof source.slot === 'string' ? source.slot : fallback?.slot
  const priority = normalizeNumber(source.priority) ?? fallback?.priority

  return {
    ...(fallback ?? {}),
    enabled: normalizeEnabled(source.enabled, fallback?.enabled ?? true),
    ...(compact !== undefined && { compact }),
    ...(minCols !== undefined && { minCols }),
    ...(position && { position }),
    ...(priority !== undefined && { priority }),
    ...(slot && { slot })
  }
}

export const normalizeTuiModules = (raw: unknown): TuiModules => {
  const modules: TuiModules = Object.fromEntries(
    Object.entries(DEFAULT_TUI_MODULES).map(([id, config]) => [id, { ...config }])
  )

  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) {
    return modules
  }

  for (const [id, value] of Object.entries(raw as Record<string, unknown>)) {
    modules[id] = normalizeTuiModuleConfig(value, modules[id])
  }

  return modules
}

export const isTuiModuleEnabled = (modules: TuiModules, id: string, cols?: number): boolean => {
  const config = modules[id] ?? DEFAULT_TUI_MODULES[id]

  if (!config?.enabled) {
    return false
  }

  return cols === undefined || config.minCols === undefined || cols >= config.minCols
}
