import unittest
from project_integration.handle_user_input.user_input_mapping import user_input_mapping
class TestUserInputMapping(unittest.TestCase):
    # Smoke test
    def test_user_input_map_smoke(self):
        data = {"age": 85,
                "sex": "Female",
                "height": 60.96,
                "weight": 9.072,
                "ethnicity": "Non-hispanic Multiracial",
                "activity_level": "Extra Active",
                "dietary_preference": "Vegan",
                "smoke_cig": "Yes",
                "mental_health": "Not at all",
                "sleep_hrs": 14.0,
                "health_condition": "Excellent",
                "diet_condition": "Excellent",
                "Poor_apetitte_overeating": "Not at all"}
        user_input_mapping(data)
        self.assertTrue(True)
    
    def test_user_input_map_1(self):   
        data = {"age": 18,
                "sex": "Male",
                "height": 60.96,
                "weight": 9.072,
                "ethnicity": "Hispanic",
                "activity_level": "Sedentary",
                "dietary_preference": "Vegan",
                "smoke_cig": "Yes",
                "mental_health": "Not at all",
                "sleep_hrs": 2.0,
                "health_condition": "Excellent",
                "diet_condition": "Excellent",
                "Poor_apetitte_overeating": "Not at all"}
        res = {'internal_age': 18,
               'internal_sex': 1,
               'internal_height': 154.8384,
               'internal_weight': 4.11498998064,
               'internal_ethnicity': 2,
               'internal_activity_level': 1,
               'internal_dietary_preference': 1,
               'internal_smoke_cig': 1,
               'internal_mental_health': 0,
               'internal_sleep_hrs': 2,
               'internal_health_condition': 1,
               'internal_diet_condition': 1,
               'internal_Poor_apetitte_overeating': 0}
        self.assertEqual(res, user_input_mapping(data))
    def test_user_input_map_2(self):   
        data = {"age": 37,
                "sex": "Male",
                "height": 60.96,
                "weight": 9.072,
                "ethnicity": "Mexican American",
                "activity_level": "Minimally Active",
                "dietary_preference": "Vegetarian",
                "smoke_cig": "No",
                "mental_health": "Several Days",
                "sleep_hrs": 1.0,
                "health_condition": "Very Good",
                "diet_condition": "Good",
                "Poor_apetitte_overeating": "more than half the days"}
        res = {'internal_age': 37,
               'internal_sex': 1,
               'internal_height': 154.8384,
               'internal_weight': 4.11498998064,
               'internal_ethnicity': 1,
               'internal_activity_level': 2,
               'internal_dietary_preference': 2,
               'internal_smoke_cig': 0,
               'internal_mental_health': 1,
               'internal_sleep_hrs': 2,
               'internal_health_condition': 2,
               'internal_diet_condition': 3,
               'internal_Poor_apetitte_overeating': 2}
        self.assertEqual(res, user_input_mapping(data))
    
    def test_user_input_map_3(self):   
        data = {"age": 37,
                "sex": "Male",
                "height": 100,
                "weight": 100,
                "ethnicity": "Non-Hispanic White",
                "activity_level": "Moderately Active",
                "dietary_preference": "Non Vegetarian",
                "smoke_cig": "No",
                "mental_health": "Several Days",
                "sleep_hrs": 1.0,
                "health_condition": "Fair",
                "diet_condition": "Poor",
                "Poor_apetitte_overeating": "nearly every day"}
        res = {'internal_age': 37,
               'internal_sex': 1,
               'internal_height': 254.0,
               'internal_weight': 45.359237,
               'internal_ethnicity': 3,
               'internal_activity_level': 3,
               'internal_dietary_preference': 3,
               'internal_smoke_cig': 0,
               'internal_mental_health': 1,
               'internal_sleep_hrs': 2,
               'internal_health_condition': 4,
               'internal_diet_condition': 5,
               'internal_Poor_apetitte_overeating': 3}
        self.assertEqual(res, user_input_mapping(data))
    
    def test_user_input_invalid_gender(self):   
        data = {"age": 37,
                "sex": "bleeblublah",
                "height": 100,
                "weight": 100,
                "ethnicity": "Non-Hispanic White",
                "activity_level": "Moderately Active",
                "dietary_preference": "Non Vegetarian",
                "smoke_cig": "No",
                "mental_health": "Several Days",
                "sleep_hrs": 1.0,
                "health_condition": "Fair",
                "diet_condition": "Poor",
                "Poor_apetitte_overeating": "nearly every day"}
        with self.assertRaises(ValueError):
            user_input_mapping(data)
    
    def test_user_input_invalid_ethnicity(self):   
        data = {"age": 37,
                "sex": "Male",
                "height": 100,
                "weight": 100,
                "ethnicity": "Female",
                "activity_level": "Moderately Active",
                "dietary_preference": "Non Vegetarian",
                "smoke_cig": "No",
                "mental_health": "Several Days",
                "sleep_hrs": 1.0,
                "health_condition": "Fair",
                "diet_condition": "Poor",
                "Poor_apetitte_overeating": "nearly every day"}
        with self.assertRaises(ValueError):
            user_input_mapping(data)
    
    def test_user_input_invalid_activity(self):   
        data = {"age": 37,
                "sex": "Male",
                "height": 100,
                "weight": 100,
                "ethnicity": "Hispanic",
                "activity_level": "Gym",
                "dietary_preference": "Non Vegetarian",
                "smoke_cig": "No",
                "mental_health": "Several Days",
                "sleep_hrs": 1.0,
                "health_condition": "Fair",
                "diet_condition": "Poor",
                "Poor_apetitte_overeating": "nearly every day"}
        with self.assertRaises(ValueError):
            user_input_mapping(data)
    
    def test_user_input_invalid_dietary_pref(self):   
        data = {"age": 37,
                "sex": "Male",
                "height": 100,
                "weight": 100,
                "ethnicity": "Hispanic",
                "activity_level": "Sedentary",
                "dietary_preference": "Biriyani",
                "smoke_cig": "No",
                "mental_health": "Several Days",
                "sleep_hrs": 1.0,
                "health_condition": "Fair",
                "diet_condition": "Poor",
                "Poor_apetitte_overeating": "nearly every day"}
        with self.assertRaises(ValueError):
            user_input_mapping(data)
if __name__ == '__main__':
    unittest.main()