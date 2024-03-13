"""
This module contains Unit tests for functions related to
Risk Insights page in the LiveLite module.

Class:
- TestRiskInsights: Contains test cases for functions related to
                Risk Insights page in the LiveLite module.
"""
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=unused-argument
import unittest
from pathlib import Path
from unittest import mock
import pandas as pd
import LiveLite

THIS_DIR = Path(__file__).parent

class TestRiskInsights(unittest.TestCase):
    """
    Test cases for functions related to Risk Insights page in the LiveLite module.
    """

    def setUp(self):
        """Mock the necessary dependencies."""
        self.mock_user_inputs = {
            "age": 24,
            "sex": "Male",
            "height": 160,
            "weight": 200,
            "ethnicity": "Non-Hispanic Black",
            "activity_level": "Minimally Active",
            "smoke_cig": "No",
            "mental_health": "Frequently these days",
            "sleep_hrs": 1.0,
            "health_condition": "Excellent",
            "diet_condition": "Good",
            "poor_appetite_overeating": "Nearly every day these days"
        }

        food_nutrition_data_path = THIS_DIR.parent / 'data/input_files/food_nutrition_data.csv'
        self.food_nutrition_data_path = pd.read_csv(food_nutrition_data_path)

        self.mock_session_state = {
            "user_inputs": self.mock_user_inputs,
            "calorie_intake": 2000,
            "food_nutrition_data": self.food_nutrition_data_path,
            "preferred_exercise_intensity_level": "moderate"
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
    def test_navigation_to_personalized_recommendations(self, mock_health_condition, mock_sleep_hours, mock_mental_health, mock_activity_level, mock_ethnicity, mock_sex, mock_age, mock_switch_page, mock_button):
        """Test navigation to Personalized Recommendations page."""
        with mock.patch('streamlit.session_state', self.mock_session_state):
            mock_button.return_value = True
            LiveLite.pagec()
            mock_switch_page.assert_called_with("pages/d_personalized_recommendations.py")

    @mock.patch('os.path.exists')
    @mock.patch('streamlit.button')
    def test_navigation_invalid_path(self, mock_button, mock_path):
        """Test navigation to other pages with invalid path."""
        mock_button.return_value = True
        mock_path.return_value = False
        with self.assertRaises(AssertionError):
            LiveLite.pagec()

if __name__ == "__main__":
    unittest.main()
