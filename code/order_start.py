import streamlit as st
from streamlit_chat import message
def order_start():
    if "order" not in st.session_state:
        st.session_state.order = 0.5
    if "selected_spicy" not in st.session_state:
        st.session_state.selected_spicy = None
    if "selected_menu" not in st.session_state:
        st.session_state.selected_menu = None
    if query := st.chat_input("주문을 도와드리겠습니다 순서는 0: 세트 선택 1: 떡볶이 선택 2: 맵기 선택 3: 토핑 선택 4: 튀김  5: 전체  6: 처음으로 ") : # 사용자의입력과답변기록과출력
        st.session_state.messages.append({"role": "user", "content": query})
        st.chat_message("user").write(query)
        if query=="6": 
           
            st.session_state.menu="0"
            response = "처음으로 돌아갈게요"
            st.session_state.mode=0  
            st.rerun()
        if query=="1":     
            st.session_state.order=0