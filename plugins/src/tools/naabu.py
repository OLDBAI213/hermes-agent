"""naabu 包装 —— 端口扫描。

AI-first：返回结构化字典，工具层不写 journal。
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
from pathlib import Path


def _resolve_binary() -> str | None:
    for p in [Path("E:/AI/security-tools/naabu.exe"), Path("E:/AI/security-tools/naabu")]:
        if p.exists():
            return str(p)
    return shutil.which("naabu") or shutil.which("naabu.exe")


def run(target: str, *, ports: str = "top-100", timeout: int = 180) -> dict:
    """对单个 host 跑端口扫描。

    ports: "top-100" | "top-1000" | "80,443,8080" 等

    返回字段：
      success     布尔
      open_ports  列表，每项含 host/port/protocol
      open_count  开放端口数量
      elapsed_ms  耗时毫秒
      err         中文错误（成功时 None）
    """
    binary = _resolve_binary()
    if not binary:
        return {
            "success": False,
            "open_ports": [],
            "open_count": 0,
            "elapsed_ms": 0,
            "err": "未找到 naabu 可执行文件（已查 E:/AI/security-tools 和 PATH）",
        }

    cmd = [binary, "-host", target, "-silent", "-json", "-no-color"]
    if ports.startswith("top-"):
        cmd += ["-top-ports", ports[4:]]
    else:
        cmd += ["-p", ports]

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
            "open_ports": [],
            "open_count": 0,
            "elapsed_ms": int((time.monotonic() - t0) * 1000),
            "err": f"naabu 超时（{timeout} 秒）",
        }
    except OSError as exc:
        return {
            "success": False,
            "open_ports": [],
            "open_count": 0,
            "elapsed_ms": int((time.monotonic() - t0) * 1000),
            "err": f"naabu 启动失败：{exc}",
        }

    elapsed_ms = int((time.monotonic() - t0) * 1000)
    if proc.returncode != 0:
        return {
            "success": False,
            "open_ports": [],
            "open_count": 0,
            "elapsed_ms": elapsed_ms,
            "err": f"naabu 退出码非零：{proc.returncode}",
        }

    open_ports = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            open_ports.append({
                "host": obj.get("host", target),
                "port": obj.get("port"),
                "protocol": obj.get("protocol", "tcp"),
            })
        except json.JSONDecodeError:
            # naabu 也会输出 host:port 纯文本格式
            if ":" in line:
                parts = line.rsplit(":", 1)
                if parts[1].isdigit():
                    open_ports.append({"host": parts[0], "port": int(parts[1]), "protocol": "tcp"})

    return {
        "success": True,
        "open_ports": open_ports,
        "open_count": len(open_ports),
        "elapsed_ms": elapsed_ms,
        "err": None,
    }