"""
This module contains functions used multiple times in a Streamlit app.

Functions:
- add_blank_lines(num_lines): Add blank lines to the Streamlit app.
- swap_pages_back(choice): Create navigation buttons to go back
                            to previous pages in the app.
- check_session_state_variable(choice): Check if session state variables
                        are loaded, and switch to the previous page if not.
"""

import os
import streamlit as st

def home_page():
    """
    Redirects to the home page.

    Raises:
        FileNotFoundError: Raised when the home page file is not found.
    """
    if os.path.exists(os.path.join(os.getcwd(), "LiveLite/streamlit_app/app.py")):
        st.switch_page("app.py")
    else:
        raise FileNotFoundError("File app.py not found")

def obesity_assessment_page():
    """
    Redirects to the obesity assessment page.

    Raises:
        FileNotFoundError: Raised when the obesity assessment file is not found.
    """
    if os.path.exists(os.path.join(os.getcwd(),
                                "LiveLite/streamlit_app/pages/b_obesity_assessment.py")):
        st.switch_page("pages/b_obesity_assessment.py")
    else:
        raise FileNotFoundError("File b_obesity_assessment.py not found")

def risk_insights_page():
    """
    Redirects to the risk insights page.

    Raises:
        FileNotFoundError: Raised when the risk insights file is not found.
    """

    if os.path.exists(os.path.join(os.getcwd(), "LiveLite/streamlit_app/pages/c_risk_insights.py")):
        st.switch_page("pages/c_risk_insights.py")
    else:
        raise FileNotFoundError("File c_risk_insights.py not found")

def personalized_recommendations_page():
    """
    Redirects to the personalized recommendations page.

    Raises:
        FileNotFoundError: Raised when the personalized recommendations file is not found.
    """
    if os.path.exists(os.path.join(os.getcwd(),
                                "LiveLite/streamlit_app/pages/d_personalized_recommendations.py")):
        st.switch_page("pages/d_personalized_recommendations.py")
    else:
        raise FileNotFoundError("File d_personalized_recommendations.py not found")

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

def swap_page_back(choice):
    """Create navigation buttons for users to go back
    to a previous page in the Streamlit app.

    Args:
        choice (str): The choice of page to navigate back to.

    Raises:
        ValueError: If `choice` is not 'home' or 'obesity assessment'.
    """
    # Provide this option to switch back "home"
    if choice == "home":
        _, col1 = st.columns([10, 1.5])
        with col1:
            if st.button("→ Home🏠", use_container_width=True):
                home_page()
    elif choice == "obesity_assessment":
        obesity_assessment_page()
    else:
        raise ValueError("Invalid choice.")

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
        if ('data_nhanes' not in st.session_state or
            'data_ihme' not in st.session_state):
            filepath = "LiveLite/streamlit_app/app.py"
            if os.path.exists(os.path.join(os.getcwd(), filepath)):
                st.switch_page("app.py")
            else:
                raise AssertionError("File app.py not found")
    elif choice == "recommendations":
        if ('user_inputs' not in st.session_state or
            'food_nutrition_data' not in st.session_state):
            filepath = "LiveLite/streamlit_app/app.py"
            if os.path.exists(os.path.join(os.getcwd(), filepath)):
                st.switch_page("app.py")
            else:
                raise AssertionError("File app.py not found")
    else:
        raise ValueError("Invalid choice.")
