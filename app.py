
import streamlit as st
from assistant import ask_ai

st.set_page_config(page_title="VIGNU AI", page_icon="🤖")

st.title("🤖 VIGNU AI")
st.write("Your Personal AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask VIGNU AI anything...")

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("VIGNU AI is thinking..."):
            try:
                answer = ask_ai(question)
                st.write(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
            except Exception as e:
                st.error(f"Error: {e}")
