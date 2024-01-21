import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt

class TwitterDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        self.df.fillna('', inplace=True)
        return self.df.head()
    
    def clean_data(self):
        pass

    def add_text_features(self):
        self.df['Positive'] = self.df['Borderlands'].fillna('')
        self.df['hashtag_count'] = self.df['Positive'].apply(lambda x: len(re.findall(r'#\w+', x)))
        vectorizer = TfidfVectorizer(max_features=10)
        self.tfidf_matrix = vectorizer.fit_transform(self.df['Positive'].values.astype('U'))
        self.df['tweet_length'] = self.df['Positive'].apply(len)
        return self.df.head()

    def plot_histogram(self):  
        ''' distribution of tweet lengths'''
        
        plt.figure(figsize=(10, 5))
        plt.hist(self.df['tweet_length'].dropna(), bins=30, color='blue', edgecolor='black')
        plt.title('Distribution of Tweet Lengths')
        plt.xlabel('Tweet Length')
        plt.ylabel('Frequency')
        plt.show()
    
#  regex feature
    def apply_regex_feature(self):
      
        self.df['mentioned_usernames'] = self.df['Positive'].apply(lambda x: re.findall(r'@\w+', x))
        return self.df.head()
    

processor = TwitterDataProcessor('C://Users//dama010//Documents//Miscellanea//All things Python//Neuer Ordner//btnlp_exercise03//twitter_training.csv')
processor.load_data()
processor.add_text_features()
processor.apply_regex_feature()
processor.plot_histogram()



'''
I'd use child classes when I wanted to inherit some functionalities of a parent class,
which would allow me to reuse a code without modification.
Moreover, I'd use them when I wanted to create a more specific version of the parent class that is targeted to a particular use case.
And they also help you organize your code by creating a hierarchy of classes that share common functionality
'''