"""
This module provides functions for calculating calorie intake
based on various factors such as weight, height, age, gender,
and activity level.

Classes:
- TestCalorieEstimate

Dependencies:
- unittest module for unit testing framework
- calculate_calorie_intake from calorie_intake_esstimate
"""
import unittest
from LiveLite import calculate_calorie_intake # pylint: disable=import-error

class TestCalorieEstimate(unittest.TestCase):
    """
    This class contains various test methods to verify the 
    correctness of the calculate_calorie_intake function.
    """

    # Smoke test
    def test_calorie_intake_smoke(self):
        """
        Smoke test to test if the function runs without errors.
        """
        calculate_calorie_intake(50, 170, 20, 1, 2)

    def test_calorie_intake_1(self):
        """
        One shot test to test if the function correctly estimates calories.
        """
        res = round(calculate_calorie_intake(50.6, 153.2, 30, 0, 4),2)
        self.assertAlmostEqual(2145.42,res,2)

    def test_calorie_intake_2(self):
        """
        One shot test to test if the function correctly estimates calories.
        """
        res = round(calculate_calorie_intake(70, 170, 24, 1, 2),2)
        self.assertAlmostEqual(2335.58,res,2)

    def test_invalid_gender(self):
        """
        Test the function with invalid gender input and check if it raises a ValueError.
        """
        with self.assertRaises(ValueError):
            calculate_calorie_intake(50, 170, 20, 4, 2)

    def test_invalid_activity_level(self):
        """
        Test the function with invalid activity level input and check if it raises a ValueError.
        """
        with self.assertRaises(ValueError):
            calculate_calorie_intake(50, 170, 20, 0, -8)

    def test_invalid_weight_type(self):
        """
        Test the function with invalid weight type input and check if it raises a TypeError.
        """
        with self.assertRaises(TypeError):
            calculate_calorie_intake("w", 170, 20, 0, 3)

    def test_invalid_height_type(self):
        """
        Test the function with invalid height type input and check if it raises a TypeError.
        """
        with self.assertRaises(TypeError):
            calculate_calorie_intake(60, -85, 20, 0, 3)

    def test_invalid_age_type(self):
        """
        Test the function with invalid age type input and check if it raises a TypeError.
        """
        with self.assertRaises(TypeError):
            calculate_calorie_intake(55.6, 170, 20.57, 0, 3)

if __name__ == '__main__':
    unittest.main()
