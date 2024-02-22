import streamlit as st
from streamlit_extras.switch_page_button import switch_page 

import sys,os
path = '././.'
sys.path.append(os.path.abspath(path))
from streamlit_integration.controller.controller import controller

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

col1, _, col3 = st.columns([2.5, 10, 1.5])
with col1:
    if st.button("⬅ Obesity Assessment", use_container_width=True):
        switch_page("Your Risk Insights🌿🏃🏼")
with col3:
    if st.button("➞ Home🏠", use_container_width=True):
        switch_page("Home🏠")
        
st.markdown("""<div style="text-align:center;"><h2 style='color:gold;'>Personalized Risk Insights and Recommendations</h2></div>""", unsafe_allow_html=True)

st.markdown('\n'*3)

_, col2, _ = st.columns([4.3, 1, 5])
with col2:
    circle_html = controller("risk_score")
    st.markdown(circle_html, unsafe_allow_html=True)

st.markdown('\n'*5)

col11, _, col3 = st.columns([1,0.2,1])
with col11:
    # To be modified
    st.markdown("""<h3>Diet Recommendation</h3>""", unsafe_allow_html=True)
    physical_activity_recommendendation = controller("physical_activity_recommender")
    st.dataframe(physical_activity_recommendendation)
with col3:
    st.markdown("""<h3>Physical Activity Recommendation</h3>""", unsafe_allow_html=True)
    physical_activity_recommendendation = controller("physical_activity_recommender")
    st.dataframe(physical_activity_recommendendation)