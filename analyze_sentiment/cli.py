from tool import Analyze_sentiment
import streamlit as st
st.title("情感分析工具")
text=st.text_area("请输入句子")
if st.button("开始分析"):
    with st.spinner("ai思考中..."):
        result = Analyze_sentiment(text=text)
    st.write(result)