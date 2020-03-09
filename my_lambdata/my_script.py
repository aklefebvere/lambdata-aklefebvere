import pandas as pd

from my_lambdata.my_mod import add_col
from my_lambdata.my_mod import is_nan

df = pd.DataFrame({"State":["CT", "CO", "CA", "TX"]})

add_col(df, 'Name', ['Connecticut', 'Colorado', 'California', 'Texas'])


print(is_nan(df))


print(df.head())

