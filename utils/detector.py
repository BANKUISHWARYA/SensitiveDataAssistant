import re

def detect_sensitive_data(text):

    patterns = {

        "Emails":
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",

        "Phone Numbers":
        r"\b\d{10}\b",

        "PAN Numbers":
        r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",

        "Aadhaar Numbers":
        r"Aadhaar:\s*(\d{4}\s\d{4}\s\d{4})",

        "Credit Card Numbers":
        r"Credit Card:\s*(\d{4}\s\d{4}\s\d{4}\s\d{4})",

        "Bank Account Numbers":
        r"Bank Account:\s*(\d{9,18})",

        "IFSC Codes":
        r"\b[A-Z]{4}0[A-Z0-9]{6}\b",

        "Employee IDs":
        r"\bEMP\d+\b",

        "API Keys":
        r"AIza[A-Za-z0-9_-]{20,}",

        "Passwords":
          r"(?i)Password:\s*password\s*=\s*(\S+)",

        "Confidential Business Information":
        r"Classification:\s*CONFIDENTIAL.*?NDA Required\."
    }

    detected = {}

    for category, pattern in patterns.items():
        matches = re.findall(pattern, text, re.DOTALL)
        matches = list(set(matches))
        detected[category] = matches   # <-- This line was missing

    return detected