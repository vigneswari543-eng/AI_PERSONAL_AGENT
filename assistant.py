
import ollama

def ask_ai(question):
    response = ollama.chat(
        model="llama3.2:1b",
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

    return response["message"]["content"]
