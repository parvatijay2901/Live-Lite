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


## UI
### Field Validation



