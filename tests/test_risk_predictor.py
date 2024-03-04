import unittest
import numpy as np
from risk_predictor import risk_predict

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
        risk_predict(inputdict, 'obesity_risk_model.joblib')
        self.assertTrue(True)
    
    def test_risk_Predict_1(self):
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
        expect_result = (32.2, "Green")
        self.assertEqual(expect_result,risk_predict(inputdict, 'obesity_risk_model.joblib'))
    
    def test_risk_Predict_2(self):
        inputdict = {'DPQ020': [0], 
                    'DPQ050': [0], 
                    'PAQ670': [0], 
                    'DBQ700': [0], 
                    'HUQ010': [0],
                    'RIAGENDR': [0] , 
                    'RIDAGEYR': [30], 
                    'RIDRETH3': [4], 
                    'SMQ040': [0],
                    'SLD012': [9],}
        expect_result = (20.0, "Blue")
        self.assertEqual(expect_result,risk_predict(inputdict, 'obesity_risk_model.joblib'))

    def test_risk_Predict_3(self):
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
        expect_result = (58.9, "Yellow")
        self.assertEqual(expect_result,risk_predict(inputdict, 'obesity_risk_model.joblib'))
    
    def test_risk_Predict_4(self):
        inputdict = {'DPQ020': [2], 
                    'DPQ050': [1], 
                    'PAQ670': [1], 
                    'DBQ700': [4], 
                    'HUQ010': [4],
                    'RIAGENDR': [0] , 
                    'RIDAGEYR': [80], 
                    'RIDRETH3': [1], 
                    'SMQ040': [1],
                    'SLD012': [2],}
        expect_result = (76.2, "Red")
        self.assertEqual(expect_result,risk_predict(inputdict, 'obesity_risk_model.joblib'))
    
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
            risk_predict(inputdict, 'obesity_risk_model.joblib')
    
    def test_risk_predict_is_input_empty(self):
        inputdict = {}
        with self.assertRaises(ValueError):
            risk_predict(inputdict, 'obesity_risk_model.joblib')
    
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
            risk_predict(inputdict, 'obesity_risk_model.joblib')
    
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
            risk_predict(inputdict, '/mode/model.joblib')

if __name__ == '__main__':
    unittest.main()