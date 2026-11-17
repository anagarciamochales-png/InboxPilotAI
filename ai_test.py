from openai import OpenAI
from config import REQUESTY_API_KEY

client = OpenAI(
    api_key=REQUESTY_API_KEY,
    base_url="https://router.requesty.ai/v1"
)

email_text = """
We enjoyed speaking with you and would like
to move forward with the next stage of the
selection process.
"""

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

print(response.choices[0].message.content)