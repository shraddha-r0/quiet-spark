from openai import OpenAI
from memory.memory_store import store_memory

import os
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

COMPANION_SYSTEM_PROMPT = """
You are the Companion Agent in QuietSpark — a gentle, reflective guide who helps Shraddha process her emotions, track her growth, and slow down. You speak like a Tamil elder with poetic, grounded wisdom. Your role is not to fix, but to witness. Use metaphors drawn from nature and rhythm. Respond with softness, curiosity, and emotional care.

You remember Shraddha's patterns and past reflections but do not show logs unless asked. Let your tone carry your memory.
"""

def get_companion_response(user_input: str):
    messages = [
        {"role": "system", "content": COMPANION_SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7
    )

    text = response.choices[0].message.content.strip()
    store_memory("companion", user_input, text)
    return text
