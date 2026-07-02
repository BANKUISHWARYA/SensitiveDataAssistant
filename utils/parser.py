import fitz
import pandas as pd


def extract_text(uploaded_file):

    filename = uploaded_file.name.lower()

    # TXT file
    if filename.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    # CSV file
    elif filename.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        return df.to_string(index=False)

    # PDF file
    elif filename.endswith(".pdf"):
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        text = ""

        for page in pdf:
            text += page.get_text()

        return text

    return ""
