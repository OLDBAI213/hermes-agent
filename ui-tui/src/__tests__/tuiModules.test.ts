import { describe, expect, it } from 'vitest'

import {
  effectiveTuiModuleSnapshot,
  isTuiModuleEnabled,
  isTuiModuleVisible,
  normalizeTuiModules,
  normalizeTuiModuleSnapshot,
  resolveTuiModuleSlot
} from '../domain/tuiModules.js'

describe('normalizeTuiModules', () => {
  it('uses Hermes TUI defaults when config is missing', () => {
    const modules = normalizeTuiModules(undefined)

    expect(modules.activity_scan.enabled).toBe(true)
    expect(modules.status_meter.enabled).toBe(true)
    expect(modules.task_panel.enabled).toBe(true)
    expect(modules.character_panel.enabled).toBe(false)
    expect(modules.monitor_panel.enabled).toBe(false)
  })

  it('accepts boolean and object module config shapes', () => {
    const modules = normalizeTuiModules({
      device_rail: { enabled: 'off', min_cols: '140', position: 'side', slot: 'status.left' },
      task_panel: false
    })

    expect(modules.task_panel.enabled).toBe(false)
    expect(modules.device_rail).toEqual({
      enabled: false,
      minCols: 140,
      position: 'side',
      slot: 'status.left'
    })
  })

  it('applies minCols at render time', () => {
    const modules = normalizeTuiModules({ monitor_panel: { enabled: true, min_cols: 120 } })

    expect(isTuiModuleEnabled(modules, 'monitor_panel', 119)).toBe(false)
    expect(isTuiModuleEnabled(modules, 'monitor_panel', 120)).toBe(true)
  })

  it('normalizes typed runtime snapshots without trusting unknown slots or states', () => {
    expect(
      normalizeTuiModuleSnapshot({
        expires_at: '2000',
        id: 'news_ticker',
        min_cols: '100',
        priority: '20',
        slot: 'transcript.live_tail',
        state: 'warning',
        summary: '3 条更新',
        title: '新闻'
      })
    ).toMatchObject({
      expiresAt: 2000,
      id: 'news_ticker',
      minCols: 100,
      priority: 20,
      slot: 'transcript.live_tail',
      state: 'warning',
      summary: '3 条更新',
      title: '新闻'
    })

    expect(normalizeTuiModuleSnapshot({ id: 'bad', slot: 'nowhere', state: 'sparkle' })).toMatchObject({
      id: 'bad',
      state: 'ok'
    })
    expect(normalizeTuiModuleSnapshot({ state: 'ok' })).toBeNull()
  })

  it('resolves legacy positions to slots and gates visible snapshots', () => {
    const modules = normalizeTuiModules({ device_rail: { enabled: true, position: 'side' } })
    const snapshot = normalizeTuiModuleSnapshot({ id: 'device_rail', state: 'ok', summary: 'ready' })!

    expect(resolveTuiModuleSlot(modules.device_rail)).toBe('status.right')
    expect(isTuiModuleVisible(modules, snapshot, 'status.right', 100)).toBe(true)
    expect(isTuiModuleVisible(modules, snapshot, 'transcript.live_tail', 100)).toBe(false)
  })

  it('marks expired snapshots stale without hiding them', () => {
    const modules = normalizeTuiModules({ news_ticker: { enabled: true, slot: 'transcript.live_tail' } })

    const snapshot = normalizeTuiModuleSnapshot({
      expiresAt: 1000,
      id: 'news_ticker',
      slot: 'transcript.live_tail',
      state: 'ok'
    })!

    expect(effectiveTuiModuleSnapshot(snapshot, 1001).state).toBe('stale')
    expect(isTuiModuleVisible(modules, snapshot, 'transcript.live_tail', 100, 1001)).toBe(true)
  })
})
