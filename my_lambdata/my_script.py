import pandas as pd
from sklearn.model_selection import train_test_split


from my_lambdata.my_mod import Mod_df

df = pd.DataFrame({"State": ["CT", "CO", "CA", "TX"]})

df = Mod_df(df)

df.add_col('Name', ['Connecticut', 'Colorado', 'California', 'Texas'])

train, test = df.split_df()
type(df.df.isna().sum())
print(train.shape, test.shape)