"""SRC Suite health checks.

Checks are intentionally non-invasive: no browser/emulator startup, no config
mutation, no login-state export. The goal is to prove what is present, what is
reachable, and whether a task report can be written.
"""
from __future__ import annotations

import argparse
import ctypes
import json
import os
import shutil
import socket
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from .journal import runs_root
from .tools.httpx import _resolve_binary as httpx_bin
from .tools.katana import _resolve_binary as katana_bin
from .tools.naabu import _resolve_binary as naabu_bin
from .tools.subfinder import _resolve_binary as subfinder_bin


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def _hermes_home() -> Path:
    return Path(os.environ.get("HERMES_HOME", "E:/AI/hermes"))


def _run(cmd: list[str], *, timeout: float = 3.0) -> dict[str, Any]:
    started = time.monotonic()
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            check=False,
            text=True,
            timeout=timeout,
            env={
                **os.environ,
                "NO_PROXY": "localhost,127.0.0.1",
                "no_proxy": "localhost,127.0.0.1",
                "PYTHONIOENCODING": "utf-8",
            },
        )
    except subprocess.TimeoutExpired:
        return {
            "ok": False,
            "exit_code": None,
            "elapsed_ms": int((time.monotonic() - started) * 1000),
            "stdout": "",
            "stderr": "",
            "error": f"timeout after {timeout:g}s",
        }
    except OSError as exc:
        return {
            "ok": False,
            "exit_code": None,
            "elapsed_ms": int((time.monotonic() - started) * 1000),
            "stdout": "",
            "stderr": "",
            "error": str(exc),
        }

    return {
        "ok": proc.returncode == 0,
        "exit_code": proc.returncode,
        "elapsed_ms": int((time.monotonic() - started) * 1000),
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "error": None,
    }


def _first_line(text: str) -> str:
    return next((line.strip() for line in text.splitlines() if line.strip()), "")


def _path_status(path: Path) -> dict[str, Any]:
    return {"path": str(path), "exists": path.exists(), "is_dir": path.is_dir()}


def _binary_status(path: str | None) -> dict[str, Any]:
    return {"available": bool(path), "path": path}


def _read_config_cdp(home: Path) -> str | None:
    cfg = home / "config.yaml"
    if not cfg.exists():
        return None
    try:
        data = yaml.safe_load(cfg.read_text(encoding="utf-8")) or {}
    except Exception:
        return None
    browser = data.get("browser")
    if isinstance(browser, dict):
        value = browser.get("cdp_url")
        return str(value) if value else None
    return None


def _read_cdp_url_file(home: Path) -> str | None:
    path = home / "browser-cdp-url.txt"
    if not path.exists():
        return None
    value = path.read_text(encoding="utf-8").strip()
    return value or None


