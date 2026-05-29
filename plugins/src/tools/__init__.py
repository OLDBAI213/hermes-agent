"""SRC Suite 工具包装层 —— 把本机 .exe 用 subprocess 包成结构化返回。

每个模块暴露 `run(...)`，返回字典。
journal 写入由 facade 负责，工具层保持纯函数。
"""
