# this module is created to define various methods related to diet and nutrition
# below are functions to print recommended quantity of food groups to consume per day 
# the functions will return none when input is not valid 
import pandas as pd
import numpy as np
#pro_data = pd.read_csv("../NutritionData/protein_rec.csv")
#pro_data["gender"] = pro_data["gender"].astype(str)




def recommendedProtein(age_in,gender_in):
    if (age_in<9) & (age_in>100):
        return None
    if (gender_in != "m") & (gender_in != "f"):
        return None
    min = 0
    max = 0
    pro_data = pd.read_csv("../NutritionData/protein_rec.csv")
    filtered_data = pro_data[
        (pro_data["gender"] == gender_in) &
        (pro_data["min_age"]<= age_in) & (age_in <= pro_data["max_age"])
    ]
    #print(filtered_data)
    min = round(filtered_data.iloc[0]['min_ounce']*28.3495)
    max = round(filtered_data.iloc[0]['max_ounce']*28.3495)
    
    #print(min)
    #print(max)

    return(min, max, "grams")

def recommendedGrains(age_in,gender_in):
    if (age_in<9) & (age_in>100):
        return None
    if (gender_in != "m") & (gender_in != "f"):
        return None
    min_g = 0
    min_wg =0 
    max_g = 0
    max_wg = 0
    grain_data = pd.read_csv("../NutritionData/grains_rec.csv")
    filtered_data = grain_data[
        (grain_data["gender"] == gender_in) &
        (grain_data["min_age"]<= age_in) & (age_in <= grain_data["max_age"])
    ]
    #print(filtered_data)
    min_g = round(filtered_data.iloc[0]['min_grains']*28.3495)
    max_g = round(filtered_data.iloc[0]['max_grains']*28.3495)
    min_wg = round(filtered_data.iloc[0]['min_whole-grains']*28.3495)
    max_wg = round(filtered_data.iloc[0]['max_whole-grains']*28.3495)
    
    #print(min)
    #print(max)

    return(min_g, max_g, min_wg, max_wg, "grams") 

def recommendedDairy():
    return(2,3,"cups")  

def recommendedFruits(gender_in):
    if gender_in == "f":
        return(1.5,2,"cups")
    if gender_in =="m":
        return(2,2.5,"cups")
    else:
        return None

def recommendedVegetables(age_in,gender_in):
    if (age_in<9) & (age_in>100):
        return None
    if (gender_in != "m") & (gender_in != "f"):
        return None
    min = 0
    max = 0
    veg_data = pd.read_csv("../NutritionData/vegetable_rec.csv")
    filtered_data = veg_data[
        (veg_data["gender"] == gender_in) &
        (veg_data["min_age"]<= age_in) & (age_in <= veg_data["max_age"])
    ]
    #print(filtered_data)
    min = filtered_data.iloc[0]['min_cups']
    max = filtered_data.iloc[0]['max_cups']
    
    #print(min)
    #print(max)

    return(min, max, "cups")   
    
'''
#sample tests
print(recommendedProtein(23,"m"))
print(recommendedProtein(1,"d"))
print(recommendedProtein(100,"m"))
print(recommendedProtein(23,"h"))

print("***")
print(recommendedGrains(23,"m"))
print(recommendedGrains(1,"d"))
print(recommendedGrains(100,"m"))
print(recommendedGrains(23,"h"))
print(recommendedDairy())
print(recommendedFruits("f"))
print(recommendedFruits("m"))
print(recommendedFruits("j"))
print("#####")
print(recommendedVegetables(23,"m"))
print(recommendedVegetables(23,"f"))
print(recommendedVegetables(2,"h"))
'''


