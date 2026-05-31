import type { RunExternalProcess } from '@hermes/ink'

import type { SetupStatusResponse } from '../gatewayTypes.js'
import type { LaunchResult } from '../lib/externalCli.js'

import type { SlashHandlerContext } from './interfaces.js'
import { patchUiState } from './uiStore.js'

export interface RunExternalSetupOptions {
  args: string[]
  ctx: Pick<SlashHandlerContext, 'gateway' | 'session' | 'transcript'>
  done: string
  launcher: (args: string[]) => Promise<LaunchResult>
  suspend: (run: RunExternalProcess) => Promise<void>
}

export async function runExternalSetup({ args, ctx, done, launcher, suspend }: RunExternalSetupOptions) {
  const { gateway, session, transcript } = ctx

  transcript.sys(`正在启动 \`hermes ${args.join(' ')}\`…`)
  patchUiState({ status: '设置中…' })

  let result: LaunchResult = { code: null }

  await suspend(async () => {
    result = await launcher(args)
  })

  if (result.error) {
    transcript.sys(`启动 Hermes 失败：${result.error}`)
    patchUiState({ status: '需要设置' })

    return
  }

  if (result.code !== 0) {
    transcript.sys(`hermes ${args[0]} 已退出，退出码 ${result.code}`)
    patchUiState({ status: '需要设置' })

    return
  }

  const setup = await gateway.rpc<SetupStatusResponse>('setup.status', {})

  if (setup?.provider_configured === false) {
    transcript.sys('仍未配置模型提供商')
    patchUiState({ status: '需要设置' })

    return
  }

  transcript.sys(done)
  session.newSession()
}
