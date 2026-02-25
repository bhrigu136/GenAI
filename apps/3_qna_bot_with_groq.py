# LLM
# TOOL - GOOGLE sEARCH tOOL
# AGENT
# MemoryErrorsTREAMING
# WEB INTERFACE

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
import streamlit as st

llm = ChatGroq(model="openai/gpt-oss-20b")
search = GoogleSearchAPIWrapper()
tools = [search.run]

memory = MemorySaver()

agent = create_agent(
    model=llm,
    tools=tools,
    checkpointer=memory,
    system_prompt="You are a amazing ai agent and can search on google as well"
)

response = agent.invoke(
    {"messages":[{"role":"user", "content":"Who is PM of India ?"}]},
    {"configurable": {"thread_id": "1"}},
)

print(response["messages"][-1].content)

