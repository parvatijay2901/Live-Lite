# Components

## Data Analysis
__Name__: Violin Plot Manager  
__What It Does__: Reads NHANES data into a dataframe, process it, and then plot the distribution with
violin plots.
__Inputs__: String: Type of data to visualize - e.g. Weight, BMI, Physical Activity, etc.  
__Outputs__: Object: Violin plot  
__Assumptions__: Data is NOT cleaned - needs to be checked for NaNs, bad data.

__Name__: Background Information  
__What It Does__: Reads NHANES data into a dataframe. Generates plots visualizing background information
such as: Prevalence of obesity by Sex, Race, Age.  
__Inputs__: Int: Year of data to visualize.
__Outputs__: Object: Bar plots showing prevalence of obesity of sex, race, age.  
__Assumptions__: Data is NOT cleaned - needs to be checked for NaNs, bad data.

__Name__: Obesity Trends  
__What It Does__: Reads NHANES data into a dataframe. Generates a line plot comparing obesity and severity
obesity overtime.  
__Inputs__: None  
__Outputs__: Object: Line plot displaying a obesity trend over time.  
__Assumptions__: Data is NOT cleaned - needs to be checked for NaNs, bad data.


## ML - Prediction



## Recommendation

## Gather Necessary input data
>> User Height/weight/gender/dietry preference/ Obesity risk/ amount of physical activity/ calory intake.

### Food

## Pre process food data and add labels
>> transform primary food data

>> Add labels and derice categories 

    Labels:
    1. High calorie
    2. Low calorie
    3. High Sugar
    4. Low sugar
    5. High Fibre 
    6. High protein
    7. Low protein 
    8. Medium protein 
    9. Vegan 
    10. Vegetarian
    11. Non vegetarian 
    12. Allergy foods 
    13. weight loss/weight gain 

## Recommend/ print Output 
>> Food groups the user should focus on

>>Build recommendation logic - from research studies on food consumption

### Physical Activity


## User Interface

**Name:** Landing page
- **What is does:** Provide a brief introduction to the website and guide users to navigate to their specific requests.
    - Welcome message or brief description.
    - Navigation links or buttons leading to the Research/Data Analysis
    - Tab and Tool (User Input) Tab.
    - Maybe an overview of the website's mission or key features.

**Name:** Research/Data analysis Tab
- **What is does:** Briefly explain about obesity, its trends over time, and its connections to various lifestyle factors through visualizations  to users.
- **Inputs:** 
    - Options for users to limit visualization options (e.g., time range, specific factors).
    - Zoom and filter options for interactive exploration.
- **Outputs:** Talk users through the visualizations and explaining their significance.

**Name:** Tool (user input) Tab
- **What is does:** Allow users to input their data for risk prediction and receive personalized recommendations related to diet and physical activity.
- **Inputs:** 
    - Input form for basic user information (age, weight, height, etc.).
    - Perform Field validation checks to handle potential incorrect inputs.
    - Integrate with risk prediction and recommendation system functions.
- **Outputs:** Rendered webpage that shows the tool output: 
    - Obesity risk level (Hazard ratio)
    - Standard and personalized recommendations.