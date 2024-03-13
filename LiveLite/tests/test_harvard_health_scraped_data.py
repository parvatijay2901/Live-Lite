"""
This module contains unit tests for the harvard_health_scraped_data module.
Each test case evaluates different aspects of the function's behavior.

Classes:
- TestScrapeCaloriesData

Dependencies:
- unittest module for unit testing framework
- request module for html request mock
- scrape_calories_data from harvard_health_scraped_data
"""
import unittest
from unittest.mock import patch, MagicMock, Mock
import requests
from LiveLite import scrape_calories_data # pylint: disable=import-error

class TestScrapeCaloriesData(unittest.TestCase):
    """
    This class contains various test methods to verify the 
    correctness of the harvard_health_scraped_data module.
    
    The TestScrapeCaloriesData class is inheriting from unittest.TestCase
    
    Attributes:
    - None

    Methods:
    - test_scrape_calories_smoke()
    - test_scrape_calories_data_1()
    - def test_scrape_calories_data_2()
    - test_scrape_calories_connection_error()
    - test_scrape_calories_invalid_url()
    - test_scrape_calories_unexpected_webpage_structure()
    """
    def test_scrape_calories_smoke(self):
        """
        Smoke test to test if the function runs without errors.
        """
        with patch('requests.get') as mocked_get:
            mocked_response = MagicMock()
            mocked_response.content = b"Mocked HTML content"
            mocked_response.ok = True
            mocked_get.return_value = mocked_response
            scrape_calories_data("LiveLite/tests/data/calories_burned_30_minutes.csv")

    @patch('LiveLite.data.scripts_to_generate.harvard_health_scraped_data.requests.get')
    @patch('LiveLite.data.scripts_to_generate.harvard_health_scraped_data.csv.writer')
    def test_scrape_calories_data_1(self, mock_csv_writer, mock_get):
        """
        One shot test to compare the HTMl and ouput csv.
        """
        # Fake HTML content to be returned by the mock response
        fake_html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Calories Burned in 30 Minutes</title>
        </head>
        <body>
            <h1>Calories Burned in 30 Minutes</h1>
            
            <table>
                <h4>Outdoor</h4>
                <tr>
                    <th>Activity</th>
                    <th>Calories (125 lbs)</th>
                    <th>Calories (155 lbs)</th>
                    <th>Calories (185 lbs)</th>
                </tr>
                <tr>
                    <td>Running</td>
                    <td>260</td>
                    <td>372</td>
                    <td>444</td>
                </tr>
            </table>
        </body>
        </html>
        """
        # Mocking the response object
        mock_response = Mock()
        mock_response.content = fake_html_content.encode('utf-8')
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        scrape_calories_data("LiveLite/tests/data/calories_burned_30_minutes.csv")
        expected_data = [('Outdoor','Running',260,372,444,2.2933333333333334,5.05593867028813)]
        mock_csv_writer.return_value.writerows.assert_called_once_with(expected_data)

    @patch('LiveLite.data.scripts_to_generate.harvard_health_scraped_data.requests.get')
    @patch('LiveLite.data.scripts_to_generate.harvard_health_scraped_data.csv.writer')
    def test_scrape_calories_data_2(self, mock_csv_writer, mock_get):
        """
        One shot test to compare the HTMl and ouput csv.
        """
        # Fake HTML content to be returned by the mock response
        fake_html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Calories Burned in 30 Minutes</title>
        </head>
        <body>
            <h1>Calories Burned in 30 Minutes</h1>
            
            <table>
                <h4>Home & Daily Life Activities</h4>
                <tr>
                    <th>Activity</th>
                    <th>Calories (125 lbs)</th>
                    <th>Calories (155 lbs)</th>
                    <th>Calories (185 lbs)</th>
                </tr>
                <tr>
                    <td>Sleeping</td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
            </table>
        </body>
        </html>
        """
        # Mocking the response object
        mock_response = Mock()
        mock_response.content = fake_html_content.encode('utf-8')
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        scrape_calories_data("LiveLite/tests/data/calories_burned_30_minutes.csv")
        expected_data = []
        mock_csv_writer.return_value.writerows.assert_called_once_with(expected_data)

    @patch('LiveLite.data.scripts_to_generate.harvard_health_scraped_data.requests.get')
    def test_scrape_calories_connection_error(self, mock_get):
        """
        Edge case test: Test for connection error
        """
        mock_get.side_effect = requests.exceptions.RequestException
        with self.assertRaises(ConnectionError):
            scrape_calories_data("LiveLite/tests/data/calories_burned_30_minutes.csv")

    def test_scrape_calories_invalid_url(self):
        """
        Edge case test: Test for wrong url
        """
        with patch('requests.get') as mocked_get:
            mocked_get.side_effect = ValueError("Invalid URL")
            with self.assertRaises(ValueError):
                scrape_calories_data("LiveLite/tests/data/calories_burned_30_minutes.csv")

    def test_scrape_calories_unexpected_webpage_structure(self):
        """
        Edge case test: Test for unexpected web structure.
        """
        with patch('requests.get') as mocked_get:
            mocked_response = MagicMock()
            mocked_response.content = b"<html></html>"
            mocked_response.raise_for_status.side_effect=ValueError("Unexpected webpage structure")
            mocked_get.return_value = mocked_response
            with self.assertRaises(ValueError):
                scrape_calories_data("LiveLite/tests/data/calories_burned_30_minutes.csv")

if __name__ == '__main__':
    unittest.main()
