from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
def Analyze_sentiment(text):
    prompt=f"""
    请分析情感,并按JSON输出:
    {{
    "sentiment": "",
    "reason": ""
    }}

    文本：{text}
    """
    res = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role":"system","content":"你是一个情感分析师"},
            {"role":"user","content":"今天天气真好"},
            {"role":"assistant","content":f"""
            {{
            "sentiment": "轻松、愉悦、舒畅",
            "reason": "1、人在烦躁、低落、忙碌焦虑时,通常没心思留意天气好不好,只有心情放松时,才会注意到阳光、微风这些细节。2、这句话是纯粹的正面评价,没有吐槽、没有无奈,说明你当下没有烦心事,心态平和,甚至想出门走走、享受一下。3、很多人会用天气映射心境 ——“天气好” 其实也在悄悄说 “我今天状态不错”。"
            }}"""},
            {"role":"user","content":prompt}
        ]
    )
    return res.choices[0].message.content