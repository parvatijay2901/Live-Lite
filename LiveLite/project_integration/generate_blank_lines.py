import streamlit as st

def add_blank_lines(num_lines=1):
    for _ in range(num_lines):
        st.write('\n')