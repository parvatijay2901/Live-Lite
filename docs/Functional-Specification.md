# Functional Specification

## Background
In today's world, obesity is becoming increasingly prevalent, raising serious concerns, especially in the US. **Live Lite** is a promising solution, aiming to revolutionize how we tackle obesity. Our project combines research and practical personalized recommendations to explore the many factors that affect weight management. Our goal is to explore valuable insights and offer practical advice to individuals looking to improve their health.


## User Profile/Stories
### Story 1:
**Who:** Dietitians

**Wants:** Will want to know the historical background of obesity based on demographics - 
to assist in recommending proper diet that fits the individual's culture.

**Interaction Methods:** Webpage

**Needs:** Provide statistically accurate data on obesity.

**Skills**: Basic web browsing skills, Understands how to fill prompts and how to interpret 
the visualizations.

### Story 2:
**Who:** Researchers

**Wants:** Learn additional insights about obesity - Specifically, predictors, demographics at risk, 
age risk, etc.

**Interaction Methods:** Webpage

**Needs:** Provide accurate data on obesity.

**Skills**: Basic web browsing skills, Understands how to fill prompts and how to interpret
the visualizations.

### Story 3:
**Who:** Individuals wanting to get into a healthy range

**Wants:** To become informed about obesity and its risk factors, Predict if the individual is at risk, Personalized recommendations on diet and physical activities

**Interaction Methods:** Webpage

**Needs:** Provide accurate data on obesity. Protect user data.

**Skills**: Basic web browsing skills, Understands how to fill prompts and how to interpret
the visualizations.

### Story 4:
**Who**: Technicians

**Wants:** Create prediction model to provide users with personalized recommendations. Train and update models with new 
data.

**Interaction Methods:** Webpage

**Needs:** Good data to build a prediction model.

**Skills**: Programming, Data Analysis, Machine learning, and basic devops skills to deploy.

## Data Source
The data we will be using to train our obesity prediction model will be data from the National Health and Nutrition Examination Survey - also known as the NHANES dataset.
This data is a comprehensive survey of random individuals in each 2 year intervals starting from 1999.

The data's variables can be divided into six larger categories:
1. Demographics
2. Dietary Data
3. Examination Data
4. Laboratory Data
5. Questionnaire Data
6. Limited Access Data

The only data unavailable to us is the Limited Access Data.

For our model we will be utilizing data from the remaining five sections. The data comes in an XPT file format which can be read into Python through pandas as a dataframe.
Each column in the file represents a question and/or measurement. For example, Gender is under column "RIAGENDR" with values 1=Male, 2=Female, and .=Missing.

How each variable is coded can be found on the [NHANES website](https://wwwn.cdc.gov/nchs/nhanes/Default.aspx)

The columns provide the unique identifier 'SEQN' as a way to tie together different responses across the various XPT files that are available from the NHANES dataset.


## Use Cases
### Use Case 1:

**Objective:** View obesity data to understand obesity.

**Steps:**

1. User will access the webpage and arrive at landing page with provide background information and
historical analysis on obesity.

2. The users will have options to filter and choose between visualizations and the type.

**Implicit Case:**
- Need default visualization at startup.

### Use Case 2:

**Objective:** Get risk of obesity and recommendation to stay fit or become fit.

**Steps:**
1. User will access the webpage and arrive at landing page.
2. User link/tab to open a form to input personal data (weight, height, age, lifestyle, etc.)
   - Implicit case: 
     - Need to accommodate both imperial and metric units.
     - To validate form fields as user enters the data for edge cases.
     - Provide disclaimers for recommendations (allergy, etc.)
3. User submits form.
4. User redirected to page that shows:
   - Risk of obesity prediction
   - Expected calorie intake for age and lifestyle
   - Recommendation on food and physical activity

**Edge Cases:**
- Impossible parameters (BMI = 0 or BMI = 100)
- Impossible age (age < 0, age > 120)

### Use Case 3:
**Objective:** Train, update, and deploy the predictive model.

**Steps:**
1. Data collection from new users
2. Update the scripts
3. Push to git / repo
4. Update documentation
5. Maintain the model by updating it regularly.
