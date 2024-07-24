import streamlit as st
st.title('나의 첫 번째 웹 서비스!')
name = st.text_input('이름을 입력해주세요')
menu = st.selectbox('좋아하는 디저트를 선택하세요!', ['망고 빙수', '마카롱', '크레페'])
if st.button('인사말 생성'):
  st.write(f'안녕하세요 {name}님! 당신이 좋아하는 디저트는 {menu}이군요 너무 맛잇겟어용 환영합니다 *^^*')
