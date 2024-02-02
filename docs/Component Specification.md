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




__Name__: Obesity Trends  
__What It Does__: Reads NHANES data into a dataframe. Generates a line plot comparing obesity and severity
obesity overtime.  
__Inputs__: None  
__Outputs__: Object: Line plot displaying a obesity trend over time.  
__Assumptions__: Data is NOT cleaned - needs to be checked 

## ML - Prediction
__Name__: Obesity Risk Predictor  
__What It Does__: Builds and train the model based on available data on obesity & associated factors. Using the user inout data, model predicts the obesity risk for the individual.  
__Inputs__: Dataset & List - custom dataset built from NHANES data. User personal data including anthropometric data and lifestyle factors.  
__Outputs__: Number- predicting the percentage of risk.  
__Assumptions__: Prediction based only the data, the user inputs for fields that we have defined & disregarding any additinal factors contributing to obesity that is not within the scope of the tool.

## Recommendation
__Name__: Estimated Calorie need   
__What It Does__: Calculates & displays the estimated calorie need for the individual to stay fit based on the inputs provided.    
__Inputs__: List- User input data such as age, gender, height, weight and activity level.  
__Outputs__: Number- expressing the calorie need in kcal.  
__Assumptions__: Using the standard formula to calculate the calorie need, no other body vital data is considered.

__Name__: Excersie recommendation.  
__What It Does__: Calculates & displays the recommended physical activites along with duration & calorie burned.  
__Inputs__: List - user data such as age, height, weight and activity levels.   
__Outputs__: List - exercise name, duration and expected calorie burn.  
__Assumptions__: The calorie burn does not vary from person to person based on health conditions, standardized for the given inputs.

## Gather Necessary input data
- User Height/weight/gender/dietry preference/ Obesity risk/ amount of physical activity/ calory intake.

### Dietary recommendation:
#### Pre-process food data and add labels:
- Transform primary food data.
- Add labels and derive categories. 
- Labels:
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

#### Output: 
- Food groups the user should focus on.
- Build recommendation logic - from research studies on food consumption.

### Physical Activity


## User Interface
__Name__: Landing page  
__What It Does__: Provide a brief introduction to the website and guide users to navigate to their specific requests (Welcome message or brief description, Navigation links or buttons leading to the Research/Data Analysis, Tab and Tool (User Input) Tab, Maybe an overview of the website's mission or key features).

__Name__: Research/Data analysis Tab     
__What It Does__: Briefly explain about obesity, its trends over time, and its connections to various lifestyle factors through visualizations  to users.  
__Inputs__: Options for users to limit visualization options (e.g., time range, specific factors), Zoom and filter options for interactive exploration.  
__Output__: Talk users through the visualizations and explaining their significance.

__Name__: Tool (user input) Tab  
__What It Does__: Allow users to input their data for risk prediction and receive personalized recommendations related to diet and physical activity.  
__Inputs__: Input form for basic user information (age, weight, height, etc.), Perform Field validation checks to handle potential incorrect inputs, Integrate with risk prediction and recommendation system functions.  
__Output__: Rendered webpage that shows the tool output: Obesity risk level (Hazard ratio), Standard and personalized recommendations.