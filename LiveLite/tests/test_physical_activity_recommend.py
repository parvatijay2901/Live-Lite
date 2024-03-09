import unittest
import numpy as np
from LiveLite import calculate_calorie_burn # pylint: disable=import-error

class TestActivity(unittest.TestCase):

    # Smoke test
    def test_activity_smoke(self):
        file = "LiveLite/data/input_files/calories_burned_30_minutes.csv"
        calculate_calorie_burn(file,60,"high")
        self.assertTrue(True)

    def test_activity_1(self):
        file = "LiveLite/data/input_files/calories_burned_30_minutes.csv"
        result = [('Gym Activities',
                    'Stretching, Hatha Yoga',
                    '30 min', '123 kcal')]
        test = calculate_calorie_burn(file,60,"low","yoga")
        self.assertEqual(result,test)
    
    def test_activity_2(self):
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
        file = "LiveLite/data/input_files/calories_burned_30_minutes.csv"
        with self.assertRaises(ValueError):
            calculate_calorie_burn(file,92,"bleebluhblah")
    
    def test_activity_invalid_activity(self):
        file = "LiveLite/data/input_files/calories_burned_30_minutes.csv"
        with self.assertRaises(ValueError):
            calculate_calorie_burn(file,92,preferred_activity="bleebluhblah")

if __name__ == '__main__':
    unittest.main()