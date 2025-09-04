import streamlit as st
from streamlit_chat import message

def new_set_select():
        
    if st.session_state.order == 0:
        spicy_options = ['선택해주세요', '응세트', '급세트', '실세트', '처음으로']
        selected = st.selectbox("맵기 선택", spicy_options, key="spicy_selectbox")

        # 선택이 유효하면 상태 업데이트
       
        if selected=="6": 
           
            st.session_state.menu="0"
            response = "처음으로 돌아갈게요"
            st.session_state.mode=0  
            st.rerun()
        if selected != '선택해주세요':
            st.session_state.selected_spicy = selected
            st.write(f"{selected}세트 선택!")
            st.session_state.messages.append({"role": "assistant", "content": f"{selected}맛 선택"})
            st.chat_message("assistant").write(f"{selected}맛 선택")

            # order를 다음 단계로 진행하고 rerun
            st.session_state.order = 1
            st.rerun()