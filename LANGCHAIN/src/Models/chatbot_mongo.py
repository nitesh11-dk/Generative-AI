from pymongo import MongoClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["chatbot_db"]
collection = db["chat_history"]

# LangChain Model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# User ID (Alag users ka alag chat store hoga)
USER_ID = "nitesh123"

# ✅ **1. Retrieve Old Chat History from MongoDB**
chat_data = collection.find_one({"user_id": USER_ID})

def convert_to_messages(history_list):
    """Convert list of dicts back to LangChain message objects"""
    msg_map = {"system": SystemMessage, "human": HumanMessage, "ai": AIMessage}
    return [msg_map[msg["type"]](content=msg["content"]) for msg in history_list]

if chat_data:
    chat_history = convert_to_messages(chat_data["history"])
else:
    chat_history = [SystemMessage(content="You are best friend of Nitesh Kushwaha")]

while True:
    prompt = input("You: ")
    if prompt.lower() == 'exit':
        break

    chat_history.append(HumanMessage(content=prompt))
    res = model.invoke(chat_history)
    response = res.content
    chat_history.append(AIMessage(content=response))
    print("MODEL:", response)

    # ✅ **2. Store Chat History in MongoDB (Convert to Dict)**
    def convert_to_dict(history):
        """Convert LangChain messages to dictionary format for MongoDB"""
        return [{"type": msg.__class__.__name__.replace("Message", "").lower(), "content": msg.content} for msg in history]

    collection.update_one(
        {"user_id": USER_ID},
        {"$set": {"history": convert_to_dict(chat_history)}},
        upsert=True  # Agar pehle se nahi hai to insert kar dega
    )

print("Final Chat History:", chat_history)
