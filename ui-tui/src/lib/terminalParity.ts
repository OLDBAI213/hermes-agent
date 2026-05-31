import {
  detectVSCodeLikeTerminal,
  type FileOps,
  isRemoteShellSession,
  shouldPromptForTerminalSetup
} from './terminalSetup.js'

export type MacTerminalHint = {
  key: string
  message: string
  tone: 'info' | 'warn'
}

export type MacTerminalContext = {
  isAppleTerminal: boolean
  isRemote: boolean
  isTmux: boolean
  vscodeLike: null | 'cursor' | 'vscode' | 'windsurf'
}

export function detectMacTerminalContext(env: NodeJS.ProcessEnv = process.env): MacTerminalContext {
  const termProgram = env['TERM_PROGRAM'] ?? ''

  return {
    isAppleTerminal: termProgram === 'Apple_Terminal' || !!env['TERM_SESSION_ID'],
    isRemote: isRemoteShellSession(env),
    isTmux: !!env['TMUX'],
    vscodeLike: detectVSCodeLikeTerminal(env)
  }
}

export async function terminalParityHints(
  env: NodeJS.ProcessEnv = process.env,
  options?: { fileOps?: Partial<FileOps>; homeDir?: string; platform?: NodeJS.Platform }
): Promise<MacTerminalHint[]> {
  const ctx = detectMacTerminalContext(env)
  const hints: MacTerminalHint[] = []

  if (
    ctx.vscodeLike &&
    (await shouldPromptForTerminalSetup({
      env,
      fileOps: options?.fileOps,
      homeDir: options?.homeDir,
      platform: options?.platform
    }))
  ) {
    hints.push({
      key: 'ide-setup',
      tone: 'info',
      message: `检测到 ${ctx.vscodeLike} 终端 · 运行 /terminal-setup 可改善 Cmd+Enter 和撤销体验`
    })
  }

  if (ctx.isAppleTerminal) {
    hints.push({
      key: 'apple-terminal',
      tone: 'warn',
      message:
        '检测到 Apple Terminal · 图片剪贴板可用 /paste 兜底；如果 Cmd+←/→/⌫ 被改写，可试 Ctrl+A / Ctrl+E / Ctrl+U'
    })
  }

  if (ctx.isTmux) {
    hints.push({
      key: 'tmux',
      tone: 'warn',
      message:
        '检测到 tmux · 剪贴板复制/粘贴会尽量使用 passthrough；开启 allow-passthrough 可提升 OSC52 稳定性'
    })
  }

  if (ctx.isRemote) {
    hints.push({
      key: 'remote',
      tone: 'warn',
      message:
        '检测到 SSH 会话 · 文本剪贴板可通过 OSC52 桥接，但图片剪贴板和本地截图路径仍取决于运行 Hermes 的机器'
    })
  }

  return hints
}
