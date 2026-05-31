import { attachedImageNotice, introMsg, toTranscriptMessages } from '../../../domain/messages.js'
import { TUI_SESSION_MODEL_FLAG } from '../../../domain/slash.js'
import type {
  BackgroundStartResponse,
  ConfigGetValueResponse,
  ConfigSetResponse,
  ImageAttachResponse,
  SessionBranchResponse,
  SessionCompressResponse,
  SessionUsageResponse,
  VoiceToggleResponse
} from '../../../gatewayTypes.js'
import { formatVoiceRecordKey, parseVoiceRecordKey } from '../../../lib/platform.js'
import { fmtK } from '../../../lib/text.js'
import type { PanelSection } from '../../../types.js'
import { DEFAULT_INDICATOR_STYLE, INDICATOR_STYLES, type IndicatorStyle } from '../../interfaces.js'
import { patchOverlayState } from '../../overlayStore.js'
import { patchUiState } from '../../uiStore.js'
import type { SlashCommand } from '../types.js'

const TUI_SESSION_MODEL_RE = new RegExp(`(?:^|\\s)${TUI_SESSION_MODEL_FLAG}(?:\\s|$)`)
const TUI_SESSION_STRIP_RE = new RegExp(`\\s*${TUI_SESSION_MODEL_FLAG}\\b\\s*`, 'g')

const stripTuiSessionFlag = (trimmed: string) => trimmed.replace(TUI_SESSION_STRIP_RE, ' ').replace(/\s+/g, ' ').trim()

const modelValueForConfigSet = (arg: string) => {
  const trimmed = arg.trim()

  if (!trimmed) {
    return trimmed
  }

  if (TUI_SESSION_MODEL_RE.test(trimmed)) {
    return stripTuiSessionFlag(trimmed)
  }

  return trimmed
}

