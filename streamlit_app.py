import streamlit as st
from streamlit_chat import message

# Page Config
st.set_page_config(page_title="ChatGPT-like UI", layout="wide")

# Sidebar
with st.sidebar:
    st.title("Options")
    st.markdown("Adjust your settings here.")
    model_option = st.selectbox("Select Model:", ["GPT-3.5", "GPT-4"])
    temperature = st.slider("Creativity (Temperature):", 0.0, 1.0, 0.7)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat UI
st.title("Chat with AI")
st.write("Ask me anything!")

# Display previous messages
for i, msg in enumerate(st.session_state["messages"]):
    message(msg["content"], is_user=msg["is_user"], key=str(i))

# User Input
user_input = st.text_input("Your message:", key="user_input")

if user_input:
    # Append user message
    st.session_state["messages"].append({"content": user_input, "is_user": True})
    
    # Placeholder AI response (replace with model call)
    ai_response = f"AI: I received your message: '{user_input}'"
    
    # Append AI response
    st.session_state["messages"].append({"content": ai_response, "is_user": False})
    
    # Refresh page to display new messages
    st.experimental_rerun()
