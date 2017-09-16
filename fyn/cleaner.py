""" check and clean dataframes """
from .config import FILL_MISSING_PRICES
import pandas as pd
from datetime import date, timedelta
import calendar


def clean_price_data(price_df):
    """clean price data"""

    assert isinstance(price_df, pd.DataFrame)

    """
    TODO:
        check index for correct datetimes
        fill in missing values
    """

    print(price_df)

    # date index checking
    if not check_weekends(price_df.index.values):
        print("Weekends present in data!")

    # check_date_existance(price_df.index.values, start_date=None, end_date=None)

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

    # hacky way
    temp_df = pd.DataFrame(index=date_list)
    temp_df['weekday'] = temp_df.index.weekday
    weekdays = temp_df['weekday'].values

    for my_day in weekdays:
        if calendar.day_name[my_day] in ['Saturday', 'Sunday']:
            return False

    return True


def check_date_existance(date_list, start_date=None, end_date=None):
    """ given a list of dates, check if all exist that should
    weekend bool: whether weekends should be included
    """

    #use the dates given if none specified
    if not start_date:
        start_date = min(date_list)

    if not end_date:
        end_Date = max(date_list)

    # create the list of correct dates
    delta = end_date - start_date

    correct_date_list = []

    for i in range(delta.days + 1):
        correct_date_list.append(d1 + timedelta(days=i))

    """if not weekend:
        correct_date_list = [
            my_date for my_date in correct_date_list
            if not calendar.day_name[my_date.dt.dayofweek] in ['Saturday', 'Sunday']
        ]"""


    # find differences in the date lists
    sup = set(date_list)
    correct = set(correct_date_list)

    print("The following dates were supplied but incorrect:\n")
    for my_date in list(sup - correct):
        print(my_date.date.today())

    print("The following dates were not supplied:\n")
    for my_date in list(correct - sup):
        print(my_date.date.today())
