"""
This module contains unit tests for the data_processor module.
Each test case evaluates different aspects of the function's behavior.

Classes:
- TestDataProcess

Dependencies:
- unittest module for unit testing framework
- data_process from data_processor
"""

import unittest
from LiveLite import data_process # pylint: disable=import-error

class TestDataProcess(unittest.TestCase):
    """
    This class contains various test methods to verify the 
    correctness of the is_obese function.
    
    The TestIsObese class is inheriting from unittest.TestCase
    
    Attributes:
    - None

    Methods:
    - test_is_obese_smoke()
    - test_is_obese_1()
    - test_is_obese_2()
    - test_invalid_height()
    - test_invalid_weight()
    """

    def test_data_process_smoke(self):
        """
        Smoke test to test if the function runs without errors.
        """
        data_process("./LiveLite/tests/sample_nhanes.csv", "./LiveLite/tests/process_nhanes.csv")
    
    


if __name__ == '__main__':
    unittest.main()
