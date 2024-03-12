"""
This page provides a comprehensive guide to obesity, covering understanding, prevention,
and management. Users can explore background information on obesity, its health consequences,
prevention, and management strategies.
"""
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import LiveLite # pylint: disable=import-error

def pagea():
    """
    This function sets up the 'Comprehensive Guide to Obesity' page,
    providing background information on obesity, discussing its health consequences,
    and offering insights into prevention and management strategies. It also includes
    a button to navigate to the 'Obesity Assessment' page.

    Raises:
        FileNotFoundError: If 'app.py' doesn't exist.
        FileNotFoundError: If 'pages/b_obesity_assessment.py' doesn't exist.
    """
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

    # If the files are not loaded, go to app.py
    LiveLite.check_session_state_variable("research")

    # Give an option to the user to navigate back
    LiveLite.swap_page_back("home")

    st.markdown("""<div style="text-align:center;"><h2><span style='color:gold;'>Comprehensive
            Guide to Obesity: </span>Understanding, Prevention, and Management</h2></div>""",
            unsafe_allow_html=True)

    LiveLite.add_blank_lines()

    st.markdown("<h3 style='color:gold;'>Background on Obesity</h3>", unsafe_allow_html=True)
    LiveLite.display_background()

    LiveLite.add_blank_lines()

    st.markdown("<h3 style='color:gold;'>Health Consequences of Obesity</h3>",
                unsafe_allow_html=True)
    LiveLite.display_health_consequences()

    LiveLite.add_blank_lines()

    st.markdown("<h3 style='color:gold'>Prevention and Management</h3>", unsafe_allow_html=True)
    LiveLite.display_prevention_and_management()

    # Give an option to the user to navigate to obesity_assessment page
    _, col2, _ = st.columns([1, 1.01, 1])
    with col2:
        with stylable_container("button",
                    css_styles="""button {background-color: #f2f2f2; color: #000000;
                                font-size: 50px;}"""):

            if st.button("Your Risk Insights🌿🏃🏼", use_container_width=True):
                LiveLite.swap_page_back("obesity_assessment")

    st.markdown("<h3 style='color:gold'>Sources</h3>", unsafe_allow_html=True)
    LiveLite.display_sources()

if __name__ == "__main__":
    LiveLite.pagea()
