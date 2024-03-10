import unittest
from unittest import mock
import LiveLite

class TestComprehensiveGuide(unittest.TestCase):
    @mock.patch("streamlit.button")
    @mock.patch("streamlit.switch_page")
    def test_navigation_not_called(self, mock_switch_page, mock_button):
        mock_button.return_value = False
        LiveLite.pageb()
        mock_switch_page.assert_not_called()

    @mock.patch("streamlit.button")
    @mock.patch("streamlit.switch_page")
    def test_navigation_to_risk_insights(self, mock_switch_page, mock_button):
        mock_button.return_value = True
        LiveLite.pageb()
        mock_switch_page.assert_called_with("pages/c_risk_insights.py")

    @mock.patch('os.path.exists')
    @mock.patch('streamlit.button')
    def test_navigation_invalid_path(self, mock_button, mock_path):
        """Testing navigation to other pages - with invalid path"""
        mock_button.return_value = True
        mock_path.return_value = False
        with self.assertRaises(FileNotFoundError):
            LiveLite.pageb()

if __name__ == "__main__":
    unittest.main()
