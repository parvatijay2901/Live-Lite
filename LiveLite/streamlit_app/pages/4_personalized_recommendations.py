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
        Personalized Recommendations</h2></div>""", unsafe_allow_html=True)

calorie_intake = LiveLite.controller("estimate_calorie_intake")
st.markdown(f"""<div style="text-align: center;"><h3>Estimated Daily Calorie Intake: {calorie_intake:.1f}Kcal</h3></div>""", unsafe_allow_html=True)
st.session_state['calorie_intake'] = calorie_intake
recommendation = LiveLite.controller("recommender_basic")

col1, _, col3 = st.columns([1,0.2,1])
with col1:
    st.markdown("""<div style="text-align: center;"><h3 style='color:gold;'>Diet Recommendation</h3></div>""", unsafe_allow_html=True)
    LiveLite.add_blank_lines()
    st.markdown("""<div style ="text-align: center;"><p style='color:#99fadc;'>Ensure you meet the recommended daily intake
                levels for these macro-nutrients for optimal health and performance!</p></div>""", unsafe_allow_html=True)

    _, col112, _ = st.columns([1,25,1])
    with col112:
        LiveLite.add_blank_lines()
        st.dataframe(recommendation[0], hide_index=True)
        LiveLite.add_blank_lines(2)
    st.markdown("""<div style ="text-align: center;"><p style='color:#99fadc;'>Include these food groups into your diet
                to nourish your body with necessary micronutrients to support metabolic processes!</p></div>""",
                unsafe_allow_html=True)
    _, col122, _ = st.columns([0.9,2,0.9])
    with col122:
        LiveLite.add_blank_lines()
        st.dataframe(recommendation[1], hide_index=True)
        LiveLite.add_blank_lines()
        with stylable_container("button", css_styles="""button {background-color: #f2f2f2; color: black;font-size: 50px;}"""):
            if st.button("View more Food Recommendations 🥦", use_container_width=True):
                st.switch_page("pages/5_more_diet_recommendations.py")
with col3:
    st.markdown("""<div style="text-align: center;"><h3 style='color:gold;'>Physical Activity Recommendation</h3></div>""", unsafe_allow_html=True)
    LiveLite.add_blank_lines()
    st.markdown("""<div style ="text-align: center;"><p style='color:#99fadc;'>Get fit and live a healthier life with
                these activities!</p></div>""", unsafe_allow_html=True)
    _, col32, _ = st.columns([1,25,1])
    with col32:
        LiveLite.add_blank_lines()
        st.dataframe(recommendation[2], hide_index=True)
