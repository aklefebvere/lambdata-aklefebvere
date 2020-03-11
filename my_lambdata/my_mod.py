# Keep global variables away from here
# Keep things within scopes such as function scopes
import pandas as pd
from sklearn.model_selection import train_test_split

class Mod_df():
    def __init__(self, df):
        self.df = df

    def add_col(self, name, vals):
        '''
        Function that creates a new column
        in a dataframe given a list of values
        '''
        self.df[name] = vals

    def is_nan(self):
       '''
       Checks for nan's in all
       series of the given dataframe
       '''
       return self.df.isna().sum()

    def split_df(self):
        '''
        Splits the dataframe into a
        80 | 20 split
        '''
        train, test = train_test_split(self.df, train_size=.80, test_size=.20, random_state=42)
        return train, test

# if __name__ == "__main__":
#    df = pd.DataFrame({"State":["CT", "CO", "CA", "TX"]})
#    df = mod_df(df)
#    df.add_col('Name', ['Connecticut', 'Colorado', 'California', 'Texas'])
#    print(df.df.head())
#    print(df.is_nan())