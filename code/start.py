import streamlit as st
from streamlit_chat import message
def start():
    if query := st.chat_input("무엇을 도와드릴까요? 1: 메뉴 2: 주문 3:추천 4:초기화 ") : # 사용자의입력과답변기록과출력
        st.session_state.messages.append({"role": "user", "content": query})
        st.chat_message("user").write(query)
        if query=="메뉴" or query=="1":
            st.session_state.menu="전체"
            st.session_state.mode =1
            response = "전체 메뉴판입니다."
            st.rerun()
            
        elif query=="2":
            st.session_state.menu=0
            st.session_state.mode =2
            response ="주문을 도와드릴게요"
            st.rerun()
        elif query=="3": 
            st.session_state.menu=0
            st.session_state.mode =3
            response = "몇명이서 식사하시나요?"
            st.rerun()
        elif query=="4": 
            st.session_state.menu=0
            st.session_state["messages"] = []
            st.rerun()
        else :
            response ="다시 말씀해주세요"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)