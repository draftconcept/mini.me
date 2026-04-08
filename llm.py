from openai import OpenAI
import config

client = OpenAI(
    base_url=config.BASE_URL,
    api_key=config.API_KEY
)

def chat(messages):
    response = client.chat.completions.create(
        model=config.MODEL,
        messages=messages
    )
    return response.choices[0].message.content