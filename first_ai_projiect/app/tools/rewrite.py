from app.llm.client import chat
from app.prompts.templates import REWRITE
def rewrite(text):
    prompt = REWRITE.format(text=text)
    messages = [
        {"role":"system","content":"你非常擅长改写句子"},
        {"role":"user","content":prompt}
    ]
    return chat(messages)