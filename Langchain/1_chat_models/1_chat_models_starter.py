from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os   

load_dotenv()  # Load environment variables from .env file

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

result = llm.invoke("Tell me a joke")
print(result.content)