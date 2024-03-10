"""
This module contains unit tests for the ml_build_train module.
Each test case evaluates different aspects of the function's behavior.

Classes:
- TestMlModel

Dependencies:
- unittest module for unit testing framework
- build_and_evaluate_model from ml_build_train
- save_model from ml_build_train
- find_most_influential_factors from ml_build_train
- Pipeline, Logisticregression from sklearn
- Patch from unittest.
"""
import os
import unittest
from unittest.mock import patch
import joblib
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
# pylint: disable=import-error
from LiveLite import build_and_evaluate_model, save_model, find_most_influential_factors

class TestMlModel(unittest.TestCase):
    """
    This class contains various test methods to verify the 
    correctness of the all 3 function.
    build_and_evaluate_model, save_model, find_most_influential_factors
    
    The TestMlModel class is inheriting from unittest.TestCase
    
    Attributes:
    - None

    Methods:
    - test_ml_model_smoke()
    - test_ml_model_1
    - test_ml_model_invalid_inputfile()
    - test_ml_model_invalid_modelfile()
    - test_invalid_parameter_search()
    - test_save_model_exception()
    """
    def test_ml_model_smoke(self):
        """
        Smoke test to test if the function runs without errors.
        """
        build_and_evaluate_model('LiveLite/tests/data/sample_ml_input.csv'
                                 ,'LiveLite/tests/data/model_test_output.joblib')

    def test_ml_model_1(self):
        """
        One Shot test to test attributes of built model.
        Test for:
            - If the model is bulit and saved.
            - If the model is Logistic Regression model
            - If the model has predict attribute.
        """
        build_and_evaluate_model('LiveLite/tests/data/sample_ml_input.csv'
                                 ,'LiveLite/tests/data/model_test_output.joblib')
        assert os.path.exists('LiveLite/tests/data/model_test_output.joblib')

        expected_steps = ['preprocessor', 'classifier']

        loaded_model = joblib.load('LiveLite/tests/data/model_test_output.joblib')
        loaded_steps = [step[0] for step in loaded_model.steps]

        assert isinstance(loaded_model, Pipeline)
        assert hasattr(loaded_model, "predict")
        assert loaded_steps == expected_steps
        assert isinstance(loaded_model.named_steps['classifier'], LogisticRegression)

    def test_ml_model_invalid_inputfile(self):
        """
        Edge Test: Test if the function throws error with wrong filepath.
        """
        with self.assertRaises(FileNotFoundError):
            build_and_evaluate_model('LiveLite/blee/blublah'
                                     ,'LiveLite/tests/data/model_test_output.joblib')

    def test_ml_model_invalid_modelfile(self):
        """
        Edge Test: Test if the function throws error with output filepath.
        """
        with self.assertRaises(FileNotFoundError):
            build_and_evaluate_model('LiveLite/tests/data/sample_ml_input.csv'
                                     ,'LiveLite/blee/bluh.blah')

    def test_invalid_parameter_search(self):
        """
        Edge Test: Test if the function throws error with wrong parameters
        """
        cat_feat =['PIZZA',
                    'PASTA',
                    'CHOCO',
                    'PANINI',
                    'SWISS',
                    'PARIS',
                    'HAHAHA',
                    'HEHEHE']
        num_feat = ['SLD012',
                    'DONE']
        with self.assertRaises(Exception):
            find_most_influential_factors('LiveLite/tests/data/sample_input_model.joblib'
                                            ,num_feat, cat_feat)

    @patch('joblib.dump')
    def test_save_model_exception(self, mock_dump):
        """
        Edge Test: Mock test to mock eception while saving the joblib file.
        """
        mock_dump.side_effect = Exception("Mocked exception")
        with self.assertRaises(Exception) as context:
            save_model("model", "filepath")
        self.assertEqual(str(context.exception),
                        "Error occurred while saving the model: Mocked exception")

if __name__ == '__main__':
    unittest.main()
