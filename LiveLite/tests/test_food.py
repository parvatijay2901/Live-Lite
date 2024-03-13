"""This script contains unit tests for all the functions
used to calculate macro and micro nutrients daily intake and
recommended quanitities of food groups to be included daily.
"""
import unittest
import pandas as pd
from LiveLite import recommended_protein, recommended_grains, recommended_fat
from LiveLite import recommended_vegetables, recommended_fruits
from LiveLite import macro_calorie, macro_nutrients_data, micro_nutrients

class TestRecommendedProtein(unittest.TestCase):
    """This class tests the recommended protein intake function
    """
    def test_smoke(self):
        """Smoke Test
        """
        recommended_protein(25, 0)

    # One-shot Test
    def test_minimum_age(self):
        """testing the functions with boundary values of age
        """
        self.assertEqual(recommended_protein(18, 0), (57, 128))

    def test_maximum_age(self):
        """testing the functions with boundary values of age
        """
        self.assertEqual(recommended_protein(100, 0), (57, 113))

    def test_minimum_male_age(self):
        """testing the functions with boundary values gender
        """
        self.assertEqual(recommended_protein(18, 1), (99, 142))

    def test_maximum_male_age(self):
        """testing the functions with boundary values gender
        """
        self.assertEqual(recommended_protein(100, 1), (71, 128))

    # Edge Test
    def test_invalid_age(self):
        """testing the functions with invalid age
        """
        with self.assertRaises(ValueError):
            recommended_protein(110, 0)

    def test_invalid_age_type(self):
        """testing the functions with invalid age
        """
        with self.assertRaises(TypeError):
            recommended_protein("25", 0)

    def test_invalid_gender(self):
        """testing the functions with invalid gender
        """
        with self.assertRaises(ValueError):
            recommended_protein(25, 2)

    def test_invalid_gender_type(self):
        """testing the functions with invalid gender
        """
        with self.assertRaises(TypeError):
            recommended_protein(25, "male")

class TestRecommendedGrains(unittest.TestCase):
    """This class tests the recommended grains intake function
    """
    #smoke test
    def test_smoke(self):
        """Smoke Test
        """
        recommended_grains(25, 0)

    #One shot test
    def test_valid_input_female_above_30(self):
        """testing the function with different input values
        """
        self.assertEqual(recommended_grains(35, 0), (142, 198, 85, 99))

    def test_valid_input_male_18_60(self):
        """testing the function with different input values
        """
        self.assertEqual(recommended_grains(40, 1), (198, 283, 99, 142))

    def test_valid_input_male_above_60(self):
        """testing the function with different input values
        """
        self.assertEqual(recommended_grains(65, 1), (170, 255, 85, 128))

    # edge test
    def test_invalid_age(self):
        """testing the functions with invalid age
        """
        with self.assertRaises(ValueError):
            recommended_grains(110, 0)

    def test_invalid_age_type(self):
        """testing the functions with invalid age
        """
        with self.assertRaises(TypeError):
            recommended_grains("25", 0)

    def test_invalid_gender(self):
        """testing the functions with invalid gender
        """
        with self.assertRaises(ValueError):
            recommended_grains(25, 2)

    def test_invalid_gender_type(self):
        """testing the functions with invalid gender
        """
        with self.assertRaises(TypeError):
            recommended_grains(25, "male")

class TestRecommendedFat(unittest.TestCase):
    """This class tests the recommended fat intake function
    """
    #Smoke test
    def smoke_test(self):
        """Smoke Test
        """
        recommended_fat(2000)

    #One- shot test
    def test_calorie_1000(self):
        """testing the function with different input values
        """
        self.assertEqual(recommended_fat(1000), 50)

    def test_calorie_2000(self):
        """testing the function with different input values
        """
        self.assertEqual(recommended_fat(2000), 50)

    def test_calorie_2500(self):
        """testing the function with different input values
        """
        self.assertEqual(recommended_fat(2500), 67)

    # edge test
    def test_negative_calorie(self):
        """testing the functions with invalid calorie values
        """
        with self.assertRaises(ValueError):
            recommended_fat(-100)

    def test_invalid_calorie_type(self):
        """testing the functions with invalid calorie values
        """
        with self.assertRaises(TypeError):
            recommended_fat("2000")

class TestRecommendedFruits(unittest.TestCase):
    """This class tests the recommended fruits intake function
    """
    #Smoke test
    def smoke_test(self):
        """Smoke Test
        """
        recommended_fruits(0)

    # One- shot test
    def test_female(self):
        """testing the function with different input values
        """
        self.assertEqual(recommended_fruits(0), (1.5, 2))

    def test_male(self):
        """testing the function with different input values
        """
        self.assertEqual(recommended_fruits(1), (2, 2.5))

    #edge test
    def test_invalid_gender(self):
        """testing the functions with invalid gender
        """
        with self.assertRaises(ValueError):
            recommended_fruits(2)

    def test_invalid_gender_type(self):
        """testing the functions with invalid gender
        """
        with self.assertRaises(TypeError):
            recommended_fruits("male")

