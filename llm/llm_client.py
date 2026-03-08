"""
LLM Client Module

Handles communication with the external language model.
Currently uses Groq API with Llama3-8B.
"""
from groq import Groq
import streamlit as st

# Initialize Groq client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Updated working Groq model
MODEL = "llama-3.1-8b-instant"


def generate_code(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=800
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Groq API Error: {str(e)}"