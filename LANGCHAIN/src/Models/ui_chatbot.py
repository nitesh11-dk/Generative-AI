import streamlit as st
from pymongo import MongoClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["chatbot_db"]
collection = db["chat_history"]

# LangChain Model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# User ID
USER_ID = "nitesh123"


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


# Initialize Streamlit App
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")
st.write("Chat with your AI assistant. Type below to start the conversation!")

# Load Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = get_chat_history(USER_ID)

# Display Chat History
st.subheader("📜 Chat History")

# Custom CSS for alignment
st.markdown("""
    <style>
    .chat-container {
        display: flex;
        flex-direction: column;
    }
    .message {
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        max-width: 70%;
    }
    .system {
        text-align: center;
        align-self: center;
    }
    .human {
        text-align: right;
        align-self: flex-start;
    }
    .ai {
        text-align: left;
        align-self: flex-end;
    }
    </style>
""", unsafe_allow_html=True)

# Chat Display
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.chat_history:
    if isinstance(msg, SystemMessage):
        st.markdown(f'<div class="message system">{msg.content}</div>', unsafe_allow_html=True)
    elif isinstance(msg, HumanMessage):
        st.markdown(f'<div class="message human">You:  {msg.content}</div>', unsafe_allow_html=True)
    elif isinstance(msg, AIMessage):
        st.markdown(f'<div class="message ai">AI:  {msg.content}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# User Input Form
with st.form(key="chat_form"):
    user_input = st.text_input("Type your message:", "")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input.strip():
    # Append User Message
    new_user_message = HumanMessage(content=user_input)
    st.session_state.chat_history.append(new_user_message)

    # Send to AI Model
    try:
        response = model.invoke(st.session_state.chat_history).content
        new_ai_message = AIMessage(content=response)
        st.session_state.chat_history.append(new_ai_message)

        # Save updated chat history to MongoDB
        save_chat_history(USER_ID, st.session_state.chat_history)

        # Refresh the page to show the new chat messages
        st.rerun()
    except Exception as e:
        st.error(f"⚠️ API Error: {e}. Please try again.")
