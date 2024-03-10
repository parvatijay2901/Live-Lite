"""
Compare Trends Over Time

Provides:
    - generate_violin_plot: Function that generates violin plots to observe trends of BMI, physical activity,
    or weight over time.

"""
import pandas as pd
import plotly.express as px


def generate_violin_plot(data, plot_type='BMI', years=None):
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
    years_possible = [1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017]

    if not isinstance(years, list) and years is not None:
        raise TypeError(
            "Years must be a list."
        )

    if years is not None:
        if not all(item in years_possible for item in years):
            raise ValueError(
                "Years contains non-valid years. Valid years start from 1999 and increment by 2 years."
            )

    if years is None:
        years = years_default

    if not isinstance(plot_type, str):
        raise TypeError('Plot Type must be str.')

    if plot_type not in ['BMI', 'Weight']:
        raise ValueError("Not valid plot type.")

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
    fig = px.box(data, x='Year', y=plot_type)
    # Customize axis labels and titles based on plot type
    if plot_type == 'BMI':
        fig.update_layout(yaxis_range=[18, 35])
        fig.update_xaxes(title='Year', tickvals=years)
        fig.update_yaxes(title='BMI (kg/m^2)')
        fig.update_layout(title='Comparison of BMI by Year', title_x=0.4)
    else:
        fig.update_xaxes(title='Year', tickvals=years)
        fig.update_yaxes(title='Weight (kg)')
        fig.update_layout(title='Comparison of Weight by Year', title_x=0.4)

    return fig