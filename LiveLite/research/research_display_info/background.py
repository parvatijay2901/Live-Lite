"""
Module for displaying background information and associated plots in streamlit.

Provides:
    - display_trends_over_time: Provides commentary and plots on BMI trends over
    time using NHANES data. Displays violin plot.
    - display_ihme_data_analysis: Provides commentary and plots on risk factors by
    death using IHME data. Displays a bar graph comparing death by risk factor over time.
    - display_background: Provides commentary and plots on prevalence of obesity over
    time using NHANES and IHME data.
"""

import streamlit as st
import LiveLite  # pylint: disable=import-error


def display_trends_over_time(data, years=None):
    """
    Displays the distribution of BMI from the NHANES data.
    Raises Type Error and Value Errors from the plotting function.
    Args:
        data: NHANES data.
        years: List of years to plot.

    Returns: None

    """
    fig = LiveLite.generate_violin_plot(data, years=years)
    LiveLite.add_blank_lines()
    st.markdown("""
        The chart below displays the overall distribution of BMI in the NHANES data set between 1999 and 2017.
        The mean BMI in 1999 was 24.89. The mean BMI in 2017 was 26.58. From 1999 to 2017,
        there was a 6.76% increase in  overall BMI in the United States. In addition, in 1999, the average BMI
        was still under the category of 'Healthy Weight'. However, in 2017 with the increase in BMI to 26.58,
        the average BMI is no longer considered 'Healthy' and is now firmly in the 'Overweight' category.
    """)
    LiveLite.add_blank_lines()
    _, col12, _ = st.columns([0.5, 2, 0.5])
    with col12:
        st.plotly_chart(fig, use_container_width=True)


def display_ihme_data_analysis(data, years):
    """
    Displays the death by risk factor for given years using IHME data.
    Raises Type Error and Value Errors from the plotting function.
    Args:
        data: IHME data.
        years: List of years.

    Returns: None.

    """
    LiveLite.add_blank_lines(2)
    st.markdown("""
        Also, according to a data published by the Institute for Health Metrics and Evaluation (IHME),
        obesity is a major risk factor for mortality in not just the United States but globally as well.
        The chart below shows that the deaths in the United States in 1990 compared with 2019 grouped by
        the associated Risk Factor. In 1990, we can see that deaths attributed to high body-mass index was around
        10th in primary causes, sitting at around 4.4 million people. In 2019, we see that deaths attributed to high
        body-mass index increased to 5th in primary causes, jumping to a staggering 10 million. From these plots we
        can confidently say that obesity is becoming an ever-increasing issue in the United States.
    """)
    fig = LiveLite.plot_ihme_data(data, years=years)
    st.plotly_chart(fig, use_container_width=True, width=1200, height=600)


def display_background():
    """
    Function that provides text commentary on plots.
    Raises no exceptions
    Returns: None

    """
    col1, _, col3 = st.columns([2, 0.2, 0.7])
    with col1:
        st.markdown("""
            Obesity is ever-growing issue in the modern world. Defined as 'weight that is
            considered higher than what is considered healthy for a given height' by the CDC.
            Body Mass Index (BMI) is a general method of defining obesity. BMI in the ranges of
            25 to 29.9 kg/m<sup>2</sup> are considered overweight and BMI greater than
            or equal to 30 kg/m<sup>2</sup> are considered obese. Obesity is nowadays described as
            a chronic disease that is only increasing in prevalence in all ages and currently now
             considered to be an ongoing global epidemic of obesity.""", unsafe_allow_html=True)
        st.markdown("""
            Using the NHANES data collected between the years of 1999 to 2018, we can observe
            that the prevalence of obesity in the United States has progressively increased from
            30.5 to 42.4 %.""", unsafe_allow_html=True)
    with col3:
        st.image("LiveLite/streamlit_app/images/background_on_obesity.png", width=200)

    display_trends_over_time(st.session_state['data_nhanes'], years=[1999, 2017])
    display_ihme_data_analysis(st.session_state['data_ihme'], years=[1990, 2019])
