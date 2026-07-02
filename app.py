import streamlit as st
import pandas as pd

from utils.parser import extract_text
from utils.detector import detect_sensitive_data
from utils.risk import calculate_risk
from utils.summary import generate_summary
from utils.llm import ask_document
from utils.mask import mask_value
from utils.pdf_report import create_pdf_report

# ---------------- Page Config ----------------

st.set_page_config(
    page_title="Sensitive Data Detection Assistant",
    page_icon="🔒",
    layout="wide"
)

# ---------------- Sidebar ----------------

st.sidebar.title("🔒 Sensitive Data Assistant")

st.sidebar.info("""
### Features

✅ Document Upload

✅ Sensitive Data Detection

✅ Risk Classification

✅ AI Compliance Summary

✅ Ask AI Questions
""")

# ---------------- Main Title ----------------

st.title("🔒 Sensitive Data Detection & Compliance Assistant")

st.markdown("""
Upload a **PDF**, **TXT**, or **CSV** document to detect sensitive information,
classify the document's risk level, generate an AI-powered compliance summary,
and ask questions about the uploaded document.
""")

# ---------------- Upload ----------------

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["pdf", "txt", "csv"]
)

# ---------------- Process ----------------

if uploaded_file is not None:

    st.success("✅ File uploaded successfully!")

    st.write("### 📄 File Details")
    st.write("**Filename:**", uploaded_file.name)
    st.write("**File Type:**", uploaded_file.type)
    st.write("**File Size:**", uploaded_file.size, "bytes")

    # Extract text
    document_text = extract_text(uploaded_file)

    # Detect sensitive data
    detected_data = detect_sensitive_data(document_text)

    # Calculate risk
    risk = calculate_risk(detected_data)

    # Generate compliance summary
    summary = generate_summary(detected_data, risk)

    # Dashboard values
    total_items = sum(len(values) for values in detected_data.values())

    if risk == "🔴 High Risk":
        compliance_score = 35

    elif risk == "🟡 Medium Risk":
        compliance_score = 70

    else:
        compliance_score = 95

    # ---------------- Dashboard ----------------

    st.divider()

    st.subheader("📊 Security Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📄 Documents", "1")
    col2.metric("🔍 Sensitive Items", total_items)
    col3.metric("🚨 Risk", risk)
    col4.metric("🛡️ Compliance", f"{compliance_score}%")

    st.progress(compliance_score / 100)

    chart_data = pd.DataFrame({
        "Category": list(detected_data.keys()),
        "Count": [len(v) for v in detected_data.values()]
    })

    st.write("### 📈 Sensitive Data Overview")
    st.bar_chart(chart_data.set_index("Category"))

    # ---------------- Extracted Text ----------------

    st.divider()

    st.subheader("📄 Extracted Text")

    st.text_area(
        "Document Content",
        document_text,
        height=250
    )

    # ---------------- Sensitive Data ----------------

    st.divider()

    st.subheader("🔍 Sensitive Data Detected")

    for category, values in detected_data.items():

        st.markdown(f"### {category}")

        if values:
            for value in values:
                st.write("•", mask_value(category, value))
        else:
            st.write("No data found.")

    # ---------------- Risk ----------------

    st.divider()

    st.subheader("🚨 Risk Classification")

    if risk == "High Risk":
        st.error("🔴 High Risk")
    elif risk == "Medium Risk":
        st.warning("🟡 Medium Risk")
    else:
        st.success("🟢 Low Risk")

    # ---------------- Summary ----------------

    st.divider()

    st.subheader("📋 AI Compliance Summary")

    st.text_area(
        "Compliance Report",
        summary,
        height=250
    )

    # ---------------- Download ----------------

    pdf_file = create_pdf_report(
        uploaded_file.name,
        risk,
        compliance_score,
        detected_data,
        summary
    )

    with open(pdf_file, "rb") as pdf:

        st.download_button(
            label="📄 Download PDF Report",
            data=pdf,
            file_name="Compliance_Report.pdf",
          mime="application/pdf"
    )

    

    # ---------------- AI Chat ----------------

    st.divider()

    st.subheader("💬 Ask AI About This Document")

    question = st.text_input("Enter your question")

    if st.button("Ask AI"):

        if question.strip():

            q = question.lower()

            if "how many email" in q:
                st.success(
                    f"There are {len(detected_data['Emails'])} email address(es)."
                )

            elif "how many phone" in q:
                st.success(
                    f"There are {len(detected_data['Phone Numbers'])} phone number(s)."
                )

            elif "risk" in q:
                st.success(f"The document is classified as {risk}.")

            elif "sensitive data" in q:

                found = [
                    category
                    for category, values in detected_data.items()
                    if values
                ]

                st.success(
                    "Sensitive data detected:\n\n• " +
                    "\n• ".join(found)
                )

            else:

                with st.spinner("🤖 Thinking..."):
                    answer = ask_document(document_text, question)

                st.success(answer)

        else:
            st.warning("Please enter a question.")


st.divider()

st.caption(
    "Built using Python • Streamlit • Gemini AI • Regex • Pandas"
)