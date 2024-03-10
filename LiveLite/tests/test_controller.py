import unittest
from unittest import mock
import LiveLite
import pandas as pd

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

        self.mock_mapped_user_inputs_obese = {'internal_age': 37,
                                            'internal_sex': 1,
                                            'internal_height': 20.0,
                                            'internal_weight': 245.359237,
                                            'internal_ethnicity': 3,
                                            'internal_activity_level': 3,
                                            'internal_smoke_cig': 0,
                                            'internal_mental_health': 1,
                                            'internal_sleep_hrs': 2,
                                            'internal_health_condition': 4,
                                            'internal_diet_condition': 5,
                                            'internal_poor_appetite_overeating': 3}

        self.mock_mapped_user_inputs_not_obese = {'internal_age': 37,
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

        self.mock_input_risk_prediction = {'DPQ020': [3],
                                        'DPQ050': [3],
                                        'PAQ670': [1],
                                        'DBQ700': [5],
                                        'HUQ010': [5],
                                        'RIAGENDR': [1],
                                        'RIDAGEYR': [70],
                                        'RIDRETH3': [1],
                                        'SMQ040': [1],
                                        'SLD012': [2]}

        self.mock_session_state = {'user_inputs': self.mock_user_inputs,
                                'calorie_intake': 2000,
                                'preferred_exercise_intensity_level':'moderate',
                                'food_nutrition_data': {}}

        self.mock_macro_nutrients = pd.DataFrame({'Fruits (cups)': [1],
                                                'Vegetables (cups)': [2],
                                                'Dairy (cups)': [0.5]})

        self.mock_micro_nutrients = pd.DataFrame({'Macro Nutrient': ['Carbohydrate', 'Protein', 'Fat'],
                                                'Quantity in Grams': [100, 50, 30],
                                                'Kcal': ['200 - 150', '100 - 75', '150 - 120']})

        self.mock_physical_activity = [('Gym Activities',
                                    'Stretching, Hatha Yoga',
                                    '30 min', '123 kcal')]

    def test_no_streamlit_session_state(self):
        with self.assertRaises(KeyError):
            LiveLite.controller("estimate_calorie_intake")

    @mock.patch('streamlit.session_state')
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.user_input_mapping')
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_age', return_value=37)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sex', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_ethnicity', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_activity_level', return_value=3)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_mental_health', return_value=1)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sleep_hours', return_value=2)
    @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_health_condition', return_value=4)
    def test_invalid_choice(self, mock_health_condition, mock_sleep_hours, mock_mental_health, mock_activity_level, mock_ethnicity, mock_sex, mock_age, mock_user_input_mapping, mock_session_state):
        """Test estimate_calorie_intake choice."""
        mock_session_state.return_value = self.mock_session_state
        mock_user_input_mapping.return_value = self.mock_mapped_user_inputs_not_obese
        with self.assertRaises(ValueError):
            LiveLite.controller("invalid_choice")

    # @mock.patch('streamlit.session_state')
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.user_input_mapping')
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_age', return_value=37)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sex', return_value=1)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_ethnicity', return_value=3)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_activity_level', return_value=3)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_mental_health', return_value=1)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sleep_hours', return_value=2)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_health_condition', return_value=4)
    # def test_estimate_calorie_intake(self, mock_health_condition, mock_sleep_hours, mock_mental_health, mock_activity_level, mock_ethnicity, mock_sex, mock_age, mock_user_input_mapping, mock_session_state):
    #     """Test estimate_calorie_intake choice."""
    #     mock_session_state.return_value = self.mock_session_state
    #     mock_user_input_mapping.return_value = self.mock_mapped_user_inputs_not_obese
    #     calorie_intake = LiveLite.controller("estimate_calorie_intake")
    #     self.assertTrue(isinstance(calorie_intake, float))

    # @mock.patch('streamlit.session_state')
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.user_input_mapping')
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_age', return_value=37)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sex', return_value=1)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_ethnicity', return_value=3)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_activity_level', return_value=3)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_mental_health', return_value=1)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sleep_hours', return_value=2)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_health_condition', return_value=4)
    # @mock.patch('LiveLite.recommendation_tool.risk_assessment.is_obese.is_obese')
    # @mock.patch('LiveLite.project_integration.handle_user_input.generate_risk_score_display.get_input_for_risk_score')
    # @mock.patch('LiveLite.recommendation_tool.risk_assessment.risk_predictor.risk_predict')
    # def test_risk_score(self, mock_predicted_risk, mock_risk_model_input, mock_is_obese, mock_health_condition, mock_sleep_hours, mock_mental_health, mock_activity_level, mock_ethnicity, mock_sex, mock_age, mock_user_input_mapping, mock_session_state):
    #     """Test estimate_calorie_intake choice."""
    #     mock_session_state.return_value = self.mock_session_state

    #     mock_user_input_mapping.return_value = self.mock_mapped_user_inputs_obese
    #     mock_is_obese.return_value = True
    #     risk_score, color = LiveLite.controller("risk_score")
    #     self.assertTrue(isinstance(risk_score, float))
    #     self.assertTrue(isinstance(color, str))

    #     mock_user_input_mapping.return_value = self.mock_mapped_user_inputs_not_obese
    #     mock_is_obese.return_value = False
    #     mock_risk_model_input.return_value = self.mock_input_risk_prediction
    #     mock_predicted_risk.return_value = 50.0, "yellow"
    #     risk_score, color = LiveLite.controller("risk_score")
    #     self.assertTrue(isinstance(risk_score, float))
    #     self.assertTrue(isinstance(color, str))

    # @mock.patch('streamlit.session_state')
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.user_input_mapping')
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_age', return_value=37)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sex', return_value=1)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_ethnicity', return_value=3)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_activity_level', return_value=3)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_mental_health', return_value=1)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_sleep_hours', return_value=2)
    # @mock.patch('LiveLite.project_integration.handle_user_input.user_input_mapping.convert_health_condition', return_value=4)
    # @mock.patch('LiveLite.recommendation_tool.nutrition_estimation.calorie_intake.calorie_intake_estimate.calculate_calorie_intake')
    # @mock.patch('LiveLite.recommendation_tool.diet_recommendation.food.macro_nutrients_data')
    # @mock.patch('LiveLite.recommendation_tool.diet_recommendation.food.micro_nutrients')
    # @mock.patch('LiveLite.recommendation_tool.physical_activity_recommendation.physical_activity_recommend.calculate_calorie_burn')
    # def test_basic_recommender(self, mock_physical_activity, mock_micro_nutrients, mock_macro_nutrients, mock_calorie_intake, mock_health_condition, mock_sleep_hours, mock_mental_health, mock_activity_level, mock_ethnicity, mock_sex, mock_age, mock_user_input_mapping, mock_session_state):
    #     """Test estimate_calorie_intake choice."""
    #     mock_session_state.return_value = self.mock_session_state
    #     mock_user_input_mapping.return_value = self.mock_mapped_user_inputs_not_obese
    #     mock_calorie_intake.return_value = self.mock_session_state['calorie_intake']
    #     mock_macro_nutrients.return_value = self.mock_macro_nutrients
    #     mock_micro_nutrients.return_value = self.mock_micro_nutrients
    #     mock_physical_activity.return_value = self.mock_physical_activity
    #     recommender_basic = LiveLite.controller("recommender_basic")
    #     self.assertTrue(isinstance(recommender_basic, float))

if __name__ == '__main__':
    unittest.main()