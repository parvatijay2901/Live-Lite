import unittest
import numpy as np
<<<<<<< HEAD:tests/ml and actvity/test_is_obese.py
from LiveLite.recommendation_tool.risk_assessment.is_obese import is_obese
=======
from recommendation_tool.risk_assessment.is_obese import is_obese
>>>>>>> c1ce701f8935890f08f262fb76dcd553454784fb:LiveLite/tests/test_is_obese.py

class TestIsObese(unittest.TestCase):

    # Smoke test
    def test_is_obese_smoke(self):
        is_obese(150, 80)
        self.assertTrue(True)
    
    def test_is_obese_1(self):
        self.assertEqual(True,is_obese(150,90))
    
    def test_is_obese_2(self):
        self.assertEqual(False,is_obese(160,40))

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            is_obese(0,90)
    
    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            is_obese(160,"w")

if __name__ == '__main__':
    unittest.main()