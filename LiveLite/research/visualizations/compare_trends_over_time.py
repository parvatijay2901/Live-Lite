import plotly.express as px

def generate_violin_plot(data, plot_type='BMI', years=None):
    if years is None:
        years = [1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017]
    
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
        fig.update_layout(title='Comparison of Days of Moderate Recreational Activity by Year', title_x=0.4)

    return fig