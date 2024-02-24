import matplotlib.pyplot as plt
import seaborn as sns

def plot_obesity_overweight_trends(data, years=None):
    if years is None:
        years = [1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017]

    data = data[data['Year'].isin(years)]
    
    # Create subplots with two plots side by side
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))

    # Plot proportion of individuals who are obese
    sns.lineplot(data=data, x='Year', y='Obese', ax=ax[0])
    ax[0].set_title('Proportion of Individuals Obese by Year')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Proportion Obese')

    # Plot proportion of individuals who are overweight (including obesity)
    sns.lineplot(data=data, x='Year', y='Overweight (including obesity)', ax=ax[1])
    ax[1].set_title('Proportion of Individuals Overweight (including obesity) by Year')
    ax[1].set_xlabel('Year')
    ax[1].set_ylabel('Proportion Overweight (including obesity)')

    # Customize x-axis 
    unique_years = sorted(data['Year'].unique())
    for axis in ax:
        axis.set_xticks(unique_years)
        axis.set_xticklabels(unique_years, rotation=45)
        axis.yaxis.grid(True)
        axis.grid(linestyle='-', linewidth='0.5', color='gray')

    plt.tight_layout()
    return fig