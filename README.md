# 🔒 Sensitive Data Detection & Compliance Assistant

An AI-powered web application built using **Python**, **Streamlit**, and **Google Gemini AI** to detect sensitive information in documents, classify risk levels, generate compliance summaries, and answer user questions about uploaded documents.

---

# 📌 Project Overview

This application helps identify sensitive and confidential information present in uploaded documents.

It supports:

- Uploading PDF, TXT, and CSV files
- Detecting sensitive information using Regular Expressions
- Classifying documents based on risk level
- Generating AI-powered compliance summaries
- Asking questions about the uploaded document using Google Gemini AI
- Downloading a PDF compliance report

---

# 🚀 Features

- 📄 Upload PDF, TXT, and CSV documents
- 🔍 Detect:
  - Email Addresses
  - Phone Numbers
  - PAN Numbers
  - Aadhaar Numbers
  - Credit Card Numbers
  - Bank Account Numbers
  - IFSC Codes
  - API Keys
  - Passwords
  - Employee IDs
  - Confidential Business Information
- ⚠️ Risk Classification (Low / Medium / High)
- 🤖 AI-generated Compliance Summary
- 💬 AI Question Answering using Gemini
- 📑 Download Compliance Report as PDF

---

# 🛠️ Technologies Used

- Python 3.11
- Streamlit
- Google Gemini API
- Regex (re)
- Pandas
- PyMuPDF
- ReportLab
- python-dotenv

---

# ⚙️ Setup Instructions

## 1. Clone the repository

```bash
git clone https://github.com/BANKUISHWARYA/SensitiveDataAssistant.git
cd SensitiveDataAssistant
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Create a .env file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Generate an API key from:

https://aistudio.google.com/app/apikey

## 5. Run the application

```bash
streamlit run app.py
```

---

# 🏗️ Architecture Overview

```
User Uploads Document
        │
        ▼
Document Parser
(PDF / TXT / CSV)
        │
        ▼
Sensitive Data Detector
(Regex Patterns)
        │
        ▼
Risk Classification
        │
        ▼
Compliance Summary
        │
        ▼
Gemini AI
(Document Question Answering)
        │
        ▼
PDF Compliance Report
```

---

# 🤖 AI / ML Approach Used

The project combines rule-based detection with Generative AI.

### Sensitive Data Detection

Regular Expressions (Regex) are used to identify:

- Emails
- PAN
- Aadhaar
- Phone Numbers
- Credit Cards
- Bank Details
- API Keys
- Passwords
- Employee IDs

### Risk Classification

Risk is calculated based on the number and type of sensitive information detected.

- Low Risk
- Medium Risk
- High Risk

### AI-powered Question Answering

Google Gemini AI receives the uploaded document as context and answers user questions, including:

- Document summaries
- Compliance observations
- Security risks
- Sensitive data explanation
- Recommended remediation steps

---

# 📂 Project Structure

```
SensitiveDataAssistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── sample_docs/
│   └── sample.txt
│
└── utils/
    ├── detector.py
    ├── parser.py
    ├── risk.py
    ├── summary.py
    ├── llm.py
    ├── mask.py
    └── pdf_report.py
```

---

# ⚠️ Challenges Faced

- Detecting multiple sensitive data formats accurately using Regex.
- Handling different document formats (PDF, TXT, CSV).
- Configuring Google Gemini API securely using environment variables.
- Deploying the application on Streamlit Cloud with API secrets.
- Managing package dependency conflicts during deployment.

---

# 🚀 Future Improvements

- OCR support for scanned PDFs.
- Automatic data masking and redaction.
- Multi-document analysis.
- RAG (Retrieval-Augmented Generation).
- Vector database integration (FAISS/ChromaDB).
- Audit logging.
- Docker support.
- User authentication and role-based access.

---

# 🌐 Deployment

**Streamlit App**

https://sensitivedataassistant-izdl27hqoi9evajpg4cjfh.streamlit.app

---

# 💻 GitHub Repository

https://github.com/BANKUISHWARYA/SensitiveDataAssistant

---

# 📷 Demo

The application demonstrates:

- Document Upload
- Sensitive Data Detection
- Risk Classification
- AI Compliance Summary
- AI Question Answering
- PDF Compliance Report Generation

---

# 👩‍💻 Developed By

**Banku Ishwarya**

Sensitive Data Detection & Compliance Assistant

Proteccio Data – AI Innovation Internship Assignment