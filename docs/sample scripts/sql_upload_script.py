import ncl.sqlsnippets as snips
import pandas as pd

#SQL Address
SQL_ADDRESS = ""
#SQL Database
SQL_DATABASE = ""
#SQL Schema (default "dbo")
SQL_SCHEMA = ""
#SQL Table name
SQL_TABLE = ""

#Path to data csv file
DATA_SOURCE = ""

#Get conn_str
conn_str = snips.get_connection_string(SQL_ADDRESS, SQL_DATABASE)

#Connect to the SQL server
engine = snips.connect_to_sql(conn_str)

data = pd.read_csv(DATA_SOURCE)

snips.upload_to_sql(data, engine, SQL_TABLE, SQL_SCHEMA, False)