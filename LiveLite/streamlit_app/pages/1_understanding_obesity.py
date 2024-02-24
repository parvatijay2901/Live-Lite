import streamlit as st
import project_integration
import research

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

_, col1 = st.columns([10, 1.5])
with col1:
        if st.button("🡆 Home🏠", use_container_width=True):
                st.switch_page("Home.py")
        
st.markdown("""<div style="text-align:center;"><h2><span style='color:gold;'>Comprehensive Guide to Obesity: </span>Understanding, Prevention, and Management</h2></div>""", unsafe_allow_html=True)
project_integration.add_blank_lines()

st.markdown("<h3 style='color:gold;'>Background on Obesity</h3>", unsafe_allow_html=True)
research.research_display_info.background.display_background()
project_integration.add_blank_lines()

st.markdown("<h3 style='color:gold;'>Health Consequences of Obesity</h3>", unsafe_allow_html=True)
research.research_display_info.health_consequences.display_health_consequences()
project_integration.add_blank_lines()

st.markdown("<h3 style='color:gold;'>Research Trends</h3>", unsafe_allow_html=True)
research.research_display_info.research_trends.display_research_trends()
project_integration.add_blank_lines()

st.markdown("<h3 style='color:gold'>Prevention and Management</h3>", unsafe_allow_html=True)
research.research_display_info.prevention_and_management.display_prevention_and_management()
if st.button("Your Risk Insights🌿🏃🏼", use_container_width=True):
        st.switch_page("pages/2_obesity_assessment.py")
project_integration.add_blank_lines()

st.markdown("<h3 style='color:gold'>Sources</h3>", unsafe_allow_html=True)
research.research_display_info.sources.display_sources()




