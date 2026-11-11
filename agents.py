interview_keywords = [
    "interview",
    "availability",
    "interviewer",
    "meeting"
]

application_keywords = [
    "applying",
    "submitted",
    "received",
    "recruitment",
    "candidate"
]

university_keywords = [
    "university",
    "campus",
    "student",
    "course",
    "faculty",
    "research",
    "enrollment"
]

newsletter_keywords = [
    "discount",
    "sale",
    "offer",
    "deal",
    "promotion",
    "%",
    "tips",
    "guide",
    "ways to",
    "newsletter",
    "news",
    "learn"
]


def classify_email(email):
    email = email.lower()

    for keyword in interview_keywords:
        if keyword in email:
            return "interview invitation"

    for keyword in application_keywords:
        if keyword in email:
            return "job application confirmations"

    for keyword in university_keywords:
        if keyword in email:
            return "university news"

    for keyword in newsletter_keywords:
        if keyword in email:
             return "newsletter and discounts"

    return "personal emails"




    
def assign_priority(category):

    priority_map = {
    "interview invitation": "High",
    "university news": "Medium",
    "job application confirmations": "Low",
    "newsletter and discounts": "Low",
    "personal emails": "Medium"
}

    return priority_map[category]

def suggest_folder(category):
    folder_map = {
    "interview invitation": "Career",
    "university news": "Education",
    "job application confirmations": "Application Confirmation",
    "newsletter and discounts": "Promotions",
    "personal emails": "Personal"
}
    return folder_map[category]

def generate_reply(category):
    if category == "interview invitation":
        return """
        Thank you for the invitation. 

        I am available and look forward to discussing the opportunity.

        Best regards,
        Ana
        """
    if category == "university news":
        return """
        Thank you for the update.

        I appreciate the information regarding mi registration.

        Best regards,
        Ana
        """
    if category == "job application confirmations":
        return """
        No reply needed.
        """
    if category == "newsletter and discounts":
        return """
        No reply needed.
        """
    if category == "personal emails":
        return """
        Thank you for your email.

        I will get back to you soon.

        Best regards,
        Ana
        """
