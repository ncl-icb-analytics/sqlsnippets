# Requirements Files in Python Projects

Brief documentation on using requirement.txt in python projects.

## Use Cases ##
* Simple way for people using your code to install all the relevant modules for your code
* Can enable versioning for your code.
  * Prevents people trying to run your code with outdated modules.
  * Prevents people trying to run your code with more recent versions of modules than your code was tested to be compatible with.

## Stanard Use ##
* To install modules using a requirements file, use the following the terminal:
```
pip install -r requirements.txt
```
* When creating a requirements.txt file it should be stored in the root of the project directory
* The format of the requirements.txt file is as follows:
```
pandas==1.5.2
SQLAlchemy==2.0.5.post1
```

* You can automate the creation of the requirements file using pipreqs
```
> pip install pipreqs

> pipreqs
```