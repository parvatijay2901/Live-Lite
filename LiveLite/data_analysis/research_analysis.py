import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import os


def violin_plot_manager(plot_type='BMI', years=None):
    if years is None:
        years = [1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017]
    if not isinstance(plot_type, str):
        raise ValueError("Plot Type Argument must be a string.")

    # Load Data
    if plot_type == 'BMI' or plot_type == 'Weight':
        path = '../data/files/NHANES/BMX/'
    elif plot_type == 'Activity':
        path = '../data/files/NHANES/PAQ/'
    else:
        raise ValueError("Not valid plot_type.")

    suffix = {
        '': 1999, 'B': 2001, 'C': 2003, 'D': 2005, 'E': 2007, 'F': 2009, 'G': 2011, 'H': 2013,
        'I': 2015, 'J': 2017
    }

    df_list = []
    for file in os.listdir(path=path):
        if file.endswith('.XPT'):
            file_path = os.path.join(path, file)

            # Load the XPT file
            df = pd.read_sas(file_path)

            if plot_type == 'BMI':
                df = df[~df['BMXWT'].isna()]
                df = df[~df['BMXHT'].isna()]
                df['BMI'] = df['BMXWT'] / ((df['BMXHT'] / 100) ** 2)
            elif plot_type == 'Weight':
                df = df[~df['BMXWT'].isna()]
            elif plot_type == 'Activity':
                df = df[~df['PAQ670'].isna()]
                df = df[~df['PAQ670'].isin([77, 99, '.'])]
            else:
                pass

            suffix_split = file.split('_')
            try:
                suffix_split = suffix_split[1].split('.')
                suffix_split = suffix_split[0]
            except IndexError:
                suffix_split = ''
            df['Year'] = suffix[suffix_split]

            df_list.append(df)
        else:
            pass

    combined_df = pd.concat(df_list)
    combined_df = combined_df[combined_df['Year'].isin(years)]

    # Create Figure
    fig, ax = plt.subplot(figsize=(10, 6))

    ax.set_xlabel('Year')
    if plot_type == 'BMI':
        sns.violinplot(data=combined_df, x='Year', y='BMI')
        ax.set_ylabel('BMI (kg/m^2)')
        ax.set_title('Comparison of BMI by Year')
    elif plot_type == 'Weight':
        sns.violinplot(data=combined_df, x='Year', y='BMXWT')
        ax.set_ylabel('Weight (kg)')
        ax.set_title('Comparison of Weight by Year')
    elif plot_type == 'Activity':
        sns.violinplot(data=combined_df, x='Year', y='PAQ670')
        ax.set_ylabel('Days of Moderate Recreational Activity')
        ax.set_title('Comparison of Days of Moderate Recreational Activity by Year')

    # Add horizontal grid lines
    ax.yaxis.grid(True)

    # Customize grid lines (optional)
    ax.grid(linestyle='-', linewidth='0.5', color='gray')

    return fig, ax


def background_information_nhanes(years=None):
    if years is None:
        years = [1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017]

    suffix = {
        '': 1999, 'B': 2001, 'C': 2003, 'D': 2005, 'E': 2007, 'F': 2009, 'G': 2011, 'H': 2013,
        'I': 2015, 'J': 2017
    }

    path = '../data/files/NHANES/BMX/'
    df_list = []
    for file in os.listdir(path=path):
        if file.endswith('.XPT'):
            file_path = os.path.join(path, file)

            # Load the XPT file
            df = pd.read_sas(file_path)

            df = df[~df['BMXWT'].isna()]
            df = df[~df['BMXHT'].isna()]

            suffix_split = file.split('_')
            try:
                suffix_split = suffix_split[1].split('.')
                suffix_split = suffix_split[0]
            except IndexError:
                suffix_split = ''

            df['Year'] = suffix[suffix_split]
            df['BMI'] = df['BMXWT'] / ((df['BMXHT'] / 100) ** 2)
            df['Overweight (including obesity)'] = df['BMI'] >= 25
            df['Obese'] = df['BMI'] >= 30

            df_list.append(df)
        else:
            pass

    combined_df = pd.concat(df_list)
    combined_df = combined_df[combined_df['Year'].isin(years)]
    # Create Figure of Prop Obese
    fig, ax = plt.subplots(1, 2, figsize=(10, 6))

    ax.set_xlabel('Year')

    sns.lineplot(data=combined_df, x='Year', y='Obese')
    sns.lineplot(data=combined_df, x='Year', y='Overweight (including obesity)')
    ax.set_ylabel('Proportion Obese')
    ax.set_title('Comparison of Proportion of Individuals Obese by Year')
    # Adjust x-axis to show only discrete years
    # Get unique sorted years from the dataframe
    unique_years = sorted(combined_df['Year'].unique())
    # Set x ticks and labels to the unique years
    ax.set_xticks(unique_years)
    ax.set_xticklabels(unique_years, rotation=45)

    # Add horizontal grid lines
    ax.yaxis.grid(True)

    # Customize grid lines (optional)
    ax.grid(linestyle='-', linewidth='0.5', color='gray')
    plt.tight_layout()

    return fig


