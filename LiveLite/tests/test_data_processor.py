"""
This module contains unit tests for the data_processor module.
Each test case evaluates different aspects of the function's behavior.
This module uses sample test data for unit test.

Classes:
- TestDataProcess

Dependencies:
- unittest module for unit testing framework
- data_process from data_processor
- Pandas dataframe module
"""
import os
import unittest
import pandas as pd
from LiveLite import data_process # pylint: disable=import-error

class TestDataProcess(unittest.TestCase):
    """
    This class contains various test methods to verify the 
    correctness of the data_processor module.
    
    The TestDataProcess class is inheriting from unittest.TestCase
    
    Attributes:
    - None

    Methods:
    - def test_data_process_smoke(self):
    - test_data_process_1()
    - test_data_process_2()
    - test_data_process_3()
    - test_data_process_4()
    - test_data_process_invalid_columns()
    """

    def test_data_process_smoke(self):
        """
        Smoke test to test if the function runs without errors.
        """
        input_file = "./LiveLite/tests/data/sample_nhanes.csv"
        output_file = "./LiveLite/tests/data/process_nhanes.csv"
        data_process(input_file, output_file)

    def test_data_process_1(self):
        """
        One shot test check if output file is created as expected.
        Compare the records in both input & output files.
        
        Check if the output file has 15 columns.
        """
        input_file = "./LiveLite/tests/data/sample_nhanes.csv"
        output_file = "./LiveLite/tests/data/process_nhanes.csv"
        data_process(input_file, output_file)
        self.assertTrue(os.path.exists(output_file))

    def test_data_process_2(self):
        """
        One shot test check if the number of records are same
        in both input & output files.
        """
        input_file = "./LiveLite/tests/data/sample_nhanes.csv"
        output_file = "./LiveLite/tests/data/process_nhanes.csv"
        data_process(input_file, output_file)
        df_input = pd.read_csv(input_file)
        df_output = pd.read_csv(output_file)
        self.assertEqual(len(df_input), len(df_output))

    def test_data_process_3(self):
        """
        One shot test check if the output file has the 'is_obese' column.
        """
        input_file = "./LiveLite/tests/data/sample_nhanes.csv"
        output_file = "./LiveLite/tests/data/process_nhanes.csv"
        data_process(input_file, output_file)
        df_output = pd.read_csv(output_file)
        self.assertIn('IsObese', df_output.columns)

    def test_data_process_4(self):
        """
        One shot test check if the output file has 15 columns.
        """
        input_file = "./LiveLite/tests/data/sample_nhanes.csv"
        output_file = "./LiveLite/tests/data/process_nhanes.csv"
        data_process(input_file, output_file)
        df_output = pd.read_csv(output_file)
        self.assertEqual(len(df_output.columns), 15)

    def test_data_process_invalid_columns(self):
        """
        Edge case: testing for invalid columns.
        """
        input_file = "./LiveLite/tests/data/sample_nhanes_invalid_col.csv"
        output_file = "./LiveLite/tests/data/process_nhanes.csv"
        with self.assertRaises(Exception):
            data_process(input_file, output_file)

if __name__ == '__main__':
    unittest.main()
