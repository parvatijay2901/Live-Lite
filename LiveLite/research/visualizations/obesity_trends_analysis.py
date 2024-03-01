"""
Obesity Trends Analysis

Provides:
    1. Function to plot the obesity trends over time.
"""
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
    years_default = [1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017]

    # If years is None, use the default years
    if years is None:
        years = years_default

    # Check if all provided years are valid
    if set(years).difference(years_default):
        raise ValueError(
            "Years contains non-valid years. Valid years start from 1999 and increment by 2 years."
        )

    # Filter the data for the selected years
    data = data[data['Year'].isin(years)]
    proportion_data = data.groupby(['Year', 'RIAGENDR'])['BMI'].mean().reset_index()
    proportion_data = proportion_data.rename(columns={'BMI': 'Proportion Obese'})


    # Create the Plotly figure
    fig = px.line(proportion_data, x='Year', y='Proportion Obese', color='RIAGENDR',
                  title='Comparison of Proportion of Individuals Obese by Year',
                  labels={'BMI': 'Proportion Obese', 'RIAGENDR': 'Gender'})

    # Customize the layout
    fig.update_layout(xaxis_title='Year',
                      yaxis_title='Proportion Obese',
                      legend_title='Gender')

    # Rotate x-axis labels for better readability
    fig.update_xaxes(tickangle=45)

    # Add horizontal grid lines for better readability
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

    return fig
