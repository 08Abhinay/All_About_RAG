from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate
import os   


load_dotenv()  # Load environment variables from .env file

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

template = "Write an {tone} email to {company} about {position} position, mentioning your {skills}."

prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({
    "tone": "professional",
    "company": "Google",
    "position": "Software Engineer",
    "skills": "Python, Machine Learning, and Problem-Solving"
})

result = llm.invoke(prompt)
print(result.content)   
print(result)

print("---------------------------------------------------")

messages = [
    ("system", "You are a helpful assistant who helps be make friends easily through {small_talk}."),
    ("human", "Hi! I'm {name}. Can you help me make friends?"),
]
chat_prompt = ChatPromptTemplate.from_messages(messages)
# print(chat_prompt)
prompt_2 = chat_prompt.invoke({
    "small_talk": "small talk",
    "name": "Alice"
})
result = llm.invoke(prompt_2)
# print(result.content)   
# print(result)
for msg in prompt_2.to_messages():
    print(msg.type, msg.content)
