import streamlit as st
from streamlit_chat import message
def menu_watching() :
    if query := st.chat_input("메뉴를 더 자세하게 보여드릴까요?  1: 떡볶이 2: 주먹밥 3:사이드 4: 튀김  5: 전체  6: 처음으로 ") : # 사용자의입력과답변기록과출력
        st.session_state.messages.append({"role": "user", "content": query})
        st.chat_message("user").write(query)
        if query=="메뉴" or query=="1":
            st.session_state.menu="떡볶이"
            st.session_state.mode =1
            response = "떡볶이 메뉴판입니다. "
            
        elif query=="2":
            st.session_state.mode =1
            st.session_state.menu="주먹밥"
            response ="주먹밥 메뉴판입니다"
        elif query=="3": 
            st.session_state.mode =1
            st.session_state.menu="사이드"
            response = "사이드 메뉴판입니다"
        elif query=="4": 
            st.session_state.mode =1
            st.session_state.menu="튀김"
            response = "튀김 메뉴판입니다"
        elif query=="5": 
            st.session_state.mode =1
            st.session_state.menu="모두"
            response = "전체 메뉴판입니다"    
        elif query=="6": 
           
            st.session_state.menu="0"
            response = "처음으로 돌아갈게요"
            st.session_state.mode=0  
            st.rerun()
        else :
            response ="다시 말씀해주세요"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)