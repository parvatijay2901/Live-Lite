import streamlit as st
from streamlit_extras.switch_page_button import switch_page 

col0, col1 = st.columns([10, 0.5])
with col1:
    if st.button("🡆", use_container_width=True):
        switch_page("Home🏠")

circle_html = """<div style="width: 500px; height: 500px; border-radius: 50%; background-color:teal; display: flex; justify-content: center; align-items: center; color: white; font-weight: bold;">Circle</div>"""
st.markdown(circle_html, unsafe_allow_html=True)