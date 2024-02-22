import streamlit as st
from streamlit_extras.switch_page_button import switch_page 

import sys,os
path = '././.'
sys.path.append(os.path.abspath(path))
from recommendation_tool.handle_user_input.get_user_inputs import get_user_inputs

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

col0, col1 = st.columns([10, 1.5])
with col1:
    if st.button("🡆 Home🏠", use_container_width=True):
        switch_page("Home🏠")
        
st.markdown("""<div style="text-align:center;"><h2 style='color:gold;'>Obesity Assessment</h2></div>""", unsafe_allow_html=True)

st.markdown('\n')

status = get_user_inputs()

st.markdown('\n'*5)

_, col2, _ = st.columns([1, 1, 1])
with col2:
    if st.button("Get Personalized Recommendations", use_container_width=True):
        if status:
            switch_page("Personalized Recommendations")
        else:
            pass # Add this section later
        