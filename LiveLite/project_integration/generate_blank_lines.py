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
        