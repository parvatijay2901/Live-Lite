import pandas as pd
import sys,os

path = './.'
sys.path.append(os.path.abspath(path))
from tool_integration.src.user_input_mapping import get_mapped_user_inputs
from recommendation_tool.obesity_risk_model.risk_score import generate_input_for_risk_score, generate_risk_score_display
from recommendation_tool.obesity_risk_model.Risk_predictor import risk_predict
from recommendation_tool.physical_activity_recommendation.physical_activity_recommend import calculate_calorie_burn
    

def read_user_inputs_from_csv(filename="user_inputs.csv"):
    try:
        df = pd.read_csv(filename)
        return df
    except Exception as err:
        pass # Add this section later

def controller(choice):
    user_inputs_df = read_user_inputs_from_csv()
    mapped_user_inputs = get_mapped_user_inputs(user_inputs_df) # To be modified based on the changed Manasa makes
    if choice == "risk_score":
        risk_predict_input = generate_input_for_risk_score(mapped_user_inputs)
        model = "recommendation_tool/obesity_risk_model/obesity_risk_model.joblib"
        risk_score = risk_predict(risk_predict_input, model)
        risk_score_display = generate_risk_score_display(risk_score)
        return risk_score_display
    if choice == "physical_activity_recommender":
        filename = "recommendation_tool/estimate_calorie_intake/calories_burned_30_minutes.csv"
        physical_activity_recommendendation = calculate_calorie_burn(mapped_user_inputs[3], filename, intensity="moderate", preferred_activity=None)
        return physical_activity_recommendendation
