import pandas as pd

if __name__ == '__main__':
    demo = pd.read_sas('./data/DEMO/DEMO_J.XPT')
    dpq = pd.read_sas('./data/DPQ/DPQ_J.XPT')
    smq = pd.read_sas('./data/SMQ/SMQ_J.XPT')
    slq = pd.read_sas('./data/SLQ/SLQ_J.XPT')
    hiq = pd.read_sas('./data/HIQ/HIQ_J.XPT')
    paq = pd.read_sas('./data/PAQ/PAQ_J.XPT')
    bmx = pd.read_sas('./data/BMX/BMX_J.XPT')
    huq = pd.read_sas('./data/HUQ/HUQ_J.XPT')
    dbq = pd.read_sas('./data/DBQ/DBQ_J.XPT')

    demo = demo[['SEQN', 'RIDAGEYR', 'RIDRETH1', 'RIDRETH3', 'INDFMPIR']]
    dpq = dpq[['SEQN', 'DPQ020', 'DPQ050']]
    smq = smq[['SEQN', 'SMQ040']]
    slq = slq[['SEQN', 'SLD012']]
    hiq = hiq[['SEQN', 'HIQ011']]
    paq = paq[['SEQN', 'PAQ670']]
    bmx = bmx[['SEQN', 'BMXWT', 'BMXWT']]
    huq = huq[['SEQN', 'HUQ030', 'HUQ010']]
    dbq = dbq[['SEQN', 'DBQ700']]

    df_list = [demo, dpq, smq, slq, hiq, paq, bmx, huq, dbq]

    merge_df = pd.DataFrame(columns=['SEQN'])
    for x in df_list:
        merge_df = pd.merge(merge_df, x, on=['SEQN'], how='outer')

    merge_df.to_csv('./outputs/merge_df.csv', index=False)
    print()