
# my_mod_test.py


import unittest
import pandas as pd

from my_lambdata.my_mod import Mod_df

df = pd.DataFrame({"State": ["CT", "CO", "CA", "TX"]})
df = Mod_df(df)


class TestMyMod(unittest.TestCase):

    def test_add_col(self):
        df.add_col('Name', ['Connecticut', 'Colorado', 'California', 'Texas'])
        self.assertTrue('Name'in df.df.columns.tolist())

    def test_is_nan(self):
        self.assertTrue(isinstance(df.df.isna().sum(), pd.Series))

    def test_split_df(self):
        train, test = df.split_df()
        self.assertTrue(type(train), pd.DataFrame)
        self.assertTrue(type(test), pd.DataFrame)


if __name__ == '__main__':
    unittest.main()
