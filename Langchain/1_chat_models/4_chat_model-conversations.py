from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI

load_dotenv()  # Load environment variables from .env file

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

chat_history = []

system_message = SystemMessage(content="You are a helpful assistant that has a conversation with the user.")
chat_history.append(system_message)

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the conversation.")
        break

    user_message = HumanMessage(content=user_input)
    chat_history.append(user_message)

    response = llm.invoke(chat_history)
    ai_message = AIMessage(content=response.content)
    chat_history.append(ai_message)

    print(f"AI: {response.content}")