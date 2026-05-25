import { formatBytes, performHeapDump } from '../../../lib/memory.js'
import type { SlashCommand } from '../types.js'

export const debugCommands: SlashCommand[] = [
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
          return ctx.transcript.sys(`heapdump 失败: ${r.error ?? '未知错误'}`)
        }

        ctx.transcript.sys(`heapdump 路径: ${r.heapPath}`)
        ctx.transcript.sys(`诊断文件: ${r.diagPath}`)
      })
    }
  },

  {
    help: '查看当前 V8 heap 和 rss 数值',
    name: 'mem',
    run: (_arg, ctx) => {
      const { arrayBuffers, external, heapTotal, heapUsed, rss } = process.memoryUsage()

      ctx.transcript.panel('内存', [
        {
          rows: [
            ['heap 已用', formatBytes(heapUsed)],
            ['heap 总量', formatBytes(heapTotal)],
            ['external', formatBytes(external)],
            ['array buffers', formatBytes(arrayBuffers)],
            ['rss', formatBytes(rss)],
            ['运行时间', `${process.uptime().toFixed(0)}s`]
          ]
        }
      ])
    }
  }
]
