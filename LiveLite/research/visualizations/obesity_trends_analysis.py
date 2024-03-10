"""
Obesity Trends Analysis

Provides:
    - plot_obesity_trends: Plots obesity trends over time with NHANES data.
    1. Function to plot the obesity trends over time.
"""
import pandas as pd
import plotly.express as px


def plot_obesity_trends(data, years=None):
    """
    Returns a line plot which visualizes obesity trends over time using NHANES data with Plotly.
    Raises value error if:
    - The years are not valid years defined in NHANES.
    :param data: DataFrame containing the data.
    :param years: Optional; List of years to plot.
    :return: Plotly Figure object.
    """
    years_possible = [1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017]

    # If years is None, use the default years
    if years is None:
        years = years_possible

    # Check if all provided years are valid
    if not all(item in years_possible for item in years):
        raise ValueError(
            "Years contains non-valid years. Valid years start from 1999 and increment by 2 years."
        )

    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            'Data must be Pandas dataframe.'
        )

    # Filter the data for the selected years
    data = data[data['Year'].isin(years)]
    proportion_data = data.groupby(['Year', 'RIAGENDR'])['BMI'].mean().reset_index()
    proportion_data = proportion_data.rename(columns={'BMI': 'Proportion Obese'})
    
    category_order = ['Male', 'Female']
    color_sequence = ['#1f77b4', '#f19cbb']
    fig = px.line(proportion_data, x='Year', y='Proportion Obese', color='RIAGENDR',
                title='Comparison of Proportion of Individuals Obese by Year',
                labels={'Proportion Obese': 'Proportion Obese', 'RIAGENDR': 'Gender'},
                category_orders={'RIAGENDR': category_order},
                color_discrete_sequence=color_sequence)

    # Customize the layout
    fig.for_each_trace(lambda t: t.update(name='Male' if t.name == '1.0' else 'Female'))
    fig.update_layout(xaxis_title='Year',
                    yaxis_title='Proportion Obese',
                    legend_title='Gender',
                    title_x=0.35)

    return fig
