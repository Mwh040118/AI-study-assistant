def summarize_prompt(text):
    return f"""
请对以下内容进行专业总结：

要求：
1. 提炼核心要点
2. 分层结构输出
3. 使用清晰标题

内容：
{text}
"""

def key_points_prompt(text):
    return f"""
请提取以下内容的重点：

要求：
- bullet points形式
- 每点不超过20字
- 覆盖全部核心信息

内容：
{text}
"""

def structured_notes_prompt(text):
    return f"""
你是一个高级知识结构化与认知建模助手。

你的任务是将输入内容转化为“思维导图式知识结构”，用于高效学习与记忆。

# 🧠 结构规则
- Level 1：核心主题（1个）
- Level 2：关键模块（3~6个）
- Level 3：具体知识点（每个模块3~5个）

# ⚙️ 输出规范
- 使用 Markdown 层级结构
- 使用 emoji 标记层级（🌳📌🔹）
- 每个节点尽量短句表达
- 强调“逻辑结构”，而不是原文复述
- 自动去除冗余信息
- 如果内容复杂，可适当归类合并

# 🎯 输出格式

## 🌳 核心主题

### 📌 模块1
🔹 要点1  
🔹 要点2  

### 📌 模块2
🔹 要点1  
🔹 要点2  

# 📄 输入内容：
{text}
"""

def qa_prompt(text, question):
    return f"""
基于以下内容回答问题：

内容：
{text}

问题：
{question}

要求：
只基于文本回答，不要编造
"""

def rewrite_prompt(text, target_style="专业且通俗易懂"):
    return f"""
请将以下内容进行改写。

目标风格：{target_style}

要求：
1. 保持原意不变
2. 优化句式结构，提升可读性
3. 修正可能的语法或表达错误

内容：
{text}
"""
