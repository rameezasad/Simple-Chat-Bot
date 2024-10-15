import streamlit as st
from Model import chat_with_gpt

st.set_page_config(page_title="DS11 GPT ChatBot", page_icon="🤖")

st.title("Hey I am a ChatBot")
st.write("Am i looking like a website")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

def send_message():
    if user_input:
        st.session_state.messages.append({"role": "Asif", "content": user_input})
        response = chat_with_gpt(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
user_input = st.text_input("Asif: ")

if st.button("Send"):
    send_message()

for i, message in enumerate(st.session_state.messages):
    role = "Asif" if message["role"] == "Asif" else "Chatbot"
    st.text_area(f"{role}:", value=message["content"], height=100, max_chars=None, key=f"{role}_{i}")

st.session_state.input = ""
