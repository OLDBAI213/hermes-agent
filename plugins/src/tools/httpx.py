"""httpx 包装 —— 存活检测 + 技术指纹。

AI-first：返回结构化字典，工具层不写 journal。
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path


def _resolve_binary() -> str | None:
    for p in [Path("E:/AI/security-tools/httpx.exe"), Path("E:/AI/security-tools/httpx")]:
        if p.exists():
            return str(p)
    return shutil.which("httpx") or shutil.which("httpx.exe")


def run(targets: list[str], *, timeout: int = 120, tech_detect: bool = True) -> dict:
    """检测一批 host/URL 的存活状态及技术指纹。

    返回字段：
      success      布尔
      results      列表，每项含 url/host/status_code/title/tech
      alive_count  存活数量
      elapsed_ms   耗时毫秒
      err          中文错误（成功时 None）
    """
    binary = _resolve_binary()
    if not binary:
        return {
            "success": False,
            "results": [],
            "alive_count": 0,
            "elapsed_ms": 0,
            "err": "未找到 httpx 可执行文件（已查 E:/AI/security-tools 和 PATH）",
        }

    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        tmp = f.name
        f.write("\n".join(targets))

    try:
        cmd = [binary, "-l", tmp, "-silent", "-status-code", "-title", "-json", "-no-color"]
        if tech_detect:
            cmd.append("-tech-detect")

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
                "results": [],
                "alive_count": 0,
                "elapsed_ms": int((time.monotonic() - t0) * 1000),
                "err": f"httpx 超时（{timeout} 秒）",
            }
        except OSError as exc:
            return {
                "success": False,
                "results": [],
                "alive_count": 0,
                "elapsed_ms": int((time.monotonic() - t0) * 1000),
                "err": f"httpx 启动失败：{exc}",
            }

        elapsed_ms = int((time.monotonic() - t0) * 1000)
        results = []
        for line in proc.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                results.append({
                    "url": obj.get("url", ""),
                    "host": obj.get("host", obj.get("input", "")),
                    "status_code": obj.get("status-code") or obj.get("status_code"),
                    "title": obj.get("title", ""),
                    "tech": obj.get("tech", []),
                    "content_length": obj.get("content-length"),
                    "scheme": obj.get("scheme", ""),
                })
            except json.JSONDecodeError:
                continue

        return {
            "success": True,
            "results": results,
            "alive_count": len(results),
            "elapsed_ms": elapsed_ms,
            "err": None,
        }
    finally:
        try:
            Path(tmp).unlink()
        except OSError:
            pass