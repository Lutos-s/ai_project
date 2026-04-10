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
st.caption("支持总结 / 翻译 / 改写 / 关键词提取")
col1 , col2 = st.columns(2)
with col1:
    text = st.text_area("请输入文本")
option = st.selectbox(
    "选择功能",
    ["总结","翻译","改写","关键词"]
)
if st.button("执行"):
    if option == "总结":
        with st.spinner("AI思考中..."):
            reslut = summarize(text)
    if option == "翻译":
        with st.spinner("AI思考中..."):
            reslut = translate(text)
    if option == "关键词":
        with st.spinner("AI思考中..."):
            reslut = keywords(text)
    if option == "改写":
        with st.spinner("AI思考中..."):
            reslut = rewrite(text)
    with col2:
        st.write(f"输出区域\n{reslut}")