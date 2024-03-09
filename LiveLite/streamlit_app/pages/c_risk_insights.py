"""
This module provides the functionality for displaying
risk insights related to obesity assessment.
"""

import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import LiveLite # pylint: disable=import-error

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Go back to the home page if the variables are not loaded
LiveLite.check_session_state_variable("recommendations")

# Provide an option to users to navigate pages back
LiveLite.swap_pages_back(choice="obesity_assessment")

st.markdown("""<div style="text-align:center;"><h2 style='color:gold;'>
            Risk Insights</h2></div>""", unsafe_allow_html=True)

# Display risk score and color
_, col2, _ = st.columns([4.3, 1, 5])
with col2:
    LiveLite.add_blank_lines()
    risk_score, color = LiveLite.controller("risk_score")
    st.session_state['risk_score'] = risk_score
    LiveLite.display_risk_score(risk_score, color)

# Display risk suggestion
LiveLite.add_blank_lines(2)
_, col2, _ = st.columns([2, 10, 2])
with col2:
    LiveLite.display_risk_suggestion(risk_score)

# Collect user inputs for exercise intensity level and food preference
LiveLite.add_blank_lines(2)
_, col2, _ = st.columns([1, 1, 1])
with col2:
    intensity = st.selectbox("Choose preferred exercise intensity level",
                            ["Moderate", "Low", "High"])
    st.session_state['preferred_exercise_intensity_level'] = intensity.lower()
    food_preference = st.selectbox("Mention your Dietary Preference", ["Vegan",
                                                                    "Vegetarian",
                                                                    "Non Vegetarian"])
    st.session_state['food_preference'] = food_preference.lower()
    # Provide user to navigate to view personalized recommendations
    with stylable_container("button",
            css_styles="""button {background-color: #f2f2f2; color: black;font-size: 50px;}"""):
        if st.button("View Personalized Recommendations 🌿🏃🏼", use_container_width=True):
            try:
                st.switch_page("pages/d_personalized_recommendations.py")
            except FileNotFoundError as e:
                raise FileNotFoundError(f"File - {e} not found") from e
