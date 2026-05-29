import { Box, Text } from '@hermes/ink'
import { useStore } from '@nanostores/react'
import { memo, useMemo } from 'react'

import { $tuiModuleState, selectTuiModulesForSlot } from '../app/tuiModuleStore.js'
import { $uiState } from '../app/uiStore.js'
import type { TuiModuleSnapshot, TuiModuleState, TuiSlotId } from '../domain/tuiModules.js'
import type { Theme } from '../theme.js'

const STATE_LABELS: Record<TuiModuleState, string> = {
  disabled: '已关闭',
  error: '错误',
  incompatible: '不兼容',
  loading: '加载中',
  ok: '正常',
  stale: '等待刷新',
  warning: '提醒'
}

const STATE_ICON: Record<TuiModuleState, string> = {
  disabled: '○',
  error: '✕',
  incompatible: '!',
  loading: '…',
  ok: '✓',
  stale: '↻',
  warning: '!'
}

const stateColor = (state: TuiModuleState, t: Theme): string => {
  if (state === 'error' || state === 'incompatible') {
    return t.color.error
  }

  if (state === 'warning' || state === 'stale') {
    return t.color.warn
  }

  if (state === 'ok') {
    return t.color.ok
  }

  return t.color.muted
}

export const formatTuiModuleLine = (snapshot: TuiModuleSnapshot): string => {
  const title = snapshot.title || snapshot.id
  const summary = snapshot.summary || snapshot.error?.message || snapshot.detail || STATE_LABELS[snapshot.state]

  return `${STATE_ICON[snapshot.state]} ${title}: ${summary}`
}

export const TuiModuleHost = memo(function TuiModuleHost({ cols, slot }: TuiModuleHostProps) {
  const ui = useStore($uiState)
  const moduleState = useStore($tuiModuleState)

  const modules = useMemo(
    () => selectTuiModulesForSlot(moduleState, ui.tuiModules, slot, cols),
    [cols, moduleState, slot, ui.tuiModules]
  )

  if (!modules.length) {
    return null
  }

  return (
    <Box flexDirection="column" marginTop={1}>
      {modules.map(module => (
        <Text color={stateColor(module.state, ui.theme)} key={module.id} wrap="truncate-end">
          {formatTuiModuleLine(module)}
        </Text>
      ))}
    </Box>
  )
})

interface TuiModuleHostProps {
  cols: number
  slot: TuiSlotId
}
