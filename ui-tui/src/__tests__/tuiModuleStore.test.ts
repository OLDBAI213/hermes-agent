import { beforeEach, describe, expect, it } from 'vitest'

import {
  getTuiModuleState,
  markTuiModulesStale,
  removeTuiModuleSnapshot,
  resetTuiModuleState,
  selectTuiModulesForSlot,
  upsertTuiModuleSnapshot
} from '../app/tuiModuleStore.js'
import { normalizeTuiModules } from '../domain/tuiModules.js'

describe('tuiModuleStore', () => {
  beforeEach(() => {
    resetTuiModuleState()
  })

  it('upserts normalized snapshots by id', () => {
    expect(upsertTuiModuleSnapshot({ id: 'stock_panel', state: 'ok', summary: 'AAPL +1%', updated_at: 1000 })).toBe(
      true
    )
    expect(upsertTuiModuleSnapshot({ summary: 'missing id' })).toBe(false)

    expect(getTuiModuleState().snapshots.stock_panel).toMatchObject({
      id: 'stock_panel',
      state: 'ok',
      summary: 'AAPL +1%',
      updatedAt: 1000
    })
  })

  it('removes snapshots by id without touching other modules', () => {
    upsertTuiModuleSnapshot({ id: 'news_panel', state: 'ok', summary: 'news' })
    upsertTuiModuleSnapshot({ id: 'stock_panel', state: 'ok', summary: 'stocks' })

    expect(removeTuiModuleSnapshot('news_panel')).toBe(true)
    expect(removeTuiModuleSnapshot('missing_panel')).toBe(false)

    expect(getTuiModuleState().snapshots.news_panel).toBeUndefined()
    expect(getTuiModuleState().snapshots.stock_panel).toMatchObject({ summary: 'stocks' })
  })

  it('selects only enabled snapshots for a slot and keeps stable priority ordering', () => {
    const modules = normalizeTuiModules({
      hidden_panel: { enabled: false, slot: 'transcript.live_tail' },
      news_panel: { enabled: true, priority: 20, slot: 'transcript.live_tail' },
      stock_panel: { enabled: true, priority: 10, slot: 'transcript.live_tail' }
    })

    upsertTuiModuleSnapshot({ id: 'news_panel', state: 'ok', summary: 'news' })
    upsertTuiModuleSnapshot({ id: 'stock_panel', state: 'ok', summary: 'stocks' })
    upsertTuiModuleSnapshot({ id: 'hidden_panel', state: 'ok', summary: 'hidden' })

    expect(selectTuiModulesForSlot(getTuiModuleState(), modules, 'transcript.live_tail', 100).map(s => s.id)).toEqual([
      'stock_panel',
      'news_panel'
    ])
  })

  it('marks non-terminal module snapshots stale on gateway exit', () => {
    upsertTuiModuleSnapshot({ id: 'news_panel', state: 'ok', summary: 'ready' })
    upsertTuiModuleSnapshot({ error: { message: 'boom' }, id: 'error_panel', state: 'error' })

    markTuiModulesStale()

    expect(getTuiModuleState().snapshots.news_panel).toMatchObject({
      detail: '网关已断开，等待模块重新上报',
      state: 'stale'
    })
    expect(getTuiModuleState().snapshots.error_panel.state).toBe('error')
  })
})
