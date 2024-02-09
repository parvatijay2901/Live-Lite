
def calculate_bmr(weight, height, age, sex):
    # Calculate Basal Metabolic Rate (BMR) based on weight, height, age, and sex.
    # Args:
    # weight (float): Weight in kilograms.
    # height (float): Height in centimeters.
    # age (int): Age in years.
    # sex (str): Gender of the person. Either 'male' or 'female'.
    # Returns:
    # float: BMR value.
    
    if sex.lower() == 'male':
        bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    
    elif sex.lower() == 'female':
        bmr = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    
    else:
        raise ValueError("Invalid value for sex. Please enter 'male' or 'female'.")
    
    return bmr

def calculate_calorie_intake(weight, height, age, sex, activity_level):
    # Calculate total calorie intake based on BMR and activity level.
    # Args:
    # weight (float): Weight in kilograms.
    # height (float): Height in centimeters.
    # age (int): Age in years.
    # sex (str): Gender of the person. Either 'male' or 'female'.
    # activity_level (str): Level of physical activity. One of: 'sedentary', 'minimally active', 'moderately active', 'very active', 'extra active'.
    # Returns:
    # float: Total calorie intake.
    try:
        bmr = calculate_bmr(weight, height, age, sex)
    
    except ValueError as ve:
        raise ValueError(ve)

    activity_multiplier = {
        'sedentary': 1.2,
        'minimally active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }
    
    activity_level_lower = activity_level.lower()
    
    if activity_level_lower not in activity_multiplier:
        raise ValueError("Invalid value for activity level. Please choose from: sedentary, minimally active, moderately active, very active, extra active.")
    
    calorie_intake = bmr * activity_multiplier[activity_level_lower]
    return calorie_intake


# Example usage : to be removed in final version of the code. Uncomment for test run
    '''
    enable for testing
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in cm: "))
    age = int(input("Enter age in years: "))
    sex = input("Enter sex (male/female): ")
    activity_level = input("Enter activity level: ")
    
   # This call must be made from streamlit & outout has to be rendered appropriately. 
    calorie_intake = calculate_calorie_intake(float(weight), float(height), int(age), sex, activity_level)
    print("Estimated calorie intake:", calorie_intake, "kcal")
'''

