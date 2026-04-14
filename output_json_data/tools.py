from openai import OpenAI
from dotenv import load_dotenv
import time
import json
import os
load_dotenv()
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
def json_output(text : str , retries = 3):
    retry = 0
    while retry < retries:
        try:
            messages = [
                {"role":"system","content":"""
你是专业情感分析助手,只输出JSON,不要任何多余内容。
输出格式：
{
  "sentiment": "",
  "reason": ""
}
                 """},
                 {"role":"user","content":text}
            ]
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                response_format={"type":"json_object"}
            )
            result = response.choices[0].message.content
            data=json.loads(result)
            return f"{data},\n{data['sentiment']}"
        except Exception as e:
            retry += 1
            print(f"调用失败，原因如下:\n{e}")
            print(f"这是第{retry}次尝试")
            wait_time = retry*1.5
            time.sleep(wait_time)
    return {"error":"API调用失败请重试"}