# lambdata-aklefebvere

# install from test PyPi:

```sh


 pip install -i https://test.pypi.org/simple/ lambdata-aklefebvere==1.5


 ```

# Usage
## Avaliable Functions from Mod_df class:
```py
# Instansiate class object
df = mod_df(df)
```

 ```py
 # add_col
 from my_lambdata.my_mod import Mod_df
 # creates a new column in a dataframe given a list of values
 df.add_col('Name', ['Connecticut', 'Colorado', 'California', 'Texas'])
 ```

 ```py
 # is_nan
 from my_lambdata.my_mod import Mod_df
 # Checks for nans in the dataframe given to the function
 df.is_nan()
 ```

 ```py
 # split_df
 from my_lambdata.my_mod import Mod_df
 # Splits the dataframe into a 80 | 20 split
 train, test = df.split_df()
 ```