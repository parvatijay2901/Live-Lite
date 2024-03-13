"""
This module provides a function for mapping user input data to internal representations
and Ml model usage.

Functions:
- user_input_mapping():
"""
def convert_age(age):
    """
    Convert age as per NHANES standards, restrciting values to 80
    Args:
        Age (int): The gender to be converted.
    Returns:
        int: number representing age
    """
    if age > 80:
        return 80
    return int(age)

def convert_sex(sex):
    """
    Convert the gender to a numerical representation.
    Args:
        sex (str): The gender to be converted.
    Returns:
        int: Numerical representation of gender (1 for male, 0 for female).
    Raises:
        ValueError: If the provided sex value is not 'male' or 'female'.
    """
    if sex.lower() == 'male':
        return 1
    if sex.lower() == 'female':
        return 0
    raise ValueError("Invalid value for sex")

def convert_ethnicity(ethnicity):
    """
    Convert the ethnicity to a numerical representation.
    Args:
        ethnicity (str): The ethnicity value to be converted.
    Returns:
        int: Numerical representation of ethnicity as defined by NHANES.
    Raises:
        ValueError: If the provided value is not in dictionary.
    """
    ethnicity_map = {
        'mexican american': 1,
        'hispanic': 2,
        'non-hispanic white': 3,
        'non-hispanic black': 4,
        'non-hispanic asian': 6,
        'other non-hispanic races': 5,
        'non-hispanic multiracial': 7
    }
    ethnicity_lower = ethnicity.lower()
    if ethnicity_lower in ethnicity_map:
        return int(ethnicity_map[ethnicity_lower])
    raise ValueError("Invalid value for ethnicity")

def convert_activity_level(activity_level):
    """
    Convert the activity level to a numerical representation.
    Args:
        activity_level (str): The actvity level to be converted.
    Returns:
        int: Numerical representation of activity level as defined by NHANES.
    Raises:
        ValueError: If the provided value is not in dictionary.
    """
    activity_map = {
        'sedentary': 1,
        'minimally active': 2,
        'moderately active': 3,
        'active': 4,
        'extra active': 5
    }
    activity_lower = activity_level.lower()
    if activity_lower in activity_map:
        return int(activity_map[activity_lower])
    raise ValueError("Invalid value for activity level")

def convert_sleep_hours(sleep_hours):
    """
    Restrict the sleep hours to valid values between 2 to 14
    Args:
        sleep_hours (int): The sleep hours factor to be processed.
    Returns:
        int: Numerical representation of sleep hours.
    """
    if sleep_hours < 2:
        return 2
    if sleep_hours > 14:
        return 14
    return int(sleep_hours)

def convert_health_condition(health_condition):
    """
    Convert the general health to a numerical representation.
    Args:
        mental_health (str): The health factor to be converted.
    Returns:
        int: Numerical representation of health factor.
    Raises:
        ValueError: If the provided value is not in dictionary.
    """
    health_map = {
        'excellent': 1,
        'very good': 2,
        'good': 3,
        'fair': 4,
        'poor': 5
    }
    health_lower = health_condition.lower()
    if health_lower in health_map:
        return int(health_map[health_lower])
    raise ValueError("Invalid value for health condition")

def convert_mental_health(mental_health):
    """
    Convert the depression factor to a numerical representation.
    Args:
        mental_health (str): The depression factor to be converted.
    Returns:
        int: Numerical representation of depression factor.
    Raises:
        ValueError: If the provided value is not in dictionary.
    """
    mental_map = {
        'not at all': 0,
        'occasionally these days': 1,
        'frequently these days': 2,
        'nearly every day these days': 3
    }
    mental_lower = mental_health.lower()
    if mental_lower in mental_map:
        return int(mental_map[mental_lower])
    raise ValueError("Invalid value for mental health")

def user_input_mapping(user_data_dict):
    """
    Maps user input data to internal representations.
    Args:
        user_data_dict (dict): A dictionary containing user input data.
    Raises:
        ValueError: If any input value is invalid.
    Returns:
        dict: A dictionary containing mapped internal
            representations of user input data.
    """
    internal_data = {}

    internal_data['internal_age'] = convert_age(user_data_dict['age'])
    internal_data['internal_sex'] = convert_sex(user_data_dict['sex'])
    # Convert height to cm.
    internal_data['internal_height'] = float(user_data_dict['height'] * 2.54)
    # Convert weight to kg.
    internal_data['internal_weight'] = float(user_data_dict['weight'] * 0.45359237)
    internal_data['internal_ethnicity'] = convert_ethnicity(user_data_dict['ethnicity'])
    internal_data['internal_activity_level'] = convert_activity_level(
                                            user_data_dict['activity_level'])
    internal_data['internal_smoke_cig'] = int(user_data_dict['smoke_cig'].lower() == 'yes')
    internal_data['internal_mental_health'] = convert_mental_health(
                                            user_data_dict['mental_health'])
    internal_data['internal_sleep_hrs'] = convert_sleep_hours(
                                        float(user_data_dict['sleep_hrs']))
    internal_data['internal_health_condition'] = convert_health_condition(
                                                user_data_dict['health_condition'])
    internal_data['internal_diet_condition'] = convert_health_condition(
                                            user_data_dict['diet_condition'])
    internal_data['internal_poor_appetite_overeating'] = convert_mental_health(
                                                        user_data_dict['poor_appetite_overeating'])
    return internal_data
