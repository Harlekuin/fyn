import pandas as pd
import numpy as np
import scipy as sp

class Analysis:

    def __init__(self, price_df, income_df=None):
        self.price_df = price_df
        if income_df:
            self.income_df = income_df

        self.start_date = price_df.index[0]
        self.end_date = price_df.index[-1]

    def key_metrics(self):
        """ used to print a summary of the data of the analysis """

        print("\n--- Key Metrics of Analysis ---\n")

        print("Start Date = {date}".format(date=self.start_date))
        print("End Date = {date}".format(date=self.end_date))

        print("{asset} assets analysed\n".format(asset=len(self.price_df.columns)))

        for asset in self.price_df.columns:
            print(asset + "\n")
            print("Start Price: {price}".format(price=self.price_df.loc[self.start_date, asset]))
            print("End Price: {price}\n\n".format(price=self.price_df.loc[self.end_date, asset]))


    def return_df(self):
        """ create the returns dataframe """

        return self.price_df