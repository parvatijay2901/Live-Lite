""" This module is created to define various methods related to diet and nutrition
below are functions to calculate recommended quantity of food groups to consume per day
the functions will raise appropriate value and type errors for Age, gender and calories.
"""
# this module is created to define various methods related to diet and nutrition
# below are functions to print recommended quantity of food groups to consume per day
# the functions will return none when input is not valid
import pandas as pd

def recommended_protein(age_in,gender_in):
    """This function returns the recommended protein intake based on age and gender
    """
    if not isinstance(age_in, int):
        raise TypeError("age should be an integer.")
    if not isinstance(gender_in, int):
        raise TypeError("gender encoding should be an integer.")
    if not 18 <= age_in <= 100:
        raise ValueError("age not in expected range.")
    if gender_in not in [0, 1]:
        raise ValueError("gender not in expected value.")

    min_protein = 0
    max_protein = 0

    if gender_in ==0:
        if 18 <= age_in <= 30:
            min_protein =2
            max_protein =4.5
        if age_in > 30:
            min_protein =2
            max_protein =4

    if gender_in ==1:
        if 18<= age_in <= 30:
            min_protein = 3.5
            max_protein = 5
        if 30 < age_in <=59:
            min_protein = 3
            max_protein= 5
        if age_in > 59:
            min_protein = 2.5
            max_protein = 4.5

    return(round(min_protein*28.34), round(max_protein*28.34))

def recommended_grains(age_in,gender_in):
    """This function calculates the recommended amount of grains per day
    """
    if not isinstance(age_in, int):
        raise TypeError("age should be an integer.")
    if not isinstance(gender_in, int):
        raise TypeError("gender encoding should be an integer.")
    if not 18 <= age_in <= 100:
        raise ValueError("age not in expected range.")
    if gender_in not in [0, 1]:
        raise ValueError("gender not in expected value.")

    min_g = 0
    min_wg =0
    max_g = 0
    max_wg = 0

    if gender_in ==0:
        if 18 <= age_in <= 30:
            min_g = 6
            min_wg =3
            max_g = 8
            max_wg = 4

        if age_in > 30:
            min_g = 5
            min_wg = 3
            max_g = 7
            max_wg = 3.5

    if gender_in ==1:
        if 18 <= age_in <= 60:
            min_g = 7
            min_wg = 3.5
            max_g = 10
            max_wg = 5

        if age_in > 60:
            min_g = 6
            min_wg = 3
            max_g = 9
            max_wg = 4.5
    return(round(min_g*28.34), round(max_g*28.34), round(min_wg*28.34), round(max_wg*28.34))

def recommended_fat(calorie):
    """This function returns the amount of fat to be consumed per day in grams.
    """
    if not isinstance(calorie, (float,int)):
        raise TypeError("calorie should be a float value")
    if not 0 <= calorie:
        raise ValueError("calorie should be more than 0.")
    if calorie <= 2000 :
        fat = 50

    if 2000< calorie <= 2500 :
        fat = 67

    if calorie > 2500:
        fat = 83
    return fat

def recommended_fruits(gender_in):
    """This function returns the cups of fruits to be consumed in a day
    """
    if not isinstance(gender_in, int):
        raise TypeError("gender encoding should be an integer.")
    if gender_in not in [0, 1]:
        raise ValueError("gender not in expected value.")
    if gender_in == 0:
        return(1.5,2)
    if gender_in ==1:
        return(2,2.5)
    return None

def recommended_vegetables(age_in,gender_in):
    """This function returns the cups of vegetables to be consumed in a day
    """
    if not isinstance(age_in, int):
        raise TypeError("age should be an integer.")
    if not isinstance(gender_in, int):
        raise TypeError("gender encoding should be an integer.")
    if not 18 <= age_in <= 100:
        raise ValueError("age not in expected range.")
    if gender_in not in [0, 1]:
        raise ValueError("gender not in expected value.")

    min_veg = 0
    max_veg = 0

    if gender_in ==1:
        if 18<= age_in <= 60:
            min_veg = 3
            max_veg = 4

        if age_in > 60:
            min_veg = 2.5
            max_veg = 3.5
    if gender_in == 0:
        if 18<= age_in <= 30:
            min_veg = 2.5
            max_veg = 3

        if age_in > 30:
            min_veg = 2
            max_veg = 3

    return(min_veg, max_veg)

