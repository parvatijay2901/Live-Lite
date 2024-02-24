import pandas as pd
import os
from datetime import date


def create_nhanes():
    suffix = {'': 1999, 'B': 2001, 'C': 2003, 'D': 2005, 'E': 2007, 'F': 2009, 'G': 2011, 'H': 2013, 'I': 2015, 'J': 2017}

    df_list = []
    path = '../files/NHANES/BMX/'
    path2 = '../files/NHANES/PAQ/'
    path3 = '../files/NHANES/DEMO/'



    for file in os.listdir(path=path):
        if file.endswith('.XPT'):
            file_path = os.path.join(path, file)

            # Load the XPT file
            df = pd.read_sas(file_path)
            df = df[~df['BMXWT'].isna()]
            df = df[~df['BMXHT'].isna()]
            df['BMI'] = df['BMXWT'] / ((df['BMXHT'] / 100) ** 2)

            df['Overweight (including obesity)'] = df['BMI'] >= 25
            df['Obese'] = df['BMI'] >= 30

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

    df_list = []
    # Hack fix, just redo the whole thing for the physical activity file.
    for file in os.listdir(path=path2):
        if file.endswith('.XPT'):
            file_path = os.path.join(path2, file)

            df = pd.read_sas(file_path)
            try:
                df = df[~df['PAQ670'].isna()]
            except KeyError:
                df = df[~df['PAD320'].isna()]

            suffix_split = file.split('_')
            try:
                suffix_split = suffix_split[1].split('.')
                suffix_split = suffix_split[0]
            except IndexError:
                suffix_split = ''
            df['Year'] = suffix[suffix_split]

            df_list.append(df)

    combined_df2 = pd.concat(df_list)

    demo_list = []
    for file in os.listdir(path=path3):
        if file.endswith('.XPT'):
            file_path = os.path.join(path3, file)

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

    demo_df = pd.concat(demo_list)

    merge = pd.merge(combined_df, combined_df2, on=['SEQN'], how='outer')
    merge = pd.merge(merge, demo_df, on=['SEQN'], how='left')
    merge = merge.set_index('SEQN')
    merge.to_parquet('../files/NHANES_Background.parquet')
    merge.to_csv('../files/NHANES_Background.csv')


def create_temp_data():
    suffix = {
        '': 1999, 'B': 2001, 'C': 2003, 'D': 2005, 'E': 2007, 'F': 2009, 'G': 2011, 'H': 2013,
        'I': 2015, 'J': 2017
    }
    df_dict = {1999: [], 2001: [], 2003: [], 2005: [], 2007: [], 2009: [], 2011: [], 2013: [], 2015: [], 2017: []}
    path = './data/'
    for folder in os.listdir(path=path):
        folder = path + folder + '/'
        for file in os.listdir(folder):
            # Assumes only XPT in the folders.
            df = pd.read_sas(folder + file)
            suffix_split = file.split('_')
            try:
                suffix_split = suffix_split[1].split('.')
                suffix_split = suffix_split[0]
            except IndexError:
                suffix_split = ''
            df['Year'] = suffix[suffix_split]

            df_dict[suffix[suffix_split]].append(df)

    final_list = []
    for _k, _v in df_dict.items():
        temp = pd.DataFrame(columns=['SEQN', 'Year'])
        for _df in _v:
            temp = pd.merge(temp, _df, on=['SEQN', 'Year'], how='outer')

        final_list.append(temp)

    final_df = pd.concat(final_list)
    final_df = final_df.sort_values(by=['SEQN', 'Year'])

    today = date.today()

    final_df.to_csv(f'./outputs/NHANES_dataset_{today}.csv', index=False)

if __name__ == '__main__':
    create_nhanes()
