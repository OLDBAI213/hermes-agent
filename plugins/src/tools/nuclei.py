"""nuclei 包装 —— POC 扫描。

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
    for p in [Path("E:/AI/security-tools/nuclei.exe"), Path("E:/AI/security-tools/nuclei")]:
        if p.exists():
            return str(p)
    return shutil.which("nuclei") or shutil.which("nuclei.exe")


def run(
    targets: "list[str] | str",
    *,
    templates: list[str] | None = None,
    severity: str = "medium,high,critical",
    timeout: int = 300,
    rate_limit: int = 50,
) -> dict:
    """对目标列表跑 nuclei POC 扫描。

    targets:   URL 列表或单个 URL
    templates: nuclei 模板路径列表，None 表示用默认模板库
    severity:  过滤等级，如 "medium,high,critical"
    rate_limit: 每秒请求数（默认 50，别太猛）

    返回字段：
      success    布尔
      findings   列表，每项含 template_id/name/severity/host/matched_at/description
      count      发现数
      elapsed_ms 耗时
      err        中文错误（成功时 None）
    """
    binary = _resolve_binary()
    if not binary:
        return {
            "success": False,
            "findings": [],
            "count": 0,
            "elapsed_ms": 0,
            "err": "未找到 nuclei 可执行文件（已查 E:/AI/security-tools 和 PATH）",
        }

    target_list = [targets] if isinstance(targets, str) else targets

    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        tmp = f.name
        f.write("\n".join(target_list))

    try:
        cmd = [
            binary, "-l", tmp,
            "-json", "-silent", "-no-color",
            "-severity", severity,
            "-rate-limit", str(rate_limit),
        ]
        if templates:
            for t in templates:
                cmd += ["-t", t]

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
                "findings": [],
                "count": 0,
                "elapsed_ms": int((time.monotonic() - t0) * 1000),
                "err": f"nuclei 超时（{timeout} 秒）",
            }
        except OSError as exc:
            return {
                "success": False,
                "findings": [],
                "count": 0,
                "elapsed_ms": int((time.monotonic() - t0) * 1000),
                "err": f"nuclei 启动失败：{exc}",
            }

        elapsed_ms = int((time.monotonic() - t0) * 1000)
        findings = []
        for line in proc.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                findings.append({
                    "template_id": obj.get("template-id", ""),
                    "name": obj.get("info", {}).get("name", ""),
                    "severity": obj.get("info", {}).get("severity", ""),
                    "host": obj.get("host", ""),
                    "matched_at": obj.get("matched-at", ""),
                    "description": obj.get("info", {}).get("description", ""),
                    "tags": obj.get("info", {}).get("tags", []),
                    "curl_command": obj.get("curl-command", ""),
                })
            except json.JSONDecodeError:
                continue

        return {
            "success": True,
            "findings": findings,
            "count": len(findings),
            "elapsed_ms": elapsed_ms,
            "err": None,
        }
    finally:
        try:
            Path(tmp).unlink()
        except OSError:
            pass