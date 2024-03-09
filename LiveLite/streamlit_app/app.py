"""
Live Lite Streamlit App

This Streamlit app provides an interface for the Live Lite project, empowering users to explore
and understand obesity, receive valuable insights about their health and wellness journey,
and access various resources for improved health outcomes. This is the landing page from
where the users can navigate themselves to other pages

Authors:
- Parvati Jayakumar
- Ted Liu
- Saikripa Mohan
- Manasa Shivappa Ronur
"""
import streamlit as st
import pandas as pd
import LiveLite # pylint: disable=import-error

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.markdown("""<div style="text-align:center;"><h1><span style='color:gold;'>Live Lite:</span>
            Empowering you to rewrite your Obesity story..</h1></div>""", unsafe_allow_html=True)
LiveLite.add_blank_lines()

col1, col2 = st.columns([2, 0.6])
with col1:
    LiveLite.add_blank_lines()
    st.markdown("<h2 style='text-align:center; color:gold;'>We're thrilled to have you here!</h2>",
                unsafe_allow_html=True)
    st.markdown("""<h4 style='text-align:center;'>Take some time to explore the features
                and resources available, and embark on your journey towards improved health
                and wellness with us.</h4>""", unsafe_allow_html=True)
    LiveLite.add_blank_lines()
    col11, col12 = st.columns([1,1])
    with col11:
        # Button that navigates to research page
        st.markdown("""<p style='text-align:center; color:#00b3b3; font-weight:bold;'>Delve into
                    the multifaceted landscape of obesity, exploring its complexities, causes,
                    and consequences</p>""", unsafe_allow_html=True)
        button_1 = st.button('Understand Obesity 🤷🏻‍♀️', use_container_width=True, key='button4')
        if button_1:
            try:
                st.switch_page("pages/a_understanding_obesity.py")
            except FileNotFoundError as e:
                raise FileNotFoundError(f"File - {e} not found") from e
    with col12:
        # Button that navigates to obesity_assessment
        st.markdown("""<p style='text-align:center; color:#00b3b3; font-weight:bold;'>
                    Receive valuable insights to help you make informed decisions about
                    your health and wellness journey</p>""", unsafe_allow_html=True)
        button_2 = st.button('Your Risk Insights🌿🏃🏼', use_container_width=True, key='button5')
        if button_2:
            try:
                st.switch_page("pages/b_obesity_assessment.py")
            except FileNotFoundError as e:
                raise FileNotFoundError(f"File - {e} not found") from e

with col2:
    st.markdown("""<style>.centered-image {display: flex;justify-content: center;height: 100%;}
                </style>""",unsafe_allow_html=True)
    # Display the logo
    try:
        st.image("LiveLite/streamlit_app/images/logo.png", width=300)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File - {e} not found") from e

LiveLite.add_blank_lines(num_lines=9)

st.markdown("""<p style='text-align:center; font-weight:bold;'>Parvati Jayakumar, Ted Liu,
            Saikripa Mohan, Manasa Shivappa Ronur</p>""", unsafe_allow_html=True)

# Load all the data used by sub-functions in the landing page
try:
    FOOD_NUTRITION_DATA_PATH = "LiveLite/data/input_files/food_nutrition_data.csv"
    DATA_NHANES_PATH = "LiveLite/data/input_files/NHANES_Background.csv"
    DATA_IHME_PATH = "LiveLite/data/input_files/IHME/number-of-deaths-by-risk-factor.csv"

    if ('food_nutrition_data' not in st.session_state or
        'data_nhanes' not in st.session_state or
        'data_ihme' not in st.session_state):
        food_nutrition_data = pd.read_csv(FOOD_NUTRITION_DATA_PATH)
        data_nhanes = pd.read_csv(DATA_NHANES_PATH, low_memory=False)
        data_ihme = pd.read_csv(DATA_IHME_PATH)
        st.session_state['food_nutrition_data'] = food_nutrition_data
        st.session_state['data_nhanes'] = data_nhanes
        st.session_state['data_ihme'] = data_ihme

except FileNotFoundError as e:
    raise FileNotFoundError(f"File - {e} not found") from e
except pd.errors.ParserError as e:
    raise pd.errors.ParserError(f"File - {e} not found") from e
