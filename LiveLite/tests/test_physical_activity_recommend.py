"""
This module contains unit tests for the physical_activity_recommend module.
Each test case evaluates different aspects of the function's behavior.

Classes:
- TestActivity

Dependencies:
- unittest module for unit testing framework
- calculate_calorie_burn from physical_activity_recommend
"""
import unittest
from LiveLite import calculate_calorie_burn # pylint: disable=import-error

class TestActivity(unittest.TestCase):
    """
    This class contains various test methods to verify the 
    correctness of the calculate_calorie_burn function.
    
    The TestActivity class is inheriting from unittest.TestCase
    
    Attributes:
    - None

    Methods:
    - test_activity_smoke()
    - test_activity_1()
    - test_activity_2()
    - test_activity_3()
    - test_activity_invalid_intentisy()
    - test_activity_invalid_activity()
    """

    def test_activity_smoke(self):
        """
        Smoke test to test if the function runs without errors.
        """
        file = "LiveLite/data/input_files/calories_burned_30_minutes.csv"
        calculate_calorie_burn(file,60,"high")

    def test_activity_1(self):
        """
        One shot test to test if the function correctly identifies obesity.
        """
        file = "LiveLite/data/input_files/calories_burned_30_minutes.csv"
        result = [('Gym Activities',
                    'Stretching, Hatha Yoga',
                    '30 min', '123 kcal')]
        test = calculate_calorie_burn(file,60,"low","yoga")
        self.assertEqual(result,test)

    def test_activity_2(self):
        """
        One shot test to test if the function correctly identifies obesity.
        """
        file = "LiveLite/data/input_files/calories_burned_30_minutes.csv"
        result = [('Gym Activities',
                   'Aerobics, Step: low impact',
                   '30 min',
                   '270 kcal'),
                   ('Home & Daily Life Activities',
                    'Playing w/kids: moderate effort', '30 min',
                    '150 kcal'),
                    ('Outdoor Activities',
                     'Gardening: general', '30 min',
                     '173 kcal'),
                     ('Training and Sports Activities',
                      'Ice Skating: general',
                      '30 min',
                      '270 kcal')]
        test = calculate_calorie_burn(file,75)
        self.assertEqual(result,test)

    def test_activity_3(self):
        """
        One shot test to test if the function correctly identifies obesity.
        """
        file = "LiveLite/data/input_files/calories_burned_30_minutes.csv"
        result = [('Gym Activities',
                   'Weight Lifting: general',
                   '30 min',
                   '142 kcal'),
                   ('Home & Daily Life Activities',
                    'Standing in line',
                    '30 min',
                    '45 kcal'),
                    ('Outdoor Activities',
                     'Raking lawn',
                     '30 min',
                     '189 kcal'),
                     ('Training and Sports Activities',
                      'Horseback Riding: general',
                      '30 min',
                      '92 kcal')]
        test = calculate_calorie_burn(file,92,"low")
        self.assertEqual(result,test)

    def test_activity_invalid_intentisy(self):
        """
        Edge case: Test if function raises ValueError for invalid intensity.
        """
        file = "LiveLite/data/input_files/calories_burned_30_minutes.csv"
        with self.assertRaises(ValueError):
            calculate_calorie_burn(file,92,"bleebluhblah")

    def test_activity_invalid_activity(self):
        """
        Edge case: Test if function raises ValueError for invalid activity.
        """
        file = "LiveLite/data/input_files/calories_burned_30_minutes.csv"
        with self.assertRaises(ValueError):
            calculate_calorie_burn(file,92,preferred_activity="bleebluhblah")

if __name__ == '__main__':
    unittest.main()
