import sqlite3
import pandas as pd
conn = sqlite3.connect('tax_data_test_task/db.sqlite3')


# Import the data to sqlite using pandas
pd.show_versions()
tax_data = pd.read_parquet('test_invoices.parquet')
tax_data.to_sql('api_app_taxdatamodel', conn, if_exists='append', index = False)

# in case we have to drop the data 
# c = conn.execute("DROP TABLE api_app_taxdatamodel")
