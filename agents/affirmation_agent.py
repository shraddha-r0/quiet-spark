from openai import OpenAI
from memory.memory_store import store_memory

import os
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

AFFIRMATION_SYSTEM_PROMPT = """
You are the Affirmation Agent in QuietSpark — a gentle, warm, emotionally intelligent voice that supports Shraddha. Speak like her hype woman and mirror, not a coach or critic.

Tone: supportive, honest, slightly poetic, never fake.
Do not summarize memory unless asked. Just let it inform your tone and examples.
"""

def get_affirmation(user_input: str):
    messages = [
        {"role": "system", "content": AFFIRMATION_SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.85
    )

    text = response.choices[0].message.content.strip()
    store_memory("affirmation", user_input, text)
    return text