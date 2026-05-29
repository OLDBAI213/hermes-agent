"""katana 包装 —— 主动爬取 endpoint 发现。

AI-first：返回结构化字典，工具层不写 journal。
"""
from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path


def _resolve_binary() -> str | None:
    for p in [Path("E:/AI/security-tools/katana.exe"), Path("E:/AI/security-tools/katana")]:
        if p.exists():
            return str(p)
    return shutil.which("katana") or shutil.which("katana.exe")


def run(target: str, *, depth: int = 3, timeout: int = 120, js_crawl: bool = True) -> dict:
    """爬取目标的所有 endpoint。

    返回字段：
      success    布尔
      endpoints  URL 列表（去重排序）
      count      数量
      elapsed_ms 耗时毫秒
      err        中文错误（成功时 None）
    """
    binary = _resolve_binary()
    if not binary:
        return {
            "success": False,
            "endpoints": [],
            "count": 0,
            "elapsed_ms": 0,
            "err": "未找到 katana 可执行文件（已查 E:/AI/security-tools 和 PATH）",
        }

    cmd = [binary, "-u", target, "-silent", "-depth", str(depth), "-no-color"]
    if js_crawl:
        cmd.append("-jc")

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
            "endpoints": [],
            "count": 0,
            "elapsed_ms": int((time.monotonic() - t0) * 1000),
            "err": f"katana 超时（{timeout} 秒）",
        }
    except OSError as exc:
        return {
            "success": False,
            "endpoints": [],
            "count": 0,
            "elapsed_ms": int((time.monotonic() - t0) * 1000),
            "err": f"katana 启动失败：{exc}",
        }

    elapsed_ms = int((time.monotonic() - t0) * 1000)
    endpoints = sorted({line.strip() for line in proc.stdout.splitlines() if line.strip()})
    return {
        "success": True,
        "endpoints": endpoints,
        "count": len(endpoints),
        "elapsed_ms": elapsed_ms,
        "err": None,
    }