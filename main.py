import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

load_dotenv()


llm = ChatOpenAI()
tools = [TavilySearch]
agent = create_agent(model=llm, tools=tools)


def main():
    print("hi")
    result = agent.invoke(
        {"messages": HumanMessage(content="what is the weather in Tokyo")}
    )
    print(result)


if __name__ == "__main__":
    main()
