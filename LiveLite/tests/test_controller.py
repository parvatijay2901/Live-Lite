"""
This module contains unit tests for controller functions in the LiveLite module.
Class:
- TestController: This class contains test modules for the controller
                function in the LiveLite module.
"""
# pylint: disable=line-too-long
# pylint: disable=unused-argument
# pylint: disable=too-many-arguments
import unittest
from pathlib import Path
from unittest import mock
import pandas as pd
import LiveLite

THIS_DIR = Path(__file__).parent
class TestController(unittest.TestCase):
    """
    This class contains test cases for various choices passed to the controller function.
    """

    def setUp(self):
        """
        Set up necessary dependencies and mock data for the tests.
        """
        self.mock_user_inputs = {"age": 47,
                                "sex": "Male",
                                "height": 70,
                                "weight": 800,
                                "ethnicity": "Non-Hispanic Asian",
                                "activity_level": "Moderately Active",
                                "smoke_cig": "Yes",
                                "mental_health": "Occasionally these days",
                                "sleep_hrs": 3.0,
                                "health_condition": "Good",
                                "diet_condition": "Very Good",
                                "poor_appetite_overeating": "Nearly every day these days"}

        food_nutrition_data_path = THIS_DIR.parent / 'data/input_files/food_nutrition_data.csv'
        self.food_nutrition_data_path = pd.read_csv(food_nutrition_data_path)

        self.mock_session_state = {"user_inputs": self.mock_user_inputs,
                                "food_nutrition_data": self.food_nutrition_data_path,
                                "search_food_items": "milk"}

    def test_no_streamlit_session_state(self):
        """
        Test behavior when streamlit session state is not available.
        """
        with self.assertRaises(KeyError):
            LiveLite.controller("estimate_calorie_intake")

    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_age', return_value=37)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sex', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_ethnicity', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_activity_level', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_mental_health', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sleep_hours', return_value=2)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_health_condition', return_value=4)
    def test_invalid_choice(self, mock_health_condition, mock_sleep_hours, mock_mental_health, mock_activity_level,
                            mock_ethnicity, mock_sex, mock_age):
        """
        Test behavior when an invalid choice is passed to the controller function.
        """
        with mock.patch('streamlit.session_state', self.mock_session_state):
            with self.assertRaises(ValueError):
                LiveLite.controller("invalid_choice")

    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_age', return_value=37)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sex', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_ethnicity', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_activity_level', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_mental_health', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sleep_hours', return_value=2)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_health_condition', return_value=4)
    def test_risk_score_choice(self, mock_health_condition, mock_sleep_hours, mock_mental_health, mock_activity_level,
                                mock_ethnicity, mock_sex, mock_age):
        """
        Test behavior when 'risk_score' choice is passed to the controller function.
        """
        with mock.patch('streamlit.session_state', self.mock_session_state):
            LiveLite.controller("risk_score")

    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_age', return_value=37)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sex', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_ethnicity', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_activity_level', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_mental_health', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sleep_hours', return_value=2)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_health_condition', return_value=4)
    def test_diet_recommender_advanced_search_food_items_choice(self, mock_health_condition, mock_sleep_hours,
                                                                mock_mental_health, mock_activity_level,
                                                                mock_ethnicity, mock_sex, mock_age):
        """
        Test behavior when 'diet_recommender_advanced_search_food_items' choice is passed to the controller function.
        """
        with mock.patch('streamlit.session_state', self.mock_session_state):
            LiveLite.controller("diet_recommender_advanced_search_food_items")

if __name__ == '__main__':
    unittest.main()
