def generate_input_for_risk_score(mapped_user_inputs):
    
    # To be modified by parvati based on how Manasa generates mapped_user_inputs
    risk_predict_input = {
        'DPQ020': [mapped_user_inputs[8]], # internal_mental_health
        'DPQ050': [mapped_user_inputs[12]], # internal_poor_appetite_overeating
        'PAQ670': [mapped_user_inputs[5]], # internal_days moderate recreational activities - check this? - I think I have to modify
        'DBQ700': [mapped_user_inputs[11]], # internal_diet_condition
        'HUQ010': [mapped_user_inputs[10]], # internal_health_condition
        'RIAGENDR': [mapped_user_inputs[1]], # internal_sex
        'RIDAGEYR': [mapped_user_inputs[0]], # internal_age
        'RIDRETH3': [mapped_user_inputs[4]], # internal_ethnicity
        'SMQ040': [mapped_user_inputs[7]], # internal_smoke_cig
        'SLD012': [mapped_user_inputs[9]] # internal_sleep_hrs
        }
    return risk_predict_input

def generate_risk_score_display(risk_score):
    # To be modified by Parvati
    circle_html = f"""<div style="width: 250px; height: 250px; border-radius: 50%; background-color: #F18F2B; display: flex; justify-content: center; align-items: center; color: black; font-weight: bold;">{risk_score}%</div>"""
    return circle_html
