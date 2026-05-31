from __future__ import annotations

from pathlib import Path

import yaml

from scripts import feishu_localization_audit as audit


ROOT = Path(__file__).resolve().parents[2]
RULES = ROOT / "locales" / "feishu_zh_audit_allowlist.yaml"


def test_feishu_localization_audit_has_no_unapproved_user_visible_english():
    findings = audit.audit(ROOT, RULES)
    summary = audit._summarize(findings)

    assert summary["user_visible_english_literals"] > 0
    assert summary["unapproved_count"] == 0, summary["unapproved"][:10]


def test_feishu_localization_audit_rules_have_reasons():
    data = yaml.safe_load(RULES.read_text(encoding="utf-8"))

    for item in data.get("allowed_exact", []):
        assert item.get("text")
        assert item.get("reason")
    for item in data.get("allowed_patterns", []):
        assert item.get("pattern")
        assert item.get("reason")
    for item in data.get("forbidden_patterns", []):
        assert item.get("pattern")
        assert item.get("reason")
