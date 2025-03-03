from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Hello from prompts!")
    gi()

def gi():
    # Initialize the model with the API key
    model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
    res = model.invoke("What is the capital of maharastra?")
    print(res.content)

if __name__ == "__main__":
    main()

