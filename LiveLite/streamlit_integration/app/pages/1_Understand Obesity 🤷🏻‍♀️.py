import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
import sys,os

path = '././.'
sys.path.append(os.path.abspath(path))
from research.display_info import background, health_consequences, prevention_and_management, research_trends, sources

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

col0, col1 = st.columns([10, 1.5])
with col1:
    if st.button("🡆 Home🏠", use_container_width=True):
        switch_page("Home🏠")
        
st.markdown("""<div style="text-align:center;"><h2><span style='color:gold;'>Comprehensive Guide to Obesity: </span>Understanding, Prevention, and Management</h2></div>""", unsafe_allow_html=True)

st.markdown('\n')

st.markdown("<h3 style='color:gold;'>Background on Obesity</h3>", unsafe_allow_html=True)
background.display_background()

st.markdown('\n')

st.markdown("<h3 style='color:gold;'>Health Consequences of Obesity</h3>", unsafe_allow_html=True)
health_consequences.display_health_consequences()

st.markdown('\n')

st.markdown("<h3 style='color:gold;'>Research Trends</h3>", unsafe_allow_html=True)
research_trends.display_research_trends()

st.markdown('\n')

st.markdown("<h3 style='color:gold'>Prevention and Management</h3>", unsafe_allow_html=True)
prevention_and_management.display_prevention_and_management()
if st.button("Your Risk Insights🌿🏃🏼", use_container_width=True):
        switch_page("Your Risk Insights🌿🏃🏼")
        
st.markdown('\n')

st.markdown("<h3 style='color:gold'>Sources</h3>", unsafe_allow_html=True)
sources.display_sources()




