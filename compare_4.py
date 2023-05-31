import pandas as pd

df_2020 = pd.read_csv('sunshine_2020.csv')
df_2022 = pd.read_csv('sunshine_2022.csv')

df_merged = pd.merge(df_2022, df_2020, on=['Sector', 'Last Name', 'First Name', 'Employer'], how='left', suffixes=('_2022', '_2020'))

# df_merged.to_csv('sunshine_difference_1.csv', index=False)

df_merged['Salary_2020'].fillna(0, inplace=True)
df_merged['Salary Difference'] = df_merged['Salary_2022'] - df_merged['Salary_2020']
df_merged.loc[df_merged['Salary_2020'] == 0, 'Salary Difference'] = 0

# df_merged.to_csv('sunshine_difference_2.csv', index=False)
df_merged['Job Title_2020'].fillna("new", inplace=True)
df_merged['Job Change'] = df_merged['Job Title_2022'] != df_merged['Job Title_2020']
df_merged['Job Change'] = df_merged['Job Change'].replace({True: 'Yes', False: 'No'})
df_merged.loc[df_merged['Job Title_2020'] == 'new', 'Job Change'] = 'New'

if df_merged['Job Title_2020'].empty:
    df_merged['Job Change'] = "New"

df_merged.to_csv('sunshine_difference.csv', index=False)
