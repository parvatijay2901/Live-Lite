"""
This module contains functions that are designed to be used together
to predict and display risk scores for obesity based on user inputs.

Functions:
- get_input_for_risk_score (mapped_user_inputs: Prepares inputs for risk
                                                score prediction based on user inputs.
- display_risk_score (risk_score, color): Displays the risk score using an SVG donut plot.
- display_risk_suggestion (risk_score): Displays suggestions based on the risk score.
"""

import streamlit as st

def get_input_for_risk_score(mapped_user_inputs):
    """Function to prepare inputs for risk score prediction.

    Args:
        mapped_user_inputs (dict): A dictionary containing user inputs.

    Returns:
        dict: A dictionary containing risk prediction inputs.

    Raises:
        TypeError: If the input mapped_user_inputs is not a dictionary.
        ValueError: If any required keys are missing in the
                    mapped_user_inputs dictionary.
    """
    if not isinstance(mapped_user_inputs, dict):
        raise TypeError("Input 'mapped_user_inputs' must be a dictionary.")

    # Make sure that all the required arguments are present in user input
    required_keys = ['internal_mental_health', 'internal_poor_appetite_overeating',
                    'internal_activity_level', 'internal_diet_condition',
                    'internal_health_condition', 'internal_sex', 'internal_age',
                    'internal_ethnicity', 'internal_smoke_cig', 'internal_sleep_hrs']
    if not all(key in mapped_user_inputs for key in required_keys):
        raise ValueError("Input dictionary 'mapped_user_inputs' is missing required keys.")

    # Generate input dict to predict obesity risk
    risk_predict_input = {
        'DPQ020': [mapped_user_inputs['internal_mental_health']],
        'DPQ050': [mapped_user_inputs['internal_poor_appetite_overeating']],
        'PAQ670': [mapped_user_inputs['internal_activity_level']],
        'DBQ700': [mapped_user_inputs['internal_diet_condition']],
        'HUQ010': [mapped_user_inputs['internal_health_condition']],
        'RIAGENDR': [mapped_user_inputs['internal_sex']],
        'RIDAGEYR': [mapped_user_inputs['internal_age']],
        'RIDRETH3': [mapped_user_inputs['internal_ethnicity']],
        'SMQ040': [mapped_user_inputs['internal_smoke_cig']],
        'SLD012': [mapped_user_inputs['internal_sleep_hrs']]
    }
    return risk_predict_input

def display_risk_score(risk_score, color):
    """Function to display the risk score.

    Args:
        risk_score (float): The risk score.
        color (str): The color.

    Returns:
        str: SVG representing the risk score display.

    Raises:
        TypeError: If risk_score is not a float value or color is not a string.
        ValueError: If risk_score is negative.
    """
    if not isinstance(risk_score, float):
        raise TypeError("Input 'risk_score' must be a float value.")

    if not isinstance(color, str):
        raise TypeError("Input 'color' must be a string.")

    if risk_score < 0:
        raise ValueError("Input 'risk_score' cannot be negative.")

    # Modify risk_score text to be displayed
    if risk_score < 100:
        risk_score = str(risk_score) + "%"
    elif risk_score == 100:
        risk_score = "Obese"
    else:
        raise ValueError("Input 'risk_score' cannot be more than 100")

    # Design a donut plot with risk_score displayed in centre
    donut_plot = f"""<div style="width: 250px; height: 250px;">
    <svg width="250" height="250" viewBox="0 0 250 250">
    <!-- Outer circle (ring) -->
    <circle cx="125" cy="125" r="100" fill="none" stroke={color} stroke-width="50" />
    <!-- Inner circle (center) -->
    <circle cx="125" cy="125" r="50" fill="none" />
    <!-- Text showing the risk score -->
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="30" font-weight="bold" fill="white">{risk_score}</text>
    </svg>
    </div>
    """
    st.markdown(donut_plot, unsafe_allow_html=True)
    return donut_plot

def display_risk_suggestion(risk_score):
    """Function to display risk suggestions based on the risk score.

    Args:
        risk_score (float): The risk score.

    Raises:
        TypeError: If risk_score is not a float value.
        ValueError: If risk_score is negative.
    """
    if not isinstance(risk_score, float):
        raise TypeError("Input 'risk_score' must be a float value.")

    if risk_score < 0:
        raise ValueError("Input 'risk_score' cannot be negative.")

    # Based on the risk_score, generate a risk_suggestion
    if risk_score <= 25:
        text = f"""Based on your assessment, your risk of obesity
        is currently low at {risk_score}%. To maintain this healthy level, why not explore
        our tips for delicious and nutritious meals, and discover fun ways to stay active?"""
    elif 25 < risk_score <= 50:
        text = f"""Your current risk of obesity is moderate at {risk_score}%. This is a good
        opportunity to explore ways to optimize your health further. We have some helpful
        resources for balanced eating and enjoyable physical activities that can make a
        positive difference."""
    elif 50 < risk_score <= 75:
        text = f"""Based on your assessment, your risk of obesity is currently high at
        {risk_score}%. This may be a good time to consider some lifestyle changes.
        We have a collection of personalized recommendations for healthy eating and physical
        activity that can help you reach your goals."""
    elif 75 < risk_score <= 99:
        text = f"""Your risk of obesity is currently very high at {risk_score}%.
        It's important to take steps to address this for your overall well-being.
        We understand this can be challenging, but we're here to support you with
        personalized guidance on healthy eating and physical activity. Let's work
        together to achieve your health goals."""
    else:
        text = """It's essential to recognize that everyone's health journey is unique,
        and it's okay to start small. Making positive changes, no matter how small,
        can have a significant impact on your overall well-being. We're here to provide
        personalized support and guidance to help you make healthier choices in both your
        eating habits and physical activity. Let's work together to achieve your health goals at a
        pace that feels comfortable for you."""

    text = f"<center>{text}</center>"
    st.markdown(text, unsafe_allow_html=True)
