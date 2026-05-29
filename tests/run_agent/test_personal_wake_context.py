from agent.conversation_loop import (
    _build_current_turn_context_injections,
    _build_personal_wake_context_block,
    _capture_personal_signal_candidates,
    _classify_personal_signal_candidates,
    _load_personal_wake_context,
    _load_personal_working_memory_context,
    _select_personal_scene_cards,
)


def test_personal_wake_loads_generated_file(tmp_path, monkeypatch):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path))
    wake_path = tmp_path / "memory-personal" / "generated" / "wake.md"
    wake_path.parent.mkdir(parents=True)
    wake_path.write_text("# Xiaobai Personal Wake\n\n- work first\n", encoding="utf-8")

    result = _load_personal_wake_context()

    assert "# Xiaobai Personal Wake" in result
    assert "- work first" in result


def test_personal_wake_skips_forbidden_framing(tmp_path, monkeypatch):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path))
    wake_path = tmp_path / "memory-personal" / "generated" / "wake.md"
    wake_path.parent.mkdir(parents=True)
    wake_path.write_text("# Xiaobai Personal Wake\n\n- safehouse\n", encoding="utf-8")

    assert _load_personal_wake_context() == ""


def test_personal_wake_context_block_is_fenced():
    block = _build_personal_wake_context_block("# Xiaobai Personal Wake\n\n- concise")

    assert block.startswith("<memory-context>")
    assert block.endswith("</memory-context>")
    assert "NOT new user input" in block
    assert "# Xiaobai Personal Wake" in block


def test_current_turn_context_injections_preserve_order():
    injections = _build_current_turn_context_injections(
        "# Xiaobai Personal Wake\n\n- concise",
        "remembered fact",
        "plugin context",
    )

    assert len(injections) == 3
    assert "Xiaobai personal working memory" in injections[0]
    assert "# Xiaobai Personal Wake" in injections[0]
    assert "recalled memory context" in injections[1]
    assert "remembered fact" in injections[1]
    assert injections[2] == "plugin context"


def test_select_personal_scene_cards_routes_research_before_work():
    cards = _select_personal_scene_cards("去 GitHub 上继续研究学习，别变成工具清单")

    assert cards[0] == "research"
    assert "work" not in cards


def test_select_personal_scene_cards_routes_audit_without_work():
    cards = _select_personal_scene_cards(
        "这样真的可以么，你仔细研究一下，你把自己当做用户或者 Hermes，你觉得换个角度有什么问题"
    )

    assert cards[0] == "audit"
    assert "research" in cards
    assert "work" not in cards


def test_select_personal_scene_cards_keeps_decision_question_out_of_human():
    cards = _select_personal_scene_cards("这个决策对不对")

    assert cards == ["decision"]


def test_select_personal_scene_cards_keeps_error_fix_out_of_human():
    cards = _select_personal_scene_cards("报错了，修一下")

    assert "failure" in cards
    assert "work" in cards
    assert "human" not in cards


def test_select_personal_scene_cards_routes_human_correction():
    cards = _select_personal_scene_cards("还是没明白，以后别这样")

    assert "human" in cards
    assert "correction" in cards


def test_personal_working_memory_loads_selected_scene_card(tmp_path, monkeypatch):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path))
    wake_path = tmp_path / "memory-personal" / "generated" / "wake.md"
    cards_dir = tmp_path / "memory-personal" / "generated" / "cards"
    cards_dir.mkdir(parents=True)
    wake_path.write_text("# 小白记忆入口\n\n- 场景卡\n", encoding="utf-8")
    (cards_dir / "research.md").write_text("# 研究架构卡\n\n- 我们的需求\n", encoding="utf-8")
    (cards_dir / "work.md").write_text("# 工作执行卡\n\n- 真实状态\n", encoding="utf-8")

    context = _load_personal_working_memory_context("去 GitHub 上继续研究学习")

    assert "# 小白记忆入口" in context
    assert "Selected scene card: research" in context
    assert "# 研究架构卡" in context
    assert "# 工作执行卡" not in context


def test_current_turn_context_injection_can_include_scene_card(tmp_path, monkeypatch):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path))
    wake_path = tmp_path / "memory-personal" / "generated" / "wake.md"
    cards_dir = tmp_path / "memory-personal" / "generated" / "cards"
    cards_dir.mkdir(parents=True)
    wake_path.write_text("# 小白记忆入口\n\n- 场景卡\n", encoding="utf-8")
    (cards_dir / "decision.md").write_text("# 决策辅助卡\n\n- 事实、假设、推断\n", encoding="utf-8")

    memory_context = _load_personal_working_memory_context("这个决策对不对")
    injections = _build_current_turn_context_injections(memory_context, "", "")

    assert len(injections) == 1
    assert injections[0].startswith("<memory-context>")
    assert "Selected scene card: decision" in injections[0]
    assert "事实、假设、推断" in injections[0]


def test_personal_signal_detector_ignores_short_continuation():
    assert _classify_personal_signal_candidates("然后呢") == []
    assert _classify_personal_signal_candidates("再检查检查，还有什么问题和可以提升的。") == []


def test_personal_signal_detector_classifies_core_candidate_types():
    messages = {
        "以后别这样，每次都要先查真实状态": "correction",
        "你这不对。": "correction",
        "还是没明白。": "correction",
        "这个项目总感觉有些问题，你去看看。": "failure_signal",
        "报错了，修一下": "failure_signal",
        "我希望小白短中文但有证据": "user_preference",
        "这个决策结果验证一下": "decision_memory",
        "项目入口在 E:\\AI\\hermes": "project_fact",
    }

    for message, expected_type in messages.items():
        types = {item["type"] for item in _classify_personal_signal_candidates(message)}
        assert expected_type in types


def test_personal_signal_detector_writes_candidates_once(tmp_path, monkeypatch):
    monkeypatch.setenv("HERMES_HOME", str(tmp_path))
    inbox_path = tmp_path / "memory-personal" / "candidates" / "inbox.jsonl"
    inbox_path.parent.mkdir(parents=True)
    inbox_path.write_text("", encoding="utf-8")

    first = _capture_personal_signal_candidates("以后别这样，报错了就先说失败。")
    second = _capture_personal_signal_candidates("以后别这样，报错了就先说失败。")

    assert {item["type"] for item in first} == {"correction", "failure_signal"}
    assert second == []
    lines = [line for line in inbox_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(lines) == 2
    assert all('"status":"candidate"' in line for line in lines)
