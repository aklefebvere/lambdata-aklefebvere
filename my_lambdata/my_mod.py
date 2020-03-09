
# Keep global variables away from here
# Keep things within scopes such as function scopes


def add_col(df, name, vals):
   '''
   Function that creates a new column
   in a dataframe given a list of values
   '''
   df[name] = vals
   
def is_nan(df):
    '''
    Checks for nan's in all
    series of the given dataframe
    '''
    return df.isna().sum()