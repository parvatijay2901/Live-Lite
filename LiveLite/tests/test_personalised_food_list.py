"""This script contains unit tests for all the functions
used for fetching variety of food from food list
based on food groups.
"""
import unittest
import pandas as pd
#from LiveLite import personalised_food_list
from LiveLite import search_food, recommended_food, beef_data, fish_data
from LiveLite import poultry_data, pork_data, legumes_data, grains_data
from LiveLite import vegan_grains_data, vegetable_data, fruits_data, dairy_data

test_beef_data = pd.DataFrame({
    "FoodGroup": ["Beef Products"] * 100,
    "Descrip": ["Beef Products"] * 100,
    "Protein_g": range(100),
    "Fat_g": range(100),
    "Energy_kcal": range(100),
    "Fiber_g": range(100),
    "Sugar_g": range(100)
})

test_fish_data = pd.DataFrame({
    "FoodGroup": ["Finfish and Shellfish Products"] * 100,
    "Descrip": ["fish Products"] * 100,
    "Protein_g": range(100),
    "Fat_g": range(100),
    "Energy_kcal": range(100),
    "Fiber_g": range(100),
    "Sugar_g": range(100)
})

test_poultry_data = pd.DataFrame({
    "FoodGroup": ["Poultry Products"] * 100,
    "Descrip": ["Poultry Products"] * 100,
    "Protein_g": range(100),
    "Fat_g": range(100),
    "Energy_kcal": range(100),
    "Fiber_g": range(100),
    "Sugar_g": range(100)
})

test_pork_data = pd.DataFrame({
    "FoodGroup": ["Pork Products"] * 100,
    "Descrip": ["Pork Products"] * 100,
    "Protein_g": range(100),
    "Fat_g": range(100),
    "Energy_kcal": range(100),
    "Fiber_g": range(100),
    "Sugar_g": range(100)
})

test_legumes_data = pd.DataFrame({
    "FoodGroup": ["Legumes and Legume Products"] * 100,
    "Descrip": ["Legumes and Legume Products"] * 100,
    "Protein_g": range(100),
    "Fat_g": range(100),
    "Energy_kcal": range(100),
    "Fiber_g": range(100),
    "Sugar_g": range(100)
})

test_grains_data = pd.DataFrame({
    "FoodGroup": ["Cereal Grains and Pasta"] * 100,
    "Descrip": ["Cereal Grains and Pasta"] * 100,
    "Protein_g": range(100),
    "Fat_g": range(100),
    "Energy_kcal": range(100),
    "Fiber_g": range(100),
    "Sugar_g": range(100)
})

test_fruits_data = pd.DataFrame({
    "FoodGroup": ["Fruits and Fruit Juices"] * 100,
    "Descrip": ["Fruits"] * 100,
    "Protein_g": range(100),
    "Fat_g": range(100),
    "Energy_kcal": range(100),
    "Fiber_g": range(100),
    "Sugar_g": range(100)
})

test_vegetables_data = pd.DataFrame({
    "FoodGroup": ["Vegetables and Vegetable Products"] * 100,
    "Descrip": ["Vegetables and Vegetable Products"] * 100,
    "Protein_g": range(100),
    "Fat_g": range(100),
    "Energy_kcal": range(100),
    "Fiber_g": range(100),
    "Sugar_g": range(100)
})

test_dairy_data = pd.DataFrame({
    "FoodGroup": ["Dairy and Egg Products"] * 100,
    "Descrip": ["Dairy"] * 100,
    "Protein_g": range(100),
    "Fat_g": range(100),
    "Energy_kcal": range(100),
    "Fiber_g": range(100),
    "Sugar_g": range(100)
})

