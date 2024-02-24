""" This module 

    Returns:
        _type_: _description_
"""
import pandas as pd
import joblib
def risk_predict(input_list):
    """_summary_

    Args:
        Inputlist (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Load the trained model
    loaded_model = joblib.load('obesity_risk_model.joblib')

    # Probability of class 1 (obese)
    new_prediction = loaded_model.predict_proba(pd.DataFrame(input_list))[:, 1]

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
