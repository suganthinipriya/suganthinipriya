#table creation for ticketbooking
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kvsp",
    database="ticket_booking"
    )
def create():
    cu=mydb.cursor()
    cu.execute("create table schedule (day varchar(20),bus_name varchar(20),time varchar(20),location varchar(20),amount int)")
    print("table created")
create()
def create1():
   cu=mydb.cursor()
   cu.execute("create table user_book(name varchar(100),addr varchar(255),phone_number int,location varchar(20),bus_name varchar(30),time varchar(30),payment_status varchar(30),members int)")
   print("succesfully created")
create1()
def alttab():
    cu=mydb.cursor()
    cu.execute("alter table user_book add column email varchar(255)")
    print("altered")
alttab()
def alttab1():
    cu=mydb.cursor()
    cu.execute("alter table schedule add column busno varchar(10)")
    print("altered")
alttab1()
def alttab2():
   cu=mydb.cursor()
   cu.execute("alter table user_book add column (busno varchar(10),day varchar(10))")
   print("altered")
alttab2()
def alttab3():
     cu=mydb.cursor()
     cu.execute("alter table user_book add column phone_number bigint")
     print("altered")
alttab3()


#def create2():
  #  cu=mydb.cursor()
   # cu.execute("create table admin_log (admin_id varchar(20),user_name varchar(20),password varchar(20))")
   # print("table created")
#create2()
def ad_insert():
                    try: 
                        id=input(("enter your id:").lower()).strip()
                        user_name=(input("enter your user_name:").lower()).strip()
                        password=(input("enter your password:").lower()).strip()
                        cur=mydb.cursor()
                        s=("insert into admin_log(admin_id,user_name,password)values(%s,%s,%s)")
                        ad=(id,user_name,password)
                        cur.execute(s,ad)
                        mydb.commit()
                        print("successfully sign in")
                    except:
                        print("printcrt info")       
ad_insert()


