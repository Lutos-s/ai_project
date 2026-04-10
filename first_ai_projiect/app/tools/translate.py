from app.llm.client import chat
from app.prompts.templates import TRANSLATE
def translate(text):
    prompt = TRANSLATE.format(text=text)
    messages =[
        {"role":"system","content":"你非常擅长英文翻译"},
        {"role":"user","content":prompt}
    ]
    return chat(messages)