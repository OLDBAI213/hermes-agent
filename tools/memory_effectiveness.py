#!/usr/bin/env python3
"""
Memory Effectiveness Tracker - 记忆有效性追踪

为 memory 工具添加有效性评分，让记忆越用越准。

设计思路（借鉴 Overmind）：
1. 每条记忆有有效性评分（0-1）
2. 被访问时 +0.1，被证明无效时 -0.2
3. 搜索时按有效性排名
4. 用户可以说"这个记忆没用"来降权

实现方式：
- 元数据存储在单独的 JSON 文件
- memory 工具调用时更新元数据
- 搜索时使用元数据进行排名
"""

import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict, field

from hermes_constants import get_hermes_home

logger = logging.getLogger(__name__)


@dataclass
class MemoryMetadata:
    """单条记忆的元数据"""
    key: str                    # 记忆标识（内容的哈希或摘要）
    content_preview: str        # 内容预览（前100字符）
    access_count: int = 0       # 访问次数
    last_accessed: str = None   # 最后访问时间
    effectiveness: float = 0.5  # 有效性评分 0-1
    ineffective_count: int = 0  # 无效次数
    created_at: str = None      # 创建时间
    target: str = "memory"      # memory 或 user


class EffectivenessTracker:
    """
    记忆有效性追踪器
    
    使用方式：
        tracker = EffectivenessTracker()
        tracker.on_access("memory", "老白的电脑配置...")
        tracker.on_ineffective("memory", "老白的电脑配置...")
        tracker.get_ranked_memories("memory", "电脑配置")
    """
    
    def __init__(self):
        self.metadata_dir = get_hermes_home() / "memories"
        self.metadata_file = self.metadata_dir / "effectiveness.json"
        self.metadata: Dict[str, MemoryMetadata] = {}
        self._load()
    
    def _load(self):
        """从磁盘加载元数据"""
        if not self.metadata_file.exists():
            return
        
        try:
            with open(self.metadata_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            for key, meta in data.items():
                self.metadata[key] = MemoryMetadata(**meta)
            
            logger.debug(f"Loaded {len(self.metadata)} memory metadata entries")
        except Exception as e:
            logger.warning(f"Failed to load effectiveness metadata: {e}")
    
    def _save(self):
        """保存元数据到磁盘"""
        self.metadata_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            data = {key: asdict(meta) for key, meta in self.metadata.items()}
            
            with open(self.metadata_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            logger.debug(f"Saved {len(self.metadata)} memory metadata entries")
        except Exception as e:
            logger.warning(f"Failed to save effectiveness metadata: {e}")
    
    def _make_key(self, content: str) -> str:
        """生成记忆的唯一标识"""
        # 使用内容的前50字符作为key
        preview = content.strip()[:50]
        return preview
    
    def on_access(self, target: str, content: str):
        """记忆被访问时调用"""
        key = self._make_key(content)
        
        if key not in self.metadata:
            self.metadata[key] = MemoryMetadata(
                key=key,
                content_preview=content[:100],
                created_at=datetime.now().isoformat(),
                target=target
            )
        
        meta = self.metadata[key]
        meta.access_count += 1
        meta.last_accessed = datetime.now().isoformat()
        meta.effectiveness = min(1.0, meta.effectiveness + 0.1)
        
        self._save()
        logger.debug(f"Memory accessed: {key[:30]}... effectiveness={meta.effectiveness:.2f}")
    
    def on_ineffective(self, target: str, content: str):
        """记忆被证明无效时调用"""
        key = self._make_key(content)
        
        if key not in self.metadata:
            self.metadata[key] = MemoryMetadata(
                key=key,
                content_preview=content[:100],
                created_at=datetime.now().isoformat(),
                target=target
            )
        
        meta = self.metadata[key]
        meta.ineffective_count += 1
        meta.effectiveness = max(0.0, meta.effectiveness - 0.2)
        
        self._save()
        logger.debug(f"Memory marked ineffective: {key[:30]}... effectiveness={meta.effectiveness:.2f}")
    
    def get_score(self, content: str) -> float:
        """获取记忆的有效性评分"""
        key = self._make_key(content)
        if key in self.metadata:
            return self.metadata[key].effectiveness
        return 0.5  # 默认评分
    
    def get_ranked_memories(self, target: str, entries: List[str], query: str = "") -> List[str]:
        """
        按有效性排名返回记忆
        
        Args:
            target: memory 或 user
            entries: 记忆条目列表
            query: 搜索查询（用于计算相关性）
        
        Returns:
            排序后的记忆条目列表
        """
        if not entries:
            return []
        
        # 计算每条记忆的得分
        scored = []
        for entry in entries:
            score = self._calculate_score(entry, query)
            scored.append((entry, score))
        
        # 按得分降序排序
        scored.sort(key=lambda x: x[1], reverse=True)
        
        return [entry for entry, _ in scored]
    
    def _calculate_score(self, content: str, query: str = "") -> float:
        """计算记忆的综合得分"""
        key = self._make_key(content)
        meta = self.metadata.get(key)
        
        if not meta:
            # 没有元数据，使用默认评分
            base_score = 0.5
        else:
            base_score = meta.effectiveness
        
        # 时间衰减（最近访问的加分）
        recency_boost = 0.0
        if meta and meta.last_accessed:
            try:
                last_accessed = datetime.fromisoformat(meta.last_accessed)
                days_since = (datetime.now() - last_accessed).days
                if days_since < 7:
                    recency_boost = 0.1
            except:
                pass
        
        # 访问频率加分（最多 +0.15）
        access_boost = 0.0
        if meta:
            access_boost = min(0.15, meta.access_count * 0.01)
        
        # 查询相关性加分
        relevance_boost = 0.0
        if query:
            query_lower = query.lower()
            content_lower = content.lower()
            
            # 简单的关键词匹配
            query_words = set(query_lower.split())
            content_words = set(content_lower.split())
            overlap = len(query_words & content_words)
            
            if overlap > 0:
                relevance_boost = min(0.3, overlap * 0.1)
        
        return base_score + recency_boost + access_boost + relevance_boost
    
    def get_stats(self) -> Dict[str, Any]:
        """获取统计信息"""
        if not self.metadata:
            return {"total": 0}
        
        total = len(self.metadata)
        avg_effectiveness = sum(m.effectiveness for m in self.metadata.values()) / total
        total_accesses = sum(m.access_count for m in self.metadata.values())
        total_ineffective = sum(m.ineffective_count for m in self.metadata.values())
        
        return {
            "total": total,
            "avg_effectiveness": round(avg_effectiveness, 2),
            "total_accesses": total_accesses,
            "total_ineffective": total_ineffective
        }


# 全局单例
_tracker: Optional[EffectivenessTracker] = None


def get_tracker() -> EffectivenessTracker:
    """获取全局追踪器实例"""
    global _tracker
    if _tracker is None:
        _tracker = EffectivenessTracker()
    return _tracker