class TestBeefData(unittest.TestCase):
    """This class contains unit tests to test
    filtered beef data frame from the dataset
    """
    def test_smoke(self):
        """Smoke test to ensure function runs without errors
        """
        beef_data(test_beef_data, "high")

    def test_one_shot(self):
        """One- shot test with possible inputs
        """
        high_result = beef_data(test_beef_data, "high")
        self.assertEqual(len(high_result), 5)

        med_result = beef_data(test_beef_data, "med")
        self.assertEqual(len(med_result), 5)

        low_result = beef_data(test_beef_data, "low")
        self.assertEqual(len(low_result), 5)

    def test_edge(self):
        """Edge test with invalid inputs
        """
        # Edge test with different risk level
        with self.assertRaises(ValueError):
            beef_data(test_beef_data, "riskaab")

        # Testing for empty DataFrame when no matching rows found
        with self.assertRaises(ValueError):
            beef_data(pd.DataFrame(), "high")

class TestFishData(unittest.TestCase):
    """This class contains unit tests to test
    filtered fish data frame from the dataset
    """
    def test_smoke(self):
        """Smoke test to ensure function runs without errors
        """
        fish_data(test_fish_data, "high")

    def test_one_shot(self):
        """One- shot test with possible inputs
        """
        high_result = fish_data(test_fish_data, "high")
        self.assertEqual(len(high_result), 5)

        med_result = fish_data(test_fish_data, "med")
        self.assertEqual(len(med_result), 5)

        low_result = fish_data(test_fish_data, "low")
        self.assertEqual(len(low_result), 5)

    def test_edge(self):
        """Edge test with invalid inputs
        """
        # Edge test with different risk level
        with self.assertRaises(ValueError):
            fish_data(test_fish_data, "riskaab")

        # Testing for empty DataFrame when no matching rows found
        with self.assertRaises(ValueError):
            fish_data(pd.DataFrame(), "high")

class TestPoultryData(unittest.TestCase):
    """This class contains unit tests to test
    filtered poultry data frame from the dataset
    """
    def test_smoke(self):
        """Smoke test to ensure function runs without errors
        """
        poultry_data(test_poultry_data, "high")

    def test_one_shot(self):
        """One- shot test with possible inputs
        """
        high_result = poultry_data(test_poultry_data, "high")
        self.assertEqual(len(high_result), 5)

        med_result = poultry_data(test_poultry_data, "med")
        self.assertEqual(len(med_result), 5)

        low_result = poultry_data(test_poultry_data, "low")
        self.assertEqual(len(low_result), 5)

    def test_edge(self):
        """Edge test with invalid inputs
        """
        # Edge test with different risk level
        with self.assertRaises(ValueError):
            poultry_data(test_poultry_data, "riskaab")

        # Testing for empty DataFrame when no matching rows found
        with self.assertRaises(ValueError):
            poultry_data(pd.DataFrame(), "high")

class TestPorkData(unittest.TestCase):
    """This class contains unit tests to test
    filtered pork data frame from the dataset
    """
    def test_smoke(self):
        """Smoke test to ensure function runs without errors
        """
        pork_data(test_pork_data, "high")

    def test_one_shot(self):
        """One- shot test with possible inputs
        """
        high_result = pork_data(test_pork_data, "high")
        self.assertEqual(len(high_result), 5)

        med_result = pork_data(test_pork_data, "med")
        self.assertEqual(len(med_result), 5)

        low_result = pork_data(test_pork_data, "low")
        self.assertEqual(len(low_result), 5)

    def test_edge(self):
        """Edge test with invalid inputs
        """
        # Edge test with different risk level
        with self.assertRaises(ValueError):
            pork_data(test_pork_data, "riskaab")

        # Testing for empty DataFrame when no matching rows found
        with self.assertRaises(ValueError):
            pork_data(pd.DataFrame(), "high")

