"""SRC Suite 门面 —— AI-first API。P0 阶段。

六大动词：recon / browse / scan / exploit / mobile / report
辅助：evidence / ledger / health / task / workflow / hardgate

P0 已实现：recon 全套（subdomains/alive/tech_detect/crawl/ports）
           workflow DAG runner（recon_full）
           hardgate 五条规则（pre-call + post-call）
           scope prelude（task.new 携带 platform/scope）
P1+：scan / exploit / mobile / report / browse
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .journal import Journal, new_task_id, runs_root
from .tools import subfinder as t_subfinder
from .tools import httpx as t_httpx
from .tools import naabu as t_naabu
from .tools import katana as t_katana
from .tools import nuclei as t_nuclei
from .tools import jsanalyze as t_js
from . import hardgate as _hardgate
from . import workflow as _workflow
from . import health as _health


def _asset_id(kind: str, value: str) -> str:
    """资产 id = sha1(kind:value) 前 16 位，跨任务稳定可去重。"""
    return hashlib.sha1(f"{kind}:{value}".encode("utf-8")).hexdigest()[:16]


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _stub(verb: str, action: str) -> dict:
    return {
        "success": False,
        "error": "未实现",
        "stage": "P1+",
        "msg": (
            f"srcsuite.{verb}.{action} 在 P1+ 阶段实施；"
            "当前 P0 可用：recon.subdomains / .alive / .tech_detect / .crawl / .ports "
            "| srcsuite.health / .task / .workflow.run / .hardgate.check"
        ),
    }


class _ReconNs:
    """侦察命名空间 —— P0 全部接通。"""

    def __init__(self, suite: "SrcSuite"):
        self._s = suite

    def subdomains(self, target: str, *, timeout: int = 120) -> dict:
        """subfinder 子域发现，结果落 assets/subdomains.json。"""
        j = self._s.require_journal()
        hg = _hardgate.check_pre(tool="recon.subdomains", target=target, scope=self._s.scope)
        if hg["status"] == "blocked":
            j.write(phase="recon", kind="hardgate_trigger", tool="subfinder",
                    target=target, output=hg, status="blocked", hardgate=hg["rule_id"])
            return {"success": False, "blocked": True, **hg, "task_id": self._s.task_id}

        j.write(phase="recon", kind="tool_call", tool="subfinder", target=target,
                input={"target": target, "timeout": timeout})

        result = t_subfinder.run(target, timeout=timeout)
        if not result["success"]:
            j.write(phase="recon", kind="error", tool="subfinder", target=target,
                    output={"elapsed_ms": result["elapsed_ms"]}, status="fail", err=result["err"])
            return {"success": False, "error": result["err"], "task_id": self._s.task_id}

        now = _utcnow()
        assets, asset_ids = [], []
        for sub in result["subdomains"]:
            aid = _asset_id("subdomain", sub)
            asset_ids.append(aid)
            assets.append({
                "asset_id": aid, "task_id": self._s.task_id,
                "kind": "subdomain", "value": sub,
                "parent_asset": _asset_id("domain", target),
                "discovered_by": "subfinder", "discovered_at": now,
                "meta": {}, "tags": [],
            })

        out_path = j.task_dir / "assets" / "subdomains.json"
        out_path.write_text(json.dumps(assets, ensure_ascii=False, indent=2), encoding="utf-8")

        j.write(phase="recon", kind="tool_result", tool="subfinder", target=target,
                output={"count": len(assets), "elapsed_ms": result["elapsed_ms"]},
                asset_ids=asset_ids, status="ok",
                refs=[str(out_path.relative_to(j.task_dir))],
                next=["recon.alive(subdomains)", "recon.tech_detect(subdomains)"])

        return {
            "success": True, "task_id": self._s.task_id,
            "count": len(assets), "subdomains": result["subdomains"],
            "assets_path": str(out_path), "elapsed_ms": result["elapsed_ms"],
        }

    def alive(self, subdomains: list[str], *, timeout: int = 120) -> dict:
        """httpx 存活检测 + 技术指纹，结果落 assets/alive_hosts.json。"""
        j = self._s.require_journal()
        if not subdomains:
            return {"success": False, "error": "subdomains 列表为空", "task_id": self._s.task_id}

        hg = _hardgate.check_pre(tool="recon.alive", scope=self._s.scope)
        if hg["status"] == "blocked":
            j.write(phase="recon", kind="hardgate_trigger", tool="httpx",
                    output=hg, status="blocked", hardgate=hg["rule_id"])
            return {"success": False, "blocked": True, **hg, "task_id": self._s.task_id}

        j.write(phase="recon", kind="tool_call", tool="httpx",
                input={"count": len(subdomains), "timeout": timeout})

        result = t_httpx.run(subdomains, timeout=timeout, tech_detect=True)
        if not result["success"]:
            j.write(phase="recon", kind="error", tool="httpx",
                    output={"elapsed_ms": result["elapsed_ms"]}, status="fail", err=result["err"])
            return {"success": False, "error": result["err"], "task_id": self._s.task_id}

        now = _utcnow()
        assets, asset_ids, alive_urls, alive_hosts = [], [], [], []
        for r in result["results"]:
            url = r.get("url") or r.get("host", "")
            if not url:
                continue
            host = r.get("host") or url.split("://")[-1].split("/")[0].split(":")[0]
            aid = _asset_id("alive_host", url)
            asset_ids.append(aid)
            alive_urls.append(url)
            if host and host not in alive_hosts:
                alive_hosts.append(host)
            assets.append({
                "asset_id": aid, "task_id": self._s.task_id,
                "kind": "alive_host", "value": url,
                "discovered_by": "httpx", "discovered_at": now,
                "meta": {
                    "status_code": r.get("status_code"),
                    "title": r.get("title", ""),
                    "tech": r.get("tech", []),
                    "content_length": r.get("content_length"),
                    "scheme": r.get("scheme", ""),
                },
                "tags": [],
            })

        out_path = j.task_dir / "assets" / "alive_hosts.json"
        out_path.write_text(json.dumps(assets, ensure_ascii=False, indent=2), encoding="utf-8")

        j.write(phase="recon", kind="tool_result", tool="httpx",
                output={"count": len(assets), "elapsed_ms": result["elapsed_ms"]},
                asset_ids=asset_ids, status="ok",
                refs=[str(out_path.relative_to(j.task_dir))],
                next=["recon.crawl(alive_urls)", "recon.ports(alive_hosts)"])

        return {
            "success": True, "task_id": self._s.task_id,
            "count": len(assets),
            "alive_urls": alive_urls,
            "alive_hosts": alive_hosts,
            "results": result["results"],
            "assets_path": str(out_path),
            "elapsed_ms": result["elapsed_ms"],
        }

    def tech_detect(self, targets: list[str], *, timeout: int = 120) -> dict:
        """httpx 技术指纹识别（对已存活目标精细识别框架），结果落 assets/tech.json。"""
        j = self._s.require_journal()
        if not targets:
            return {"success": False, "error": "targets 列表为空", "task_id": self._s.task_id}

        j.write(phase="recon", kind="tool_call", tool="httpx-tech",
                input={"count": len(targets), "timeout": timeout})

        result = t_httpx.run(targets, timeout=timeout, tech_detect=True)
        if not result["success"]:
            j.write(phase="recon", kind="error", tool="httpx-tech",
                    output={"elapsed_ms": result["elapsed_ms"]}, status="fail", err=result["err"])
            return {"success": False, "error": result["err"], "task_id": self._s.task_id}

        tech_map = {
            (r.get("url") or r.get("host", "")): r.get("tech", [])
            for r in result["results"]
            if r.get("url") or r.get("host")
        }
        out_path = j.task_dir / "assets" / "tech.json"
        out_path.write_text(json.dumps(tech_map, ensure_ascii=False, indent=2), encoding="utf-8")

        j.write(phase="recon", kind="tool_result", tool="httpx-tech",
                output={"count": len(tech_map), "elapsed_ms": result["elapsed_ms"]},
                status="ok", refs=[str(out_path.relative_to(j.task_dir))],
                next=["scan.nuclei(tech_map) 按框架选 POC"])

        return {
            "success": True, "task_id": self._s.task_id,
            "tech_map": tech_map, "count": len(tech_map),
            "assets_path": str(out_path), "elapsed_ms": result["elapsed_ms"],
        }

    def crawl(self, target: "str | list[str]", *, depth: int = 3, timeout: int = 120) -> dict:
        """katana 爬取 endpoint，结果落 assets/endpoints.json。"""
        j = self._s.require_journal()
        targets: list[str] = ([target] if isinstance(target, str) else list(target))[:10]
        if not targets:
            return {"success": False, "error": "target 为空", "task_id": self._s.task_id}

        all_endpoints: list[str] = []
        total_ms = 0
        for t in targets:
            hg = _hardgate.check_pre(tool="recon.crawl", target=t, scope=self._s.scope)
            if hg["status"] == "blocked":
                j.write(phase="recon", kind="hardgate_trigger", tool="katana",
                        target=t, output=hg, status="blocked", hardgate=hg["rule_id"])
                continue

            j.write(phase="recon", kind="tool_call", tool="katana",
                    target=t, input={"depth": depth, "timeout": timeout})

            r = t_katana.run(t, depth=depth, timeout=timeout)
            total_ms += r["elapsed_ms"]
            if r["success"]:
                all_endpoints.extend(r["endpoints"])
            else:
                j.write(phase="recon", kind="error", tool="katana", target=t,
                        output={"elapsed_ms": r["elapsed_ms"]}, status="fail", err=r["err"])

        all_endpoints = sorted(set(all_endpoints))
        now = _utcnow()
        assets, asset_ids = [], []
        for ep in all_endpoints:
            aid = _asset_id("endpoint", ep)
            asset_ids.append(aid)
            assets.append({
                "asset_id": aid, "task_id": self._s.task_id,
                "kind": "endpoint", "value": ep,
                "discovered_by": "katana", "discovered_at": now,
                "meta": {}, "tags": [],
            })

        out_path = j.task_dir / "assets" / "endpoints.json"
        out_path.write_text(json.dumps(assets, ensure_ascii=False, indent=2), encoding="utf-8")

        j.write(phase="recon", kind="tool_result", tool="katana",
                output={"count": len(assets), "elapsed_ms": total_ms},
                asset_ids=asset_ids, status="ok",
                refs=[str(out_path.relative_to(j.task_dir))],
                next=["scan.nuclei(endpoints)", "js 分析各 endpoint"])

        return {
            "success": True, "task_id": self._s.task_id,
            "count": len(assets), "endpoints": all_endpoints,
            "assets_path": str(out_path), "elapsed_ms": total_ms,
        }

    def ports(self, target: "str | list[str]", *, ports: str = "top-100", timeout: int = 180) -> dict:
        """naabu 端口扫描，结果落 assets/ports.json。"""
        j = self._s.require_journal()
        targets: list[str] = ([target] if isinstance(target, str) else list(target))[:10]
        if not targets:
            return {"success": False, "error": "target 为空", "task_id": self._s.task_id}

        all_ports: list[dict] = []
        total_ms = 0
        for t in targets:
            hg = _hardgate.check_pre(tool="recon.ports", target=t, scope=self._s.scope)
            if hg["status"] == "blocked":
                j.write(phase="recon", kind="hardgate_trigger", tool="naabu",
                        target=t, output=hg, status="blocked", hardgate=hg["rule_id"])
                continue

            j.write(phase="recon", kind="tool_call", tool="naabu",
                    target=t, input={"ports": ports, "timeout": timeout})

            r = t_naabu.run(t, ports=ports, timeout=timeout)
            total_ms += r["elapsed_ms"]
            if r["success"]:
                all_ports.extend(r["open_ports"])
            else:
                j.write(phase="recon", kind="error", tool="naabu", target=t,
                        output={"elapsed_ms": r["elapsed_ms"]}, status="fail", err=r["err"])

        out_path = j.task_dir / "assets" / "ports.json"
        out_path.write_text(json.dumps(all_ports, ensure_ascii=False, indent=2), encoding="utf-8")

        j.write(phase="recon", kind="tool_result", tool="naabu",
                output={"count": len(all_ports), "elapsed_ms": total_ms},
                status="ok", refs=[str(out_path.relative_to(j.task_dir))],
                next=["对开放端口跑 nuclei", "高危端口专项检测"])

        return {
            "success": True, "task_id": self._s.task_id,
            "count": len(all_ports), "open_ports": all_ports,
            "assets_path": str(out_path), "elapsed_ms": total_ms,
        }


class _StubNs:
    """通用未实现命名空间，任意属性访问都返回占位。"""

    def __init__(self, verb: str):
        self._verb = verb

    def __getattr__(self, action: str):
        def _stubbed(*_a, **_kw) -> dict:
            return _stub(self._verb, action)
        return _stubbed


class _ScanNs:
    """扫描命名空间 —— P1 接通 nuclei。"""

    def __init__(self, suite: "SrcSuite"):
        self._s = suite

    def nuclei(
        self,
        targets: "list[str] | str",
        *,
        templates: list[str] | None = None,
        severity: str = "medium,high,critical",
        timeout: int = 300,
        rate_limit: int = 50,
    ) -> dict:
        """nuclei POC 扫描，结果落 assets/findings_nuclei.json。"""
        j = self._s.require_journal()
        target_list = [targets] if isinstance(targets, str) else list(targets)
        if not target_list:
            return {"success": False, "error": "targets 为空", "task_id": self._s.task_id}

        for t in target_list[:3]:
            hg = _hardgate.check_pre(tool="scan.nuclei", target=t, scope=self._s.scope)
            if hg["status"] == "blocked":
                j.write(phase="scan", kind="hardgate_trigger", tool="nuclei",
                        target=t, output=hg, status="blocked", hardgate=hg["rule_id"])
                return {"success": False, "blocked": True, **hg, "task_id": self._s.task_id}

        j.write(phase="scan", kind="tool_call", tool="nuclei",
                input={"count": len(target_list), "severity": severity, "timeout": timeout})

        result = t_nuclei.run(
            target_list, templates=templates,
            severity=severity, timeout=timeout, rate_limit=rate_limit,
        )
        if not result["success"]:
            j.write(phase="scan", kind="error", tool="nuclei",
                    output={"elapsed_ms": result["elapsed_ms"]}, status="fail", err=result["err"])
            return {"success": False, "error": result["err"], "task_id": self._s.task_id}

        now = _utcnow()
        findings = result["findings"]
        finding_ids = [_asset_id("finding", f["matched_at"] + f["template_id"]) for f in findings]

        out_path = j.task_dir / "assets" / "findings_nuclei.json"
        out_path.write_text(
            __import__("json").dumps(
                [{"finding_id": fid, "task_id": self._s.task_id, "source": "nuclei",
                  "discovered_at": now, **f}
                 for fid, f in zip(finding_ids, findings)],
                ensure_ascii=False, indent=2,
            ),
            encoding="utf-8",
        )

        j.write(phase="scan", kind="tool_result", tool="nuclei",
                output={"count": len(findings), "elapsed_ms": result["elapsed_ms"]},
                status="ok", refs=[str(out_path.relative_to(j.task_dir))],
                next=["对每个 finding 核实复现", "高危发现问老白是否提交"])

        return {
            "success": True, "task_id": self._s.task_id,
            "count": len(findings), "findings": findings,
            "assets_path": str(out_path), "elapsed_ms": result["elapsed_ms"],
        }

    def __getattr__(self, action: str):
        def _stubbed(*_a, **_kw) -> dict:
            return _stub("scan", action)
        return _stubbed


class _JsNs:
    """JS 分析命名空间 —— P1 纯 Python 实现，无需外部工具。"""

    def __init__(self, suite: "SrcSuite"):
        self._s = suite

    def analyze(self, urls: "list[str] | str", *, timeout: int = 15) -> dict:
        """下载并分析 JS 文件，提取 endpoint + 扫密钥，结果落 assets/js_analysis.json。"""
        j = self._s.require_journal()
        url_list = [urls] if isinstance(urls, str) else list(urls)
        if not url_list:
            return {"success": False, "error": "urls 为空", "task_id": self._s.task_id}

        j.write(phase="recon", kind="tool_call", tool="jsanalyze",
                input={"count": len(url_list)})

        all_endpoints: list[str] = []
        all_secrets: list[dict] = []
        results = []
        for url in url_list:
            r = t_js.analyze_url(url, timeout=timeout)
            results.append(r)
            if r["success"]:
                all_endpoints.extend(r["endpoints"])
                all_secrets.extend(r["secrets"])

        all_endpoints = sorted(set(all_endpoints))
        out = {
            "task_id": self._s.task_id,
            "js_files": results,
            "endpoints_total": all_endpoints,
            "secrets_total": all_secrets,
        }
        out_path = j.task_dir / "assets" / "js_analysis.json"
        out_path.write_text(
            __import__("json").dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        j.write(phase="recon", kind="tool_result", tool="jsanalyze",
                output={"js_files": len(results), "endpoints": len(all_endpoints),
                        "secrets": len(all_secrets)},
                status="ok", refs=[str(out_path.relative_to(j.task_dir))],
                next=["对发现的 endpoint 跑 scan.nuclei", "人工核查 secrets"])

        return {
            "success": True, "task_id": self._s.task_id,
            "js_count": len(results),
            "endpoint_count": len(all_endpoints),
            "secret_count": len(all_secrets),
            "endpoints": all_endpoints,
            "secrets": all_secrets,
            "assets_path": str(out_path),
        }

    def endpoints(self, content: str) -> dict:
        """直接分析 JS 文本内容，提取 endpoint（不需要下载）。"""
        eps = t_js.endpoint_extract(content)
        return {"success": True, "endpoints": eps, "count": len(eps)}

    def secrets(self, content: str) -> dict:
        """直接扫描 JS 文本内容里的密钥泄露。"""
        hits = t_js.secret_scan(content)
        return {"success": True, "secrets": hits, "count": len(hits)}

    def __getattr__(self, action: str):
        def _stubbed(*_a, **_kw) -> dict:
            return _stub("js", action)
        return _stubbed



class _WorkflowNs:
    """workflow 命名空间 —— 执行预定义 DAG。"""

    def __init__(self, suite: "SrcSuite"):
        self._s = suite

    def run(self, flow_name: str, *, target: str, **params: Any) -> dict:
        """执行预定义 workflow。"""
        return _workflow.run_flow(self._s, flow_name, target=target, **params)

    def list(self) -> dict:
        """列出可用 workflow 名称。"""
        return {"success": True, "flows": _workflow.list_flows()}


class _HardgateNs:
    """硬门命名空间 —— AI 可直接查询规则或重载。"""

    def check(self, *, tool: str | None = None, target: str | None = None,
              method: str | None = None, path: str | None = None,
              args: list[str] | None = None, scope: list[str] | None = None) -> dict:
        return _hardgate.check_pre(
            tool=tool, target=target, method=method, path=path, args=args, scope=scope
        )

    def reload(self) -> dict:
        _hardgate._reload()
        return {"success": True, "msg": "hardgate 规则已重新加载"}

    def rules(self) -> dict:
        return {"success": True, "count": len(_hardgate._rules()), "rules": _hardgate._rules()}


class _TaskNs:
    """任务管理命名空间：新建 / 接管 / 查尾巴。"""

    def __init__(self, suite: "SrcSuite"):
        self._s = suite

    def new(
        self, *,
        target: str | None = None,
        note: str | None = None,
        platform: str = "local",
        scope: list[str] | None = None,
    ) -> dict:
        """新建任务，写 init 事件，携带平台标识和 scope。

        platform: "local" | "vulbox" | "butian" | "tsrc" | "asrc" | "h1"
        scope: ["*.example.com", "example.com"] 或 None（local 自动设 ["*"]）
        """
        tid = new_task_id()
        self._s.attach(tid)
        effective_scope = scope if scope is not None else (["*"] if platform == "local" else [])
        self._s.scope = effective_scope

        j = self._s.require_journal()
        j.write(
            phase="init", kind="decision", target=target,
            decision="任务启动",
            input={"note": note, "platform": platform, "scope": effective_scope},
        )
        return {
            "success": True, "task_id": tid, "task_dir": str(j.task_dir),
            "platform": platform, "scope": effective_scope,
        }

    def attach(self, task_id: str) -> dict:
        """接管现有任务，返回最近一条事件供 AI 续作。"""
        self._s.attach(task_id)
        j = self._s.require_journal()
        last = j.tail(1)
        return {
            "success": True, "task_id": task_id,
            "task_dir": str(j.task_dir),
            "last_event": last[0] if last else None,
        }

    def tail(self, n: int = 20) -> dict:
        """查最近 n 条 journal 事件。"""
        j = self._s.require_journal()
        return {"success": True, "task_id": j.task_id, "events": j.tail(n)}


class SrcSuite:
    """AI-first 门面对象。有状态：持有当前 task_id + scope，所有动词操作它。"""

    def __init__(self, task_id: str | None = None, scope: list[str] | None = None):
        self.task_id: str | None = task_id
        self._journal: Journal | None = Journal(task_id) if task_id else None
        self.scope: list[str] = scope if scope is not None else ["*"]

        self.recon = _ReconNs(self)
        self.browse = _BrowseNs(self)
        self.scan = _ScanNs(self)
        self.js = _JsNs(self)
        self.exploit = _StubNs("exploit")
        self.mobile = _StubNs("mobile")
        self.platform = _PlatformNs(self)
        self.report = _StubNs("report")
        self.evidence = _StubNs("evidence")
        self.ledger = _StubNs("ledger")
        self.task = _TaskNs(self)
        self.workflow = _WorkflowNs(self)
        self.hardgate = _HardgateNs()

    def attach(self, task_id: str) -> None:
        self.task_id = task_id
        self._journal = Journal(task_id)

    def require_journal(self) -> Journal:
        if self._journal is None:
            raise RuntimeError("还没接管任务，请先调 srcsuite.task.new() 或 .attach(task_id)")
        return self._journal

    def health(self, *, write_report: bool = False) -> dict:
        """探测 SRC 作业链真实可用状态，不启动浏览器或模拟器。"""
        return _health.run_health(
            current_task=self.task_id,
            scope=self.scope,
            workflows=_workflow.list_flows(),
            hardgate_rules=len(_hardgate._rules()),
            write_report=write_report,
        )

    def status(self, *, write_report: bool = True) -> dict:
        """给 Hermes 前台使用的 SRC 总状态，避免凭旧记忆判断工具能否调用。"""
        from . import status as _status

        return _status.run_status(write_report=write_report)


class _PlatformNs:
    """平台只读 smoke：验证 Hermes 能读平台页面和登录态信号。"""

    def __init__(self, suite: SrcSuite):
        self._s = suite

    def smoke(
        self,
        platforms: list[str] | None = None,
        *,
        cdp_url: str | None = None,
        write_report: bool = False,
    ) -> dict:
        from . import platform_smoke as _platform_smoke

        result = _platform_smoke.run_smoke(platforms=platforms, cdp_url=cdp_url, write_report=write_report)
        if self._s._journal is not None:
            self._s.require_journal().write(
                phase="platform",
                kind="tool_result",
                tool="platform.smoke",
                input={"platforms": platforms or ["vulbox", "butian"], "cdp_url": cdp_url},
                output={
                    "status": result["status"],
                    "platforms": {
                        name: item.get("assessment", {})
                        for name, item in result.get("platforms", {}).items()
                    },
                },
                status="ok" if result["status"] == "ready" else "degraded",
                refs=list((result.get("report_files") or {}).values()),
            )
        return result


class _BrowseNs:
    """浏览器只读结构化能力。"""

    def __init__(self, suite: SrcSuite):
        self._s = suite

    def map(
        self,
        url: str | None = None,
        *,
        cdp_url: str | None = None,
        write_report: bool = False,
    ) -> dict:
        from . import interaction_map as _interaction_map

        result = _interaction_map.run_interaction_map(url=url, cdp_url=cdp_url, write_report=write_report)
        if self._s._journal is not None:
            self._s.require_journal().write(
                phase="browse",
                kind="tool_result",
                tool="browse.map",
                input={"url": url, "cdp_url": cdp_url},
                output={
                    "success": result["success"],
                    "page": result.get("page"),
                    "counts": (result.get("interaction_map") or {}).get("counts"),
                },
                status="ok" if result["success"] else "fail",
                refs=list((result.get("report_files") or {}).values()),
            )
        return result
