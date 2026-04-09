from app.llm.client import chat
from app.prompts.templates import SUMMARIZE
def summarize(text):
    prompt = SUMMARIZE.format(text=text)
    messages = [
        {"role":"user","content":prompt}
    ]
    return chat(messages)