from fyn import fyn
import pandas as pd

price_data = pd.read_csv(".\examples\example_data.csv", index_col=0)

analysis = fyn(price_df=price_data)

analysis.key_metrics()

print(analysis.price_df)
print(analysis.return_df)

print(analysis.covariance_matrix())
