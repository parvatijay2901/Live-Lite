"""
This module contains unit tests for the functions defined in the LiveLite module.

Class:
- TestCommonModuleFunctions: contains individual test cases for each function.
"""
# pylint: disable=unused-argument
import unittest
from unittest import mock
import LiveLite
class TestCommonModuleFunctions(unittest.TestCase):
    """Test cases for LiveLite common module functions."""
    @mock.patch('os.path.exists')
    @mock.patch('streamlit.switch_page')
    def test_invalid_home_page(self, mock_switch_page, mock_wrong_path):
        """Test home_page function"""
        mock_wrong_path.side_effect = lambda path: False
        with self.assertRaises(FileNotFoundError):
            LiveLite.home_page()

    @mock.patch('os.path.exists')
    @mock.patch('streamlit.switch_page')
    def test_invalid_obesity_assessment_page(self, mock_switch_page, mock_wrong_path):
        """Test obesity_assessment_page function"""
        mock_wrong_path.side_effect = lambda path: False
        with self.assertRaises(FileNotFoundError):
            LiveLite.obesity_assessment_page()

    @mock.patch('os.path.exists')
    @mock.patch('streamlit.switch_page')
    def test_invalid_risk_insights_page(self, mock_switch_page, mock_wrong_path):
        """Test risk_insights_page function"""
        mock_wrong_path.side_effect = lambda path: False
        with self.assertRaises(FileNotFoundError):
            LiveLite.risk_insights_page()

    @mock.patch('os.path.exists')
    @mock.patch('streamlit.switch_page')
    def test_invalid_personalized_recommendations_page(self, mock_switch_page, mock_wrong_path):
        """Test personalized_recommendations_page function"""
        mock_wrong_path.side_effect = lambda path: False
        with self.assertRaises(FileNotFoundError):
            LiveLite.personalized_recommendations_page()

    def test_add_blank_lines_valid_inputs(self):
        """Test add_blank_lines function with valid inputs"""
        # Default argument
        LiveLite.add_blank_lines()

        # By giving an argument
        LiveLite.add_blank_lines(num_lines=2)

    def test_add_blank_lines_invalid_input(self):
        """Test add_blank_lines function"""
        # Test with invalid (str) input
        with self.assertRaises(TypeError):
            LiveLite.add_blank_lines(num_lines='2')
        # Test with invalid negative input
        with self.assertRaises(ValueError):
            LiveLite.add_blank_lines(num_lines=-2)
        LiveLite.add_blank_lines()

    @mock.patch('streamlit.button')
    @mock.patch('streamlit.switch_page')
    def test_swap_pages_back_valid_inputs(self, mock_switch_page, mock_button):
        """Test swap_pages_back with various valid choices"""

        # Test with choice = "obesity_assessment"
        choice = "obesity_assessment"
        LiveLite.swap_pages_back(choice)
        mock_button.assert_any_call("← Obesity Assessment 📑", use_container_width=True)
        mock_button.assert_any_call("→ Home🏠", use_container_width=True)

        # Test with choice = "basic_risk_insights"
        choice = "basic_risk_insights"
        LiveLite.swap_pages_back(choice)
        mock_button.assert_any_call("← Basic Risk Insights🏃🏼", use_container_width=True)
        mock_button.assert_any_call("→ Home🏠", use_container_width=True)

        # Test with choice = "basic_recommendations"
        choice = "basic_recommendations"
        LiveLite.swap_pages_back(choice)
        mock_button.assert_any_call("← Basic Recommendations🌿", use_container_width=True)
        mock_button.assert_any_call("→ Home🏠", use_container_width=True)

    def test_swap_pages_back_invalid_input(self):
        """Test swap_pages_back with an invalid choice"""
        with self.assertRaises(ValueError):
            LiveLite.swap_pages_back("invalid")

    def test_swap_page_back_invalid_input(self):
        """Test swap_pages_back with an invalid choice"""
        with self.assertRaises(ValueError):
            LiveLite.swap_page_back("invalid")

    @mock.patch('streamlit.session_state', {'data_ihme': True})
    @mock.patch('os.path.exists')
    @mock.patch('streamlit.switch_page')
    def test_check_session_state_variable_research(self, mock_switch_page, mock_wrong_path):
        """Test check_session_state_variable with choice 'research',
        when all session_state variables does not exist."""

        # Test if app.py exist
        LiveLite.check_session_state_variable("research")
        with self.assertRaises(AssertionError):
            mock_switch_page.assert_not_called()

        # Test if app.py doesn't exist
        mock_wrong_path.side_effect = lambda path: False
        with self.assertRaises(AssertionError):
            LiveLite.check_session_state_variable("research")

    @mock.patch('streamlit.session_state', {'user_inputs': True})
    @mock.patch('os.path.exists')
    @mock.patch('streamlit.switch_page')
    def test_check_session_state_variable_recommendations(self, mock_switch_page, mock_wrong_path):
        """Test check_session_state_variable with choice 'recommendations',
        when all session_state variables does not exist."""

        # Test if app.py exist
        LiveLite.check_session_state_variable("recommendations")
        with self.assertRaises(AssertionError):
            mock_switch_page.assert_not_called()

        # Test if app.py doesn't exist
        mock_wrong_path.side_effect = lambda path: False
        with self.assertRaises(AssertionError):
            LiveLite.check_session_state_variable("recommendations")

    def test_check_session_state_variable_invalid_choice(self):
        "Test check_session_state_variable with an invalid choice"
        with self.assertRaises(ValueError):
            LiveLite.check_session_state_variable("invalid")

if __name__ == '__main__':
    unittest.main()
