import requests
from django.conf import settings
from django.http import JsonResponse
from openai import OpenAI

OPENAI_KEY = getattr(settings, 'OPEN_API_KEY',None)
client = OpenAI(api_key=OPENAI_KEY)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

