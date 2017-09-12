import fyn
import pandas as pd

price_data = pd.read_csv("pricedata.csv", index_col=0)

analysis = fyn.fyn(price_df=price_data)

analysis.key_metrics()
