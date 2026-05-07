import tiktoken

def count_tokens(text: str, model: str = "gpt-3.5-turbo"):
    """
    计算文本的 token 数量
    注意：对于 Qwen 等模型，tiktoken 只是一个近似估算
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        # 如果模型不直接支持，默认使用 cl100k_base (GPT-4/3.5-turbo)
        encoding = tiktoken.get_encoding("cl100k_base")
        
    return len(encoding.encode(text))

def check_token_limit(text: str, limit: int = 4000):
    """检查是否超过 token 限制"""
    tokens = count_tokens(text)
    return tokens <= limit, tokens
