# SEQN sequence num
# BMXHT	Standing Height (cm)	
# BMXWT	Weight (kg)	
# DPQ020	Feeling down, depressed, or hopeless	0-3, good - poor
# DPQ050	Poor appetite or overeating	0-3, good - poor
# SLD012	Sleep hours	number from 2 to 14.5
# PAQ670	Days moderate recreational activities	1 to 5 , sedentary - extra active
# DBQ700	How healthy is the diet	1-5 , good - poor
# HUQ010	General health condition	1-5 , good - poor
# RIAGENDR	Gender	0 - female, 1 - male
# RIDRETH3	Race/Ethnicity - Recode	1, 2, 3 ,4 , 6, 7 
# SMQ040	Do you now smoke cigarettes	0 no, 1 yes

import pandas as pd
import numpy as np


# Specify the file path of your CSV file
file_path = 'NHANES_dataset_2024-02-09.csv'

# Specify the columns you want to read
columns_to_read = ['SEQN',
    'BMXHT',
    'BMXWT',
    'RIDAGEYR',
    'DPQ020',
    'DPQ050',
    'SLD012',
    'PAQ670',
    'DBQ700',
    'HUQ010',
    'RIAGENDR',
    'RIDRETH3',
    'SMQ040',
    'INDFMPIR'
]
# Read the CSV file into a DataFrame, reading only the specified columns
df = pd.read_csv(file_path, usecols=columns_to_read)

# Drop rows with blank height or weight
df.dropna(subset=['BMXHT', 'BMXWT'], inplace=True)

# BMI = weight (kg) / (height (m) ^ 2)
df['BMI'] = df['BMXWT'] / ((df['BMXHT'] / 100) ** 2)  

# Add a new binary column 'Is_obese' based on BMI
df['IsObese'] = (df['BMI'] >= 30).astype(int)

# Drop the 'BMI' column
df.drop(columns=['BMI'], inplace=True)



def process_SMQ040(row):
    if row['SMQ040'] == 3:
        return 0
    elif row['SMQ040'] in [1, 2]:
        return 1
    elif row['RIDAGEYR'] > 18:
        return np.random.choice([0, 1])
    else:
        return 0


def process_SLD012(row):
    if pd.isnull(row['SLD012']):
        if row['RIDAGEYR'] < 10:
            return np.random.choice(np.arange(8, 14.6, 0.5))
        else:
            return np.random.choice(np.arange(2, 10.1, 0.5))
    else:
        return row['SLD012']
    
def process_general_1_5(row, column_name):
    if row[column_name] in [7, 9] or pd.isnull(row[column_name]):  # If field is 7, 9, or blank
        return np.random.choice([1, 2, 3, 4, 5])  # Random value between 1 to 5
    else:
        return row[column_name]
    

def process_general_0_3(row, column_name):
    if row[column_name] in [7, 9] or pd.isnull(row[column_name]) or row[column_name] not in [0, 1, 2, 3] :  
        if row['RIDAGEYR'] <= 16:
            return 0
        return np.random.choice([0, 1, 2, 3])  # Random value between 0 to 3
    else:
        return row[column_name]
    
def process_PAQ670(row):
    if row['PAQ670'] in [77, 99] or pd.isnull(row['PAQ670']) or row['PAQ670'] not in [1, 2, 3, 4, 5, 6, 7] :  
        if row['RIDAGEYR'] <= 12:
            processed_value =  7
        processed_value = np.random.choice([1, 2, 3, 4, 5, 6, 7])  # Random value between 1 to 7
    else:
        processed_value =  row['PAQ670']

    if processed_value == 1:
        return 1
    elif processed_value in [2, 3]:
        return 2
    elif processed_value == 4:
        return 3
    elif processed_value in [5, 6]:
        return 4
    elif processed_value == 7:
        return 5


def process_RIDRETH3(row):
    if pd.isnull(row['RIDRETH3']) or row['RIDRETH3'] not in [1, 2, 3, 4, 6, 7] :  
        return np.random.choice([1, 2, 3, 4, 6, 7])  # Random value between 1 to 7
    else:
        return row['RIDRETH3']

def process_RIAGENDR(row):
    if row['RIAGENDR'] == 2 :  
        return 0
    else:
        return row['RIAGENDR']
    
df['RIAGENDR'] = df.apply(lambda row: process_RIAGENDR(row), axis=1)
df['SMQ040'] = df.apply(lambda row: process_SMQ040(row), axis=1)
df['SLD012'] = df.apply(lambda row: process_SLD012(row), axis=1)
df['HUQ010'] = df.apply(lambda row: process_general_1_5(row,'HUQ010'), axis=1)
df['DBQ700'] = df.apply(lambda row: process_general_1_5(row,'DBQ700'), axis=1)
df['DPQ050'] = df.apply(lambda row: process_general_0_3(row,'DPQ050'), axis=1)
df['DPQ020'] = df.apply(lambda row: process_general_0_3(row,'DPQ020'), axis=1)
df['PAQ670'] = df.apply(lambda row: process_PAQ670(row), axis=1)
df['RIDRETH3'] = df.apply(lambda row: process_RIDRETH3(row), axis=1)


# Retain only records with no missing values in any column
# df.dropna(inplace=True)

# df = df[df['RIDAGEYR'] >= 18]

# Write the DataFrame to a new CSV file
output_file_path = 'ML_input.csv'
df.to_csv(output_file_path, index=False)


print(f"DF has been saved to '{output_file_path}'.")





