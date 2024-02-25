# this module is created to define various methods related to diet and nutrition
# below are functions to print recommended quantity of food groups to consume per day 
# the functions will return none when input is not valid 
import pandas as pd
import numpy as np

def recommendedProtein(age_in,gender_in):
    if (age_in<9) & (age_in>100):
        return None
    if (gender_in != 0) & (gender_in != 1):
        return None
    min = 0
    max = 0

    if gender_in ==0:
        if 9 <= age_in <= 13:
            min =4
            max =6
        if 14 <= age_in <= 30:
            min =5
            max =6.5
        if age_in >= 31:
            min =5
            max =6

    if gender_in ==1:
        if 9 <= age_in <= 13:
            min = 5
            max = 6.5
        if 13 < age_in <= 18:
            min = 5.5
            max = 7
        if 18< age_in <= 30:
            min = 6.5
            max = 7
        if 30 < age_in <=59:
            min = 6
            max= 7
        if age_in > 59:
            min = 5.5
            max = 6.5

    return(round(min*28.34), round(max*28.34), "grams")

#print(recommendedProtein(23,1))

def recommendedGrains(age_in,gender_in):
    if (age_in<9) & (age_in>100):
        return None
    if (gender_in != 1) & (gender_in != 0):
        return None
    min_g = 0
    min_wg =0 
    max_g = 0
    max_wg = 0

    if gender_in ==0:
        if 9 < age_in <= 13:
            min_g = 5
            min_wg =2.5
            max_g = 7
            max_wg = 3.5

        if 13 < age_in <= 30:
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
        if 9 < age_in <= 13:
            min_g = 5
            min_wg =3
            max_g = 9
            max_wg = 4.5

        if 13 < age_in <= 18:
            min_g = 6
            min_wg =3
            max_g = 10
            max_wg = 5

        if 18 <= age_in <= 30:
            min_g = 8
            min_wg = 4
            max_g = 10
            max_wg = 5

        if 30 < age_in <= 60:
            min_g = 7
            min_wg = 3.5
            max_g = 10
            max_wg = 5

        if age_in > 60:
            min_g = 6
            min_wg = 3
            max_g = 9
            max_wg = 4.5
   

    return(round(min_g*28.34), round(max_g*28.34), round(min_wg*28.34), round(max_wg*28.34), "grams") 

def recommededFat(calorie):
    if calorie <= 2000 :
        fat = 50

    if 2000< calorie <= 2500 :
        fat = 67

    if calorie > 2500:
        fat = 83

    return(fat, "grams")

def recommendedDairy():
    return(2,3,"cups")  

def recommendedFruits(gender_in):
    if gender_in == 0:
        return(1.5,2,"cups")
    if gender_in ==1:
        return(2,2.5,"cups")
    else:
        return None

def recommendedVegetables(age_in,gender_in):
    if (age_in<9) & (age_in>100):
        return None
    if (gender_in != 0) & (gender_in != 1):
        return None
    min = 0
    max = 0

    if gender_in ==1:
        if 18<= age_in <= 60:
            min = 3
            max = 4

        if age_in > 60:
            min = 2.5
            max = 3.5
    if gender_in == 0:
        if 18<= age_in <= 30:
            min = 2.5
            max = 3

        if age_in > 30:
            min = 2
            max = 3

    return(min, max, "cups")

def macro_calorie(macro,calorie):
    min = 0 
    max = 0
    if macro == "protein":
        min = 0.1*calorie
        max = 0.3*calorie

    if macro == "carbohydrate":
        min = 0.45*calorie
        max = 0.65*calorie

    if macro == "fat":
        min = 0.2*calorie
        max = 0.3*calorie

    return(round(min), round(max), "calories")
  
#functions below returns a dataframe for recommended calrie and macro nutrient portion per day    
def macro_nutrients_data(age, gender, calorie):

    carb_quantity = f'{recommendedGrains(age, gender)[0]} - {recommendedGrains(age, gender)[1]}g of carbs/grains of which {recommendedGrains(age, gender)[2]} - {recommendedGrains(age, gender)[3]} of whole grains '
    protein_quantity = f'{recommendedProtein(age, gender)[0]} - {recommendedProtein(age, gender)[1]} grams'
    fat_quantity = f'{recommededFat(calorie)[0]} grams'
    carbohydrate_calorie = macro_calorie("carbohydrate", calorie)
    protein_calorie = macro_calorie("protein", calorie)
    fat_calorie = macro_calorie("fat", calorie)

    data = {
        'Macro Nutrient': ['Carbohydrate', 'Protein', 'Fat'],
        'Quantity in Grams': [carb_quantity, protein_quantity, fat_quantity],
        'Kcal': [f'{carbohydrate_calorie[0]} - {carbohydrate_calorie[1]}', f'{protein_calorie[0]} - {protein_calorie[1]}'
                 , f'{fat_calorie[0]} - {fat_calorie[1]}']
    }
    df = pd.DataFrame(data)
    return df

def micro_nutrients(age, gender):
    fruits = recommendedFruits(gender)
    vegetables = recommendedVegetables(age, gender)
    dairy = recommendedDairy()

    data = {
        'Fruits (cups)' : [f'{fruits[0]} - {fruits[1]}'],
        'Vegetables (cups)' : [f'{vegetables[0]} - {vegetables[1]}'],
        'Dairy (cups)' : [f'{dairy[0]} - {dairy[1]}'],
    }

    df = pd.DataFrame(data)
    return df


#print(macro_nutrients_data(24,0, 2400))
#print(micro_nutrients(24, 0))
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


