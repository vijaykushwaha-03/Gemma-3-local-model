import streamlit as st
import requests

st.title("🧠 Local Gemma Chatbot")

prompt = st.text_input("Ask something")

if prompt:
    try:
        res = requests.post("http://localhost:11434/api/generate", json={
            "model": "gemma:2b",
            "prompt": prompt,
            "stream": False
        })
        res.raise_for_status()
        st.write(res.json().get("response", "No response found."))
    except Exception as e:
        st.error(f"Error connecting to local Ollama instance: {e}")