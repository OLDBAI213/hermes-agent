export interface TuiModuleConfig {
  compact?: boolean
  enabled: boolean
  minCols?: number
  position?: string
  priority?: number
  slot?: string
}

export type TuiModules = Record<string, TuiModuleConfig>

export const TUI_EXTENSION_NAME = 'hermes-tui-extension-core'
export const TUI_EXTENSION_VERSION = '0.2.0'
export const TUI_EXTENSION_PROTOCOL_VERSION = 1

export const TUI_SLOT_IDS = [
  'intro.summary',
  'intro.detail',
  'status.left',
  'status.right',
  'transcript.live_tail',
  'overlay.panel'
] as const

export type TuiSlotId = (typeof TUI_SLOT_IDS)[number]

export const TUI_MODULE_STATES = ['disabled', 'loading', 'ok', 'warning', 'stale', 'error', 'incompatible'] as const

export type TuiModuleState = (typeof TUI_MODULE_STATES)[number]

export interface TuiModuleSnapshot {
  data?: Record<string, unknown>
  detail?: string
  error?: {
    code?: string
    hint?: string
    message: string
  }
  expiresAt?: number
  id: string
  minCols?: number
  priority?: number
  slot?: TuiSlotId
  state: TuiModuleState
  summary?: string
  title?: string
  updatedAt?: number
  version?: string
}

export const DEFAULT_TUI_MODULES: TuiModules = {
  activity_scan: { enabled: true },
  character_panel: { enabled: false },
  monitor_panel: { enabled: false },
  status_meter: { enabled: true },
  task_panel: { enabled: true }
}

const truthy = new Set(['1', 'true', 'yes', 'on'])
const falsey = new Set(['0', 'false', 'no', 'off'])
const slotIds: ReadonlySet<string> = new Set(TUI_SLOT_IDS)
const moduleStates: ReadonlySet<string> = new Set(TUI_MODULE_STATES)

const positionSlots: Record<string, TuiSlotId> = {
  activity: 'transcript.live_tail',
  bottom: 'transcript.live_tail',
  detail: 'intro.detail',
  intro: 'intro.summary',
  overlay: 'overlay.panel',
  side: 'status.right',
  status: 'status.right',
  top: 'intro.summary',
  transcript: 'transcript.live_tail'
}

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

const normalizeString = (raw: unknown): string | undefined =>
  typeof raw === 'string' && raw.trim() ? raw.trim() : undefined

const normalizeTimestamp = (raw: unknown): number | undefined => {
  const value = typeof raw === 'number' ? raw : typeof raw === 'string' ? Number(raw.trim()) : Number.NaN

  return Number.isFinite(value) && value > 0 ? value : undefined
}

export const isTuiSlotId = (raw: unknown): raw is TuiSlotId => typeof raw === 'string' && slotIds.has(raw)

export const normalizeTuiSlotId = (raw: unknown, fallback?: TuiSlotId): TuiSlotId | undefined =>
  isTuiSlotId(raw) ? raw : fallback

export const normalizeTuiModuleState = (raw: unknown, fallback: TuiModuleState = 'ok'): TuiModuleState =>
  typeof raw === 'string' && moduleStates.has(raw) ? (raw as TuiModuleState) : fallback

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

export const tuiModuleConfigFor = (modules: TuiModules, id: string): TuiModuleConfig | undefined =>
  modules[id] ?? DEFAULT_TUI_MODULES[id]

export const isTuiModuleEnabled = (modules: TuiModules, id: string, cols?: number): boolean => {
  const config = tuiModuleConfigFor(modules, id)

  if (!config?.enabled) {
    return false
  }

  return cols === undefined || config.minCols === undefined || cols >= config.minCols
}

export const resolveTuiModuleSlot = (
  config?: TuiModuleConfig,
  fallback: TuiSlotId = 'transcript.live_tail'
): TuiSlotId =>
  normalizeTuiSlotId(config?.slot) ?? positionSlots[(config?.position ?? '').trim().toLowerCase()] ?? fallback

export const effectiveTuiModuleSnapshot = (snapshot: TuiModuleSnapshot, now = Date.now()): TuiModuleSnapshot => {
  if (
    snapshot.expiresAt &&
    snapshot.expiresAt <= now &&
    snapshot.state !== 'disabled' &&
    snapshot.state !== 'error' &&
    snapshot.state !== 'incompatible'
  ) {
    return { ...snapshot, state: 'stale' }
  }

  return snapshot
}

export const isTuiModuleVisible = (
  modules: TuiModules,
  snapshot: TuiModuleSnapshot,
  slot: TuiSlotId,
  cols?: number,
  now = Date.now()
): boolean => {
  const effective = effectiveTuiModuleSnapshot(snapshot, now)

  if (effective.state === 'disabled') {
    return false
  }

  const config = tuiModuleConfigFor(modules, effective.id)
  const resolvedSlot = effective.slot ?? resolveTuiModuleSlot(config)
  const minCols = effective.minCols ?? config?.minCols

  if (resolvedSlot !== slot) {
    return false
  }

  if (!isTuiModuleEnabled(modules, effective.id, cols)) {
    return false
  }

  return cols === undefined || minCols === undefined || cols >= minCols
}

export const normalizeTuiModuleSnapshot = (raw: unknown): TuiModuleSnapshot | null => {
  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) {
    return null
  }

  const source = raw as Record<string, unknown>
  const id = normalizeString(source.id)

  if (!id) {
    return null
  }

  const detail = normalizeString(source.detail)

  const error =
    source.error && typeof source.error === 'object' && !Array.isArray(source.error)
      ? (source.error as Record<string, unknown>)
      : null

  const errorMessage = normalizeString(error?.message)
  const errorCode = normalizeString(error?.code)
  const errorHint = normalizeString(error?.hint)
  const data = source.data && typeof source.data === 'object' && !Array.isArray(source.data) ? source.data : undefined
  const expiresAt = normalizeTimestamp(source.expiresAt ?? source.expires_at)
  const minCols = normalizeNumber(source.minCols ?? source.min_cols)
  const priority = normalizeNumber(source.priority)
  const slot = normalizeTuiSlotId(source.slot)
  const summary = normalizeString(source.summary)
  const title = normalizeString(source.title)
  const updatedAt = normalizeTimestamp(source.updatedAt ?? source.updated_at)
  const version = normalizeString(source.version)

  return {
    id,
    state: normalizeTuiModuleState(source.state),
    ...(data && { data: data as Record<string, unknown> }),
    ...(detail && { detail }),
    ...(errorMessage && {
      error: {
        message: errorMessage,
        ...(errorCode && { code: errorCode }),
        ...(errorHint && { hint: errorHint })
      }
    }),
    ...(expiresAt && { expiresAt }),
    ...(minCols && { minCols }),
    ...(priority !== undefined && { priority }),
    ...(slot && { slot }),
    ...(summary && { summary }),
    ...(title && { title }),
    ...(updatedAt && { updatedAt }),
    ...(version && { version })
  }
}
