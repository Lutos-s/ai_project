import few_shot
import streamlit as st
st.title("关键词提取器")
text = st.text_area("输入文本")
result=few_shot.Sumarize(text=text)
if st.button("总结"):
    st.write(result)