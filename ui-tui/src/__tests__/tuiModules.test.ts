import { describe, expect, it } from 'vitest'

import { isTuiModuleEnabled, normalizeTuiModules } from '../domain/tuiModules.js'

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
})
