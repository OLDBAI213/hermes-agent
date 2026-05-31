import {
  normalizeTuiModuleState,
  TUI_EXTENSION_VERSION,
  type TuiModuleState
} from '../../../domain/tuiModules.js'
import { formatBytes, performHeapDump } from '../../../lib/memory.js'
import { buildTuiDoctorReport } from '../../tuiDoctor.js'
import { getTuiModuleState, removeTuiModuleSnapshot, upsertTuiModuleSnapshot } from '../../tuiModuleStore.js'
import { patchUiState } from '../../uiStore.js'
import type { SlashCommand } from '../types.js'

const SMOKE_MODULE_ID = 'tui_smoke'
const SMOKE_STATES: TuiModuleState[] = ['ok', 'loading', 'warning', 'stale', 'error', 'disabled', 'incompatible']
const SMOKE_STATE_SUMMARY: Record<TuiModuleState, string> = {
  disabled: '模块已关闭',
  error: '模块错误',
  incompatible: '模块不兼容',
  loading: '模块加载中',
  ok: '模块正常',
  stale: '模块等待刷新',
  warning: '模块有提醒'
}

export const debugCommands: SlashCommand[] = [
  {
    help: '查看 TUI 扩展和模块运行状态',
    name: 'tui-doctor',
    run: (_arg, ctx) => {
      ctx.transcript.page(buildTuiDoctorReport(ctx.ui, getTuiModuleState()), 'TUI 诊断')
    }
  },

  {
    help: '渲染或清理本地 TUI 模块烟测快照',
    name: 'tui-module-smoke',
    run: (arg, ctx) => {
      const value = arg.trim().toLowerCase()

      if (value === 'clear') {
        removeTuiModuleSnapshot(SMOKE_MODULE_ID)
        patchUiState(state => {
          const { [SMOKE_MODULE_ID]: _removed, ...tuiModules } = state.tuiModules

          return { ...state, tuiModules }
        })
        ctx.transcript.sys('TUI 模块烟测已清理')

        return
      }

      if (value && !SMOKE_STATES.includes(value as TuiModuleState)) {
        ctx.transcript.sys('用法: /tui-module-smoke [ok|loading|warning|stale|error|disabled|incompatible|clear]')

        return
      }

      const state = normalizeTuiModuleState(value || 'ok')
      const summary = SMOKE_STATE_SUMMARY[state]

      patchUiState(ui => ({
        ...ui,
        tuiModules: {
          ...ui.tuiModules,
          [SMOKE_MODULE_ID]: {
            enabled: state !== 'disabled',
            slot: 'transcript.live_tail'
          }
        }
      }))
      upsertTuiModuleSnapshot({
        id: SMOKE_MODULE_ID,
        slot: 'transcript.live_tail',
        state,
        summary,
        title: 'TUI 模块烟测',
        version: TUI_EXTENSION_VERSION
      })
      ctx.transcript.sys(`TUI 模块烟测: ${summary}`)
    }
  },

  {
    help: '写入 V8 heap 快照和内存诊断（见 HERMES_HEAPDUMP_DIR）',
    name: 'heapdump',
    run: (_arg, ctx) => {
      const { heapUsed, rss } = process.memoryUsage()

      ctx.transcript.sys(`正在写入 heap dump（heap ${formatBytes(heapUsed)} · rss ${formatBytes(rss)}）…`)

      void performHeapDump('manual').then(r => {
        if (ctx.stale()) {
          return
        }

        if (!r.success) {
          return ctx.transcript.sys(`heapdump 失败：${r.error ?? '未知错误'}`)
        }

        ctx.transcript.sys(`heapdump 文件：${r.heapPath}`)
        ctx.transcript.sys(`诊断文件：${r.diagPath}`)
      })
    }
  },

  {
    help: '打印当前 V8 heap 和 rss 数值',
    name: 'mem',
    run: (_arg, ctx) => {
      const { arrayBuffers, external, heapTotal, heapUsed, rss } = process.memoryUsage()

      ctx.transcript.panel('内存', [
        {
          rows: [
            ['heap 已用', formatBytes(heapUsed)],
            ['heap 总量', formatBytes(heapTotal)],
            ['外部内存', formatBytes(external)],
            ['ArrayBuffer', formatBytes(arrayBuffers)],
            ['rss', formatBytes(rss)],
            ['运行时长', `${process.uptime().toFixed(0)}s`]
          ]
        }
      ])
    }
  }
]
