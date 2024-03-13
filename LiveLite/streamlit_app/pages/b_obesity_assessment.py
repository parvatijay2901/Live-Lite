"""
This page allows users to assess their risk of obesity by answering a few questions. The responses
provided by the users will be used to generate personalized feedback and recommendations to support
their health and well-being.
"""

import os
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import LiveLite # pylint: disable=import-error

def pageb():
    """
    This function sets up the 'Obesity Risk Assessment' page, allowing users to answer questions
    to better understand their risk of obesity. User responses are saved for personalized feedback
    and recommendations. Users can also navigate back to the home page.

    Raises:
        FileNotFoundError: If the file 'app.py' doesn't exist when navigating back to the home page.
        FileNotFoundError: If the file 'pages/c_risk_insights.py' doesn't
                        exist when navigating to view insights.
    """
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

    # Give an option to the user to navigate back
    LiveLite.swap_page_back("home")

    st.markdown("""<div style="text-align:center;"><h2 style='color:gold;'>
                Obesity Risk Assessment</h2></div>""", unsafe_allow_html=True)

    st.markdown("""<h4 style='text-align:center;'>Answer a few questions to better understand
                your risk of obesity. Your responses will help us provide personalized feedback
                and recommendations to support your health and well-being.</h4>""",
                unsafe_allow_html=True)

    LiveLite.add_blank_lines(3)

    # Provide an option for the users to fill/save user inputs
    st.session_state['user_inputs'] = {}
    user_inputs = LiveLite.get_user_inputs()
    st.session_state['user_inputs'] = user_inputs

    LiveLite.add_blank_lines(3)

    # Give an option to the user to view our insights
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        with stylable_container("button",
                    css_styles="""button {background-color: #f2f2f2; color: black;
                                font-size: 50px;}"""):
            if st.button("Assess your Obesity Risk 🔎", use_container_width=True):
                page_path = "LiveLite/streamlit_app/pages/c_risk_insights.py"
                if os.path.exists(os.path.join(os.getcwd(), page_path)):
                    # Log - save the user inputs in a CSV
                    LiveLite.write_user_inputs_to_csv(user_inputs,
                            filename='LiveLite/data/output_files/user_inputs.csv')
                    st.switch_page("pages/c_risk_insights.py")
                else:
                    raise FileNotFoundError("File pages/c_risk_insights.py not found")

if __name__ == "__main__":
    LiveLite.pageb()
