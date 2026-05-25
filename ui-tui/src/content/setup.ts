import type { PanelSection } from '../types.js'

export const SETUP_REQUIRED_TITLE = '需要设置'

export const buildSetupRequiredSections = (): PanelSection[] => [
  {
    text: 'Hermes 需要先配置模型服务，TUI 才能开始会话。'
  },
  {
    rows: [
      ['/model', '在当前界面配置 provider + model'],
      ['/setup', '运行首次设置向导'],
      ['Ctrl+C', '退出后手动运行 `hermes setup`']
    ],
    title: '可选操作'
  }
]
