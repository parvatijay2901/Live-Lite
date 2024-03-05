"""
This module implements a logistic regression model to predict 
obesity risk based on various features.
The model is trained using data from the 'ml_input.csv' file.

Functions:
- build_and_evaluate_model()
- save_model()
- find_most_influential_factors()
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import class_weight
import joblib

def build_and_evaluate_model():
    """
    Builds and evaluates a logistic regression model for predicting obesity risk.
    Raises:
        Exception: If an error occurs while fitting a regression model.
    Returns:
        None
    """
    try:
        # Load data
        data = pd.read_csv('./data/input_files/ml_input.csv')
        x = data.drop(['SEQN', 'BMXHT', 'BMXWT','IsObese'], axis=1)
        y = data['IsObese']

        # Define categorical and numerical features
        categorical_features = ['DPQ020',
                                'DPQ050',
                                'PAQ670',
                                'DBQ700',
                                'HUQ010',
                                'RIAGENDR',
                                'RIDRETH3',
                                'SMQ040']
        numerical_features = ['SLD012', 'RIDAGEYR']

        # Define preprocessing steps for numerical and categorical features
        numerical_transformer = StandardScaler()
        categorical_transformer = OneHotEncoder(handle_unknown='ignore')

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numerical_transformer, numerical_features),
                ('cat', categorical_transformer, categorical_features)
            ])

        # Logistic regression model
        model = Pipeline([
            ('preprocessor', preprocessor),
            ('classifier', LogisticRegression(max_iter=2000))
        ])

        # Split the data into test data & training data
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        # Calculate class weights to handle class imbalance
        class_weights = (class_weight.compute_class_weight('balanced',
                        classes=np.unique(y_train), y=y_train))
        print("Class Weights: ", class_weights)

        # Define the hyperparameter grid
        param_grid = {
            # Regularization strength
            'classifier__C': [0.001, 0.01, 0.1, 1, 10, 100],
            'classifier__penalty': ['l2'],
            # Solver algorithm
            'classifier__solver': ['lbfgs', 'saga']
        }

        # Perform grid search with cross-validation
        grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
        grid_search.fit(x_train, y_train)

        # Get the best hyperparameters and model
        best_params = grid_search.best_params_
        best_model = grid_search.best_estimator_

        # Evaluate the best model
        y_pred = best_model.predict(x_test)

        accuracy = accuracy_score(y_test, y_pred)

        print("Best Parameters:", best_params)
        print(f'Best Accuracy: {accuracy}')
        print('Classification Report:')
        print(classification_report(y_test, y_pred))
        save_model(best_model, 'obesity_risk_model.joblib')

    except Exception as e:
        raise type(e)(f"Error occurred while building and evaluating the model: {e}") from e

def save_model(model, filepath):
    """
    Saves the trained model to a local file.
    Args:
        model(pipeline): Best regression model based on hyperparameter grid search
        filepath(str)
    Raises:
        FileNotFoundError: If the specified filepath is invalid.
        Exception: If an error occurs while saving the model.
    Returns:
        None
    """
    try:
        joblib.dump(model, filepath)
        print('Model built and saved')
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Invalid filepath: {e}") from e
    except Exception as e:
        raise type(e)(f"Error occurred while saving the model: {e}") from e

def find_most_influential_factors(model, num_features, cat_features):
    """
    Finds the most influential factors in the trained logistic regression model.
    Raises:
        Exception: If an error occurs during the search of coefficients.
    Returns:
        None
    """
    try:
        # Extracting the coefficients from the logistic regression model
        coefficients = model.named_steps['classifier'].coef_[0]
        encoded_features = (
            model.named_steps['preprocessor']
            .named_transformers_['cat']
            .get_feature_names_out(input_features=cat_features)
        )
        # Combining numerical features and encoded categorical features
        all_features = num_features + list(encoded_features)

        coefficients_df = pd.DataFrame({'Feature': all_features, 'Coefficient': coefficients})

        # Sorting by absolute coefficient values to identify the most influential features
        coefficients_df['Abs_Coefficient'] = abs(coefficients_df['Coefficient'])
        coefficients_df = coefficients_df.sort_values(by='Abs_Coefficient', ascending=False)

        print("Top Features Predicting Obesity:")
        print(coefficients_df.head(3))

    except Exception as e:
        raise Exception(f"Error occurred while building and evaluating the model: {str(e)}")

if __name__ == "__main__":
    build_and_evaluate_model()
