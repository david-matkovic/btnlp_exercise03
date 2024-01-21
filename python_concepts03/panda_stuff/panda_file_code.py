import pandas as pd

df = pd.read_csv(
    r'C:\Users\dama010\Documents\Miscellanea\All things Python\Neuer Ordner\btnlp_exercise03\panda_file.csv',
    low_memory=False
)


for column in df.columns:

    if df[column].dtype == float: 
        df[column].fillna(0, inplace=True)

    elif df[column].dtype == object:
        df[column].fillna('Unknown', inplace=True)


if 'zip_code' in df.columns:
    df['zip_code'] = df['zip_code'].apply(lambda x: str(int(x)).zfill(5) if pd.notnull(x) else x)


pseudo_nans = ['N/A', 'None', 'NaN']
df.replace(pseudo_nans, 'Unknown', inplace=True)

if 'zip_code' in df.columns:
    df['zip_code'] = df['zip_code'].astype(str)


df.to_csv(r'C:\Users\dama010\Documents\Miscellanea\All things Python\Neuer Ordner\btnlp_exercise03\cleaned_panda_file.csv', index=False)
