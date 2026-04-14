import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent
sys.path.append(str(ROOT_DIR))
import streamlit as st
from llm import chat
from memmerory import ChatMemory
from teampleas import PYTHON,ENGLISH,INTERVIEWER
st.title("AI-CHAT-bot")
option = st.selectbox(
    "选择功能",
    ["Python","English","Interviewer"]
)
if option == "Python":
    system_prompt=PYTHON
elif option == "English":
    system_prompt=ENGLISH
elif option == "Interviewer":
    system_prompt=INTERVIEWER
if "memory" not in st.session_state or st.session_state.role != option:
    st.session_state.memory = ChatMemory(system_prompt=system_prompt)
    st.session_state.role = option
memory = st.session_state.memory

for msg in memory.get()[1:]:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

user_input=st.chat_input("有问题,尽管问")
if user_input:
    st.chat_message("user").write(user_input)
    memory.add_user(user_input=user_input)
    reply = chat(memory.get())
    st.chat_message("assistant").write(reply)
    memory.add_assistant(reply)
if st.button("清空记忆"):
    st.session_state.memory = ChatMemory(system_prompt=system_prompt)