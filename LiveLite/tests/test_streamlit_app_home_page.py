"""
This module contains test cases for the functions related to home page
navigation and loading data in the LiveLite module.

Class:
- TestHomepage: Contains test cases related to home page navigation and
loading data in the LiveLite module.
"""
import unittest
from unittest import mock
import LiveLite

class TestHomePage(unittest.TestCase):
    """
    Class containing test cases for the functions related to
    home page navigation and loading data in the LiveLite module.
    """

    @mock.patch('streamlit.button')
    @mock.patch('streamlit.switch_page')
    def test_navigation_button_understanding_obesity_valid_path(self,
                                                                mock_switch_page,
                                                                mock_button):
        """Testing navigation to Understand Obesity page - with valid path"""
        mock_button.side_effect = [True,False]
        LiveLite.app()
        mock_switch_page.assert_called_once_with("pages/a_understanding_obesity.py")

    @mock.patch('os.path.exists')
    @mock.patch('streamlit.button')
    def test_navigation_button_understanding_obesity_invalid_path(self, mock_button, mock_path):
        """Testing navigation to Understand Obesity page - with invalid path"""
        mock_button.return_value = True
        mock_path.return_value = False
        with self.assertRaises(FileNotFoundError):
            LiveLite.app()

    @mock.patch('streamlit.button')
    @mock.patch('streamlit.switch_page')
    def test_navigation_button_obesity_assessment_valid_path(self, mock_switch_page, mock_button):
        """Testing navigation to Obesity Assessment page - with valid path"""
        mock_button.side_effect = [False, True]
        LiveLite.app()
        mock_switch_page.assert_called_once_with("pages/b_obesity_assessment.py")

    @mock.patch('os.path.exists')
    def test_logo_invalid_path(self, mock_path):
        """Testing logo - with invalid path"""
        mock_path.return_value = False
        with self.assertRaises(FileNotFoundError):
            LiveLite.app()

    @mock.patch('streamlit.session_state', {})
    def test_load_data_valid_path(self):
        """Testing if input files are loaded properly"""
        LiveLite.load_data()

    @mock.patch('streamlit.session_state', {})
    @mock.patch('os.path.exists')
    def test_load_data_invalid_path(self, mock_path):
        """Testing with invalid paths - catch the raised error
        if input files are not loaded properly"""
        mock_path.return_value = False
        with self.assertRaises(FileNotFoundError):
            LiveLite.load_data()

if __name__ == "__main__":
    unittest.main()
