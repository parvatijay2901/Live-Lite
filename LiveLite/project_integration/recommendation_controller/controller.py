import streamlit as st
import pandas as pd
import project_integration
import recommendation_tool
    
def controller(choice):
    
    if 'user_inputs' not in st.session_state:
        st.switch_page("pages/2_obesity_assessment.py")
        
    user_inputs = st.session_state['user_inputs']
    mapped_user_inputs = project_integration.user_input_mapping(user_inputs)
    
    if choice == "risk_score":
        is_obese = recommendation_tool.is_obese(mapped_user_inputs['internal_height'], mapped_user_inputs['internal_weight'])
        if is_obese:
            risk_score = 100
        else:
            risk_predict_input = project_integration.get_input_for_risk_score(mapped_user_inputs)
            model = "./recommendation_tool/risk_assessment/trained_models/obesity_risk_model.joblib"
            risk_score = recommendation_tool.risk_predict(risk_predict_input, model)
        return risk_score
    
    if choice == "physical_activity_recommender":
        filename = "./data/input_files/calories_burned_30_minutes.csv"
        intensity = st.session_state['preferred_exercise_intensity_level']
        physical_activity_recommendendation_list = recommendation_tool.calculate_calorie_burn(filename, mapped_user_inputs['internal_weight'], intensity=intensity)
        physical_activity_recommendendation_df = pd.DataFrame(physical_activity_recommendendation_list, columns=["Activity Type", "Activity Name", "Duration", "Calories Expended"])
        return physical_activity_recommendendation_df
