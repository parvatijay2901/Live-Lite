import streamlit as st
import pandas as pd
import LiveLite
    
def controller(choice):
    
    if 'user_inputs' not in st.session_state or 'food_nutrition_data' not in st.session_state:
        st.switch_page("Home.py")
        
    user_inputs = st.session_state['user_inputs']
    mapped_user_inputs = LiveLite.user_input_mapping(user_inputs)
    
    if choice == "estimate_calorie_intake":
        calorie_intake = LiveLite.calculate_calorie_intake(mapped_user_inputs['internal_weight'],
                                                                    mapped_user_inputs['internal_height'],
                                                                    mapped_user_inputs['internal_age'],
                                                                    mapped_user_inputs['internal_sex'],
                                                                    mapped_user_inputs['internal_activity_level'])
        return calorie_intake
    
    if choice == "risk_score":
        is_obese = LiveLite.is_obese(mapped_user_inputs['internal_height'], mapped_user_inputs['internal_weight'])
        if is_obese:
            risk_score = 100
            color = '#ff6242'
        else:
            risk_predict_input = LiveLite.get_input_for_risk_score(mapped_user_inputs)
            model = "LiveLite/recommendation_tool/risk_assessment/trained_models/obesity_risk_model.joblib"
            risk_score, color = LiveLite.risk_predict(risk_predict_input, model)
        return risk_score, color
    
    if choice == "diet_recommender_basic":
        macro_nutrients_df = LiveLite.macro_nutrients_data(mapped_user_inputs['internal_age'], mapped_user_inputs['internal_sex'], st.session_state['calorie_intake'])
        micro_nutrients_df = LiveLite.micro_nutrients(mapped_user_inputs['internal_age'], mapped_user_inputs['internal_sex'])
        return [macro_nutrients_df, micro_nutrients_df]

    if choice == "diet_recommender_advanced_based_on_food_preference":
        food_nutrition_data = st.session_state['food_nutrition_data']
        risk_score = st.session_state['risk_score']
        food_preference = st.session_state['food_preference']
        recommended_foods_df = LiveLite.recommended_food(food_nutrition_data, risk_score, food_preference)
        return recommended_foods_df
    
    if choice == "diet_recommender_advanced_search_food_items":
        food_nutrition_data = st.session_state['food_nutrition_data']
        search_food_items = st.session_state['search_food_items']
        searched_foods_df = LiveLite.search_food(food_nutrition_data, search_food_items)
        return searched_foods_df
    
    if choice == "physical_activity_recommender":
        filename = "LiveLite/data/input_files/calories_burned_30_minutes.csv"
        intensity = st.session_state['preferred_exercise_intensity_level']
        print(intensity)
        physical_activity_recommendendation_list = LiveLite.calculate_calorie_burn(filename, mapped_user_inputs['internal_weight'], intensity=intensity)
        print(physical_activity_recommendendation_list)
        physical_activity_recommendendation_df = pd.DataFrame(physical_activity_recommendendation_list, columns=["Activity Type", "Activity Name", "Duration", "Calories Expended"])
        return physical_activity_recommendendation_df