from langchain_ollama import ChatOllama
from tools import save_code_tool

def get_llm():
    
    llm = ChatOllama(
        model="qwen2.5-coder:7b",
        base_url="http://host.docker.internal:11434",  # important
        temperature=0.1,
    )
    
    return llm