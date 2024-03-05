# This script uses user input details such as:
# - Obesity risk score 
# - Diet preference (vegan, vegetarian, non-vegetarian)
# - If the user is obesed. 
# a variety of food groups will be appended to a dataframe 
# food groups : Beef, pork, poultry, dairy, eggs, grains, legumes, fruits, vegetables, Nuts and seeds
import pandas as pd
import string

def recommended_food(data, risk_score, food_preference):
    food_data = data[["FoodGroup","Descrip","Energy_kcal","Protein_g","Fat_g","Carb_g","Sugar_g","Fiber_g"]]

    #logic to determine risk level
    if risk_score > 75:
        risk_level = "high"
    elif 35 < risk_score <= 75:
        risk_level = "medium"
    elif risk_score <= 35:
        risk_level = "low"

    # Beef
    beef = food_data[(food_data["FoodGroup"]=="Beef Products") & (food_data["Protein_g"]>0)]
    beef_high_risk = beef.sort_values("Fat_g")
    beef_high_risk = beef_high_risk.head(40)
    sample_beef_high_risk = beef_high_risk.sample(n=5, replace=False)
    #print(sample_beef_high_risk)

    beef_med_risk = beef.sort_values("Energy_kcal")
    beef_med_risk = beef_med_risk.head(40)
    sample_beef_med_risk = beef_med_risk.sample(n=5, replace= False)
    #print(sample_beef_med_risk)

    beef_low_risk = beef.sort_values("Protein_g")
    beef_low_risk = beef_low_risk.tail(40)
    sample_beef_low_risk = beef_low_risk.sample(n=5, replace = False)
    #print(sample_beef_low_risk)

    # Fish and shellfish
    fish = food_data[(food_data["FoodGroup"]=="Finfish and Shellfish Products") & (food_data["Protein_g"]>0)]
    fish_high_risk = fish.sort_values("Fat_g")
    fish_high_risk = fish_high_risk.head(40)
    sample_fish_high_risk = fish_high_risk.sample(n=5, replace=False)
    #print(sample_fish_high_risk)

    fish_med_risk = fish.sort_values("Energy_kcal")
    fish_med_risk = fish_med_risk.head(40)
    sample_fish_med_risk = fish_med_risk.sample(n=5, replace= False)
    #print(sample_fish_med_risk)

    fish_low_risk = fish.sort_values("Protein_g")
    fish_low_risk = fish_low_risk.tail(40)
    sample_fish_low_risk = fish_low_risk.sample(n=5, replace = False)
    #print(sample_fish_low_risk)

    # poultry
    poultry = food_data[(food_data["FoodGroup"]=="Poultry Products") & (food_data["Protein_g"]>0)]
    poultry_high_risk = poultry.sort_values("Fat_g")
    poultry_high_risk = poultry_high_risk.head(40)
    sample_poultry_high_risk = poultry_high_risk.sample(n=5, replace=False)
    #print(sample_poultry_high_risk)

    poultry_med_risk = poultry.sort_values("Energy_kcal")
    poultry_med_risk = poultry_med_risk.head(40)
    sample_poultry_med_risk = poultry_med_risk.sample(n=5, replace= False)
    #print(sample_poultry_med_risk)

    poultry_low_risk = poultry.sort_values("Protein_g")
    poultry_low_risk = poultry_low_risk.tail(40)
    sample_poultry_low_risk = poultry_low_risk.sample(n=5, replace = False)
    #print(sample_poultry_low_risk)

    # Pork
    pork = food_data[(food_data["FoodGroup"]=="Pork Products") & (food_data["Protein_g"]>0)]
    pork_high_risk = pork.sort_values("Fat_g")
    pork_high_risk = pork_high_risk.head(40)
    sample_pork_high_risk = pork_high_risk.sample(n=5, replace=False)
    #print(sample_pork_high_risk)

    pork_med_risk = pork.sort_values("Energy_kcal")
    pork_med_risk = pork_med_risk.head(40)
    sample_pork_med_risk = pork_med_risk.sample(n=5, replace= False)
    #print(sample_pork_med_risk)

    pork_low_risk = pork.sort_values("Protein_g")
    pork_low_risk = pork_low_risk.tail(40)
    sample_pork_low_risk = pork_low_risk.sample(n=5, replace = False)
    #print(sample_pork_low_risk)

    # legumes
    legumes = food_data[(food_data["FoodGroup"]=="Legumes and Legume Products") & (food_data["Protein_g"]>0)]
    legumes = legumes[legumes["Descrip"].str.contains("milk|sauce")== False]
    legumes_high_risk = legumes.sort_values("Energy_kcal")
    legumes_high_risk = legumes_high_risk.head(40)
    legumes_high_risk = legumes_high_risk.sort_values("Protein_g")
    legumes_high_risk = legumes_high_risk.tail(20)
    sample_legumes_high_risk = legumes_high_risk.sample(n=5, replace=False)
    #print(sample_legumes_high_risk)

    legumes_med_risk = legumes.sort_values("Fat_g")
    legumes_med_risk = legumes_med_risk.head(40)
    legumes_med_risk = legumes_med_risk.sort_values("Protein_g")
    legumes_med_risk = legumes_med_risk.tail(20)
    sample_legumes_med_risk = legumes_med_risk.sample(n=5, replace= False)
    #print(sample_legumes_med_risk)

    legumes_low_risk = legumes.sort_values("Protein_g")
    legumes_low_risk = legumes_low_risk.tail(40)
    sample_legumes_low_risk = legumes_low_risk.sample(n=5, replace = False)
    #print(sample_legumes_low_risk)

    # cereal, grains and pasta
    # to -do do calc based on avergae, kcal, protein, carb and fiber content.
    # give grains with protein for vegan No egg.
    grains = food_data[(food_data["FoodGroup"]=="Cereal Grains and Pasta")]
    grains_vegan = grains
    grains_high_risk = grains.sort_values("Fiber_g")
    grains_high_risk = grains_high_risk.tail(40)
    sample_grains_high_risk = grains_high_risk.sample(n=5, replace=False)
    #print(sample_grains_high_risk)

    grains_med_risk = grains.sort_values("Energy_kcal")
    grains_med_risk = grains_med_risk.head(40)
    sample_grains_med_risk = grains_med_risk.sample(n=5, replace= False)
    #print(sample_grains_med_risk)

    grains_low_risk = grains.sort_values("Protein_g")
    grains_low_risk = grains_low_risk.tail(40)
    sample_grains_low_risk = grains_low_risk.sample(n=5, replace = False)
    #print(sample_grains_low_risk)

    # grains for vegan 
    grains_vegan = grains_vegan[grains_vegan["Descrip"].str.contains("egg")== False]
    grains_vegan = grains_vegan.sort_values("Protein_g")
    grains_vegan = grains_vegan.tail(60)
    sample_vegan_grains = grains_vegan.sample(n=5, replace =False)
    #print(sample_vegan_grains)

    # Fruits
    # filter juices as they are low in fibre and higher in kcal/ added sugar., removing alcoholic beverages
    fruits = food_data[(food_data["FoodGroup"]=="Fruits and Fruit Juices") & (food_data["Sugar_g"] <= 20)]
    #df = df[df[“column_name”].str.contains(“string1|string2”)==False]
    fruits = fruits[fruits["Descrip"].str.contains("Alcoholic|juice|USDA")== False]
    fruits = fruits.sort_values("Fiber_g")
    fruits = fruits.tail(100)
    fruits = fruits.sample(n=5, replace = False)
    #print(fruits)

    #veggies
    # Since vegans vegetarians need more protein from plants, below logic tries to fetch high protein veggies
    veggies = food_data[(food_data["FoodGroup"]=="Vegetables and Vegetable Products")]
    veggies = veggies[veggies["Descrip"].str.contains("juice")==False]
    veggies_non_vegetarian = veggies
    veggies = veggies.sort_values("Protein_g")
    veggies = veggies.tail(100)
    veggies = veggies.sample(n=5, replace = False)
    #print(veggies)

    # veggies for non vegetarians
    veggies_non_vegetarian = veggies_non_vegetarian.sort_values("Fiber_g")
    veggies_non_vegetarian = veggies_non_vegetarian.tail(100)
    veggies_non_vegetarian = veggies_non_vegetarian.sample(n=5, replace = False)
    #print(veggies_non_vegetarian)

    # dairy 
    dairy = food_data[(food_data["FoodGroup"]=="Dairy and Egg Products")]
    dairy = dairy[dairy["Descrip"].str.contains("egg|Egg")== False]
    dairy_low_risk = dairy

    dairy_high_med_risk = dairy.sort_values("Fat_g")
    dairy_high_med_risk = dairy_high_med_risk.head(70)
    dairy_high_med_risk = dairy_high_med_risk.sample(n=5, replace = False)
    #print(dairy_high_med_risk)

    #include this for vegan and vegetarian. 
    dairy_low_risk = dairy_low_risk.sort_values("Protein_g")
    dairy_low_risk = dairy_low_risk.tail(50)
    dairy_low_risk = dairy_low_risk.sample(n=5, replace = False)
    #print(dairy_low_risk)

    food_groups = {
        'vegan': {
            "high": [sample_legumes_high_risk, sample_vegan_grains, fruits, veggies],
            "medium": [sample_legumes_med_risk, sample_vegan_grains, fruits, veggies],
            "low": [sample_legumes_low_risk, sample_vegan_grains, fruits, veggies],
        },
        'vegetarian': {
            "high": [sample_legumes_high_risk, sample_vegan_grains, fruits, veggies, dairy_high_med_risk],
            "medium": [legumes_med_risk, sample_vegan_grains, fruits, veggies, dairy_high_med_risk],
            "low": [legumes_low_risk, sample_vegan_grains, fruits, veggies, dairy_low_risk],
        },
        'non vegetarian': {
            "high": [sample_beef_high_risk, sample_pork_high_risk, sample_fish_high_risk, sample_poultry_high_risk, sample_grains_high_risk, fruits, veggies_non_vegetarian, dairy_high_med_risk],
            "medium": [sample_beef_med_risk, sample_pork_med_risk, sample_fish_med_risk, sample_poultry_med_risk, sample_grains_med_risk, fruits, veggies_non_vegetarian, dairy_high_med_risk],
            "low": [sample_beef_low_risk, sample_pork_low_risk, sample_fish_low_risk, sample_poultry_low_risk, grains_low_risk, fruits, veggies_non_vegetarian, dairy_low_risk],
        }

    }

    food_groups_df = pd.concat(food_groups[food_preference][risk_level] , ignore_index = True)

    new_group_values = {
    'Beef Products': 'Beef',
    'Pork Products': 'Pork',
    "Finfish and Shellfish Products": 'Seafood',
    "Poultry Products": 'Poultry',
    'Fruits and Fruit Juices': 'Fruits',
    'Vegetables and Vegetable Products': 'Vegetables',
    "Dairy and Egg Products": 'Dairy'
    }
    food_groups_df['FoodGroup'] = food_groups_df['FoodGroup'].map(new_group_values).fillna(food_groups_df['FoodGroup'])
    food_groups_df.rename(columns={"FoodGroup": "Food Category",
                                "Descrip": "Description",
                                "Energy_kcal": "Calories (kcal)",
                                "Protein_g": "Protein (gm)",
                                "Fat_g": "Fat (gm)",
                                "Carb_g": "Carbohydrates (gm)",
                                "Sugar_g": "Sugar (gm)",
                                "Fiber_g": "Fiber (gm)"}, inplace=True)
    #food_groups_df.to_csv("out.csv")
    #print(food_groups_df)
    return food_groups_df

def search_food(data, food_item):
    if food_item == "":
        return None
    else:
        food_item = food_item.translate(str.maketrans('', '', string.punctuation))
        food_item = food_item.lower()
        
    food_data = data[["FoodGroup","Descrip","Energy_kcal","Protein_g","Fat_g","Carb_g","Sugar_g","Fiber_g"]]
    out = food_data[(food_data["Descrip"].str.contains(food_item))]
    out = out[["Descrip","Energy_kcal","Protein_g","Carb_g","Sugar_g","Fiber_g"]]
    out.rename(columns={"Descrip": "Description",
                        "Energy_kcal": "Calories (kcal)",
                        "Protein_g": "Protein (gm)",
                        "Carb_g": "Carbohydrates (gm)",
                        "Sugar_g": "Sugar (gm)",
                        "Fiber_g": "Fiber (gm)"}, inplace=True)

    return(out)

#print(search_food("milk",filter_data))
#print(recommended_food(risk_score = 55, food_preference = 3))