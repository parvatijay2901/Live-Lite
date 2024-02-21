import pandas as pd
import numpy as np

food = pd.read_csv("../NutritionData/nutrition_data1.csv")
#print(food.head())
filter_data = food[["FoodGroup","ShortDescrip","Descrip","Energy_kcal","Protein_g","Fat_g","Carb_g","Sugar_g","Fiber_g"]]
filter_data.head()

def dairy_protein_food(data):
    #data = filter_data
    out = data[(data["FoodGroup"]=="Dairy and Egg Products") & (data["Descrip"].str.contains('Cheese' or 'Milk' or'Yogurt' or 'Whey')) & (data["Protein_g"]>0)]
    out = out[["Descrip","Energy_kcal","Protein_g","Carb_g","Sugar_g","Fiber_g"]]

    return(out)

#print(dairy_protein_food(filter_data).head())

def egg_protein_food(data):
    out = data[(data["FoodGroup"]=="Dairy and Egg Products") & (data["Descrip"].str.contains('Egg')) & (data["Protein_g"]>0)]
    out = out[["Descrip","Energy_kcal","Protein_g","Carb_g","Sugar_g","Fiber_g"]]

    return(out)

#print(egg_protein_food(filter_data).head())

def seafood_protein(data):
    out = data[(data["FoodGroup"]=="Finfish and Shellfish Products") & (data["Protein_g"]>0)]
    out = out[["Descrip","Energy_kcal","Protein_g","Carb_g","Sugar_g","Fiber_g"]]

    return(out)

#print(seafood_protein(filter_data).head())

def poultry_meat_protein(data):
    out = data[(data["FoodGroup"]=="Poultry Products") & (data["Protein_g"]>0)]
    out = out[["Descrip","Energy_kcal","Protein_g","Carb_g","Sugar_g","Fiber_g"]]

    return(out)

#print(poultry_meat_protein(filter_data).head())

def sausage_luncheon_meat(data):
    out = data[(data["FoodGroup"]=="Sausages and Luncheon Meats") & (data["Protein_g"]>0)]
    out = out[["Descrip","Energy_kcal","Protein_g","Carb_g","Sugar_g","Fiber_g"]]

    return(out)

#print(sausage_luncheon_meat(filter_data).head())

def vegan_protein(data):
    out = data[(data["FoodGroup"]=="Legumes and Legume Products") & (data["Protein_g"]>0)]
    out = out[["Descrip","Energy_kcal","Protein_g","Carb_g","Sugar_g","Fiber_g"]]

    return(out)

#print(vegan_protein(filter_data).head())

def carbs(data):
    out = data[(data["FoodGroup"]=="Cereal Grains and Pasta")]
    out = out[["Descrip","Energy_kcal","Protein_g","Carb_g","Sugar_g","Fiber_g"]]

    return(out)

#print(carbs(filter_data).head())

def fruits(data):
    out = data[(data["FoodGroup"]=="Fruits and Fruit Juices")]
    out = out[["Descrip","Energy_kcal","Protein_g","Carb_g","Sugar_g","Fiber_g"]]

    return(out)

#print(fruits(filter_data).head())

def vegetables(data):
    out = data[(data["FoodGroup"]=="Vegetables and Vegetable Products")]
    out = out[["Descrip","Energy_kcal","Protein_g","Carb_g","Sugar_g","Fiber_g"]]

    return(out)

#print(vegetables(filter_data).head())

def search_food(food_item, data):
    if food_item == "":
        return None
    out = data[(data["Descrip"].str.contains(food_item))]
    out = out[["Descrip","Energy_kcal","Protein_g","Carb_g","Sugar_g","Fiber_g"]]

    return(out)

#print(search_food("milk",filter_data))

