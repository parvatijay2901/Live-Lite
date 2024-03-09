"""
IHME Data Analysis

Provides:
    - rename_column_ihme: renames ihme dataframe columns so labels in plots are readable.
    - process_ihme_data: pre-processes ihme data for plotting. Returns a processed dataframe, year list, and label
    to highlight in the plot.
    - plot_ihme_data: Plots the processed ihme data.

    1. Functions to process IHME data for plotting.
    2. Plot the processed IHME data to visualize obesity.
"""
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def rename_column_ihme(column_name):
    """
    Function that renames columns so they can fit into the plot axis
    :param column_name: string of the column name
    :return: string of the modified column name.
    """
    start_keyword = "attributed to "
    end_keyword = ", in both sexes"
    if start_keyword in column_name and end_keyword in column_name:
        start_index = column_name.find(start_keyword) + len(start_keyword)
        end_index = column_name.find(end_keyword)
        return column_name[start_index:end_index]

    return column_name


def process_ihme_data(ihme, years=None, highlighted_risk_factor="high body-mass index"):
    """
    Processes (pivots) the ihme data for plotting.
    :param ihme: Dataframe of ihme data.
    :param years: Optional; list of years.
    :param highlighted_risk_factor: Default=high body-mass index. Designates which factor to
    highlight in plot.
    :return: Returns a data summary, the years, and the highlighted factor.
    """
    if years is None:
        years = [1990, 2017]

    # Filter and rename columns
    ihme = ihme[~ihme['Code'].isna()]
    ihme.columns = [rename_column_ihme(col) for col in ihme.columns]

    # Reshape data
    ihme_long = pd.melt(
        ihme,
        id_vars=['Entity', 'Code', 'Year'],
        var_name='Risk Factor',
        value_name='Deaths'
    )

    # Filter data by years
    data_filtered_years = ihme_long[ihme_long['Year'].isin(years)]

    # Summarize data
    data_summary = data_filtered_years.groupby(['Risk Factor', 'Year'])
    data_summary = data_summary['Deaths'].sum().reset_index()

    return data_summary, years, highlighted_risk_factor


def plot_ihme_data(data, years=None, highlighted_risk_factor="high body-mass index"):
    """
    Plots the ihme data for the given years and highlights the designated risk factor.
    Raises Type errors if:
    - data is not a dataframe.
    - years is not a list.
    - highlighted_risk_factor is not a str.
    :param data: Dataframe of data to plot.
    :param years: List of years to plot.
    :param highlighted_risk_factor: Default=high body-mass index. Designates which factor to
    highlight in the plot.
    :return: Figure object.
    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            'Data should be a Pandas dataframe.'
        )

    possible_years = range(1990, 2020, 1)
    if years is not None:
        if not all(item in possible_years for item in years):
            raise ValueError(
                "Years contains non-valid years. Valid years start from 1999 and increment by 2 years."
            )

    if years is None:
        years = [1990, 2017]

    if not isinstance(years, list):
        raise TypeError(
            "Years should be a list."
        )
    if not isinstance(highlighted_risk_factor, str):
        raise TypeError(
            "Highlighted risk factor should be str."
        )

    risk_factors = [rename_column_ihme(col) for col in data.columns]
    if {highlighted_risk_factor}.difference(risk_factors):
        raise ValueError(
            'Invalid risk factor.'
        )

    data_summary, years, highlighted_risk_factor = process_ihme_data(data, years)

    fig = make_subplots(
        rows=1, cols=len(years),
        subplot_titles=[f'Deaths by Risk Factor in {year}' for year in years],
        shared_yaxes=True
    )

    data_summary = data_summary.sort_values(by=['Year', 'Deaths'], ascending=True)

    for i, year in enumerate(years, 1):
        data_year = data_summary[data_summary['Year'] == year]

        colors = [
            '#ff6347' if risk == highlighted_risk_factor else '#95a5a6'
            for risk in data_year['Risk Factor']
        ]

        fig.add_trace(go.Bar(
            y=data_year['Risk Factor'],
            x=data_year['Deaths'],
            orientation='h',
            marker={'color': colors},
            name=f'{year}',
            text=data_year['Deaths'].apply(lambda x: f'{x:,.0f}'),
            textposition='outside'
        ), row=1, col=i)

        fig.update_xaxes(title_text='Number of Deaths', range=[0, 20000000], row=1, col=i)

        if i == 0:
            y_axis = list(data_year['Risk Factor'])
            temp_vals = list(range(len(y_axis)))

            fig.update_yaxes(tickmode='array', tickvals=temp_vals, ticktext=y_axis, row=1, col=1)

    fig.update_layout(
        title='Deaths by Risk Factor',
        title_x=0.45,
        height=500,
        showlegend=False,
        autosize=True,
        yaxis={'dtick': 1},
        margin={'l': 50, 'r': 50, 't': 100, 'b': 50}
    )
    fig.update_yaxes(title_text="Risk Factor", row=1, col=1)

    return fig
