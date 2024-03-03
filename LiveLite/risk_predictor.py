"""
This module provides a function for predicting the risk of obesity 
based on input features and saved model.

Functions:
- risk_predict()

"""
import pandas as pd
import joblib

def risk_predict(input_dict, model):
    """
    Predicts the risk of obesity based on the input factors.

    Args:
        input_list (list): List of factors
        model (str): saved model full path name
    Raises:
        ValueError: If the input list is empty or if the input features
                    are not in the expected format.
        FileNotFoundError: If the model file is not found.
    Returns:
        tuple: A tuple containing the obesity risk percentage
               and corresponding risk color.
    """
    if not input_dict:
        raise ValueError("Input list is empty")

    # Check if input features are in the expected format
    if not all(isinstance(value[0], int) for value in input_dict.values()):
        raise TypeError("Input features must be numeric")

    # Load the trained model
    try:
        loaded_model = joblib.load(model)
    except FileNotFoundError as fnf:
        raise FileNotFoundError("Model file not found") from fnf

    # Probability of class 1 (obese)
    new_prediction = loaded_model.predict_proba(pd.DataFrame(input_dict))[:, 1]

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
