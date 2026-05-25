import { PassThrough } from 'stream'

import { renderSync, type ScrollBoxHandle } from '@hermes/ink'
import React, { createRef } from 'react'
import { afterEach, describe, expect, it } from 'vitest'

import { GatewayProvider } from '../app/gatewayContext.js'
import { resetOverlayState } from '../app/overlayStore.js'
import { patchUiState, resetUiState } from '../app/uiStore.js'
import { AppLayout } from '../components/appLayout.js'
import { stripAnsi } from '../lib/text.js'
import { DEFAULT_THEME } from '../theme.js'
import type { AppLayoutProps } from '../app/interfaces.js'
import type { Msg } from '../types.js'

const makeStreams = (rows: number) => {
  const stdout = new PassThrough()
  const stdin = new PassThrough()
  const stderr = new PassThrough()

  Object.assign(stdout, { columns: 90, isTTY: false, rows })
  Object.assign(stdin, { isTTY: false })
  Object.assign(stderr, { isTTY: false })

  return { stderr, stdin, stdout }
}

const noop = () => {}

const makeProps = (rows: number): AppLayoutProps => {
  const historyItems: Msg[] = Array.from({ length: rows }, (_, index) => ({
    role: 'assistant',
    text: `history row ${index}`
  }))

  return {
    actions: {
      answerApproval: noop,
      answerClarify: noop,
      answerSecret: noop,
      answerSudo: noop,
      clearSelection: noop,
      onModelSelect: noop,
      resumeById: noop,
      setStickyPrompt: noop
    },
    composer: {
      cols: 90,
      compIdx: 0,
      completions: [],
      empty: false,
      handleTextPaste: () => null,
      input: 'VISIBLE_INPUT_SENTINEL',
      inputBuf: [],
      pagerPageSize: 5,
      queueEditIdx: null,
      queuedDisplay: [],
      submit: noop,
      updateInput: noop,
      voiceRecordKey: { alt: false, ctrl: false, key: 'v', shift: false }
    },
    mouseTracking: true,
    progress: {
      showProgressArea: false
    },
    status: {
      cwdLabel: 'E:\\AI\\hermes',
      goodVibesTick: 0,
      sessionStartedAt: Date.now(),
      showStickyPrompt: false,
      statusColor: DEFAULT_THEME.color.statusGood,
      stickyPrompt: '',
      turnStartedAt: null,
      voiceLabel: ''
    },
    transcript: {
      historyItems,
      scrollRef: createRef<ScrollBoxHandle>(),
      virtualHistory: {
        bottomSpacer: 0,
        end: historyItems.length,
        measureRef: () => noop,
        offsets: historyItems.map((_, index) => index),
        start: 0,
        topSpacer: 0
      },
      virtualRows: historyItems.map((msg, index) => ({
        index,
        key: String(index),
        msg
      }))
    }
  }
}

afterEach(() => {
  resetOverlayState()
  resetUiState()
})

describe('AppLayout fullscreen layout', () => {
  it('keeps the composer visible when transcript content exceeds the viewport', () => {
    resetOverlayState()
    resetUiState()
    patchUiState({
      info: { model: 'test-model', profile_name: 'test' },
      statusBar: 'top'
    })

    const streams = makeStreams(10)
    let output = ''
    streams.stdout.on('data', chunk => {
      output += chunk.toString()
    })

    const gateway = {
      gw: {},
      rpc: () => Promise.resolve(null)
    }

    const instance = renderSync(
      React.createElement(
        GatewayProvider,
        { value: gateway as never },
        React.createElement(AppLayout, makeProps(80))
      ),
      {
      patchConsole: false,
      stderr: streams.stderr as NodeJS.WriteStream,
      stdin: streams.stdin as NodeJS.ReadStream,
      stdout: streams.stdout as NodeJS.WriteStream
      }
    )

    instance.unmount()
    instance.cleanup()

    expect(stripAnsi(output)).toContain('VISIBLE_INPUT_SENTINEL')
  })
})