class TestRecommendedVegetables(unittest.TestCase):
    """This class tests the recommended vegetables intake function
    """
    #Smoke test
    def smoke_test(self):
        """Smoke Test
        """
        recommended_vegetables(25,0)

    # One shot tests
    def test_female_18_to_30(self):
        """testing the function with different input values
        """
        self.assertEqual(recommended_vegetables(25, 0), (2.5, 3))

    def test_female_above_30(self):
        """testing the function with different input values
        """
        self.assertEqual(recommended_vegetables(35, 0), (2, 3))

    def test_male_18_to_60(self):
        """testing the function with different input values
        """
        self.assertEqual(recommended_vegetables(40, 1), (3, 4))

    def test_male_above_60(self):
        """testing the function with different input values
        """
        self.assertEqual(recommended_vegetables(65, 1), (2.5, 3.5))

    # Edge test
    def test_invalid_age(self):
        """testing the functions with invalid age
        """
        with self.assertRaises(ValueError):
            recommended_vegetables(110, 0)

    def test_invalid_age_type(self):
        """testing the functions with invalid age
        """
        with self.assertRaises(TypeError):
            recommended_vegetables("25", 0)

    def test_invalid_gender(self):
        """testing the functions with invalid gender
        """
        with self.assertRaises(ValueError):
            recommended_vegetables(25, 2)

    def test_invalid_gender_type(self):
        """testing the functions with invalid gender
        """
        with self.assertRaises(TypeError):
            recommended_vegetables(25, "male")

class TestMacroCalorie(unittest.TestCase):
    """This class tests the recommended macro calories portion function
    """
    # smoke test
    def smoke_test(self):
        """Smoke Test
        """
        macro_calorie("fat",2500)

    # One shot test
    def test_protein(self):
        """testing the function with different input values
        """
        self.assertEqual(macro_calorie("protein", 2000), (200, 600))

    def test_carbohydrate(self):
        """testing the function with different input values
        """
        self.assertEqual(macro_calorie("carbohydrate", 2000), (900, 1300))

    def test_fat(self):
        """testing the function with different input values
        """
        self.assertEqual(macro_calorie("fat", 2000), (400, 600))

    # Edge test
    def test_invalid_macro(self):
        """testing the functions with invalid nutrient name
        """
        with self.assertRaises(ValueError):
            macro_calorie("fiber", 2000)

    def test_invalid_macro_type(self):
        """testing the functions with invalid nutrient name
        """
        with self.assertRaises(TypeError):
            macro_calorie(123, 2000)

    def test_negative_calorie(self):
        """testing the functions with invalid calorie values
        """
        with self.assertRaises(ValueError):
            macro_calorie("protein", -200)

    def test_invalid_calorie_type(self):
        """testing the functions with invalid calorie values
        """
        with self.assertRaises(TypeError):
            macro_calorie("protein", "2000")

class TestMacroNutrientsData(unittest.TestCase):
    """This class tests the recommended macro nutrients intake function
    """
    # Smoke test:
    def smoke_test(self):
        """Smoke Test
        """
        macro_nutrients_data(25,0,2500)

    # One shot test :
    def test_valid_input_female(self):
        """testing the function with different input values
        """
        result = macro_nutrients_data(25, 0, 2000)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 3)

    def test_valid_input_male(self):
        """testing the function with different input values
        """
        result = macro_nutrients_data(35, 1, 2500)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 3)

    # edge test
    def test_invalid_age(self):
        """testing the functions with invalid age
        """
        with self.assertRaises(ValueError):
            macro_nutrients_data(110, 0, 2000)

    def test_invalid_age_type(self):
        """testing the functions with invalid age
        """
        with self.assertRaises(TypeError):
            macro_nutrients_data("25", 0, 2000)

    def test_invalid_gender(self):
        """testing the functions with invalid gender
        """
        with self.assertRaises(ValueError):
            macro_nutrients_data(25, 2, 2000)

    def test_invalid_gender_type(self):
        """testing the functions with invalid gender
        """
        with self.assertRaises(TypeError):
            macro_nutrients_data(25, "male", 2000)

    def test_negative_calorie(self):
        """testing the functions with invalid calorie value
        """
        with self.assertRaises(ValueError):
            macro_nutrients_data(25, 0, -200)

    def test_invalid_calorie_type(self):
        """testing the functions with invalid calorie value
        """
        with self.assertRaises(TypeError):
            macro_nutrients_data(25, 0, "2000")

class TestMicroNutrients(unittest.TestCase):
    """This class tests the recommended micro nutrients intake function
    """
    # Smoke test:
    def smoke_test(self):
        """Smoke Test
        """
        micro_nutrients(45,0)

    # One shot test
    def test_valid_input_female(self):
        """testing the function with different input values
        """
        result = micro_nutrients(25, 0)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 1)

    def test_valid_input_male(self):
        """testing the function with different input values
        """
        result = micro_nutrients(35, 1)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 1)

    # edge test
    def test_invalid_age(self):
        """testing the functions with invalid age
        """
        with self.assertRaises(ValueError):
            micro_nutrients(110, 0)

    def test_invalid_age_type(self):
        """testing the functions with invalid age
        """
        with self.assertRaises(TypeError):
            micro_nutrients("25", 0)

    def test_invalid_gender(self):
        """testing the functions with invalid gender
        """
        with self.assertRaises(ValueError):
            micro_nutrients(25, 2)

    def test_invalid_gender_type(self):
        """testing the functions with invalid gender
        """
        with self.assertRaises(TypeError):
            micro_nutrients(25, "male")

if __name__ == '__main__':
    unittest.main()
