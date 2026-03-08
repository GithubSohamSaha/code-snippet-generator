# 🤖 AI Code Snippet Generator Agent

A **Streamlit-based AI coding assistant** that generates programming code snippets using a Large Language Model (LLM).

The system allows users to interact through a **chat-style interface** and automatically generates **clean, runnable code with minimal explanations**.

---

## 🌐 Live Demo

🔗 https://code-snippet-generator-27mywk8qvg827jmefv96ce.streamlit.app/

---

# 🚀 Features

✨ Multi-language code generation (Python, C, C++, Java, etc.)  
💬 Chat-style interactive interface  
📜 Persistent conversation history  
🗑 Delete conversation functionality  
🧠 Clean code output with minimal comments  
⚡ Fast inference using **Groq LLM API**  
💾 Lightweight JSON-based chat storage  

---

# 🏗 System Architecture


User Input
│
▼
🖥 Streamlit UI
│
▼
🧩 Prompt Builder
│
▼
⚡ Groq LLM API
│
▼
📄 Generated Code Response
│
▼
💾 Conversation Storage (JSON)


---

# 🛠 Tech Stack

| Component | Technology |
|--------|--------|
| 🖥 Frontend UI | Streamlit |
| ⚙ Backend Logic | Python |
| 🤖 LLM Inference | Groq API |
| 🧠 Model Used | LLaMA 3.1 |
| 💾 Storage | JSON-based local storage |
| ☁ Deployment | Streamlit Cloud |

---

# 📦 Installation

Clone the repository


git clone https://github.com/GithubSohamSaha/code-snippet-generator.git

cd code-snippet-generator


Install dependencies


pip install -r requirements.txt


Create the secrets file


.streamlit/secrets.toml


Add your Groq API key


GROQ_API_KEY="your_api_key_here"


Run the application


streamlit run app.py


---

# 💡 Example Usage

Example prompt:


write a python program to check palindrome number


The AI will generate clean runnable code.

---

Built as part of **B.Tech CSE Mini Project**.
