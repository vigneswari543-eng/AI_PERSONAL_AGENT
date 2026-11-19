import streamlit as st
from groq import Groq

def ask_ai(question):
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are VIGNU AI, a friendly personal AI assistant. Give clear, simple and helpful answers."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        max_completion_tokens=1024
    )

    return response.choices[0].message.content
