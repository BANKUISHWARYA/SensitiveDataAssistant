import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")


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