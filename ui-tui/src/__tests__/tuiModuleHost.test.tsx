import { PassThrough } from 'stream'

import { renderSync } from '@hermes/ink'
import React from 'react'
import { afterEach, beforeEach, describe, expect, it } from 'vitest'

import { resetTuiModuleState, upsertTuiModuleSnapshot } from '../app/tuiModuleStore.js'
import { patchUiState, resetUiState } from '../app/uiStore.js'
import { TuiModuleHost } from '../components/tuiModuleHost.js'
import { normalizeTuiModules } from '../domain/tuiModules.js'
import { stripAnsi } from '../lib/text.js'

const makeStreams = () => {
  const stdout = new PassThrough()
  const stdin = new PassThrough()
  const stderr = new PassThrough()

  Object.assign(stdout, { columns: 90, isTTY: false, rows: 8 })
  Object.assign(stdin, { isTTY: false })
  Object.assign(stderr, { isTTY: false })

  return { stderr, stdin, stdout }
}

describe('TuiModuleHost', () => {
  beforeEach(() => {
    resetUiState()
    resetTuiModuleState()
  })

  afterEach(() => {
    resetUiState()
    resetTuiModuleState()
  })

  it('renders enabled module snapshots in the requested slot', () => {
    patchUiState({
      tuiModules: normalizeTuiModules({ news_panel: { enabled: true, slot: 'transcript.live_tail' } })
    })
    upsertTuiModuleSnapshot({ id: 'news_panel', state: 'ok', summary: '3 条更新', title: '新闻' })

    const streams = makeStreams()
    let output = ''
    streams.stdout.on('data', chunk => {
      output += chunk.toString()
    })

    const instance = renderSync(React.createElement(TuiModuleHost, { cols: 90, slot: 'transcript.live_tail' }), {
      patchConsole: false,
      stderr: streams.stderr as NodeJS.WriteStream,
      stdin: streams.stdin as NodeJS.ReadStream,
      stdout: streams.stdout as NodeJS.WriteStream
    })

    instance.unmount()
    instance.cleanup()

    expect(stripAnsi(output)).toContain('✓ 新闻: 3 条更新')
  })

  it('stays invisible when the module is not enabled', () => {
    upsertTuiModuleSnapshot({ id: 'news_panel', state: 'ok', summary: '3 条更新', title: '新闻' })

    const streams = makeStreams()
    let output = ''
    streams.stdout.on('data', chunk => {
      output += chunk.toString()
    })

    const instance = renderSync(React.createElement(TuiModuleHost, { cols: 90, slot: 'transcript.live_tail' }), {
      patchConsole: false,
      stderr: streams.stderr as NodeJS.WriteStream,
      stdin: streams.stdin as NodeJS.ReadStream,
      stdout: streams.stdout as NodeJS.WriteStream
    })

    instance.unmount()
    instance.cleanup()

    expect(stripAnsi(output)).not.toContain('新闻')
  })
})
