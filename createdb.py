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
    conn.close()

#Start creating the MongDB Database and store documents in different collections

def execute_json(filename,collection):
    json_to_read=open(filename,'r')
    filedata=json.load(json_to_read)
    print(filedata)
    if isinstance(filedata,list):
        db_col= MongoDB().db[collection]
        db_col.insert_many(filedata)
        print("succesfully inserted in mongodb "+collection)
    else:
        db_col.insert_one(filedata)
        print("succesfully inserted single record mongodb" + collection)

#Execute commands for create MARIADB database and also create BANKAYA db in MONGO
#Also get data from the external files
execute_sql (r'C:\Users\esteb\OneDrive\Documentos\isra\code\bankaya\bankaya.sql')
execute_json(r'C:\Users\esteb\OneDrive\Documentos\isra\code\bankaya\customers_data.json',"customers_data")
execute_json(r'C:\Users\esteb\OneDrive\Documentos\isra\code\bankaya\items_data.json',"items_data")
execute_json(r'C:\Users\esteb\OneDrive\Documentos\isra\code\bankaya\items_bought_data.json',"items_bought_data")

#Export from MONGO TO MARIADB

#Export customers
def export_customers():
    db_ins = MongoDB().db['customers_data']
    cust_data = db_ins.find()
    cur = MariaDB("BANKAYA")
    for data in  cust_data:
        print(data["firstname"])
        try: 
            cur.execute("INSERT INTO CUSTOMER (first_name,last_name,phone_number,curp,rfc,address_cust) VALUES (?, ?, ?, ?, ?, ?)", (data["firstname"],data["lastname"],data["phone_number"],data["curp"],data["rfc"],data["address"])) 
        except mariadb.Error as e: 
            print(f"MariaDB Error: {e}")
    print("Succesfuly exported customers")
    cur.commit()  

#Export items
def export_items():
    db_ins = MongoDB().db['items_data']
    cust_data = db_ins.find()
    cur = MariaDB("BANKAYA")
    for data in  cust_data:
        print(data["title"])
        try: 
            cur.execute("INSERT INTO ITEMS (item,price) VALUES (?, ?)", (data["title"],data["price"]))
        except mariadb.Error as e: 
            print(f"MariaDB Error: {e}")
    print("Succesfully Exported items")   
    cur.commit() 

#Export item_bougths
def export_item_bougths():
    db_ins = MongoDB().db['items_bougth_data']
    cust_data = db_ins.find()
    cur = MariaDB("BANKAYA")
    for data in  cust_data:
        print(data["title"])
        try: 
            cur.execute("INSERT INTO ITEMS (item,price) VALUES (?, ?)", (data["title"],data["price"]))
        except mariadb.Error as e: 
            print(f"MariaDB Error: {e}")
    print("Succesfully Exported items")   
    cur.commit() 
#Function calls
export_customers()
export_items()