"""
This module contains unit tests for the user_input_mapping module.
Each test case evaluates different aspects of the function's behavior.

Classes:
- TestUserInputMapping

Dependencies:
- unittest module for unit testing framework
- user_input_mapping from user_input_mapping
"""
import unittest
from LiveLite import user_input_mapping # pylint: disable=import-error

class TestUserInputMapping(unittest.TestCase):
    """
    This class contains various test methods to verify the 
    correctness of the user_input_mapping function.
    
    The TestUserInputMapping class is inheriting from unittest.TestCase
    
    Attributes:
    - None

    Methods:
    - test_user_input_map_smoke()
    - test_user_input_map_1()
    - test_user_input_map_2()
    - test_user_input_map_3()
    - test_user_input_invalid_gender()
    - test_user_input_invalid_ethnicity()
    - test_user_input_invalid_activity()
    - test_user_input_invalid_health_condition()
    - test_user_input_invalid_health_condition()
    """
    def test_user_input_map_smoke(self):
        """
        Smoke test to test if the function runs without errors.
        """
        data = {"age": 85,
                "sex": "Female",
                "height": 60.96,
                "weight": 9.072,
                "ethnicity": "Non-hispanic Multiracial",
                "activity_level": "Extra Active",
                "smoke_cig": "Yes",
                "mental_health": "Not at all",
                "sleep_hrs": 16.0,
                "health_condition": "Excellent",
                "diet_condition": "Excellent",
                "poor_appetite_overeating": "Not at all"}
        user_input_mapping(data)

    def test_user_input_map_1(self):
        """
        One shot test to test if the function correctly maps the data
        """
        data = {"age": 18,
                "sex": "Male",
                "height": 60.96,
                "weight": 9.072,
                "ethnicity": "Hispanic",
                "activity_level": "Sedentary",
                "smoke_cig": "Yes",
                "mental_health": "Not at all",
                "sleep_hrs": 2.0,
                "health_condition": "Excellent",
                "diet_condition": "Excellent",
                "poor_appetite_overeating": "Not at all"}
        res = {'internal_age': 18,
                'internal_sex': 1,
                'internal_height': 154.8384,
                'internal_weight': 4.11498998064,
                'internal_ethnicity': 2,
                'internal_activity_level': 1,
                'internal_smoke_cig': 1,
                'internal_mental_health': 0,
                'internal_sleep_hrs': 2,
                'internal_health_condition': 1,
                'internal_diet_condition': 1,
                'internal_poor_appetite_overeating': 0}
        self.assertEqual(res, user_input_mapping(data))

    def test_user_input_map_2(self):
        """
        One shot test to test if the function correctly maps the data
        """
        data = {"age": 37,
                "sex": "Male",
                "height": 60.96,
                "weight": 9.072,
                "ethnicity": "Mexican American",
                "activity_level": "Minimally Active",
                "smoke_cig": "No",
                "mental_health": "Occasionally these days",
                "sleep_hrs": 1.0,
                "health_condition": "Very Good",
                "diet_condition": "Good",
                "poor_appetite_overeating": "Frequently these days"}
        res = {'internal_age': 37,
                'internal_sex': 1,
                'internal_height': 154.8384,
                'internal_weight': 4.11498998064,
                'internal_ethnicity': 1,
                'internal_activity_level': 2,
                'internal_smoke_cig': 0,
                'internal_mental_health': 1,
                'internal_sleep_hrs': 2,
                'internal_health_condition': 2,
                'internal_diet_condition': 3,
                'internal_poor_appetite_overeating': 2}
        self.assertEqual(res, user_input_mapping(data))

    def test_user_input_map_3(self):
        """
        One shot test to test if the function correctly maps the data
        """
        data = {"age": 37,
                "sex": "Male",
                "height": 100,
                "weight": 100,
                "ethnicity": "Non-Hispanic White",
                "activity_level": "Moderately Active",
                "smoke_cig": "No",
                "mental_health": "Occasionally these days",
                "sleep_hrs": 1.0,
                "health_condition": "Fair",
                "diet_condition": "Poor",
                "poor_appetite_overeating": "Nearly every day these days"}
        res = {'internal_age': 37,
                'internal_sex': 1,
                'internal_height': 254.0,
                'internal_weight': 45.359237,
                'internal_ethnicity': 3,
                'internal_activity_level': 3,
                'internal_smoke_cig': 0,
                'internal_mental_health': 1,
                'internal_sleep_hrs': 2,
                'internal_health_condition': 4,
                'internal_diet_condition': 5,
                'internal_poor_appetite_overeating': 3}
        self.assertEqual(res, user_input_mapping(data))

    def test_user_input_invalid_gender(self):
        """
        Edge Case: Test if the function raises ValueError for invalid gender.
        """
        data = {"age": 37,
                "sex": "bleeblublah",
                "height": 100,
                "weight": 100,
                "ethnicity": "Non-Hispanic Asian",
                "activity_level": "Moderately Active",
                "smoke_cig": "No",
                "mental_health": "Occasionally these days",
                "sleep_hrs": 1.0,
                "health_condition": "Fair",
                "diet_condition": "Poor",
                "poor_appetite_overeating": "Nearly every day these days"}
        with self.assertRaises(ValueError):
            user_input_mapping(data)

    def test_user_input_invalid_ethnicity(self):
        """
        Edge Case: Test if the function raises ValueError for invalid ethnicity.
        """
        data = {"age": 37,
                "sex": "Male",
                "height": 100,
                "weight": 100,
                "ethnicity": "Female",
                "activity_level": "Moderately Active",
                "smoke_cig": "No",
                "mental_health": "Occasionally these days",
                "sleep_hrs": 1.0,
                "health_condition": "Fair",
                "diet_condition": "Poor",
                "poor_appetite_overeating": "Nearly every day these days"}
        with self.assertRaises(ValueError):
            user_input_mapping(data)

    def test_user_input_invalid_activity(self):
        """
        Edge Case: Test if the function raises ValueError for invalid activity.
        """
        data = {"age": 37,
                "sex": "Male",
                "height": 100,
                "weight": 100,
                "ethnicity": "Non-Hispanic Asian",
                "activity_level": "Gym",
                "smoke_cig": "No",
                "mental_health": "Occasionally these days",
                "sleep_hrs": 1.0,
                "health_condition": "Fair",
                "diet_condition": "Poor",
                "poor_appetite_overeating": "Nearly every day these days"}
        with self.assertRaises(ValueError):
            user_input_mapping(data)

    def test_user_input_invalid_health_condition(self):
        """
        Edge Case: Test if the function raises ValueError for invalid health condition.
        """
        data = {"age": 37,
                "sex": "Male",
                "height": 100,
                "weight": 100,
                "ethnicity": "Hispanic",
                "activity_level": "Sedentary",
                "smoke_cig": "No",
                "mental_health": "Frequently these days",
                "sleep_hrs": 1.0,
                "health_condition": "Unhealthy",
                "diet_condition": "Poor",
                "poor_appetite_overeating": "Nearly every day these days"}
        with self.assertRaises(ValueError):
            user_input_mapping(data)

    def test_user_input_invalid_mental_condition(self):
        """
        Edge Case: Test if the function raises ValueError for invalid mental condition.
        """
        data = {"age": 37,
                "sex": "Male",
                "height": 100,
                "weight": 100,
                "ethnicity": "Hispanic",
                "activity_level": "Sedentary",
                "smoke_cig": "No",
                "mental_health": "Madddd",
                "sleep_hrs": 1.0,
                "health_condition": "Fair",
                "diet_condition": "Poor",
                "poor_appetite_overeating": "Nearly every day these days"}
        with self.assertRaises(ValueError):
            user_input_mapping(data)

if __name__ == '__main__':
    unittest.main()
    