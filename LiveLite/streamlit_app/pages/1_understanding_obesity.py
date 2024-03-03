import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import LiveLite

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

_, col1 = st.columns([10, 1.5])
with col1:
        if st.button("🡆 Home🏠", use_container_width=True):
                st.switch_page("Home.py")
        
st.markdown("""<div style="text-align:center;"><h2><span style='color:gold;'>Comprehensive Guide to Obesity: </span>Understanding, Prevention, and Management</h2></div>""", unsafe_allow_html=True)
LiveLite.add_blank_lines()

st.markdown("<h3 style='color:gold;'>Background on Obesity</h3>", unsafe_allow_html=True)
LiveLite.display_background()
LiveLite.add_blank_lines()

st.markdown("<h3 style='color:gold;'>Health Consequences of Obesity</h3>", unsafe_allow_html=True)
LiveLite.display_health_consequences()
LiveLite.add_blank_lines()

st.markdown("<h3 style='color:gold'>Prevention and Management</h3>", unsafe_allow_html=True)
LiveLite.display_prevention_and_management()

_, col2, _ = st.columns([1, 1, 1])
with col2:
        with stylable_container("button", css_styles="""button {background-color: #f2f2f2; color: black;font-size: 50px;}"""):
                if st.button("Your Risk Insights🌿🏃🏼", use_container_width=True):
                        st.switch_page("pages/2_obesity_assessment.py")
LiveLite.add_blank_lines()

st.markdown("<h3 style='color:gold'>Sources</h3>", unsafe_allow_html=True)
LiveLite.display_sources()




