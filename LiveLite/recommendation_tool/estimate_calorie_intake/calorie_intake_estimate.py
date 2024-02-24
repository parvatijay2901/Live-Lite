""" This module computes the bmr values & utilizes this bmr value to
    compute estimation of daily calorie intake for the user
"""
def calculate_bmr(weight_kg, height_cm, age, sex):
    """ Calculate BMR based on weight, height, age, and sex.

    Args:
        weight_kg (float): Weight in kilograms
        height_cm (float): Height in centimeters
        age (int): Age in years.
        sex (boolean): Gender of the person.'0 - female' or '1 - male'

    Raises:
        ValueError: Invalid gender value

    Returns:
        float: BMR value
    """

    if sex == 1:
        bmr = 66 + (6.3 * weight_kg) + (12.9 * height_cm) - (6.8 * age)
    elif sex == 0:
        bmr = 655 + (4.3 * weight_kg) + (4.7 * height_cm) - (4.7 * age)
    else:
        raise ValueError("Invalid value for sex")
    return bmr

def calculate_calorie_intake(weight_kg, height_cm, age, sex, activity_level):
    """ This function calculates the estimated calorie intake based on
        the user input data and bmr calculated.

    Args:
        weight_kg (float): Weight in kilograms
        height_cm (float): Height in centimeters
        age (int): Age in years.
        sex (boolean): Gender of the person. Either '0 - female' or '1 - male'
        activity_level (int): Activity level ranging from 1 - 5

    Raises:
        ValueError: Inavlid bmr
        ValueError: Invalid activity level 

    Returns:
        float: calorie intake in kcal
    """

    try:
        bmr = calculate_bmr(weight_kg, height_cm, age, sex)
    except ValueError as ve:
        raise ValueError(ve) from ve

    activity_multiplier = {
        1 : 1.2,
        2 : 1.375,
        3 : 1.55,
        4 : 1.725,
        5 : 1.9
    }

    if activity_level not in activity_multiplier:
        raise ValueError("Invalid value for activity level")

    calorie_intake = bmr * activity_multiplier[activity_level]
    return calorie_intake
