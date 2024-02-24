import streamlit as st
import project_integration

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

col1, _, col3 = st.columns([2.5, 10, 1.5])
with col1:
    if st.button("⬅ Obesity Assessment 📑", use_container_width=True):
        st.switch_page("pages/2_obesity_assessment.py")
with col3:
    if st.button("➞ Home🏠", use_container_width=True):
        st.switch_page("Home.py")
        
st.markdown("""<div style="text-align:center;"><h2 style='color:gold;'>Risk Insights and Recommendations</h2></div>""", unsafe_allow_html=True)
_, col2, _ = st.columns([4.3, 1, 5])
with col2:
    project_integration.add_blank_lines()
    risk_score = project_integration.controller("risk_score")
    project_integration.display_risk_score(risk_score)
    
project_integration.add_blank_lines(2)


_, col2, _ = st.columns([2, 10, 2])
with col2:    
    project_integration.display_risk_suggestion(risk_score)
project_integration.add_blank_lines(2)

_, col2, _ = st.columns([1, 1, 1])
with col2: 
    intensity = st.selectbox("Choose preferred exercise intensity level", ["Low", "Moderate", "High"])
    st.session_state['preferred_exercise_intensity_level'] = intensity.lower()   
    view_recommendations = st.button("View Personalized Recommendations 🌿🏃🏼", use_container_width=True)
    project_integration.add_blank_lines(2)
if view_recommendations:
    col1, _, col3 = st.columns([1,0.2,1])
    with col1:
        ## TO BE MODIFIED
        st.markdown("""<div style="text-align: center;"><h3 style='color:gold;'>Diet Recommendation</h3></div>""", unsafe_allow_html=True)
        # 1. Show the macro nutrient table
        # 2. "View more recommendations" button
        # 3. provide a dropdown with unique food categories
            # 3.1 Filter to only have that dataframe
        # 4. Provide a search bar
            # 4.1 Filter to only have that dataframe
    with col3:
        st.markdown("""<div style="text-align: center;"><h3 style='color:gold;'>Physical Activity Recommendation</h3></div>""", unsafe_allow_html=True)
        project_integration.add_blank_lines()
        st.markdown("""<div style ="text-align: center;">Get fit and live a healthier life with these activities!</div>""", unsafe_allow_html=True)
        _, col32, _ = st.columns([1,25,1])
        with col32:
            project_integration.add_blank_lines()
            physical_activity_recommendation = project_integration.controller("physical_activity_recommender")
            st.dataframe(physical_activity_recommendation, hide_index=True)