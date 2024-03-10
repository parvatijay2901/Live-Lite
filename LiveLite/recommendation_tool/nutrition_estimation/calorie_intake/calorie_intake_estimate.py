""" 
This module computes estimation of daily calorie intake for the user.

Functions:
- calculate_bmr()
- calculate_calorie_intake()
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
        bmr = 88.4 + (13.3 * weight_kg) + (4.8 * height_cm) - (5.7 * age)
    elif sex == 0:
        bmr = 447.6 + (9.2 * weight_kg) + (3 * height_cm) - (4.3 * age)
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
        TypeError: If weight, height, or age are not positive numbers.
        ValueError: Invalid activity level.
        ValueError: Invalid BMR.

    Returns:
        float: calorie intake in kcal
    """
    if not isinstance(age, int) or age <= 0:
        raise TypeError("Age must be a positive whole number")

    if not isinstance(height_cm, (int,float)) or height_cm <= 0 :
        raise TypeError("Height must be a positive number")

    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        raise TypeError("Weight must be a positive number")

    try:
        bmr = calculate_bmr(weight_kg, height_cm, age, sex)
    except ValueError as val_err:
        raise ValueError(val_err) from val_err

    # Different multiplier for each activity level.
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
