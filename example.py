from fyn import fyn
import pandas as pd
import os

price_data_file = os.path.join(os.getcwd(), "examples/example_data.csv")
income_data_file = os.path.join(os.getcwd(), "examples/example_income.csv")

# price_data = pd.read_csv(".\examples\example_data.csv", index_col=0)
price_data = pd.read_csv(price_data_file, index_col=0)
income_data = pd.read_csv(income_data_file, index_col=0)

analysis = fyn(price_df=price_data, income_df=income_data)

analysis.key_metrics()

print(analysis.price_df)
print(analysis.income_df)
print(analysis.return_df)

print(analysis.covariance_matrix())
