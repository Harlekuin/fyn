import pandas as pd
from .loader import load_price_data, load_income_data
from .cleaner import clean_price_data, clean_income_data

def fyn(price_df, income_df=None):
    """
    full process for the analysis
    """

    # load dataframes
    price_df = load_price_data(price_df)

    if income_df:
        income_df = load_income_data(income_df)

    # clean dataframes
    price_df = clean_price_data(price_df)

    if income_df:
        income_df = clean_income_data(income_df)
