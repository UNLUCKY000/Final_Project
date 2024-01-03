import streamlit as st
from gpt4all import GPT4All
model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")
st.title("Chat with GPT-4")
input_text = st.text_input("Your message:")
if input_text:
    output = model.generate(input_text, max_tokens=300)
    st.text(output)
