from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
res = llm.invoke("What is the capital of india ? ")
print(res.content)
