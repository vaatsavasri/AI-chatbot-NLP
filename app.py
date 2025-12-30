import streamlit as st
from chatbot import chatbot_response

st.title("AI Chatbot using NLP")

user_input = st.text_input("You:")

if user_input:
    response = chatbot_response(user_input)
    st.text_area("Bot:", response)
