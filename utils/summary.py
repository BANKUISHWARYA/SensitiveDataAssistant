def generate_summary(detected_data, risk):

    summary = f"""
Compliance Summary

Overall Risk Level:
{risk}

Detected Sensitive Information:
"""

    for category, values in detected_data.items():
        if values:
            summary += f"\n• {category}: {len(values)} detected"

    summary += "\n\nSecurity Risks:\n"

    if detected_data["Aadhaar Numbers"] or detected_data["PAN Numbers"]:
        summary += "• Personally Identifiable Information (PII) detected.\n"

    if detected_data["Credit Card Numbers"] or detected_data["Bank Account Numbers"]:
        summary += "• Financial information detected.\n"

    if detected_data["Passwords"] or detected_data["API Keys"]:
        summary += "• Credentials and authentication secrets detected.\n"

    if detected_data["Emails"] or detected_data["Phone Numbers"]:
        summary += "• Contact information is present.\n"

    summary += """
Suggested Remediation:
• Encrypt sensitive documents.
• Restrict document access using role-based permissions.
• Mask sensitive information before sharing.
• Rotate exposed passwords and API keys immediately.
• Store confidential documents securely.
• Follow GDPR/DPDP and organizational compliance policies.
"""

    return summary