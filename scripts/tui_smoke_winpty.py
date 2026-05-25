#!/usr/bin/env python3
"""Run a Windows ConPTY smoke check for Hermes TUI.

This script exists for non-interactive agent shells on Windows.  The normal
`hermes --tui` entry correctly refuses to start when stdin is not a TTY; this
smoke harness gives the same Node/Ink entry a real ConPTY via pywinpty, captures
rendered output, and verifies startup/input markers.

Run from the repo root:

    uv run --extra pty python scripts/tui_smoke_winpty.py
"""

from __future__ import annotations

import argparse
import os
import queue
import re
import sys
import tempfile
import threading
import time
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MARKERS = ("Hermes",)
FAIL_MARKERS = (
    "当前不是 TTY",
    "not TTY",
    "GatewayContext missing",
    "Error: --dev is incompatible",
)


ANSI_CSI_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
ANSI_OSC_RE = re.compile(r"\x1b\][\s\S]*?(?:\x07|\x1b\\)")
ANSI_OTHER_RE = re.compile(r"\x1b[PX^_][\s\S]*?(?:\x07|\x1b\\)")
ANSI_ESC_RE = re.compile(r"\x1b(?!\[|\]|P|X|\^|_)[ -/]*[0-~]")
CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1a\x1c-\x1f\x7f]")


def strip_ansi(value: str) -> str:
    return CONTROL_RE.sub("", ANSI_ESC_RE.sub("", ANSI_CSI_RE.sub("", ANSI_OTHER_RE.sub("", ANSI_OSC_RE.sub("", value)))))


def fail(message: str, output: str = "", *, code: int = 1) -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    if output:
        print("\n--- captured output tail ---", file=sys.stderr)
        print(output[-4000:], file=sys.stderr)
    return code


def import_winpty():
    try:
        from winpty import PtyProcess
    except ModuleNotFoundError:
        print(
            "pywinpty is missing. Run: uv run --extra pty python scripts/tui_smoke_winpty.py",
            file=sys.stderr,
        )
        raise SystemExit(2)

    return PtyProcess


def make_tui_process(dev: bool, via_cli: bool) -> tuple[list[str], Path, dict[str, str], str]:
    sys.path.insert(0, str(ROOT))

    from hermes_cli.main import _make_tui_argv  # type: ignore

    env = os.environ.copy()
    env.setdefault("HERMES_PYTHON", sys.executable)
    env.setdefault("HERMES_PYTHON_SRC_ROOT", str(ROOT))
    env.setdefault("NODE_ENV", "development" if dev else "production")
    env.setdefault("HERMES_TUI_INLINE", "1")
    env.setdefault("HERMES_TUI_DISABLE_MOUSE", "1")
    env.pop("HERMES_TUI_RESUME", None)

    if not env.get("TERMINAL_CWD"):
        env["TERMINAL_CWD"] = env.get("HERMES_CWD") or str(ROOT)
    env.setdefault("HERMES_CWD", env["TERMINAL_CWD"])

    tokens = env.get("NODE_OPTIONS", "").split()
    if not any(token.startswith("--max-old-space-size=") for token in tokens):
        tokens.append("--max-old-space-size=8192")
    if "--expose-gc" not in tokens:
        tokens.append("--expose-gc")
    env["NODE_OPTIONS"] = " ".join(tokens)

    fd, active_session_file = tempfile.mkstemp(prefix="hermes-tui-smoke-session-", suffix=".json")
    os.close(fd)
    env["HERMES_TUI_ACTIVE_SESSION_FILE"] = active_session_file

    if via_cli:
        argv, cwd = [sys.executable, str(ROOT / "hermes"), "--tui"], ROOT
    else:
        argv, cwd = _make_tui_argv(ROOT / "ui-tui", dev)

    return argv, cwd, env, active_session_file


def start_reader(proc, out: "queue.Queue[str | None]") -> threading.Thread:
    def run() -> None:
        while True:
            try:
                chunk = proc.read(4096)
            except EOFError:
                out.put(None)
                return
            except Exception as exc:  # pragma: no cover - diagnostic path
                out.put(f"\n[reader-error] {type(exc).__name__}: {exc}\n")
                out.put(None)
                return
            if chunk:
                out.put(chunk)

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    return thread


