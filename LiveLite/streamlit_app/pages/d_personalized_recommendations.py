"""
This page displays personalized recommendations for
diet and physical activity based on user inputs.
"""
import os
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import LiveLite # pylint: disable=import-error

def paged():
    """
    This function sets up the 'Personalized Recommendations' page,
    calculating estimated daily calorie intake and providing personalized
    recommendations for diet and physical activity based on user inputs.
    Users can also navigate to view more food recommendations.

    Raises:
        FileNotFoundError: File 'pages/e_more_diet_recommendations.py' doesn't exist.
    """
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

    # Go back to the home page if the variables are not loaded
    LiveLite.check_session_state_variable("recommendations")

    # Provide an option to the user to navigate to other pages
    LiveLite.swap_pages_back(choice="basic_risk_insights")

    st.markdown("""<div style="text-align:center;"><h2 style='color:gold;'>
            Personalized Recommendations</h2></div>""", unsafe_allow_html=True)

    # Calculate estimated daily calorie intake
    calorie_intake = LiveLite.controller("estimate_calorie_intake")
    st.markdown(f"""<div style="text-align: center;"><h3>Estimated Daily Calorie Intake:
                {calorie_intake:.1f}Kcal</h3></div>""", unsafe_allow_html=True)
    st.session_state['calorie_intake'] = calorie_intake

    # Get personalized recommendations
    recommendation = LiveLite.controller("recommender_basic")
    col1, _, col3 = st.columns([1,0.2,1])
    with col1:
        st.markdown("""<div style="text-align: center;"><h3 style='color:gold;'>
                    Diet Recommendation</h3></div>""", unsafe_allow_html=True)
        LiveLite.add_blank_lines()
        st.markdown("""<div style ="text-align: center;"><p style='color:#99fadc;'>Ensure you
                    meet the recommended daily intake levels for these macro-nutrients for optimal
                    health and performance!</p></div>""", unsafe_allow_html=True)
        _, col112, _ = st.columns([1,25,1])
        with col112:
            LiveLite.add_blank_lines()
            # Display macronutrients diet df
            st.dataframe(recommendation[0], hide_index=True)
            LiveLite.add_blank_lines(2)
        st.markdown("""<div style ="text-align: center;"><p style='color:#99fadc;'>Include these
                    food groups into your diet to nourish your body with necessary micronutrients to
                    support metabolic processes!</p></div>""", unsafe_allow_html=True)
        _, col122, _ = st.columns([1,2,1])
        with col122:
            LiveLite.add_blank_lines()
            # Display micronutrients diet df
            st.dataframe(recommendation[1], hide_index=True)
            LiveLite.add_blank_lines()
            with stylable_container("button",
                    css_styles="""button {background-color: #f2f2f2; color: black;
                                font-size: 50px;}"""):
                if st.button("View more Food Recommendations 🥦", use_container_width=True):
                    page_path = "LiveLite/streamlit_app/pages/d_personalized_recommendations.py"
                    if os.path.exists(os.path.join(os.getcwd(), page_path)):
                        st.switch_page("pages/e_more_diet_recommendations.py")
                    else:
                        raise FileNotFoundError("pages/e_more_diet_recommendations.py not found")

    with col3:
        st.markdown("""<div style="text-align: center;"><h3 style='color:gold;'>
                    Physical Activity Recommendation</h3></div>""", unsafe_allow_html=True)
        LiveLite.add_blank_lines()
        st.markdown("""<div style ="text-align: center;"><p style='color:#99fadc;'>
                    Get fit and live a healthier life with these activities!</p></div>""",
                    unsafe_allow_html=True)
        _, col32, _ = st.columns([1,25,1])
        with col32:
            LiveLite.add_blank_lines()
            # Display physical_activity_recommendation df
            st.dataframe(recommendation[2], hide_index=True)

if __name__ == "__main__":
    paged()
