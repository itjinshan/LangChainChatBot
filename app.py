import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

# App Framework
st.title("Personal Assistant")
prompt = st.text_input("How can I help: ")

# LLMs
llm = OpenAI(temperature = 0.9)

if prompt:
        response = llm(prompt)
        st.write(response)