export const sessionCommands: SlashCommand[] = [
  {
    aliases: ['bg', 'btw'],
    help: '启动后台提示词任务',
    name: 'background',
    run: (arg, ctx) => {
      if (!arg) {
        return ctx.transcript.sys('用法: /background <prompt>')
      }

      ctx.gateway.rpc<BackgroundStartResponse>('prompt.background', { session_id: ctx.sid, text: arg }).then(
        ctx.guarded<BackgroundStartResponse>(r => {
          if (!r.task_id) {
            return
          }

          patchUiState(state => ({ ...state, bgTasks: new Set(state.bgTasks).add(r.task_id!) }))
          ctx.transcript.sys(`后台任务 ${r.task_id} 已启动`)
        })
      )
    }
  },

  {
    help: '切换或显示模型',
    name: 'model',
    run: (arg, ctx) => {
      if (ctx.session.guardBusySessionSwitch('切换模型')) {
        return
      }

      if (!arg.trim()) {
        return patchOverlayState({ modelPicker: true })
      }

      ctx.gateway
        .rpc<ConfigSetResponse>('config.set', { key: 'model', session_id: ctx.sid, value: modelValueForConfigSet(arg) })
        .then(
          ctx.guarded<ConfigSetResponse>(r => {
            if (!r.value) {
              return ctx.transcript.sys('错误：模型切换返回无效响应')
            }

            ctx.transcript.sys(`模型 → ${r.value}`)
            ctx.local.maybeWarn(r)

            patchUiState(state => ({
              ...state,
              info: state.info ? { ...state.info, model: r.value! } : { model: r.value!, skills: {}, tools: {} }
            }))
          })
        )
    }
  },

  {
    aliases: ['switch'],
    help: '切换当前 TUI 会话',
    name: 'sessions',
    run: (arg, ctx) => {
      if (arg.trim().toLowerCase() === 'new') {
        return ctx.session.newLiveSession()
      }

      patchOverlayState({ sessions: true })
    }
  },

  {
    help: '附加图片',
    name: 'image',
    run: (arg, ctx) => {
      ctx.gateway.rpc<ImageAttachResponse>('image.attach', { path: arg, session_id: ctx.sid }).then(
        ctx.guarded<ImageAttachResponse>(r => {
          ctx.transcript.sys(attachedImageNotice(r))

          if (r.remainder) {
            ctx.composer.setInput(r.remainder)
          }
        })
      )
    }
  },

  {
    help: '切换当前会话人格',
    name: 'personality',
    run: (arg, ctx) => {
      if (!arg) {
        return
      }

      ctx.gateway.rpc<ConfigSetResponse>('config.set', { key: 'personality', session_id: ctx.sid, value: arg }).then(
        ctx.guarded<ConfigSetResponse>(r => {
          if (r.history_reset) {
            ctx.session.resetVisibleHistory(r.info ?? null)
          }

          ctx.transcript.sys(`人格：${r.value || '默认'}${r.history_reset ? ' · 已清空转写' : ''}`)
          ctx.local.maybeWarn(r)
        })
      )
    }
  },

  {
    help: '压缩转写上下文',
    name: 'compress',
    run: (arg, ctx) => {
      ctx.gateway
        .rpc<SessionCompressResponse>('session.compress', {
          session_id: ctx.sid,
          ...(arg ? { focus_topic: arg } : {})
        })
        .then(
          ctx.guarded<SessionCompressResponse>(r => {
            if (Array.isArray(r.messages)) {
              const rows = toTranscriptMessages(r.messages)

              ctx.transcript.setHistoryItems(r.info ? [introMsg(r.info), ...rows] : rows)
            }

            if (r.info) {
              patchUiState({ info: r.info })
            }

            if (r.usage) {
              patchUiState(state => ({ ...state, usage: { ...state.usage, ...r.usage } }))
            }

            if (r.summary?.headline) {
              const prefix = r.summary.noop ? '' : '✓ '

              ctx.transcript.sys(`${prefix}${r.summary.headline}`)

              if (r.summary.token_line) {
                ctx.transcript.sys(`  ${r.summary.token_line}`)
              }

              if (r.summary.note) {
                ctx.transcript.sys(`  ${r.summary.note}`)
              }

              return
            }

            if ((r.removed ?? 0) <= 0) {
              return ctx.transcript.sys('没有需要压缩的内容')
            }

            ctx.transcript.sys(
              `已压缩 ${r.removed} 条消息${r.usage?.total ? ` · ${fmtK(r.usage.total)} 令牌` : ''}`
            )
          })
        )
        .catch(ctx.guardedErr)
    }
  },

  {
    aliases: ['fork'],
    help: '分支当前会话',
    name: 'branch',
    run: (arg, ctx) => {
      const prevSid = ctx.sid

      ctx.gateway.rpc<SessionBranchResponse>('session.branch', { name: arg, session_id: ctx.sid }).then(
        ctx.guarded<SessionBranchResponse>(r => {
          if (!r.session_id) {
            return
          }

          void ctx.session.closeSession(prevSid)
          patchUiState({ sid: r.session_id })
          ctx.session.setSessionStartedAt(Date.now())
          ctx.transcript.sys(`已创建分支 → ${r.title ?? ''}`)
        })
      )
    }
  },

  {
    help: '语音模式 [on|off|tts|status]',
    name: 'voice',
    run: (arg, ctx) => {
      const normalized = (arg ?? '').trim().toLowerCase()

      const action =
        normalized === 'on' || normalized === 'off' || normalized === 'tts' || normalized === 'status'
          ? normalized
          : 'status'

      ctx.gateway.rpc<VoiceToggleResponse>('voice.toggle', { action }).then(
        ctx.guarded<VoiceToggleResponse>(r => {
          ctx.voice.setVoiceEnabled(!!r.enabled)
          ctx.voice.setVoiceTts(!!r.tts)

          // Render the configured record key (config.yaml ``voice.record_key``)
          // instead of hardcoded "Ctrl+B" — the gateway response carries the
          // current value so /voice status and /voice on stay in sync with
          // both the CLI and the TUI's actual binding (#18994).
          //
          // Copilot review on #19835 caught that rendering from the fresh
          // backend response WITHOUT updating the frontend ``voice.recordKey``
          // state would skew display and binding between config-edit and
          // the next ``mtime`` poll (~5s). Parse once, push into state so
          // ``useInputHandlers()`` picks up the new binding immediately.
          //
          // Round-2 follow-up: only push state when the response actually
          // carries ``record_key`` — otherwise an older gateway (or a future
          // branch that forgets to include it) would clobber a custom user
          // binding back to the default on every /voice invocation. The
          // label still falls back to the documented default for display.
          const parsed = r.record_key ? parseVoiceRecordKey(r.record_key) : undefined

          if (parsed) {
            ctx.voice.setVoiceRecordKey(parsed)
          }

          const recordKeyLabel = formatVoiceRecordKey(parsed ?? parseVoiceRecordKey('ctrl+b'))

          // Match CLI's _show_voice_status / _enable_voice_mode /
          // _toggle_voice_tts output shape so users don't have to learn
          // two vocabularies.
          if (action === 'status') {
            const mode = r.enabled ? '开' : '关'
            const tts = r.tts ? '开' : '关'
            ctx.transcript.sys('语音模式状态')
            ctx.transcript.sys(`  模式：${mode}`)
            ctx.transcript.sys(`  语音输出：${tts}`)
            ctx.transcript.sys(`  录音键：${recordKeyLabel}`)

            // CLI 的依赖状态块：把 STT/音频配置问题直接显示出来，
            // 避免用户每次按录音键才发现不可用。
            if (r.details) {
              ctx.transcript.sys('')
              ctx.transcript.sys('  依赖状态：')

              for (const line of r.details.split('\n')) {
                if (line.trim()) {
                  ctx.transcript.sys(`    ${line}`)
                }
              }
            }

            return
          }

          if (action === 'tts') {
            ctx.transcript.sys(`语音 TTS 已${r.tts ? '开启' : '关闭'}。`)

            return
          }

          // on/off — mirror cli.py:_enable_voice_mode's 3-line output
          if (r.enabled) {
            const tts = r.tts ? '（TTS 已开启）' : ''
            ctx.transcript.sys(`语音模式已开启${tts}`)
            ctx.transcript.sys(`  按 ${recordKeyLabel} 开始/停止录音`)
            ctx.transcript.sys('  /voice tts  切换语音输出')
            ctx.transcript.sys('  /voice off  关闭语音模式')
          } else {
            ctx.transcript.sys('语音模式已关闭。')
          }
        })
      )
    }
  },

  {
    help: '切换主题皮肤',
    name: 'skin',
    run: (arg, ctx) => {
      if (!arg) {
        return ctx.gateway
          .rpc<ConfigGetValueResponse>('config.get', { key: 'skin' })
          .then(ctx.guarded<ConfigGetValueResponse>(r => ctx.transcript.sys(`皮肤：${r.value || '默认'}`)))
      }

      ctx.gateway
        .rpc<ConfigSetResponse>('config.set', { key: 'skin', value: arg })
        .then(ctx.guarded<ConfigSetResponse>(r => r.value && ctx.transcript.sys(`皮肤 → ${r.value}`)))
    }
  },

  {
    help: '选择忙碌动画样式：kaomoji、emoji、unicode 或 ascii',
    name: 'indicator',
    usage: `用法: /indicator [${INDICATOR_STYLES.join('|')}]`,
    run: (arg, ctx) => {
      const value = arg.trim().toLowerCase()

      if (!value) {
        return ctx.gateway
          .rpc<ConfigGetValueResponse>('config.get', { key: 'indicator' })
          .then(
            ctx.guarded<ConfigGetValueResponse>(r =>
              ctx.transcript.sys(`忙碌动画：${r.value || DEFAULT_INDICATOR_STYLE}`)
            )
          )
      }

      if (!(INDICATOR_STYLES as readonly string[]).includes(value)) {
        return ctx.transcript.sys(`用法: /indicator [${INDICATOR_STYLES.join('|')}]`)
      }

      ctx.gateway.rpc<ConfigSetResponse>('config.set', { key: 'indicator', value }).then(
        ctx.guarded<ConfigSetResponse>(r => {
          if (!r.value) {
            return
          }

          // Hot-swap the running TUI immediately so the next render
          // uses the new style without waiting for the 5s mtime poll
          // to re-apply config.full.
          patchUiState({ indicatorStyle: value as IndicatorStyle })
          ctx.transcript.sys(`忙碌动画 → ${r.value}`)
        })
      )
    }
  },

  {
    help: '切换 yolo 模式（当前会话审批）',
    name: 'yolo',
    run: (_arg, ctx) => {
      ctx.gateway
        .rpc<ConfigSetResponse>('config.set', { key: 'yolo', session_id: ctx.sid })
        .then(ctx.guarded<ConfigSetResponse>(r => ctx.transcript.sys(`审批直通：${r.value === '1' ? '开启' : '关闭'}`)))
    }
  },

  {
    help: '查看或设置 reasoning effort（同步当前 Agent）',
    name: 'reasoning',
    run: (arg, ctx) => {
      if (!arg) {
        return ctx.gateway
          .rpc<ConfigGetValueResponse>('config.get', { key: 'reasoning' })
          .then(
            ctx.guarded<ConfigGetValueResponse>(
              r => r.value && ctx.transcript.sys(`推理强度：${r.value} · 显示 ${r.display || 'hide'}`)
            )
          )
      }

      ctx.gateway
        .rpc<ConfigSetResponse>('config.set', { key: 'reasoning', session_id: ctx.sid, value: arg })
        .then(
          ctx.guarded<ConfigSetResponse>(r => {
            if (!r.value) {
              return
            }

            if (r.value === 'hide') {
              patchUiState(state => ({
                ...state,
                sections: { ...state.sections, thinking: 'hidden' },
                showReasoning: false
              }))
            } else if (r.value === 'show') {
              patchUiState(state => ({
                ...state,
                sections: { ...state.sections, thinking: 'expanded' },
                showReasoning: true
              }))
            }

            ctx.transcript.sys(`推理强度：${r.value}`)
          })
        )
    }
  },

  {
    help: '切换 fast 模式 [normal|fast|status|on|off|toggle]',
    name: 'fast',
    run: (arg, ctx) => {
      const mode = arg.trim().toLowerCase()
      const valid = new Set(['', 'status', 'normal', 'fast', 'on', 'off', 'toggle'])

      if (!valid.has(mode)) {
        return ctx.transcript.sys('用法: /fast [normal|fast|status|on|off|toggle]')
      }

      if (!mode || mode === 'status') {
        return ctx.gateway
          .rpc<ConfigGetValueResponse>('config.get', { key: 'fast', session_id: ctx.sid })
          .then(
            ctx.guarded<ConfigGetValueResponse>(r =>
              ctx.transcript.sys(`fast 模式：${r.value === 'fast' ? 'fast' : 'normal'}`)
            )
          )
          .catch(ctx.guardedErr)
      }

      ctx.gateway
        .rpc<ConfigSetResponse>('config.set', { key: 'fast', session_id: ctx.sid, value: mode })
        .then(
          ctx.guarded<ConfigSetResponse>(r => {
            const next = r.value === 'fast' ? 'fast' : 'normal'
            ctx.transcript.sys(`fast 模式：${next}`)
            patchUiState(state => ({
              ...state,
              info: state.info
                ? {
                    ...state.info,
                    fast: next === 'fast',
                    service_tier: next === 'fast' ? 'priority' : ''
                  }
                : state.info
            }))
          })
        )
        .catch(ctx.guardedErr)
    }
  },

  {
    help: '忙碌输入模式 [queue|steer|interrupt|status]',
    name: 'busy',
    run: (arg, ctx) => {
      const mode = arg.trim().toLowerCase()
      const valid = new Set(['', 'status', 'queue', 'steer', 'interrupt'])

      if (!valid.has(mode)) {
        return ctx.transcript.sys('用法: /busy [queue|steer|interrupt|status]')
      }

      if (!mode || mode === 'status') {
        return ctx.gateway
          .rpc<ConfigGetValueResponse>('config.get', { key: 'busy' })
          .then(
            ctx.guarded<ConfigGetValueResponse>(r => {
              const current = r.value || 'interrupt'
              ctx.transcript.sys(`忙碌输入模式：${current}`)
            })
          )
          .catch(ctx.guardedErr)
      }

      ctx.gateway
        .rpc<ConfigSetResponse>('config.set', { key: 'busy', value: mode })
        .then(
          ctx.guarded<ConfigSetResponse>(r => {
            const next = r.value || mode
            ctx.transcript.sys(`忙碌输入模式：${next}`)
          })
        )
        .catch(ctx.guardedErr)
    }
  },

  {
    help: '切换详细工具输出模式（同步当前 Agent）',
    name: 'verbose',
    run: (arg, ctx) => {
      ctx.gateway
        .rpc<ConfigSetResponse>('config.set', { key: 'verbose', session_id: ctx.sid, value: arg || 'cycle' })
        .then(ctx.guarded<ConfigSetResponse>(r => r.value && ctx.transcript.sys(`详细输出：${r.value}`)))
    }
  },

  {
    help: '会话用量（实时计数）',
    name: 'usage',
    run: (_arg, ctx) => {
      ctx.gateway.rpc<SessionUsageResponse>('session.usage', { session_id: ctx.sid }).then(r => {
        if (ctx.stale()) {
          return
        }

        if (r) {
          patchUiState({
            usage: { calls: r.calls ?? 0, input: r.input ?? 0, output: r.output ?? 0, total: r.total ?? 0 }
          })
        }

        if (!r?.calls) {
          return ctx.transcript.sys('还没有 API 调用')
        }

        const f = (v: number | undefined) => (v ?? 0).toLocaleString()
        const cost = r.cost_usd != null ? `${r.cost_status === 'estimated' ? '~' : ''}$${r.cost_usd.toFixed(4)}` : null

        const rows: [string, string][] = [
          ['模型', r.model ?? ''],
          ['输入令牌', f(r.input)],
          ['缓存读取令牌', f(r.cache_read)],
          ['缓存写入令牌', f(r.cache_write)],
          ['输出令牌', f(r.output)],
          ['总令牌', f(r.total)],
          ['API 调用', f(r.calls)]
        ]

        if (cost) {
          rows.push(['费用', cost])
        }

        const sections: PanelSection[] = [{ rows }]

        if (r.context_max) {
          sections.push({ text: `上下文：${f(r.context_used)} / ${f(r.context_max)} (${r.context_percent}%)` })
        }

        if (r.compressions) {
          sections.push({ text: `压缩次数：${r.compressions}` })
        }

        ctx.transcript.panel('用量', sections)
      })
    }
  }
]
