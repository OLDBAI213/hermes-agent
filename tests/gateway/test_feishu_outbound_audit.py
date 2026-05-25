"""Tests for Feishu outbound audit logging."""

from __future__ import annotations

import json

from tests.gateway.feishu_helpers import make_adapter_skeleton


def test_feishu_outbound_audit_writes_ndjson(monkeypatch, tmp_path):
    adapter = make_adapter_skeleton()
    adapter._outbound_audit = True
    adapter._outbound_audit_full_payload = True
    monkeypatch.setenv("HERMES_HOME", str(tmp_path))

    payload = json.dumps(
        {
            "zh_cn": {
                "title": "工具调用记录",
                "content": [[{"tag": "text", "text": "1. 正在检查"}]],
            }
        },
        ensure_ascii=False,
    )
    adapter._audit_outbound_message(
        stage="edit.build",
        chat_id="oc_test",
        message_id="om_test",
        msg_type="post",
        payload=payload,
        metadata={"thread_id": "omt_test", "ignored": "value"},
    )

    audit_path = tmp_path / "logs" / "feishu-outbound.ndjson"
    rows = audit_path.read_text(encoding="utf-8").splitlines()
    assert len(rows) == 1

    row = json.loads(rows[0])
    assert row["stage"] == "edit.build"
    assert row["chat_id"] == "oc_test"
    assert row["message_id"] == "om_test"
    assert row["msg_type"] == "post"
    assert "工具调用记录" in row["payload_preview"]
    assert row["payload"] == payload
    assert row["metadata_keys"] == ["ignored", "thread_id"]


def test_feishu_outbound_audit_noops_when_disabled(monkeypatch, tmp_path):
    adapter = make_adapter_skeleton()
    adapter._outbound_audit = False
    adapter._outbound_audit_full_payload = False
    monkeypatch.setenv("HERMES_HOME", str(tmp_path))

    adapter._audit_outbound_message(
        stage="send.build",
        chat_id="oc_test",
        msg_type="text",
        payload=json.dumps({"text": "hello"}, ensure_ascii=False),
    )

    assert not (tmp_path / "logs" / "feishu-outbound.ndjson").exists()
