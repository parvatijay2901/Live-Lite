""" This script uses user input details such as:
Obesity risk score
Diet preference (vegan, vegetarian, non-vegetarian)
a variety of food groups will be appended to a dataframe.
food groups : Beef, pork, poultry, dairy, eggs, grains, legumes, fruits, vegetables, Nuts and seeds
"""
import string
import pandas as pd
# pylint: disable=R0914
def validate_input_dataframe(df):
    """Validate input DataFrame.
    Parameters:
        df (pd.DataFrame): Input DataFrame to be validated. 
    Raises:
        TypeError: If the input is not a DataFrame.
        ValueError: If the DataFrame fails validation checks.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input is not a DataFrame.")
    # Check if DataFrame has required columns
    required_columns = ["FoodGroup","Descrip","Energy_kcal","Protein_g","Fat_g","Carb_g",
                      "Sugar_g","Fiber_g"]
    if not all(col in df.columns for col in required_columns):
        raise ValueError("DataFrame is missing the required columns.")
    # Check if value columns have float or integer values
    if not all(df[col].dtype in [float, int] for col in ["Energy_kcal","Protein_g","Fat_g","Carb_g",
                      "Sugar_g","Fiber_g"]):
        raise ValueError("value Columns should have float or integer values.")

def beef_data(food_data, risk_level):
    """This function selects sample beef data from the food dataset based on the risk level
    """
    if food_data.empty:
        raise ValueError("food_data is empty")
    if risk_level not in ["high", "med", "low"]:
        raise ValueError("risk level must be one of 'high', 'med', or 'low'")

    beef = food_data[(food_data["FoodGroup"]=="Beef Products") & (food_data["Protein_g"]>0)]

    if risk_level == "high":
        beef_high_risk = beef.sort_values("Fat_g")
        beef_high_risk = beef_high_risk.head(40)
        sample_beef_high_risk = beef_high_risk.sample(n=5, replace=False)
        return sample_beef_high_risk

    if risk_level == "med":
        beef_med_risk = beef.sort_values("Energy_kcal")
        beef_med_risk = beef_med_risk.head(40)
        sample_beef_med_risk = beef_med_risk.sample(n=5, replace= False)
        return sample_beef_med_risk

    beef_low_risk = beef.sort_values("Protein_g")
    beef_low_risk = beef_low_risk.tail(40)
    sample_beef_low_risk = beef_low_risk.sample(n=5, replace = False)
    return sample_beef_low_risk

def fish_data(food_data, risk_level):
    """This function selects sample fish data from the food dataset based on the risk level
    """
    if food_data.empty:
        raise ValueError("food_data is empty")
    if risk_level not in ["high", "med", "low"]:
        raise ValueError("risk level must be one of 'high', 'med', or 'low'")

    fish = food_data[(food_data["FoodGroup"]=="Finfish and Shellfish Products")
                     & (food_data["Protein_g"]>0)]
    if risk_level == "high":
        fish_high_risk = fish.sort_values("Fat_g")
        fish_high_risk = fish_high_risk.head(40)
        sample_fish_high_risk = fish_high_risk.sample(n=5, replace=False)
        return sample_fish_high_risk

    if risk_level == "med":
        fish_med_risk = fish.sort_values("Energy_kcal")
        fish_med_risk = fish_med_risk.head(40)
        sample_fish_med_risk = fish_med_risk.sample(n=5, replace= False)
        return sample_fish_med_risk

    fish_low_risk = fish.sort_values("Protein_g")
    fish_low_risk = fish_low_risk.tail(40)
    sample_fish_low_risk = fish_low_risk.sample(n=5, replace = False)
    return sample_fish_low_risk

def poultry_data(food_data, risk_level):
    """This function selects sample poultry data from the food dataset based on the risk level
    """
    if food_data.empty:
        raise ValueError("food_data is empty")
    if risk_level not in ["high", "med", "low"]:
        raise ValueError("risk level must be one of 'high', 'med', or 'low'")

    poultry = food_data[(food_data["FoodGroup"]=="Poultry Products")
                        & (food_data["Protein_g"]>0)]
    if risk_level == "high":
        poultry_high_risk = poultry.sort_values("Fat_g")
        poultry_high_risk = poultry_high_risk.head(40)
        sample_poultry_high_risk = poultry_high_risk.sample(n=5, replace=False)
        return sample_poultry_high_risk

    if risk_level == "med":
        poultry_med_risk = poultry.sort_values("Energy_kcal")
        poultry_med_risk = poultry_med_risk.head(40)
        sample_poultry_med_risk = poultry_med_risk.sample(n=5, replace= False)
        return sample_poultry_med_risk

    poultry_low_risk = poultry.sort_values("Protein_g")
    poultry_low_risk = poultry_low_risk.tail(40)
    sample_poultry_low_risk = poultry_low_risk.sample(n=5, replace = False)
    return sample_poultry_low_risk

def pork_data(food_data, risk_level):
    """This function selects sample pork data from the food dataset based on the risk level
    """
    if food_data.empty:
        raise ValueError("food_data is empty")
    if risk_level not in ["high", "med", "low"]:
        raise ValueError("risk level must be one of 'high', 'med', or 'low'")

    pork = food_data[(food_data["FoodGroup"]=="Pork Products")
                     & (food_data["Protein_g"]>0)]
    if risk_level == "high":
        pork_high_risk = pork.sort_values("Fat_g")
        pork_high_risk = pork_high_risk.head(40)
        sample_pork_high_risk = pork_high_risk.sample(n=5, replace=False)
        return sample_pork_high_risk

    if risk_level == "med":
        pork_med_risk = pork.sort_values("Energy_kcal")
        pork_med_risk = pork_med_risk.head(40)
        sample_pork_med_risk = pork_med_risk.sample(n=5, replace= False)
        return sample_pork_med_risk

    pork_low_risk = pork.sort_values("Protein_g")
    pork_low_risk = pork_low_risk.tail(40)
    sample_pork_low_risk = pork_low_risk.sample(n=5, replace = False)
    return sample_pork_low_risk

def legumes_data(food_data, risk_level):
    """This function selects sample legumes data from the food dataset based on the risk level
    """
    if food_data.empty:
        raise ValueError("food_data is empty")
    if risk_level not in ["high", "med", "low"]:
        raise ValueError("risk level must be one of 'high', 'med', or 'low'")

    legumes = food_data[(food_data["FoodGroup"]=="Legumes and Legume Products")
                        & (food_data["Protein_g"]>0)]
    legumes = legumes[~legumes["Descrip"].str.contains("milk|sauce")]

    if risk_level == "high":
        legumes_high_risk = legumes.sort_values("Energy_kcal")
        legumes_high_risk = legumes_high_risk.head(40)
        legumes_high_risk = legumes_high_risk.sort_values("Protein_g")
        legumes_high_risk = legumes_high_risk.tail(20)
        sample_legumes_high_risk = legumes_high_risk.sample(n=5, replace=False)
        return sample_legumes_high_risk

    if risk_level == "med":
        legumes_med_risk = legumes.sort_values("Fat_g")
        legumes_med_risk = legumes_med_risk.head(40)
        legumes_med_risk = legumes_med_risk.sort_values("Protein_g")
        legumes_med_risk = legumes_med_risk.tail(20)
        sample_legumes_med_risk = legumes_med_risk.sample(n=5, replace= False)
        return sample_legumes_med_risk

    legumes_low_risk = legumes.sort_values("Protein_g")
    legumes_low_risk = legumes_low_risk.tail(40)
    sample_legumes_low_risk = legumes_low_risk.sample(n=5, replace = False)
    return sample_legumes_low_risk

def grains_data(food_data, risk_level):
    """This function selects sample grains data from the food dataset based on the risk level
    """
    if food_data.empty:
        raise ValueError("food_data is empty")
    if risk_level not in ["high", "med", "low"]:
        raise ValueError("risk level must be one of 'high', 'med', or 'low'")

    grains = food_data[(food_data["FoodGroup"]=="Cereal Grains and Pasta")]

    if risk_level == "high":
        grains_high_risk = grains.sort_values("Fiber_g")
        grains_high_risk = grains_high_risk.tail(40)
        sample_grains_high_risk = grains_high_risk.sample(n=5, replace=False)
        return sample_grains_high_risk

    if risk_level == "med":
        grains_med_risk = grains.sort_values("Energy_kcal")
        grains_med_risk = grains_med_risk.head(40)
        sample_grains_med_risk = grains_med_risk.sample(n=5, replace= False)
        return sample_grains_med_risk

    grains_low_risk = grains.sort_values("Protein_g")
    grains_low_risk = grains_low_risk.tail(40)
    sample_grains_low_risk = grains_low_risk.sample(n=5, replace = False)
    return sample_grains_low_risk

def vegan_grains_data(food_data):
    """This function selects sample grains data from the food dataset for vegans and vegetarians
    """
    if food_data.empty:
        raise ValueError("food_data is empty")

    grains_vegan = food_data[(food_data["FoodGroup"]=="Cereal Grains and Pasta")]
    grains_vegan = grains_vegan[~grains_vegan["Descrip"].str.contains("egg")]
    grains_vegan = grains_vegan.sort_values("Protein_g")
    grains_vegan = grains_vegan.tail(50)
    sample_vegan_grains = grains_vegan.sample(n=5, replace =False)
    return sample_vegan_grains

def fruits_data(food_data):
    """This function selects sample fruits data from the food dataset
    """
    if food_data.empty:
        raise ValueError("food_data is empty")
    fruits = food_data[(food_data["FoodGroup"]=="Fruits and Fruit Juices")
                       & (food_data["Sugar_g"] <= 20)]
    fruits = fruits[~fruits["Descrip"].str.contains("Alcoholic|juice|Juice|USDA")]
    fruits = fruits.sort_values("Fiber_g")
    fruits = fruits.tail(50)
    fruits_sample = fruits.sample(n=5, replace = False)
    return fruits_sample

def vegetable_data(food_data, food_preference):
    """This function selects sample vegtables data from the food dataset.
    vegans & vegetarians need more protein from plants, logic tries to fetch high protein veggies
    """
    if food_data.empty:
        raise ValueError("food_data is empty")
    if food_preference not in ["vegan", "vegetarian", "non vegetarian"]:
        raise ValueError("Invalid food preference")

    veggies = food_data[(food_data["FoodGroup"]=="Vegetables and Vegetable Products")]
    veggies = veggies[~veggies["Descrip"].str.contains("juice")]
    veggies_non_vegetarian = veggies

    if food_preference in ('vegan', 'vegetarian'):
        veggies = veggies.sort_values("Protein_g")
        veggies = veggies.tail(50)
        veggies = veggies.sample(n=5, replace = False)
        return veggies

    veggies_non_vegetarian = veggies_non_vegetarian.sort_values("Fiber_g")
    veggies_non_vegetarian = veggies_non_vegetarian.tail(50)
    veggies_non_vegetarian = veggies_non_vegetarian.sample(n=5, replace = False)
    return veggies_non_vegetarian

def dairy_data(food_data, risk_level):
    """This function selects sample dairy data from the food dataset
    """
    if food_data.empty:
        raise ValueError("food_data is empty")
    if risk_level not in ["high", "med", "low"]:
        raise ValueError("risk level must be one of 'high', 'med', or 'low'")

    dairy = food_data[(food_data["FoodGroup"]=="Dairy and Egg Products")]
    dairy = dairy[~dairy["Descrip"].str.contains("egg|Egg")]

    if risk_level in ('high', 'med'):
        dairy_high_med_risk = dairy.sort_values("Fat_g")
        dairy_high_med_risk = dairy_high_med_risk.head(50)
        sample_dairy_high_med_risk = dairy_high_med_risk.sample(n=5, replace = False)
        return sample_dairy_high_med_risk

    dairy_low_risk = dairy.sort_values("Protein_g")
    dairy_low_risk = dairy_low_risk.tail(50)
    sample_dairy_low_risk = dairy_low_risk.sample(n=5, replace = False)
    return sample_dairy_low_risk


def recommended_food(data, risk_score, food_preference):
    """This function creates a dataframe for each of the food groups
    to be included in a person's diet based on the risk score and 
    food preference.

    Args:
        data (dataframe): Food data
        risk_score (int): risk score of obesity of the user
        food_preference (string): vegan, vegetraian or non vegetarian

    Returns:
        Dataframe: concatenated dataframe containing nutritional 
        and calorific information of each of the food groups.
    """
    if data.empty:
        raise ValueError("data is empty")
    if not isinstance(food_preference, str):
        raise TypeError("food preference should be a string")
    if food_preference not in ["vegan", "vegetarian", "non vegetarian"]:
        raise ValueError("Invalid food preference ***")
    try:
        # Validate the input DataFrame
        validate_input_dataframe(data)
    except (TypeError, ValueError) as e:
        print("Input DataFrame is not valid:", e)
    if not isinstance(risk_score, (float,int)):
        raise TypeError("risk score should be a float value")
    if not 0 <= risk_score <= 100:
        raise ValueError("risk score is not in expected range.")

    food_data = data[["FoodGroup","Descrip","Energy_kcal","Protein_g","Fat_g","Carb_g",
                      "Sugar_g","Fiber_g"]]

    #logic to determine risk level
    if risk_score > 75:
        risk_level = "high"
    elif 35 < risk_score <= 75:
        risk_level = "med"
    elif risk_score <= 35:
        risk_level = "low"

    if food_preference == "vegan":
        d1 = legumes_data(food_data, risk_level)
        d2 = vegan_grains_data(food_data)
        d3 = fruits_data(food_data)
        d4 = vegetable_data(food_data,"vegan")
        food_dataframe = pd.concat((d1,d2,d3,d4) , ignore_index = True)

    if food_preference == "vegetarian":
        d1 = legumes_data(food_data, risk_level)
        d2 = vegan_grains_data(food_data)
        d3 = fruits_data(food_data)
        d4 = vegetable_data(food_data,"vegetarian")
        d5 = dairy_data(food_data, risk_level)
        food_dataframe = pd.concat((d1,d2,d3,d4,d5) , ignore_index = True)

    if food_preference == "non vegetarian":
        d1 = beef_data(food_data, risk_level)
        d2 = pork_data(food_data, risk_level)
        d3 = fish_data(food_data, risk_level)
        d4 = poultry_data(food_data, risk_level)
        d5 = grains_data(food_data, risk_level)
        d6 = fruits_data(food_data)
        d7 = vegetable_data(food_data,"non vegetarian")
        d8 = dairy_data(food_data, risk_level)
        food_dataframe = pd.concat((d1,d2,d3,d4,d5,d6,d7,d8) , ignore_index = True)

    new_group_values = {
    'Beef Products': 'Beef',
    'Pork Products': 'Pork',
    "Finfish and Shellfish Products": 'Seafood',
    "Poultry Products": 'Poultry',
    'Fruits and Fruit Juices': 'Fruits',
    'Vegetables and Vegetable Products': 'Vegetables',
    "Dairy and Egg Products": 'Dairy'
    }
    food_dataframe['FoodGroup'] = food_dataframe['FoodGroup'].map(
        new_group_values).fillna(food_dataframe['FoodGroup'])
    food_dataframe.rename(columns={"FoodGroup": "Food Category",
                                "Descrip": "Description (per 100gms)",
                                "Energy_kcal": "Calories (kcal)",
                                "Protein_g": "Protein (gm)",
                                "Fat_g": "Fat (gm)",
                                "Carb_g": "Carbohydrates (gm)",
                                "Sugar_g": "Sugar (gm)",
                                "Fiber_g": "Fiber (gm)"}, inplace=True)
    return food_dataframe

def search_food(data, food_item):
    """This function searches the input food from the dataset to provide 
    nutritional and calorific information. The output is a filtered dataframe
    containing the search food.
    """
    try:
        # Validate the input DataFrame
        validate_input_dataframe(data)
    except (TypeError, ValueError) as e:
        print("Input DataFrame is not valid:", e)
    if not isinstance(food_item, str):
        raise TypeError("food item should be a string.")
    if food_item == "":
        return None

    food_item = food_item.translate(str.maketrans('', '', string.punctuation))
    food_data = data[["FoodGroup","Descrip","Energy_kcal","Protein_g",
                      "Fat_g","Carb_g","Sugar_g","Fiber_g"]]
    out = food_data[(food_data["Descrip"].str.contains(food_item, case =False))]
    out = out[["Descrip","Energy_kcal","Protein_g","Carb_g","Sugar_g","Fiber_g"]]
    out.rename(columns={"Descrip": "Description (per 100gms)",
                        "Energy_kcal": "Calories (kcal)",
                        "Protein_g": "Protein (gm)",
                        "Carb_g": "Carbohydrates (gm)",
                        "Sugar_g": "Sugar (gm)",
                        "Fiber_g": "Fiber (gm)"}, inplace=True)

    return out

#data = pd.read_csv("../../data/input_files/food_nutrition_data.csv")
#print(search_food(data,"milk"))
#print(recommended_food(data, risk_score = 80, food_preference = "non vegetarian"))
