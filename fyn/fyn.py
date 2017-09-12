import pandas as pd
from . import loader

def fyn(price_df, income_df=None):
    """
    full process for the analysis
    """

    price_df = loader.load_price_data(price_df)

    if income_df:
        income_df = loader.load_income_data(income_df)

    
