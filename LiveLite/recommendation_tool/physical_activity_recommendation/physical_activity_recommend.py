"""
This module provides functions to calculate estimated calorie burn
based on weight and activity intensity.

Functions:
- custom_median(): Calculates the median of a given series.
- calculate_calorie_burn(): Calculates estimated calorie burn
                            based on weight and activity intensity.
"""

import pandas as pd

def custom_median(series):
    """
    Calculate the median of a given series.
    Args:
        series (pandas.Series): The input series for which median is to be calculated.
    Returns:
        float: The median of the series.
    """
    sorted_values = series.sort_values()
    length = len(sorted_values)
    if length % 2 == 0:
        return sorted_values.iloc[length // 2 - 1]
    return sorted_values.iloc[length // 2]

# pylint: disable=too-many-locals
# Disbaling the pylint too many locals check, as the code is fully readable
# and needs local variables for data processing.
def calculate_calorie_burn(filename, weight_kg, intensity="moderate", preferred_activity=None):
    """
    Calculate estimated calorie burn based on weight and activity intensity.
    Args:
        filename (str): Input csv file.
        weight_kg (float): Weight in kilograms.
        intensity (str, optional): Intensity level of the activity. Defaults to "moderate".
        preferred_activity (str, optional): Preferred activity. Defaults to None.
    Raises:
        ValueError: If the intensity level is invalid.
    Returns:
        list of tuples: List containing tuples of activity type, 
                        activity, duration, and estimated burn calories.
    """
    result = []

    df = pd.read_csv(filename)

    if preferred_activity is None:
        # Choose the calorie based on the type of measure of intensity.
        if intensity == "moderate":
            chosen_calorie = (df.groupby('Activity Type')['cal_per_kg_avg']
                              .agg(custom_median).reset_index())
        elif intensity == "low":
            chosen_calorie = (df.groupby('Activity Type')['cal_per_kg_avg']
                              .min().reset_index())
        elif intensity == "high":
            chosen_calorie = (df.groupby('Activity Type')['cal_per_kg_avg']
                              .max().reset_index())
        else:
            raise ValueError("Invalid intensity level")

        # Calculate estimated calorie burn for the given weight input
        estimated_burn = chosen_calorie['cal_per_kg_avg'] * weight_kg

        # Create list of tuples with activity type, activity, duration, and estimated burn calories
        for idx, row in chosen_calorie.iterrows():
            activity_type = row['Activity Type']
            cal_per_kg_avg = row['cal_per_kg_avg']

            # Get the records that match the chosen calorie value and activities
            activity = (df.loc[(df['Activity Type'] == activity_type)
                        & (df['cal_per_kg_avg'] == cal_per_kg_avg)
                        ,'Activity'].iloc[0])

            duration = "30 min"

            # Fetch the corresponding calculated calorie value
            calories = estimated_burn.iloc[idx]
            result.append((activity_type, activity, duration, f"{calories:.0f} kcal"))

    else:
        chosen_record = df[df['Activity'].str.lower().str.contains(preferred_activity.lower())]

        if chosen_record.empty:
            raise ValueError(f"No records found for preferred activity: {preferred_activity}")

        for idx, row in chosen_record.iterrows():
            activity_type = row['Activity Type']
            activity = row['Activity']
            duration = "30 min"
            calories = row['cal_per_kg_avg'] * weight_kg
            result.append((activity_type, activity, duration, f"{calories:.0f} kcal"))

    return result
