import type {
  BrowserManageResponse,
  CommandsCatalogResponse,
  DelegationPauseResponse,
  ProcessStopResponse,
  ReloadEnvResponse,
  ReloadMcpResponse,
  RollbackDiffResponse,
  RollbackListResponse,
  RollbackRestoreResponse,
  SlashExecResponse,
  SpawnTreeListResponse,
  SpawnTreeLoadResponse,
  ToolsConfigureResponse
} from '../../../gatewayTypes.js'
import type { PanelSection } from '../../../types.js'
import { applyDelegationStatus, getDelegationState } from '../../delegationStore.js'
import { patchOverlayState } from '../../overlayStore.js'
import { getSpawnHistory, pushDiskSnapshot, setDiffPair, type SpawnSnapshot } from '../../spawnHistoryStore.js'
import type { SlashCommand } from '../types.js'

interface SkillInfo {
  category?: string
  description?: string
  name?: string
  path?: string
}

interface SkillsListResponse {
  skills?: Record<string, string[]>
}

interface SkillsInspectResponse {
  info?: SkillInfo
}

interface SkillsSearchResponse {
  results?: { description?: string; name: string }[]
}

interface SkillsInstallResponse {
  installed?: boolean
  name?: string
}

interface SkillsBrowseItem {
  description?: string
  name: string
  source?: string
  trust?: string
}

interface SkillsBrowseResponse {
  items?: SkillsBrowseItem[]
  page?: number
  total?: number
  total_pages?: number
}

interface SkillsReloadResponse {
  output?: string
}

