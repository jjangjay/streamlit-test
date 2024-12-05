import streamlit as st


st.title('st.from')


st.header('1. "with" 표기법 사용 예시')
st.subheader('커피 머신')
with st.form('my_form'):
    st.subheader('커피 주문하기')
    coffee_bean_val = st.selectbox('커피콩', ['아라비카', '로부스타'])
    coffee_roast_val = st.selectbox('로스팅', ['라이트', '미디엄', '다크'])
    brewing_val = st.selectbox('추출 방법', ['에어로프레스', '드립', '프렌치 프레스', '모카 포트', '샤이폰'])
    serving_type_val = st.selectbox('서빙 형식', ['핫', '아이스', '프라페',])
    milk_val = st.select_slider('우유', ['없음', '낮음', '보통', '높음'])
    owncup_val = st.selectbox('자신의 컵 가져오기')
    submitted = st.form_submit_button('제출')  # 모든 양식은 제출 버튼을 가져야 함
if submitted:
    st.markdown(f'''
    - 커피콩: {coffee_bean_val}
    - 커피 로스팅: {coffee_roast_val}
    - 추출 방법: {brewing_val}
    - 서빙 형식: {serving_type_val}
    - 우유: {milk_val}
    - 자신의 컵 가져오기: {owncup_val}
    ''')
else:
    st.write('주문하세요!')
