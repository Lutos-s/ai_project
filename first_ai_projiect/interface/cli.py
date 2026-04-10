import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent
sys.path.append(str(ROOT_DIR))
from app.tools.summarize  import summarize
from app.tools.translate import translate
from app.tools.rewrite import rewrite
from app.tools.keywords import keywords
import streamlit as st
st.title("AI文本总结工具")
text = st.text_area("请输入文本")
option = st.selectbox(
    "选择功能",
    ["总结","翻译","改写","关键词"]
)
if st.button("执行"):
    if option == "总结":
        reslut = summarize(text)
    if option == "翻译":
        reslut = translate(text)
    if option == "关键词":
        reslut = keywords(text)
    if option == "改写":
        reslut = rewrite(text)
    st.write(reslut)