import { withInkSuspended } from '@hermes/ink'

import { launchHermesCommand } from '../../../lib/externalCli.js'
import { runExternalSetup } from '../../setupHandoff.js'
import type { SlashCommand } from '../types.js'

export const setupCommands: SlashCommand[] = [
  {
    help: '运行完整设置向导（启动 `hermes setup`）',
    name: 'setup',
    run: (arg, ctx) =>
      void runExternalSetup({
        args: ['setup', ...arg.split(/\s+/).filter(Boolean)],
        ctx,
        done: '设置完成，正在启动会话…',
        launcher: launchHermesCommand,
        suspend: withInkSuspended
      })
  }
]
