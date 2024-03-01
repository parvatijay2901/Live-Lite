"""
Compare Trends Over Time

Provides:
    1. Function that generates violin plots to observe trends of BMI, physical activity,
    or weight over time.
"""

import plotly.express as px


def generate_violin_plot(data, plot_type='BMI', years=None):
    """
    Creates a violin plot which plots the distribution of the variable
     specified by plot_type of specified years.
    :param data: Combined processed NHANES data.
    :param plot_type: String specifying the variable to plot.
    :param years: List of years to plot.
    :return: Figure object.
    """

    years_default = [1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017]

    if years is not None:
        years = years_default
    else:
        years = years_default

    if list(set(years).difference(years_default)):
        raise ValueError("Valid years start from 1999 and increment by 2 years.")

    if not isinstance(plot_type, str):
        raise ValueError("Plot Type Argument must be a string.")

    data = data[data['Year'].isin(years)]

    # Create Figure
    fig = px.violin(data, x='Year', y=plot_type, box=True, points=False)

    # Customize axis labels and titles based on plot type
    if plot_type == 'BMI':
        fig.update_xaxes(title='Year')
        fig.update_yaxes(title='BMI (kg/m^2)')
        fig.update_layout(title='Comparison of BMI by Year', title_x=0.4)
    elif plot_type == 'Weight':
        fig.update_xaxes(title='Year')
        fig.update_yaxes(title='Weight (kg)')
        fig.update_layout(title='Comparison of Weight by Year', title_x=0.4)
    elif plot_type == 'Activity':
        fig.update_xaxes(title='Year')
        fig.update_yaxes(title='Days of Moderate Recreational Activity')
        fig.update_layout(title='Comparison of Days of Moderate Recreational Activity by Year',
                          title_x=0.4)

    return fig
