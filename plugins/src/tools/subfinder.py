"""subfinder 包装 —— 调本机 subfinder.exe 跑子域发现。

AI-first：返回结构化字典（success / subdomains / raw_stderr / elapsed_ms / cmd / err）。
工具层不写 journal，由 facade 调用方负责。
"""
from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path


def _resolve_binary() -> str | None:
    """找 subfinder.exe —— 优先 E:/AI/security-tools，找不到再退回 PATH。"""
    candidates = [
        Path("E:/AI/security-tools/subfinder.exe"),
        Path("E:/AI/security-tools/subfinder"),
    ]
    for p in candidates:
        if p.exists():
            return str(p)
    which = shutil.which("subfinder") or shutil.which("subfinder.exe")
    return which


def run(target: str, *, timeout: int = 120, sources: list[str] | None = None) -> dict:
    """对单个域名跑 subfinder。

    返回字段：
      success    布尔，成功/失败
      subdomains 子域列表（去重排序）
      raw_stderr 工具原始 stderr（保持英文不翻译）
      elapsed_ms 耗时毫秒
      cmd        实际执行的命令行
      err        中文错误信息（成功时 None）
    """
    binary = _resolve_binary()
    if not binary:
        return {
            "success": False,
            "subdomains": [],
            "raw_stderr": "",
            "elapsed_ms": 0,
            "cmd": [],
            "err": "未找到 subfinder 可执行文件（已查 E:/AI/security-tools 和 PATH）",
        }

    cmd = [binary, "-d", target, "-silent"]
    if sources:
        cmd += ["-s", ",".join(sources)]

    t0 = time.monotonic()
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "subdomains": [],
            "raw_stderr": "",
            "elapsed_ms": int((time.monotonic() - t0) * 1000),
            "cmd": cmd,
            "err": f"subfinder 超时（{timeout} 秒）",
        }
    except OSError as exc:
        return {
            "success": False,
            "subdomains": [],
            "raw_stderr": "",
            "elapsed_ms": int((time.monotonic() - t0) * 1000),
            "cmd": cmd,
            "err": f"subfinder 启动失败：{exc}",
        }

    elapsed_ms = int((time.monotonic() - t0) * 1000)
    if proc.returncode != 0:
        return {
            "success": False,
            "subdomains": [],
            "raw_stderr": proc.stderr,
            "elapsed_ms": elapsed_ms,
            "cmd": cmd,
            "err": f"subfinder 退出码非零：{proc.returncode}",
        }

    subdomains = sorted({line.strip() for line in proc.stdout.splitlines() if line.strip()})
    return {
        "success": True,
        "subdomains": subdomains,
        "raw_stderr": proc.stderr,
        "elapsed_ms": elapsed_ms,
        "cmd": cmd,
        "err": None,
    }
