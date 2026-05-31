import {
  effectiveTuiModuleSnapshot,
  isTuiModuleVisible,
  TUI_EXTENSION_NAME,
  TUI_EXTENSION_PROTOCOL_VERSION,
  TUI_EXTENSION_VERSION,
  TUI_SLOT_IDS,
  type TuiModuleState
} from '../domain/tuiModules.js'

import type { UiState } from './interfaces.js'
import { describeTuiModulePlacement, type TuiModuleStoreState } from './tuiModuleStore.js'

const STATE_LABELS: Record<TuiModuleState, string> = {
  disabled: '已关闭',
  error: '错误',
  incompatible: '不兼容',
  loading: '加载中',
  ok: '正常',
  stale: '等待刷新',
  warning: '提醒'
}

const yesNo = (value: boolean) => (value ? '是' : '否')

export const buildTuiDoctorReport = (
  ui: UiState,
  modules: TuiModuleStoreState,
  cols = 80,
  now = Date.now()
): string => {
  const configs = Object.entries(ui.tuiModules)
  const enabledConfigs = configs.filter(([, config]) => config.enabled).length

  const snapshots = Object.values(modules.snapshots)
    .map(snapshot => effectiveTuiModuleSnapshot(snapshot, now))
    .sort((a, b) => a.id.localeCompare(b.id))

  const visible = snapshots.filter(snapshot =>
    TUI_SLOT_IDS.some(slot => isTuiModuleVisible(ui.tuiModules, snapshot, slot, cols, now))
  )

  const lines = [
    'TUI 诊断',
    '',
    '核心状态',
    `- 会话: ${ui.sid || '未连接'}`,
    `- 网关状态: ${ui.status}`,
    `- 状态栏: ${ui.statusBar}`,
    `- 鼠标/滚轮跟踪: ${ui.mouseTracking}`,
    `- 细节模式: ${ui.detailsMode}`,
    `- 流式输出: ${yesNo(ui.streaming)}`,
    '',
    '扩展内核',
    `- 名称: ${TUI_EXTENSION_NAME}`,
    `- 版本: ${TUI_EXTENSION_VERSION}`,
    `- 协议: ${TUI_EXTENSION_PROTOCOL_VERSION}`,
    `- 事件: tui.module.update`,
    '',
    '扩展模块',
    `- 配置项: ${enabledConfigs}/${configs.length} 已开启`,
    `- 运行快照: ${snapshots.length}`,
    `- 当前可见: ${visible.length}`,
    `- 可用插槽: ${TUI_SLOT_IDS.join(', ')}`
  ]

  if (!snapshots.length) {
    lines.push('- 模块状态: 暂无模块上报')
  } else {
    for (const snapshot of snapshots) {
      const placement = describeTuiModulePlacement(ui.tuiModules, snapshot)
      const status = placement.enabled ? '可显示' : '配置关闭'
      const summary = snapshot.summary || snapshot.error?.message || snapshot.detail || STATE_LABELS[snapshot.state]

      lines.push(`- ${snapshot.id}: ${STATE_LABELS[snapshot.state]} · ${status} · ${placement.slot} · ${summary}`)
    }
  }

  lines.push(
    '',
    '建议',
    visible.length || !snapshots.length
      ? '- 未发现阻塞问题'
      : '- 有模块已上报但未显示，请检查 display.tui_modules 配置和终端宽度'
  )

  return lines.join('\n')
}