class TestLegumesData(unittest.TestCase):
    """This class contains unit tests to test
    filtered legumes data frame from the dataset
    """
    def test_smoke(self):
        """Smoke test to ensure function runs without errors
        """
        legumes_data(test_legumes_data, "high")

    def test_one_shot(self):
        """One- shot test with possible inputs
        """
        high_result = legumes_data(test_legumes_data, "high")
        self.assertEqual(len(high_result), 5)

        med_result = legumes_data(test_legumes_data, "med")
        self.assertEqual(len(med_result), 5)

        low_result = legumes_data(test_legumes_data, "low")
        self.assertEqual(len(low_result), 5)

    def test_edge(self):
        """Edge test with invalid inputs
        """
        # Edge test with different risk level
        with self.assertRaises(ValueError):
            legumes_data(test_legumes_data, "riskaab")

        # Testing for empty DataFrame when no matching rows found
        with self.assertRaises(ValueError):
            legumes_data(pd.DataFrame(), "high")

class TestGrainsData(unittest.TestCase):
    """This class contains unit tests to test
    filtered grains data frame from the dataset
    """
    def test_smoke(self):
        """Smoke test to ensure function runs without errors
        """
        grains_data(test_grains_data, "high")

    def test_one_shot(self):
        """One- shot test with possible inputs
        """
        high_result = grains_data(test_grains_data, "high")
        self.assertEqual(len(high_result), 5)

        med_result = grains_data(test_grains_data, "med")
        self.assertEqual(len(med_result), 5)

        low_result = grains_data(test_grains_data, "low")
        self.assertEqual(len(low_result), 5)

    def test_edge(self):
        """Edge test with invalid inputs
        """
        # Edge test with different risk level
        with self.assertRaises(ValueError):
            grains_data(test_grains_data, "riskaab")

        # Testing for empty DataFrame when no matching rows found
        with self.assertRaises(ValueError):
            grains_data(pd.DataFrame(), "high")

class TestVeganGrainsData(unittest.TestCase):
    """This class contains unit tests to test
    filtered grains data frame from the dataset
    """
    def test_smoke(self):
        """Smoke test to ensure function runs without errors
        """
        vegan_grains_data(test_grains_data)

    def test_one_shot(self):
        """One- shot test with possible inputs
        """
        result = vegan_grains_data(test_grains_data)
        self.assertEqual(len(result), 5)

    def test_edge(self):
        """Edge test with invalid inputs
        """
        # Testing for empty DataFrame when no matching rows found
        with self.assertRaises(ValueError):
            vegan_grains_data(pd.DataFrame())

class TestFruitsData(unittest.TestCase):
    """This class contains unit tests to test
    filtered fruits data frame from the dataset
    """
    def test_smoke(self):
        """Smoke test to ensure function runs without errors
        """
        fruits_data(test_fruits_data)

    def test_one_shot(self):
        """One- shot test with possible inputs
        """
        result = fruits_data(test_fruits_data)
        self.assertEqual(len(result), 5)

    def test_edge(self):
        """Edge test with invalid inputs
        """
        # Testing for empty DataFrame when no matching rows found
        with self.assertRaises(ValueError):
            fruits_data(pd.DataFrame())

class TestVegetableData(unittest.TestCase):
    """This class contains unit tests to test
    filtered vegatable data frame from the dataset
    """
    def test_smoke(self):
        """Smoke test to ensure function runs without errors
        """
        vegetable_data(test_vegetables_data, "vegan")

    def test_one_shot(self):
        """One- shot test with possible inputs
        """
        high_result = vegetable_data(test_vegetables_data, "vegan")
        self.assertEqual(len(high_result), 5)

        med_result = vegetable_data(test_vegetables_data, "vegetarian")
        self.assertEqual(len(med_result), 5)

        low_result = vegetable_data(test_vegetables_data, "non vegetarian")
        self.assertEqual(len(low_result), 5)

    def test_edge(self):
        """Edge test with invalid inputs
        """
        # Edge test with different risk level
        with self.assertRaises(ValueError):
            vegetable_data(test_vegetables_data, "riskaab")

        # Testing for empty DataFrame when no matching rows found
        with self.assertRaises(ValueError):
            vegetable_data(pd.DataFrame(), "vegan")

