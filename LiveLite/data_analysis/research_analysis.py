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


def background_information(years=None):
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

    # Create Figure
    fig, ax = plt.subplot(figsize=(10, 6))

    ax.set_xlabel('Year')

    sns.violinplot(data=combined_df, x='Year', y='BMI')
    ax.set_ylabel('Proportion Obese')
    ax.set_title('Comparison of Proportion of Individuals Obese by Year')


    # Add horizontal grid lines
    ax.yaxis.grid(True)

    # Customize grid lines (optional)
    ax.grid(linestyle='-', linewidth='0.5', color='gray')

    return fig, ax


def obesity_trends():
    path = '../data/files/NHANES/BMX/'

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

            temp_dict = {'Year': suffix[suffix_split], 'Obesity_Proportion': len(df['Obese'] == 1) / len(df), 'Overweight_Proportion': len(df['Overweight (including obesity)'] == 1) / len(df)}

            df_list.append(pd.DataFrame(temp_dict))
        else:
            pass

        combined_df = pd.concat(df_list)

        # Create Figure of Prop
        fig, ax = plt.subplot(figsize=(10, 6))

        ax.set_xlabel('Year')

        sns.lineplot(data=combined_df, x='Year', y='Obesity_Proportion', marker='o', label='Obesity', ax=ax, color='blue')
        sns.lineplot(data=combined_df, x='Year', y='Overweight_Proportion', marker='x', label='Overweight', ax=ax, color='red')


        # Add title and labels
        ax.set_title('Proportion of Obesity and Overweight in the US (1999-2017)')
        ax.set_xlabel('Year')
        ax.set_ylabel('Proportion')

        # Add legend
        ax.legend()

        # Add grid lines
        ax.grid(True)

        return fig, ax




