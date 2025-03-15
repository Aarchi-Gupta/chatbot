import streamlit as st

# Page Config
st.set_page_config(page_title="Chat UI", layout="wide")

# Sidebar
with st.sidebar:
    st.title("ChatGPT-like UI")
    st.markdown("Adjust your settings here.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

# Chat UI with ChatGPT-style layout
st.markdown("""
    <style>
        .stChatMessage {
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .user-message {
            background-color: #dcf8c6;
            text-align: right;
        }
        .assistant-message {
            background-color: #f1f1f1;
            text-align: left;
        }
        .stTextInput {
            position: fixed;
            bottom: 10px;
            width: 90%;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Chat Interface")

# Display previous messages in chat format
chat_container = st.container()
with chat_container:
    for i, msg in enumerate(st.session_state["messages"]):
        with st.chat_message("user" if msg["is_user"] else "assistant"):
            st.markdown(f'<div class="stChatMessage {"user-message" if msg["is_user"] else "assistant-message"}">{msg["content"]}</div>', unsafe_allow_html=True)

# User Input Box at Bottom
user_input = st.text_input("Type your message and press Enter...", key="user_input", label_visibility="hidden")

if user_input:
    # Append user message and AI response
    st.session_state["messages"].append({"content": user_input, "is_user": True})
    st.session_state["messages"].append({"content": user_input, "is_user": False})
    
    # Clear input field
    st.session_state["user_input"] = ""
    st.rerun()
