#***************travel agency*****************
from ast import If
from audioop import add
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kvsp",
    database='travel_agency'
    )
#payment purpose
mydb1=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kvsp",
    database="atm_machine"
)
print("************welcome to gankrish agency***********")
print("HAVE A SAFE AND HAPPY JOURNEY BOOKNOW!!!")
print("contact number:7788991011")
print("address:modhilal street,kumbakonam")
print("website:www.gankrishagency.com")
#view schedule
def viewsche():
    cur=mydb.cursor()
    print("city car flight bus")
    cur.execute("select * from travel_schedule")
    res=cur.fetchall()
    for i in res:
        print(i)
viewsche()
op=['admin','user','booking_status']
print(op)
op1=input("enter your option:")
states='true'
if(op1=='admin'):
    def login():
        try:
            user_name=input("enter your user name:")
            password=input("enter your password:")
            cur=mydb.cursor()
            s=("select user_name,password from admins where user_name=%s and password=%s")
            ad=(user_name,password)
            cur.execute(s,ad)
            res=cur.fetchone()
            for i in res:
                print(i)
            print("successfully logged in")
        except:
            states='false'
            print("username or password is wrong!!")
    login()
    if(states=='true'):
        ops=['makeschedule','updateschedule','updateadmin','viewuser']
        print(ops)

        ops2=input("enter your choice:")
        if(ops2=="makeschedule"):
            
            def makesche():
                try:
                    city=input("enter city name:").lower()
                    car_amount=int(input("enter amount:"))
                    f_amount=int(input("enter amount:"))
                    bus_amount=int(input("enter amount:"))
                    cur=mydb.cursor()
                    s=("insert into travel_schedule (city,car_amount,flight_amount,bus_amount)values(%s,%s,%s,%s)")
                    ad=(city,car_amount,f_amount,bus_amount)
                    cur.execute(s,ad)
                    mydb.commit()
                    print(" schedule created")
                except:
                    print("give valid information")
            makesche()
        elif(ops2=="updateschedule"):
            def upsche():
                try:
                    city=input("enter city name:").lower()
                    car_amount=int(input("enter amount:"))
                    f_amount=int(input("enter amount:"))
                    bus_amount=int(input("enter amount:"))
                    cur=mydb.cursor()
                    s=("update travel_schedule set car_amount=%s,flight_amount=%s,bus_amount=%s where city=%s")
                    ad=(car_amount,f_amount,bus_amount,city)
                    cur.execute(s,ad)
                    mydb.commit()
                    print("successfully updated")
                except:
                    print("give valid info")
            upsche()
        elif(ops2=="updateadmin"):
            def upad():
                try:
                    user_name=input("enter user name:")
                    password=input("enter new password:")
                    cur=mydb.cursor()
                    s=("update admins set password=%s where user_name=%s")
                    ad=(password,user_name)
                    cur.execute(s,ad)
                    mydb.commit()
                    print("password changed successfully")
                except:
                    print("enter valid user_name or correct password!!")
            upad()
        elif(ops2=="viewuser"):
            def viewus():
                cur=mydb.cursor()
                cur.execute("select * from user_travel_book")
                res=cur.fetchall()
                for i in res:
                    print(i)
            viewus()
        else:
            print("type valid option!!!")
elif(op1=='user'):
    def book():
        name=input("enter name:")
        addr=input("enter address:")
        email=input("enter email:")
        phone=int(input("enter phone number:"))
        aadhar=input("enter aadhar number:")
        travel_city=input("enter city you need to travel:")
        travel_type=input("enter travel type:")
        cur=mydb.cursor()
        s=("insert into user_travel_book (name,addr,email,phone_number,aadhar,travel_city,travel_type)values(%s,%s,%s,%s,%s,%s,%s)")
        ad=(name,addr,email,phone,aadhar,travel_city,travel_type)
        cur.execute(s,ad)
        mydb.commit()
        print("proceed for payment")
        def payment():
                try:
                    st="true"
                    email=input("enter email:")
                    phone=int(input("enter phone number:"))
                    user_name=input("enter your user name:").lower()
                    pin=int(input("enter your 4 digit pin:"))
                    acc_no=input("enter your account number accXXX:")
                    amount=int(input("enter amount to pay:"))
                    cur1=mydb1.cursor()
                    s1=("update user_info set balance=(balance-%s) where user_name=%s and pin=%s and acc_no=%s")
                    add=((amount),user_name,pin,acc_no)
                    cur1.execute(s1,add)
                    print("successfully paid")
                    mydb1.commit()
                except:
                    print("payment is not successfull")
                    st="false"
                if(st=="true"):
                    
                        cur=mydb.cursor()
                        s2=("update user_travel_book set payment_status='paid' where email=%s or phone_number=%s")
                        ad2=(email,phone)
                        cur.execute(s2,ad2)
                        mydb.commit()
                else:
                    print("status if not paid")
        payment()
    book()
elif(op1=="bookingstatus"):
        email=input("enter your emailid:")
        phone=int(input("enter your phone number:"))
        def status_check():
            try:
                cur=mydb.cursor()
                s1=("select name , payment_status from user_travel_book where (email=%s or phone_number=%s) and( payment_status='paid')")
                ad=(email,phone)
                cur.execute(s1,ad)
                res=cur.fetchone()
                for i in res:
                   print(i)
                print("ticket is booked happy and safe journey!!!!")
            except:
               print("email or phonenumber is wrong")
        status_check()
else:
    print("valid option")





            




