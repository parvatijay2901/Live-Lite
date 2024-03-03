"""
Compare Trends Over Time

Provides:
    1. Function that generates violin plots to observe trends of BMI, physical activity,
    or weight over time.
"""
import pandas as pd
import plotly.express as px


def generate_violin_plot(data, plot_type='Weight', years=None):
    """
    Creates a violin plot which plots the distribution of the variable
    specified by plot_type of specified years.
    Raises Value Error if:
    - Years are not valid in NHANES.
    Raises Type Error if:
    - data is not a dataframe.
    - plot_type is not a str.
    - years is not None or not a list.
    :param data: Combined processed NHANES data.
    :param plot_type: String specifying the variable to plot.
    :param years: List of years to plot.
    :return: Figure object.
    """
    years_default = [1999, 2005, 2011, 2017]

    if years is not None:
        years = years_default
    elif not isinstance(years, list):
        raise TypeError(
            "Years must be a list."
        )
    else:
        years = years_default

    if plot_type not in ['BMI', 'Weight']:
        raise ValueError("Not valid plot type.")

    if list(set(years).difference(years_default)):
        raise ValueError("Valid years start from 1999 and increment by 6 years.")

    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            "Data must be a dataframe."
        )

    if not isinstance(plot_type, str):
        raise TypeError("Plot Type Argument must be a string.")

    data = data[data['Year'].isin(years)]

    if plot_type == 'Weight':
        plot_type = 'BMXWT'

    # Create Figure
    fig = px.violin(data, x='Year', y=plot_type, box=True, points=False)

    # Customize axis labels and titles based on plot type
    if plot_type == 'BMI':
        fig.update_xaxes(title='Year', tickvals=years)
        fig.update_yaxes(title='BMI (kg/m^2)')
        fig.update_layout(title='Comparison of BMI by Year', title_x=0.4)
    elif plot_type == 'Weight':
        fig.update_xaxes(title='Year', tickvals=years)
        fig.update_yaxes(title='Weight (kg)')
        fig.update_layout(title='Comparison of Weight by Year', title_x=0.4)

    return fig
