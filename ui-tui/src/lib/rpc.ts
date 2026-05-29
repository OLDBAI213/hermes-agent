import type { CommandDispatchResponse } from '../gatewayTypes.js'

export type RpcResult = Record<string, any>

export const asRpcResult = <T extends RpcResult = RpcResult>(value: unknown): T | null =>
  !value || typeof value !== 'object' || Array.isArray(value) ? null : (value as T)

export const asCommandDispatch = (value: unknown): CommandDispatchResponse | null => {
  const o = asRpcResult(value)

  if (!o || typeof o.type !== 'string') {
    return null
  }

  const t = o.type

  if (t === 'exec' || t === 'plugin') {
    return { type: t, output: typeof o.output === 'string' ? o.output : undefined }
  }

  if (t === 'alias' && typeof o.target === 'string') {
    return { type: 'alias', target: o.target }
  }

  if (t === 'skill' && typeof o.name === 'string') {
    return { type: 'skill', name: o.name, message: typeof o.message === 'string' ? o.message : undefined }
  }

  if (t === 'send' && typeof o.message === 'string') {
    return {
      type: 'send',
      message: o.message,
      notice: typeof o.notice === 'string' ? o.notice : undefined,
    }
  }

  return null
}

const EXACT_ERROR_MESSAGES: Record<string, string> = {
  'agent does not support steer': '当前 Agent 不支持插入消息',
  'agent initialization timed out': 'Agent 初始化超时',
  'argv must be list[str]': '命令参数格式错误',
  'cannot delete an active session': '不能删除正在运行的会话',
  'cli.exec: timeout': '命令执行超时',
  'empty command': '命令为空',
  'empty paste': '粘贴内容为空',
  'enable voice mode first: /voice on': '请先使用 /voice on 开启语音模式',
  'gateway attach url changed': '网关连接地址已变化，正在重连',
  'gateway closed': '网关已关闭',
  'gateway not running': '网关未运行',
  'gateway restarting': '网关正在重启',
  'gateway websocket connection failed': '网关 WebSocket 连接失败',
  'gateway websocket startup failed': '网关 WebSocket 启动失败',
  'gateway websocket unavailable': '网关 WebSocket 不可用',
  'hash required': '缺少 hash',
  'image not found': '图片不存在',
  'last user message is empty': '上一条用户消息为空',
  'managed install — credentials are read-only': '托管安装的凭据只读',
  'model value required': '缺少模型名称',
  'names required': '缺少名称',
  'no active session': '没有活动会话',
  'no active session to retry': '没有可重试的活动会话',
  'no previous user message to retry': '没有可重试的上一条用户消息',
  'session busy': '会话正在运行',
  'session not found': '会话不存在',
  'session_id required': '缺少 session_id',
  'slug is required': '缺少 slug',
  'slug and api_key are required': '缺少 slug 和 api_key',
  'snapshot must be an object': 'snapshot 必须是对象',
  'subagent_id required': '缺少 subagent_id',
  'subagents list required': '缺少子 Agent 列表',
  'text is required': '缺少文本',
  'text required': '缺少文本',
  'tui module id required': '缺少 TUI 模块 ID',
  'usage: /queue <prompt>': '用法: /queue <prompt>',
  'usage: /steer <prompt>': '用法: /steer <prompt>',
  'voice mode is off — enable with /voice on': '语音模式未开启，请使用 /voice on',
  'voice module not available': '语音模块不可用',
  'request failed': '请求失败',
  'unknown error': '未知错误'
}

const ERROR_LABELS: Record<string, string> = {
  action: '操作',
  browser: '浏览器',
  command: '命令',
  'config key': '配置项',
  'details_mode': '细节显示模式',
  'fast mode': '快速模式',
  'reasoning value': '推理设置',
  'section': '分区',
  'tui module state': 'TUI 模块状态',
  'voice action': '语音操作',
  provider: '模型提供商',
  resume: '恢复会话',
  branch: '创建分支',
  delete: '删除',
  steer: '插入消息',
  goals: '目标',
  'spawn_tree.save': '保存子 Agent 树',
  'spawn_tree.load': '读取子 Agent 树'
}

const label = (value: string): string => ERROR_LABELS[value] ?? value

const normalizeUserErrorMessage = (message: string): string => {
  const text = message.trim()

  if (!text) {
    return '请求失败'
  }

  if (EXACT_ERROR_MESSAGES[text]) {
    return EXACT_ERROR_MESSAGES[text]
  }

  let match = text.match(/^gateway exited(?: \((.+)\))?$/)

  if (match) {
    return match[1] ? `网关已退出（${match[1]}）` : '网关已退出'
  }

  match = text.match(/^gateway error: (.+)$/)

  if (match) {
    return `网关错误：${match[1]}`
  }

  match = text.match(/^gateway websocket closed(?: \((.+)\))?(?: during connect)?$/)

  if (match) {
    return match[1] ? `网关 WebSocket 已关闭（${match[1]}）` : '网关 WebSocket 已关闭'
  }

  match = text.match(/^gateway not connected: (.+)$/)

  if (match) {
    return `网关未连接：${match[1]}`
  }

  match = text.match(/^timeout: (.+)$/)

  if (match) {
    return `请求超时：${match[1]}`
  }

  match = text.match(/^unknown ([\w.-]+): (.+)$/)

  if (match) {
    return `未知${label(match[1] ?? '')}：${match[2]}`
  }

  match = text.match(/^(.+) failed: (.+)$/)

  if (match) {
    return `${label(match[1] ?? '')}失败：${match[2]}`
  }

  match = text.match(/^(.+) unavailable: (.+)$/)

  if (match) {
    return `${label(match[1] ?? '')}不可用：${match[2]}`
  }

  return text
}

export const rpcErrorMessage = (err: unknown) => {
  if (err instanceof Error && err.message) {
    return normalizeUserErrorMessage(err.message)
  }

  if (typeof err === 'string' && err.trim()) {
    return normalizeUserErrorMessage(err)
  }

  return '请求失败'
}
