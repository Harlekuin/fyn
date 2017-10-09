"""load price data into a dataframe, and pass to load_price_data"""

import pandas as pd
import numpy as np

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

    print("the price data is:")
    print(price_df)
    print("the return dataframe is:")
    print(return_df)
    print("the income data is:")
    print(income_df)

    if income_df is not None:
        # modify the return data frame

        for asset in income_df.columns:
            print("asset {asset} found in income_df".format(asset=asset))

            if asset in price_df.columns:
                for date, income_amt in income_df.iterrows():

                    if not pd.isnull(income_amt[asset]):

                        print(
                            "asset {asset} has an income of {amt} on the date {date}".format(
                                asset=asset,
                                amt=income_amt[asset],
                                date=date))

                        # get the price at the date of the income payment
                        print('working with date ' + str(date))

                        price = price_df.loc[date, asset]

                        print("asset {asset} had a price of {price} on that date".format(asset=asset, price=price))

                        previous_day_int = price_df.index.get_loc(date) - 1
                        print("the int index of the previous day is {x}".format(x=previous_day_int))

                        # previous_days_price = price_df.iloc[previous_day_int, asset]
                        previous_days_price = price_df[asset].iloc[previous_day_int]

                        print("asset {asset} had a price of {price} on the previous date".format(asset=asset, price=previous_days_price))

                        # actual_return = (price + income_amt[asset])/previous_days_price

                        actual_return = (income_amt[asset] + price - previous_days_price) / previous_days_price * 100

                        print(
                            "the recorded return was {ret}, however this is being overridden by the actual return of {actual_return}".format(
                                ret=return_df.loc[date, asset],
                                actual_return=actual_return))

                        return_df.loc[date, asset] = actual_return


        print("the final return dataframe is:")
        print(return_df)
        return return_df
