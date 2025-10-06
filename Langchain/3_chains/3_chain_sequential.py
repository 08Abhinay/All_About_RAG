from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda

load_dotenv()  # Load environment variables from .env file

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Create a prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant who helps be make contacts easily through {small_talk}."),
        ("human", "Hi! I'm {name}. Can you help me network?"),
    ]
)       

#Translating the above template to French
prompt_french_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a translator that translates English to {language}."),
        ("human", "Translate the following text to {language}: {text}"),
    ]
)   


chain = prompt_template | llm | StrOutputParser() | \
        prompt_french_template | llm | StrOutputParser()
        
response = chain.invoke({
    "small_talk": "small talk",
    "name": "Alice",        
    "language": "French"
})      
print(response)

