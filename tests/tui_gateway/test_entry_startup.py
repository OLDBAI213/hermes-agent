import io


def test_entry_emits_ready_before_scheduling_mcp(monkeypatch):
    from tui_gateway import entry

    events = []

    monkeypatch.setattr(entry, "resolve_skin", lambda: {"name": "test"})
    monkeypatch.setattr(entry, "_should_discover_mcp_tools", lambda: True)
    monkeypatch.setattr(entry, "_start_mcp_discovery_background", lambda: events.append("mcp"))
    monkeypatch.setattr(entry, "_log_exit", lambda reason: events.append(("exit", reason)))
    monkeypatch.setattr(entry.sys, "stdin", io.StringIO(""))

    def capture_write(payload):
        if payload.get("method") == "event":
            events.append(payload["params"]["type"])
        else:
            events.append(payload)
        return True

    monkeypatch.setattr(entry, "write_json", capture_write)

    entry.main()

    assert events[:2] == ["gateway.ready", "mcp"]


def test_entry_skips_mcp_scheduler_without_configured_servers(monkeypatch):
    from tui_gateway import entry

    events = []

    monkeypatch.setattr(entry, "resolve_skin", lambda: {"name": "test"})
    monkeypatch.setattr(entry, "_should_discover_mcp_tools", lambda: False)
    monkeypatch.setattr(
        entry,
        "_start_mcp_discovery_background",
        lambda: (_ for _ in ()).throw(AssertionError("MCP scheduler should be skipped")),
    )
    monkeypatch.setattr(entry, "_log_exit", lambda reason: events.append(("exit", reason)))
    monkeypatch.setattr(entry.sys, "stdin", io.StringIO(""))
    monkeypatch.setattr(
        entry,
        "write_json",
        lambda payload: events.append(payload["params"]["type"]) or True,
    )

    entry.main()

    assert events == [
        "gateway.ready",
        ("exit", "stdin EOF (TUI closed the command pipe)"),
    ]