export const opsCommands: SlashCommand[] = [
  {
    help: '停止后台进程',
    name: 'stop',
    run: (_arg, ctx) => {
      ctx.gateway
        .rpc<ProcessStopResponse>('process.stop', {})
        .then(
          ctx.guarded<ProcessStopResponse>(r => {
            const killed = Number(r.killed ?? 0)
            ctx.transcript.sys(`已停止 ${killed} 个后台进程`)
          })
        )
        .catch(ctx.guardedErr)
    }
  },

  {
    aliases: ['reload_mcp'],
    help: '重载当前会话的 MCP server（会提示缓存影响）',
    name: 'reload-mcp',
    run: (arg, ctx) => {
      // Parse arg: `now` / `always` skip the confirmation gate.
      // `always` additionally persists approvals.mcp_reload_confirm=false.
      const a = (arg || '').trim().toLowerCase()

      const params: { session_id: string | null; confirm?: boolean; always?: boolean } = {
        session_id: ctx.sid
      }

      if (a === 'now' || a === 'approve' || a === 'once' || a === 'yes') {
        params.confirm = true
      } else if (a === 'always') {
        params.confirm = true
        params.always = true
      }

      ctx.gateway
        .rpc<ReloadMcpResponse>('reload.mcp', params)
        .then(
          ctx.guarded<ReloadMcpResponse>(r => {
            if (r.status === 'confirm_required') {
              ctx.transcript.sys(r.message || '/reload-mcp 需要确认')

              return
            }

            if (r.status === 'reloaded') {
              ctx.transcript.sys(
                params.always
                  ? 'MCP server 已重载，之后 /reload-mcp 不再要求确认'
                  : 'MCP server 已重载'
              )

              return
            }

            ctx.transcript.sys('重载完成')
          })
        )
        .catch(ctx.guardedErr)
    }
  },

  {
    help: '重新读取 ~/.hermes/.env 到当前网关',
    name: 'reload',
    run: (_arg, ctx) => {
      ctx.gateway
        .rpc<ReloadEnvResponse>('reload.env', {})
        .then(
          ctx.guarded<ReloadEnvResponse>(r => {
            const n = Number(r.updated ?? 0)
            ctx.transcript.sys(`.env 已重载（更新 ${n} 个变量）`)
          })
        )
        .catch(ctx.guardedErr)
    }
  },

  {
    help: '管理浏览器 CDP 连接 [connect|disconnect|status]',
    name: 'browser',
    run: (arg, ctx) => {
      const [rawAction = 'status', ...rest] = arg.trim().split(/\s+/).filter(Boolean)
      const action = rawAction.toLowerCase()

      if (!['connect', 'disconnect', 'status'].includes(action)) {
        return ctx.transcript.sys(
          '用法: /browser [connect|disconnect|status] [url] · 持久配置: 在 config.yaml 设置 browser.cdp_url'
        )
      }

      const sid = ctx.sid ?? null
      const url = action === 'connect' ? rest.join(' ').trim() || 'http://127.0.0.1:9222' : undefined

      if (url) {
        ctx.transcript.sys(`正在检查 Chromium 系浏览器远程调试地址: ${url}...`)
      }

      ctx.gateway
        .rpc<BrowserManageResponse>('browser.manage', { action, session_id: sid, ...(url && { url }) })
        .then(
          ctx.guarded<BrowserManageResponse>(r => {
            // Without a session we can't subscribe to streamed
            // browser.progress events, so flush the bundled list.
            if (!sid) {
              r.messages?.forEach(message => ctx.transcript.sys(message))
            }

            if (action === 'status') {
              return ctx.transcript.sys(
                r.connected
                  ? `浏览器已连接: ${r.url || '（URL 不可用）'}`
                  : '浏览器未连接（可试 /browser connect <url>，或在 config.yaml 设置 browser.cdp_url）'
              )
            }

            if (action === 'disconnect') {
              return ctx.transcript.sys('浏览器已断开')
            }

            if (r.connected) {
              ctx.transcript.sys('已通过 CDP 连接到正在运行的 Chromium 系浏览器')
              ctx.transcript.sys(`端点: ${r.url || '（URL 不可用）'}`)
              ctx.transcript.sys('下一次浏览器工具调用会使用这个 CDP 端点')
            }
          })
        )
        .catch(ctx.guardedErr)
    }
  },

  {
    help: '列出、对比或恢复检查点',
    name: 'rollback',
    run: (arg, ctx) => {
      if (!ctx.sid) {
        return ctx.transcript.sys('没有活动会话，无法回滚')
      }

      const trimmed = arg.trim()
      const [first = '', ...rest] = trimmed.split(/\s+/).filter(Boolean)
      const lower = first.toLowerCase()

      if (!trimmed || lower === 'list' || lower === 'ls') {
        return ctx.gateway
          .rpc<RollbackListResponse>('rollback.list', { session_id: ctx.sid })
          .then(
            ctx.guarded<RollbackListResponse>(r => {
              if (!r.enabled) {
                return ctx.transcript.sys('检查点未启用')
              }

              const checkpoints = r.checkpoints ?? []

              if (!checkpoints.length) {
                return ctx.transcript.sys('没有找到检查点')
              }

                ctx.transcript.panel('回滚检查点', [
                {
                  rows: checkpoints.map((c, idx) => [
                    `${idx + 1}. ${c.hash.slice(0, 10)}`,
                    [c.timestamp, c.message].filter(Boolean).join(' · ') || '（无元数据）'
                  ])
                }
              ])
            })
          )
          .catch(ctx.guardedErr)
      }

      if (lower === 'diff') {
        const hash = rest[0]

        if (!hash) {
          return ctx.transcript.sys('用法: /rollback diff <checkpoint>')
        }

        return ctx.gateway
          .rpc<RollbackDiffResponse>('rollback.diff', { hash, session_id: ctx.sid })
          .then(
            ctx.guarded<RollbackDiffResponse>(r => {
              const body = (r.rendered || r.diff || '').trim()

              if (!body && !r.stat) {
                return ctx.transcript.sys('这个检查点之后没有变更')
              }

              const text = [r.stat || '', body].filter(Boolean).join('\n\n')
              ctx.transcript.page(text, '回滚差异')
            })
          )
          .catch(ctx.guardedErr)
      }

      const hash = first
      const filePath = rest.join(' ').trim()

      return ctx.gateway
        .rpc<RollbackRestoreResponse>('rollback.restore', {
          ...(filePath ? { file_path: filePath } : {}),
          hash,
          session_id: ctx.sid
        })
        .then(
          ctx.guarded<RollbackRestoreResponse>(r => {
            if (!r.success) {
              return ctx.transcript.sys(`回滚失败: ${r.error || r.message || '未知错误'}`)
            }

            const target = filePath || 'workspace'
            const detail = r.reason || r.message || r.restored_to || '已恢复'
            ctx.transcript.sys(`已恢复 ${target}: ${detail}`)

            if ((r.history_removed ?? 0) > 0) {
              ctx.transcript.setHistoryItems(prev => ctx.transcript.trimLastExchange(prev))
            }
          })
        )
        .catch(ctx.guardedErr)
    }
  },

  {
    aliases: ['tasks'],
    help: '打开子 Agent 树面板（实时审查、终止、暂停）',
    name: 'agents',
    run: (arg, ctx) => {
      const sub = arg.trim().toLowerCase()

      // Stay compatible with the gateway `/agents [pause|resume|status]` CLI —
      // explicit subcommands skip the overlay and act directly so scripts and
      // multi-step flows can drive it without entering interactive mode.
      if (sub === 'pause' || sub === 'resume' || sub === 'unpause') {
        const paused = sub === 'pause'
        ctx.gateway.gw
          .request<DelegationPauseResponse>('delegation.pause', { paused })
          .then(r => {
            applyDelegationStatus({ paused: r?.paused })
            ctx.transcript.sys(`委托 · ${r?.paused ? '已暂停' : '已恢复'}`)
          })
          .catch(ctx.guardedErr)

        return
      }

      if (sub === 'status') {
        const d = getDelegationState()
        ctx.transcript.sys(
          `委托 · ${d.paused ? '已暂停' : '运行中'} · 上限 d${d.maxSpawnDepth ?? '?'}/${d.maxConcurrentChildren ?? '?'}`
        )

        return
      }

      patchOverlayState({ agents: true, agentsInitialHistoryIndex: 0 })
    }
  },

  {
    help: '回放已完成的子 Agent 树 · `/replay [N|last|list|load <path>]`',
    name: 'replay',
    run: (arg, ctx) => {
      const history = getSpawnHistory()
      const raw = arg.trim()
      const lower = raw.toLowerCase()

      // ── Disk-backed listing ─────────────────────────────────────
      if (lower === 'list' || lower === 'ls') {
        ctx.gateway
          .rpc<SpawnTreeListResponse>('spawn_tree.list', {
            limit: 30,
            session_id: ctx.sid ?? 'default'
          })
          .then(
            ctx.guarded<SpawnTreeListResponse>(r => {
              const entries = r.entries ?? []

              if (!entries.length) {
                return ctx.transcript.sys('当前会话没有磁盘归档的子 Agent 树')
              }

              const rows: [string, string][] = entries.map(e => {
                const ts = e.finished_at ? new Date(e.finished_at * 1000).toLocaleString() : '?'
                const label = e.label || `${e.count} 个子 Agent`

                return [`${ts} · ${e.count}×`, `${label}\n  ${e.path}`]
              })

              ctx.transcript.panel('子 Agent 树归档', [{ rows }])
            })
          )
          .catch(ctx.guardedErr)

        return
      }

      // ── Disk-backed load by path ─────────────────────────────────
      if (lower.startsWith('load ')) {
        const path = raw.slice(5).trim()

        if (!path) {
          return ctx.transcript.sys('用法: /replay load <path>')
        }

        ctx.gateway
          .rpc<SpawnTreeLoadResponse>('spawn_tree.load', { path })
          .then(
            ctx.guarded<SpawnTreeLoadResponse>(r => {
              if (!r.subagents?.length) {
                return ctx.transcript.sys('快照为空或无法读取')
              }

              // Push onto the in-memory history so the overlay picks it up
              // by index 1 just like any other snapshot.
              pushDiskSnapshot(r, path)
              patchOverlayState({ agents: true, agentsInitialHistoryIndex: 1 })
            })
          )
          .catch(ctx.guardedErr)

        return
      }

      // ── In-memory nav (same-session) ─────────────────────────────
      if (!history.length) {
        return ctx.transcript.sys('当前会话没有已完成的子 Agent 树，可试 /replay list')
      }

      let index = 1

      if (raw && lower !== 'last') {
        const parsed = parseInt(raw, 10)

        if (Number.isNaN(parsed) || parsed < 1 || parsed > history.length) {
          return ctx.transcript.sys(`回放编号超出范围 1..${history.length} · 磁盘归档请用 /replay list`)
        }

        index = parsed
      }

      patchOverlayState({ agents: true, agentsInitialHistoryIndex: index })
    }
  },

  {
    help: '对比两个已完成的子 Agent 树 · `/replay-diff <baseline> <candidate>`',
    name: 'replay-diff',
    run: (arg, ctx) => {
      const parts = arg.trim().split(/\s+/).filter(Boolean)

      if (parts.length !== 2) {
        return ctx.transcript.sys('用法: /replay-diff <a> <b>  （例如 /replay-diff 1 2 对比最近两次）')
      }

      const [a, b] = parts
      const history = getSpawnHistory()

      const resolve = (token: string): null | SpawnSnapshot => {
        const n = parseInt(token!, 10)

        if (Number.isFinite(n) && n >= 1 && n <= history.length) {
          return history[n - 1] ?? null
        }

        return null
      }

      const baseline = resolve(a!)
      const candidate = resolve(b!)

      if (!baseline || !candidate) {
        return ctx.transcript.sys(`回放差异: 无法解析编号 · 历史中有 ${history.length} 条记录`)
      }

      setDiffPair({ baseline, candidate })
      patchOverlayState({ agents: true, agentsInitialHistoryIndex: 0 })
    }
  },

  {
    aliases: ['reload_skills'],
    help: '重新扫描当前 TUI 网关中的已安装技能',
    name: 'reload-skills',
    run: (_arg, ctx) => {
      ctx.gateway
        .rpc<SkillsReloadResponse>('skills.reload', {})
        .then(
          ctx.guarded<SkillsReloadResponse>(r => {
            ctx.transcript.page(r.output || '技能已重载', '重载技能')
            ctx.gateway
              .rpc<CommandsCatalogResponse>('commands.catalog', {})
              .then(
                ctx.guarded<CommandsCatalogResponse>(catalog => {
                  if (!catalog?.pairs) {
                    return
                  }

                  ctx.local.setCatalog({
                    canon: (catalog.canon ?? {}) as Record<string, string>,
                    categories: catalog.categories ?? [],
                    pairs: catalog.pairs as [string, string][],
                    skillCount: (catalog.skill_count ?? 0) as number,
                    sub: (catalog.sub ?? {}) as Record<string, string[]>
                  })
                })
              )
              .catch(() => {})
          })
        )
        .catch(ctx.guardedErr)
    }
  },

  {
    help: '浏览、查看、安装技能',
    name: 'skills',
    run: (arg, ctx, cmd) => {
      const text = arg.trim()

      if (!text) {
        return patchOverlayState({ skillsHub: true })
      }

      const [sub, ...rest] = text.split(/\s+/)
      const query = rest.join(' ').trim()
      const { rpc } = ctx.gateway
      const { panel, sys } = ctx.transcript

      const runViaSlashWorker = () => {
        ctx.gateway.gw
          .request<SlashExecResponse>('slash.exec', { command: cmd.slice(1), session_id: ctx.sid })
          .then(r => {
            if (ctx.stale()) {
              return
            }

            const body = r?.output || '/skills: 没有输出'
            const formatted = r?.warning ? `警告: ${r.warning}\n${body}` : body
            const long = formatted.length > 180 || formatted.split('\n').filter(Boolean).length > 2

            long ? ctx.transcript.page(formatted, '技能输出') : ctx.transcript.sys(formatted)
          })
          .catch(ctx.guardedErr)
      }

      if (sub === 'list') {
        rpc<SkillsListResponse>('skills.manage', { action: 'list' })
          .then(
            ctx.guarded<SkillsListResponse>(r => {
              const cats = Object.entries(r.skills ?? {}).sort()

              if (!cats.length) {
                return sys('没有可用技能')
              }

              panel(
                '技能列表',
                cats.map<PanelSection>(([title, items]) => ({ items, title }))
              )
            })
          )
          .catch(ctx.guardedErr)

        return
      }

      if (sub === 'inspect') {
        if (!query) {
          return sys('用法: /skills inspect <name>')
        }

        rpc<SkillsInspectResponse>('skills.manage', { action: 'inspect', query })
          .then(
            ctx.guarded<SkillsInspectResponse>(r => {
              const info = r.info ?? {}

              if (!info.name) {
                return sys(`未知技能: ${query}`)
              }

              const rows: [string, string][] = [
                ['名称', String(info.name)],
                ['分类', String(info.category ?? '')],
                ['路径', String(info.path ?? '')]
              ]

              const sections: PanelSection[] = [{ rows }]

              if (info.description) {
                sections.push({ text: String(info.description) })
              }

              panel('技能详情', sections)
            })
          )
          .catch(ctx.guardedErr)

        return
      }

      if (sub === 'search') {
        if (!query) {
          return sys('用法: /skills search <query>')
        }

        rpc<SkillsSearchResponse>('skills.manage', { action: 'search', query })
          .then(
            ctx.guarded<SkillsSearchResponse>(r => {
              const results = r.results ?? []

              if (!results.length) {
                return sys(`没有找到: ${query}`)
              }

              panel(`搜索: ${query}`, [{ rows: results.map(s => [s.name, s.description ?? '']) }])
            })
          )
          .catch(ctx.guardedErr)

        return
      }

      if (sub === 'install') {
        if (!query) {
              return sys('用法: /skills install <name 或 url>')
        }

        sys(`正在安装 ${query}…`)

        rpc<SkillsInstallResponse>('skills.manage', { action: 'install', query })
          .then(
            ctx.guarded<SkillsInstallResponse>(r =>
              sys(r.installed ? `已安装 ${r.name ?? query}` : '安装失败')
            )
          )
          .catch(ctx.guardedErr)

        return
      }

      if (sub === 'browse') {
        const pageNum = query ? parseInt(query, 10) : 1

        if (Number.isNaN(pageNum) || pageNum < 1) {
          return sys('用法: /skills browse [page]  （page 必须是正数）')
        }

        sys('正在获取社区技能（扫描 6 个来源，可能需要约 15 秒）…')

        rpc<SkillsBrowseResponse>('skills.manage', { action: 'browse', page: pageNum })
          .then(
            ctx.guarded<SkillsBrowseResponse>(r => {
              const items = r.items ?? []

              if (!items.length) {
                return sys(`第 ${pageNum} 页没有技能${r.total ? `（总数 ${r.total}）` : ''}`)
              }

              const rows: [string, string][] = items.map(s => [
                s.trust ? `${s.name} · ${s.trust}` : s.name,
                String(s.description ?? '').slice(0, 160)
              ])

              const footer: string[] = []

              if (r.page && r.total_pages) {
                footer.push(`第 ${r.page}/${r.total_pages} 页`)
              }

              if (r.total) {
                footer.push(`共 ${r.total} 个技能`)
              }

              if (r.page && r.total_pages && r.page < r.total_pages) {
                footer.push(`/skills browse ${r.page + 1} 查看更多`)
              }

              panel(`浏览技能${pageNum > 1 ? ` — p${pageNum}` : ''}`, [
                { rows },
                ...(footer.length ? [{ text: footer.join(' · ') }] : [])
              ])
            })
          )
          .catch(ctx.guardedErr)

        return
      }

      runViaSlashWorker()
    }
  },

  {
    help: '启用或禁用工具（变更后会重置当前界面历史）',
    name: 'tools',
    run: (arg, ctx, cmd) => {
      const [subcommand, ...names] = arg.trim().split(/\s+/).filter(Boolean)

      if (subcommand !== 'disable' && subcommand !== 'enable') {
        ctx.gateway.gw
          .request<SlashExecResponse>('slash.exec', { command: cmd.slice(1), session_id: ctx.sid })
          .then(r => {
            if (ctx.stale()) {
              return
            }

            const body = r?.output || '/tools: 没有输出'
            const text = r?.warning ? `警告: ${r.warning}\n${body}` : body
            const long = text.length > 180 || text.split('\n').filter(Boolean).length > 2

            long ? ctx.transcript.page(text, '工具输出') : ctx.transcript.sys(text)
          })
          .catch(ctx.guardedErr)

        return
      }

      if (!names.length) {
        ctx.transcript.sys(`用法: /tools ${subcommand} <name> [name ...]`)
        ctx.transcript.sys(`内置工具集: /tools ${subcommand} web`)
        ctx.transcript.sys(`MCP 工具: /tools ${subcommand} github:create_issue`)

        return
      }

      ctx.gateway
        .rpc<ToolsConfigureResponse>('tools.configure', { action: subcommand, names, session_id: ctx.sid })
        .then(
          ctx.guarded<ToolsConfigureResponse>(r => {
            if (r.info) {
              ctx.session.setSessionStartedAt(Date.now())
              ctx.session.resetVisibleHistory(r.info)
            }

            if (r.changed?.length) {
              ctx.transcript.sys(`${subcommand === 'disable' ? '已禁用' : '已启用'}: ${r.changed.join(', ')}`)
            }

            if (r.unknown?.length) {
              ctx.transcript.sys(`未知工具集: ${r.unknown.join(', ')}`)
            }

            if (r.missing_servers?.length) {
              ctx.transcript.sys(`缺少 MCP server: ${r.missing_servers.join(', ')}`)
            }

            if (r.reset) {
              ctx.transcript.sys('会话已重置，新的工具配置已生效。')
            }
          })
        )
        .catch(ctx.guardedErr)
    }
  }
]
