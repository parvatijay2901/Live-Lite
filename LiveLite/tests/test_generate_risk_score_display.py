"""
This module contains unit tests for functions related to
displaying risk score in the LiveLite module.

Class:
- TestRiskScoreDisplay: Contains test cases for the functions in
                        displaying risk score in LiveLite module.
"""

import unittest
import LiveLite

class TestRiskScoreDisplay(unittest.TestCase):
    """Test cases for the functions in displaying risk score"""

    def test_get_input_for_risk_score_invalid_str_input(self):
        """Test invalid input (str) for get_input_for_risk_score"""
        with self.assertRaises(TypeError):
            LiveLite.get_input_for_risk_score("not_a_dict")

    def test_get_input_for_risk_score_invalid_mapped_input(self):
        """Test invalid input (missing keys) for get_input_for_risk_score"""
        mapped_user_inputs = {'internal_mental_health': 1,
                            'internal_poor_appetite_overeating': 0}
        with self.assertRaises(ValueError):
            LiveLite.get_input_for_risk_score(mapped_user_inputs)

    def test_get_input_for_risk_score_valid_input(self):
        """Test valid input for get_input_for_risk_score"""
        mapped_user_inputs = {'internal_mental_health': 1,
                            'internal_poor_appetite_overeating': 0,
                            'internal_activity_level': 2,
                            'internal_diet_condition': 1,
                            'internal_health_condition': 1,
                            'internal_sex': 0,
                            'internal_age': 30,
                            'internal_ethnicity': 1,
                            'internal_smoke_cig': 0,
                            'internal_sleep_hrs': 6}
        result = LiveLite.get_input_for_risk_score(mapped_user_inputs)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 10)

    def test_display_risk_score_invalid_input(self):
        """Test invalid input for display_risk_score"""
        # Invalid input (str) instead of float risk_score
        with self.assertRaises(TypeError):
            LiveLite.display_risk_score("risk_score", "blue")
        # Invalid input - negative risk_score
        with self.assertRaises(ValueError):
            LiveLite.display_risk_score(-50.0, "red")
        # Invalid input - >100 risk_score
        with self.assertRaises(ValueError):
            LiveLite.display_risk_score(150.0, "red")
        # Invalid input (int) instead of str color
        with self.assertRaises(TypeError):
            LiveLite.display_risk_score(50.0, 1)

    def test_display_risk_score_valid_input1(self):
        """Test valid input for display_risk_score"""
        risk_score = 19.5
        color = "yellow"
        result = LiveLite.display_risk_score(risk_score, color)
        self.assertIn("<svg", result)
        self.assertIn("19.5%", result)

    def test_display_risk_score_valid_input2(self):
        """Test valid input for display_risk_score"""
        risk_score = 49.5
        color = "yellow"
        result = LiveLite.display_risk_score(risk_score, color)
        self.assertIn("<svg", result)
        self.assertIn("49.5%", result)

    def test_display_risk_score_valid_input3(self):
        """Test valid input for display_risk_score"""
        risk_score = 69.5
        color = "yellow"
        result = LiveLite.display_risk_score(risk_score, color)
        self.assertIn("<svg", result)
        self.assertIn("69.5%", result)

    def test_display_risk_score_valid_input4(self):
        """Test valid input for display_risk_score"""
        risk_score = 99.5
        color = "yellow"
        result = LiveLite.display_risk_score(risk_score, color)
        self.assertIn("<svg", result)
        self.assertIn("99.5%", result)

    def test_display_risk_score_valid_input5(self):
        """Test valid input for display_risk_score"""
        risk_score = 100.0
        color = "yellow"
        result = LiveLite.display_risk_score(risk_score, color)
        self.assertIn("<svg", result)
        self.assertIn("Obese", result)

    def test_display_risk_suggestion_invalid_input(self):
        """Test invalid input for display_risk_suggestion"""
        # Invalid input (str) instead of float risk_score
        with self.assertRaises(TypeError):
            LiveLite.display_risk_suggestion("risk_score")
        # Invalid input - negative risk_score
        with self.assertRaises(ValueError):
            LiveLite.display_risk_suggestion(-50.0)

    def test_display_risk_suggestion_valid_input(self):
        """Test valid input for display_risk_suggestion"""
        risk_scores = [5.0, 30.5, 60.0, 90.0, 100.0]
        for risk_score in risk_scores:
            LiveLite.display_risk_suggestion(risk_score)
            # No output from this function

if __name__ == '__main__':
    unittest.main()
