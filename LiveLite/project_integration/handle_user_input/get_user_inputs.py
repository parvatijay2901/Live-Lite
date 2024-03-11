"""
Module that has functions to get general inputs (Obesity Assessment) from the user.

Functions:
- get_demographic_inputs(user_inputs): Function to get demographic inputs from the user
- get_general_inputs(user_inputs): Function to get general inputs from the user.
- write_user_inputs_to_csv(user_inputs, filename): Function to write user inputs to a CSV file.
- get_user_inputs: Function to get user inputs.
"""

import os
import streamlit as st
import pandas as pd

def get_demographic_inputs(user_inputs):
    """Function to get demographic inputs from the user.

    Args:
        user_inputs (dict): A dictionary containing user inputs.

    Returns:
        dict: A dictionary containing user inputs including demographic information.

    Raises:
        TypeError: If user_inputs is not a dictionary.
        ValueError: If any input values are invalid.
    """
    if not isinstance(user_inputs, dict):
        raise TypeError("Input 'user_inputs' must be a dictionary.")

    user_inputs['age'] = st.number_input("Age", min_value=18, step=1, max_value=120)
    user_inputs['sex'] = st.selectbox("Sex at Birth", ["Male", "Female"])
    col1, col2 = st.columns([1, 1])
    with col1:
        feet = st.number_input("Height (feet)", min_value=2.0, step=1.0, max_value=7.0)
    with col2:
        inches = st.number_input("Height (inches)")
    user_inputs['height'] = (feet * 12) + inches
    user_inputs['weight'] = st.number_input("Weight (lb)", min_value=20.0, step=1.0)
    user_inputs['ethnicity'] = st.selectbox("Self-identified Race/Ethnicity", [
                                                                "Hispanic",
                                                                "Mexican American",
                                                                "Non-Hispanic White",
                                                                "Non-Hispanic Black",
                                                                "Non-Hispanic Asian",
                                                                "Non-Hispanic Multiracial",
                                                                "Other Non-Hispanic Races"])

    return user_inputs

def get_general_inputs(user_inputs):
    """Function to get general inputs from the user.

    Args:
        user_inputs (dict): A dictionary containing user inputs.

    Returns:
        dict: A dictionary containing user inputs including general information.

    Raises:
        TypeError: If user_inputs is not a dictionary.
        ValueError: If any input values are invalid.
    """
    if not isinstance(user_inputs, dict):
        raise TypeError("Input 'user_inputs' must be a dictionary.")

    user_inputs['activity_level'] = st.selectbox("Mention your Activity level", ["Sedentary",
                                                                                "Minimally Active",
                                                                                "Moderately Active",
                                                                                "Active",
                                                                                "Extra Active"])
    user_inputs['smoke_cig'] = st.selectbox("Do you Smoke Cigarettes?", ["No", "Yes"])
    user_inputs['mental_health'] = st.selectbox("""Have you experienced any feelings of sadness,
                                                low mood, or hopelessness lately?""",
                                                ["Not at all",
                                                "Occasionally these days",
                                                "Frequently these days",
                                                "Nearly every day these days"])
    user_inputs['sleep_hrs'] = st.number_input("How many hours do you think you slept yesterday?",
                                                min_value=2.0,
                                                step=1.0,
                                                max_value=14.5)
    user_inputs['health_condition'] = st.selectbox("Describe your current health condition",
                                                ["Excellent", "Very good", "Good", "Fair", "Poor"])
    user_inputs['diet_condition'] = st.selectbox("How healthy do you think is your diet?",
                                                ["Excellent", "Very good", "Good", "Fair", "Poor"])
    user_inputs['poor_appetite_overeating'] = st.selectbox("""How often have you been bothered by
                                                        poor appetite or overeating issues?""",
                                                        ["Not at all",
                                                        "Occasionally these days",
                                                        "Frequently these days",
                                                        "Nearly every day these days"])
    return user_inputs

def write_user_inputs_to_csv(user_inputs, filename):
    """Function to write user inputs to a CSV file.

    Args:
        user_inputs (dict): A dictionary containing user inputs.
        filename (str): The filename to write to.

    Raises:
        TypeError: If user_inputs is not a dictionary or filename is not a string.
        ValueError: If filename is an empty string.
    """
    if not isinstance(user_inputs, dict):
        raise TypeError("Input 'user_inputs' must be a dictionary.")
    if not isinstance(filename, str):
        raise TypeError("Input 'filename' must be a string.")
    if not filename:
        raise ValueError("Input 'filename' cannot be an empty string.")

    file_exists = os.path.exists(filename)
    df = pd.DataFrame([user_inputs])
    if file_exists:
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, index=False)

def get_user_inputs():
    """Function to get user inputs.

    Returns:
        dict: A dictionary containing user inputs.

    Raises:
        ValueError: If any required inputs are missing.
        TypeError: If the return value of get_demographic_inputs() or
                get_general_inputs() is not a dictionary.
    """
    user_inputs = {}
    col1, _, col3 = st.columns([1, 0.1, 1])
    with col1:
        user_inputs = get_demographic_inputs(user_inputs)
        if not isinstance(user_inputs, dict):
            raise TypeError("user_inputs is not a dictionary.")
    with col3:
        user_inputs = get_general_inputs(user_inputs)
        if not isinstance(user_inputs, dict):
            raise TypeError("user_inputs is not a dictionary.")
    return user_inputs
