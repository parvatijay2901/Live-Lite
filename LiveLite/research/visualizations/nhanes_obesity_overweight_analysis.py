"""
NHANES Obesity Overweight Analysis

Provides:
    - plot_obesity_overweight_trends: plots NHANES proportion of obesity data.
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
        years = years_possible


    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            "Data must be a dataframe."
        )

    data = data[data['Year'].isin(years)]
    prop_data = data.groupby('Year').agg({'Obese': 'mean', 'Overweight (including obesity)': 'mean'}).reset_index()

    max_proportion_obese = prop_data[['Obese']].max().max()
    max_proportion_overweight = prop_data[['Overweight (including obesity)']].max().max()

    min_proportion_obese = prop_data[['Obese']].min().min()
    min_proportion_overweight = prop_data[['Overweight (including obesity)']].min().min()

    # Optionally, you can add a small margin to the max limit for visual aesthetics
    max_proportion_obese += max_proportion_obese * 0.05
    max_proportion_overweight += max_proportion_overweight * 0.05

    # Create subplots with two plots side by side
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=(
            'Proportion of Individuals Obese by Year',
            'Proportion of Individuals Overweight (including obesity) by Year'
        )
    )

    # Plot proportion of individuals who are obese
    fig.add_trace(
        go.Scatter(
            x=prop_data['Year'], y=prop_data['Obese'], mode='lines', name='Obese'
        ),
        row=1,
        col=1
    )

    # Plot proportion of individuals who are overweight (including obesity)
    fig.add_trace(
        go.Scatter(
            x=prop_data['Year'], y=prop_data['Overweight (including obesity)'],
            mode='lines',
            name='Overweight (including obesity)'
        ),
        row=2,
        col=1
    )

    # Customize axes and layout with the same y-axis range for both plots
    fig.update_yaxes(title_text='Proportion', range=[min_proportion_obese, max_proportion_obese], row=1, col=1)
    fig.update_xaxes(title_text='Year', row=1, col=1)

    fig.update_yaxes(title_text='Proportion', range=[min_proportion_overweight, max_proportion_overweight], row=2, col=1)
    fig.update_xaxes(title_text='Year', row=2, col=1)

    fig.update_layout(
        grid={'rows': 2, 'columns': 1},
        height=800, width=800,
        title_text="Obesity and Overweight Trends Over Years",
        title_x=0.45,
        showlegend=False
    )

    return fig
