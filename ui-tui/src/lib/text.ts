import {
  LIVE_RENDER_MAX_CHARS,
  LIVE_RENDER_MAX_LINES,
  THINKING_COT_MAX
} from '../config/limits.js'
import { FACES } from '../content/faces.js'
import { VERBS } from '../content/verbs.js'
import type { ThinkingMode } from '../types.js'

const ESC = String.fromCharCode(27)
const BEL = String.fromCharCode(7)
const ANSI_CSI_RE = new RegExp(`${ESC}\\[[0-?]*[ -/]*[@-~]`, 'g')
const ANSI_CSI_WITH_CMD_RE = new RegExp(`${ESC}\\[[0-?]*[ -/]*([@-~])`, 'g')
const ANSI_INCOMPLETE_CSI_RE = new RegExp(`${ESC}\\[[0-?]*[ -/]*(?=${ESC}|\\n|$)`, 'g')
const ANSI_OSC_RE = new RegExp(`${ESC}\\][\\s\\S]*?(?:${BEL}|${ESC}\\\\)`, 'g')
const ANSI_STRING_RE = new RegExp(`${ESC}[PX^_][\\s\\S]*?(?:${BEL}|${ESC}\\\\)`, 'g')
const ANSI_NON_CSI_ESC_SEQ_RE = new RegExp(`${ESC}(?!\\[|\\]|P|X|\\^|_)[ -/]*[0-~]`, 'g')
const ANSI_STRAY_ESC_RE = new RegExp(`${ESC}(?!\\[)[\\s\\S]?`, 'g')
const CONTROL_RE = /[\x00-\x08\x0B\x0C\x0D\x0E-\x1A\x1C-\x1F\x7F]/g
const WS_RE = /\s+/g

export const stripAnsi = (s: string) =>
  s
    .replace(ANSI_OSC_RE, '')
    .replace(ANSI_STRING_RE, '')
    .replace(ANSI_INCOMPLETE_CSI_RE, '')
    .replace(ANSI_CSI_RE, '')
    .replace(ANSI_INCOMPLETE_CSI_RE, '')
    .replace(ANSI_NON_CSI_ESC_SEQ_RE, '')
    .replace(ANSI_STRAY_ESC_RE, '')
    .replace(CONTROL_RE, '')

export const sanitizeAnsiForRender = (s: string) =>
  s
    .replace(ANSI_OSC_RE, '')
    .replace(ANSI_STRING_RE, '')
    .replace(ANSI_INCOMPLETE_CSI_RE, '')
    .replace(ANSI_CSI_WITH_CMD_RE, (seq, cmd: string) => (cmd === 'm' ? seq : ''))
    .replace(ANSI_INCOMPLETE_CSI_RE, '')
    .replace(ANSI_NON_CSI_ESC_SEQ_RE, '')
    .replace(ANSI_STRAY_ESC_RE, '')
    .replace(CONTROL_RE, '')

export const hasAnsi = (s: string) => s.includes(ESC)

const renderEstimateLine = (line: string) => {
  const trimmed = line.trim()

  if (trimmed.startsWith('|')) {
    return trimmed
      .split('|')
      .filter(Boolean)
      .map(cell => cell.trim())
      .join('  ')
  }

  return line
    .replace(/!\[(.*?)\]\(([^)\s]+)\)/g, '[image: $1]')
    .replace(/\[(.+?)\]\((https?:\/\/[^\s)]+)\)/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\*\*(.+?)\*\*/g, '$1')
    .replace(/(?<!\w)__(.+?)__(?!\w)/g, '$1')
    .replace(/\*(.+?)\*/g, '$1')
    .replace(/(?<!\w)_(.+?)_(?!\w)/g, '$1')
    .replace(/~~(.+?)~~/g, '$1')
    .replace(/==(.+?)==/g, '$1')
    .replace(/\[\^([^\]]+)\]/g, '[$1]')
    .replace(/^#{1,6}\s+/, '')
    .replace(/^\s*[-*+]\s+\[( |x|X)\]\s+/, (_m, checked: string) => `• [${checked.toLowerCase() === 'x' ? 'x' : ' '}] `)
    .replace(/^\s*[-*+]\s+/, '• ')
    .replace(/^\s*(\d+)\.\s+/, '$1. ')
    .replace(/^\s*(?:>\s*)+/, '│ ')
}

