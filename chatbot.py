import requests
import time

URL = "http://localhost:11434/api/generate"

def chat(prompt):
    try:
        response = requests.post(URL, json={
            "model": "gemma:2b",
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return response.json().get("response", "No response found in API reply.")
    except Exception as e:
        return f"Error connecting to local Ollama instance: {e}"

print("🧠 Local AI Chatbot (type 'exit' to quit)\n")

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        start = time.time()
        reply = chat(user_input)
        end = time.time()

        print(f"AI: {reply}")
        print(f"⏱ Response time: {round(end - start, 2)} sec\n")