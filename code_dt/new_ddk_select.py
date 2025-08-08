import streamlit as st
from streamlit_chat import message
order_steps = [
    {
        "name": "spicy", 
        "title": "맵기 선택", 
        "options": ['부상', '부상+', '중상', '혼수상태', '사망']
    },
    {
        "name": "menu", 
        "title": "떡볶이 선택", 
        "options": ['응떡2-3인분', '반반2-3인분', '응오2-3인분', '떡볶이1-2인분']
    },
    {
        "name": "topping1", 
        "title": "기본 토핑 1", 
        "options": ['수제비(추천)', '메추리알', '비엔나', '고구마떡', '물만두(추천)'],
        "condition": lambda session: session.get("menu") == '떡볶이1-2인분'
    },
    {
        "name": "topping2", 
        "title": "기본 토핑 2", 
        "options": ['수제비(추천)', '메추리알', '비엔나', '고구마떡', '물만두(추천)'],
        "condition": lambda session: session.get("menu") == '떡볶이1-2인분'
    },
    {
        "name": "extra23", 
        "title": "추가 토핑", 
        "options": ['토핑추가 X','수제비 (10개)','집채어묵 (3개)','물만두 (6개)','고구마떡 (6개)','비엔나소시지 (6개)','메추리알 (6개)','계란 (2개)','떡 추가','오뎅 추가']
    },
    {
        "name": "extra12", 
        "title": "추가 토핑", 
        "options": ['토핑추가 X','수제비 (10개)','집채어묵 (3개)','물만두 (6개)','고구마떡 (6개)','비엔나소시지 (6개)','메추리알 (6개)','계란 (2개)'],
        "condition": lambda session: session.get("menu") == '떡볶이1-2인분'
    },
    {
        "name": "cheese", 
        "title": "치즈 선택", 
        "options": ['치즈추가 X','치즈 1개','치즈 2개','치즈 3개','치즈 4개']
    },
]
def ddk_select():
    current_order = st.session_state.get("order", 0)

    for i, step in enumerate(order_steps):
        # 조건이 있다면 검사
        if "condition" in step and not step["condition"](st.session_state):
            continue
        if current_order != i:
            continue

        st.session_state.messages.append({"role": "assistant", "content": step["title"]})
        st.chat_message("assistant").write(step["title"])
        selected = st.selectbox(step["title"], ['선택해주세요'] + step["options"], key=f"select_{step['name']}")

        if selected != '선택해주세요':
            st.session_state[step["name"]] = selected
            st.write(f"{selected} 선택됨!")
            st.session_state.messages.append({"role": "assistant", "content": f"{selected} 선택"})
            st.chat_message("assistant").write(f"{selected} 선택")

            st.session_state.order = current_order + 1
            st.rerun()
        break
