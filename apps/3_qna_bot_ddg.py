from dotenv import load_dotenv
load_dotenv()

# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

import streamlit as st

# LLM
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash"
# )
llm = ChatGroq(model="openai/gpt-oss-20b", streaming=True)

# Search Tool
search = DuckDuckGoSearchRun()

tools = [search]

# Memory
if "memory" not in st.session_state:
    st.session_state.memory = MemorySaver()
    # st.session_state.memory.save("Hello, I am your assistant. How can I help you today?", thread_id="1")
    st.session_state.history = []

# Agent
agent = create_agent(
    model=llm,
    tools=tools,
    checkpointer=st.session_state.memory,
    system_prompt="""
    You are an AI assistant that can search the web using DuckDuckGo.
    Give accurate and concise answers.
    """
)

# Streamlit UI
st.subheader("QuickAnswer - Answer at the speed of thought")

for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input("Ask anything")

if query:
    st.session_state.history.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)

    response = agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": "1"}},
        stream_mode="messages"
    )

    # answer = response["messages"][-1].content

    # st.chat_message("ai").markdown(answer)

    ai_container = st.chat_message("ai")
    with ai_container:
        space = st.empty()

        message = ""
        for chunk in response:
            message = message + chunk[0].content
            space.write(message)

        st.session_state.history.append({"role": "ai", "content": message})