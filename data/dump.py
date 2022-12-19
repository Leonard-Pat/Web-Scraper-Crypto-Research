import pandas as pd
import sqlite3
import os



cwd = os.getcwd()
db_path = os.path.join(cwd, "database/clean_data.db")

db_connection = sqlite3.connect(db_path)
cursor = db_connection.cursor()

# read the data from the database table into a DataFrame
df = pd.read_sql("SELECT * FROM treasury", db_connection)

# export the DataFrame to an Excel file
df.to_excel("treasury_clean.xlsx", index=False)

# read the data from the database table into a DataFrame
df = pd.read_sql("SELECT * FROM proposals_on_chain", db_connection)

# export the DataFrame to an Excel file
df.to_excel("proposals_on_chain_clean.xlsx", index=False)

# read the data from the database table into a DataFrame
df = pd.read_sql("SELECT * FROM information", db_connection)

# export the DataFrame to an Excel file
df.to_excel("information_clean.xlsx", index=False)

# read the data from the database table into a DataFrame
df = pd.read_sql("SELECT * FROM governance_on_chain", db_connection)

# export the DataFrame to an Excel file
df.to_excel("governance_on_chain_clean.xlsx", index=False)