import { atom } from 'nanostores'

import {
  effectiveTuiModuleSnapshot,
  isTuiModuleVisible,
  normalizeTuiModuleSnapshot,
  resolveTuiModuleSlot,
  tuiModuleConfigFor,
  type TuiModules,
  type TuiModuleSnapshot,
  type TuiSlotId
} from '../domain/tuiModules.js'

const buildTuiModuleState = (): TuiModuleStoreState => ({
  snapshots: {}
})

export const $tuiModuleState = atom<TuiModuleStoreState>(buildTuiModuleState())

export const getTuiModuleState = () => $tuiModuleState.get()

export const patchTuiModuleState = (
  next: Partial<TuiModuleStoreState> | ((state: TuiModuleStoreState) => TuiModuleStoreState)
) =>
  $tuiModuleState.set(typeof next === 'function' ? next($tuiModuleState.get()) : { ...$tuiModuleState.get(), ...next })

export const upsertTuiModuleSnapshot = (raw: unknown, now = Date.now()): boolean => {
  const snapshot = normalizeTuiModuleSnapshot(raw)

  if (!snapshot) {
    return false
  }

  patchTuiModuleState(state => ({
    snapshots: {
      ...state.snapshots,
      [snapshot.id]: {
        ...state.snapshots[snapshot.id],
        ...snapshot,
        updatedAt: snapshot.updatedAt ?? now
      }
    }
  }))

  return true
}

export const removeTuiModuleSnapshot = (id: string): boolean => {
  const moduleId = id.trim()

  if (!moduleId || !$tuiModuleState.get().snapshots[moduleId]) {
    return false
  }

  patchTuiModuleState(state => {
    const { [moduleId]: _removed, ...snapshots } = state.snapshots

    return { snapshots }
  })

  return true
}

export const markTuiModulesStale = () =>
  patchTuiModuleState(state => {
    const snapshots = Object.fromEntries(
      Object.entries(state.snapshots).map(([id, snapshot]) => [
        id,
        snapshot.state === 'disabled' || snapshot.state === 'error' || snapshot.state === 'incompatible'
          ? snapshot
          : {
              ...snapshot,
              detail: snapshot.detail ?? '网关已断开，等待模块重新上报',
              state: 'stale' as const
            }
      ])
    )

    return { snapshots }
  })

export const selectTuiModulesForSlot = (
  state: TuiModuleStoreState,
  modules: TuiModules,
  slot: TuiSlotId,
  cols?: number,
  now = Date.now()
): TuiModuleSnapshot[] =>
  Object.values(state.snapshots)
    .map(snapshot => effectiveTuiModuleSnapshot(snapshot, now))
    .filter(snapshot => isTuiModuleVisible(modules, snapshot, slot, cols, now))
    .sort((a, b) => {
      const aConfig = tuiModuleConfigFor(modules, a.id)
      const bConfig = tuiModuleConfigFor(modules, b.id)
      const aPriority = a.priority ?? aConfig?.priority ?? 100
      const bPriority = b.priority ?? bConfig?.priority ?? 100

      return aPriority - bPriority || a.id.localeCompare(b.id)
    })

export const describeTuiModulePlacement = (modules: TuiModules, snapshot: TuiModuleSnapshot): TuiModulePlacement => {
  const config = tuiModuleConfigFor(modules, snapshot.id)

  return {
    enabled: !!config?.enabled,
    slot: snapshot.slot ?? resolveTuiModuleSlot(config)
  }
}

export const resetTuiModuleState = () => $tuiModuleState.set(buildTuiModuleState())

export interface TuiModulePlacement {
  enabled: boolean
  slot: TuiSlotId
}

export interface TuiModuleStoreState {
  snapshots: Record<string, TuiModuleSnapshot>
}