def macro_calorie(macro,calorie):
    """This function returns the calorie of each macro nutrients to be consumed in  a day
    """
    if not isinstance(macro, str):
        raise TypeError("food preference should be a string")
    if not isinstance(calorie, (float,int)):
        raise TypeError("calorie should be a float value")
    if macro not in ["protein", "carbohydrate", "fat"]:
        raise ValueError("Invalid macro nutrient!")
    if not 0 <= calorie:
        raise ValueError("calorie should be more than 0.")
    min_calorie = 0
    max_calorie = 0
    if macro == "protein":
        min_calorie = 0.1*calorie
        max_calorie = 0.3*calorie

    if macro == "carbohydrate":
        min_calorie = 0.45*calorie
        max_calorie = 0.65*calorie

    if macro == "fat":
        min_calorie = 0.2*calorie
        max_calorie = 0.3*calorie

    return(round(min_calorie), round(max_calorie))

#functions below returns a dataframe for recommended calrie and macro nutrient portion per day
def macro_nutrients_data(age, gender, calorie):
    """ This function calculate the necessary macro nutrients quantity and reutrns a dataframe
    based on input parameters age, gender and calories.
    """
    if not isinstance(gender, int):
        raise TypeError("gender encoding should be an integer.")
    if not isinstance(calorie, (float,int)):
        raise TypeError("calorie should be a float value")
    if not isinstance(age, int):
        raise TypeError("age should be an integer.")
    if not 18 <= age <= 100:
        raise ValueError("age not in expected range.")
    if gender not in [0, 1]:
        raise ValueError("gender not in expected value.")
    if not 0 <= calorie:
        raise ValueError("calorie should be more than 0.")

    carb_quantity = (f"{recommended_grains(age, gender)[0]}-{recommended_grains(age, gender)[1]}"
                     f"g of carbs/grains of which"
                     f"{recommended_grains(age, gender)[2]}-{recommended_grains(age, gender)[3]}"
                     f" of whole grains")
    protein_quantity = (f"{recommended_protein(age, gender)[0]}-"
                        f"{recommended_protein(age, gender)[1]}"
                        f" grams")
    fat_quantity = f'{recommended_fat(calorie)} grams'
    carbohydrate_calorie = macro_calorie("carbohydrate", calorie)
    protein_calorie = macro_calorie("protein", calorie)
    fat_calorie = macro_calorie("fat", calorie)

    data = {
        'Macro Nutrient': ['Carbohydrate', 'Protein', 'Fat'],
        'Quantity in Grams': [carb_quantity, protein_quantity, fat_quantity],
        'Kcal': [f'{carbohydrate_calorie[0]} - {carbohydrate_calorie[1]}',
                 f'{protein_calorie[0]} - {protein_calorie[1]}'
                 , f'{fat_calorie[0]} - {fat_calorie[1]}']
    }
    df = pd.DataFrame(data)
    return df

def micro_nutrients(age, gender):
    """This function take in age and gender and returns the dataframe containing the
    recommended quantity of fruits, vegetables and dairy.
    """
    if not isinstance(age, int):
        raise TypeError("age should be an integer.")
    if not isinstance(gender, int):
        raise TypeError("gender encoding should be an integer.")
    if not 18 <= age <= 100:
        raise ValueError("age not in expected range.")
    if gender not in [0, 1]:
        raise ValueError("gender not in expected value.")

    fruits = recommended_fruits(gender)
    vegetables = recommended_vegetables(age, gender)

    data = {
        'Fruits (cups)' : [f'{fruits[0]}-{fruits[1]}'],
        'Vegetables (cups)' : [f'{vegetables[0]}-{vegetables[1]}'],
        'Dairy (cups)' : ["2-3"],
    }
    df = pd.DataFrame(data)
    return df

#print(macro_nutrients_data(24,0, 2400))
#print(micro_nutrients(24, 0))
