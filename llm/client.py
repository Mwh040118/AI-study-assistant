from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME

# 初始化客户端，增加 base_url 支持
client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL
)

def call_llm(prompt: str, stream: bool = False):
    """
    调用大模型，支持流式输出
    """
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "你是一个专业的学习助手，擅长总结、结构化知识和解答疑问。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            stream=stream
        )
        
        if stream:
            return response
        else:
            return response.choices[0].message.content
            
    except Exception as e:
        return f"调用模型出错: {str(e)}"
