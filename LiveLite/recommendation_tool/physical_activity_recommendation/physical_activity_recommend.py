import pandas as pd

# Read data from the CSV file into a dataframe
df = pd.read_csv("calories_burned_30_minutes.csv")

# Custom function to choose a moderate calorie burn va;oe
def custom_median(series):
    sorted_values = series.sort_values()
    length = len(sorted_values)
    if length % 2 == 0:
        return sorted_values.iloc[length // 2 - 1]  # Return the first of the two center values
    else:
        return sorted_values.iloc[length // 2]

def calculate_calorie_burn(weight_lbs, intensity="moderate", preferred_activity=None):
    result = []

    if preferred_activity is None:
        # Choose the calorie based on the type of measure of intensity.
        if intensity == "moderate":
            chosen_calorie = df.groupby('Activity Type')['cal_per_lb_avg'].agg(custom_median).reset_index()
        elif intensity == "low":
            chosen_calorie = df.groupby('Activity Type')['cal_per_lb_avg'].min().reset_index()
        elif intensity == "high":
            chosen_calorie = df.groupby('Activity Type')['cal_per_lb_avg'].max().reset_index()
        else:
            raise ValueError("Invalid intensity level")

        print("Chosen calorie:")
        #print(chosen_calorie)

        # Calculate estimated calorie burn for the given weight input
        estimated_burn = chosen_calorie['cal_per_lb_avg'] * weight_lbs
        #print(estimated_burn)

        # Create list of tuples with activity type, activity, duration, and estimated burn calories
        for idx, row in chosen_calorie.iterrows():
            activity_type = row['Activity Type']
            cal_per_lb_avg = row['cal_per_lb_avg']

            # Get the records that match the chosen calorie value and activities
            activity = df.loc[(df['Activity Type'] == activity_type) & (df['cal_per_lb_avg'] == cal_per_lb_avg), 'Activity'].iloc[0]

            # Set default duration period
            duration = "30 min"

            # Fetch the corresponding calculated calorie value
            calories = estimated_burn.iloc[idx]
            result.append((activity_type, activity, duration, f"{calories:.0f} kcal"))

    else:
        chosen_record = df[df['Activity'].str.lower().str.contains(preferred_activity.lower())]
        #print("Chosen record:")
        #print(chosen_record)
        for idx, row in chosen_record.iterrows():
            activity_type = row['Activity Type']
            activity = row['Activity']
            duration = "30 min"
            calories = row['cal_per_lb_avg'] * weight_lbs
            result.append((activity_type, activity, duration, f"{calories:.0f} kcal"))

    return result

# Example usage:
output_list = calculate_calorie_burn(150)
print(output_list)
