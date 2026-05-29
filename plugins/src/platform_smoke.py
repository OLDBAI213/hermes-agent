"""SRC platform login/state smoke checks via Chrome CDP.

This module is read-only: it opens platform pages, extracts machine-readable
page structure, and reports whether Hermes can continue platform work.
"""
from __future__ import annotations

import argparse
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from websockets.sync.client import connect

from .journal import runs_root


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def _hermes_home() -> Path:
    return Path(os.environ.get("HERMES_HOME", "E:/AI/hermes"))


def _read_cdp_url(home: Path) -> str:
    config_path = home / "config.yaml"
    if config_path.exists():
        try:
            data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
            browser = data.get("browser") if isinstance(data, dict) else None
            value = browser.get("cdp_url") if isinstance(browser, dict) else None
            if value:
                return str(value)
        except Exception:
            pass
    url_file = home / "browser-cdp-url.txt"
    if url_file.exists():
        value = url_file.read_text(encoding="utf-8").strip()
        if value:
            return value
    return "http://localhost:9444"


def _local_cdp_base(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    if parsed.hostname == "localhost":
        url = urllib.parse.urlunparse(parsed._replace(netloc=f"127.0.0.1:{parsed.port or 80}"))
    return url.rstrip("/")


def _clean(text: Any, *, limit: int = 160) -> str:
    value = " ".join(str(text or "").split())
    return value[:limit]


class CdpError(RuntimeError):
    pass


class CdpPage:
    def __init__(self, cdp_url: str, *, timeout: float = 5.0):
        self.cdp_url = cdp_url
        self.timeout = timeout
        self._next_id = 0

    def _page_ws_url(self) -> str:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        try:
            with opener.open(_local_cdp_base(self.cdp_url) + "/json/list", timeout=self.timeout) as resp:
                targets = json.loads(resp.read().decode("utf-8", errors="replace"))
        except (OSError, urllib.error.URLError, json.JSONDecodeError) as exc:
            raise CdpError(f"CDP target list failed: {exc}") from exc

        pages = [
            item
            for item in targets
            if item.get("type") == "page" and item.get("webSocketDebuggerUrl")
        ]
        if not pages:
            raise CdpError("CDP has no page target with websocket debugger url")
        return pages[0]["webSocketDebuggerUrl"].replace("ws://localhost:", "ws://127.0.0.1:")

    def _call(self, ws: Any, method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        self._next_id += 1
        command: dict[str, Any] = {"id": self._next_id, "method": method}
        if params is not None:
            command["params"] = params
        ws.send(json.dumps(command))
        while True:
            message = json.loads(ws.recv(timeout=self.timeout))
            if message.get("id") != self._next_id:
                continue
            if "error" in message:
                error = message["error"]
                raise CdpError(error.get("message") or str(error))
            return message.get("result", {})

    def _connect_page_ws(self) -> Any:
        last_error: Exception | None = None
        for attempt in range(5):
            try:
                return connect(self._page_ws_url(), open_timeout=self.timeout)
            except Exception as exc:
                last_error = exc
                if "10048" not in str(exc) or attempt == 4:
                    raise
                time.sleep(0.25 * (attempt + 1))
        raise CdpError(str(last_error))

    def snapshot(self, url: str | None = None, *, wait_seconds: float = 8.0) -> dict[str, Any]:
        started = time.monotonic()
        requested_url = url or "<current>"
        try:
            with self._connect_page_ws() as ws:
                self._call(ws, "Page.enable")
                self._call(ws, "Runtime.enable")
                if url:
                    self._call(ws, "Page.navigate", {"url": url})

                deadline = time.monotonic() + wait_seconds
                ready_state = ""
                while time.monotonic() < deadline:
                    time.sleep(0.25)
                    state = self._call(
                        ws,
                        "Runtime.evaluate",
                        {"expression": "document.readyState", "returnByValue": True},
                    )
                    ready_state = state.get("result", {}).get("value") or ""
                    if ready_state == "complete":
                        break

                expression = r"""
(() => {
  const clean = (value, limit = 160) => String(value || '').replace(/\s+/g, ' ').trim().slice(0, limit);
  const text = document.body && document.body.innerText || '';
  const clickableSelector = [
    'a','button','[role="button"]','input','textarea','select','[onclick]','[tabindex]',
    '[class*="switch" i]','[class*="toggle" i]','[class*="qr" i]','[class*="code" i]',
    '[class*="scan" i]','[class*="icon" i]','[class*="corner" i]','[class*="login" i]'
  ].join(',');
  const buttonSelector = 'button,[role="button"],input[type="button"],input[type="submit"]';
  const inputSelector = 'input,textarea,select';
  const viewport = { width: window.innerWidth || 0, height: window.innerHeight || 0 };
  const classNameFor = (el) => {
    const value = el.className || '';
    if (typeof value === 'string') return value;
    if (value && typeof value.baseVal === 'string') return value.baseVal;
    return '';
  };
  const selectorFor = (el) => {
    if (!el || !el.tagName) return '';
    if (el.id) return `${el.tagName.toLowerCase()}#${CSS.escape(el.id)}`;
    const parts = [];
    let node = el;
    for (let depth = 0; node && node.nodeType === 1 && depth < 4; depth++, node = node.parentElement) {
      let part = node.tagName.toLowerCase();
      if (node.classList && node.classList.length) {
        part += '.' + Array.from(node.classList).slice(0, 3).map((c) => CSS.escape(c)).join('.');
      }
      if (node.parentElement) {
        const siblings = Array.from(node.parentElement.children).filter((child) => child.tagName === node.tagName);
        if (siblings.length > 1) part += `:nth-of-type(${siblings.indexOf(node) + 1})`;
      }
      parts.unshift(part);
    }
    return parts.join(' > ');
  };
  const describe = (el) => {
    const rect = el.getBoundingClientRect();
    const style = window.getComputedStyle(el);
    const label = clean(el.innerText || el.value || el.getAttribute('aria-label') || el.title || el.alt || el.getAttribute('data-title'));
    const visible = rect.width > 0 && rect.height > 0 && style.display !== 'none' && style.visibility !== 'hidden' && style.opacity !== '0' && style.pointerEvents !== 'none';
    const center = { x: Math.round(rect.left + rect.width / 2), y: Math.round(rect.top + rect.height / 2) };
    let region = 'middle';
    if (rect.top < viewport.height * 0.28 && rect.left > viewport.width * 0.62) region = 'top-right';
    else if (rect.top < viewport.height * 0.28 && rect.left < viewport.width * 0.38) region = 'top-left';
    else if (rect.top > viewport.height * 0.72 && rect.left > viewport.width * 0.62) region = 'bottom-right';
    else if (rect.top > viewport.height * 0.72 && rect.left < viewport.width * 0.38) region = 'bottom-left';
    return {
      tag: el.tagName.toLowerCase(),
      text: label,
      href: el.href || '',
      id: el.id || '',
      className: clean(classNameFor(el), 120),
      name: el.getAttribute('name') || '',
      role: el.getAttribute('role') || '',
      type: el.getAttribute('type') || '',
      title: el.title || '',
      ariaLabel: el.getAttribute('aria-label') || '',
      selector: selectorFor(el),
      rect: {
        x: Math.round(rect.left), y: Math.round(rect.top),
        width: Math.round(rect.width), height: Math.round(rect.height)
      },
      center,
      region,
      visible,
      cursor: style.cursor || '',
      hasOnclick: Boolean(el.onclick || el.getAttribute('onclick')),
      unlabeled: !label
    };
  };
  const controls = Array.from(document.querySelectorAll(clickableSelector))
    .map(describe)
    .filter((item) => item.visible)
    .slice(0, 160);
  const visualCandidates = Array.from(document.querySelectorAll('body *'))
    .map(describe)
    .filter((item) => {
      const small = item.rect.width >= 8 && item.rect.width <= 90 && item.rect.height >= 8 && item.rect.height <= 90;
      const likelyControl = item.cursor === 'pointer' || item.hasOnclick || item.unlabeled || /switch|toggle|qr|code|scan|icon|corner|login/i.test(item.className + ' ' + item.id + ' ' + item.title + ' ' + item.ariaLabel);
      return item.visible && small && likelyControl && item.region === 'top-right';
    })
    .slice(0, 30);
  return {
    url: location.href,
    title: document.title || '',
    readyState: document.readyState,
    textLength: text.length,
    textSample: clean(text, 2200),
    viewport,
    counters: {
      links: document.links.length,
      forms: document.forms.length,
      inputs: document.querySelectorAll(inputSelector).length,
      buttons: document.querySelectorAll(buttonSelector).length,
      clickable: controls.length,
      topRightCandidates: visualCandidates.length
    },
    links: Array.from(document.links).slice(0, 80).map(a => ({
      text: clean(a.innerText || a.textContent),
      href: a.href || ''
    })),
    controls,
    topRightCandidates: visualCandidates,
    forms: Array.from(document.forms).slice(0, 20).map(form => ({
      action: form.action || '',
      method: form.method || '',
      inputCount: form.querySelectorAll(inputSelector).length
    }))
  };
})()
"""
                runtime = self._call(
                    ws,
                    "Runtime.evaluate",
                    {"expression": expression, "returnByValue": True},
                )
                value = runtime.get("result", {}).get("value") or {}
                try:
                    ax_tree = self._call(ws, "Accessibility.getFullAXTree", {"depth": 2})
                    ax_nodes = len(ax_tree.get("nodes", []))
                    ax_error = None
                except Exception as exc:
                    ax_nodes = 0
                    ax_error = str(exc)
        except Exception as exc:
            return {
                "ok": False,
                "requested_url": requested_url,
                "final_url": None,
                "title": None,
                "ready_state": None,
                "text_length": 0,
                "counters": {},
                "links": [],
                "controls": [],
                "top_right_candidates": [],
                "forms": [],
                "accessibility_nodes": 0,
                "elapsed_ms": int((time.monotonic() - started) * 1000),
                "error": str(exc),
            }

        return {
            "ok": True,
            "requested_url": requested_url,
            "final_url": value.get("url"),
            "title": value.get("title"),
            "ready_state": value.get("readyState") or ready_state,
            "text_length": int(value.get("textLength") or 0),
            "text_sample": value.get("textSample") or "",
            "counters": value.get("counters") or {},
            "links": value.get("links") or [],
            "controls": value.get("controls") or [],
            "top_right_candidates": value.get("topRightCandidates") or [],
            "forms": value.get("forms") or [],
            "accessibility_nodes": ax_nodes,
            "accessibility_error": ax_error,
            "elapsed_ms": int((time.monotonic() - started) * 1000),
            "error": None,
        }


PLATFORMS: dict[str, dict[str, Any]] = {
    "vulbox": {
        "name": "漏洞盒子",
        "pages": [
            {"kind": "public_projects", "url": "https://www.vulbox.com/projects/list"},
            {"kind": "account_projects", "url": "https://user.vulbox.com/projectHall/myProject"},
            {"kind": "protected_my_vuln_projects", "url": "https://user.vulbox.com/dashboard/myvuln/project"},
        ],
        "logged_in_signals": [
            "个人中心",
            "我的漏洞",
            "我的项目",
            "财务中心",
            "漏洞提交",
            "退出",
            "logined-wrapper",
            "usermenus-wrapper",
            "go_misson",
        ],
        "login_prompts": ["登录", "注册", "account/login"],
        "project_signals": ["项目大厅", "企业SRC", "赏金", "漏洞", "项目详情", "提交漏洞"],
        "protected_project_signals": ["我的漏洞", "漏洞编号", "漏洞名称", "项目名称", "提交时间", "待审核", "已确认", "已修复"],
    },
    "butian": {
        "name": "补天",
        "pages": [
            {"kind": "public_projects", "url": "https://www.butian.net/Reward/plan"},
            {"kind": "account", "url": "https://www.butian.net/WhiteHat/Center"},
        ],
        "logged_in_signals": ["个人中心", "个人空间", "我的漏洞", "我的项目", "控制台", "退出", "退出系统", "安全专家"],
        "login_prompts": ["登录", "注册", "验证码", "奇安信", "login.html"],
        "project_signals": ["公益SRC", "专属SRC", "企业SRC", "赏金", "漏洞", "厂商"],
    },
}


def _joined_page_text(page: dict[str, Any]) -> str:
    parts = [
        page.get("title") or "",
        page.get("final_url") or "",
        page.get("text_sample") or "",
    ]
    parts.extend(item.get("text") or item.get("href") or "" for item in page.get("links", []))
    for item in page.get("controls", []):
        parts.extend([
            item.get("text") or "",
            item.get("href") or "",
            item.get("className") or "",
            item.get("selector") or "",
        ])
    return "\n".join(parts)


def _signals(text: str, patterns: list[str]) -> list[str]:
    return [pattern for pattern in patterns if pattern and pattern in text]


def _truth_cell(value: Any) -> str:
    if value is True:
        return "是"
    if value is False:
        return "否"
    return "未检查"


def assess_platform(platform: str, pages: list[dict[str, Any]]) -> dict[str, Any]:
    spec = PLATFORMS[platform]
    all_text = "\n".join(_joined_page_text(page) for page in pages if page.get("ok"))
    logged_in_signals = _signals(all_text, spec["logged_in_signals"])
    login_prompts = _signals(all_text, spec["login_prompts"])
    project_signals = _signals(all_text, spec["project_signals"])
    readable_pages = [page for page in pages if page.get("ok") and page.get("text_length", 0) > 0]
    protected_pages = [
        page
        for page in pages
        if str(page.get("kind") or "").startswith("protected_")
    ]
    protected_text = "\n".join(_joined_page_text(page) for page in protected_pages if page.get("ok"))
    protected_project_signals = _signals(protected_text, spec.get("protected_project_signals", []))
    protected_readable_pages = [
        page
        for page in protected_pages
        if page.get("ok") and page.get("text_length", 0) > 0
    ]
    protected_blocked_pages = [
        {
            "kind": page.get("kind"),
            "requested_url": page.get("requested_url"),
            "final_url": page.get("final_url"),
            "title": page.get("title"),
            "text_length": page.get("text_length", 0),
            "error": page.get("error"),
        }
        for page in protected_pages
        if (not page.get("ok")) or page.get("text_length", 0) <= 0
    ]

    account_pages = [
        page
        for page in pages
        if page.get("kind") in {"account", "account_projects"}
    ]
    account_text = "\n".join(_joined_page_text(page) for page in account_pages if page.get("ok"))
    account_logged_in_signals = _signals(account_text, spec["logged_in_signals"])
    account_login_prompts = _signals(account_text, spec["login_prompts"])
    account_redirected_to_login = any(
        "login" in str(page.get("final_url") or "").lower()
        for page in account_pages
        if page.get("ok")
    ) or bool(account_login_prompts)

    if account_logged_in_signals and not account_redirected_to_login:
        login_state = "likely_logged_in"
    elif logged_in_signals and not account_redirected_to_login and not account_login_prompts:
        login_state = "likely_logged_in"
    elif account_redirected_to_login or login_prompts:
        login_state = "login_required_or_unknown"
    else:
        login_state = "unknown"

    return {
        "platform": platform,
        "name": spec["name"],
        "structure_readable": bool(readable_pages),
        "project_entry_readable": bool(project_signals),
        "protected_project_page_readable": bool(protected_readable_pages) if protected_pages else None,
        "protected_project_data_readable": bool(protected_project_signals) if protected_pages else None,
        "protected_project_signals": protected_project_signals[:8],
        "protected_pages_checked": len(protected_pages),
        "protected_readable_pages": len(protected_readable_pages),
        "protected_blocked_pages": protected_blocked_pages[:8],
        "login_state": login_state,
        "logged_in_signals": logged_in_signals[:8],
        "account_logged_in_signals": account_logged_in_signals[:8],
        "login_prompts": login_prompts[:8],
        "account_login_prompts": account_login_prompts[:8],
        "project_signals": project_signals[:8],
        "account_redirected_to_login": account_redirected_to_login,
        "readable_pages": len(readable_pages),
        "pages_checked": len(pages),
    }


def _page_summary(page: dict[str, Any]) -> dict[str, Any]:
    return {
        "ok": page.get("ok"),
        "kind": page.get("kind"),
        "requested_url": page.get("requested_url"),
        "final_url": page.get("final_url"),
        "title": page.get("title"),
        "ready_state": page.get("ready_state"),
        "text_length": page.get("text_length", 0),
        "counters": page.get("counters") or {},
        "top_right_candidates": (page.get("top_right_candidates") or [])[:8],
        "accessibility_nodes": page.get("accessibility_nodes", 0),
        "elapsed_ms": page.get("elapsed_ms", 0),
        "error": page.get("error"),
    }


def _interaction_item(item: dict[str, Any]) -> dict[str, Any]:
    rect = item.get("rect") or {}
    center = item.get("center") or {}
    label = item.get("text") or item.get("ariaLabel") or item.get("title") or item.get("id") or item.get("className") or item.get("selector") or "unlabeled"
    return {
        "label": _clean(label, limit=120),
        "tag": item.get("tag") or "",
        "role": item.get("role") or "",
        "type": item.get("type") or "",
        "href": item.get("href") or "",
        "selector": item.get("selector") or "",
        "region": item.get("region") or "",
        "center": center,
        "rect": rect,
        "unlabeled": bool(item.get("unlabeled")),
    }


def build_interaction_map(page: dict[str, Any], *, limit: int = 80) -> dict[str, Any]:
    controls = [item for item in page.get("controls", []) if item.get("visible", True)]
    top_right_candidates = []
    seen_top_right: set[tuple[Any, Any, Any]] = set()
    for item in controls + page.get("top_right_candidates", []):
        if not item.get("visible", True) or item.get("region") != "top-right":
            continue
        center = item.get("center") or {}
        key = (item.get("selector"), center.get("x"), center.get("y"))
        if key in seen_top_right:
            continue
        seen_top_right.add(key)
        top_right_candidates.append(item)
    inputs = [
        item
        for item in controls
        if item.get("tag") in {"input", "textarea", "select"} or item.get("type") in {"text", "password", "search", "email", "tel"}
    ]
    buttons = [
        item
        for item in controls
        if item.get("tag") == "button" or item.get("role") == "button" or item.get("type") in {"button", "submit"}
    ]
    links = [
        item
        for item in controls
        if item.get("tag") == "a" or item.get("href")
    ]
    icon_candidates = []
    seen_icons: set[tuple[Any, Any, Any]] = set()
    for item in controls + top_right_candidates:
        if not (item.get("unlabeled") or item.get("region") == "top-right"):
            continue
        center = item.get("center") or {}
        key = (item.get("selector"), center.get("x"), center.get("y"))
        if key in seen_icons:
            continue
        seen_icons.add(key)
        icon_candidates.append(item)
    by_region: dict[str, int] = {}
    for item in controls:
        region = item.get("region") or "middle"
        by_region[region] = by_region.get(region, 0) + 1

    return {
        "url": page.get("final_url") or page.get("requested_url"),
        "title": page.get("title"),
        "viewport": page.get("viewport") or {},
        "counts": {
            "controls": len(controls),
            "inputs": len(inputs),
            "buttons": len(buttons),
            "links": len(links),
            "icon_candidates": len(icon_candidates),
            "top_right_candidates": len(top_right_candidates),
        },
        "by_region": by_region,
        "inputs": [_interaction_item(item) for item in inputs[:limit]],
        "buttons": [_interaction_item(item) for item in buttons[:limit]],
        "links": [_interaction_item(item) for item in links[:limit]],
        "icon_candidates": [_interaction_item(item) for item in icon_candidates[:limit]],
        "top_right_candidates": [_interaction_item(item) for item in top_right_candidates[:limit]],
    }


def run_smoke(
    *,
    platforms: list[str] | None = None,
    cdp_url: str | None = None,
    write_report: bool = False,
) -> dict[str, Any]:
    home = _hermes_home()
    cdp_url = cdp_url or _read_cdp_url(home)
    selected = platforms or ["vulbox", "butian"]
    client = CdpPage(cdp_url)
    platform_results: dict[str, Any] = {}

    for platform in selected:
        if platform not in PLATFORMS:
            platform_results[platform] = {"success": False, "error": f"unknown platform: {platform}"}
            continue
        pages: list[dict[str, Any]] = []
        for page in PLATFORMS[platform]["pages"]:
            snapshot = client.snapshot(page["url"])
            snapshot["kind"] = page["kind"]
            pages.append(snapshot)
        assessment = assess_platform(platform, pages)
        interaction_maps = [build_interaction_map(page) for page in pages if page.get("ok")]
        platform_results[platform] = {
            "success": assessment["structure_readable"],
            "assessment": assessment,
            "pages": [_page_summary(page) for page in pages],
            "interaction_maps": interaction_maps,
        }

    any_readable = any(item.get("success") for item in platform_results.values())
    report: dict[str, Any] = {
        "success": True,
        "checked_at": _now(),
        "status": "ready" if any_readable else "degraded",
        "cdp_url": cdp_url,
        "platforms": platform_results,
        "hard_gate": "只读登录态 smoke；不提交、不验证漏洞、不绕过验证码/风控。",
    }
    if write_report:
        report["report_files"] = _write_report(report)
    return report


def _write_report(report: dict[str, Any]) -> dict[str, str]:
    out_dir = runs_root() / f"platform_smoke_{_stamp()}"
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "platform-smoke.json"
    md_path = out_dir / "platform-smoke.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(_render_markdown(report), encoding="utf-8")
    return {"dir": str(out_dir), "json": str(json_path), "markdown": str(md_path)}


def _render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# SRC Platform Smoke",
        "",
        f"- 时间: {report['checked_at']}",
        f"- 总状态: {report['status']}",
        f"- CDP: {report['cdp_url']}",
        f"- 硬门: {report['hard_gate']}",
        "",
        "| 平台 | 结构可读 | 项目入口可读 | 内部任务页可读 | 内部任务数据可读 | 登录态判断 | 登录提示 | 项目信号 |",
        "|---|---:|---:|---:|---:|---|---|---|",
    ]
    for platform, item in report["platforms"].items():
        assessment = item.get("assessment") or {}
        lines.append(
            f"| {assessment.get('name', platform)} | "
            f"{'是' if assessment.get('structure_readable') else '否'} | "
            f"{'是' if assessment.get('project_entry_readable') else '否'} | "
            f"{_truth_cell(assessment.get('protected_project_page_readable'))} | "
            f"{_truth_cell(assessment.get('protected_project_data_readable'))} | "
            f"{assessment.get('login_state', 'unknown')} | "
            f"{', '.join(assessment.get('login_prompts') or [])} | "
            f"{', '.join(assessment.get('project_signals') or [])} |"
        )

    for platform, item in report["platforms"].items():
        lines += ["", f"## {platform}", ""]
        assessment = item.get("assessment") or {}
        protected_data_readable = assessment.get("protected_project_data_readable")
        if protected_data_readable is not None:
            lines += [
                "- 内部页判定:",
                f"  - 内部任务页可读: {_truth_cell(assessment.get('protected_project_page_readable'))}",
                f"  - 内部任务数据可读: {_truth_cell(protected_data_readable)}",
            ]
            protected_signals = assessment.get("protected_project_signals") or []
            if protected_signals:
                lines.append(f"  - 内部数据信号: {', '.join(protected_signals)}")
            elif protected_data_readable is False:
                lines.append("  - 结论: 工具可用，但内部任务数据未验证可读；不能说已经找到项目数据。")
            lines.append("")
        for page in item.get("pages", []):
            counters = page.get("counters") or {}
            lines += [
                f"- 页面: {page.get('kind')}",
                f"- URL: {page.get('final_url') or page.get('requested_url')}",
                f"- 标题: {_clean(page.get('title'), limit=120)}",
                f"- 结构读取: {'成功' if page.get('ok') else '失败'}",
                f"- 文本长度: {page.get('text_length', 0)}",
                f"- 链接/表单/按钮/可点击: {counters.get('links', 0)}/{counters.get('forms', 0)}/{counters.get('buttons', 0)}/{counters.get('clickable', 0)}",
                f"- 右上角无文字/图标候选: {len(page.get('top_right_candidates') or [])}",
                f"- Accessibility 节点: {page.get('accessibility_nodes', 0)}",
            ]
            for candidate in (page.get("top_right_candidates") or [])[:3]:
                rect = candidate.get("rect") or {}
                center = candidate.get("center") or {}
                label = candidate.get("text") or candidate.get("className") or candidate.get("selector") or "unlabeled"
                lines.append(
                    f"  - 候选: {label} @ ({center.get('x')},{center.get('y')}) "
                    f"{rect.get('width')}x{rect.get('height')}"
                )
            if page.get("error"):
                lines.append(f"- 错误: {_clean(page['error'], limit=180)}")
            lines.append("")
        for imap in item.get("interaction_maps", []):
            lines += [
                f"### 可交互地图: {_clean(imap.get('title'), limit=80)}",
                "",
                f"- URL: {imap.get('url')}",
                f"- 控件/输入/按钮/链接/图标候选/右上角候选: {imap['counts']['controls']}/{imap['counts']['inputs']}/{imap['counts']['buttons']}/{imap['counts']['links']}/{imap['counts']['icon_candidates']}/{imap['counts'].get('top_right_candidates', 0)}",
                f"- 区域分布: {json.dumps(imap.get('by_region') or {}, ensure_ascii=False)}",
            ]
            for group in ["inputs", "buttons", "top_right_candidates", "icon_candidates"]:
                sample = imap.get(group) or []
                if not sample:
                    continue
                lines.append(f"- {group} 示例:")
                for action in sample[:8]:
                    center = action.get("center") or {}
                    label = action.get("label") or "unlabeled"
                    lines.append(f"  - {label} [{action.get('tag')}/{action.get('type')}] @ ({center.get('x')},{center.get('y')})")
            lines.append("")
    return "\n".join(lines) + "\n"


def compact_report(report: dict[str, Any]) -> dict[str, Any]:
    return {
        "success": report.get("success"),
        "status": report.get("status"),
        "cdp_url": report.get("cdp_url"),
        "platforms": {
            name: {
                "success": item.get("success"),
                "assessment": item.get("assessment"),
                "interaction_counts": [
                    imap.get("counts") for imap in item.get("interaction_maps", [])
                ],
            }
            for name, item in (report.get("platforms") or {}).items()
        },
        "report_files": report.get("report_files"),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run read-only SRC platform smoke checks.")
    parser.add_argument("--platform", action="append", choices=sorted(PLATFORMS), help="platform to check")
    parser.add_argument("--cdp-url", help="CDP url to check, default reads Hermes config")
    parser.add_argument("--write-report", action="store_true", help="write platform-smoke.json/md under runs/src")
    parser.add_argument("--full", action="store_true", help="print the full structured report instead of compact summary")
    args = parser.parse_args(argv)
    report = run_smoke(platforms=args.platform, cdp_url=args.cdp_url, write_report=args.write_report)
    print(json.dumps(report if args.full else compact_report(report), ensure_ascii=False, indent=2))
    return 0 if report["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
