import streamlit as st

# Page Config
st.set_page_config(page_title="Chat UI", layout="wide")

# Sidebar
with st.sidebar:
    st.title("Options")
    st.markdown("Adjust your settings here.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat UI
st.title("Chat Interface")
st.write("Type a message below.")

# Display previous messages
for i, msg in enumerate(st.session_state["messages"]):
    st.chat_message("user" if msg["is_user"] else "assistant").write(msg["content"])

# User Input
user_input = st.text_input("Your message:", key="user_input")

if user_input:
    # Append user message and AI response
    st.session_state["messages"].append({"content": user_input, "is_user": True})
    st.session_state["messages"].append({"content": user_input, "is_user": False})
    
    # Display response immediately
    st.chat_message("assistant").write(user_input)
