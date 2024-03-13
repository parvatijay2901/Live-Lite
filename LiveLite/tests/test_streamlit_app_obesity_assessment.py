"""
This module contains unit tests for functions related to the
Obesity Assessment page in the LiveLite module.

Class:
- TestObesityAssessment: Contains test cases for functions related to the
                        Obesity Assessment page in the LiveLite module.
"""
# pylint: disable=line-too-long

import unittest
from unittest import mock
import LiveLite

class TestObesityAssessment(unittest.TestCase):
    """
    Test cases for functions related to the Obesity Assessment page in the LiveLite module.
    """

    @mock.patch("streamlit.button")
    @mock.patch("streamlit.switch_page")
    def test_navigation_not_called(self, mock_switch_page, mock_button):
        """Test navigation not called when button is not clicked."""
        mock_button.return_value = False
        LiveLite.pageb()
        mock_switch_page.assert_not_called()

    @mock.patch("streamlit.button")
    @mock.patch("streamlit.switch_page")
    def test_navigation_to_risk_insights(self, mock_switch_page, mock_button):
        """Test navigation to Risk Insights page when button is clicked."""
        mock_button.return_value = True
        LiveLite.pageb()
        mock_switch_page.assert_called_with("pages/c_risk_insights.py")

    @mock.patch('os.path.exists')
    @mock.patch('streamlit.button')
    def test_navigation_invalid_path(self, mock_button, mock_path):
        """Test navigation to other pages with invalid path."""
        mock_button.return_value = True
        mock_path.return_value = False
        with self.assertRaises(FileNotFoundError):
            LiveLite.pageb()

if __name__ == "__main__":
    unittest.main()
