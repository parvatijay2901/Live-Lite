import pandas as pd
import joblib  

### TO BE DELETED AFTER TETSING ##
test_data = {
    'DPQ020': [3], # internal_mental_health
    'DPQ050': [3], # internal_poor_appetite_overeating
    'PAQ670': [1], # internal_days moderate recreational activities
    'DBQ700': [5], # internal_diet_condition
    'HUQ010': [5], # internal_health_condition
    'RIAGENDR': [0], # internal_sex
    'RIDAGEYR': [60], # internal_age
    'RIDRETH3': [3], # internal_ethnicity
    'SMQ040': [1], # internal_smoke_cig
    'SLD012': [2] # internal_sleep_hrs
}

# Call this function with dictionary of user input to predict risk
def risk_predict(Inputlist, model):
    
    # Load the trained model
    loaded_model = joblib.load(model)

    # Predict risk using the test data
    new_prediction = loaded_model.predict_proba(pd.DataFrame(test_data))[:, 1]  # Probability of class 1 (obese)
    
    Obesityrisk = round(new_prediction[0] * 100, 1)
    # print(f'Predicted Obesity Risk: {Obesityrisk} %')
    return Obesityrisk
   

# risk_predict(test_data)


