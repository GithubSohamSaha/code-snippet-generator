# AI Code Snippet Generator Agent

This project is a **Streamlit-based AI code assistant** that generates code snippets using an LLM.
live Demo : https://code-snippet-generator-27mywk8qvg827jmefv96ce.streamlit.app/

## Features

- Multi-language code generation
- Chat-style interface
- Conversation history
- Delete conversations
- Minimal explanation with clean code
- Fast inference using Groq LLM

## Tech Stack

- Python
- Streamlit
- Groq API (LLM)
- JSON-based chat storage

## Installation

Clone the repository:


git clone https://github.com/yourusername/code-snippet-generator.git

cd code-snippet-generator


Install dependencies:


pip install -r requirements.txt


Create `.streamlit/secrets.toml`:


GROQ_API_KEY="your_api_key_here"


Run the app:


streamlit run app.py


## Deployment

This project can be deployed using:

- Streamlit Cloud
- Render
- HuggingFace Spaces

## Example

Ask prompts like:


write a python program to check palindrome number


The AI will generate clean runnable code.

---

Built as part of **B.Tech CSE Mini Project**.
