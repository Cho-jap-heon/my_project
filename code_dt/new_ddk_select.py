import streamlit as st
from streamlit_chat import message
order_steps = [
    {
        "name": "맵기", 
        "title": "맵기 선택", 
        "options": ['부상', '부상+', '중상', '혼수상태', '사망']
    },
    {
        "name": "떡볶이", 
        "title": "떡볶이 선택", 
        "options": ['응떡2-3인분', '반반2-3인분', '응오2-3인분', '떡볶이1-2인분']
    },
    {
        "name": "떡볶이12", 
        "title": "떡볶이_업그레이드", 
        "options": ['기본 떡볶이', '로제 떡볶이'],
        "condition": lambda session: session.get("떡볶이") == '떡볶이1-2인분'
    },
    {
        "name": "떡볶이23", 
        "title": "떡볶이_업그레이드", 
        "options": ['기본 떡볶이', '로제 떡볶이','후추꾸덕볶이','크림카레떡볶이'],
        "condition": lambda session: session.get("떡볶이") != '떡볶이1-2인분'
    },
    {
        "name": "기본토핑1", 
        "title": "기본 토핑 1", 
        "options": ['수제비(추천)', '메추리알', '비엔나', '물만두(추천)'],
        "condition": lambda session: session.get("떡볶이") == '떡볶이1-2인분'
    },
    {
        "name": "기본토핑2", 
        "title": "기본 토핑 2", 
        "options": ['수제비(추천)', '메추리알', '비엔나', '물만두(추천)'],
        "condition": lambda session: session.get("떡볶이") == '떡볶이1-2인분'
    },
    {
        "name": "2-3인분_추가토핑", 
        "title": "추가 토핑23", 
        "options": ['토핑추가 X','수제비 (10개)','집채어묵 (3개)','물만두 (6개)','비엔나소시지 (6개)','메추리알 (6개)','계란 (2개)','떡 추가','오뎅 추가'],
        "multi": True,
        "condition": lambda session: session.get("떡볶이") != '떡볶이1-2인분'
    },
    {
        "name": "1-2인분_추가토핑", 
        "title": "추가 토핑12", 
        "options": ['토핑추가 X','수제비 (10개)','집채어묵 (3개)','물만두 (6개)','비엔나소시지 (6개)','메추리알 (6개)','계란 (2개)'],
        "condition": lambda session: session.get("떡볶이") == '떡볶이1-2인분',
        "multi": True
    },
    {
        "name": "치즈", 
        "title": "치즈 선택", 
        "options": ['치즈추가 X','치즈 1개','치즈 2개','치즈 3개','치즈 4개']
    },
    
]

def new_ddk_select():
    
    current_order = st.session_state.get("order", 0)
    #order_steps=[]
    for i, step in enumerate(order_steps):
        # 조건이 있다면, 조건에 맞지 않으면 그냥 건너뜀
        if "condition" in step and not step["condition"](st.session_state):
            continue

        # 현재 순서가 아닌 step이면 건너뜀
        if i != current_order:
            continue
        
        # 메시지 출력
        st.session_state.messages.append({"role": "assistant", "content": step["title"]})
        st.chat_message("assistant").write(step["title"])
        # 선택지 표시
        if step.get("multi", False):
            
            selected = st.multiselect(step["title"], step["options"],key=f"select_{i}_{step['name']}")
            
            if st.button("✅ 선택 완료", key=f"confirm_{step['name']}") and selected:
                st.session_state[step["name"]] = selected
                #st.write(f"{selected} 선택됨!")
                st.session_state.messages.append({"role": "assistant", "content": f"{selected} 선택"})
                st.chat_message("assistant").write(f"{selected} 선택")

                st.session_state["extra"] = selected

                # 다음 조건 맞는 step 찾기
                for j in range(i + 1, len(order_steps)):
                    if "condition" not in order_steps[j] or order_steps[j]["condition"](st.session_state):
                        st.session_state.order = j
                        break
                else:
                    st.session_state.order = len(order_steps)

                st.rerun()
                break

        else:
            selected = st.selectbox(step["title"], ['선택해주세요'] + step["options"],key=f"select_{i}_{step['name']}")
            # 선택 완료 시 상태 저장 후 다음 단계로 이동
            if selected != '선택해주세요':
                st.session_state[step["name"]] = selected
                #st.write(f"{selected} 선택됨!")
                st.session_state.messages.append({"role": "assistant", "content": f"{selected} 선택"})
                st.chat_message("assistant").write(f"{selected} 선택")

                # 다음 조건 맞는 step 찾기
                for j in range(i + 1, len(order_steps)):
                    if "condition" not in order_steps[j] or order_steps[j]["condition"](st.session_state):
                        st.session_state.order = j
                        break
                else:
                    # 모든 step 완료
                    st.session_state.order = len(order_steps)

                st.rerun()
                break
    print('sss')       
    if st.session_state.get("order", 0) >= len(order_steps):
        select_steps={'선택해주세요','선택해주세요','선택해주세요','선택해주세요','메뉴_추가','초기화','주문하기'}
        selected_orders = st.selectbox("주문_결정", select_steps, key="order_select")
                # 선택 완료 시 상태 저장 후 다음 단계로 이동
        if selected_orders != '선택해주세요':
            if selected_orders=='주문하기':
                st.write(f"{selected_orders} 선택됨!")
                st.session_state.messages.append({"role": "assistant", "content": f"{selected_orders} 선택"})
                st.chat_message("assistant").write(f"{selected_orders} 선택")
                st.chat_message("assistant").write("✅주문이 완료되었습니다!")
                st.write({step["name"]: st.session_state.get(step["name"]) for step in order_steps if step["name"] in st.session_state})
            if selected_orders=='초기화':
                    
            # 주문 관련 키 제거
                for step in order_steps:
                    if step["name"] in st.session_state:
                        del st.session_state[step["name"]]
                st.session_state.order = 0
                st.session_state.messages = []
                st.rerun()
            if selected_orders=='메뉴_추가':
                    
            # 주문 관련 키 제거
                
                st.session_state.order = 0
                st.write({step["name"]: st.session_state.get(step["name"]) for step in order_steps if step["name"] in st.session_state})
                st.rerun()