from app.llm.client import chat
from app.prompts.templates import KEYWORDS
def keywords(text):
    prompt = KEYWORDS.format(text=text)
    messages =[
        {"role":"system","content":"你非常擅长提取关键词"},
        {"role":"user","content":prompt}
    ]
    return chat(messages)