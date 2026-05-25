import { describe, expect, it } from 'vitest'

import { artWidth, parseRichMarkup } from '../banner.js'

describe('banner art parsing', () => {
  it('keeps multiple rich color spans on the same visual line', () => {
    expect(parseRichMarkup('A[#ff0000]B[/]C[#00ff00]D[/]')).toEqual([
      [
        ['', 'A'],
        ['#ff0000', 'B'],
        ['', 'C'],
        ['#00ff00', 'D']
      ]
    ])
  })

  it('measures terminal display cells rather than JavaScript string length', () => {
    const lines = parseRichMarkup('[#ff0000]表[/]x')

    expect(lines[0]).toEqual([
      ['#ff0000', '表'],
      ['', 'x']
    ])
    expect('表x'.length).toBe(2)
    expect(artWidth(lines)).toBe(3)
  })
})