export const compactPreview = (s: string, max: number) => {
  const one = s.replace(WS_RE, ' ').trim()

  return !one ? '' : one.length > max ? one.slice(0, max - 1) + '…' : one
}

export const estimateTokensRough = (text: string) => (!text ? 0 : (text.length + 3) >> 2)

export const edgePreview = (s: string, head = 16, tail = 28) => {
  const one = s.replace(WS_RE, ' ').trim().replace(/\]\]/g, '] ]')

  return !one
    ? ''
    : one.length <= head + tail + 4
      ? one
      : `${one.slice(0, head).trimEnd()}.. ${one.slice(-tail).trimStart()}`
}

export const pasteTokenLabel = (text: string, lineCount: number) => {
  const preview = edgePreview(text)

  if (!preview) {
    return `[[ [${fmtK(lineCount)} lines] ]]`
  }

  const [head = preview, tail = ''] = preview.split('.. ', 2)

  return tail
    ? `[[ ${head.trimEnd()}.. [${fmtK(lineCount)} lines] .. ${tail.trimStart()} ]]`
    : `[[ ${preview} [${fmtK(lineCount)} lines] ]]`
}

const STATUS_WORDS = [...VERBS]

const LEGACY_REASONING_STATUS_WORDS = [
  'pondering',
  'contemplating',
  'musing',
  'cogitating',
  'ruminating',
  'deliberating',
  'mulling',
  'reflecting',
  'processing',
  'reasoning',
  'analyzing',
  'computing',
  'synthesizing',
  'formulating',
  'brainstorming'
]

