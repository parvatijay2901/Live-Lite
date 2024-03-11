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

# pylint: disable=too-many-locals
# Disbaling the pylint too many locals check, as the code is fully readable
# and need local variables for data processing.
def build_and_evaluate_model(inputfile, outputfile):
    """
    Builds and evaluates a logistic regression model for predicting obesity risk.
    Args:
        inputfile (str): Full path for input csv file.
        outputfile (str): Full path for output model.
    Raises:
        Exception: If an invalid input file path is passed.
    Returns:
        None
    """
    try:
        # Load data
        data = pd.read_csv(inputfile)
        x_var = data.drop(['SEQN', 'BMXHT', 'BMXWT','IsObese'], axis=1)
        y_var = data['IsObese']

        # Define categorical and numerical features
        categorical_features = ['DPQ020',
                                'DPQ050',
                                'PAQ670',
                                'DBQ700',
                                'HUQ010',
                                'RIAGENDR',
                                'RIDRETH3',
                                'SMQ040']
        numerical_features = ['SLD012',
                              'RIDAGEYR']

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
        x_train, x_test, y_train, y_test = train_test_split(x_var,
                                                            y_var,
                                                            test_size=0.2,
                                                            random_state=42)

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

        # Save the model to be used by risk predictor
        save_model(best_model, outputfile)

        # Find the best parameters that influence obesity risk.
        find_most_influential_factors(best_model, numerical_features, categorical_features)

    except FileNotFoundError as excep:
        raise FileNotFoundError(f"Invalid input filepath: {excep}") from excep

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
        print(f"Model built and saved to '{filepath}'.")
    except FileNotFoundError as ex:
        raise FileNotFoundError(f"Invalid filepath: {ex}") from ex
    except Exception as exc:
        raise type(exc)(f"Error occurred while saving the model: {exc}") from exc

def find_most_influential_factors(model, num_features, cat_features):
    """
    Finds the most influential factors in the trained logistic regression model.
    Args:
        model (str): Full path of the saved model.
        num_features (list): Numerical factors of the model.
        cat_features (list): Categorical factors of the model.
    Raises:
        Exception: If an error occurs during the search of coefficients.
    Returns:
        None
    """
    try:
        # Extracting the coefficients from the logistic regression model
        coefficients = model.named_steps['classifier'].coef_[0]
        encoded_features = (model.named_steps['preprocessor']
                            .named_transformers_['cat']
                            .get_feature_names_out(input_features=cat_features)
        )
        # Combining numerical features and encoded categorical features
        all_features = num_features + list(encoded_features)

        coeff_df = pd.DataFrame({'Feature': all_features,
                                'Coefficient': coefficients})

        # Sorting by absolute coefficient values
        coeff_df['Abs_Coefficient'] = abs(coeff_df['Coefficient'])
        coeff_df = coeff_df.sort_values(by='Abs_Coefficient',ascending=False)

        print("Top Features Predicting Obesity:")
        print(coeff_df.head(3))

    except Exception as exc:
        raise type(exc)(f"Error occurred while searching for parameters: {exc}") from exc

if __name__ == "__main__":
    IP = "./data/ml_input.csv"
    OP = "./LiveLite/recommendation_tool/risk_assessment/trained_models/obesity_risk_model.joblib"
    build_and_evaluate_model(IP,OP)
