import { describe, expect, it } from 'vitest'

import { shouldShowFullBannerArt } from '../components/branding.js'

describe('startup banner responsiveness', () => {
  it('keeps full ASCII art out of standard-width terminals to avoid startup smear', () => {
    expect(shouldShowFullBannerArt(80, 115)).toBe(false)
    expect(shouldShowFullBannerArt(100, 115)).toBe(false)
    expect(shouldShowFullBannerArt(119, 115)).toBe(false)
  })

  it('allows full ASCII art only on wide terminals', () => {
    expect(shouldShowFullBannerArt(120, 115)).toBe(true)
    expect(shouldShowFullBannerArt(140, 115)).toBe(true)
  })
})
