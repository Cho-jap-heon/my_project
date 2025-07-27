
import streamlit as st
from streamlit_chat import message
def reference():
    if query := st.chat_input("1: 커플 2: 두명 3: 패밀리 4: 단체  5: 솔로  6: 처음으로 ") : # 사용자의입력과답변기록과출력
        st.session_state.messages.append({"role": "user", "content": query})
        st.chat_message("user").write(query)
        if query=="메뉴" or query=="1":
            
            response = "1-2인분 세트. "
            
        elif query=="2":
            
            response ="응세트"
        elif query=="3": 
            
            response = "급세트"
        elif query=="4": 
           
            response = "4명당 실세트"
        elif query=="5": 
           
            response = "1-2인분 떡볶이"    
        elif query=="6": 
           
            st.session_state.menu="0"
            response = "처음으로 돌아갈게요"
            st.session_state.mode=0  
            st.rerun()
        else :
            response ="다시 말씀해주세요"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
