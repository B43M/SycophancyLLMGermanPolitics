import pandas as pd

# import an delete unimportant columns 

# df = pd.read_excel('Data\Wahl-O-Mat Niedersachsen 2022_Datensatz_v1.01.xlsx')
# filtered = df[df['Partei: Nr.'] <= 6]

# filtered.drop(columns=['Position: Begründung'], inplace=True)
# filtered.to_excel('Data\LTWN2022Filtered.xlsx', index=False)


# sort parties to match Ids

# df1 = pd.read_excel('Data\BT2021Filtered.xlsx')
# df2 = pd.read_excel('Data\LTWN2022Filtered.xlsx')
# for party_name in df1['Partei: Kurzbezeichnung'].unique():
#     matching_party_df1 = df1[df1['Partei: Kurzbezeichnung'].str.contains(party_name, case=False, na=False)]

#     matching_id = matching_party_df1['Partei: Nr.'].iloc[0] if not matching_party_df1.empty else None

#     df2.loc[df2['Partei: Kurzbezeichnung'].str.contains(party_name[:3], case=False, na=False), 'Partei: Nr.'] = matching_id
# df2.to_excel('Data\LTWN2022Filtered.xlsx', index=False)


# generate list of questions

def getThese(df):
    theseList = []
    for these in df['These: These'].unique():
        theseList.push(these)
    return theseList

# generate full Questions data

def mergeDfs(df1, df2, df3):
    fixedDf1, count = fixCount(df1)
    fixedDf2, count = fixCount(df2, count)
    fixedDf3, count = fixCount(df3, count)
    
    return pd.concat([fixedDf1, fixedDf2, fixedDf3])    
    
def fixCount(df, count = 0):
    these = ''
    rowcounter = 0
    for i in range(len(df)):
        if (these != df.loc[i, 'These: These']):
            these = df.loc[i, 'These: These']
            count += 1
            df.loc[i, 'These: Nr.'] = count
        else:
            df.loc[i, 'These: Nr.'] = count
        

    return df, count



df1 = pd.read_excel('Data\BT2021Filtered.xlsx')
df2 = pd.read_excel('Data\LTWN2022Filtered.xlsx')
df3 = pd.read_excel('Data\LTWB2023Filtered.xlsx')

fulldf = mergeDfs(df1, df2, df3)

fulldf.to_excel('Data\Fulldata.xlsx', index=False)