def background_information_ihme(years=None):
    if years is None:
        years = [1990, 2017]

    # Create Figure on Death by Risk Factor (Global)
    ihme = pd.read_csv('../data/files/IHME/number-of-deaths-by-risk-factor.csv')
    ihme = ihme[~ihme['Code'].isna()]
    ihme_long = pd.melt(ihme, id_vars=['Entity', 'Code', 'Year'], var_name='Risk Factor', value_name='Deaths')

    data_filtered_years = ihme_long[ihme_long['Year'].isin(years)]

    data_summary = data_filtered_years.groupby(['Risk Factor', 'Year'])['Deaths'].sum().reset_index()

    # Create figure and axes
    fig, axs = plt.subplots(1, len(years), figsize=(20, 10), sharey=True)

    for i, year in enumerate(years):
        data_year = data_summary[data_summary['Year'] == year].sort_values(by='Deaths', ascending=True)

        # Define colors for each bar based on the risk factor
        colors = ['#3498db' if years in risk else '#95a5a6' for risk in data_year['Risk Factor']]

        # Plot with conditional coloring
        sns.barplot(data=data_year, y='Risk Factor', x='Deaths', ax=axs[i], hue='Risk Factors', palette=colors)
        axs[i].set_title(f'Deaths by Risk Factor in {year}')
        axs[i].set_xlabel('Number of Deaths')
        axs[i].set_ylabel('')

        # Annotate with exact numbers
        for p in axs[i].patches:
            width = p.get_width()
            axs[i].text(width, p.get_y() + p.get_height() / 2,
                        '{:,.0f}'.format(width), va='center')

    # Adjust layout
    axs[0].set_ylabel('Risk Factor')
    plt.tight_layout()

    return fig


def obesity_trends(years=None):
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

    path = '../data/files/NHANES/BMX/'
    df_list = []
    for file in os.listdir(path=path):
        if file.endswith('.XPT'):
            file_path = os.path.join(path, file)

            # Load the XPT file
            df = pd.read_sas(file_path)

            df = df[~df['BMXWT'].isna()]
            df = df[~df['BMXHT'].isna()]

            suffix_split = file.split('_')
            try:
                suffix_split = suffix_split[1].split('.')
                suffix_split = suffix_split[0]
            except IndexError:
                suffix_split = ''

            df['Year'] = suffix[suffix_split]
            df['BMI'] = df['BMXWT'] / ((df['BMXHT'] / 100) ** 2)
            df['Overweight (including obesity)'] = df['BMI'] >= 25
            df['Obese'] = df['BMI'] >= 30

            df_list.append(df)
        else:
            pass

    combined_df = pd.concat(df_list)
    combined_df = combined_df[combined_df['Year'].isin(years)]

    # Import Demographics
    path = '../data/files/NHANES/DEMO/'
    demo_list = []
    for file in os.listdir(path=path):
        if file.endswith('.XPT'):
            file_path = os.path.join(path, file)

            # Load the XPT file
            df = pd.read_sas(file_path)

            suffix_split = file.split('_')
            try:
                suffix_split = suffix_split[1].split('.')
                suffix_split = suffix_split[0]
            except IndexError:
                suffix_split = ''
            df['Year'] = suffix[suffix_split]
            demo_list.append(df)
        else:
            pass

    demo_df = pd.concat(demo_list)
    demo_df = demo_df[demo_df['Year'].isin(years)]

    combined_df = pd.merge(combined_df, demo_df, on=['SEQN', 'Year'], how='outer')

    # Create Figure of Prop Obese
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.set_xlabel('Year')

    sns.lineplot(data=combined_df, x='Year', y='BMI', hue='RIAGENDR', palette='viridis')
    ax.set_ylabel('Proportion Obese')
    ax.set_title('Comparison of Proportion of Individuals Obese by Year')

    # Adjust x-axis to show only discrete years
    # Get unique sorted years from the dataframe
    unique_years = sorted(combined_df['Year'].unique())
    # Set x ticks and labels to the unique years
    ax.set_xticks(unique_years)
    ax.set_xticklabels(unique_years, rotation=45)

    # Add horizontal grid lines
    ax.yaxis.grid(True)

    # Customize grid lines (optional)
    ax.grid(linestyle='-', linewidth='0.5', color='gray')

    return fig

