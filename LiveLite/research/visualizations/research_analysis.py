"""
research_analysis

Provides:
   1. Functions that generate informative plots for the information page.
"""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def violin_plot_manager(data, plot_type='BMI', years=None):
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


def background_information_nhanes(data, years=None):
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
    else:
        years = years_default

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


def rename_column_ihme(column_name):
    """
    Helper function to rename long column names within IHME dataframes.
    :param column_name: Column name as string.
    :return: Modified column name.
    """
    start_keyword = "attributed to "
    end_keyword = ", in both sexes"
    if start_keyword in column_name and end_keyword in column_name:
        start_index = column_name.find(start_keyword) + len(start_keyword)
        end_index = column_name.find(end_keyword)
        return column_name[start_index:end_index]

    return column_name


def background_information_ihme(data, years=None):
    """
    Generates a bar plot comparing death by risk factor using IHME data.
    :param years: List of years to compare.
    :return: Figure object.
    """
    if years is None:
        years = [1990, 2017]

    # Create Figure on Death by Risk Factor (Global)
    # ihme = pd.read_csv('../../data/files/IHME/number-of-deaths-by-risk-factor.csv')
    ihme = data[~data['Code'].isna()].copy()
    ihme.columns = [rename_column_ihme(col) for col in ihme.columns]
    ihme_long = pd.melt(ihme, id_vars=['Entity', 'Code', 'Year'],
                        var_name='Risk Factor', value_name='Deaths')

    data_filtered_years = ihme_long[ihme_long['Year'].isin(years)]

    data_summary = (
        data_filtered_years.groupby(['Risk Factor', 'Year'])['Deaths'].sum().reset_index()
    )

    # Create figure with subplots
    fig = make_subplots(rows=1, cols=len(years),
                        subplot_titles=[f'Deaths by Risk Factor in {year}' for year in years],
                        shared_yaxes=True)

    highlighted_risk_factor = "high body-mass index"

    for i, year in enumerate(years, 1):
        data_year = (data_summary[data_summary['Year'] == year]
                     .sort_values(by='Deaths', ascending=True))

        # Define colors for each bar based on the risk factor
        colors = ['#ff6347' if risk == highlighted_risk_factor else '#95a5a6'
                  for risk in data_year['Risk Factor']]

        # Add bar trace for each risk factor
        fig.add_trace(go.Bar(
            y=data_year['Risk Factor'],
            x=data_year['Deaths'],
            orientation='h',
            marker={'color': colors},
            name=f'{year}',
            text=data_year['Deaths'].apply(lambda x: f'{x:,.0f}'),
            textposition='auto'
        ), row=1, col=i)

        # Set subplot title
        fig.update_xaxes(title_text='Number of Deaths', row=1, col=i)
    fig.update_yaxes(title_text='Risk Factor', row=1, col=1)

    # Set layout
    fig.update_layout(
        title='Deaths by Risk Factor',
        title_x=0.5,
        height=500,
        showlegend=False,
        margin={'l': 50, 'r': 50, 't': 100, 'b': 50}
    )
    fig.update_yaxes(title_text="Risk Factor", row=1, col=1)

    return fig


def obesity_trends(data, years=None):
    """
    Returns a line plot which visualizes obesity trends over time using NHANES data with Plotly.
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

    # Create the Plotly figure
    fig = px.line(data, x='Year', y='BMI', color='RIAGENDR',
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
