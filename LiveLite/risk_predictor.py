"""
This module provides a function for predicting the risk of obesity 
based on input features and saved model.

Functions:
- risk_predict(): Predicts the risk of obesity.

"""
import pandas as pd
import joblib

def risk_predict(input_list):
    """
    Predicts the risk of obesity based on the input factors.

    Args:
        input_list (list): List of factors
    Raises:
        ValueError: If the input list is empty or if the input features
                    are not in the expected format.
        FileNotFoundError: If the model file is not found.
    Returns:
        tuple: A tuple containing the obesity risk percentage
               and corresponding risk color.
    """
    if not input_list:
        raise ValueError("Input list is empty")

    # Check if input features are in the expected format
    if not all(isinstance(feature, (int, float)) for feature in input_list):
        raise ValueError("Input features must be numeric")

    # Load the trained model
    try:
        loaded_model = joblib.load('obesity_risk_model.joblib')
    except FileNotFoundError as fnf:
        raise FileNotFoundError("Model file not found") from fnf

    # Probability of class 1 (obese)
    new_prediction = loaded_model.predict_proba(pd.DataFrame(input_list))[:, 1]

    obesity_risk = round(new_prediction[0] * 100, 1)

    if 0 <= obesity_risk <= 25:
        color = 'Blue'  # Low risk
    elif 25 < obesity_risk <= 50:
        color = 'Green'  # Moderate risk
    elif 50 < obesity_risk <= 75:
        color = 'Yellow'  # High risk
    else:
        color = 'Red'  # Very high risk

    return obesity_risk, color
