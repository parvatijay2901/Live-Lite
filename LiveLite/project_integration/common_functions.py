"""_summary_
"""
import streamlit as st

def add_blank_lines(num_lines=1):
    """_summary_

    Args:
        num_lines (int, optional): _description_. Defaults to 1.
    """
    for _ in range(num_lines):
        st.write('\n')

def swap_pages_back(choice="obesity_assessment"):

    col1, _, col3 = st.columns([2.5, 10, 1.5])

    if choice == "obesity_assessment":
        with col1:
            if st.button("← Obesity Assessment 📑", use_container_width=True):
                st.switch_page("pages/b_obesity_assessment.py")
        with col3:
            if st.button("→ Home🏠", use_container_width=True):
                st.switch_page("app.py")
    elif choice == "basic_risk_insights":
        with col1:
            if st.button("← Basic Risk Insights🌿🏃🏼", use_container_width=True):
                st.switch_page("pages/3_risk_insights.py")
        with col3:
            if st.button("→ Home🏠", use_container_width=True):
                st.switch_page("app.py")