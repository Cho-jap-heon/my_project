
# cd C:\Users\806jh\Downloads\My_project&&streamlit run app.py
#from gtts import gTTS
#import os
import streamlit as st
import pandas as pd
from streamlit_chat import message
#from datetime import datetime
#from playsound import playsound
# 저장 디렉토리 설정
BASE_PATH = "C:/Users/806jh/Desktop/voice_files"
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
def reference():
    if query := st.chat_input("1: 커플 2: 두명 3: 패밀리 4: 단체  5: 솔로  6: 처음으로 ") : # 사용자의입력과답변기록과출력
        st.session_state.messages.append({"role": "user", "content": query})
        st.chat_message("user").write(query)
        if query=="메뉴" or query=="1":
            #st.session_state.menu="떡볶이"
            #st.session_state.mode =1
            response = "1-2인분 세트. "
            
        elif query=="2":
            #st.session_state.mode =1
            #st.session_state.menu="주먹밥"
            response ="응세트"
        elif query=="3": 
            #st.session_state.mode =1
            #st.session_state.menu="사이드"
            response = "급세트"
        elif query=="4": 
            #st.session_state.mode =1
            #st.session_state.menu="튀김"
            response = "4명당 실세트"
        elif query=="5": 
            #st.session_state.mode =1
            #st.session_state.menu="모두"
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
def ddk_select():
        #status = st.radio('맵기 선택', ['부상', '부상+','중상','혼수상태','사망','선택완료'])
        # 사용법
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
        selected1 = st.selectbox("토핑 선택", topping1_options, key="menu_selectbox")
        
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
        selected2 = st.selectbox("토핑 선택", topping2_options, key="menu_selectbox2")
        
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
        selected = st.selectbox("추가토핑 선택", menu_options, key="menu_selectbox")
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
        menu_options = ['선택해주세요','토핑추가 X','수제비 (10개)','집채어묵 (3개)','물만두 (6개)','고구마떡 (6개)','비엔나소시지 (6개)','메추리알 (6개)','계란 (2개)','떡 추가','오뎅 추가']
        selected = st.selectbox("추가토핑 선택", menu_options, key="menu_selectbox")
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
        menu_options = ['선택해주세요','치즈추가 X','치즈 1개','치즈 2개','치즈 3개','치즈 4개']
        selected = st.selectbox("추가토핑 선택", menu_options, key="menu_selectbox")
        if selected != '선택해주세요':
            if selected == '치즈추가 X':
                st.session_state.order = 4
                st.rerun()
            st.session_state.selected_menu = selected
            st.write(f"{selected}메뉴 선택!")
            st.session_state.messages.append({"role": "assistant", "content": f"{selected}메뉴 선택"})
            st.chat_message("assistant").write(f"{selected}메뉴 선택")

            # order를 다음 단계로 진행하고 rerun
            st.session_state.order = 4
            st.rerun()    
    elif st.session_state.order == 4:
        response = "떡볶이 선택 완료. 주문을 저장할게요."
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
        st.rerun()    
# 디렉토리 없으면 생성
#if not os.path.exists(BASE_PATH):
    #os.makedirs(BASE_PATH)

# 고유 파일명 생성 함수
#def unique_filename(prefix):
    #timestamp = datetime.now().strftime('%H%M%S')
    #return os.path.join(BASE_PATH, f"{prefix}_{timestamp}.mp3")

# 재생 안전 처리 함수
#def safe_play(file_path):
    #try:
        #playsound(file_path)
    #except Exception as e:
        #print(f"재생 중 오류 발생: {e}")

#hello="무엇을도와드릴까요"
#hello_file = unique_filename("hello")
#gTTS(text=hello, lang='ko').save(hello_file)

df= pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.title('★주문의 요정★')
if "menu" not in st.session_state:
    st.session_state.menu = 0

if "messages" not in st.session_state:
      
    st.session_state.messages = [{"role": "assistant", "content": "안녕하세요! 주문을 도와드릴게요."}]
    #safe_play(hello_file)
    st.session_state.mode = 0
for msg in st.session_state.messages:    
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
    
if st.session_state.mode == 0:
    st.image("character3.png")  
    
    #st.image("C:/Users/806jh/Downloads/My_project\character.png")       
    start()

elif st.session_state.mode == 1:  
    
    menu_watching()
        
elif st.session_state.mode == 3:
    reference()
elif st.session_state.mode == 2:  
    order_start()
    ddk_select()
            
menu_more_watching()                 

    

