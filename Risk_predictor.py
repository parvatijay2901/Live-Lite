import pandas as pd
import joblib  

### TO BE DELETED AFTER TETSING ##
test_data = {
    'DPQ020': [0], 
    'DPQ050': [0], 
    'PAQ670': [5], 
    'DBQ700': [1], 
    'HUQ010': [1], 
    'RIAGENDR': [0], 
    'RIDAGEYR': [60],
    'RIDRETH3': [1], 
    'SMQ040': [0],
    'SLD012': [3]
}

# Call this function with dictionary of user input to preidct risk
def risk_predict(Inputlist):
    
    # Load the trained model
    loaded_model = joblib.load('obesity_risk_model.joblib')

    # Predict risk using the test data
    new_prediction = loaded_model.predict_proba(pd.DataFrame(test_data))[:, 1]  # Probability of class 1 (obese)
    
    Obesityrisk = round(new_prediction[0] * 100, 1)
    print(f'Predicted Obesity Risk: {Obesityrisk} %')
    return Obesityrisk
   

risk_predict(test_data)


