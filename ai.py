import os
import requests
import openai
from openai import OpenAI
import streamlit as st
# from dotenv import load_dotenv
# load_dotenv()

# OpenAI API 키
# Openai 스트림릿 업로드용
client = OpenAI(
    api_key = st.secrets["api_key"]
)

# # 공식 문서
# client = OpenAI(
#   organization='org-bNGRXqy4I0CDJRyM07FYlISo',
# )

# # API 요청을 보낼 엔드포인트
# url = "https://api.openai.com/v1/endpoint"

# # 요청 헤더 설정
# headers = {
#     "Authorization": f"Bearer {openai_api_key}"
# }

# # HTTP GET 요청 보내기
# response = requests.get(url, headers=headers)

# # 응답 확인
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Error:", response.status_code)

# client = OpenAI()

# gpt-3.5-turbo
def gpt_turbo(user_input):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a competent Korean language secretary who solves everything."},
        {"role": "user", "content": f"{user_input}"}
    ]
    )
    response = completion.choices[0].message
    answer = completion.choices[0].message.content
    print(response)
    st.write(answer)
    return answer