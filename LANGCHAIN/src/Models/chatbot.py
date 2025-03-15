from unittest import TestSuite
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage ,SystemMessage,AIMessage
load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

chat_histroy = []

chat_histroy.append(SystemMessage(content="You are bestfreind of nitesh kushwaha"))

while True:
    prompt = input("You :")
    if prompt.lower() == 'exit':
        break
    chat_histroy.append(HumanMessage(content=prompt))
    res = model.invoke(chat_histroy)
    response = res.content
    chat_histroy.append(AIMessage(content=response))
    print("MODEL:" ,response)
    
    
print(chat_histroy)    
    

