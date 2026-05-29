import { describe, expect, it } from 'vitest'

import { asRpcResult, rpcErrorMessage } from '../lib/rpc.js'

describe('asRpcResult', () => {
  it('keeps plain object payloads', () => {
    expect(asRpcResult({ ok: true, value: 'x' })).toEqual({ ok: true, value: 'x' })
  })

  it('rejects missing or non-object payloads', () => {
    expect(asRpcResult(undefined)).toBeNull()
    expect(asRpcResult(null)).toBeNull()
    expect(asRpcResult('oops')).toBeNull()
    expect(asRpcResult(['bad'])).toBeNull()
  })
})

describe('rpcErrorMessage', () => {
  it('prefers Error messages', () => {
    expect(rpcErrorMessage(new Error('boom'))).toBe('boom')
  })

  it('falls back for unknown errors', () => {
    expect(rpcErrorMessage('broken')).toBe('broken')
    expect(rpcErrorMessage({ code: 500 })).toBe('请求失败')
  })

  it('localizes common gateway transport errors', () => {
    expect(rpcErrorMessage(new Error('gateway restarting'))).toBe('网关正在重启')
    expect(rpcErrorMessage(new Error('gateway not running'))).toBe('网关未运行')
    expect(rpcErrorMessage(new Error('gateway not connected: session.info'))).toBe('网关未连接：session.info')
    expect(rpcErrorMessage(new Error('timeout: model.list'))).toBe('请求超时：model.list')
    expect(rpcErrorMessage(new Error('gateway websocket closed (1006) during connect'))).toBe(
      '网关 WebSocket 已关闭（1006）'
    )
    expect(rpcErrorMessage(new Error('gateway exited (1)'))).toBe('网关已退出（1）')
  })

  it('localizes common TUI RPC errors', () => {
    expect(rpcErrorMessage(new Error('session not found'))).toBe('会话不存在')
    expect(rpcErrorMessage(new Error('model value required'))).toBe('缺少模型名称')
    expect(rpcErrorMessage(new Error('empty paste'))).toBe('粘贴内容为空')
    expect(rpcErrorMessage(new Error('unknown provider: mimo'))).toBe('未知模型提供商：mimo')
    expect(rpcErrorMessage(new Error('resume failed: db unavailable'))).toBe('恢复会话失败：db unavailable')
  })
})
