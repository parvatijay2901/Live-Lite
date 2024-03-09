import unittest
from LiveLite import build_and_evaluate_model # pylint: disable=import-error

class TestMlModel(unittest.TestCase):
    
    def test_ml_model_smoke(self):
        build_and_evaluate_model('LiveLite/tests/sample_ml_input.csv'
                                 ,'LiveLite/tests/model_test_output.joblib')
        self.assertTrue(True)
    
    def test_ml_model_invalid_inputfile(self):
        with self.assertRaises(FileNotFoundError):
            build_and_evaluate_model('LiveLite/blee/blublah'
                                     ,'LiveLite/tests/model_test_output.joblib')
    
    def test_ml_model_invalid_modelfile(self):
        with self.assertRaises(FileNotFoundError):
            build_and_evaluate_model('LiveLite/tests/sample_ml_input.csv'
                                     ,'LiveLite/blee/bluh.blah')

if __name__ == '__main__':
    unittest.main()
