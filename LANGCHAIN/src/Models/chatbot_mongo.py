from pymongo import MongoClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os
import time


load_dotenv()


MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["chatbot_db"]
collection = db["chat_history"]


model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

USER_ID = "nitesh1234"


def get_chat_history(user_id):
    """Retrieve chat history from MongoDB and convert it to LangChain message format."""
    chat_data = collection.find_one({"user_id": user_id})
    if not chat_data:
        return [SystemMessage(content="You are best friend of Nitesh Kushwaha")]

    msg_map = {"system": SystemMessage, "human": HumanMessage, "ai": AIMessage}
    return [msg_map[msg["type"]](content=msg["content"]) for msg in chat_data["history"] if msg["content"].strip()]


def save_chat_history(user_id, chat_history):
    """Convert chat history to dictionary format and store it in MongoDB."""
    history_dict = [
        {"type": msg.__class__.__name__.replace("Message", "").lower(), "content": msg.content}
        for msg in chat_history if msg.content.strip()
    ]
    collection.update_one({"user_id": user_id}, {"$set": {"history": history_dict}}, upsert=True)


def chat():
    """Main chatbot loop."""
    chat_history = get_chat_history(USER_ID)

    while True:
        prompt = input("You: ").strip()
        if prompt.lower() == 'exit':
            break

        if not prompt:
            print("⚠️ Empty input ignored. Please enter a valid message.")
            continue

        chat_history.append(HumanMessage(content=prompt))

        # Ensure no empty messages before sending to Gemini
        valid_chat_history = [msg for msg in chat_history if msg.content.strip()]
        if not valid_chat_history:
            print("⚠️ No valid messages to send to Gemini. Skipping request.")
            continue

        try:
            res = model.invoke(valid_chat_history)
            response = res.content
        except Exception as e:
            print(f"⚠️ API Error: {e}. Retrying in 5 seconds...")
            time.sleep(5)
            continue

        chat_history.append(AIMessage(content=response))
        print("MODEL:", response)

        # Save updated chat history
        save_chat_history(USER_ID, chat_history)

    print("Final Chat History:", chat_history)


if __name__ == "__main__":
    chat()
