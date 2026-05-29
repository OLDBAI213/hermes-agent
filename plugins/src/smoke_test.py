"""P-1 冒烟测试 —— 验证 门面→工具→日志→schema 整条链路通不通。

用法：
    cd E:/AI/hermes/hermes-agent
    python -m plugins.src.smoke_test [目标域名]

默认目标：example.com（IANA 名下的安全测试域，有几个公开子域）。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# 允许 `python smoke_test.py` 直跑（同时不影响 `python -m plugins.src.smoke_test`）
_HERE = Path(__file__).resolve().parent
if str(_HERE.parent.parent) not in sys.path:
    sys.path.insert(0, str(_HERE.parent.parent))

from plugins.src.facade import SrcSuite  # noqa: E402


def main(argv: list[str]) -> int:
    target = argv[1] if len(argv) > 1 else "example.com"

    print(f"[冒烟] 目标 = {target}")
    suite = SrcSuite()

    print("[冒烟] 步骤 1：健康检查 ...")
    h = suite.health()
    print(json.dumps(h, indent=2, ensure_ascii=False))
    if not h["tools"]["subfinder"]["available"]:
        print("[冒烟] 失败：subfinder 找不到")
        return 2

    print("\n[冒烟] 步骤 2：新建任务 ...")
    t = suite.task.new(target=target, note="P-1 冒烟测试")
    print(json.dumps(t, indent=2, ensure_ascii=False))

    print(f"\n[冒烟] 步骤 3：跑子域发现 recon.subdomains({target}) ...")
    r = suite.recon.subdomains(target, timeout=60)
    print(json.dumps({k: v for k, v in r.items() if k != "subdomains"}, indent=2, ensure_ascii=False))
    if r.get("subdomains"):
        preview = r["subdomains"][:5]
        print(f"[冒烟] 前 {len(preview)} 个子域：{preview}")

    print("\n[冒烟] 步骤 4：看最近 5 条 journal 事件 ...")
    tail = suite.task.tail(5)
    for ev in tail["events"]:
        print(json.dumps(ev, ensure_ascii=False))

    if not r.get("success"):
        print(f"\n[冒烟] 失败：recon.subdomains 出错：{r.get('error')}")
        return 3

    print(f"\n[冒烟] 通过：任务编号={suite.task_id}，资产数={r['count']}，耗时={r['elapsed_ms']} 毫秒")
    print(f"[冒烟] 日志文件：{suite.require_journal().path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
