# Bankaya ETL pipeline

This is a script built in Python 3.7 for ETL testing purposes. The main idea is to create code to automate the following process:
1. Create a SQL Database with the following tables:

- CUSTOMER This table will contain a primary key as well as the customers first and last names, phone number, curp, rfc and address information.
- ITEMS This table will contain a primary key, item name and item price.
- ITEMS_BOUGHT This table will contain order number, price, comments and primary keys in the ITEM and CUSTOMER tables.

2. Create a NoSQL Database with the following structure:

```
[{"title":"USB","price":10.2},
 {"title":"Mouse","price":12.23},
 {"title":"Monitor","price":199.99}]
 
```

3. Extract information from both origins to any DWH (BigQuery)


## Getting Started

For getting started you have to install or have access to a MARIADB instance locally or remotely or a MONGODB as well.For access to a Datawarehouse in this case we will use Google Bigquery.It is highly recomended to get some credentials and access to Bigquery to run properly the script.To run in your local machine you must have to change the connections strings in the following classes:

1. connmaria.py 

```
def __init__(self,db=None):
        #NOT RECOMENDAABLE THIS LINE ITS BETTER TO KEEP IN AN A OS ENVIRONMENT FOR HIDE CREDENTIALS OR IN VAULT
        #self._conn = mariadb.connect(os.environ["CREDENTIALS"])
        #JUST FOR DEMO PURPOSES DONT PUT THIS LINE IN PRODUCTION!
        self._conn = mariadb.connect(user="xxx",password="xxx",host="xxx",database=db)
        self._cursor = self._conn.cursor()
 
```



2. connmongo.py

```
def __init__(self):
        _client = MongoClient('localhost', 27017)
        self.db = _client['bankaya']
 
```

3. Google Service Account
If you don’t have a service account,[follow this guide to create one](https://cloud.google.com/iam/docs/creating-managing-service-accounts), and then proceed to download the JSON file to your local machine to interact with BigQuery.

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to setup in your environment Python 3.7 and download the following libraries mariadb,mongodb and google-cloud-bigquery.

```
pip install mariadb
pip install pymongo
pip install google-cloud-bigquery

```
Also if you prefer we provided a requirements.txt for all libraries just type in your terminal:

```
pip install -r requirements.txt

```

### Installing

When you are done with the earlier steps you just have to run in your terminal:


```
python createdb.py

```
The SQL creation data for the MariaDB is on the file bankaya.sql
The jsons for the collections for the MongoDB (NoSQL) are customers_data.json,items_data.json and items_bought_data.json
You will see messages if you did it well or error messages saying what is wrong. Please always check your connections strings configured properly.

## Authors

* **Israel Gaytan** - *Initial work* - [Isra](https://github.com/isragaytan)

## License

This project has no licensed

## Acknowledgments

* Thanks to bankaya for this funny test.

