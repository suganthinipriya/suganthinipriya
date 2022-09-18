# for travel agency the created database and tables and data insertion are implemented alone combine all in progarm
from ssl import create_default_context
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kvsp",
    database='travel_agency'
)
#databasecreation
def createag():
    cur=mydb.cursor()
    s=("create database travel_agency")
    cur.execute(s)
createag()
#schedule table
def createagtab():
   cur=mydb.cursor()
   s=("create table travel_schedule (city varchar(255)PRIMARY KEY,car_amount bigint,flight_amount bigint,bus_amount bigint)")
   cur.execute(s)
createagtab()
#usertable
def createuser():
   cur=mydb.cursor()
   cur.execute("create table user_travel_book(name varchar(255),addr varchar(255),email varchar(60),phone_number bigint,aadhar varchar(12) PRIMARY KEY,travel_city varchar(80),travel_type varchar(10))")
createuser()
#admintable
def creatad():
    cur=mydb.cursor()
    cur.execute('create table admins (user_name varchar(20)primary key,password varchar(8))')
creatad()
#insert admin info
def insad():
    try:
       user_name=input("enter user_name:")
       password=input("enter your password")
       cur=mydb.cursor()
       s="insert into admins(user_name,password)values(%s,%s)"
       ad=(user_name,password)
       cur.execute(s,ad)
       mydb.commit()
       print("successfully inserted")
    except:
        print("user_name must be unique!!")
insad()
#alter table
def alttab2():
  cu=mydb.cursor()
  cu.execute("alter table user_travel_book add column (payment_status varchar(20))")
  print("altered")
alttab2()