from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
res = model.invoke("what is the capital of nitesh ?")

print(res.content)