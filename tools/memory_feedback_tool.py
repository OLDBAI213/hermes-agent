#!/usr/bin/env python3
"""
Memory Feedback Tool - 记忆反馈工具

让用户可以反馈记忆的有效性，让记忆越用越准。

使用方式：
- 用户说"这个记忆没用" → 调用 on_ineffective
- 用户使用了某个记忆 → 自动调用 on_access
- 搜索时按有效性排名
"""

import json
from typing import Optional
from tools.registry import registry
from tools.memory_effectiveness import get_tracker


def memory_feedback(
    action: str,
    target: str = "memory",
    content: str = None,
    memory_key: str = None,
) -> str:
    """
    记忆反馈工具
    
    Args:
        action: 操作类型
            - "access": 记忆被访问（自动调用）
            - "ineffective": 记忆没用（用户反馈）
            - "score": 查看记忆评分
            - "stats": 查看统计信息
        target: memory 或 user
        content: 记忆内容（用于 access 和 ineffective）
        memory_key: 记忆标识（用于 score）
    
    Returns:
        JSON 格式的操作结果
    """
    tracker = get_tracker()
    
    if action == "access":
        if not content:
            return json.dumps({
                "success": False,
                "error": "Content is required for 'access' action."
            })
        
        tracker.on_access(target, content)
        score = tracker.get_score(content)
        
        return json.dumps({
            "success": True,
            "action": "access",
            "message": f"记忆访问已记录，当前有效性: {score:.2f}",
            "effectiveness": score
        })
    
    elif action == "ineffective":
        if not content:
            return json.dumps({
                "success": False,
                "error": "Content is required for 'ineffective' action."
            })
        
        tracker.on_ineffective(target, content)
        score = tracker.get_score(content)
        
        return json.dumps({
            "success": True,
            "action": "ineffective",
            "message": f"已标记为无效，当前有效性: {score:.2f}",
            "effectiveness": score
        })
    
    elif action == "score":
        if not content and not memory_key:
            return json.dumps({
                "success": False,
                "error": "Content or memory_key is required for 'score' action."
            })
        
        content_to_check = content or memory_key
        score = tracker.get_score(content_to_check)
        
        return json.dumps({
            "success": True,
            "action": "score",
            "effectiveness": score,
            "message": f"有效性评分: {score:.2f}"
        })
    
    elif action == "stats":
        stats = tracker.get_stats()
        
        return json.dumps({
            "success": True,
            "action": "stats",
            "stats": stats
        })
    
    else:
        return json.dumps({
            "success": False,
            "error": f"Invalid action '{action}'. Use 'access', 'ineffective', 'score', or 'stats'."
        })


# 注册工具
registry.register(
    name="memory_feedback",
    toolset="memory",
    schema={
        "name": "memory_feedback",
        "description": "记忆反馈工具 - 让用户可以反馈记忆的有效性，让记忆越用越准。",
        "parameters": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["access", "ineffective", "score", "stats"],
                    "description": "操作类型"
                },
                "target": {
                    "type": "string",
                    "enum": ["memory", "user"],
                    "default": "memory",
                    "description": "memory 或 user"
                },
                "content": {
                    "type": "string",
                    "description": "记忆内容（用于 access 和 ineffective）"
                },
                "memory_key": {
                    "type": "string",
                    "description": "记忆标识（用于 score）"
                }
            },
            "required": ["action"]
        }
    },
    handler=lambda args, **kw: memory_feedback(
        action=args.get("action", ""),
        target=args.get("target", "memory"),
        content=args.get("content"),
        memory_key=args.get("memory_key")
    ),
)
