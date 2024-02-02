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
