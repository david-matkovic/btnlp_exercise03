import pandas as pd
import re
from textblob import TextBlob


file_path = 'C://Users//dama010//Documents//Miscellanea//All things Python//Neuer Ordner//btnlp_exercise03//twitter_training.csv'
twitter_df = pd.read_csv(file_path)

summary = twitter_df.describe(include='all')
head = twitter_df.head()

pre_df = twitter_df

print(head)
print(summary)

missing_values = pre_df.isnull().sum()

pre_df.fillna('', inplace=True)
print(missing_values)

if pre_df[pre_df.columns[0]].dtype != object:
    pre_df[pre_df.columns[0]] = pre_df[pre_df.columns[0]].astype(str)

for col in pre_df.select_dtypes(include=[object]).columns:
    pre_df[col] = pre_df[col].apply(lambda x: x.lower() if isinstance(x, str) else x)

for col in pre_df.select_dtypes(include=[object]).columns:
    pre_df[col] = pre_df[col].str.replace(r'[^\x00-\x7F]+', ' ', regex=True)

for col in pre_df.select_dtypes(include=[object]).columns:
    pre_df[col] = pre_df[col].str.strip().replace(r'\s+', ' ', regex=True)

print(pre_df.head())


print("HELLO")
print(pre_df.columns)


#regex
def find_mentions(text):
    return re.findall(r'@\w+', text)


pre_df['Borderlands'] = pre_df['Positive'].apply(find_mentions)
print(pre_df.head())



#textblob

pre_df['sentiment'] = pre_df['Positive'].apply(lambda x: TextBlob(x).sentiment.polarity)

print(pre_df.head())