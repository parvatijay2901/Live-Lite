import streamlit as st
from streamlit_extras.switch_page_button import switch_page 

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.markdown("""<div style="text-align:center;"><h1><span style='color:gold;'>Live Lite:</span> Empowering you to rewrite your Obesity story..</h1></div>""", unsafe_allow_html=True)

st.write('\n'*2)

col1, col2 = st.columns([2, 0.6])
with col1:
   st.write('\n'*3)
   st.markdown("<h2 style='text-align:center; color:gold;'>We're thrilled to have you here!</h2>", unsafe_allow_html=True)
   st.markdown("<h4 style='text-align:center;'>Take some time to explore the features and resources available, and embark on your journey towards improved health and wellness with us.</h4>", unsafe_allow_html=True)
   st.write('\n')
   col11, col12 = st.columns([1,1])
   with col11:
      st.markdown("<p style='text-align:center; color:teal; font-weight:bold;'>Delve into the multifaceted landscape of obesity, exploring its complexities, causes, and consequences</p>", unsafe_allow_html=True)
      button_1 = st.button('Understand Obesity 🤷🏻‍♀️', use_container_width=True, key='button4')
      if button_1:
         switch_page("Understand Obesity 🤷🏻‍♀️")
   with col12:
      st.markdown("<p style='text-align:center; color:teal; font-weight:bold;'>Receive valuable insights to help you make informed decisions about your health and wellness journey</p>", unsafe_allow_html=True)
      button_2 = st.button('Your Risk Insights🌿🏃🏼', use_container_width=True, key='button5')
      if button_2:
         switch_page("Your Risk Insights🌿🏃🏼")
with col2:
   st.markdown("""<style>.centered-image {display: flex;justify-content: center;height: 100%;}</style>""",unsafe_allow_html=True)
   st.image("streamlit_integration/app/logo.png", width=300)

for _ in range(8):   
   st.write('\n')
st.markdown("<p style='text-align:center; font-weight:bold;'>Parvati Jayakumar, Ted Liu, Saikripa Mohan, Manasa Shivappa Ronur</p>", unsafe_allow_html=True)