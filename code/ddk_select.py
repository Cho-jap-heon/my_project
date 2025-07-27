import streamlit as st
from streamlit_chat import message
def ddk_select():
        
    if st.session_state.order == 0:
        spicy_options = ['선택해주세요', '부상', '부상+', '중상', '혼수상태', '사망']
        selected = st.selectbox("맵기 선택", spicy_options, key="spicy_selectbox")

        # 선택이 유효하면 상태 업데이트
        if selected != '선택해주세요':
            st.session_state.selected_spicy = selected
            st.write(f"{selected}맛 선택!")
            st.session_state.messages.append({"role": "assistant", "content": f"{selected}맛 선택"})
            st.chat_message("assistant").write(f"{selected}맛 선택")

            # order를 다음 단계로 진행하고 rerun
            st.session_state.order = 1
            st.rerun()

    # 떡볶이 선택 단계
    elif st.session_state.order == 1:
        response = "이번엔 떡볶이를 선택해주세요."
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
        menu_options = ['선택해주세요', '응떡2-3인분', '반반2-3인분', '응오2-3인분', '떡볶이1-2인분']
        selected = st.selectbox("맵기 선택", menu_options, key="menu_selectbox")
        if selected != '선택해주세요':
            if selected == '떡볶이1-2인분':
                st.session_state.order = 1.1
                st.rerun()
            st.session_state.selected_menu = selected
            st.write(f"{selected}메뉴 선택!")
            st.session_state.messages.append({"role": "assistant", "content": f"{selected}메뉴 선택"})
            st.chat_message("assistant").write(f"{selected}메뉴 선택")

            # order를 다음 단계로 진행하고 rerun
            st.session_state.order = 2
            st.rerun()
    elif st.session_state.order == 1.1:
        response = "이번엔 1-2인분 떡볶이의 첫번째 기본 토핑을 선택해주세요."
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
        topping1_options = ['선택해주세요', '수제비(추천)', '메추리알', '비엔나', '고구마떡','물만두(추천)']
        selected1 = st.selectbox("토핑 선택", topping1_options, key="tp1_selectbox")
        
        if selected1 != '선택해주세요':
            
            st.session_state.selected_topping1 = selected1
            st.write(f"{selected1}토핑1 선택!")
            st.session_state.messages.append({"role": "assistant", "content": f"{selected1}토핑1 선택"})
            st.chat_message("assistant").write(f"{selected1}토핑1 선택")
            st.session_state.order = 1.2
            st.rerun()
    elif st.session_state.order == 1.2:
        response = "이번엔 1-2인분 떡볶이의 두번째 기본 토핑을 선택해주세요."
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
        topping2_options = ['선택해주세요', '수제비(추천)', '메추리알', '비엔나', '고구마떡','물만두(추천)']
        selected2 = st.selectbox("토핑 선택", topping2_options, key="tp2_selectbox2")
        
        if selected2 != '선택해주세요':
            
            st.session_state.selected_topping2 = selected2
            st.write(f"{selected2}토핑2 선택!")
            st.session_state.messages.append({"role": "assistant", "content": f"{selected2}토핑2 선택"})
            st.chat_message("assistant").write(f"{selected2}토핑2 선택")
            st.session_state.order = 2.1
            st.rerun()
    elif st.session_state.order == 2:
        response = "이번엔 떡볶이의 추가 토핑을 선택해주세요."
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
        menu_options = ['선택해주세요','토핑추가 X','수제비 (10개)','집채어묵 (3개)','물만두 (6개)','고구마떡 (6개)','비엔나소시지 (6개)','메추리알 (6개)','계란 (2개)','떡 추가','오뎅 추가']
        selected = st.selectbox("추가토핑 선택", menu_options, key="ext_selectbox")
        if selected != '선택해주세요':
            if selected == '토핑추가 X':
                st.session_state.order = 3
                st.rerun()
            st.session_state.selected_menu = selected
            st.write(f"{selected}메뉴 선택!")
            st.session_state.messages.append({"role": "assistant", "content": f"{selected}메뉴 선택"})
            st.chat_message("assistant").write(f"{selected}메뉴 선택")

            # order를 다음 단계로 진행하고 rerun
            st.session_state.order = 3
            st.rerun()    
    elif st.session_state.order == 2.1:
        response = "이번엔 1-2인분 떡볶이의 추가 토핑을 선택해주세요."
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
        menu_options = ['선택해주세요','토핑추가 X','수제비 (10개)','집채어묵 (3개)','물만두 (6개)','고구마떡 (6개)','비엔나소시지 (6개)','메추리알 (6개)','계란 (2개)']
        selected = st.selectbox("추가토핑 선택", menu_options, key="ex1t_selectbox")
        if selected != '선택해주세요':
            if selected == '토핑추가 X':
                st.session_state.order = 3
                st.rerun()
            st.session_state.selected_menu = selected
            st.write(f"{selected}메뉴 선택!")
            st.session_state.messages.append({"role": "assistant", "content": f"{selected}메뉴 선택"})
            st.chat_message("assistant").write(f"{selected}메뉴 선택")

            # order를 다음 단계로 진행하고 rerun
            st.session_state.order = 3
            st.rerun()    
    elif st.session_state.order == 3:
        response = "치즈선택. 1개당 3500원입니다."
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
        cs_options = ['선택해주세요','치즈추가 X','치즈 1개','치즈 2개','치즈 3개','치즈 4개']
        selected = st.selectbox("추가치즈 선택", cs_options, key="cs_selectbox")
        if selected != '선택해주세요':
            if selected == '치즈추가 X':
                st.session_state.order = 4
                st.rerun()
            st.session_state.selected_menu = selected
            st.write(f"{selected}메뉴 선택!")
            st.session_state.messages.append({"role": "assistant", "content": f"{selected}치즈 선택"})
            st.chat_message("assistant").write(f"{selected}메뉴 선택")

            # order를 다음 단계로 진행하고 rerun
            st.session_state.order = 4
            st.rerun()    
    elif st.session_state.order == 4:
        response = "떡볶이 선택 완료. 주문을 저장할게요."
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
        st.rerun()    