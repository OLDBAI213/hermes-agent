import { describe, expect, it } from 'vitest'

import { DEFAULT_THEME } from '../theme.js'
import type { SessionActiveItem } from '../gatewayTypes.js'
import {
  activeSessionCountLabel,
  canTypeOrchestratorPrompt,
  currentSessionSelectionIndex,
  orchestratorContextHint,
  orchestratorContextHintSegments,
  orchestratorGlobalHotkeyHint,
  orchestratorGlobalHotkeyHintSegments,
  orchestratorHintSegmentColor,
  clampOrchestratorSelection,
  closeFallbackAfterClose,
  draftModelArgFromPickerValue,
  draftModelDisplayLabel,
  fixedSessionColumnStyle,
  draftTitleFromPrompt,
  isNewSessionRow,
  newSessionMarkerColor,
  newSessionRowIndex,
  orchestratorRowClickAction,
  orchestratorVisibleRowIndexes,
  selectedSessionRowStyle
} from '../components/activeSessionSwitcher.js'

describe('session orchestrator helpers', () => {
  it('labels live sessions compactly for tight overlays', () => {
    expect(activeSessionCountLabel(0)).toBe('0 个实时会话')
    expect(activeSessionCountLabel(1)).toBe('1 个实时会话')
    expect(activeSessionCountLabel(3)).toBe('3 个实时会话')
    expect(activeSessionCountLabel(1)).not.toContain('in this TUI')
  })

  it('keeps session orchestrator hotkey hints short and contextual', () => {
    expect(orchestratorContextHint(false)).toBe('会话行： Enter 切换 · Ctrl+D 关闭')
    expect(orchestratorContextHint(true)).toBe('新建行： 输入提示词 · Enter 开始 · Tab 模型')
    expect(orchestratorGlobalHotkeyHint).toBe('↑↓ 移动 · Ctrl+N 新建 · Ctrl+R 刷新 · Esc 关闭')
    expect(orchestratorGlobalHotkeyHint.length).toBeLessThanOrEqual(56)
  })

  it('assigns themed colors consistently to orchestrator labels and hotkeys', () => {
    expect(orchestratorContextHintSegments(false)).toEqual([
      { role: 'label', text: '会话行：' },
      { role: 'text', text: ' ' },
      { role: 'hotkey', text: 'Enter' },
      { role: 'text', text: ' 切换 · ' },
      { role: 'hotkey', text: 'Ctrl+D' },
      { role: 'text', text: ' 关闭' }
    ])
    expect(orchestratorContextHintSegments(true)).toEqual([
      { role: 'label', text: '新建行：' },
      { role: 'text', text: ' 输入提示词 · ' },
      { role: 'hotkey', text: 'Enter' },
      { role: 'text', text: ' 开始 · ' },
      { role: 'hotkey', text: 'Tab' },
      { role: 'text', text: ' 模型' }
    ])
    expect(orchestratorGlobalHotkeyHintSegments.filter(s => s.role === 'hotkey').map(s => s.text)).toEqual([
      '↑↓',
      'Ctrl+N',
      'Ctrl+R',
      'Esc'
    ])
    expect(orchestratorHintSegmentColor(DEFAULT_THEME, 'hotkey')).toBe(DEFAULT_THEME.color.accent)
    expect(orchestratorHintSegmentColor(DEFAULT_THEME, 'label')).toBe(DEFAULT_THEME.color.label)
    expect(orchestratorHintSegmentColor(DEFAULT_THEME, 'text')).toBe(DEFAULT_THEME.color.muted)
    expect(newSessionMarkerColor(DEFAULT_THEME, false)).toBe(DEFAULT_THEME.color.label)
    expect(newSessionMarkerColor(DEFAULT_THEME, true)).toBe(DEFAULT_THEME.color.text)
  })

  it('uses a readable selected row style instead of accent-on-accent inverse text', () => {
    const style = selectedSessionRowStyle(DEFAULT_THEME)

    expect(style.backgroundColor).toBe(DEFAULT_THEME.color.selectionBg)
    expect(style.color).toBe(DEFAULT_THEME.color.text)
    expect(style.backgroundColor).not.toBe(DEFAULT_THEME.color.accent)
    expect(style.color).not.toBe(DEFAULT_THEME.color.accent)
  })

  it('turns model picker values into session-scoped draft model args', () => {
    expect(draftModelArgFromPickerValue('kimi-k2.6 --provider ollama-cloud --tui-session')).toBe(
      'kimi-k2.6 --provider ollama-cloud'
    )
    expect(draftModelArgFromPickerValue('openai/gpt-5.5 --provider openai-codex --global')).toBe(
      'openai/gpt-5.5 --provider openai-codex'
    )
  })

  it('highlights the current live session when the picker opens', () => {
    const sessions = [
      { id: 'first', status: 'idle' },
      { id: 'second', status: 'working', current: true },
      { id: 'third', status: 'idle' }
    ] satisfies SessionActiveItem[]

    expect(currentSessionSelectionIndex(sessions, 'second')).toBe(1)
    expect(
      currentSessionSelectionIndex([{ id: 'first', status: 'idle' }, { id: 'third', status: 'idle' }], 'third')
    ).toBe(1)
    expect(currentSessionSelectionIndex(sessions, 'missing')).toBe(1)
    expect(currentSessionSelectionIndex([], 'missing')).toBe(0)
  })

  it('adds a selectable New row after the live sessions and gates prompt typing to it', () => {
    expect(newSessionRowIndex(0)).toBe(0)
    expect(newSessionRowIndex(3)).toBe(3)
    expect(clampOrchestratorSelection(-5, 2)).toBe(0)
    expect(clampOrchestratorSelection(99, 2)).toBe(2)
    expect(isNewSessionRow(0, 0)).toBe(true)
    expect(isNewSessionRow(1, 2)).toBe(false)
    expect(isNewSessionRow(2, 2)).toBe(true)
    expect(canTypeOrchestratorPrompt(1, 2)).toBe(false)
    expect(canTypeOrchestratorPrompt(2, 2)).toBe(true)
    expect(orchestratorVisibleRowIndexes(3, 3, 12)).toEqual([0, 1, 2, 3])
    expect(orchestratorVisibleRowIndexes(13, 13, 12)).toContain(13)
  })

  it('selects a safe fallback after closing the current live session', () => {
    const remaining = [
      { id: 'next', status: 'idle' },
      { id: 'other', status: 'working' }
    ] satisfies SessionActiveItem[]

    expect(closeFallbackAfterClose('other', 'current', remaining)).toEqual({ action: 'stay' })
    expect(closeFallbackAfterClose('current', 'current', remaining)).toEqual({ action: 'activate', sessionId: 'next' })
    expect(closeFallbackAfterClose('current', 'current', [])).toEqual({ action: 'new' })
  })

  it('shows clean draft model labels without picker flags or provider params', () => {
    expect(draftModelDisplayLabel('kimi-k2.6 --provider ollama-cloud --tui-session')).toBe('kimi-k2.6')
    expect(draftModelDisplayLabel('openai/gpt-5.5 --provider openai-codex --global')).toBe('gpt-5.5')
    expect(draftModelDisplayLabel('')).toBe('当前/默认')
  })

  it('maps row clicks to existing-session activation or New-row focus', () => {
    const sessions = [
      { id: 'a', status: 'idle' },
      { id: 'b', status: 'idle' }
    ] satisfies SessionActiveItem[]

    expect(orchestratorRowClickAction(1, sessions)).toEqual({ action: 'activate', sessionId: 'b' })
    expect(orchestratorRowClickAction(2, sessions)).toEqual({ action: 'select-new' })
    expect(orchestratorRowClickAction(99, sessions)).toEqual({ action: 'select-new' })
  })

  it('keeps fixed table columns from shrinking into adjacent columns', () => {
    expect(fixedSessionColumnStyle().flexShrink).toBe(0)
  })

  it('builds a compact title from the orchestrator prompt', () => {
    expect(draftTitleFromPrompt('  Build the websocket orchestrator panel and make it robust.  ', 24)).toBe(
      'Build the websocket orc…'
    )
  })
})
