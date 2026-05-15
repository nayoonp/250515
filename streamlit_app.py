import streamlit as st

st.set_page_config(
    page_title="자기소개 페이지",
    page_icon="👋",
    layout="centered",
)

st.title("👋 안녕하세요!")

st.markdown(
    "저는 **박나윤**입니다.\n\n"
    "청주교육대학교 교육학과 1학년입니다."
)

st.header("📌 소개")
st.write(
    "- 청주교육대학교 교육학과 1학년\n"
    "- 관심 분야: 동기들과 놀기\n"
    "- 지금 만들고 있는 프로젝트나 취미: 처음으로 코딩해보는 중"
)

st.header("💼 경력 / 활동")
st.write(
    "1. 파이썬 해봄\n"
    "2. 지금 하고 있는 일: 현대 수학의 융합적 이해 수업에서 스트림릿을 해보는 중"
)

st.header("📫 연락처")
st.write(
    "- 이메일: nayoonzzang06@gmail.com\n"
    "- 깃허브: https://github.com/yourname\n"
)

st.info("이 부분은 나중에 자세한 내용으로 바꿔서 사용하시면 됩니다.")
