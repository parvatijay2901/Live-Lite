import matplotlib.pyplot as plt
import seaborn as sns

def plot_obesity_trends(data, years=None):
    """
    Returns a line plot which visualizes obesity
    :param years:
    :return:
    """
    if years is None:
        years = [1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017]

    suffix = {
        '': 1999, 'B': 2001, 'C': 2003, 'D': 2005, 'E': 2007, 'F': 2009, 'G': 2011, 'H': 2013,
        'I': 2015, 'J': 2017
    }

    data = data[data['Year'].isin(years)]

    # Create Figure of Prop Obese
    fig = plt.figure(figsize=(10, 6))
    
    sns.lineplot(data=data, x='Year', y='BMI', hue='RIAGENDR', palette='viridis')
    plt.xlabel('Year')
    plt.ylabel('Proportion Obese')
    plt.title('Comparison of Proportion of Individuals Obese by Year')

    # Adjust x-axis to show only discrete years
    # Get unique sorted years from the dataframe
    unique_years = sorted(data['Year'].unique())
    # Set x ticks and labels to the unique years
    plt.xticks(unique_years, rotation=45)

    # Add horizontal grid lines and customize grid lines (optional)
    plt.grid(axis='y', linestyle='-', linewidth='0.5', color='gray')

    return fig
