# Bankaya ETL pipeline

This is a script built in Python 3.7 for ETL testing purposes. The main idea is create 1 MARIADB database dynamically , and then create a NoSQL database (MONGODB). After those database are
created , put NoSQL data in to MARIADB and then move to a DWH.All creation scripts (bankaya.sql) for MARIADB and items_data.json and customers_data.json are also provided

## Getting Started

For getting started you have to install or have access to a MARIADB instance locally or remotely or a MONGODB as well.To run in your local machine you must have to change the connections strings some proper changes
in 2 classes. connmaria.py and connmongo.py
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to setup in your environment Python 3.7, mariadb and pymysql.

```
pip install mariadb
pip install pymysql
```

### Installing

You just have to install MariaDB anb MongoDB downlodable from their proper sites.


```

## Authors

* **Israel Gaytan** - *Initial work* - [Isra](https://github.com/isragaytan)

## License

This project has no licensed

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
