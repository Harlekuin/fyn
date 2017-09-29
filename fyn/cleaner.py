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

    price_df = remove_weekends(price_df)

    check_date_existance(price_df.index.values, start_date=None, end_date=None)

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

def remove_weekends(df):
    """ remove weekend records from supplied dataframe """

    # TODO: assert index is datetime

    df['weekday'] = df.index.weekday
    df = df[-df['weekday'].isin([5, 6])]
    df = df.drop('weekday', axis=1)

    return df


def check_date_existance(date_list, start_date=None, end_date=None, weekend=False):
    """ given a list of dates, check if all exist that should
    weekend bool: whether weekends should be included
    """

    #use the dates given if none specified
    if not start_date:
        start_date = min(date_list)

    if not end_date:
        end_date = max(date_list)

    date_range = pd.date_range(start=start_date, end=end_date)

    cor_df_t = pd.DataFrame(index=date_range)

    cor_df_t['weekday'] = cor_df_t.index.weekday


    if not weekend:
        # remove weekend values
        wkday = lambda x: calendar.day_name[x]

        cor_df_t['weekday_name'] = cor_df_t['weekday'].apply(wkday)


        # TODO: combine these
        cor_df_t.drop(cor_df_t[cor_df_t['weekday_name'] == 'Saturday'].index, inplace=True)
        cor_df_t.drop(cor_df_t[cor_df_t['weekday_name'] == 'Sunday'].index, inplace=True)

    print(cor_df_t)


    # find differences in the date lists
    sup = set(date_list)
    correct = set(cor_df_t.index.values)

    print(sup)
    print('\n-----\n')
    print(correct)

    print("The following dates were supplied but incorrect:\n")
    for my_date in list(sup - correct):
        # print(my_date.date.today())
        print(my_date)

    print("The following dates were not supplied:\n")
    for my_date in list(correct - sup):
        # print(my_date.date.today())
        print(my_date)
