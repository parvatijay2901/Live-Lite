"""
This module contains unit tests for the LiveLite project that tests
various functionalities related to user inputs.

Classes:
- TestGetUserInputs: Contains test cases for the user inputs functionality
                    in LiveLite module.
"""
# pylint: disable=line-too-long
import unittest
import tempfile
import os
from unittest import mock
import LiveLite

class TestGetUserInputs(unittest.TestCase):
    """Test cases for the user inputs functionality."""

    def test_get_demographic_inputs(self):
        """Test getting demographic inputs"""
        user_inputs = {}
        with self.assertRaises(TypeError):
            LiveLite.get_demographic_inputs("not_a_dict")
        user_inputs = LiveLite.get_demographic_inputs(user_inputs)
        self.assertTrue('age' in user_inputs)
        self.assertTrue('sex' in user_inputs)
        self.assertTrue('height' in user_inputs)
        self.assertTrue('weight' in user_inputs)
        self.assertTrue('ethnicity' in user_inputs)

    def test_get_general_inputs(self):
        """Test getting general inputs"""
        user_inputs = {}
        with self.assertRaises(TypeError):
            LiveLite.get_general_inputs("not_a_dict")
        user_inputs = LiveLite.get_general_inputs(user_inputs)
        self.assertTrue('activity_level' in user_inputs)
        self.assertTrue('smoke_cig' in user_inputs)
        self.assertTrue('mental_health' in user_inputs)
        self.assertTrue('sleep_hrs' in user_inputs)
        self.assertTrue('health_condition' in user_inputs)
        self.assertTrue('diet_condition' in user_inputs)
        self.assertTrue('poor_appetite_overeating' in user_inputs)

    def test_write_user_inputs_to_csv(self):
        """Test writing user inputs to CSV"""
        user_inputs = {'age': 25, 'sex': 'Male'}
        with tempfile.TemporaryDirectory() as temp_dir:
            filename = os.path.join(temp_dir, 'temp.csv')
            LiveLite.write_user_inputs_to_csv(user_inputs, filename)
            self.assertTrue(os.path.exists(filename))
            with self.assertRaises(TypeError):
                LiveLite.write_user_inputs_to_csv("not_a_dict", filename)
            with self.assertRaises(TypeError):
                LiveLite.write_user_inputs_to_csv(user_inputs, 1234)
            with self.assertRaises(ValueError):
                LiveLite.write_user_inputs_to_csv(user_inputs, "")

            LiveLite.write_user_inputs_to_csv(user_inputs, filename)
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                self.assertEqual(len(lines), 3)

    @mock.patch('LiveLite.project_integration.handle_user_input.get_user_inputs.get_demographic_inputs')
    def test_get_user_inputs_demographic_not_dict(self, mock_get_demographic_inputs):
        """Test getting user inputs with non-dict demographic inputs"""
        mock_get_demographic_inputs.return_value = "not_a_dict"
        with self.assertRaises(TypeError):
            LiveLite.get_user_inputs()

    @mock.patch('LiveLite.project_integration.handle_user_input.get_user_inputs.get_general_inputs')
    def test_get_user_inputs_general_not_dict(self, mock_get_general_inputs):
        """Test getting user inputs with non-dict general inputs"""
        mock_get_general_inputs.return_value = "not_a_dict"
        with self.assertRaises(TypeError):
            LiveLite.get_user_inputs()

    def test_get_user_inputs_dict(self):
        """Test getting user inputs"""
        user_inputs = LiveLite.get_user_inputs()
        self.assertTrue(isinstance(user_inputs, dict))

if __name__ == '__main__':
    unittest.main()
