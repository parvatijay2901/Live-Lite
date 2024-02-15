import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib  
data = pd.read_csv('ML_input.csv')
X = data.drop(['SEQN', 'BMXHT', 'BMXWT','IsObese'], axis=1)
y = data['IsObese']
categorical_features = ['DPQ020', 'DPQ050', 'PAQ670', 'DBQ700', 'HUQ010', 'RIAGENDR', 'RIDRETH3', 'SMQ040']
numerical_features = ['SLD012', 'RIDAGEYR']

# Define preprocessing steps for numerical and categorical features
numerical_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore')
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Define Logistic regression model
model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=2000))
])
# Split the data into test data & training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'obesity_risk_model.joblib')
print('Model built and saved')