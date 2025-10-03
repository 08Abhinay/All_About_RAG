from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema.output_parser import StrOutputParser
import os   


load_dotenv()  # Load environment variables from .env file

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

messages = [
    ("system", "You are a helpful assistant who helps be make contacts easily through {small_talk}."),
    ("human", "Hi! I'm {name}. Can you help me network?"),
]

chat_prompt = ChatPromptTemplate.from_messages(messages)


chain = chat_prompt | llm | StrOutputParser()
response = chain.invoke({
    "small_talk": "small talk",
    "name": "Alice"
})
print(response)