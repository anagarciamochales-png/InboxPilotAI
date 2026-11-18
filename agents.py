from openai import OpenAI
import streamlit as st
import json
from datetime import date
from pathlib import Path


try:
    from config import REQUESTY_API_KEY
except ImportError:
    REQUESTY_API_KEY = st.secrets["REQUESTY_API_KEY"]

MAX_DAILY_REQUESTS = 100

COUNTER_FILE = Path("request_counter.json")


def can_make_ai_request(is_admin=False):
    # Admin bypass
    if is_admin:
        return True
    
    today = str(date.today())

    if not COUNTER_FILE.exists():
        data = {"date": today, "count": 0}
        with open(COUNTER_FILE, "w") as f:
            json.dump(data, f)

    with open(COUNTER_FILE, "r") as f:
        data = json.load(f)

    # Reset every day
    if data["date"] != today:
        data = {"date": today, "count": 0}

        with open(COUNTER_FILE, "w") as f:
            json.dump(data, f)

    return data["count"] < MAX_DAILY_REQUESTS

def register_ai_request():
    today = str(date.today())

    if COUNTER_FILE.exists():
        with open(COUNTER_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {"date": today, "count": 0}

    if data["date"] != today:
        data = {"date": today, "count": 0}

    data["count"] += 1

    with open(COUNTER_FILE, "w") as f:
        json.dump(data, f)

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

def ai_classify_email(email_text, is_admin=False):
    # Check daily limit BEFORE calling the AI
    if not can_make_ai_request(is_admin):
        return "AI_LIMIT_REACHED"

    client = OpenAI(
        api_key=REQUESTY_API_KEY,
        base_url="https://router.requesty.ai/v1"
    )

    response = client.chat.completions.create(
        model="novita/ling-3.1-flash",
        messages=[
            {
                "role": "user",
                "content": f"""
Classify this email into exactly one category:

- interview invitation
- university news
- job application confirmations
- newsletter and discounts
- personal emails

Return ONLY the category name.

Email:

{email_text}
"""
            }
        ]
    )
    # Register usage only after a successful request
    if not is_admin:
        register_ai_request()

    return response.choices[0].message.content.strip()

def ai_generate_reply(email_text, is_admin=False):
    if not can_make_ai_request(is_admin):
        return "AI_LIMIT_REACHED"
    
    client = OpenAI(
        api_key=REQUESTY_API_KEY,
        base_url="https://router.requesty.ai/v1"
    )

    response = client.chat.completions.create(
        model="novita/ling-3.1-flash",
        messages=[
            {
                "role": "user",
                "content": f"""
Write a professional email reply.

Requirements:
- Professional tone
- Accept the interview invitation
- Be concise
- Include greeting
- Include closing
- Sign with:

Ana García Mochales Ortiz

Email:

{email_text}
"""
            }
        ]
    )
    if not is_admin:
        register_ai_request()

    return response.choices[0].message.content.strip()

    
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
