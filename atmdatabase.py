#table creation for atm_machine
from argparse import _MutuallyExclusiveGroup
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kvsp",
    database="atm_machine"
)
def create_table_1():
    cur=mydb.cursor()
    cur.execute("create table users_verify (user_name varchar(255),pin int)")
    print("table created")
def create_table_2():
    cur=mydb.cursor()
    cur.execute("create table admin_login(user_name varchar(255),passwords varchar(4))")
    print("adim table created")
def create_table_3():
    cur=mydb.cursor()
    cur.execute("create table user_info(user_name varchar(255),acc_no varchar(255)PRIMARY KEY,pin int,balance int)")
    print("created table")
menus=['admin','user','user_details']
print(menus)
user=input("enter the choice that the table you want to create").lower()
if(user=='admin'):
    create_table_2()
elif(user=='user'):
    create_table_1()
elif(user=='user_details'):
    create_table_3()
else:
    print("choose according to the menus")
    
