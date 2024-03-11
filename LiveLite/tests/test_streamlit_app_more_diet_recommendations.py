import unittest
from pathlib import Path
from unittest import mock
import LiveLite
import pandas as pd

THIS_DIR = Path(__file__).parent
class TestMoreDietRecommendations(unittest.TestCase):
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

        recommended_food_path = THIS_DIR.parent / 'tests/data/sample_recommended_food_df.csv'
        self.recommended_food = pd.read_csv(recommended_food_path)

        food_nutrition_data_path = THIS_DIR.parent / 'data/input_files/food_nutrition_data.csv'
        self.food_nutrition_data = pd.read_csv(food_nutrition_data_path)

        self.mock_session_state1 = {"user_inputs": self.mock_user_inputs,
                                    "calorie_intake": 2000,
                                    "food_nutrition_data":self.food_nutrition_data,
                                    "preferred_exercise_intensity_level":"moderate",
                                    "risk_score":50.0,
                                    "food_preference":"vegetarian",
                                    "recommended_foods_df":self.recommended_food,
                                    "search_food_items":""}

        self.mock_session_state2 = {"user_inputs": self.mock_user_inputs,
                                    "calorie_intake": 2000,
                                    "food_nutrition_data":self.food_nutrition_data,
                                    "preferred_exercise_intensity_level":"moderate",
                                    "risk_score":50.0,
                                    "food_preference":"vegetarian",
                                    "recommended_foods_df":self.recommended_food,
                                    "search_food_items":"milk"}

        self.mock_session_state3 = {"user_inputs": self.mock_user_inputs,
                                    "calorie_intake": 2000,
                                    "food_nutrition_data":self.food_nutrition_data,
                                    "preferred_exercise_intensity_level":"moderate",
                                    "risk_score":50.0,
                                    "food_preference":"vegetarian"}

    @mock.patch("streamlit.button")
    @mock.patch("streamlit.switch_page")
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_age', return_value=37)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sex', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_ethnicity', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_activity_level', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_mental_health', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sleep_hours', return_value=2)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_health_condition', return_value=4)
    def test_page_functioning_input1(self, mock_health_condition, mock_sleep_hours, mock_mental_health, mock_activity_level, mock_ethnicity, mock_sex, mock_age, mock_switch_page, mock_button):
        with mock.patch('streamlit.session_state', self.mock_session_state1):
            mock_button.return_value = True
            LiveLite.pagee()
            self.assertTrue(True)

    @mock.patch("streamlit.button")
    @mock.patch("streamlit.switch_page")
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_age', return_value=37)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sex', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_ethnicity', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_activity_level', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_mental_health', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sleep_hours', return_value=2)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_health_condition', return_value=4)
    def test_page_functioning_input2(self, mock_health_condition, mock_sleep_hours, mock_mental_health, mock_activity_level, mock_ethnicity, mock_sex, mock_age, mock_switch_page, mock_button):
        with mock.patch('streamlit.session_state', self.mock_session_state2):
            mock_button.return_value = True
            LiveLite.pagee()
            self.assertTrue(True)

    @mock.patch("streamlit.button")
    @mock.patch("streamlit.switch_page")
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_age', return_value=37)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sex', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_ethnicity', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_activity_level', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_mental_health', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sleep_hours', return_value=2)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_health_condition', return_value=4)
    def test_page_functioning_input3(self, mock_health_condition, mock_sleep_hours, mock_mental_health, mock_activity_level, mock_ethnicity, mock_sex, mock_age, mock_switch_page, mock_button):
        with mock.patch('streamlit.session_state', self.mock_session_state3):
            mock_button.return_value = True
            LiveLite.pagee()
            self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
