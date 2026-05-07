import streamlit as st
from llm.client import call_llm
from llm.prompts import qa_prompt, structured_notes_prompt, summarize_prompt, key_points_prompt, rewrite_prompt
from utils.file_loader import extract_text_from_file
from utils.tokenizer import count_tokens

# 页面配置
st.set_page_config(page_title="AI 智能学习助手", page_icon="🧠", layout="wide")

st.title("🧠 AI 智能学习助手")
st.markdown("---")

# 侧边栏：文件上传与设置
with st.sidebar:
    st.header("📂 数据输入")
    upload_file = st.file_uploader("上传学习资料 (PDF 或 TXT)", type=["pdf", "txt"])
    
    st.header("⚙️ 设置")
    mode = st.selectbox(
        "选择功能模式",
        ["总结模式", "重点提取", "结构化笔记", "改写模式", "问答模式"]
    )
    
    if upload_file:
        content = extract_text_from_file(upload_file)
        token_count = count_tokens(content)
        st.info(f"📄 已加载文件: {upload_file.name}")
        st.info(f"🔢 预估 Token 消耗: {token_count}")
    else:
        content = ""

# 主界面
if not upload_file:
    text_input = st.text_area("或者在此处直接输入学习内容", height=300)
    if text_input:
        content = text_input
        token_count = count_tokens(content)
        st.caption(f"🔢 当前输入 Token 估算: {token_count}")

# 额外输入逻辑
question = ""
target_style = ""
if mode == "问答模式":
    question = st.text_input("请输入你想针对内容提问的问题")
elif mode == "改写模式":
    target_style = st.text_input("请输入期望的改写风格（例如：科普风、严谨学术风、小红书风）", value="专业且通俗易懂")

if st.button("🚀 开始处理"):
    if not content:
        st.warning("请先上传文件或输入文本内容！")
    elif mode == "问答模式" and not question:
        st.warning("进入问答模式，请输入具体问题！")
    else:
        # 根据模式选择 Prompt
        if mode == "总结模式":
            prompt = summarize_prompt(content)
        elif mode == "重点提取":
            prompt = key_points_prompt(content)
        elif mode == "结构化笔记":
            prompt = structured_notes_prompt(content)
        elif mode == "改写模式":
            prompt = rewrite_prompt(content, target_style)
        else:  # 问答模式
            prompt = qa_prompt(content, question)

        st.subheader("🤖 AI 处理结果")
        
        # 使用流式输出
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            stream = call_llm(prompt, stream=True)
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            
            # 记录到 session_state (可选，用于后续扩展)
            if "history" not in st.session_state:
                st.session_state.history = []
            st.session_state.history.append({"mode": mode, "result": full_response})
            
        except Exception as e:
            st.error(f"处理过程中出现错误: {e}")

st.markdown("---")
st.caption("Powered by Qwen-Turbo | Designed for AI Application Engineers")
