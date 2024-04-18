import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import pymysql
from st_aggrid import AgGrid, GridOptionsBuilder
import os
os.chdir('/app')
from utils import *

img = Image.open("/app/asset/popo.png")
side_bar_img = make_circle(img)

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with st.sidebar:
    
    # 제목과 부제목 추가 (HTML 사용)
    st.sidebar.markdown('<h1 style="font-size: 50px;">AXIS</h1>', unsafe_allow_html=True)
    st.sidebar.markdown('<h2 style="font-size: 18px; color: grey">AI XRAY Inspector System for Sunjin</h2>', unsafe_allow_html=True)
    
    st.sidebar.image(side_bar_img, use_column_width=True)
    
    st.sidebar.markdown('<h2 style="font-size: 18px; color: grey"></h2>', unsafe_allow_html=True) # 공백용
    
    choose = option_menu("Menu", ["모니터링", "실험하기"],
                         icons=['bi bi-stack', 'kanban'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

# 메인 스레드에서는 Streamlit 애플리케이션 실행
#if choose == "모니터링":
#    run_Main_Dashboard()
#elif choose == "실험하기":
#    run_test_Dashboard()