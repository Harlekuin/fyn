"""load price data into a dataframe, and pass to load_price_data"""

import pandas as pd

def load_price_data(price_df):
    """
    load price_df
    """

    price_df.index = pd.to_datetime(price_df.index)

    return price_df

def load_income_data(income_df):
    """
    load income_df
    """

    income_df.index = pd.to_datetime(income_df.index)

    return income_df
