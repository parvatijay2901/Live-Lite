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

    color = interpolate_color(obesity_risk)

    return obesity_risk, color

def interpolate_color(value):
    """
    Interpolate between two RGB colors, pastel red and pastel green
    with pastel yellow as intermediate color.
    
    Args:
        value (int): Value used to determine the color
    Returns:
        hex_color (str): Hex code for a color corresponding
                         to the value.
    """
    if value <= 50:
        red = int(119 + (251 - 119) * value / 50)
        green = int(221 + (251 - 221) * value / 50)
        blue = int(119 + (99 - 119) * value / 50)
    else:
        red = int(251 + (255 - 251) * (value - 50) / 50)
        green = int(251 + (105 - 251) * (value - 50) / 50)
        blue = int(99 + (97 - 99) * (value - 50) / 50)

    hex_color = f'#{red:02x}{green:02x}{blue:02x}'

    return hex_color
