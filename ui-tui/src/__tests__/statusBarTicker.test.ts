import { describe, expect, it } from 'vitest'

import { explicitBusyStatusLabel, padVerb, VERB_PAD_LEN } from '../components/appChrome.js'
import { VERBS } from '../content/verbs.js'

describe('FaceTicker verb padding', () => {
  it('pads every verb to the same width', () => {
    for (const verb of VERBS) {
      expect(padVerb(verb)).toHaveLength(VERB_PAD_LEN)
    }
  })

  it('keeps trailing ellipsis attached', () => {
    for (const verb of VERBS) {
      expect(padVerb(verb).startsWith(`${verb}…`)).toBe(true)
    }
  })

  it('keeps explicit busy statuses visible instead of replacing them with the ticker', () => {
    expect(explicitBusyStatusLabel('运行中…')).toBe('')
    expect(explicitBusyStatusLabel('等待输入…')).toBe('等待输入…')
    expect(explicitBusyStatusLabel('回答已生成，后台收尾…')).toBe('回答已生成，后台收尾…')
  })
})
