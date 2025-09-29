from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os   

load_dotenv()  # Load environment variables from .env file

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

messages = [
    SystemMessage(content="You are a helpful assistant that translates English to French."),
    HumanMessage(content="Translate the following sentence: 'I love programming.'"),
]

response = llm.invoke(messages)
print(response.content)
