from fyn import fyn
import pandas as pd
import os

price_data_file = os.path.join(os.getcwd(), "examples/example_data.xlsx")
income_data_file = os.path.join(os.getcwd(), "examples/example_income.xlsx")

price_data = pd.read_excel(price_data_file, index_col=0)
income_data = pd.read_excel(income_data_file, index_col=0)

analysis = fyn(price_df=price_data, income_df=income_data)

analysis.key_metrics()

print("\nprice dataframe:")
print(analysis.price_df)

print("\nincome dataframe:")
print(analysis.income_df)

print("\nreturn dataframe:")
print(analysis.return_df)

print("\ncovariance matrix:")
print(analysis.covariance_matrix())
