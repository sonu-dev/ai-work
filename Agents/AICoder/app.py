import json
from  tools import save_code_tool
import streamlit as st
from agent import create_code_agent


st.set_page_config(page_title="AI Code Generator Agent")

st.title("AI Code Generator Agent (Ollama and qwen2.5-coder:7b)")

if "agent" not in st.session_state:
    st.session_state.agent = create_code_agent()
    
agent = st.session_state.agent

user_input = st.text_area(
    "Enter coding task:",
    height=150,
    placeholder="Example: Create FastAPI CRUD API and save file"
)


if st.button("Generate Code") and user_input:
    with st.spinner("Generating..."):
        response = agent.invoke({"messages": [{"role": "user", "content": user_input}]})
        
        # AIMessage containing JSON tool call
        ai_msg = response["messages"][-1].content if isinstance(response, dict) else str(response)

        try:
            # Try to parse JSON
            tool_call = json.loads(ai_msg)

            if tool_call.get("name") == "save_code_tool":
                args = tool_call.get("arguments", {})
                result = save_code_tool.invoke(args)
                st.success(f"Tool executed: {tool_call['name']}")
                st.code(result)
            else:
                st.code(ai_msg, language="python")

        except json.JSONDecodeError:
            # Not JSON → just display AI output
            st.code(ai_msg, language="python")