from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI
from google.cloud import firestore

load_dotenv()  # Load environment variables from .env file

# PROJECT_ID = "langchain-64527"
PROJECT_ID = "langchain-2a239"  # Replace with your actual GCP project ID
COLLECTION_NAME = "chat_history"
SESSION_ID = "chat_session_1"  # You can change this to manage different sessions

print("Initializing Firestore chat message history...")
client = firestore.Client(project=PROJECT_ID)
chat_history = FirestoreChatMessageHistory(
    client=client,
    collection=COLLECTION_NAME,
    session_id=SESSION_ID
)
print("Firestore chat message history initialized.")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)



# system_message = SystemMessage(content="You are a helpful assistant that has a conversation with the user.")
# chat_history.append(system_message)

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the conversation.")
        break

    user_message = HumanMessage(content=user_input)
    chat_history.add_user_message(user_input)

    messages = chat_history.messages + [user_message]

    response = llm.invoke(messages)
    ai_message = AIMessage(content=response.content)
    chat_history.add_ai_message(response.content)

    print(f"AI: {response.content}")