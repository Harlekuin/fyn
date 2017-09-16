""" check and clean dataframes """
from .config import FILL_MISSING_PRICES
import pandas as pd
from datetime import date
import calendar


def clean_price_data(price_df):
    """clean price data"""

    assert isinstance(price_df, pd.DataFrame)

    """
    TODO:
        check index for correct datetimes
        fill in missing values
    """

    return price_df



def clean_income_data(income_df):
    """clean income data"""

    assert isinstance(income_df, pd.DataFrame)

    """
    TODO:
        check index for correct datetimes
    """

    return income_df

def check_weekends(date_list):
    """ given a list of dates, check if any are weekends """

    for my_date in date_list:
        if calendar.day_name[my_date.weekday()] in ['Saturday', 'Sunday']:
            return False

    return True
