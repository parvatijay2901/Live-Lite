"""
This module contains unit tests for functions related to
Personalized Recommendations page in the LiveLite module.

Classes:
- TestPersonalizedRecommendations: Contains test cases for functions related to
                                Personalized Recommendations page in the LiveLite module.
"""
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=unused-argument
import unittest
from unittest import mock
from pathlib import Path
import pandas as pd
import LiveLite

THIS_DIR = Path(__file__).parent

class TestPersonalizedRecommendations(unittest.TestCase):
    """
    This class contains test cases for functions related to
    Personalized Recommendations page in the LiveLite module.
    """

    def setUp(self):
        """Mock the necessary dependencies."""
        self.mock_user_inputs = {
            "age": 90,
            "sex": "Male",
            "height": 150,
            "weight": 80,
            "ethnicity": "Mexican American",
            "activity_level": "Sedentary",
            "smoke_cig": "No",
            "mental_health": "Occasionally these days",
            "sleep_hrs": 1.0,
            "health_condition": "Excellent",
            "diet_condition": "Good",
            "poor_appetite_overeating": "Not at all"
        }

        food_nutrition_data_path = THIS_DIR.parent / 'data/input_files/food_nutrition_data.csv'
        self.food_nutrition_data_path = pd.read_csv(food_nutrition_data_path)

        self.mock_session_state = {
            "user_inputs": self.mock_user_inputs,
            "calorie_intake": 2500,
            "food_nutrition_data": self.food_nutrition_data_path,
            "preferred_exercise_intensity_level": "low"
        }

    @mock.patch("streamlit.button")
    @mock.patch("streamlit.switch_page")
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_age', return_value=37)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sex', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_ethnicity', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_activity_level', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_mental_health', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sleep_hours', return_value=2)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_health_condition', return_value=4)
    def test_navigation_to_more_recommendations(self, mock_health_condition, mock_sleep_hours, mock_mental_health, mock_activity_level, mock_ethnicity, mock_sex, mock_age, mock_switch_page, mock_button):
        """Test navigation to More Diet Recommendations page."""
        with mock.patch('streamlit.session_state', self.mock_session_state):
            mock_button.return_value = True
            LiveLite.paged()
            mock_switch_page.assert_called_with("pages/e_more_diet_recommendations.py")

    @mock.patch('os.path.exists')
    @mock.patch('streamlit.button')
    def test_navigation_invalid_path(self, mock_button, mock_path):
        """Test navigation to other pages with invalid path."""
        mock_button.return_value = True
        mock_path.return_value = False
        with self.assertRaises(AssertionError):
            LiveLite.paged()

if __name__ == "__main__":
    unittest.main()
