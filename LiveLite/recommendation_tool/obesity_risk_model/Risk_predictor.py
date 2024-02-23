import pandas as pd
import joblib  

# # ### TO BE DELETED AFTER TETSING ##
# test_data = {
#     'DPQ020': [3], 
#     'DPQ050': [3], 
#     'PAQ670': [1], 
#     'DBQ700': [5], 
#     'HUQ010': [5], 
#     'RIAGENDR': [0], 
#     'RIDAGEYR': [60],
#     'RIDRETH3': [3], 
#     'SMQ040': [1],
#     'SLD012': [2]
# }

# Call this function with dictionary of user input to preidct risk
def risk_predict(Inputlist):
    
    # Load the trained model
    loaded_model = joblib.load('obesity_risk_model.joblib')

    # Predict risk using the test data
    new_prediction = loaded_model.predict_proba(pd.DataFrame(test_data))[:, 1]  # Probability of class 1 (obese)
    
    obesityrisk = round(new_prediction[0] * 100, 1)
    
    if 0 <= obesityrisk <= 25:
        color = 'Blue'  # Low risk
    elif 25 < obesityrisk <= 50:
        color = 'Green'  # Moderate risk
    elif 50 < obesityrisk <= 75:
        color = 'Yellow'  # High risk
    else:
        color = 'Red'  # Very high risk
    
    return obesityrisk, color

# result = risk_predict(test_data)
# print(f'Predicted Obesity Risk: {result[0]} %, {result[1]}')


