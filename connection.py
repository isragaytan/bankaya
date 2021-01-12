import mariadb
import logging
import os


class MariaDB:
    """Class to connect to Mariadb"""
    def __init__(self):
        #NOT RECOMENDAABLE THIS LINE. ITS BETTER TO KEEP IN AN A OS ENVIRONMENT FOR HIDE CREDENTIALS OR IN VAULT
        #self._conn = mariadb.connect(os.environ["CREDENTIALS"])
        #JUST FOR DEMO PURPOSES DONT PUT THIS LINE IN PRODUCTION
        self._conn = mariadb.connect(user="root",password="13Shaila1@",host="localhost")
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()