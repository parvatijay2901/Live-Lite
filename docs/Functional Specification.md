# User Stories
## Story 1:
**Who:** Dietitians

**Wants:** Will want to know the historical background of obesity based on demographics - 
to assist in recommending proper diet that fits the individual's culture.

**Interaction Methods:** Webpage

**Needs:** Provide statistically accurate data on obesity.

**Skills**: Basic web browsing skills, Understands how to fill prompts and how to interpret 
the visualizations.

## Story 2:
**Who:** Researchers

**Wants:** Learn additional insights about obesity - Specifically, predictors, demographics at risk, 
age risk, etc.

**Interaction Methods:** Webpage

**Needs:** Provide accurate data on obesity.

**Skills**: Basic web browsing skills, Understands how to fill prompts and how to interpret
the visualizations.

## Story 3:
**Who:** Individuals wanting to get into a healthy range

**Wants:** To become informed about obesity and its risk factors, Predict if the individual is at risk, Personalized recommendations on diet and physical activities

**Interaction Methods:** Webpage

**Needs:** Provide accurate data on obesity. Protect user data.

**Skills**: Basic web browsing skills, Understands how to fill prompts and how to interpret
the visualizations.


## Story 4:
**Who**: Technicians

**Wants:** Create prediction model to provide users with personalized recommendations. Train and update models with new 
data.

**Interaction Methods:** Webpage

**Needs:** Good data to build a prediction model.

**Skills**: Programming, Data Analysis, Machine learning, and basic devops skills to deploy.

#
#
# Use Cases
## Use Case 1:

Objective: View obesity data to understand obesity.

Steps:

1. User will access the webpage and arrive at landing page with provide background information and
historical analysis on obesity.

2. The users will have options to filter and choose between visualizations and the type.

Implicit Case:

- Need default visualization at startup.


## Use Case 2:

Objective: Get risk of obesity and recommendation to stay fit or become fit.

Steps:
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

Edge Cases:
- Impossible parameters (BMI = 0 or BMI = 100)
- Impossible age (age < 0, age > 120)


## Use Case 3:

Objective: Train, update, and deploy the predictive model.

Steps:
1. Data collection from new users
2. Update the scripts
3. Push to git / repo
4. Update documentation
5. Maintain the model by updating it regularly.
