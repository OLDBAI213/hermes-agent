#!/usr/bin/env python3
"""
Memory Effectiveness System Test - 记忆有效性系统测试

测试有效性评分系统是否正常工作。
"""

import tempfile
import os
import json

# 设置临时 HERMES_HOME
with tempfile.TemporaryDirectory() as tmpdir:
    os.environ['HERMES_HOME'] = tmpdir
    
    # 导入模块
    from tools.memory_effectiveness import EffectivenessTracker
    from tools.memory_feedback_tool import memory_feedback
    
    print("=" * 60)
    print("Memory Effectiveness System Test")
    print("=" * 60)
    
    # 1. 测试 EffectivenessTracker
    print("\n1. Testing EffectivenessTracker...")
    tracker = EffectivenessTracker()
    
    # 添加一些记忆
    memories = [
        "老白的电脑配置是 AMD Ryzen 5 5600 + RTX 3070 Ti",
        "Hermes Agent 使用飞书作为主要沟通渠道",
        "GitHub 用户名是 OLDBAI213",
        "补天平台账号是 OLDBAI",
    ]
    
    for mem in memories:
        tracker.on_access("memory", mem)
        print(f"  Added: {mem[:40]}...")
    
    # 测试访问
    print("\n2. Testing access tracking...")
    tracker.on_access("memory", memories[0])
    tracker.on_access("memory", memories[0])
    print(f"  Score for '{memories[0][:30]}...': {tracker.get_score(memories[0]):.2f}")
    
    # 测试无效标记
    print("\n3. Testing ineffective marking...")
    tracker.on_ineffective("memory", memories[1])
    print(f"  Score for '{memories[1][:30]}...': {tracker.get_score(memories[1]):.2f}")
    
    # 测试排名
    print("\n4. Testing ranking...")
    ranked = tracker.get_ranked_memories("memory", memories, "电脑配置")
    print("  Ranked by relevance to '电脑配置':")
    for i, mem in enumerate(ranked, 1):
        score = tracker.get_score(mem)
        print(f"    {i}. {mem[:40]}... (score: {score:.2f})")
    
    # 测试统计
    print("\n5. Testing stats...")
    stats = tracker.get_stats()
    print(f"  Stats: {json.dumps(stats, indent=2)}")
    
    # 2. 测试 memory_feedback 工具
    print("\n6. Testing memory_feedback tool...")
    
    # 测试 stats
    result = memory_feedback(action="stats")
    print(f"  Stats: {result}")
    
    # 测试 score
    result = memory_feedback(action="score", content=memories[0])
    print(f"  Score: {result}")
    
    # 测试 ineffective
    result = memory_feedback(action="ineffective", target="memory", content=memories[2])
    print(f"  Ineffective: {result}")
    
    print("\n" + "=" * 60)
    print("All tests passed!")
    print("=" * 60)
