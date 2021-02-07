import mariadb
import json
import string
import random
from connmaria import MariaDB
from connmongo import MongoDB

#Start creating the MySQL with Initial Scripts DataBase

def execute_sql(filename):
    print("Beggining Reading External SQL File to create BANKAYA")
    sql_to_read=open(filename,'r')
    sql_file= sql_to_read.read()
    sql_to_read.close()

    sql_commands = sql_file.split(";")
    print("Ready with SQL commands...proceeding...")
    conn = MariaDB()
    for cmds in sql_commands:
        #print(cmds)
        try:
            conn.execute(cmds)
        except mariadb.Error as e:
            print(f"Error:{e}")
    print("MariaDB Bankaya Database created succesfully")
    conn.close()

#Start creating the MongDB Database and store documents in different collections

def execute_json(filename,collection):
    print("Reading external jsons to import into MongoDB ->"+collection)
    json_to_read=open(filename,'r')
    filedata=json.load(json_to_read)
    print(filedata)
    if isinstance(filedata,list):
        db_col= MongoDB().db[collection]
        db_col.insert_many(filedata)
        print("Succesfully inserted in mongodb "+collection)
    else:
        db_col.insert_one(filedata)
        print("Succesfully inserted single record mongodb" + collection)

#Execute commands for create MARIADB database and also create BANKAYA db in MONGO
#Also get data from the external files
execute_sql (r'C:\Users\esteb\OneDrive\Documentos\isra\code\bankaya\bankaya.sql')
execute_json(r'C:\Users\esteb\OneDrive\Documentos\isra\code\bankaya\customers_data.json',"customers_data")
execute_json(r'C:\Users\esteb\OneDrive\Documentos\isra\code\bankaya\items_data.json',"items_data")
execute_json(r'C:\Users\esteb\OneDrive\Documentos\isra\code\bankaya\items_bought_data.json',"items_bought_data")

#Export from MONGO TO MARIADB

#Export customers
def export_customers():
    print("Exporting CUSTOMERS data to MariaDB ....")
    db_ins = MongoDB().db['customers_data']
    cust_data = db_ins.find()
    cur = MariaDB("BANKAYA")
    for data in  cust_data:
        try: 
            cur.execute("INSERT INTO CUSTOMER (first_name,last_name,phone_number,curp,rfc,address_cust) VALUES (?, ?, ?, ?, ?, ?)", (data["firstname"],data["lastname"],data["phone_number"],data["curp"],data["rfc"],data["address"])) 
        except mariadb.Error as e: 
            print(f"MariaDB Error: {e}")
    print("Succesfuly exported customers")
    cur.commit()  

#Export items
def export_items():
    print("Exporting ITEMS data to MariaDB ....")
    db_ins = MongoDB().db['items_data']
    cust_data = db_ins.find()
    cur = MariaDB("BANKAYA")
    for data in  cust_data:
        #print(data["title"])
        try: 
            cur.execute("INSERT INTO ITEMS (item,price) VALUES (?, ?)", (data["title"],data["price"]))
        except mariadb.Error as e: 
            print(f"MariaDB Error: {e}")
    print("Succesfully Exported ITEMS")   
    cur.commit() 

#Get Single Price
def get_price(ids):
    cur = MariaDB("BANKAYA")
    price = cur.query("""SELECT price FROM items WHERE id = ? """,(ids,))
    for p in price:
        #print("El precio es :",p[0])
        ret_val = p[0]
        return ret_val


#Export item_bougths
def export_item_bougths():
    print("Exporting ITEMS BOUGHT data to MariaDB ....")
    db_ins = MongoDB().db['items_bought_data']
    cust_data = db_ins.find()
    cur = MariaDB("BANKAYA")
    for data in  cust_data:
        #print(data["id_items"])
        items = data["id_items"]
        #Generate ID for order
        rand_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)]) 
        for ids in items:
            #Get price before inserting as requested. 
            price = get_price(ids)
             #print("El precio de getprices es",price)
            try:
                cur.execute("INSERT INTO ITEMS_BOUGHT (order_number,date_order,price,id_items,id_customers,comments) \
                VALUES (?, ?, ?, ?, ?, ?)", (rand_id,data["date_order"],price,ids,data["id_customer"],data["comments"]))
            except mariadb.Error as e:
                print(f"MariaDB Error : {e}")
    cur.commit()    
    print("Succesfully Exported ITEMS BOUGHT")   
    #cur.commit() 


#Main function ...do this forever
if __name__=="__main__":
    export_customers()
    export_items()
    export_item_bougths()