import streamlit as st
import pandas as pd

def get_demographic_inputs():
    age = st.number_input("Age", min_value=18, step=1)
    sex = st.selectbox("Sex at Birth", ["Male", "Female"])
    height = st.number_input("Height (in cm)", min_value=100.0)
    weight = st.number_input("Weight (in kg)", min_value=20.0)
    ethnicity = st.selectbox("Self-identified Race/Ethnicity", ["Hispanic", "Mexican American", "Non-Hispanic White", "Non-Hispanic Black", "Non-Hispanic Asian", "Non-Hispanic Multiracial", "Other Non-Hispanic Races"])
    return age, sex, height, weight, ethnicity

def get_general_inputs():
    activity_level = st.selectbox("Mention your Activity level", ["Sedentary", "Moderately Active", "Active"])
    dietary_preference = st.text_input("Mention your Dietary Preference", "") # Modify after checking with Sai
    smoke_cig = st.selectbox("Do you Smoke Cigarettes?", ["Yes", "No"])
    mental_health = st.selectbox("Have you experienced any feelings of sadness, low mood, or hopelessness lately?", ["Not at all", "Occasionally these days", "Frequently these days", "Nearly every day these days"])
    sleep_hrs = st.number_input("How many hours do you think you slept yesterday?", min_value=0.0)
    health_condition = st.selectbox("Describe your current health condition", ["Excellent", "Very good", "Good", "Fair", "Poor"])
    diet_condition = st.selectbox("How healthy do you think is your diet?", ["Excellent", "Very good", "Good", "Fair", "Poor"])
    poor_appetite_overeating = st.selectbox("How often have you been bothered by poor appetite or overeating issues?", ["Not at all", "Occasionally these days", "Frequently these days", "Nearly every day these days"])
    return activity_level, dietary_preference, smoke_cig, mental_health, sleep_hrs, health_condition, diet_condition, poor_appetite_overeating

def write_user_inputs_to_csv(user_inputs):
    try:
        df = pd.DataFrame([user_inputs], columns=["age", "sex", "height", "weight", "ethnicity", "activity_level", "dietary_preference", "smoke_cig", "mental_health", "sleep_hrs", "health_condition", "diet_condition", "poor_appetite_overeating"])
        df.to_csv('user_inputs.csv', index=False)
        return True
    except Exception as e:
        return False
    
def get_user_inputs():
    col1, _, col3 = st.columns([1, 0.1, 1])
    with col1:
        age, sex, height, weight, ethnicity = get_demographic_inputs()
    with col3:
        activity_level, dietary_preference, smoke_cig, mental_health, sleep_hrs, health_condition, diet_condition, poor_appetite_overeating = get_general_inputs()
        
    user_inputs = [age, sex, height, weight, ethnicity, activity_level, dietary_preference, smoke_cig, mental_health, sleep_hrs, health_condition, diet_condition, poor_appetite_overeating]
    status = write_user_inputs_to_csv(user_inputs)    
    return status