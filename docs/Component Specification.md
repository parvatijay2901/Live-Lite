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

## Dietary recommendation:
__Name__: Food portion recommendation.
__What It Does__: Displays the amount of each food groups that should be consumed by the user in a day.
__Inputs__: List - user data such as age, gender, food preference.
__Outputs__: tuple - minimum and maximum quantitiy of each food group.
__Assumptions__: The quantities are referred from USDA website.

__Name__: Food choices recommendation.  
__What It Does__: Displays the list of food in a given food group with calorie/fat/protein levels based on user input.
__Inputs__: List - user data such as age, gender, food preference, goal(weight loss/gain).
__Outputs__: List - Output a list of primary food varieties.
__Assumptions__: The food list and the calorie content are referred from USDA website.

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