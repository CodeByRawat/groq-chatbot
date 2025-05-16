import streamlit as st
import requests
import os

# Set title
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Chat with Groq LLaMA 3")

# Input box
user_input = st.text_input("You:", placeholder="Ask me anything...")

# API setup
api_key = st.secrets.get("GROQ_API_KEY")
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
model = "llama3-8b-8192"

# Generate response when user enters input
if user_input:
    with st.spinner("Thinking..."):
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )

        try:
            data = response.json()
            reply = data["choices"][0]["message"]["content"]
            st.markdown(f"**GroqBot:** {reply}")
        except Exception as e:
            st.error("Error fetching response from Groq API.")
