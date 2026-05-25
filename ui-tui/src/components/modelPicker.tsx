import { Box, Text, useInput, useStdout } from '@hermes/ink'
import { useEffect, useMemo, useState } from 'react'

import { providerDisplayNames } from '../domain/providers.js'
import { TUI_SESSION_MODEL_FLAG } from '../domain/slash.js'
import type { GatewayClient } from '../gatewayClient.js'
import type { ModelOptionProvider, ModelOptionsResponse } from '../gatewayTypes.js'
import { asRpcResult, rpcErrorMessage } from '../lib/rpc.js'
import type { Theme } from '../theme.js'

import { OverlayHint, useOverlayKeys, windowItems } from './overlayControls.js'

const VISIBLE = 12
const MIN_WIDTH = 40
const MAX_WIDTH = 90

type Stage = 'provider' | 'key' | 'model' | 'disconnect'

export function ModelPicker({ gw, onCancel, onSelect, sessionId, t }: ModelPickerProps) {
  const [providers, setProviders] = useState<ModelOptionProvider[]>([])
  const [currentModel, setCurrentModel] = useState('')
  const [err, setErr] = useState('')
  const [loading, setLoading] = useState(true)
  const [persistGlobal, setPersistGlobal] = useState(false)
  const [providerIdx, setProviderIdx] = useState(0)
  const [modelIdx, setModelIdx] = useState(0)
  const [stage, setStage] = useState<Stage>('provider')
  const [keyInput, setKeyInput] = useState('')
  const [keySaving, setKeySaving] = useState(false)
  const [keyError, setKeyError] = useState('')

  const { stdout } = useStdout()
  // Pin the picker to a stable width so the FloatBox parent (which shrinks-
  // to-fit with alignSelf="flex-start") doesn't resize as long provider /
  // model names scroll into view, and so `wrap="truncate-end"` on each row
  // has an actual constraint to truncate against.
  const width = Math.max(MIN_WIDTH, Math.min(MAX_WIDTH, (stdout?.columns ?? 80) - 6))

  useEffect(() => {
    gw.request<ModelOptionsResponse>('model.options', sessionId ? { session_id: sessionId } : {})
      .then(raw => {
        const r = asRpcResult<ModelOptionsResponse>(raw)

        if (!r) {
          setErr('响应无效: model.options')
          setLoading(false)

          return
        }

        const next = r.providers ?? []
        setProviders(next)
        setCurrentModel(String(r.model ?? ''))
        setProviderIdx(
          Math.max(
            0,
            next.findIndex(p => p.is_current)
          )
        )
        setModelIdx(0)
        setStage('provider')
        setErr('')
        setLoading(false)
      })
      .catch((e: unknown) => {
        setErr(rpcErrorMessage(e))
        setLoading(false)
      })
  }, [gw, sessionId])

  const provider = providers[providerIdx]
  const models = provider?.models ?? []
  const names = useMemo(() => providerDisplayNames(providers), [providers])

  const back = () => {
    if (stage === 'model' || stage === 'key' || stage === 'disconnect') {
      setStage('provider')
      setModelIdx(0)
      setKeyInput('')
      setKeyError('')
      setKeySaving(false)

      return
    }

    onCancel()
  }

  useOverlayKeys({ onBack: back, onClose: onCancel })

  useInput((ch, key) => {
    // Key entry stage handles its own input
    if (stage === 'key') {
      if (keySaving) {
        return
      }

      if (key.return) {
        if (!keyInput.trim()) {
          return
        }

        setKeySaving(true)
        setKeyError('')
        gw.request<{ provider?: ModelOptionProvider }>('model.save_key', {
          slug: provider?.slug,
          api_key: keyInput.trim(),
          ...(sessionId ? { session_id: sessionId } : {}),
        })
          .then(raw => {
            const r = asRpcResult<{ provider?: ModelOptionProvider }>(raw)

            if (!r?.provider) {
              setKeyError('保存 key 失败')
              setKeySaving(false)

              return
            }

            // Update the provider in our list with fresh data
            setProviders(prev =>
              prev.map(p => p.slug === r.provider!.slug ? r.provider! : p)
            )
            setKeyInput('')
            setKeySaving(false)
            setStage('model')
            setModelIdx(0)
          })
          .catch((e: unknown) => {
            setKeyError(rpcErrorMessage(e))
            setKeySaving(false)
          })

        return
      }

      if (key.backspace || key.delete) {
        setKeyInput(v => v.slice(0, -1))

        return
      }

      // ctrl+u clears input
      if (ch === '\u0015') {
        setKeyInput('')

        return
      }

      if (ch && !key.ctrl && !key.meta) {
        setKeyInput(v => v + ch)
      }

      return
    }

    // Disconnect confirmation stage
    if (stage === 'disconnect') {
      if (ch.toLowerCase() === 'y' || key.return) {
        if (!provider) {
          setStage('provider')

          return
        }

        setKeySaving(true)
        gw.request<{ disconnected?: boolean }>('model.disconnect', {
          slug: provider.slug,
          ...(sessionId ? { session_id: sessionId } : {}),
        })
          .then(raw => {
            const r = asRpcResult<{ disconnected?: boolean }>(raw)

            if (r?.disconnected) {
              // Mark provider as unauthenticated in local state
              setProviders(prev =>
                prev.map(p => p.slug === provider.slug
                  ? { ...p, authenticated: false, models: [], total_models: 0, warning: p.key_env ? `粘贴 ${p.key_env} 以启用` : '运行 `hermes model` 配置' }
                  : p
                )
              )
            }

            setKeySaving(false)
            setStage('provider')
          })
          .catch(() => {
            setKeySaving(false)
            setStage('provider')
          })

        return
      }

      if (ch.toLowerCase() === 'n' || key.escape) {
        setStage('provider')

        return
      }

      return
    }

    const count = stage === 'provider' ? providers.length : models.length
    const sel = stage === 'provider' ? providerIdx : modelIdx
    const setSel = stage === 'provider' ? setProviderIdx : setModelIdx

    if (key.upArrow && sel > 0) {
      setSel(v => v - 1)

      return
    }

    if (key.downArrow && sel < count - 1) {
      setSel(v => v + 1)

      return
    }

    if (key.return) {
      if (stage === 'provider') {
        if (!provider) {
          return
        }

        if (provider.authenticated === false) {
          // api_key providers: prompt for key inline
          if (provider.auth_type === 'api_key' && provider.key_env) {
            setStage('key')
            setKeyInput('')
            setKeyError('')
          }

          // Other auth types: no-op (warning shown tells them to run hermes model)
          return
        }

        setStage('model')
        setModelIdx(0)

        return
      }

      const model = models[modelIdx]

      if (provider && model) {
        onSelect(`${model} --provider ${provider.slug}${persistGlobal ? ' --global' : ` ${TUI_SESSION_MODEL_FLAG}`}`)
      } else {
        setStage('provider')
      }

      return
    }

    if (ch.toLowerCase() === 'g') {
      setPersistGlobal(v => !v)

      return
    }

    // Disconnect: only in provider stage, only for authenticated providers
    if (ch.toLowerCase() === 'd' && stage === 'provider' && provider?.authenticated !== false) {
      setStage('disconnect')

      return
    }
  })

  if (loading) {
    return <Text color={t.color.muted}>正在加载模型…</Text>
  }

  if (err) {
    return (
      <Box flexDirection="column">
        <Text color={t.color.label}>错误: {err}</Text>
        <OverlayHint t={t}>Esc/q 取消</OverlayHint>
      </Box>
    )
  }

  if (!providers.length) {
    return (
      <Box flexDirection="column">
        <Text color={t.color.muted}>没有可用 provider</Text>
        <OverlayHint t={t}>Esc/q 取消</OverlayHint>
      </Box>
    )
  }

  // ── Key entry stage ──────────────────────────────────────────────────
  if (stage === 'key' && provider) {
    const masked = keyInput ? '•'.repeat(Math.min(keyInput.length, 40)) : ''

    return (
      <Box flexDirection="column" width={width}>
        <Text bold color={t.color.accent} wrap="truncate-end">
          配置 {provider.name}
        </Text>

        <Text color={t.color.muted} wrap="truncate-end">
          在下方粘贴 API key（保存到 ~/.hermes/.env）
        </Text>

        <Text color={t.color.muted} wrap="truncate-end"> </Text>

        <Text color={t.color.muted} wrap="truncate-end">
          {provider.key_env}:
        </Text>

        <Text color={t.color.accent} wrap="truncate-end">
          {'  '}{masked || '（空）'}{keySaving ? '' : '▎'}
        </Text>

        <Text color={t.color.muted} wrap="truncate-end"> </Text>

        {keyError ? (
          <Text color={t.color.label} wrap="truncate-end">
            错误: {keyError}
          </Text>
        ) : keySaving ? (
          <Text color={t.color.muted} wrap="truncate-end">
            正在保存…
          </Text>
        ) : (
          <Text color={t.color.muted} wrap="truncate-end"> </Text>
        )}

        <OverlayHint t={t}>Enter 保存 · Ctrl+U 清空 · Esc 返回</OverlayHint>
      </Box>
    )
  }

  // ── Disconnect confirmation stage ─────────────────────────────────────
  if (stage === 'disconnect' && provider) {
    return (
      <Box flexDirection="column" width={width}>
        <Text bold color={t.color.accent} wrap="truncate-end">
          断开 {provider.name}？
        </Text>

        <Text color={t.color.muted} wrap="truncate-end"> </Text>

        <Text color={t.color.muted} wrap="truncate-end">
          这会删除 {provider.name} 已保存的凭据。
        </Text>

        <Text color={t.color.muted} wrap="truncate-end">
          之后再次选择它即可重新认证。
        </Text>

        <Text color={t.color.muted} wrap="truncate-end"> </Text>

        {keySaving ? (
          <Text color={t.color.muted} wrap="truncate-end">正在断开…</Text>
        ) : (
          <OverlayHint t={t}>y/Enter 确认 · n/Esc 取消</OverlayHint>
        )}
      </Box>
    )
  }

  // ── Provider selection stage ─────────────────────────────────────────
  if (stage === 'provider') {
    const rows = providers.map(
      (p, i) => {
        const authMark = p.authenticated === false ? '○' : p.is_current ? '*' : '●'
        const modelCount = p.total_models ?? p.models?.length ?? 0

        const suffix = p.authenticated === false
          ? (p.auth_type === 'api_key' ? '（缺少 key）' : '（需要设置）')
          : `${modelCount} 个模型`

        return `${authMark} ${names[i]} · ${suffix}`
      }
    )

    const { items, offset } = windowItems(rows, providerIdx, VISIBLE)

    return (
      <Box flexDirection="column" width={width}>
        <Text bold color={t.color.accent} wrap="truncate-end">
          选择 provider（第 1/2 步）
        </Text>

        <Text color={t.color.muted} wrap="truncate-end">
          下一步显示完整模型 ID · Enter 继续
        </Text>

        <Text color={t.color.muted} wrap="truncate-end">
          当前: {currentModel || '（未知）'}
        </Text>
        <Text color={t.color.label} wrap="truncate-end">
          {provider?.warning ? `警告: ${provider.warning}` : ' '}
        </Text>
        <Text color={t.color.muted} wrap="truncate-end">
          {offset > 0 ? ` ↑ 还有 ${offset} 项` : ' '}
        </Text>

        {Array.from({ length: VISIBLE }, (_, i) => {
          const row = items[i]
          const idx = offset + i
          const p = providers[idx]
          const dimmed = p?.authenticated === false

          return row ? (
            <Text
              bold={providerIdx === idx}
              color={providerIdx === idx ? t.color.accent : dimmed ? t.color.label : t.color.muted}
              inverse={providerIdx === idx}
              key={providers[idx]?.slug ?? `row-${idx}`}
              wrap="truncate-end"
            >
              {providerIdx === idx ? '▸ ' : '  '}
              {idx + 1}. {row}
            </Text>
          ) : (
            <Text color={t.color.muted} key={`pad-${i}`} wrap="truncate-end">
              {' '}
            </Text>
          )
        })}

        <Text color={t.color.muted} wrap="truncate-end">
          {offset + VISIBLE < rows.length ? ` ↓ 还有 ${rows.length - offset - VISIBLE} 项` : ' '}
        </Text>

        <Text color={t.color.muted} wrap="truncate-end">
          保存范围: {persistGlobal ? '全局' : '当前会话'} · g 切换
        </Text>
        <OverlayHint t={t}>↑/↓ 选择 · Enter 确认 · d 断开 · Esc/q 取消</OverlayHint>
      </Box>
    )
  }

  // ── Model selection stage ────────────────────────────────────────────
  const { items, offset } = windowItems(models, modelIdx, VISIBLE)

  return (
    <Box flexDirection="column" width={width}>
      <Text bold color={t.color.accent} wrap="truncate-end">
        选择模型（第 2/2 步）
      </Text>

      <Text color={t.color.muted} wrap="truncate-end">
        {names[providerIdx] || '（未知 provider）'} · Esc 返回
      </Text>
      <Text color={t.color.label} wrap="truncate-end">
        {provider?.warning ? `警告: ${provider.warning}` : ' '}
      </Text>
      <Text color={t.color.muted} wrap="truncate-end">
        {offset > 0 ? ` ↑ 还有 ${offset} 项` : ' '}
      </Text>

      {Array.from({ length: VISIBLE }, (_, i) => {
        const row = items[i]
        const idx = offset + i

        if (!row) {
          return !models.length && i === 0 ? (
            <Text color={t.color.muted} key="empty" wrap="truncate-end">
              这个 provider 没有列出模型
            </Text>
          ) : (
            <Text color={t.color.muted} key={`pad-${i}`} wrap="truncate-end">
              {' '}
            </Text>
          )
        }

        const prefix = modelIdx === idx ? '▸ ' : row === currentModel ? '* ' : '  '

        return (
          <Text
            bold={modelIdx === idx}
            color={modelIdx === idx ? t.color.accent : t.color.muted}
            inverse={modelIdx === idx}
            key={`${provider?.slug ?? 'prov'}:${idx}:${row}`}
            wrap="truncate-end"
          >
            {prefix}
            {idx + 1}. {row}
          </Text>
        )
      })}

      <Text color={t.color.muted} wrap="truncate-end">
        {offset + VISIBLE < models.length ? ` ↓ 还有 ${models.length - offset - VISIBLE} 项` : ' '}
      </Text>

      <Text color={t.color.muted} wrap="truncate-end">
        保存范围: {persistGlobal ? '全局' : '当前会话'} · g 切换
      </Text>
      <OverlayHint t={t}>
        {models.length ? '↑/↓ 选择 · Enter 切换 · Esc 返回 · q 关闭' : 'Enter/Esc 返回 · q 关闭'}
      </OverlayHint>
    </Box>
  )
}

interface ModelPickerProps {
  gw: GatewayClient
  onCancel: () => void
  onSelect: (value: string) => void
  sessionId: string | null
  t: Theme
}
