"""load price data into a dataframe, and pass to load_price_data"""

import pandas as pd
import numpy as np
import yaml

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


def load_return_data(price_df, income_df=None):
    """
    load a dataframe from price and income data.
    returns a dataframe of returns
    if income data is supplied, the returns are modified
    """

    return_df = price_df.pct_change() * 100

    if income_df is not None:

        for asset in income_df.columns:

            if asset in price_df.columns:

                for date, income_amt in income_df.iterrows():

                    if not pd.isnull(income_amt[asset]):

                        # get the price at the date of the income payment
                        price = price_df.loc[date, asset]

                        # find the integer location of the previous index
                        previous_day_int = price_df.index.get_loc(date) - 1
                        previous_days_price = price_df[asset].iloc[previous_day_int]

                        actual_return = (income_amt[asset] + price - previous_days_price) / previous_days_price * 100

                        return_df.loc[date, asset] = actual_return

        return return_df

def load_start_data(start_yaml):
    """
    load a yaml string with a start date and asset units held on that date.
    Can be nothing.
    """

    start_yaml = yaml.load(start_yaml)
    return start_yaml['date'], start_yaml['assets']


def value_dataframe(price_df, start_date, asset_dict):
    """
    return a dataframe tracking the total value of the portfolio using
    prices and units through the dates
    """

    assert('portfolio_value' not in price_df.columns)

    value_df = price_df.copy()

    # remove dates earlier than the start date
    value_df = value_df[start_date:]

    # multiply by the starting units
    value_df = value_df.mul(pd.Series(asset_dict), axis=1)

    # add the a portfolio value column
    value_df['portfolio_value'] = value_df.sum(axis=1)

    return value_df


def load_transactions(transaction_df):
    """
    load transactions into a dataframe
    """

    return transaction_df
