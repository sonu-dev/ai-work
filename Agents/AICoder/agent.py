from llm import get_llm
from tools import save_code_tool
from langchain.agents import create_agent


def create_code_agent():
    
    llm = get_llm()
    tools = [save_code_tool]

    agent = create_agent(
        model=llm.bind_tools(tools),
        tools=tools,
        system_prompt="You are a coding agent. Always use tools to save generated code."
    )

    return agent