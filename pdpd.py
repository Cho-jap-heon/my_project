#  cd C:\Users\806jh\Downloads\My_project
import streamlit as st
import pandas as pd
from streamlit_chat import message
from code_dt.start import start
from code_dt.menu_watching import menu_watching
from code_dt.reference import reference
from code_dt.menu_more_watching import menu_more_watching
from code_dt.ddk_select import ddk_select
from code_dt.order_start import order_start

# 만들어야하는거 종료되거나 리셋하면 행렬 전부 초기화, 가격 개수 메뉴 행렬
# 딕셔너리 형태로 1-2인분은 9500이렇게 할지, 1-2:9500이런식으로 하고 거기다 로입설처럼 : 이후로 잘라서 메꾸기 이경우 if문을 많이 써야하나, 그냥 행렬로 열 구분해서 만들기
# 기본 가격들과 메뉴 각각을 전부 따로 저장을 해놓고 새로운 행렬에 그것들 복사하기 vs 기본 모드 행렬에서 개수들 전부 0으로 초기화 > 주문될때마다 1씩 추가
df= pd.DataFrame({
    'ddk_order': ['1-2','2-3', '치즈', 4,5,6,7,8,9,10],
    'ddk_number': [1,2,3,4,5,6,7,8,9,10],
    'ddk_price':[1,2,3,4,5,6,7,8,9,10]
})
df['output']=df['ddk_order']*df['ddk_number']
df.loc[4, 'ddk_price'] = 3000

st.write(df)

'''
ddk_select에서 이걸 임포트
토핑이나 튀김들을 전부 행렬로 만들어놓기?
그러고 메뉴모드에서만 임포트
주문 메뉴에서 뭐 선택 하면 기본 가격으로 값 추가
토핑 등등은 토핑 열에 추가 기보토핑1,2 열 추가토핑 열
주문 삭제는 어떻게 할지 모르겠으나 그러면 그 값을 다시 0으로 교체

계산 모드는 가격 열(개수*가격)전부 합친 맨 아래 열 배출

'''