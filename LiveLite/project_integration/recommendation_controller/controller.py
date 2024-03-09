"""_summary_

Returns:
    _type_: _description_
"""
import streamlit as st
import pandas as pd
import LiveLite # pylint: disable=import-error
def controller(choice):
    """Function to control different choices and return corresponding results.

    Args:
        choice (str): The choice made by the user.

    Returns:
        list: A list containing the result(s) based on the choice.
    """
    if 'user_inputs' not in st.session_state or 'food_nutrition_data' not in st.session_state:
        st.switch_page("app.py")

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
        is_obese = LiveLite.is_obese(mapped_user_inputs['internal_height'],
                                    mapped_user_inputs['internal_weight'])
        if is_obese:
            risk_score = 100
            color = '#ff6961'
        else:
            risk_predict_input = LiveLite.get_input_for_risk_score(mapped_user_inputs)
            risk_score, color = LiveLite.risk_predict(risk_predict_input,
            "LiveLite/recommendation_tool/risk_assessment/trained_models/obesity_risk_model.joblib")
        return risk_score, color

    if choice == "recommender_basic":
        macro_nutrients_df = LiveLite.macro_nutrients_data(mapped_user_inputs['internal_age'],
                                                        mapped_user_inputs['internal_sex'],
                                                        st.session_state['calorie_intake'])
        micro_nutrients_df = LiveLite.micro_nutrients(mapped_user_inputs['internal_age'],
                                                    mapped_user_inputs['internal_sex'])

        physical_activity_list = LiveLite.calculate_calorie_burn(
            "LiveLite/data/input_files/calories_burned_30_minutes.csv",
            mapped_user_inputs['internal_weight'],
            intensity=st.session_state['preferred_exercise_intensity_level'])
        physical_activity_df = pd.DataFrame(physical_activity_list,
                                            columns=["Activity Type",
                                                    "Activity Name",
                                                    "Duration",
                                                    "Calories Expended"])
        return [macro_nutrients_df, micro_nutrients_df, physical_activity_df]

    if choice == "diet_recommender_advanced_based_on_food_preference":
        recommended_foods_df = LiveLite.recommended_food(st.session_state['food_nutrition_data'],
                                                        st.session_state['risk_score'],
                                                        st.session_state['food_preference'])
        return recommended_foods_df

    if choice == "diet_recommender_advanced_search_food_items":
        searched_foods_df = LiveLite.search_food(st.session_state['food_nutrition_data'],
                                                st.session_state['search_food_items'])
        return searched_foods_df

    return None
