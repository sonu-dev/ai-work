from langchain_ollama import ChatOllama
from tools import save_code_tool

def get_llm():
    
    llm = ChatOllama(
        model="qwen2.5-coder:7b",
        temperature=0,
        debug=True
    )
    
    return llm