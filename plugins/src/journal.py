"""SRC Suite 工作日志 —— JSONL 读写。

AI-first：一行一事件，AI 用 grep/jq 直接查文件。
断点续作：seq 单任务单调递增，新 session 读最后一条即可续作。
人类报告按需 render，不作为默认产物。
"""
from __future__ import annotations

import json
import os
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def runs_root() -> Path:
    """返回 runs/src 根目录，可通过环境变量 HERMES_HOME 覆盖。"""
    env = os.environ.get("HERMES_HOME")
    base = Path(env) if env else Path("E:/AI/hermes")
    return base / "runs" / "src"


class Journal:
    """单任务一份 journal，追加写 JSONL。"""

    def __init__(self, task_id: str):
        self.task_id = task_id
        self.task_dir = runs_root() / task_id
        self.task_dir.mkdir(parents=True, exist_ok=True)
        (self.task_dir / "assets").mkdir(exist_ok=True)
        (self.task_dir / "evidence").mkdir(exist_ok=True)
        self.path = self.task_dir / "journal.jsonl"
        self._lock = threading.Lock()
        self._seq = self._load_last_seq()

    def _load_last_seq(self) -> int:
        """读现有 journal 找出最大 seq，断点续作时不冲号。"""
        if not self.path.exists():
            return 0
        last = 0
        with self.path.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    ev = json.loads(line)
                    if isinstance(ev.get("seq"), int) and ev["seq"] > last:
                        last = ev["seq"]
                except json.JSONDecodeError:
                    continue
        return last

    def write(
        self,
        *,
        phase: str,
        kind: str,
        tool: str | None = None,
        target: str | None = None,
        input: dict | None = None,
        output: dict | None = None,
        asset_ids: list[str] | None = None,
        finding_id: str | None = None,
        decision: str | None = None,
        next: list[str] | None = None,
        hardgate: str | None = None,
        status: str | None = None,
        refs: list[str] | None = None,
        err: str | None = None,
    ) -> dict[str, Any]:
        """写一条事件。字段说明见 schemas/journal_event.json。"""
        with self._lock:
            self._seq += 1
            ev = {
                "ts": _utcnow(),
                "task_id": self.task_id,
                "seq": self._seq,
                "phase": phase,
                "kind": kind,
                "tool": tool,
                "target": target,
                "input": input,
                "output": output,
                "asset_ids": asset_ids or [],
                "finding_id": finding_id,
                "decision": decision,
                "next": next or [],
                "hardgate": hardgate,
                "status": status,
                "refs": refs or [],
                "err": err,
            }
            with self.path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(ev, ensure_ascii=False) + "\n")
            return ev

    def tail(self, n: int = 20) -> list[dict]:
        """读最后 n 条事件，AI 续作时打开局面用。"""
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as f:
            lines = f.readlines()
        events: list[dict] = []
        for line in lines[-n:]:
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
        return events

    def last_state(self) -> dict | None:
        """返回最后一条 kind=resume_state 事件，AI 续作时从这里捡起完整快照。"""
        if not self.path.exists():
            return None
        last_state: dict | None = None
        with self.path.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    ev = json.loads(line)
                    if ev.get("kind") == "resume_state":
                        last_state = ev
                except json.JSONDecodeError:
                    continue
        return last_state


def new_task_id(prefix: str = "src") -> str:
    """生成新任务编号，格式 src_YYYYMMDD_HHMMSS。"""
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{stamp}"
