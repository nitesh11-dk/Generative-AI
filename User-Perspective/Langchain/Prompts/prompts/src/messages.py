from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
messages=[
    SystemMessage(content='Yoou are a helpful assistance'),
    HumanMessage(content='Define love in one word') 
]

print(messages)
res = model.invoke(messages)

messages.append(AIMessage(content=res.content))
print(messages)