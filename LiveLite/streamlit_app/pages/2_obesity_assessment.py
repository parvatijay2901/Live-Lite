import streamlit as st
import LiveLite
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.session_state['user_inputs'] = {}

col0, col1 = st.columns([10, 1.5])
with col1:
    if st.button("→ Home🏠", use_container_width=True):
        st.switch_page("Home.py")
        
st.markdown("""<div style="text-align:center;"><h2 style='color:gold;'>Obesity Risk Assessment</h2></div>""", unsafe_allow_html=True)

st.markdown("""<h4 style='text-align:center;'>Answer a few questions to better understand your risk of obesity. Your responses will 
            help us provide personalized feedback and recommendations to support your health and well-being.</h4>""", 
            unsafe_allow_html=True)
LiveLite.add_blank_lines(3)

user_inputs = LiveLite.get_user_inputs()
st.session_state['user_inputs'] = user_inputs
LiveLite.add_blank_lines(3)

_, col2, _ = st.columns([1, 1, 1])
with col2:
    with stylable_container("button", css_styles="""button {background-color: #f2f2f2; color: black;font-size: 50px;}"""):
        if st.button("Assess your Obesity Risk 🔎", use_container_width=True):
            LiveLite.write_user_inputs_to_csv(user_inputs, filename='LiveLite/data/output_files/user_inputs.csv')
            st.switch_page("pages/3_risk_insights.py")