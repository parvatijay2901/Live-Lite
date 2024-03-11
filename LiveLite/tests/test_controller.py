import unittest
from pathlib import Path
from unittest import mock
import LiveLite
import pandas as pd

THIS_DIR = Path(__file__).parent
class TestController(unittest.TestCase):
    """Test suite for the controller function."""

    def setUp(self):
        """Mock the necessary dependencies."""
        self.mock_user_inputs = {"age": 37,
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

        food_nutrition_data_path = THIS_DIR.parent / 'data/input_files/food_nutrition_data.csv'
        self.food_nutrition_data_path = pd.read_csv(food_nutrition_data_path)

        self.mock_session_state = {"user_inputs": self.mock_user_inputs,
                                "food_nutrition_data":self.food_nutrition_data_path}

    def test_no_streamlit_session_state(self):
        with self.assertRaises(KeyError):
            LiveLite.controller("estimate_calorie_intake")

    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_age', return_value=37)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sex', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_ethnicity', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_activity_level', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_mental_health', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sleep_hours', return_value=2)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_health_condition', return_value=4)
    def test_invalid_choice(self, mock_health_condition, mock_sleep_hours, mock_mental_health, mock_activity_level, mock_ethnicity, mock_sex, mock_age):
        """Test estimate_calorie_intake choice."""
        with mock.patch('streamlit.session_state', self.mock_session_state):
        # mock_user_input_mapping.return_value = self.mock_mapped_user_inputs
            with self.assertRaises(ValueError):
                LiveLite.controller("invalid_choice")

if __name__ == '__main__':
    unittest.main()