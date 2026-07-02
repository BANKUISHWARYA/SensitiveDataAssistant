def calculate_risk(detected_data):

    score = 0

    score += len(detected_data["Emails"]) * 1
    score += len(detected_data["Phone Numbers"]) * 1
    score += len(detected_data["PAN Numbers"]) * 2
    score += len(detected_data["Aadhaar Numbers"]) * 3
    score += len(detected_data["Credit Card Numbers"]) * 3
    score += len(detected_data["Bank Account Numbers"]) * 3
    score += len(detected_data["IFSC Codes"]) * 1
    score += len(detected_data["Employee IDs"]) * 1
    score += len(detected_data["API Keys"]) * 4
    score += len(detected_data["Passwords"]) * 4
    score += len(detected_data["Confidential Business Information"]) * 2

    if score <= 5:
        return "🟢 Low Risk"

    elif score <= 12:
        return "🟡 Medium Risk"

    else:
        return "🔴 High Risk"