""" transform dataframes to preferred format """

import pandas as pd

def transform_price_data(price_df):
    """transform price data"""

    return price_df



def transform_income_data(income_df):
    """transform income data"""

    return income_df


def units_by_date(start_date, asset_dict, transaction_df, price_df):
    """
    calculate a dataframe, index of date, columns of assets, that has
    units at each date (from price_df.index)
    """

    # create the starting skeleton of the dataframe we will fill
    unit_df = pd.DataFrame(
        columns = price_df.columns,
        index = price_df.index
    )

    unit_df = unit_df[start_date:]


    # add the starting value to every cell
    for asset in unit_df.columns:
        if not asset in asset_dict.keys():
            asset_dict[asset] = 0

        unit_df[asset] = asset_dict[asset]


    # iterate through transactions and apply to all dates after
    for date, transaction in transaction_df.iterrows():
        if date.date() >= start_date:
            unit_df.loc[date:, transaction['asset']] += transaction['quantity']
            
    value_df = price_df[start_date:] * unit_df

    value_df['portfolio_value'] = value_df.sum(axis=1)

    return value_df, unit_df
