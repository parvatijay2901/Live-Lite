import unittest
import numpy as np
from recommendation_tool.risk_assessment.risk_predictor import risk_predict

class TestRiskPredict(unittest.TestCase):

    # Smoke test
    def test_risk_Predict_smoke(self):
        inputdict = {'DPQ020': [2], 
                    'DPQ050': [2], 
                    'PAQ670': [2], 
                    'DBQ700': [2], 
                    'HUQ010': [2],
                    'RIAGENDR': [0] , 
                    'RIDAGEYR': [30], 
                    'RIDRETH3': [4], 
                    'SMQ040': [0],
                    'SLD012': [5],}
        risk_predict(inputdict, 'recommendation_tool/risk_assessment/trained_models/obesity_risk_model.joblib')
        self.assertTrue(True)
    
    def test_risk_Predict_1(self):
        inputdict = {'DPQ020': [3], 
                    'DPQ050': [3], 
                    'PAQ670': [1], 
                    'DBQ700': [5], 
                    'HUQ010': [5],
                    'RIAGENDR': [1] , 
                    'RIDAGEYR': [70], 
                    'RIDRETH3': [1], 
                    'SMQ040': [1],
                    'SLD012': [2],}
        expect_result = (78.3, '#ffa07a')
        self.assertEqual(expect_result,risk_predict(inputdict, './tests/sample_input_model.joblib'))
    
    def test_risk_Predict_2(self):
        inputdict = {'DPQ020': [2], 
                    'DPQ050': [2], 
                    'PAQ670': [2], 
                    'DBQ700': [2], 
                    'HUQ010': [2],
                    'RIAGENDR': [1] , 
                    'RIDAGEYR': [30], 
                    'RIDRETH3': [4], 
                    'SMQ040': [0],
                    'SLD012': [5],}
        expect_result = (52.6, "#ffff99")
        self.assertEqual(expect_result,risk_predict(inputdict, './tests/sample_input_model.joblib'))

    def test_risk_Predict_3(self):
        inputdict = {'DPQ020': [1], 
                    'DPQ050': [2], 
                    'PAQ670': [5], 
                    'DBQ700': [2], 
                    'HUQ010': [1],
                    'RIAGENDR': [1] , 
                    'RIDAGEYR': [32], 
                    'RIDRETH3': [2], 
                    'SMQ040': [1],
                    'SLD012': [8],}
        expect_result = (36.4, "#66915c")
        self.assertEqual(expect_result,risk_predict(inputdict, './tests/sample_input_model.joblib'))
    
    def test_risk_Predict_4(self):
        inputdict = {'DPQ020': [0], 
                    'DPQ050': [0], 
                    'PAQ670': [5], 
                    'DBQ700': [2], 
                    'HUQ010': [2],
                    'RIAGENDR': [0] , 
                    'RIDAGEYR': [20], 
                    'RIDRETH3': [4], 
                    'SMQ040': [0],
                    'SLD012': [10],}
        expect_result = (20.9, "#add8e6")
        self.assertEqual(expect_result,risk_predict(inputdict, './tests/sample_input_model.joblib'))
    
    def test_risk_predict_invalid_type(self):
        inputdict = {'DPQ020': [1.8], 
                    'DPQ050': [1], 
                    'PAQ670': [5.34], 
                    'DBQ700': [3], 
                    'HUQ010': [4.6],
                    'RIAGENDR': [1] , 
                    'RIDAGEYR': [70], 
                    'RIDRETH3': [2], 
                    'SMQ040': [1],
                    'SLD012': [2],}
        with self.assertRaises(TypeError):
            risk_predict(inputdict, 'recommendation_tool/risk_assessment/trained_models/obesity_risk_model.joblib')
    
    def test_risk_predict_is_input_empty(self):
        inputdict = {}
        with self.assertRaises(ValueError):
            risk_predict(inputdict, 'recommendation_tool/risk_assessment/trained_models/obesity_risk_model.joblib')
    
    def test_risk_predict_invalid_data(self):
        inputdict = {'DPQ020': [1.8], 
                    'DPQ050': [1], 
                    'PAQ670': [5.34], 
                    'DBQ700': [3], 
                    'HUQ010': [4.6],
                    'RIAGENDR': [1] , 
                    'RIDAGEYR': [70], 
                    'RIDRETH3': [2], 
                    'SMQ040': [1],
                    'SLD012': [2],}
        with self.assertRaises(TypeError):
            risk_predict(inputdict, 'recommendation_tool/risk_assessment/trained_models/obesity_risk_model.joblib')
    
    def test_risk_predict_is_model_path_valid(self):
        inputdict = {'DPQ020': [1], 
                    'DPQ050': [1], 
                    'PAQ670': [5], 
                    'DBQ700': [3], 
                    'HUQ010': [4],
                    'RIAGENDR': [1] , 
                    'RIDAGEYR': [70], 
                    'RIDRETH3': [2], 
                    'SMQ040': [1],
                    'SLD012': [2],}
        with self.assertRaises(FileNotFoundError):
            risk_predict(inputdict, '/blee/bluu.blah')

if __name__ == '__main__':
    unittest.main()