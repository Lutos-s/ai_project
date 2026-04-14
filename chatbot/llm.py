from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
cli = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
def chat(messages):
    response = cli.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    return response.choices[0].message.content