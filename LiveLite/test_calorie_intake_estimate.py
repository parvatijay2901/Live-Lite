import unittest
import numpy as np
from calorie_intake_estimate import calculate_calorie_intake

class TestKnn(unittest.TestCase):

    # Smoke test
    def test_calorie_intake_smoke(self):
        calculate_calorie_intake(50, 170, 20, 1, 2)
        self.assertTrue(True)
    
    def test_calorie_intake_1(self):
        self.assertAlmostEqual(2504.04,
                               calculate_calorie_intake(50.6, 153.2, 30, 0, 4)
                               ,2)

    def test_calorie_intake_2(self):
        self.assertAlmostEqual(3488.10,
                               calculate_calorie_intake(70, 170, 24, 1, 2)
                               ,2)

    def test_invalid_gender(self):
        with self.assertRaises(ValueError):
            calculate_calorie_intake(50, 170, 20, 4, 2)
    
    def test_invalid_activity_level(self):
        with self.assertRaises(ValueError):
            calculate_calorie_intake(50, 170, 20, 0, -8)
    
    def test_invalid_weight_type(self):
        with self.assertRaises(TypeError):
            calculate_calorie_intake("w", 170, 20, 0, 3)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            calculate_calorie_intake(60, -85, 20, 0, 3)
    
    def test_invalid_age_type(self):
        with self.assertRaises(TypeError):
            calculate_calorie_intake(55.6, 170, 20.57, 0, 3)


if __name__ == '__main__':
    unittest.main()