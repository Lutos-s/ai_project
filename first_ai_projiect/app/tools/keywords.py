from app.llm.client import chat
from app.prompts.templates import KEYWORDS
def keywords(text):
    prompt = KEYWORDS.format(text=text)
    messages =[
        {"role":"user","content":prompt}
    ]
    return chat(messages)