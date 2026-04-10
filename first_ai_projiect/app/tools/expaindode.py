from app.llm.client import chat
from app.prompts.templates import EXPAINCODE
def expaincode(text):
    prompt = EXPAINCODE.format(text)
    messages = [
        {"role":"system","content":"你是一名专业程序员"},
        {"role":"user","content":prompt}
    ]
    return chat(messages)