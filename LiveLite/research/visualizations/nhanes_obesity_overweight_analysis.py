"""
NHANES Obesity Overweight Analysis

Provides:
    1. Function that plots NHANES proportion of obese and overweight over time.
"""
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_obesity_overweight_trends(data, years=None):
    """
    Generates a line plot comparing the proportion of obese
     and overweight individuals over specified years.
    :param data: Combined processed NHANES dataframe.
    :param years: List of years.
    :return: Figure object.
    """
    years_default = [1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017]

    if years is not None:
        years = years_default
    elif isinstance(years, list):
        raise TypeError(
            "Years must be a list."
        )
    else:
        years = years_default

    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            "Data must be a dataframe."
        )

    if list(set(years).difference(years_default)):
        raise ValueError("Valid years start from 1999 and increment by 2 years.")

    data = data[data['Year'].isin(years)]

    # Create subplots with two plots side by side
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=(
            'Proportion of Individuals Obese by Year',
            'Proportion of Individuals Overweight (including obesity) by Year'
        )
    )

    # Plot proportion of individuals who are obese
    fig.add_trace(
        go.Scatter(
            x=data['Year'], y=data['Obese'], mode='lines', name='Obese'
        ),
        row=1,
        col=1
    )

    # Plot proportion of individuals who are overweight (including obesity)
    fig.add_trace(
        go.Scatter(
            x=data['Year'], y=data['Overweight (including obesity)'],
            mode='lines',
            name='Overweight (including obesity)'
        ),
        row=1,
        col=2
    )

    fig.update_xaxes(title_text='Year', row=1, col=1)
    fig.update_yaxes(title_text='Proportion Obese', row=1, col=1)
    fig.update_xaxes(title_text='Year', row=1, col=2)
    fig.update_yaxes(title_text='Proportion Overweight (including obesity)', row=1, col=2)

    # rotate x-axis labels
    fig.update_xaxes(tickangle=45)

    # add grid lines for better readability
    fig.update_layout(
        grid={'rows': 1, 'columns': 2},
        height=600, width=1000,
        title_text="Obesity and Overweight Trends Over Years"
    )
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')

    return fig
