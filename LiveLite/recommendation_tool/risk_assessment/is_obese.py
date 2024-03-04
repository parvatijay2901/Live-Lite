"""
This moduled checks if the user is obese or not.
"""
def is_obese(height_cm, weight_kg):
    """
    Determines whether a person is obese based on their 
    height (in cm) and weight (in kg).
    Args:
        height_cm (float): Height of the person in cm.
        weight_kg (float): Weight of the person in kg.
    Raises:
        ValueError: If height_cm or weight_kg is not a positive number.
    Returns:
        bool: True if the person is obese, False otherwise.
    """
    if not isinstance(height_cm, (int,float)) or height_cm <= 0 :
        raise ValueError("Height must be a positive number")

    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        raise ValueError("Weight must be a positive number")

    height_m = height_cm / 100
    # Calculate BMI (Body Mass Index)
    bmi = weight_kg / (height_m ** 2)
    # Person is obese if BMI is >= 30
    return bmi >= 30
