from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage ,SystemMessage

messages = [
    SystemMessage("heelo you are my except in threejs , react three fiber library nodejs for creating a 3D websites"),
    HumanMessage("please tell me how do i create a small sphere inthe canvas using react three fiebr ")
]


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
# res = llm.invoke("What is the capital of india ? ")
res = llm.invoke(messages)
print(res.content)
