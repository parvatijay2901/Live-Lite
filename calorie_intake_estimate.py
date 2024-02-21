
def calculate_bmr(weight_kg, height_cm, age, sex):
    # Calculate Basal Metabolic Rate (BMR) based on weight, height, age, and sex.
    # Args:
    # weight (float): Weight in kilograms.
    # height (float): Height in centimeters.
    # age (int): Age in years.
    # sex (boolean) : Gender of the person. Either '0 - female' or '1 - male'.
    # Returns:
    # float: BMR value.
    
    if sex == 1:
        bmr = 66 + (6.3 * weight_kg) + (12.9 * height_cm) - (6.8 * age)
    
    elif sex == 0:
        bmr = 655 + (4.3 * weight_kg) + (4.7 * height_cm) - (4.7 * age)
    
    else:
        raise ValueError("Invalid value for sex")
    
    return bmr

def calculate_calorie_intake(weight_kg, height_cm, age, sex, activity_level):
    # Calculate total calorie intake based on BMR and activity level.
    # Args:
    # weight (float): Weight in kilograms.
    # height (float): Height in centimeters.
    # age (int): Age in years.
    # sex (boolean): Gender of the person. Either '0 - female' or '1 - male'.
    # activity_level (int): Level of physical activity. One of: '1-sedentary', '2-minimally active', '3-moderately active', '4-very active', '5-extra active'.
    # Returns:
    # float: Total calorie intake.
    try:
        bmr = calculate_bmr(weight_kg, height_cm, age, sex)
    
    except ValueError as ve:
        raise ValueError(ve)

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

'''
# Example usage : To be removed in final version of the code. Uncomment for test run    
# This call must be made from streamlit & output has to be rendered appropriately. 
calorie_intake = calculate_calorie_intake (float(56), float(150), int(30), 0, int(2))
print("Estimated calorie intake:", calorie_intake, "kcal")
'''
