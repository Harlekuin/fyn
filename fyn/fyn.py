import pandas as pd
import numpy as np

from .loader import load_price_data, load_income_data
from .cleaner import clean_price_data, clean_income_data
from .transformer import transform_price_data, transform_income_data
from .analyse import Analysis


def fyn(price_df, income_df=None):
    """
    full process for the analysis
    """

    # save copies of the original raw data
    raw_price_df = price_df.copy(deep=True)
    if income_df:
        raw_income_df = income_df.copy(deep=True)
    else:
        raw_income_df = None


    # load dataframes
    price_df = load_price_data(price_df)

    if income_df:
        income_df = load_income_data(income_df)

    # clean dataframes
    price_df = clean_price_data(price_df)

    if income_df:
        income_df = clean_income_data(income_df)

    # transform dataframes
    price_df = transform_price_data(price_df)

    if income_df:
        income_df = transform_income_data(income_df)

    return Analysis(price_df=price_df, income_df=income_df)
