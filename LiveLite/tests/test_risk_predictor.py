"""
This module contains unit tests for the risk_predictor module.
Each test case evaluates different aspects of the function's behavior.

Classes:
- TestRiskPredict

Dependencies:
- unittest module for unit testing framework
- risk_predict from risk_predictor
"""
import unittest
from LiveLite import risk_predict # pylint: disable=import-error

class TestRiskPredict(unittest.TestCase):
    """
    This class contains various test methods to verify the 
    correctness of the risk_predict function.
    
    The TestIsObese class is inheriting from unittest.TestCase
    
    Attributes:
    - None

    Methods:
    - test_risk_predict_smoke()
    - test_risk_predict_1()
    - test_risk_predict_2()
    - test_risk_predict_3()
    - test_risk_predict_4()
    - test_risk_predict_invalid_type()
    - test_risk_predict_is_input_data_empty()
    - test_risk_predict_invalid_input_data()
    - test_risk_predict_is_model_path_valid()
    """
    def test_risk_predict_smoke(self):
        """
        Smoke test on original model to test if
        the function runs without any errors.
        """
        inputdict = {'DPQ020': [2],
                    'DPQ050': [2],
                    'PAQ670': [2], 
                    'DBQ700': [2], 
                    'HUQ010': [2],
                    'RIAGENDR': [0], 
                    'RIDAGEYR': [30], 
                    'RIDRETH3': [4],
                    'SMQ040': [0],
                    'SLD012': [5],}
        risk_predict(inputdict, 'LiveLite/recommendation_tool'
                                '/risk_assessment/trained_models'
                                '/obesity_risk_model.joblib')

    def test_risk_predict_1(self):
        """
        One shot test on the sample model with known prediction.
        """
        inputdict = {'DPQ020': [3],
                    'DPQ050': [3],
                    'PAQ670': [1], 
                    'DBQ700': [5], 
                    'HUQ010': [5],
                    'RIAGENDR': [1], 
                    'RIDAGEYR': [70],
                    'RIDRETH3': [1], 
                    'SMQ040': [1],
                    'SLD012': [2],}
        expect_result = (78.3, '#fda861')
        self.assertEqual(expect_result,
                         risk_predict(inputdict,
                                    'LiveLite/tests/data'
                                    '/sample_input_model.joblib'))

    def test_risk_predict_2(self):
        """
        One shot test on the sample model with known prediction
        and expected hex code for color.
        """
        inputdict = {'DPQ020': [2],
                    'DPQ050': [2],
                    'PAQ670': [2], 
                    'DBQ700': [2], 
                    'HUQ010': [2],
                    'RIAGENDR': [1],
                    'RIDAGEYR': [30],
                    'RIDRETH3': [4], 
                    'SMQ040': [0],
                    'SLD012': [5],}
        expect_result = (52.6, "#fbf362")
        self.assertEqual(expect_result,
                         risk_predict(inputdict,
                                      'LiveLite/tests/data'
                                      '/sample_input_model.joblib'))

    def test_risk_predict_3(self):
        """
        One shot test on the sample model with known prediction
        and expected hex code for color.
        """
        inputdict = {'DPQ020': [1],
                    'DPQ050': [2],
                    'PAQ670': [5], 
                    'DBQ700': [2], 
                    'HUQ010': [1],
                    'RIAGENDR': [1],
                    'RIDAGEYR': [32],
                    'RIDRETH3': [2], 
                    'SMQ040': [1],
                    'SLD012': [8],}
        expect_result = (36.4, "#d7f268")
        self.assertEqual(expect_result,
                         risk_predict(inputdict,
                                      'LiveLite/tests/data'
                                      '/sample_input_model.joblib'))

    def test_risk_predict_4(self):
        """
        One shot test on the sample model with known prediction
        and expected hex code for color.
        """
        inputdict = {'DPQ020': [0],
                    'DPQ050': [0],
                    'PAQ670': [5], 
                    'DBQ700': [2], 
                    'HUQ010': [2],
                    'RIAGENDR': [0], 
                    'RIDAGEYR': [20],
                    'RIDRETH3': [4],
                    'SMQ040': [0],
                    'SLD012': [10],}
        expect_result = (20.9, "#aee96e")
        self.assertEqual(expect_result,
                         risk_predict(inputdict,
                                      'LiveLite/tests/data'
                                      '/sample_input_model.joblib'))

    def test_risk_predict_invalid_type(self):
        """
        Edge case test: Test for invalid input data type.
        """
        inputdict = {'DPQ020': [1.8],
                    'DPQ050': [1],
                    'PAQ670': [5.34], 
                    'DBQ700': [3], 
                    'HUQ010': [4.6],
                    'RIAGENDR': [1], 
                    'RIDAGEYR': [70],
                    'RIDRETH3': [2],
                    'SMQ040': [1],
                    'SLD012': [2],}
        with self.assertRaises(TypeError):
            risk_predict(inputdict, 'LiveLite/recommendation_tool'
                                    '/risk_assessment/trained_models'
                                    '/obesity_risk_model.joblib')

    def test_risk_predict_is_input_data_empty(self):
        """
        Edge case test on original model.
        """
        inputdict = {}
        with self.assertRaises(ValueError):
            risk_predict(inputdict, 'LiveLite/recommendation_tool'
                                    '/risk_assessment/trained_models'
                                    '/obesity_risk_model.joblib')

    def test_risk_predict_invalid_input_data(self):
        """
        Edge case test on the original model.
        """
        inputdict = {'DPQ020': [1.8],
                    'DPQ050': [1],
                    'PAQ670': [5.34], 
                    'DBQ700': [3], 
                    'HUQ010': [4.6],
                    'RIAGENDR': [1], 
                    'RIDAGEYR': [70],
                    'RIDRETH3': [2],
                    'SMQ040': [1],
                    'SLD012': [2],}
        with self.assertRaises(TypeError):
            risk_predict(inputdict, 'LiveLite/recommendation_tool'
                                    '/risk_assessment/trained_models'
                                    '/obesity_risk_model.joblib')

    def test_risk_predict_is_model_path_valid(self):
        """
        Edge case test: When model file path is invalid.
        """
        inputdict = {'DPQ020': [1],
                    'DPQ050': [1],
                    'PAQ670': [5], 
                    'DBQ700': [3], 
                    'HUQ010': [4],
                    'RIAGENDR': [1], 
                    'RIDAGEYR': [70],
                    'RIDRETH3': [2],
                    'SMQ040': [1],
                    'SLD012': [2],}
        with self.assertRaises(FileNotFoundError):
            risk_predict(inputdict, '/blee/bluu.blah')

if __name__ == '__main__':
    unittest.main()
