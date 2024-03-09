import streamlit as st
import LiveLite
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

col1, _, col3 = st.columns([2.5, 10, 1.5])
with col1:
    if st.button("← Obesity Assessment 📑", use_container_width=True):
        st.switch_page("pages/2_obesity_assessment.py")
with col3:
    if st.button("→ Home🏠", use_container_width=True):
        st.switch_page("Home.py")
        
st.markdown("""<div style="text-align:center;"><h2 style='color:gold;'>
            Risk Insights</h2></div>""", unsafe_allow_html=True)
_, col2, _ = st.columns([4.3, 1, 5])
with col2:
    LiveLite.add_blank_lines()
    risk_score, color = LiveLite.controller("risk_score")
    st.session_state['risk_score'] = risk_score
    LiveLite.display_risk_score(risk_score, color)
    
LiveLite.add_blank_lines(2)

_, col2, _ = st.columns([2, 10, 2])
with col2:    
    LiveLite.display_risk_suggestion(risk_score)
LiveLite.add_blank_lines(2)

_, col2, _ = st.columns([1, 1, 1])
with col2: 
    intensity = st.selectbox("Choose preferred exercise intensity level", ["Moderate", "Low", "High"])
    st.session_state['preferred_exercise_intensity_level'] = intensity.lower()  
    food_preference = st.selectbox("Mention your Dietary Preference", ["Vegan",
                                                                    "Vegetarian",
                                                                    "Non Vegetarian"]) 
    st.session_state['food_preference'] = food_preference.lower()
    
    with stylable_container("button", css_styles="""button {background-color: #f2f2f2; color: black;font-size: 50px;}"""):
        if st.button("View Personalized Recommendations 🌿🏃🏼", use_container_width=True):
            st.switch_page("pages/4_personalized_recommendations.py")