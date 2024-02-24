def is_obese(height_cm, weight_kg):
    #Determines whether a person is obese based on their height (in cm) and weight (in kg).
    #Args:
    #height_cm (float): Height of the person in cm.
    #weight_kg (float): Weight of the person in kg.
    #Returns:
    #bool: True if the person is obese, False otherwise.
    
    try:
        # Convert height from centimeters to meters
        height_m = height_cm / 100

        # Calculate BMI (Body Mass Index)
        bmi = weight_kg / (height_m ** 2)

        # Check if BMI indicates obesity (BMI >= 30)
        return bmi >= 30
    
    except ZeroDivisionError:
        print("Error: Height can't be zero.")
        return False
    
    except Exception as e:
        print("An error occurred:", e)
        return False
'''
#Example usage
if is_obese(150, 80):
    print("The person is obese.")
else:
    print("The person is not obese.")
'''