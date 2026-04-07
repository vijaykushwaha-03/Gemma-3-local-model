# Gemma Local AI Chatbot (Offline)

This is a lightweight local AI project that uses Google's `gemma:2b` model via Ollama. It runs entirely offline on your local machine, ensuring complete privacy, zero API costs, and low latency.

## 🛠️ Requirements
- **Ollama**: To serve the local model.
- **Python 3**: For running the interface scripts.

## 🚀 Setup Instructions

### 1. Install & Setup Ollama
If you haven't installed Ollama yet, run:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Download the Model
Pull the local model before using the application:
```bash
ollama pull gemma:2b
```

### 3. Install Python Dependencies
Set up the virtual environment and install requirements:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 💻 How to Run

Before running the Python scripts, ensure the Ollama model is available or actively running in the background.

### Option A: Command Line Interface (CLI)
Run the fast, lightweight CLI version:
```bash
source venv/bin/activate
python3 chatbot.py
```
*(Type "exit" to quit the CLI chatbot)*

### Option B: Web UI (Streamlit)
Run the graphical browser-based Chatbot interface:
```bash
source venv/bin/activate
streamlit run app.py
```

## 📊 Performance Monitoring
To see how much RAM and CPU the offline model is using, run `htop` or `top` in a separate terminal tab while chatting. You can also run `sudo iftop` or `nethogs` to verify zero network activity (proving it is 100% offline).