"""
This module contains unit tests for the is_obese module.
Each test case evaluates different aspects of the function's behavior.

Classes:
- TestIsObese

Dependencies:
- unittest module for unit testing framework
- is_obese from is_obese
"""

import unittest
from LiveLite import is_obese # pylint: disable=import-error

class TestIsObese(unittest.TestCase):
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

    def test_is_obese_smoke(self):
        """
        Smoke test to test if the function runs without errors.
        """
        is_obese(150, 80)

    def test_is_obese_1(self):
        """
        One shot test to test if the function correctly identifies obesity.
        """
        self.assertEqual(True, is_obese(150, 90))

    def test_is_obese_2(self):
        """
        One shot test to test if the function correctly identifies obesity.
        """
        self.assertEqual(False, is_obese(160, 40))

    def test_invalid_height(self):
        """
        Edge Case: Test if the function raises ValueError for invalid height.
        """
        with self.assertRaises(ValueError):
            is_obese(0, 90)

    def test_invalid_weight(self):
        """
        Edge case: Test if the function raises ValueError for invalid weight.
        """
        with self.assertRaises(ValueError):
            is_obese(160, "w")

if __name__ == '__main__':
    unittest.main()
