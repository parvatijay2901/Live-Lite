"""
This page provides personalized food recommendations
based on the user's food preferences.
"""

import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import LiveLite # pylint: disable=import-error

def pagee():
    """
    This function sets up the 'Food Recommendations' page, providing users with
    personalized food suggestions based on their food preferences. Users can select
    a food category to view recommendations or search for specific food items.
    Nutritional content for searched food items is also displayed.
    """
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

    # Go back to the home page if the variables are not loaded
    LiveLite.check_session_state_variable("recommendations")

    # Provide an option to the user to navigate to other pages
    LiveLite.swap_pages_back(choice="basic_recommendations")

    st.markdown("""<div style="text-align:center;"><h2>Food Recommendations</h2></div>""",
                unsafe_allow_html=True)
    LiveLite.add_blank_lines()

    st.markdown("""<div style="text-align:center;"><h3 style='color:gold;'>
                Personalized Suggestions</h3></div>""", unsafe_allow_html=True)

    # Retrieve or generate personalized food recommendations
    if 'recommended_foods_df' not in st.session_state:
        recommended_foods_df = LiveLite.controller(
                                "diet_recommender_advanced_based_on_food_preference")
        st.session_state['recommended_foods_df'] = recommended_foods_df
    else:
        recommended_foods_df = st.session_state['recommended_foods_df']
    food_category = recommended_foods_df['Food Category'].unique().tolist()

    # Display food recommendations based on selected food category
    st.markdown("""<div style ="text-align: center;"><p style='color:#99fadc;'>Below are some
                food items based on your food preference that you can incorporate into your diet
                to maintain a balanced calorie intake and optimize your nutritional intake for the
                best outcomes!</p></div>""", unsafe_allow_html=True)
    _, col12,_ = st.columns([1,10,1])
    with col12:
        food_category_choice = st.selectbox("Choose a food category to view", food_category)
        recommended_food_category_df = recommended_foods_df[
        recommended_foods_df['Food Category'] == food_category_choice]
        st.dataframe(recommended_food_category_df, hide_index=True)

    LiveLite.add_blank_lines(3)

    st.markdown("""<div style="text-align:center;"><h3 style='color:gold;'>Nutritional Content
                </h3></div>""", unsafe_allow_html=True)
    st.markdown("""<div style ="text-align: center;"><p style='color:#99fadc;'>Learn More About
                the Nutritional Content of Any Food!</p></div>""", unsafe_allow_html=True)

    # Display search input field for food items
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        if 'search_food_items' not in st.session_state:
            search_food_items = st.text_input("Enter your Choice")
        else:
            search_food_items = st.text_input("Enter your Choice",
                                            value=st.session_state['search_food_items'])
        st.session_state['search_food_items'] = search_food_items

        with stylable_container("button",
                    css_styles="""button {background-color: #f2f2f2; color: black;
                                font-size: 50px;}"""):
            view_search_results = st.button("View Food of Your Choice 🥗", use_container_width=True)
        LiveLite.add_blank_lines(2)
    if view_search_results:
        searched_foods_df = LiveLite.controller("diet_recommender_advanced_search_food_items")
        if searched_foods_df is not None:
            if len(searched_foods_df) != 0:
                _, col22 = st.columns([0.3,1])
                with col22:
                    st.dataframe(searched_foods_df, hide_index=True)
            else:
                st.markdown("""<div style ="text-align: center;"><p>
                            Sorry, we couldn't find that item in our database!</p></div>""",
                            unsafe_allow_html=True)
        else:
            st.markdown("""<div style ="text-align: center;"><p>
                        Sorry, we couldn't find that item in our database!</p></div>""",
                        unsafe_allow_html=True)

if __name__ == "__main__":
    pagee()
