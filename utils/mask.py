def mask_value(category, value):

    if category == "Emails":

        name, domain = value.split("@")
        return name[:2] + "****@" + domain

    elif category == "Phone Numbers":

        return value[:2] + "******" + value[-2:]

    elif category == "PAN Numbers":

        return value[:3] + "****" + value[-3:]

    elif category == "Aadhaar Numbers":

        return "XXXX XXXX " + value[-4:]

    elif category == "Credit Card Numbers":

        digits = value.replace(" ", "")
        return "XXXX XXXX XXXX " + digits[-4:]

    elif category == "Bank Account Numbers":

        return "XXXXXX" + value[-4:]

    elif category == "API Keys":

        return value[:6] + "************"

    elif category == "Passwords":

        return "********"

    else:

        return value