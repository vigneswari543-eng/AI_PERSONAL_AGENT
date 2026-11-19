
import streamlit as st
from ollama import Client

def ask_ai(question):
    api_key = st.secrets["OLLAMA_API_KEY"]

    client = Client(
        host="https://ollama.com",
        headers={
            "Authorization": f"Bearer {api_key}"
        }
    )

    response = client.chat(
        model="gemma4:31b",
        messages=[
            {
                "role": "system",
                "content": "You are VIGNU AI, a friendly and intelligent personal assistant. Give clear and helpful answers."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.message.content
