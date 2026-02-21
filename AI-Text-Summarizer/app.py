import streamlit as st
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

DB_PATH = "chroma_db"

# ---- Load vectorstore ----
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# ---- Load LLM ----
llm = ChatOllama(model="llama3", temperature=0.2)

# ---- Prompt ----
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Use the following context to answer the question.

Context:
{context}

Chat History:
{chat_history}

Question:
{question}

Answer:
""")

# ---- Streamlit session ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

st.title("Local RAG Chat (Ollama + LangChain)")

user_input = st.chat_input("Ask a question...")

if user_input:
    # 1️⃣ Retrieve docs
    docs = retriever.invoke(user_input)  # <-- correct

    # 2️⃣ Format context
    context = format_docs(docs)

    # 3️⃣ Combine chat history
    chat_history_text = "\n".join(f"{role}: {msg}" for role, msg in st.session_state.chat_history)

    # 4️⃣ Build prompt
    final_prompt = prompt.format(
        context=context,
        chat_history=chat_history_text,
        question=user_input
    )

    # 5️⃣ Get LLM response
    response = llm.invoke(final_prompt)  # <-- NEW

    # 6️⃣ Save chat
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", response))

# ---- Display chat ----
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(message)