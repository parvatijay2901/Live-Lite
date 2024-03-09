import unittest
from unittest.mock import patch, MagicMock, Mock
import requests
from bs4 import BeautifulSoup
from LiveLite import scrape_calories_data # pylint: disable=import-error

class TestScrapeCaloriesData(unittest.TestCase):

    def test_scrape_calories_smoke(self):
        with patch('requests.get') as mocked_get:
            mocked_response = MagicMock()
            mocked_response.content = b"Mocked HTML content"
            mocked_response.ok = True
            mocked_get.return_value = mocked_response
            scrape_calories_data()
    
    @patch('LiveLite.data.scripts_to_generate.harvard_health_scraped_data.requests.get')
    @patch('LiveLite.data.scripts_to_generate.harvard_health_scraped_data.csv.writer')
    def test_scrape_calories_data_1(self, mock_csv_writer, mock_get):
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

        # Assigning the mock response to the mock get function
        mock_get.return_value = mock_response

        # Calling the function under test
        scrape_calories_data()

        expected_data = ('Outdoor', 'Running', 260, 372, 444, 2.2933333333333334, 5.05593867028813)
        mock_csv_writer.return_value.writerows.assert_called_once_with(expected_data)   


    @patch('LiveLite.data.scripts_to_generate.harvard_health_scraped_data.requests.get')
    @patch('LiveLite.data.scripts_to_generate.harvard_health_scraped_data.csv.writer')
    def test_scrape_calories_data_2(self, mock_csv_writer, mock_get):
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

        # Assigning the mock response to the mock get function
        mock_get.return_value = mock_response

        # Calling the function under test
        scrape_calories_data()

        expected_data = [('Home & Daily Life Activities', 'Sleeping', 0, 0, 0, 0, 0)]
        mock_csv_writer.return_value.writerows.assert_called_once_with(expected_data)   



    @patch('LiveLite.data.scripts_to_generate.harvard_health_scraped_data.requests.get')
    def test_scrape_calories_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException
        with self.assertRaises(ConnectionError):
            scrape_calories_data()

    def test_scrape_calories_invalid_url(self):
        with patch('requests.get') as mocked_get:
            mocked_get.side_effect = ValueError("Invalid URL")
            with self.assertRaises(ValueError):
                scrape_calories_data()

    def test_scrape_calories_unexpected_webpage_structure(self):
        with patch('requests.get') as mocked_get:
            mocked_response = MagicMock()
            mocked_response.content = b"<html></html>"
            mocked_response.raise_for_status.side_effect = ValueError("Unexpected webpage structure")
            mocked_get.return_value = mocked_response
            with self.assertRaises(ValueError):
                scrape_calories_data()

if __name__ == '__main__':
    unittest.main()