def _local_cdp_base(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    if parsed.hostname == "localhost":
        url = urllib.parse.urlunparse(parsed._replace(netloc=f"127.0.0.1:{parsed.port or 80}"))
    return url.rstrip("/")


def _probe_cdp(url: str, *, timeout: float = 1.0) -> dict[str, Any]:
    version_url = _local_cdp_base(url) + "/json/version"
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    started = time.monotonic()
    try:
        with opener.open(version_url, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8", errors="replace"))
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        return {
            "url": url,
            "reachable": False,
            "elapsed_ms": int((time.monotonic() - started) * 1000),
            "product": None,
            "browser": None,
            "error": str(exc),
        }
    return {
        "url": url,
        "reachable": True,
        "elapsed_ms": int((time.monotonic() - started) * 1000),
        "product": payload.get("Browser") or payload.get("browser"),
        "browser": payload.get("Browser"),
        "error": None,
    }


def _browser_structure_snapshot(url: str | None, *, timeout: float = 3.0) -> dict[str, Any]:
    if not url:
        return {
            "ok": False,
            "target_url": None,
            "title": None,
            "ready_state": None,
            "text_length": 0,
            "links": 0,
            "forms": 0,
            "inputs": 0,
            "buttons": 0,
            "clickable": 0,
            "accessibility_nodes": 0,
            "error": "CDP url not configured",
        }

    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    started = time.monotonic()
    try:
        with opener.open(_local_cdp_base(url) + "/json/list", timeout=timeout) as resp:
            targets = json.loads(resp.read().decode("utf-8", errors="replace"))
        pages = [
            item
            for item in targets
            if item.get("type") == "page" and item.get("webSocketDebuggerUrl")
        ]
        if not pages:
            raise RuntimeError("no page target with websocket debugger url")

        ws_url = pages[0]["webSocketDebuggerUrl"].replace("ws://localhost:", "ws://127.0.0.1:")
        from websockets.sync.client import connect

        next_id = 0

        def connect_ws() -> Any:
            for attempt in range(5):
                try:
                    return connect(ws_url, open_timeout=timeout)
                except Exception as exc:
                    if "10048" not in str(exc) or attempt == 4:
                        raise
                    time.sleep(0.25 * (attempt + 1))

        def call(method: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
            nonlocal next_id
            next_id += 1
            command = {"id": next_id, "method": method}
            if params is not None:
                command["params"] = params
            ws.send(json.dumps(command))
            while True:
                message = json.loads(ws.recv(timeout=timeout))
                if message.get("id") != next_id:
                    continue
                if "error" in message:
                    error = message["error"]
                    raise RuntimeError(error.get("message") or str(error))
                return message.get("result", {})

        with connect_ws() as ws:
            expression = """
(() => {
  const clickableSelector = 'a,button,[role="button"],input,textarea,select,[onclick]';
  const buttonSelector = 'button,[role="button"],input[type="button"],input[type="submit"]';
  return {
    url: location.href,
    title: document.title || '',
    readyState: document.readyState,
    textLength: (document.body && document.body.innerText || '').length,
    links: document.links.length,
    forms: document.forms.length,
    inputs: document.querySelectorAll('input,textarea,select').length,
    buttons: document.querySelectorAll(buttonSelector).length,
    clickable: document.querySelectorAll(clickableSelector).length
  };
})()
"""
            runtime = call("Runtime.evaluate", {"expression": expression, "returnByValue": True})
            value = runtime.get("result", {}).get("value") or {}
            try:
                ax = call("Accessibility.getFullAXTree", {"depth": 2})
                ax_nodes = len(ax.get("nodes", []))
                ax_error = None
            except Exception as exc:
                ax_nodes = 0
                ax_error = str(exc)
    except Exception as exc:
        return {
            "ok": False,
            "target_url": None,
            "title": None,
            "ready_state": None,
            "text_length": 0,
            "links": 0,
            "forms": 0,
            "inputs": 0,
            "buttons": 0,
            "clickable": 0,
            "accessibility_nodes": 0,
            "elapsed_ms": int((time.monotonic() - started) * 1000),
            "error": str(exc),
        }

    return {
        "ok": True,
        "target_url": value.get("url"),
        "title": value.get("title"),
        "ready_state": value.get("readyState"),
        "text_length": int(value.get("textLength") or 0),
        "links": int(value.get("links") or 0),
        "forms": int(value.get("forms") or 0),
        "inputs": int(value.get("inputs") or 0),
        "buttons": int(value.get("buttons") or 0),
        "clickable": int(value.get("clickable") or 0),
        "accessibility_nodes": ax_nodes,
        "accessibility_error": ax_error,
        "elapsed_ms": int((time.monotonic() - started) * 1000),
        "error": None,
    }


def _browser_report(home: Path) -> dict[str, Any]:
    configured = _read_config_cdp(home)
    url_file = _read_cdp_url_file(home)
    recommended = "http://localhost:9444"
    urls = []
    for url in [configured, url_file, recommended, "http://localhost:9222", "http://localhost:9333"]:
        if url and url not in urls:
            urls.append(url)

    chrome = Path("C:/Program Files/Google/Chrome/Application/chrome.exe")
    edge = Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
    profiles = {
        "hermes_chrome_debug_9333": _path_status(home / "chrome-debug-9333"),
        "src_project_browser_profile": _path_status(Path("E:/AI/src_project/browser_profile")),
        "src_project_vulbox_profile": _path_status(Path("E:/AI/src_project/vulbox_profile")),
        "recommended_shared_main": _path_status(Path("E:/AI/browser-profiles/shared-main")),
        "recommended_src_main": _path_status(Path("E:/AI/browser-profiles/src-main")),
    }
    probes = [_probe_cdp(url) for url in urls]
    reachable = [p for p in probes if p["reachable"]]
    structure_url = reachable[0]["url"] if reachable else configured or url_file or recommended
    structure = _browser_structure_snapshot(structure_url)
    reachable_urls = [p["url"] for p in reachable]
    if not reachable_urls and structure["ok"]:
        reachable_urls = [structure_url]

    return {
        "configured_cdp_url": configured,
        "url_file_cdp_url": url_file,
        "recommended_cdp_url": recommended,
        "cdp_urls_match_recommendation": configured == recommended and url_file == recommended,
        "any_cdp_reachable": bool(reachable_urls),
        "reachable_urls": reachable_urls,
        "probes": probes,
        "structure": structure,
        "chrome": _path_status(chrome),
        "edge": _path_status(edge),
        "profiles": profiles,
    }


def browser_status(home: Path | None = None) -> dict[str, Any]:
    """Return the browser callability report used by Hermes CLI/MCP wrappers."""
    return _browser_report(home or _hermes_home())


def _dns_probe(host: str, *, port: int = 443) -> dict[str, Any]:
    started = time.monotonic()
    try:
        infos = socket.getaddrinfo(host, port, proto=socket.IPPROTO_TCP)
    except OSError as exc:
        return {
            "host": host,
            "ok": False,
            "elapsed_ms": int((time.monotonic() - started) * 1000),
            "addresses": [],
            "error": str(exc),
        }
    addresses = sorted({info[4][0] for info in infos})
    return {
        "host": host,
        "ok": bool(addresses),
        "elapsed_ms": int((time.monotonic() - started) * 1000),
        "addresses": addresses[:5],
        "error": None,
    }


def _https_probe(url: str, *, timeout: float = 5.0) -> dict[str, Any]:
    started = time.monotonic()
    req = urllib.request.Request(url, headers={"User-Agent": "Hermes-SrcSuite-Health/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(512)
            status = getattr(resp, "status", None)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {
            "url": url,
            "ok": False,
            "status": None,
            "elapsed_ms": int((time.monotonic() - started) * 1000),
            "bytes_read": 0,
            "error": str(exc),
        }
    return {
        "url": url,
        "ok": bool(status and 200 <= int(status) < 400),
        "status": status,
        "elapsed_ms": int((time.monotonic() - started) * 1000),
        "bytes_read": len(body),
        "error": None,
    }


def _redact_url(value: str) -> str:
    try:
        parsed = urllib.parse.urlparse(value)
    except ValueError:
        return "<set>"
    if not parsed.scheme or not parsed.netloc:
        return "<set>"
    host = parsed.hostname or ""
    if parsed.port:
        host = f"{host}:{parsed.port}"
    return urllib.parse.urlunparse(parsed._replace(netloc=host, path="", params="", query="", fragment=""))


def _env_proxy_status(name: str) -> dict[str, Any]:
    value = os.environ.get(name) or os.environ.get(name.lower())
    return {"set": bool(value), "value": _redact_url(value) if value else None}


def _network_report() -> dict[str, Any]:
    dns = {
        "example.com": _dns_probe("example.com"),
        "baidu.com": _dns_probe("www.baidu.com"),
    }
    https = {
        "example.com": _https_probe("https://example.com"),
        "baidu.com": _https_probe("https://www.baidu.com"),
    }
    no_proxy = os.environ.get("NO_PROXY") or os.environ.get("no_proxy") or ""
    return {
        "dns_ok": any(item["ok"] for item in dns.values()),
        "https_ok": any(item["ok"] for item in https.values()),
        "dns": dns,
        "https": https,
        "proxy_env": {
            "HTTP_PROXY": _env_proxy_status("HTTP_PROXY"),
            "HTTPS_PROXY": _env_proxy_status("HTTPS_PROXY"),
            "ALL_PROXY": _env_proxy_status("ALL_PROXY"),
            "NO_PROXY": _env_proxy_status("NO_PROXY"),
        },
        "no_proxy_has_localhost": "localhost" in no_proxy and "127.0.0.1" in no_proxy,
    }


def _screen_metrics() -> dict[str, Any]:
    if os.name != "nt":
        return {"available": False, "width": None, "height": None, "remote_session": None, "error": "not windows"}
    try:
        user32 = ctypes.windll.user32
        width = int(user32.GetSystemMetrics(0))
        height = int(user32.GetSystemMetrics(1))
        remote = bool(user32.GetSystemMetrics(0x1000))
    except Exception as exc:
        return {"available": False, "width": None, "height": None, "remote_session": None, "error": str(exc)}
    return {
        "available": width > 0 and height > 0,
        "width": width,
        "height": height,
        "remote_session": remote,
        "error": None,
    }


def _chrome_render_probe(artifact_dir: Path | None) -> dict[str, Any]:
    chrome = Path("C:/Program Files/Google/Chrome/Application/chrome.exe")
    if not chrome.exists():
        return {"ok": False, "artifact": None, "bytes": 0, "error": "chrome not found"}
    if artifact_dir is None:
        return {"ok": None, "artifact": None, "bytes": 0, "error": "not run without report directory"}

    display_dir = artifact_dir / "display"
    display_dir.mkdir(parents=True, exist_ok=True)
    html = display_dir / "render.html"
    screenshot = display_dir / "chrome-render.png"
    html.write_text(
        "<!doctype html><meta charset='utf-8'><title>SRC Health</title>"
        "<style>body{font-family:Arial;margin:40px}main{width:640px;height:360px;"
        "border:4px solid #31C476;padding:24px}</style>"
        "<main><h1>SRC Health Render</h1><p>Chrome rendering check.</p></main>",
        encoding="utf-8",
    )
    result = _run(
        [
            str(chrome),
            "--headless=new",
            "--disable-gpu",
            "--no-first-run",
            "--disable-default-apps",
            "--window-size=1280,720",
            f"--screenshot={screenshot}",
            html.as_uri(),
        ],
        timeout=15,
    )
    size = screenshot.stat().st_size if screenshot.exists() else 0
    return {
        "ok": result["ok"] and size > 1000,
        "artifact": str(screenshot) if screenshot.exists() else None,
        "bytes": size,
        "elapsed_ms": result["elapsed_ms"],
        "error": result["error"] or (result["stderr"][:500] if not result["ok"] else None),
    }


def _display_report(artifact_dir: Path | None = None) -> dict[str, Any]:
    screen = _screen_metrics()
    chrome_render = _chrome_render_probe(artifact_dir)
    return {
        "screen": screen,
        "chrome_render": chrome_render,
        "display_ok": bool(screen["available"] and chrome_render["ok"]),
    }


def _security_tools_report() -> dict[str, Any]:
    sec = Path("E:/AI/security-tools")
    return {
        "root": _path_status(sec),
        "tools": {
            "subfinder": _binary_status(subfinder_bin()),
            "httpx": _binary_status(httpx_bin()),
            "naabu": _binary_status(naabu_bin()),
            "katana": _binary_status(katana_bin()),
            "nuclei": _binary_status(str(sec / "nuclei.exe") if (sec / "nuclei.exe").exists() else shutil.which("nuclei")),
            "ffuf": _binary_status(str(sec / "ffuf.exe") if (sec / "ffuf.exe").exists() else shutil.which("ffuf")),
        },
    }


def _connected_devices(stdout: str) -> list[str]:
    devices: list[str] = []
    for line in stdout.splitlines():
        line = line.strip()
        if not line or line.startswith("List of devices"):
            continue
        parts = line.split()
        if len(parts) >= 2 and parts[1] == "device":
            devices.append(parts[0])
    return devices


def _adb_screencap(adb: Path, serial: str, artifact_dir: Path | None) -> dict[str, Any]:
    if artifact_dir is None:
        return {"ok": None, "artifact": None, "bytes": 0, "error": "not run without report directory"}
    android_dir = artifact_dir / "android"
    android_dir.mkdir(parents=True, exist_ok=True)
    screenshot = android_dir / f"{serial}-screencap.png"
    started = time.monotonic()
    try:
        proc = subprocess.run(
            [str(adb), "-s", serial, "exec-out", "screencap", "-p"],
            capture_output=True,
            check=False,
            timeout=10,
        )
    except (subprocess.TimeoutExpired, OSError) as exc:
        return {
            "ok": False,
            "artifact": None,
            "bytes": 0,
            "elapsed_ms": int((time.monotonic() - started) * 1000),
            "error": str(exc),
        }
    if proc.returncode == 0 and proc.stdout:
        screenshot.write_bytes(proc.stdout)
    size = screenshot.stat().st_size if screenshot.exists() else 0
    return {
        "ok": proc.returncode == 0 and size > 1000,
        "artifact": str(screenshot) if screenshot.exists() else None,
        "bytes": size,
        "elapsed_ms": int((time.monotonic() - started) * 1000),
        "error": proc.stderr.decode("utf-8", errors="replace")[:500] if proc.returncode else None,
    }


def _adb_ui_dump(adb: Path, serial: str, artifact_dir: Path | None) -> dict[str, Any]:
    if artifact_dir is None:
        return {"ok": None, "xml": None, "json": None, "nodes": 0, "clickable": 0, "error": "not run without report directory"}
    android_dir = artifact_dir / "android"
    android_dir.mkdir(parents=True, exist_ok=True)
    xml_path = android_dir / f"{serial}-window.xml"
    summary_path = android_dir / f"{serial}-window-summary.json"
    dump = _run([str(adb), "-s", serial, "shell", "uiautomator", "dump", "/sdcard/window.xml"], timeout=10)
    if not dump["ok"]:
        return {"ok": False, "xml": None, "json": None, "nodes": 0, "clickable": 0, "error": dump["error"] or dump["stderr"]}
    pull = _run([str(adb), "-s", serial, "pull", "/sdcard/window.xml", str(xml_path)], timeout=10)
    if not pull["ok"] or not xml_path.exists():
        return {"ok": False, "xml": None, "json": None, "nodes": 0, "clickable": 0, "error": pull["error"] or pull["stderr"]}
    text = xml_path.read_text(encoding="utf-8", errors="replace")
    nodes = text.count("<node ")
    clickable = text.count('clickable="true"')
    size = _run([str(adb), "-s", serial, "shell", "wm", "size"], timeout=5)
    focus = _run([str(adb), "-s", serial, "shell", "dumpsys", "window"], timeout=10)
    focus_lines = [
        line.strip()
        for line in focus["stdout"].splitlines()
        if "mCurrentFocus" in line or "mFocusedApp" in line
    ][:3]
    summary = {
        "ok": True,
        "xml": str(xml_path),
        "json": str(summary_path),
        "nodes": nodes,
        "clickable": clickable,
        "screen_size": size["stdout"].strip(),
        "focus": focus_lines,
    }
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def _android_report(artifact_dir: Path | None = None) -> dict[str, Any]:
    sdk_candidates = [
        Path("E:/AI/android/sdk"),
        Path("C:/Users/Administrator/AppData/Local/Android/Sdk"),
    ]
    sdk_root = next((p for p in sdk_candidates if p.exists()), sdk_candidates[0])
    adb = sdk_root / "platform-tools" / "adb.exe"
    emulator = sdk_root / "emulator" / "emulator.exe"
    java_candidates = [
        Path("E:/AI/android/jre17/jdk-17.0.19+10-jre/bin/java.exe"),
        Path("C:/Program Files/Android/Android Studio/jbr/bin/java.exe"),
    ]
    java = next((p for p in java_candidates if p.exists()), None)

    adb_version = _run([str(adb), "version"], timeout=3) if adb.exists() else None
    devices = _run([str(adb), "devices", "-l"], timeout=3) if adb.exists() else None
    avds = _run([str(emulator), "-list-avds"], timeout=5) if emulator.exists() else None
    root_avd_present = bool(avds and "root_avd" in avds.get("stdout", "").split())
    connected = _connected_devices(devices["stdout"]) if devices else []
    screen = _adb_screencap(adb, connected[0], artifact_dir) if adb.exists() and connected else {
        "ok": False,
        "artifact": None,
        "bytes": 0,
        "error": "no connected android device",
    }
    ui_dump = _adb_ui_dump(adb, connected[0], artifact_dir) if adb.exists() and connected else {
        "ok": False,
        "xml": None,
        "json": None,
        "nodes": 0,
        "clickable": 0,
        "error": "no connected android device",
    }

    return {
        "sdk_root": _path_status(sdk_root),
        "adb": {
            **_path_status(adb),
            "version": _first_line(adb_version["stdout"]) if adb_version else "",
            "devices_stdout": devices["stdout"] if devices else "",
            "connected_devices": connected,
        },
        "emulator": {
            **_path_status(emulator),
            "avds": avds["stdout"].splitlines() if avds and avds["ok"] else [],
            "root_avd_present": root_avd_present,
        },
        "screen": screen,
        "ui_dump": ui_dump,
        "java": _path_status(java) if java else {"path": None, "exists": False, "is_dir": False},
    }


def _task_storage_report() -> dict[str, Any]:
    root = runs_root()
    try:
        root.mkdir(parents=True, exist_ok=True)
        writable = True
        error = None
    except OSError as exc:
        writable = False
        error = str(exc)
    return {"runs_dir": str(root), "exists": root.exists(), "writable": writable, "error": error}


def _yes_no(value: bool) -> str:
    return "是" if value else "否"


def _capability(name: str, call_path: bool, live_callable: bool, good_to_use: bool, blocker: str | None) -> dict[str, Any]:
    return {
        "name": name,
        "call_path_exists": call_path,
        "live_callable_by_hermes": live_callable,
        "good_to_use": good_to_use,
        "blocker": blocker,
    }


def _capability_matrix(report: dict[str, Any]) -> dict[str, dict[str, Any]]:
    tools = report["security_tools"]["tools"]
    browser = report["browser"]
    android = report["android"]
    storage = report["task_storage"]
    network = report["network"]
    display = report["display"]

    bulk_path = all(tools[name]["available"] for name in ["subfinder", "httpx", "katana"])
    bulk_live = bulk_path and storage["writable"] and network["dns_ok"]
    bulk_good = bulk_live and network["https_ok"]

    browser_path = bool(browser["chrome"]["exists"] and (browser["configured_cdp_url"] or browser["url_file_cdp_url"]))
    browser_live = bool(browser["any_cdp_reachable"])
    browser_structure = bool(browser["structure"]["ok"])
    src_profile_ready = bool(browser["profiles"].get("recommended_shared_main", {}).get("exists"))
    browser_good = bool(
        browser_live
        and browser_structure
        and browser["cdp_urls_match_recommendation"]
        and src_profile_ready
    )
    browser_blockers = []
    if not browser_live:
        browser_blockers.append("CDP 没连上")
    if browser_live and not browser_structure:
        browser_blockers.append("页面 DOM/Accessibility 结构不可读")
    if not browser["cdp_urls_match_recommendation"]:
        browser_blockers.append("CDP 配置/文件未统一到 9444")
    if not src_profile_ready:
        browser_blockers.append("统一 shared-main profile 不存在")

    android_path = bool(android["adb"]["exists"] and android["emulator"]["exists"])
    android_live = android_path and bool(android["emulator"]["root_avd_present"])
    android_good = android_live and bool(android["screen"]["ok"])
    android_ui_good = android_live and bool(android["ui_dump"]["ok"])

    return {
        "bulk_collection": _capability(
            "批量搜索/资产获取",
            bulk_path,
            bulk_live,
            bulk_good,
            None if bulk_good else "工具、网络或落盘有一项不可用",
        ),
        "browser_logged_in_cdp": _capability(
            "持久 Profile 浏览器/CDP",
            browser_path,
            browser_live,
            browser_good,
            "；".join(browser_blockers) if browser_blockers else None,
        ),
        "browser_structured_page": _capability(
            "浏览器机器可读页面结构",
            browser_path,
            browser_structure,
            browser_structure,
            None if browser_structure else "CDP 未连接或无法读取 DOM/Accessibility",
        ),
        "browser_interaction_map": _capability(
            "浏览器交互地图",
            browser_path,
            browser_structure,
            browser_structure,
            None if browser_structure else "CDP 未连接或无法读取 DOM/Accessibility",
        ),
        "chrome_render": _capability(
            "Chrome 显示渲染",
            bool(browser["chrome"]["exists"]),
            bool(display["chrome_render"]["ok"]),
            bool(display["display_ok"]),
            None if display["display_ok"] else "Chrome 渲染截图失败或桌面不可用",
        ),
        "android_adb_avd": _capability(
            "安卓 ADB/AVD",
            android_path,
            android_live,
            android_live,
            None if android_live else "ADB、emulator 或 root_avd 不可用",
        ),
        "android_screen": _capability(
            "安卓画面截图",
            android_live,
            bool(android["screen"]["ok"]),
            bool(android["screen"]["ok"]),
            None if android["screen"]["ok"] else "当前没有连接中的安卓设备",
        ),
        "android_ui_tree": _capability(
            "安卓机器可读 UI 树",
            android_live,
            bool(android["ui_dump"]["ok"]),
            android_ui_good,
            None if android_ui_good else "当前没有连接中的安卓设备或 uiautomator dump 失败",
        ),
        "task_storage": _capability(
            "SRC 任务落盘",
            storage["exists"],
            storage["writable"],
            storage["writable"],
            storage["error"],
        ),
    }


def _render_markdown(report: dict[str, Any]) -> str:
    usable = report["usable_now"]
    browser = report["browser"]
    android = report["android"]
    storage = report["task_storage"]
    tools = report["security_tools"]["tools"]
    capabilities = report["capabilities"]
    lines = [
        "# SRC Suite Health",
        "",
        f"- 时间: {report['checked_at']}",
        f"- 总状态: {report['status']}",
        f"- 任务目录: {storage['runs_dir']}",
        "",
        "## 能力状态",
        "",
        f"- 大规模搜索/资产工具: {'可用' if usable['bulk_collection'] else '不可用'}",
        f"- 外网 DNS/HTTPS: {'可用' if usable['external_network'] else '不可用'}",
        f"- Windows/Chrome 显示渲染: {'可用' if usable['local_display'] else '不可用'}",
        f"- 持久 Profile 浏览器 CDP: {'可连' if usable['logged_in_browser'] else '未连上'}",
        f"- 浏览器机器可读页面: {'可用' if usable['browser_structured_page'] else '未验证'}",
        f"- 浏览器交互地图: {'可用' if usable['browser_interaction_map'] else '未验证'}",
        f"- 安卓/模拟器基础: {'可用' if usable['android_base'] else '不可用'}",
        f"- 安卓画面截图: {'可用' if usable['android_display'] else '未验证'}",
        f"- 安卓机器可读 UI: {'可用' if usable['android_ui_tree'] else '未验证'}",
        f"- 任务目录落盘: {'可写' if usable['task_storage'] else '不可写'}",
        "",
        "## Hermes 调用矩阵",
        "",
        "| 能力 | 接入口存在 | Hermes 现在能直接调用 | 调用后好用 | 阻塞 |",
        "|---|---:|---:|---:|---|",
    ]
    for item in capabilities.values():
        lines.append(
            f"| {item['name']} | {_yes_no(item['call_path_exists'])} | "
            f"{_yes_no(item['live_callable_by_hermes'])} | {_yes_no(item['good_to_use'])} | "
            f"{item['blocker'] or ''} |"
        )
    lines += [
        "",
        "## 网络",
        "",
        f"- DNS: {'可用' if report['network']['dns_ok'] else '不可用'}",
        f"- HTTPS: {'可用' if report['network']['https_ok'] else '不可用'}",
        f"- NO_PROXY 包含本地地址: {'是' if report['network']['no_proxy_has_localhost'] else '否'}",
        "",
        "## 显示",
        "",
        f"- 屏幕: {report['display']['screen']['width']}x{report['display']['screen']['height']}",
        f"- Chrome 渲染截图: {report['display']['chrome_render']['artifact'] or '未生成'}",
        "",
        "## 浏览器",
        "",
        f"- 配置 CDP: {browser['configured_cdp_url']}",
        f"- 文件 CDP: {browser['url_file_cdp_url']}",
        f"- 推荐 CDP: {browser['recommended_cdp_url']}",
        f"- 当前可连: {', '.join(browser['reachable_urls']) if browser['reachable_urls'] else '无'}",
        f"- 机器可读页面: {'可用' if browser['structure']['ok'] else '未验证'}",
        f"- 当前页面: {browser['structure']['target_url'] or '未读取'}",
        f"- 可点击元素: {browser['structure']['clickable']}",
        f"- Accessibility 节点: {browser['structure']['accessibility_nodes']}",
        "",
        "## 安卓",
        "",
        f"- SDK: {android['sdk_root']['path']} ({'存在' if android['sdk_root']['exists'] else '缺失'})",
        f"- ADB: {android['adb']['path']} ({'存在' if android['adb']['exists'] else '缺失'})",
        f"- Emulator: {android['emulator']['path']} ({'存在' if android['emulator']['exists'] else '缺失'})",
        f"- root_avd: {'存在' if android['emulator']['root_avd_present'] else '未发现'}",
        f"- 已连接设备: {', '.join(android['adb']['connected_devices']) if android['adb']['connected_devices'] else '无'}",
        f"- 安卓截图: {android['screen']['artifact'] or '未生成'}",
        f"- 安卓 UI XML: {android['ui_dump']['xml'] or '未生成'}",
        f"- 可点击节点: {android['ui_dump']['clickable']}",
        "",
        "## 安全工具",
        "",
    ]
    for name, item in tools.items():
        lines.append(f"- {name}: {'可用' if item['available'] else '缺失'}")
    return "\n".join(lines) + "\n"


def _write_report(report: dict[str, Any], task_dir: Path | None = None) -> dict[str, str]:
    task_dir = task_dir or runs_root() / f"health_{_stamp()}"
    task_dir.mkdir(parents=True, exist_ok=True)
    json_path = task_dir / "health-report.json"
    md_path = task_dir / "health-report.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(_render_markdown(report), encoding="utf-8")
    return {"dir": str(task_dir), "json": str(json_path), "markdown": str(md_path)}


def run_health(
    *,
    current_task: str | None = None,
    scope: list[str] | None = None,
    workflows: list[str] | None = None,
    hardgate_rules: int | None = None,
    write_report: bool = False,
) -> dict[str, Any]:
    home = _hermes_home()
    report_dir = runs_root() / f"health_{_stamp()}" if write_report else None
    security = _security_tools_report()
    network = _network_report()
    browser = _browser_report(home)
    display = _display_report(report_dir)
    android = _android_report(report_dir)
    task_storage = _task_storage_report()

    bulk_collection = all(
        security["tools"][name]["available"]
        for name in ["subfinder", "httpx", "katana"]
    )
    android_base = (
        android["adb"]["exists"]
        and android["emulator"]["exists"]
        and android["emulator"]["root_avd_present"]
    )
    usable_now = {
        "bulk_collection": bulk_collection,
        "external_network": network["dns_ok"] and network["https_ok"],
        "local_display": display["display_ok"],
        "logged_in_browser": browser["any_cdp_reachable"],
        "browser_structured_page": bool(browser["structure"]["ok"]),
        "browser_interaction_map": bool(browser["structure"]["ok"]),
        "android_base": android_base,
        "android_display": bool(android["screen"]["ok"]),
        "android_ui_tree": bool(android["ui_dump"]["ok"]),
        "task_storage": task_storage["writable"],
    }
    status = "ready" if all(usable_now.values()) else "degraded"

    report: dict[str, Any] = {
        "success": True,
        "stage": "P1-health",
        "checked_at": _now(),
        "status": status,
        "hermes_home": str(home),
        "task_storage": task_storage,
        "runs_dir": task_storage["runs_dir"],
        "runs_dir_exists": task_storage["exists"],
        "network": network,
        "display": display,
        "security_tools": security,
        "tools": security["tools"],
        "browser": browser,
        "android": android,
        "usable_now": usable_now,
        "workflows": workflows or [],
        "hardgate_rules": hardgate_rules,
        "containers": {"docker": bool(shutil.which("docker")), "wsl": bool(shutil.which("wsl"))},
        "current_task": current_task,
        "scope": scope or ["*"],
    }
    report["capabilities"] = _capability_matrix(report)
    if write_report:
        report["report_files"] = _write_report(report, report_dir)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run non-invasive SRC Suite health checks.")
    parser.add_argument("--write-report", action="store_true", help="write health-report.json/md under runs/src")
    args = parser.parse_args(argv)
    report = run_health(write_report=args.write_report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
