""" check and clean dataframes """
from .config import FILL_MISSING_PRICE
import pandas as pd


def clean_income_data(price_df):
    """clean price data"""

    assert isinstance(price_df, pd.dataframe)

    """
    TODO:
        check index for correct datetimes
        fill in missing values

    """

    return price_df



def clean_income_data(income_df):
    """clean income data"""

    assert isinstance(income_df, pd.dataframe)

    """
    TODO:
        check index for correct datetimes

    """

    return income_df
