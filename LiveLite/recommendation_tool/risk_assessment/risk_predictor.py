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
def risk_predict(Inputlist, model):
    
    # Load the trained model
    loaded_model = joblib.load(model)

    # Predict risk using the test data
    new_prediction = loaded_model.predict_proba(pd.DataFrame(Inputlist))[:, 1]  # Probability of class 1 (obese)
    
    obesityrisk = round(new_prediction[0] * 100, 1)
    
    return obesityrisk

# result = risk_predict(test_data)
# print(f'Predicted Obesity Risk: {result[0]} %, {result[1]}')


