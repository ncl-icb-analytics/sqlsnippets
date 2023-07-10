# Using env Variables

Brief documentation on using environment variables in python projects.

## Use cases ##
* Allows code repos to be published without including sensitive information like the sandpit sql address
* Allows for code that can be run with multiple settings to not have settings hardcoded into the repo. Avoids changes to settings for individual executions being tracked in the git history.

## Standard Use ##
* Install the dotenv module:

```
pip install python-dotenv
```

* In your project directory create a env file called ".env"
  
* Make sure the .env file is listed in the .gitignore file for the project. You can create a sample version of the .env file as documentation for people who use your code from github.

* Add envirnoment variables to the .env file with the following format:
```python
SOURCEDIR = "./data/"
OUTPUTDIR = "./output/"
```
* In your python file, import the following functions to extract variable values from your .env file:

```python
from os import getenv
from dotenv import load_dotenv
```
* Call load_dotenv and then use getenv to load values into variables in your file:

```python
load_dotenv(override=True)

SOURCEDIR = getenv("SOURCEDIR")
OUTPUTDIR = getenv("OUTPUTDIR")

print(SOURCEDIR)
> "./data/"
```

* When calling load_dotenv, setting override to True will allow the environment variable values to be overwritten when the code is re-executed. By default, the environment variables will preserve their original value from the first execution of the code.

* By default, all env variables are strings. If you want to use numbers or Boolean values in the env file, convert them to the desired data type when you import the values into your python file.

```python
#In the .env file
#Notice the lack of ""

SQL_CHUNKSIZE = 100
SQL_DTYPES = True
```
```python
#In the python file

from os import getenv
from dotenv import load_dotenv
import json

#For ints
SQL_CHUNKSIZE = int(getenv("SQL_CHUNKSIZE")),
#For Boolean (needs the json module)
SQL_DTYPES = json.loads(getenv("SQL_DTYPES").lower()),
```

