from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
def Sumarize(text):
    res = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role":"system","content":"你是一个关键词提取助手，输出简洁关键词"},
            {"role":"user","content":"今天天气真好"},
            {"role":"assistant","content":"关键词:天气"},
            {"role":"user","content":"我喜欢打篮球和足球"},
            {"role":"assistant","content":"关键词:篮球，足球"},
            {"role":"user","content":text}
        ]
    )
    return res.choices[0].message.content