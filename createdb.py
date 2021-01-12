import logging
import mariadb
import json
from connmaria import MariaDB
from connmongo import MongoDB

#Start creating the MySQL with Initial Scripts DataBase

def execute_sql(filename):
    sql_to_read=open(filename,'r')
    sql_file= sql_to_read.read()
    sql_to_read.close()

    sql_commands = sql_file.split(";")
    conn = MariaDB()
    for cmds in sql_commands:
        #print(cmds)
        try:
            conn.execute(cmds)
        except mariadb.Error as e:
            print(f"Error:{e}")


#Start creating the MongDB Database and store documents in different collections

def execute_json(filename,collection):
    json_to_read=open(filename,'r')
    filedata=json.load(json_to_read)
    print(filedata)
    if isinstance(filedata,list):
        db_col= MongoDB().db[collection]
        db_col.insert_many(filedata)
        print("succesfully inserted in mongodb")
    
#Execute commands for creating all stuff
execute_sql (r'C:\Users\esteb\OneDrive\Documentos\isra\code\bankaya\bankaya.sql')
execute_json(r'C:\Users\esteb\OneDrive\Documentos\isra\code\bankaya\customers_data.json',"customers_data")
execute_json(r'C:\Users\esteb\OneDrive\Documentos\isra\code\bankaya\items_data.json',"items_data")