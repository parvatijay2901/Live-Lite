import streamlit as st
import time

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

def main():
#     page_bg_color = f"""
#     <style>
#     body {{
#         background-color: #3c3254; /* Background color */
#         color: #EEEEEE; /* Font color */
#     }}
#     [data-testid="stAppViewContainer"] > .main {{
#         background-color: #3c3254; /* Background color */
#     }}
#     [data-testid="stHeader"] {{
#         background: rgba(0,0,0,0); /* Transparent header background */
#     }}
#     </style>
# """

#     st.markdown(page_bg_color, unsafe_allow_html=True)


    st.title("Obesity Analysis and Lifestyle Tool")
    st.write("Welcome to our app! Use the sidebar to navigate through different pages.")
    
if __name__ == "__main__":
    main()