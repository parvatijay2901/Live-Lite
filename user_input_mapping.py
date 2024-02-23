def user_input_mapping(user_data_dict):
    converted_data = {}

    def convert_age(age):
        if age >= 80:
            return 80
        else:
            return int(age)

    def convert_sex(sex):
        if sex.lower() == 'male':
            return 1
        elif sex.lower() == 'female':
            return 0
        else:
            raise ValueError("Invalid value for sex")


    def convert_ethnicity(ethnicity):
        ethnicity_map = {
            'mexican american': 1,
            'hispanic': 2,
            'non-hispanic white': 3,
            'non-hispanic black': 4,
            'non-hispanic asian': 6,
            'other non-hispanic races': 5,
            'non-hispanic multiracial': 7
        }
        ethnicity_lower = ethnicity.lower()
        if ethnicity_lower in ethnicity_map:
            return int(ethnicity_map[ethnicity_lower])
        else:
            raise ValueError("Invalid value for ethnicity")

    def convert_activity_level(activity_level):
        activity_map = {
            'sedentary': 1,
            'minimally active': 2,
            'moderately active': 3,
            'very active': 4,
            'extra active': 5
        }
        activity_lower = activity_level.lower()
        if activity_lower in activity_map:
            return int(activity_map[activity_lower])
        else:
            raise ValueError("Invalid value for activity level")

    def convert_dietary_preference(dietary_preference):
        dietary_map = {
            'vegan': 1,
            'vegeterian': 2,
            'non vegetarian': 3
        }
        dietary_lower = dietary_preference.lower()
        if dietary_lower in dietary_map:
            return int(dietary_map[dietary_lower])
        else:
            raise ValueError("Invalid value for dietary preference")

    def convert_sleep_hours(sleep_hours):
        if sleep_hours < 2:
            return 2
        elif sleep_hours > 14:
            return 14
        else:
            return int(sleep_hours)

    def convert_health_condition(health_condition):
        health_map = {
            'excellent': 1,
            'very good': 2,
            'good': 3,
            'fair': 4,
            'poor': 5
        }
        health_lower = health_condition.lower()
        if health_lower in health_map:
            return int(health_map[health_lower])
        else:
            raise ValueError("Invalid value for health condition")

    def convert_mental_health(mental_health):
        mental_map = {
            'not at all': 0,
            'several days': 1,
            'more than half the days': 2,
            'nearly every day': 3
        }
        mental_lower = mental_health.lower()
        if mental_lower in mental_map:
            return int(mental_map[mental_lower])
        else:
            raise ValueError("Invalid value for mental health")

    converted_data['internal_age'] = convert_age(user_data_dict['age'])
    converted_data['internal_sex'] = convert_sex(user_data_dict['sex'])
    converted_data['internal_height'] = float(user_data_dict['height']*2.54)
    converted_data['internal_weight'] = float(user_data_dict['weight']*0.45359237)
    converted_data['internal_ethnicity'] = convert_ethnicity(user_data_dict['ethnicity'])
    converted_data['internal_activity_level'] = convert_activity_level(user_data_dict['activity_level'])
    converted_data['internal_dietary_preference'] = convert_dietary_preference(user_data_dict['dietary_preference'])
    converted_data['internal_smoke_cig'] = int(user_data_dict['smoke_cig'].lower() == 'yes')
    converted_data['internal_mental_health'] = convert_mental_health(user_data_dict['mental_health'])
    converted_data['internal_sleep_hrs'] = convert_sleep_hours(float(user_data_dict['sleep_hrs']))
    converted_data['internal_health_condition'] = convert_health_condition(user_data_dict['health_condition'])
    converted_data['internal_diet_condition'] = convert_health_condition(user_data_dict['diet_condition'])
    converted_data['internal_Poor_apetitte_overeating'] = convert_mental_health(user_data_dict['Poor_apetitte_overeating'])

    return converted_data


# # Example usage
# data = {
#         'age': 25,
#         'sex': 'Male',
#         'height': 175.5,
#         'weight': 70.3,
#         'ethnicity': 'Hispanic',
#         'activity_level': 'Moderately Active',
#         'dietary_preference': 'Non Vegetarian',
#         'smoke_cig': 'No',
#         'mental_health': 'Several days',
#         'sleep_hrs': 7,
#         'health_condition': 'Good',
#         'diet_condition': 'Good',
#         'Poor_apetitte_overeating': 'Not at all'
#     }

# converted_data = user_input_mapping(data)
# print(converted_data)
