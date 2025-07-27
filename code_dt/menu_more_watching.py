import streamlit as st
from streamlit_chat import message
def menu_more_watching():
    if st.session_state.menu == "전체":    #메뉴 출력
        st.image("IMG_9213.jpeg")
    elif st.session_state.menu == "떡볶이":
        st.image("main.png")
        response = "1-2인분 떡볶이는 토핑 5개중 2개 선택해주셔야 합니다. \n(비엔나, 고구마떡, 메추리알, 수제비, 물만두) "
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
    elif st.session_state.menu == "사이드":
        st.image("side.png")
    elif st.session_state.menu == "주먹밥":
        st.image("rice.png")
    elif st.session_state.menu == "튀김":
        st.image("fry.png")
    elif st.session_state.menu == "모두":
        st.image("fry.png")
        st.image("side.png")
        st.image("rice.png")
        st.image("main.png")