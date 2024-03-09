import unittest
import pandas as pd
#from LiveLite import personalised_food_list
from LiveLite.recommendation_tool.diet_recommendation.personalised_food_list import search_food, recommended_food, beef_data

sample_food_data = pd.DataFrame({
    "FoodGroup": ["Beef Products"] * 100,
    "Descrip": ["Beef Products"] * 100,
    "Protein_g": range(100),
    "Fat_g": range(100),
    "Energy_kcal": range(100)
})

class TestBeefData(unittest.TestCase):
    def test_smoke(self):
        # Smoke test to ensure function runs without errors
        beef_data(sample_food_data, "high")
        

    def test_one_shot(self):
        # One-shot test with a single input
        result = beef_data(sample_food_data, "high")
        self.assertEqual(len(result), 5)

        high_result = beef_data(sample_food_data, "high")
        self.assertEqual(len(high_result), 5)

        med_result = beef_data(sample_food_data, "med")
        self.assertEqual(len(med_result), 5)

        low_result = beef_data(sample_food_data, "low")
        self.assertEqual(len(low_result), 5)

    def test_edge(self):
        # Edge test with different risk levels

        # Testing for empty DataFrame when no matching rows found
        with self.assertRaises(ValueError):
            beef_data(pd.DataFrame(), "high")

        #empty_result = beef_data(pd.DataFrame(), "high")
        #self.assertTrue(empty_result.empty)

if __name__ == '__main__':
    unittest.main()
    