const THINKING_CLEANUP_WORDS = [...STATUS_WORDS, ...LEGACY_REASONING_STATUS_WORDS]
const escapeRegex = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
const THINKING_STATUS_SOURCE = STATUS_WORDS.map(escapeRegex).join('|')
const THINKING_CLEANUP_SOURCE = THINKING_CLEANUP_WORDS.map(escapeRegex).join('|')
const THINKING_FACE_SOURCE = FACES.map(escapeRegex).join('|')
const THINKING_STATUS_RE = new RegExp(`^(?:${THINKING_STATUS_SOURCE})\\.{0,3}$`, 'i')
const THINKING_CLEANUP_RE = new RegExp(`^(?:${THINKING_CLEANUP_SOURCE})\\.{0,3}$`, 'i')
const THINKING_FACE_PREFIX_RE = new RegExp(`^\\s*(?:${THINKING_FACE_SOURCE})\\s*`, 'u')
const THINKING_FACE_ONLY_RE = new RegExp(`^(?:${THINKING_FACE_SOURCE})$`, 'u')
const CJK_RE = /[\u3400-\u9fff]/g
const LATIN_CHAR_RE = /[A-Za-z]/g
const LATIN_WORD_RE = /[A-Za-z][A-Za-z'-]{2,}/g
const INLINE_CODE_RE = /`[^`]*`/g
const WINDOWS_PATH_RE = /\b[A-Za-z]:[\\/][^\s"'`]+/g
const URL_RE = /https?:\/\/[^\s"'`]+/g

const ENGLISH_REASONING_PHRASE_RE =
  /\b(?:let me|i need to|i should|i will|i'll|i can|i'm going to|we need to|now let me|actually|found|looks like|this means|the key|need to|going to)\b/i

const ENGLISH_REASONING_SUMMARY_RULES: { pattern: RegExp; summary: string }[] = [
  {
    pattern:
      /\bpath\b[\s\S]{0,100}\b(?:resolution|resolve|wrong|incorrect|fix|retry|try again)\b|\b(?:resolution|resolve|wrong|incorrect|fix|retry|try again)\b[\s\S]{0,100}\bpath\b/i,
    summary: '路径解析不正确，正在修正路径并重试。'
  },
  {
    pattern: /\bconfig(?:uration)?\b|\bsettings?\b/i,
    summary: '正在检查配置和运行状态。'
  },
  {
    pattern: /\b(?:test|tests|pytest|vitest|eslint|type-check|build)\b/i,
    summary: '正在检查验证结果并处理失败项。'
  },
  {
    pattern: /\b(?:tool|tools|call|execute|run command|shell)\b/i,
    summary: '正在调用工具并检查返回结果。'
  },
  {
    pattern: /\b(?:file|directory|folder|workspace|repo|repository)\b/i,
    summary: '正在检查相关文件和工作区路径。'
  },
  {
    pattern: /\b(?:error|exception|failed|failure|wrong|incorrect|bug)\b/i,
    summary: '正在定位错误原因并修正。'
  }
]

const THINKING_STATUS_CHUNK_RE = new RegExp(
  `(?:^|[^\\p{L}\\p{N}\n]+)\\s*(?:(?:${THINKING_FACE_SOURCE})\\s*)?(?:${THINKING_CLEANUP_SOURCE})\\.{0,3}\\s*`,
  'giu'
)

const stripThinkingStatusLine = (line: string) =>
  line
    .replace(THINKING_STATUS_CHUNK_RE, '')
    .replace(THINKING_FACE_PREFIX_RE, '')
    .trim()

export const cleanThinkingText = (reasoning: string) =>
  reasoning
    .split('\n')
    .map(line => line.replace(THINKING_STATUS_CHUNK_RE, '').trim())
    .filter(line => line && !THINKING_STATUS_RE.test(line.replace(/\.\.\.$/, '').trim()))
    .join('\n')
    .replace(/([^\n])(?=\*\*[^*\n][^\n]*?\*\*)/g, '$1\n\n')
    .replace(/\n{3,}/g, '\n\n')
    .trim()

export const isLikelyEnglishReasoningText = (reasoning: string) => {
  const raw = cleanThinkingText(reasoning)
    .replace(INLINE_CODE_RE, '')
    .replace(WINDOWS_PATH_RE, '')
    .replace(URL_RE, '')
    .trim()

  if (!raw) {
    return false
  }

  const latinChars = raw.match(LATIN_CHAR_RE)?.length ?? 0
  const latinWords = raw.match(LATIN_WORD_RE)?.length ?? 0
  const cjkChars = raw.match(CJK_RE)?.length ?? 0

  if (latinWords < 6 || latinChars < 40) {
    return false
  }

  return ENGLISH_REASONING_PHRASE_RE.test(raw) || latinChars > Math.max(80, cjkChars * 2.5)
}

const summarizeEnglishReasoning = (reasoning: string) => {
  for (const rule of ENGLISH_REASONING_SUMMARY_RULES) {
    if (rule.pattern.test(reasoning)) {
      return rule.summary
    }
  }

  return '模型正在分析当前步骤。'
}

export const thinkingPreview = (reasoning: string, mode: ThinkingMode, max: number = THINKING_COT_MAX) => {
  const raw = cleanThinkingText(reasoning)
  const display = raw && isLikelyEnglishReasoningText(raw) ? summarizeEnglishReasoning(raw) : raw

  return !display || mode === 'collapsed' ? '' : mode === 'full' ? display : compactPreview(display.replace(WS_RE, ' '), max)
}

export const boundedLiveRenderText = (
  text: string,
  { maxChars = LIVE_RENDER_MAX_CHARS, maxLines = LIVE_RENDER_MAX_LINES } = {}
) => boundedRenderText(text, 'showing live tail', { maxChars, maxLines })

const boundedRenderText = (
  text: string,
  labelPrefix: string,
  { maxChars, maxLines }: { maxChars: number; maxLines: number }
) => {
  if (text.length <= maxChars && text.split('\n', maxLines + 1).length <= maxLines) {
    return text
  }

  let start = 0
  let idx = text.length

  for (let seen = 0; seen < maxLines && idx > 0; seen++) {
    idx = text.lastIndexOf('\n', idx - 1)
    start = idx < 0 ? 0 : idx + 1

    if (idx < 0) {
      break
    }
  }

  const lineStart = start
  start = Math.max(lineStart, text.length - maxChars)

  if (start > lineStart) {
    const nextBreak = text.indexOf('\n', start)

    if (nextBreak >= 0 && nextBreak < text.length - 1) {
      start = nextBreak + 1
    }
  }

  const tail = text.slice(start).trimStart()
  const omittedLines = countNewlines(text, start)
  const omittedChars = Math.max(0, text.length - tail.length)

  const label =
    omittedLines > 0
      ? `[${labelPrefix}; omitted ${fmtK(omittedLines)} lines / ${fmtK(omittedChars)} chars]\n`
      : `[${labelPrefix}; omitted ${fmtK(omittedChars)} chars]\n`

  return `${label}${tail}`
}

const countNewlines = (text: string, end: number) => {
  let count = 0

  for (let i = 0; i < end; i++) {
    if (text.charCodeAt(i) === 10) {
      count++
    }
  }

  return count
}

export const stripTrailingPasteNewlines = (text: string) => (/[^\n]/.test(text) ? text.replace(/\n+$/, '') : text)

const TOOL_LABELS_ZH: Record<string, string> = {
  apply_patch: '应用补丁',
  browser: '浏览器',
  browser_back: '浏览器返回',
  browser_cdp: '浏览器 CDP',
  browser_click: '浏览器点击',
  browser_console: '浏览器控制台',
  browser_get_images: '浏览器图片',
  browser_navigate: '浏览器跳转',
  browser_open: '打开浏览器',
  browser_press: '浏览器按键',
  browser_scroll: '浏览器滚动',
  browser_snapshot: '浏览器快照',
  browser_type: '浏览器输入',
  browser_vision: '浏览器视觉',
  clarify: '澄清问题',
  cronjob: '定时任务',
  create_file: '创建文件',
  delegate_task: '委托任务',
  delete_file: '删除文件',
  edit_file: '编辑文件',
  edit_message: '更新消息',
  execute_code: '执行代码',
  find: '查找',
  grep: '搜索',
  list_dir: '列目录',
  list_files: '列文件',
  memory: '记忆',
  mcp_github_create_or_update_file: '创建/更新 GitHub 文件',
  mcp_github_create_repository: '创建 GitHub 仓库',
  mcp_github_get_file_contents: '读取 GitHub 文件',
  patch: '修改文件',
  read_file: '读取文件',
  run_command: '运行命令',
  search_code: '搜索代码',
  search_files: '搜索文件',
  send_message: '发送消息',
  session_search: '会话搜索',
  skill_view: '查看技能',
  skill_manage: '技能管理',
  task_analysis: '任务分析',
  terminal: '终端',
  tool: '调用工具',
  todo: '待办',
  vision_analyze: '视觉分析',
  web_extract: '网页提取',
  web_search: '网页搜索',
  write_file: '写入文件'
}

const DEFAULT_TOOL_EMOJI = '🔧'

const TOOL_EMOJIS: Record<string, string> = {
  apply_patch: '🛠️',
  browser: '🌐',
  browser_back: '↩️',
  browser_cdp: '🧪',
  browser_click: '🖱️',
  browser_console: '🖥️',
  browser_get_images: '🖼️',
  browser_navigate: '🌐',
  browser_open: '🌐',
  browser_press: '⌨️',
  browser_scroll: '↕️',
  browser_snapshot: '📸',
  browser_type: '⌨️',
  browser_vision: '👁️',
  clarify: '❓',
  cronjob: '⏰',
  create_file: '📄',
  delegate_task: '🧩',
  delete_file: '🗑️',
  edit_file: '✏️',
  edit_message: '✏️',
  execute_code: '💻',
  find: '🔎',
  grep: '🔎',
  list_dir: '📁',
  list_files: '📁',
  memory: '🧠',
  mcp_github_create_or_update_file: '✍️',
  mcp_github_create_repository: '📦',
  mcp_github_get_file_contents: '📄',
  patch: '🛠️',
  read_file: '📖',
  run_command: '💻',
  search_code: '🔎',
  search_files: '🔎',
  send_message: '📰',
  session_search: '🔎',
  skill_manage: '📚',
  skill_view: '📚',
  task_analysis: '🧩',
  terminal: '💻',
  tool: DEFAULT_TOOL_EMOJI,
  todo: '📋',
  vision_analyze: '👁️',
  web_extract: '📄',
  web_search: '🌐',
  write_file: '✍️'
}

const TOOL_EMOJI_PREFIXES = [...new Set(Object.values(TOOL_EMOJIS).map(emoji => `${emoji} `))]
const normalizeToolName = (name: string) => name.trim().toLowerCase()
const isDecoratedToolLabel = (label: string) => TOOL_EMOJI_PREFIXES.some(prefix => label.startsWith(prefix))

const TOOL_CONTEXT_LABELS: Record<string, Record<string, string>> = {
  cronjob: {
    create: '创建任务',
    delete: '删除任务',
    list: '查看列表',
    pause: '暂停任务',
    remove: '删除任务',
    resume: '恢复任务',
    status: '查看状态',
    update: '更新任务'
  },
  todo: {
    add: '新增待办',
    clear: '清空待办',
    list: '查看列表',
    remove: '删除待办',
    update: '更新待办'
  }
}

const CONTEXT_ACTION_PREFIXES: Record<string, string> = {
  browser_click: '点击',
  browser_console: '查看控制台',
  browser_get_images: '查看图片',
  browser_navigate: '打开',
  browser_open: '打开',
  browser_press: '按键',
  browser_scroll: '滚动',
  browser_type: '输入',
  browser_vision: '识别',
  execute_code: '代码',
  find: '查找',
  grep: '关键词',
  run_command: '命令',
  search_code: '关键词',
  search_files: '关键词',
  session_search: '关键词',
  terminal: '命令',
  web_extract: '提取',
  web_search: '搜索'
}

const fallbackToolLabel = (name: string) => {
  const trimmed = name.trim()

  if (/[\s\u3400-\u9fff]/u.test(trimmed)) {
    return trimmed
  }

  return (
    trimmed
      .split('_')
      .filter(Boolean)
      .map(p => p[0]!.toUpperCase() + p.slice(1))
      .join(' ') || name
  )
}

export const toolTrailLabel = (name: string) => {
  const key = normalizeToolName(name)

  if (TOOL_LABELS_ZH[key]) {
    return TOOL_LABELS_ZH[key]
  }

  return fallbackToolLabel(name)
}

export const toolTrailIcon = (name: string) => TOOL_EMOJIS[normalizeToolName(name)] ?? DEFAULT_TOOL_EMOJI

export const toolTrailDisplayLabel = (name: string) => {
  const label = toolTrailLabel(name)

  return isDecoratedToolLabel(label) ? label : `${toolTrailIcon(name)} ${label}`
}

const formatToolContext = (name: string, context: string) => {
  const preview = compactPreview(context, 80)
  const key = normalizeToolName(name)
  const actionKey = preview.toLowerCase()
  const mapped = TOOL_CONTEXT_LABELS[key]?.[actionKey]

  if (mapped || !preview) {
    return mapped ?? preview
  }

  const prefix = CONTEXT_ACTION_PREFIXES[key]

  return prefix ? `${prefix} ${preview}` : preview
}

export const formatToolCall = (name: string, context = '') => {
  const label = toolTrailDisplayLabel(name)
  const preview = formatToolContext(name, context)

  return preview ? `${label}：${preview}` : label
}

export const buildToolTrailLine = (
  name: string,
  context: string,
  error?: boolean,
  note?: string,
  duration?: number
) => {
  const notePreview = compactPreview(note ?? '', 72)
  const detail = error && notePreview ? `失败原因：${notePreview}` : notePreview
  const took = duration !== undefined ? ` (${duration.toFixed(1)}s)` : ''

  return `${formatToolCall(name, context)}${took}${detail ? ` :: ${detail}` : ''} ${error ? '✗' : '✓'}`
}

const verboseToolBlock = (label: string, text?: string) => {
  const body = (text ?? '').trim()

  return body ? `${label}：\n${boundedLiveRenderText(body)}` : ''
}

export const buildVerboseToolTrailLine = (
  name: string,
  context: string,
  error?: boolean,
  duration?: number,
  argsText?: string,
  resultText?: string
) => {
  const detail = [verboseToolBlock('参数', argsText), verboseToolBlock(error ? '错误' : '结果', resultText)]
    .filter(Boolean)
    .join('\n')
  const took = duration !== undefined ? ` (${duration.toFixed(1)}s)` : ''

  return `${formatToolCall(name, context)}${took}${detail ? ` :: ${detail}` : ''} ${error ? '✗' : '✓'}`
}

export const isToolTrailResultLine = (line: string) => line.endsWith(' ✓') || line.endsWith(' ✗')

export const parseToolTrailResultLine = (line: string) => {
  if (!isToolTrailResultLine(line)) {
    return null
  }

  const mark = line.endsWith(' ✗') ? '✗' : '✓'
  const body = line.slice(0, -2)
  const sep = body.indexOf(' :: ')

  if (sep >= 0) {
    return { call: body.slice(0, sep), detail: body.slice(sep + 4), mark }
  }

  const legacy = body.indexOf(': ')

  if (legacy > 0) {
    return { call: body.slice(0, legacy), detail: body.slice(legacy + 2), mark }
  }

  return { call: body, detail: '', mark }
}

export const splitToolDuration = (call: string) => {
  const match = call.match(/^(.*?)( \(\d+(?:\.\d)?s\))$/)

  return match ? { label: match[1]!, duration: match[2]! } : { label: call, duration: '' }
}

export const isTransientTrailLine = (line: string) =>
  line.startsWith('drafting ') ||
  line.startsWith('正在准备 ') ||
  line.startsWith('模型：') ||
  line === 'analyzing tool output…' ||
  line === '正在分析工具输出…'

const toolTrailGroupLabels = (label: string) => {
  const trimmed = label.trim()
  const labels = new Set([trimmed])

  labels.add(`${DEFAULT_TOOL_EMOJI} ${trimmed}`)

  for (const [key, zh] of Object.entries(TOOL_LABELS_ZH)) {
    if (zh === trimmed) {
      labels.add(`${TOOL_EMOJIS[key] ?? DEFAULT_TOOL_EMOJI} ${trimmed}`)
    }
  }

  return [...labels].filter(Boolean)
}

export const sameToolTrailGroup = (label: string, entry: string) =>
  toolTrailGroupLabels(label).some(
    candidate =>
      entry === `${candidate} ✓` ||
      entry === `${candidate} ✗` ||
      entry.startsWith(`${candidate}(`) ||
      entry.startsWith(`${candidate} ::`) ||
      entry.startsWith(`${candidate}:`) ||
      entry.startsWith(`${candidate}：`)
  )

export const lastCotTrailIndex = (trail: readonly string[]) => {
  for (let i = trail.length - 1; i >= 0; i--) {
    if (!isToolTrailResultLine(trail[i]!)) {
      return i
    }
  }

  return -1
}

export const estimateRows = (text: string, w: number, compact = false) => {
  let fence: { char: '`' | '~'; len: number } | null = null
  let rows = 0

  for (const raw of text.split('\n')) {
    const line = stripAnsi(raw)
    const maybeFence = line.match(/^\s*(`{3,}|~{3,})(.*)$/)

    if (maybeFence) {
      const marker = maybeFence[1]!
      const lang = maybeFence[2]!.trim()

      if (!fence) {
        fence = { char: marker[0] as '`' | '~', len: marker.length }

        if (lang) {
          rows += Math.ceil((`─ ${lang}`.length || 1) / w)
        }
      } else if (marker[0] === fence.char && marker.length >= fence.len) {
        fence = null
      }

      continue
    }

    const inCode = Boolean(fence)
    const trimmed = line.trim()

    if (!inCode && trimmed.startsWith('|') && /^[|\s:-]+$/.test(trimmed)) {
      continue
    }

    const rendered = inCode ? line : renderEstimateLine(line)

    if (compact && !rendered.trim()) {
      continue
    }

    rows += Math.ceil((rendered.length || 1) / w)
  }

  return Math.max(1, rows)
}

export const flat = (r: Record<string, string[]>) => Object.values(r).flat()

const COMPACT_NUMBER = new Intl.NumberFormat('en-US', { maximumFractionDigits: 1, notation: 'compact' })

export const fmtK = (n: number) => COMPACT_NUMBER.format(n).replace(/[KMBT]$/, s => s.toLowerCase())

export const pick = <T>(a: T[]) => a[Math.floor(Math.random() * a.length)]!

export const isPasteBackedText = (text: string) =>
  /\[\[paste:\d+(?:[^\n]*?)\]\]|\[paste #\d+ (?:attached|excerpt)(?:[^\n]*?)\]/.test(text)
