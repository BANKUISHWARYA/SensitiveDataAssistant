import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load local .env (for local development)
load_dotenv()

# Get API key from Streamlit Secrets first, then .env
api_key = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API Key not found!")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_document(document_text, question):
    prompt = f"""
You are a cybersecurity compliance assistant.

Document:
{document_text}

Question:
{question}

Answer briefly and accurately.
"""

    response = model.generate_content(prompt)
    return response.text