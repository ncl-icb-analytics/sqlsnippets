# NCL SQLSnippets

This is a python module adding a standard set of functions to interact with the sandpit

- [NCL SQLSnippets](#ncl-sqlsnippets)
  - [History](#history)
    - [\[1.0\] - 10/07/2023](#10---10072023)
    - [\[1.1\] - 10/08/2023](#11---10082023)
    - [\[1.2\] - 06/12/2023](#12---06122023)
    - [\[1.3\] - 12/01/2024](#13---12012024)
  - [Installation](#installation)
  - [Standard Use](#standard-use)
  - [Functions](#functions)
    - [get\_connection\_string](#get_connection_string)
    - [connect\_to\_sql](#connect_to_sql)
    - [connect](#connect)
    - [upload\_to\_sql](#upload_to_sql)
    - [list\_all\_tables](#list_all_tables)
    - [table\_exists](#table_exists)
    - [backup\_table](#backup_table)
    - [restore\_table](#restore_table)
    - [list\_all\_columns](#list_all_columns)
    - [columns\_exist](#columns_exist)
    - [execute\_query](#execute_query)
    - [execute\_sfw](#execute_sfw)
    - [generate\_session](#generate_session)
    - [execute\_query\_session](#execute_query_session)
    - [commit\_changes](#commit_changes)
  - [License](#license)


## History ##
### [1.0] - 10/07/2023 ###
* Initial set of functions
* Instructions for installing as a module

### [1.1] - 10/08/2023 ###
* Added connect function

### [1.2] - 06/12/2023 ###
* Converted to project (https://pypi.org/project/ncl-sqlsnippets/1.2.0/)

### [1.3] - 12/01/2024 ###
* Added functionality for manual commits through new functions
* generate_session, execute_query_session, commit_changes functions added

## Installation

* As of v1.2.0 the sql snippets module can be install through pip
```
pip install ncl_sqlsnippets
```

## Standard Use

* In your other python and notebook files you can add the sqlsnippets module like any other standard module.

```python
import ncl_sqlsnippets as snips
```

* Likewise functions from sqlsnippets can be called like functions from any standard module

```python
#Build connection string
conn_str = snips.get_connection_string(SQL_ADDRESS, SQL_DATABASE)

#Connect to database
engine = snips.connect_to_sql(conn_str=conn_str)

#Upload data
snips.upload_to_sql(data, engine, SQL_TABLE, SQL_SCHEMA, replace=False)
```

## Functions



### get_connection_string
```python
get_connection_string (server_addres, database, server_type="mssql", driver="SQL+Server")
```
Returns a connection string for the sandpit.

**Parameters:**

* **server_address**: _str_ \
The server name of the database. It can be found in the Connect to Server pop-up when openning MS SQL Server Management Studio.

* **database**: _str_ \
Name of the database. 

* **server_type**: _str_ \
Type of SQL server. Does not need to be set unless we ever migrate from MS SQL.

* **driver**: _str_ \
Driver for the SQL server. Does not need to be set unless we ever migrate from MS SQL.

**Returns**: _str_ \
Connection string to establish the connection in the connect_to_sql function.



### connect_to_sql
```python
connect_to_sql (conn_str)
```
Takes a connection string and returns a connection to the database in the form of an engine. 

**Parameters:**

* **conn_str**: _str_ \
Connection string. 

**Returns**: _engine_ \
Connection to the database. Store this in a variable and use it as a parameter in the other sqlsnippets functions.



### connect
```
connect (server_address, database)
```
Wrapper for the main connection functions. Returns the engine connection object.

**Parameters:**
* **server_address**: _str_ \
The server name of the database. It can be found in the Connect to Server pop-up when openning MS SQL Server Management Studio.

* **database**: _str_ \
Name of the database. 



### upload_to_sql
```python
upload_to_sql (data, engine, table, schema, replace, chunks=100, dtypes={})
```
Takes data and uploads it to a target table in the database. If the table does not exist it will be created.

**Parameters:**

* **data**: _DataFrame_ \
Data to upload in the form of a pandas data frame.

* **engine**: _engine_ \
Engine object from the connect_to_sql function.

**table**: _str_ \
Name of the table in the database.

**schema**: _str_ \
Name of the schema in the database (this should either be "dbo" or your BLUE account prefix in most cases).

**replace**: _Boolean_ \
If set to True, this function will replace any existing data in the table. If set to False it will append the data instead. \
**Warning: This will drop the original table when set to True**

**chunks**: _int_ \
This specifies the block size for data being uploaded. Generally bigger blocks means faster uploads. The function will fail if the block size exceeds the maximum limit for MS SQL (2100). As a rule of thumb, this figure should not exceed 2100/(number of columns).

**dtypes**: _dict_ \
Optional parameter to specify the types of the data columns, useful for specifying when a column should be intrepretted by the server as a date value. You can choose to only specify the type for a subset of the columns.
```python
dtypes = {
    "date" : types.Date
}
```
A list of dtype values recognised by the function are listed here: https://docs.sqlalchemy.org/en/20/core/type_basics.html

**Returns**: _None_



### list_all_tables
```python
list_all_tables (engine)
```
Lists all tables in a database. This will use the database specified in the connection string used.

**Parameters:**

* **engine**: _engine_ \
Engine object from the connect_to_sql function.

**Returns**: _DataFrame_ \
Returns a database with the following columns: SchemaName, TableName.



### table_exists
```python
table_exists (engine, table, schema)
```
Checks if a given table exists in the database. The schema for the table needs to be provided as well.

**Parameters:**

* **engine**: _engine_ \
Engine object from the connect_to_sql function.

**table**: _str_ \
Name of the table in the database.

**schema**: _str_ \
Name of the schema in the database (this should either be "dbo" or your BLUE account prefix in most cases).

**Returns**: _Boolean_ \
Returns True if [schema].[table] exists in the database.



### backup_table
```python
backup_table (engine, table, schema)
```
Creates a backup of the specified table ([database].[schema].[table]). The backup table will have the same name as the original but with "_backup" as a suffix.

**Parameters:**

* **engine**: _engine_ \
Engine object from the connect_to_sql function.

**table**: _str_ \
Name of the table in the database.

**schema**: _str_ \
Name of the schema in the database (this should either be "dbo" or your BLUE account prefix in most cases).

**Returns**: _None_ \



### restore_table
```python
restore_table (engine, table, schema)
```
Replaces the table specified ([database].[schema].[table]) and replaces it with the backup table. Any table with the same name as the specified table but with "_backup" as a suffix to the table name will be considered to be the backup table.

**Parameters:**

* **engine**: _engine_ \
Engine object from the connect_to_sql function.

**table**: _str_ \
Name of the table in the database.

**schema**: _str_ \
Name of the schema in the database (this should either be "dbo" or your BLUE account prefix in most cases).

**Returns**: _None_ \



### list_all_columns
```python
list_all_columns (engine, table, schema)
```
Lists all columns for a given table. This will use the database specified in the connection string used.

**Parameters:**

* **engine**: _engine_ \
Engine object from the connect_to_sql function.

**table**: _str_ \
Name of the table in the database.

**schema**: _str_ \
Name of the schema in the database (this should either be "dbo" or your BLUE account prefix in most cases).

**Returns**: _Series_ \
Returns a list of columns in the table in the form of a pandas Series.



### columns_exist
```python
columns_exist (engine, table, schema, columns)
```
Checks if given columns exists in the specified table. The schema for the table needs to be provided as well.

**Parameters:**

* **engine**: _engine_ \
Engine object from the connect_to_sql function.

**table**: _str_ \
Name of the table in the database.

**schema**: _str_ \
Name of the schema in the database (this should either be "dbo" or your BLUE account prefix in most cases).

**Returns**: _Array_ \
Returns a list of all missing columns. \
**Warning: If all columns exist in the table then this returns an empty list which can be logically treated as False.**



### execute_query
```python
execute_query (engine, query)
```
Executes a generic query. For queries where you expect rows to be returned use execute_sfw().
**Warning: This function commits changes to the database at the end of every call.**

**Parameters:**

* **engine**: _engine_ \
Engine object from the connect_to_sql function.

**query**: _str_ \
The query to execute as a string

**Returns**: _None_ \



### execute_sfw
```python
execute_sfw (engine, query)
```
Executes a Select From Where query. The function is for queries where you expect a response to process, for other queries use execute_query().

**Parameters:**

* **engine**: _engine_ \
Engine object from the connect_to_sql function.

**query**: _str_ \
The query to execute as a string

**Returns**: _DataFrame_ \
The query result is returned as a pandas data frame.



### generate_session
```
session, transaction = generate_session(engine)
```
Generates a session object. Non-sfw queries can be executed with it without auto-committing the result.

**Parameters:**

* **engine**: _engine_ \
Engine object from the connect_to_sql function.

**Returns**: _Session_, _Transaction_ \
The generated session along with a transaction object are returned



### execute_query_session
```
execute_query_session(query, session)
```
Executes a non-sfw query. This will not commit changes.

**Parameters:**

* **query**: _str_ \
SQL query command as string

* **session**: _session_ \
Session object from the generate_session function.



### commit_changes
```
commit_changes(transaction)
```
Commits changes made during a session.

**Parameters:**

* **transaction**: _transaction_ \
Transaction object from the generate_session function.

## License
This repository is dual licensed under the [Open Government v3](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) & MIT. All code can outputs are subject to Crown Copyright.
