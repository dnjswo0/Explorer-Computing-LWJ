import streamlit as st
import pandas as pd
import numpy as np

# 탭 생성
st.title("10주차 과제")
st.caption("자기소개와 수업 시간표")
tab1, tab2 = st.tabs(["자기소개", "수업 시간표"])

with tab1:
    st.markdown("# 나의 소개 페이지")
    st.markdown("## 자기소개")
    st.text("안녕하세요, 제 이름은 이원재입니다.")
    st.markdown("저는 서울대학교 사회학과에 재학중이며, \n프로그래밍과 데이터 분석/시각화에 관심이 많아 컴퓨팅 탐색 과목을 수강중입니다.")

    st.markdown("## 좋아하는 것")
    st.text("저는 음악을 듣는 것을 매우 좋아합니다.")
    st.markdown("최근에 많이 듣는 음악은 [Jesus of Suburbia - Green day](https://youtu.be/vH0mb_Vbq7g?si=bfB0pObVgQACxaeN)입니다.")

    st.markdown("## 앞으로의 목표")
    st.text("앞으로 다양한 프로젝트를 진행하면서 프로그래밍 실력을 키우고 싶습니다.")
    st.caption("제가 좋아하는 파이썬 코드 예시")
    st.code("for i in range(3) :\n print('Hello, Streamlit!')", language = "python")
    st.caption("피타고라스 정리")
    st.latex("a^2 + b^2 = c^2")

with tab2:
    data = {"요일": ["월", "화", "수", "목", "금"], "1교시": ["통계학", "글쓰기", "통계학", "컴퓨팅", "컴퓨팅"], "2교시" : ["전공", "예술", "", "글쓰기", "전공"]}
    df = pd.DataFrame(data)

    st.markdown("# 📚 나의 수업 시간표")
    st.markdown("## 정적 시간표(st.table)")
    st.table(df)

    st.markdown("## 수업 정보(st.json)")
    computing_data = {"요일" : "금", "학점" : "3"}
    writing_data = {"요일" : ["화", "목"], "학점" : "2"}
    json_data = {"컴퓨팅 탐색" : computing_data, "대학글쓰기" : writing_data}
    st.json(json_data)

    st.markdown("## 이번 학기 요약(st.metric)")
    st.metric(label="수강 과목 수", value="6")
    st.metric(label="총 학점", value="17", delta="+3")
