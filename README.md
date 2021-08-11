# Data engineering assignment at DataChef

This is the repository of the assignment for the data engineering position at DataChef.

The solution is tested with Python 3.9 and PostgreSQL 12.

The repository does not contain the csv files and images. Please extract/copy the images to 'flaskr/static/images/' and import the data into DB using the 'import_quarter.py' script.

# Installation
The '.devcontainer' folder would help you set up the application in VSCODE with the help of the 'Remote Containers" plugin. If you prefer to not use VSCODE, consult the the files in '.devcontainer' folder. The application needs a PostgreSQL instance available at '127.0.0.1:5432'.

## Usage

### Initialize the DB schema
``` bash
$ flask init-db
```

### Importing data
To import csv data:
``` bash
$ python import_quarter.py -f <folder> -q <quarter>
```

For Example:
``` bash
$ python import_quarter.py -f ./csv/4 -q 4
```

### Run the application
``` bash
$ flask run
```

### Stress test
``` bash
$ python stresstest_script.py
```
