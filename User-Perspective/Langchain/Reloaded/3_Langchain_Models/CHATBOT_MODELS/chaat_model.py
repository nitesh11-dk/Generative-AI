from langchain_google_genai import GoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

chat_model = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)

result = chat_model.invoke("What is the capital of India?")
print(result)