class TestDairyData(unittest.TestCase):
    """This class contains unit tests to test
    filtered dairy data frame from the dataset
    """
    def test_smoke(self):
        """Smoke test to ensure function runs without errors
        """
        dairy_data(test_dairy_data, "high")

    def test_one_shot(self):
        """One- shot test with possible inputs
        """
        high_result = dairy_data(test_dairy_data, "high")
        self.assertEqual(len(high_result), 5)

        med_result = dairy_data(test_dairy_data, "med")
        self.assertEqual(len(med_result), 5)

        low_result = dairy_data(test_dairy_data, "low")
        self.assertEqual(len(low_result), 5)

    def test_edge(self):
        """Edge test with invalid inputs
        """
        # Edge test with different risk level
        with self.assertRaises(ValueError):
            dairy_data(test_dairy_data, "riskaab")

        # Testing for empty DataFrame when no matching rows found
        with self.assertRaises(ValueError):
            dairy_data(pd.DataFrame(), "high")

class TestRecommendedFood(unittest.TestCase):
    """This class contains unit tests to test
    for displaying the concatenated dataframes of each food group based on
    food preference and obesity risk score.
    """
    def setUp(self):
        """set up test data
        """
        self.test_data = pd.read_csv("LiveLite/tests/data/food_nutrition_test_data.csv")

    #smoke test
    def smoke_test(self):
        """Smoke test to ensure function runs without errors
        """
        recommended_food(self.test_data, 34, "vegetarian")

    # One- shot test
    def test_one_shot(self):
        """One- shot test with possible inputs
        """
        result = recommended_food(self.test_data, 50, "non vegetarian")
        self.assertIsInstance(result, pd.DataFrame)
        expected_columns = ["Food Category", "Description (per 100gms)", "Calories (kcal)",
                            "Protein (gm)", "Fat (gm)", "Carbohydrates (gm)",
                            "Sugar (gm)", "Fiber (gm)"]
        self.assertCountEqual(result.columns, expected_columns)
        self.assertEqual(len(result), 40)

    # edge tests:
    def test_empty_input(self):
        """Test case for empty input DataFrame
        """
        with self.assertRaises(ValueError):
            recommended_food(pd.DataFrame(), 50, "vegetarian")

    def test_invalid_food_preference(self):
        """Test case for invalid food preference
        """
        with self.assertRaises(ValueError):
            recommended_food(self.test_data, 50, "invalid")

    def test_invalid_risk_score(self):
        """Test case for invalid risk score
        """
        with self.assertRaises(TypeError):
            recommended_food(self.test_data, "high", "vegetarian")

    def test_risk_score_out_of_range(self):
        """Test case for risk score out of range
        """
        with self.assertRaises(ValueError):
            recommended_food(self.test_data, 150, "vegetarian")

    def test_invalid_food_preference_type(self):
        """Test case for invalid food preference type
        """
        with self.assertRaises(TypeError):
            recommended_food(self.test_data, 50, 123)

class TestSearchFood(unittest.TestCase):
    """This class contains unit tests to test
    for displaying relevant food information based on user input string.
    """
    def setUp(self):
        """set up test data
        """
        self.search_data = pd.read_csv("LiveLite/tests/data/food_nutrition_test_data.csv")

    #smoke test
    def smoke_test(self):
        """Smoke test to ensure function runs without errors
        """
        search_food(self.search_data, "milk")

    # One shot test
    def test_search_existing_food(self):
        """One- shot test with possible inputs
        """
        result = search_food(self.search_data, "apple")
        self.assertIsInstance(result, pd.DataFrame)
        self.assertGreaterEqual(len(result), 1)
        found = any("apple" in desc.lower() for desc in result["Description (per 100gms)"].values)
        self.assertTrue(found)

    # Edge test
    def test_invalid_food_item_type(self):
        """Test case for invalid food item type
        """
        with self.assertRaises(TypeError):
            search_food(self.search_data, 123)

    def test_empty_food_item(self):
        """Test case for empty food item
        """
        result = search_food(self.search_data, "")
        self.assertIsNone(result)

    def test_search_nonexistent_food(self):
        """Test case for searching a nonexistent food item
        """
        result = search_food(self.search_data, "Jake")
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
