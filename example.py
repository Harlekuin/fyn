import fyn
import pandas as pd
import os


with open("examples/example_start.yaml") as f:
    start_date, asset_dict = fyn.loader.load_start_data(f)


price_data_file = os.path.join(os.getcwd(), "examples/example_data.xlsx")
income_data_file = os.path.join(os.getcwd(), "examples/example_income.xlsx")
transaction_data_file = os.path.join(os.getcwd(), "examples/example_transactions.xlsx")


price_data = pd.read_excel(price_data_file, index_col=0)
income_data = pd.read_excel(income_data_file, index_col=0)
transaction_data = pd.read_excel(transaction_data_file, index_col=0)

transacton_data = fyn.cleaner.clean_transaction_data(transaction_data, start_date)

fyn.cleaner.start_assets_vs_price_data(price_data, asset_dict)

price_data = fyn.cleaner.clean_price_data(price_data)

start_date = fyn.cleaner.start_date_vs_price_data(price_data, start_date)

print("The final start date is:")
print(start_date)

value_df, unit_df = fyn.transformer.units_by_date(
    start_date=start_date,
    asset_dict=asset_dict,
    transaction_df=transaction_data,
    price_df=price_data
)


# value_df = fyn.loader.value_dataframe(price_data, start_date, asset_dict)

print("The portfolio value dataframe:")
print(value_df)

print("The unit count dataframe:")
print(unit_df)

analysis = fyn.fyn(price_df=price_data, income_df=income_data)

analysis.key_metrics()

print("\nprice dataframe:")
print(analysis.price_df)

print("\nincome dataframe:")
print(analysis.income_df)

print("\nreturn dataframe:")
print(analysis.return_df)

print("\ncovariance matrix:")
print(analysis.covariance_matrix())
