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


Example output:


def is_palindrome(n):
return str(n) == str(n)[::-1]

num = int(input("Enter a number: "))

if is_palindrome(num):
print("Palindrome")
else:
print("Not Palindrome")


The assistant generates **clean, executable code along with a short explanation**.

---

# 🚀 Deployment

This project can be deployed using:

☁ **Streamlit Cloud**  
⚙ **Render**  
🤗 **HuggingFace Spaces**

Streamlit deployment is the **simplest option**.

---

# ⚠ Technical Boundaries / Limitations

Although the system performs well for many coding tasks, some limitations exist:

⚠ Very large or complex programs may exceed token limits.  
⚠ Generated code may require manual debugging for advanced logic.  
⚠ Conversation history currently uses **local JSON storage**, which is not scalable for production.  
⚠ API rate limits may apply depending on the Groq usage tier.  
⚠ No user authentication or multi-user system is implemented.  
⚠ The model may occasionally produce incomplete responses if token limits are reached.

---

# 🔮 Possible Future Improvements

🚀 Integration with **database storage (SQLite / PostgreSQL)**  
🎨 Add **syntax highlighting + copy code button**  
🧠 Automatic **programming language detection**  
🔐 Implement **user authentication**  
⚡ Add **real-time streaming responses**  
🧪 Implement **code execution sandbox**  
👥 Multi-user chat sessions  
🔎 Conversation history search  
🤖 Support for **multiple LLM providers**

---

# 📁 Project Structure


code-snippet-generator│├── app.py├── requirements.txt├── README.md│├── llm│ ├── llm\_client.py│ └── prompt\_builder.py│├── storage│ └── chat\_store.py│└── data└── conversations.json


---

# 👨‍💻 Author

**Soham Saha**  
🎓 B.Tech Computer Science Engineering  

📘 Mini Project – CSE 6th Semester

---

# 📜 License

This project is intended for **academic and educational purposes**.
