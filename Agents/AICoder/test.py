from agent import create_code_agent


agent = create_code_agent()


response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Create FastAPI CRUD API and save file"
        }
    ]
})


print(response["messages"][-1].content)