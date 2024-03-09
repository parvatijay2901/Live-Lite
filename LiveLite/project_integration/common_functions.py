"""
This module contains functions used multiple times in a Streamlit app.

Functions:
- add_blank_lines(num_lines): Add blank lines to the Streamlit app.
- swap_pages_back(choice): Create navigation buttons to go back
                            to previous pages in the app.
- check_session_state_variable(choice): Check if session state variables
                        are loaded, and switch to the previous page if not.
"""

import streamlit as st

def home_page():
    """
    Redirects to the home page.

    Raises:
        FileNotFoundError: Raised when the home page file is not found.
    """
    try:
        st.switch_page("app.py")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File - {e} not found") from e

def obesity_assessment_page():
    """
    Redirects to the obesity assessment page.

    Raises:
        FileNotFoundError: Raised when the obesity assessment file is not found.
    """
    try:
        st.switch_page("pages/b_obesity_assessment.py")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File - {e} not found") from e

def risk_insights_page():
    """
    Redirects to the risk insights page.

    Raises:
        FileNotFoundError: Raised when the risk insights file is not found.
    """
    try:
        st.switch_page("pages/c_risk_insights.py")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File - {e} not found") from e

def personalized_recommendations_page():
    """
    Redirects to the personalized recommendations page.

    Raises:
        FileNotFoundError: Raised when the personalized recommendations file is not found.
    """
    try:
        st.switch_page("pages/d_personalized_recommendations.py")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File - {e} not found") from e

def add_blank_lines(num_lines=1):
    """Function to add blank lines to the Streamlit app.

    Args:
        num_lines (int, optional): Number of blank lines to add. Defaults to 1.

    Raises:
        TypeError: If `num_lines` is not an integer.
        ValueError: If `num_lines` is less than or equal to 0.
    """
    if not isinstance(num_lines, int):
        raise TypeError("num_lines must be an integer.")
    if num_lines <= 0:
        raise ValueError("num_lines must be greater than 0.")

    for _ in range(num_lines):
        st.write('\n')

def swap_pages_back(choice):
    """Create navigation buttons for users to go back
    to previous pages in the Streamlit app.

    Args:
        choice (str): The choice of page to navigate back to.

    Raises:
        ValueError: If `choice` is not one of "obesity_assessment",
                                            "basic_risk_insights",
                                            or "basic_recommendations".
    """

    col1, _, col3 = st.columns([2.5, 10, 1.5])

    # Provide this option in c_risk_insights page
    if choice == "obesity_assessment":
        with col1:
            if st.button("← Obesity Assessment 📑", use_container_width=True):
                obesity_assessment_page()
        with col3:
            if st.button("→ Home🏠", use_container_width=True):
                home_page()
    # Provide this option in d_personalized_recommendations
    elif choice == "basic_risk_insights":
        with col1:
            if st.button("← Basic Risk Insights🏃🏼", use_container_width=True):
                risk_insights_page()
        with col3:
            if st.button("→ Home🏠", use_container_width=True):
                home_page()
    # Provide this option in e_more_diet_recommendations
    elif choice == "basic_recommendations":
        with col1:
            if st.button("← Basic Recommendations🌿", use_container_width=True):
                personalized_recommendations_page()
        with col3:
            if st.button("→ Home🏠", use_container_width=True):
                home_page()
    else:
        raise ValueError("Invalid choice.")

def check_session_state_variable(choice):
    """Check if session state variables are loaded,
    and switch to the previous page if not.

    Args:
        choice (str): Frontend choice based on the page
        that calls. Should be either "research" or "recommendations".

    Raises:
        ValueError: If `choice` is not "research" or "recommendations".
        FileNotFoundError: If the required files are not found.
    """
    if choice == "research":
        try:
            if ('data_nhanes' not in st.session_state or
                'data_ihme' not in st.session_state):
                st.switch_page("app.py")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File - {e} not found") from e
    elif choice == "recommendations":
        try:
            if ('user_inputs' not in st.session_state or
                'food_nutrition_data' not in st.session_state):
                st.switch_page("app.py")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"File - {e} not found") from e
    else:
        raise ValueError("Invalid choice.")
