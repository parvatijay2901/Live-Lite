"""
This page provides a comprehensive guide to obesity, covering understanding, prevention,
and management. Users can explore background information on obesity, its health consequences,
prevention, and management strategies.
"""
import os
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import LiveLite # pylint: disable=import-error

def pagea():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

    # If the files are not loaded, go to app.py
    LiveLite.check_session_state_variable("research")

    # Give an option to the user to navigate back
    _, col1 = st.columns([10, 1.5])
    with col1:
        if st.button("→ Home🏠", use_container_width=True):
            page_path = "LiveLite/streamlit_app/app.py"
            if os.path.exists(os.path.join(os.getcwd(), page_path)):
                st.switch_page("app.py")
            else:
                raise FileNotFoundError("File app.py not found")

    st.markdown("""<div style="text-align:center;"><h2><span style='color:gold;'>Comprehensive
            Guide to Obesity: </span>Understanding, Prevention, and Management</h2></div>""",
            unsafe_allow_html=True)

    LiveLite.add_blank_lines()

    st.markdown("<h3 style='color:gold;'>Background on Obesity</h3>", unsafe_allow_html=True)
    LiveLite.display_background()

    LiveLite.add_blank_lines()

    st.markdown("<h3 style='color:gold;'>Health Consequences of Obesity</h3>", unsafe_allow_html=True)
    LiveLite.display_health_consequences()

    LiveLite.add_blank_lines()

    st.markdown("<h3 style='color:gold'>Prevention and Management</h3>", unsafe_allow_html=True)
    LiveLite.display_prevention_and_management()

    # Give an option to the user to navigate to obesity_assessment page
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        with stylable_container("button",
                    css_styles="""button {background-color: #f2f2f2; color: black;font-size: 50px;}"""):

            if st.button("Your Risk Insights🌿🏃🏼", use_container_width=True):
                page_path = "LiveLite/streamlit_app/pages/b_obesity_assessment.py"
                if os.path.exists(os.path.join(os.getcwd(), page_path)):
                    st.switch_page("pages/b_obesity_assessment.py")
                else:
                    raise FileNotFoundError("File pages/b_obesity_assessment.py not found")

    st.markdown("<h3 style='color:gold'>Sources</h3>", unsafe_allow_html=True)
    LiveLite.display_sources()

if __name__ == "__main__":
    LiveLite.pagea()
