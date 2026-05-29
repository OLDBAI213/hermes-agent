"""JS 文件分析 —— 纯 Python 实现，无需外部工具。

两件事：
1. endpoint_extract：从 JS 里找 URL 路径、API 接口
2. secret_scan：找疑似密钥、token、密码泄露
"""
from __future__ import annotations

import re
import urllib.request
import urllib.error
from pathlib import Path


# ── endpoint 提取 ──────────────────────────────────────────────────────────────

_EP_PATTERNS = [
    # /api/v1/user、/admin/login 等路径
    re.compile(r'["\'](\/?(?:api|v\d|admin|auth|user|account|login|logout|order|pay|upload|download|search|config|internal)[^\s"\'<>]{0,120})["\']', re.I),
    # fetch("/xxx") / axios.get("/xxx")
    re.compile(r'(?:fetch|axios\.\w+|http\.\w+|request)\s*\(\s*["\']([/\w][^\s"\']{0,200})["\']', re.I),
    # url: "/xxx"
    re.compile(r'url\s*[:=]\s*["\']([/\w][^\s"\']{0,200})["\']', re.I),
    # href = "/xxx"
    re.compile(r'href\s*=\s*["\']([/\w][^\s"\']{0,200})["\']', re.I),
]

# ── 密钥/敏感信息 ──────────────────────────────────────────────────────────────

_SECRET_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("AWS Access Key",       re.compile(r'\b(AKIA[0-9A-Z]{16})\b')),
    ("AWS Secret Key",       re.compile(r'aws.{0,20}["\']([A-Za-z0-9/+=]{40})["\']', re.I)),
    ("GitHub Token",         re.compile(r'\b(gh[pousr]_[A-Za-z0-9_]{36,})\b')),
    ("Generic JWT",          re.compile(r'\b(eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,})\b')),
    ("Google API Key",       re.compile(r'\b(AIza[0-9A-Za-z_-]{35})\b')),
    ("Stripe Secret Key",    re.compile(r'\b(sk_live_[0-9a-zA-Z]{24,})\b')),
    ("Private Key Header",   re.compile(r'-----BEGIN (?:RSA |EC )?PRIVATE KEY-----')),
    ("Generic Secret Field", re.compile(r'(?:secret|password|passwd|token|apikey|api_key|access_key|auth_token)\s*[:=]\s*["\']([^\s"\']{8,80})["\']', re.I)),
    ("Bearer Token",         re.compile(r'[Bb]earer\s+([A-Za-z0-9\-._~+/]{20,})')),
]


def fetch_js(url: str, *, timeout: int = 15) -> tuple[str, str | None]:
    """下载 JS 内容，返回 (content, error)。"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read(5 * 1024 * 1024)  # 最多 5 MB
            encoding = resp.headers.get_content_charset("utf-8")
            return raw.decode(encoding, errors="replace"), None
    except urllib.error.URLError as e:
        return "", str(e)
    except Exception as e:
        return "", str(e)


def endpoint_extract(content: str, base_url: str = "") -> list[str]:
    """从 JS 文本中提取 endpoint 路径。"""
    found: set[str] = set()
    for pat in _EP_PATTERNS:
        for m in pat.finditer(content):
            ep = m.group(1).strip()
            if ep and len(ep) > 2 and not ep.startswith("//"):
                found.add(ep)
    # 过滤明显的非接口（图片、字体等）
    skip_ext = {".png", ".jpg", ".gif", ".svg", ".woff", ".ttf", ".eot", ".ico", ".css", ".map"}
    return sorted(ep for ep in found if not any(ep.lower().endswith(x) for x in skip_ext))


def secret_scan(content: str) -> list[dict]:
    """从 JS 文本中扫描疑似密钥/敏感信息。"""
    hits: list[dict] = []
    lines = content.splitlines()
    for lineno, line in enumerate(lines, 1):
        for kind, pat in _SECRET_PATTERNS:
            for m in pat.finditer(line):
                val = m.group(1) if m.lastindex else m.group(0)
                hits.append({
                    "kind": kind,
                    "value": val[:120],
                    "line": lineno,
                    "context": line.strip()[:200],
                })
    return hits


def analyze_url(url: str, *, timeout: int = 15) -> dict:
    """下载并分析单个 JS URL，返回 endpoints + secrets。"""
    content, err = fetch_js(url, timeout=timeout)
    if err:
        return {"success": False, "url": url, "endpoints": [], "secrets": [], "err": err}
    return {
        "success": True,
        "url": url,
        "size": len(content),
        "endpoints": endpoint_extract(content, url),
        "secrets": secret_scan(content),
        "err": None,
    }


def analyze_file(path: str) -> dict:
    """分析本地 JS 文件。"""
    p = Path(path)
    if not p.exists():
        return {"success": False, "path": path, "endpoints": [], "secrets": [], "err": "文件不存在"}
    content = p.read_text(encoding="utf-8", errors="replace")
    return {
        "success": True,
        "path": path,
        "size": len(content),
        "endpoints": endpoint_extract(content),
        "secrets": secret_scan(content),
        "err": None,
    }