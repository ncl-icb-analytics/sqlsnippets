import ncl.sqlsnippets as snips

#SQL Address
SQL_ADDRESS = ""
#SQL Database
SQL_DATABASE = ""
#SQL Schema (default "dbo")
SQL_SCHEMA = ""
#SQL Table name
SQL_TABLE = ""

#Get conn_str
conn_str = snips.get_connection_string(SQL_ADDRESS, SQL_DATABASE)

#Connect to the SQL server
engine = snips.connect_to_sql(conn_str)

snips.backup_table(engine, SQL_TABLE, SQL_SCHEMA)
#snips.restore_table(engine, SQL_TABLE, SQL_SCHEMA)