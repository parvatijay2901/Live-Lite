from LiveLite.data.scripts_to_generate.harvard_health_scraped_data import scrape_calories_data
from LiveLite.data.scripts_to_generate.data_processor import data_process

from LiveLite.project_integration.common_functions import add_blank_lines, swap_pages_back, check_session_state_variable
from LiveLite.project_integration.handle_user_input.get_user_inputs import get_user_inputs, get_demographic_inputs, get_general_inputs, write_user_inputs_to_csv
from LiveLite.project_integration.handle_user_input.get_user_inputs import write_user_inputs_to_csv
from LiveLite.project_integration.handle_user_input.user_input_mapping import user_input_mapping
from LiveLite.project_integration.handle_user_input.generate_risk_score_display import get_input_for_risk_score, display_risk_score, display_risk_suggestion
from LiveLite.project_integration.recommendation_controller.controller import controller

from LiveLite.research.research_display_info.background import display_background
from LiveLite.research.research_display_info.health_consequences import display_health_consequences
from LiveLite.research.research_display_info.prevention_and_management import display_prevention_and_management
from LiveLite.research.research_display_info.sources import display_sources
from LiveLite.research.visualizations.ihme_data_analysis import plot_ihme_data
from LiveLite.research.visualizations.nhanes_obesity_overweight_analysis import plot_obesity_overweight_trends
from LiveLite.research.visualizations.obesity_trends_analysis import plot_obesity_trends
from LiveLite.research.visualizations.compare_trends_over_time import generate_violin_plot

from LiveLite.recommendation_tool.risk_assessment.risk_predictor import risk_predict
from LiveLite.recommendation_tool.risk_assessment.is_obese import is_obese
from LiveLite.recommendation_tool.risk_assessment.ml_build_train import build_and_evaluate_model, save_model, find_most_influential_factors
from LiveLite.recommendation_tool.nutrition_estimation.calorie_intake.calorie_intake_estimate import calculate_calorie_intake
from LiveLite.recommendation_tool.diet_recommendation.food import micro_nutrients, macro_nutrients_data
from LiveLite.recommendation_tool.diet_recommendation.personalised_food_list import search_food, recommended_food, beef_data
from LiveLite.recommendation_tool.physical_activity_recommendation.physical_activity_recommend import calculate_calorie_burn