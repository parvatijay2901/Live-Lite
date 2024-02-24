import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def rename_column_ihme(column_name):
    start_keyword = "attributed to "
    end_keyword = ", in both sexes"
    if start_keyword in column_name and end_keyword in column_name:
        start_index = column_name.find(start_keyword) + len(start_keyword)
        end_index = column_name.find(end_keyword)
        return column_name[start_index:end_index]
    else:
        return column_name

def process_ihme_data(ihme, years=None, highlighted_risk_factor="high body-mass index"):
    if years is None:
        years = [1990, 2017]

    # Filter and rename columns
    ihme = ihme[~ihme['Code'].isna()]
    ihme.columns = [rename_column_ihme(col) for col in ihme.columns]

    # Reshape data
    ihme_long = pd.melt(ihme, id_vars=['Entity', 'Code', 'Year'], var_name='Risk Factor', value_name='Deaths')

    # Filter data by years
    data_filtered_years = ihme_long[ihme_long['Year'].isin(years)]

    # Summarize data
    data_summary = data_filtered_years.groupby(['Risk Factor', 'Year'])['Deaths'].sum().reset_index()

    return data_summary, years, highlighted_risk_factor

def plot_ihme_data(data, years, highlighted_risk_factor="high body-mass index"):
    data_summary, years, highlighted_risk_factor = process_ihme_data(data, years)
    
    fig = make_subplots(rows=1, cols=len(years), subplot_titles=[f'Deaths by Risk Factor in {year}' for year in years], shared_yaxes=True)

    for i, year in enumerate(years, 1):
        data_year = data_summary[data_summary['Year'] == year].sort_values(by='Deaths', ascending=True)

        colors = ['#ff6347' if risk == highlighted_risk_factor else '#95a5a6' for risk in data_year['Risk Factor']]

        fig.add_trace(go.Bar(
            y=data_year['Risk Factor'],
            x=data_year['Deaths'],
            orientation='h',
            marker=dict(color=colors),
            name=f'{year}',
            text=data_year['Deaths'].apply(lambda x: f'{x:,.0f}'),
            textposition='auto'
        ), row=1, col=i)

        fig.update_xaxes(title_text='Number of Deaths', row=1, col=i)
    
    fig.update_yaxes(title_text='Risk Factor', row=1, col=1)

    fig.update_layout(
        title='Deaths by Risk Factor',
        title_x=0.5,
        height=500,
        showlegend=False,
        margin=dict(l=50, r=50, t=100, b=50)
    )
    fig.update_yaxes(title_text="Risk Factor", row=1, col=1)

    return fig