import pandas as pd
import numpy as np
from .loader import load_return_data

class Analysis:

    def __init__(self, price_df, income_df=None):
        self.price_df = price_df
        if income_df is not None:
            self.income_df = income_df

        self.start_date = price_df.index[0]
        self.end_date = price_df.index[-1]

        self.return_df = load_return_data(self.price_df, self.income_df)


    def key_metrics(self):
        """ used to print a summary of the data of the analysis """

        print("\n--- Key Metrics of Analysis ---\n")

        print("Start Date = {date}".format(date=self.start_date))
        print("End Date = {date}".format(date=self.end_date))

        print("\n{asset} assets analysed\n".format(asset=len(self.price_df.columns)))

        for asset in self.price_df.columns:
            print('-- ' + asset + ' --')
            print("Start Price: ${price:.2f}".format(price=self.price_df.loc[self.start_date, asset]))
            print("End Price: ${price:.2f}\n".format(price=self.price_df.loc[self.end_date, asset]))

            if asset in self.income_df.columns:
                print("Total Income for " + asset + ":")
                print("${income:.2f}\n".format(income=self.income_df[asset].sum()))

            # add income and returns


    def return_data(self):
        """ create the returns dataframe in percent """

        return self.price_df.pct_change() * 100

    def covariance_matrix(self):
        """ covariance matrix """

        return self.return_df.cov()
