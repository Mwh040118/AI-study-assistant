import PyPDF2
import io

def load_text(file):
    """读取纯文本文件"""
    return file.read().decode("utf-8")

def load_pdf(file):
    """读取PDF文件内容"""
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    """根据文件类型提取文本"""
    if uploaded_file is None:
        return ""
    
    file_type = uploaded_file.name.split(".")[-1].lower()
    
    if file_type == "txt":
        return load_text(uploaded_file)
    elif file_type == "pdf":
        return load_pdf(uploaded_file)
    else:
        return "不支持的文件格式"
