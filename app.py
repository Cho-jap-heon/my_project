# cd C:\Users\806jh\Downloads\My_project&&streamlit run app.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'code'))


import streamlit as st
import pandas as pd
from streamlit_chat import message
from code_dt.start import start
from code_dt.menu_watching import menu_watching
from code_dt.reference import reference
from code_dt.menu_more_watching import menu_more_watching
from code_dt.new_ddk_select import new_ddk_select
from code_dt.order_start import order_start

df= pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
print("DEBUG type:", type(st.session_state))
print("DEBUG value:", st.session_state)

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

    st.image("img_dt/character3.png")      
    start()

elif st.session_state.mode == 1:  
    
    menu_watching()
        
elif st.session_state.mode == 3:

    reference()
elif st.session_state.mode == 2:  
    order_start()
    new_ddk_select()
    
            
menu_more_watching()                 

    
