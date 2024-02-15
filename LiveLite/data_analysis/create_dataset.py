import pandas as pd
import os
from datetime import date

if __name__ == '__main__':
    # demo = pd.read_sas('./data/DEMO/DEMO_J.XPT')
    # dpq = pd.read_sas('./data/DPQ/DPQ_J.XPT')
    # smq = pd.read_sas('./data/SMQ/SMQ_J.XPT')
    # slq = pd.read_sas('./data/SLQ/SLQ_J.XPT')
    # hiq = pd.read_sas('./data/HIQ/HIQ_J.XPT')
    # paq = pd.read_sas('./data/PAQ/PAQ_J.XPT')
    # bmx = pd.read_sas('./data/BMX/BMX_J.XPT')
    # huq = pd.read_sas('./data/HUQ/HUQ_J.XPT')
    # dbq = pd.read_sas('./data/DBQ/DBQ_J.XPT')
    #
    # demo = demo[['SEQN', 'RIDAGEYR', 'RIDRETH1', 'RIDRETH3', 'INDFMPIR']]
    # dpq = dpq[['SEQN', 'DPQ020', 'DPQ050']]
    # smq = smq[['SEQN', 'SMQ040']]
    # slq = slq[['SEQN', 'SLD012']]
    # hiq = hiq[['SEQN', 'HIQ011']]
    # paq = paq[['SEQN', 'PAQ670']]
    # bmx = bmx[['SEQN', 'BMXWT', 'BMXHT']]
    # huq = huq[['SEQN', 'HUQ030', 'HUQ010']]
    # dbq = dbq[['SEQN', 'DBQ700']]

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