def contains_all(haystack: str, needles: Iterable[str]) -> bool:
    return all(needle in haystack for needle in needles)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Hermes TUI under Windows ConPTY and verify startup output.")
    parser.add_argument("--cols", type=int, default=120)
    parser.add_argument("--rows", type=int, default=32)
    parser.add_argument("--timeout", type=float, default=25.0)
    parser.add_argument("--dev", action="store_true", help="Run src/entry.tsx via tsx instead of dist/entry.js.")
    parser.add_argument("--via-cli", action="store_true", help="Run the local hermes --tui wrapper instead of Node entry.js.")
    parser.add_argument(
        "--marker",
        action="append",
        dest="markers",
        help="Required startup marker in rendered output. Can be repeated. Default: Hermes.",
    )
    parser.add_argument("--input", help="Optional text to type into the TUI after startup markers appear.")
    parser.add_argument(
        "--after-input-marker",
        action="append",
        dest="after_input_markers",
        help="Required marker after --input is typed. Can be repeated.",
    )
    parser.add_argument(
        "--forbid-marker",
        action="append",
        dest="forbid_markers",
        help="Marker that must not appear before the smoke exits successfully. Can be repeated.",
    )
    parser.add_argument(
        "--settle",
        type=float,
        default=0.0,
        help="Seconds to keep reading after success markers before passing. Useful with --forbid-marker.",
    )
    parser.add_argument("--resize-cols", type=int, help="Resize the ConPTY to this column count after normal markers pass.")
    parser.add_argument("--resize-rows", type=int, help="Resize the ConPTY to this row count after normal markers pass.")
    parser.add_argument(
        "--after-resize-marker",
        action="append",
        dest="after_resize_markers",
        help="Required marker in output after --resize-cols/--resize-rows. Can be repeated.",
    )
    parser.add_argument(
        "--after-resize-forbid-marker",
        action="append",
        dest="after_resize_forbid_markers",
        help="Marker that must not appear in output after resize. Can be repeated.",
    )
    parser.add_argument(
        "--resize-settle",
        type=float,
        default=1.0,
        help="Seconds to keep reading after resize markers before passing.",
    )
    parser.add_argument("--dump", type=Path, help="Write sanitized captured output for debugging.")
    args = parser.parse_args()

    if not sys.platform.startswith("win"):
        return fail("This smoke harness is for native Windows. Use hermes_cli.pty_bridge on POSIX.", code=2)

    PtyProcess = import_winpty()
    argv, cwd, env, active_session_file = make_tui_process(args.dev, args.via_cli)
    markers = tuple(args.markers or DEFAULT_MARKERS)
    proc = None
    raw_chunks: list[str] = []
    out: "queue.Queue[str | None]" = queue.Queue()
    input_sent = False
    startup_seen = False
    pass_at: float | None = None
    resize_done = False
    resize_pass_at: float | None = None
    resize_sanitized_start = 0

    def maybe_resize() -> bool:
        nonlocal resize_done, resize_sanitized_start

        if resize_done:
            return False

        if args.resize_cols is None and args.resize_rows is None:
            return False

        if proc is None:
            return False

        rows = max(8, args.resize_rows or args.rows)
        cols = max(40, args.resize_cols or args.cols)
        resize_sanitized_start = len(strip_ansi("".join(raw_chunks)))
        proc.setwinsize(rows, cols)
        resize_done = True

        return True

    def resize_window_text(sanitized: str) -> str:
        return sanitized[resize_sanitized_start:] if resize_done else ""

    def print_pass() -> None:
        print("PASS: TUI started under Windows ConPTY.")
        print(f"markers: {', '.join(markers)}")
        if args.input:
            print("input: accepted")
        if args.forbid_markers:
            print(f"forbidden: absent ({', '.join(args.forbid_markers)})")
        if resize_done:
            size = f"{args.resize_cols or args.cols}x{args.resize_rows or args.rows}"
            print(f"resize: accepted ({size})")
            if args.after_resize_forbid_markers:
                print(f"resize forbidden: absent ({', '.join(args.after_resize_forbid_markers)})")
        print(f"argv: {' '.join(argv)}")

    try:
        proc = PtyProcess.spawn(argv, cwd=str(cwd), env=env, dimensions=(max(8, args.rows), max(40, args.cols)))
        start_reader(proc, out)

        deadline = time.monotonic() + args.timeout
        sanitized = ""

        while time.monotonic() < deadline:
            try:
                chunk = out.get(timeout=0.2)
            except queue.Empty:
                if resize_pass_at is not None and time.monotonic() >= resize_pass_at:
                    print_pass()
                    return 0

                if pass_at is not None and time.monotonic() >= pass_at:
                    print_pass()
                    return 0

                if proc is not None and not proc.isalive():
                    break
                continue

            if chunk is None:
                break

            raw_chunks.append(chunk)
            sanitized = strip_ansi("".join(raw_chunks))

            for marker in FAIL_MARKERS:
                if marker in sanitized:
                    return fail(f"failure marker appeared: {marker}", sanitized)

            for marker in args.forbid_markers or ():
                if marker in sanitized:
                    return fail(f"forbidden marker appeared: {marker}", sanitized)

            if resize_done:
                resized = resize_window_text(sanitized)

                for marker in args.after_resize_forbid_markers or ():
                    if marker in resized:
                        return fail(f"forbidden marker appeared after resize: {marker}", sanitized)

                if contains_all(resized, tuple(args.after_resize_markers or ())) and resize_pass_at is None:
                    resize_pass_at = time.monotonic() + max(0, args.resize_settle)

                    if args.resize_settle <= 0:
                        print_pass()
                        return 0

                    continue

            if not startup_seen and contains_all(sanitized, markers):
                startup_seen = True

                if not args.input:
                    if maybe_resize():
                        continue

                    if args.settle > 0:
                        pass_at = time.monotonic() + args.settle
                        continue

                    print_pass()
                    return 0

                proc.write(args.input)
                input_sent = True

            if input_sent and contains_all(sanitized, tuple(args.after_input_markers or ())):
                if maybe_resize():
                    continue

                if args.settle > 0 and pass_at is None:
                    pass_at = time.monotonic() + args.settle
                    continue

                print_pass()
                return 0

            if pass_at is not None and time.monotonic() >= pass_at:
                print_pass()
                return 0

        sanitized = strip_ansi("".join(raw_chunks))
        if input_sent and args.after_input_markers:
            missing = ', '.join(args.after_input_markers)
            return fail(f"timed out waiting for input markers: {missing}", sanitized)

        return fail(f"timed out waiting for startup markers: {', '.join(markers)}", sanitized)
    finally:
        if args.dump:
            try:
                args.dump.parent.mkdir(parents=True, exist_ok=True)
                args.dump.write_text(strip_ansi("".join(raw_chunks)), encoding="utf-8")
            except OSError as exc:
                print(f"warning: failed to write dump: {exc}", file=sys.stderr)

        if proc is not None:
            try:
                if proc.isalive():
                    proc.sendcontrol("c")
                    time.sleep(0.5)
                proc.close(force=True)
            except Exception:
                pass

        try:
            os.unlink(active_session_file)
        except OSError:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
