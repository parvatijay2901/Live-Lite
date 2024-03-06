import unittest
from LiveLite.recommendation_tool.risk_assessment.ml_build_train import build_and_evaluate_model

class TestMlModel(unittest.TestCase):
    
    def test_ml_model_smoke(self):
        build_and_evaluate_model('./LiveLite/tests/sample_ml_input.csv'
                                 ,'./LiveLite/tests/model_test_output.joblib')
        self.assertTrue(True)
    
    def test_ml_model_invalid_inputfile(self):
        with self.assertRaises(FileNotFoundError):
            build_and_evaluate_model('./blee/blublah'
                                     ,'./LiveLite/tests/model_test_output.joblib')
    
    def test_ml_model_invalid_modelfile(self):
        with self.assertRaises(FileNotFoundError):
            build_and_evaluate_model('./LiveLite/tests/sample_ml_input.csv'
                                     ,'./blee/bluh.blah')

if __name__ == '__main__':
    unittest.main()
