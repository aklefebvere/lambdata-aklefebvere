# lambdata-aklefebvere

# install from test PyPi:

```sh


 pip install -i https://test.pypi.org/simple/ lambdata-aklefebvere==1.5

 ```


# Avaliable Functions from Mod_df class:
```py
df = mod_df(df)
# Instansiate class object
```

 ```py
 # add_col
 from my_lambdata.my_mod import Mod_df

 df.add_col('Name', ['Connecticut', 'Colorado', 'California', 'Texas'])
 # creates a new column in a dataframe given a list of values
 ```

 ```py
 # is_nan
 from my_lambdata.my_mod import Mod_df

 df.is_nan()
 # Checks for nans in the dataframe given to the function
 ```

 ```py
 # split_df
 from my_lambdata.my_mod import Mod_df

 train, test = df.split_df()
 # Splits the dataframe into a 80 | 20 split
 ```