import streamlit as st

from print_msg import print_msg
from ai import gpt_turbo



with st.form("top_form"):
        user_input = st.text_input("무엇을 도와드릴까요?")           
        submit = st.form_submit_button("Submit") 
if submit and user_input:
    st.write(user_input + '에 대해 알려드리겠습니다')
    print(user_input)
    with st.spinner('Wait for it...'):     
        gpt_turbo(user_input)
