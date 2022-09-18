from pydoc import stripid
#***********ticket booking*************
import mysql.connector
from psutil import users
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kvsp",
    database="ticket_booking"
)
mydb1=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kvsp",
    database="atm_machine"
)
print("*****welcome to travel express*****")
print("Have a pleasant journey with safe book here !!!!!!")
# schedule
def view():
    cur=mydb.cursor()
    cur.execute("select busno,bus_name,day,time,location,amount from schedule")
    res=cur.fetchall()
    for i in res:
        print(i)
    print("have pleasent and safe journey book here !!!!")
view()
#look for option
a=['admin','user','ticketstatus']
print(a)
s=input("enter your option:")
#admin details
if(s=='admin'):
    def admin():
        status="true"
        opt=['signup']
        print(opt)
        option=input("enter your option:")
        op=['updateschedule','createschedule','updateamdmin','viewuser']
        try:
            if(option=='signup'):
                def login_admin():
                    admin_id=(input("enter your id:").lower()).strip()
                    user_name=(input("enter your user name:").lower()).strip()
                    password=(input("enter your password:").lower()).strip()
                    cur=mydb.cursor()
                    s=("select * from admin_log where admin_id=%s and user_name=%s and password=%s")
                    ad=(admin_id,user_name,password)
                    cur.execute(s,ad)
                    res=cur.fetchone()
                    for i in res:
                      print(i)
                    print("sucessfully logged in!!")
                login_admin()
            else:
                print("pass or user name or id is wrong")
                status="false"          
        except:
            status="false"
        if(status=="true"):
            print(op)
            select=input("enter your option:").lower()
            if(select=="createschedule"):
                def crsched():
                    bus_no=input("enter bus no")
                    day=(input("enter day:").lower()).strip()
                    bus_name=(input("enter bus name:").lower()).strip()
                    time=(input("enter time:").lower()).strip()
                    location=input("enter locationto-from:")
                    amount=int(input("enter amount:"))
                    cur=mydb.cursor()
                    s1=("insert into schedule (day,busno,bus_name,time,location,amount)values(%s,%s,%s,%s,%s,%s)")
                    ad=(day,bus_no,bus_name,time,location,amount)
                    cur.execute(s1,ad)
                    mydb.commit()
                    print("successfully scheduled")
                crsched()
            elif(select=='updateschedule'):
                def upsche():
                    bus_no=input("enter bus no")
                    day=(input("enter day:").lower()).strip()
                    bus_name=(input("enter bus name:").lower()).strip()
                    time=(input("enter time:").lower()).strip()
                    location=input("enter locationto-from:")
                    amount=int(input("enter amount:"))
                    cur=mydb.cursor()
                    s1=("update schedule set day=%s,bus_name=%s,time=%s,location=%s,amount=%s where busno=%s")
                    ad=(day,bus_name,time,location,amount,bus_no)
                    cur.execute(s,ad)
                    mydb.commit()
                    print("successfully updated!!")
                upsche()
            elif(select=='updateadmin'):
                def upad():
                    cur=mydb.cursor()
                    id=input("enter your id:").lower()
                    user_name=input("enter your user name:").lower()
                    password=input("enter your password:").lower()
                    s1=("update admin_log set user_name=%s,password=%s where admin_id=%s")
                    ad=(user_name,password,id)
                    cur.execute(s1,ad)
                    mydb.commit()
                    print("successfully updated")
                upad()
            elif(select=='viewuser'):
                def views():
                    cur=mydb.cursor()
                    cur.execute("select * from user_book")
                    res=cur.fetchall()
                    for i in res:
                        print(i)
                views()

            else:
                print("give correct details")
    admin()
#ticket status verification
elif(s=='ticketstatus'):
    email=input("enter your emailid:")
    phone_number=int(input("enter your phone number:"))
    def status_check():
        cur=mydb.cursor()
        s1=("select name , payment_status from user_book where (email=%s or phone_number=%s) and( payment_status='paid')")
        ad=(email,phone_number)
        cur.execute(s1,ad)
        res=cur.fetchone()
        for i in res:
            print(i)
        print("ticket is booked happy and safe journey!!!!")
    status_check()

#book your bus
elif(s=="user"):
    print('welcome to happy journey site!!!!') 
    bus_no=input("enter the bus number") 
    location=input("enter your journey location:")
    bus_name=input("enter your bus name:")
    day=input("enter day:")
    time=input("enter your time of travel:")
    check_seats=input("available or not")
    if(check_seats=='available'):
        members=int(input(" enter number persons join with you "))
        no_seats_avail=int(input("enter number of seats available"))
        if(no_seats_avail>=members):
            op1=['book','pay','ticketstatus']
            print(op1)
            ops=input("enter your choice")
            if(ops=='book'):
                def book_ticket():
                    name=input("enter your name:")
                    email=input("enter your emailid:")
                    phone_number=int(input("enter your phone number:"))
                    address=input("enter your address:")
                    cur=mydb.cursor()
                    s1=("insert into user_book(name,addr,phone_number,email,members,location,bus_name,time,day,bus_no)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                    ad=(name,address,phone_number,email,members,location,bus_name,time,day,bus_no)
                    cur.execute(s1,ad)
                    mydb.commit()
                    print("successfully book proceed to pay")
                book_ticket()
    # pay amount
            elif(ops=='pay'):
                
                try:
                    def pay_amount():
                        user_name=input("enter your user name:").lower()
                        pin=int(input("enter your 4 digit pin:"))
                        acc_no=input("enter your account number accXXX:")
                        amount=int(input("enter amount to pay:"))
                        cur1=mydb1.cursor()
                        s1=("update user_info set balance=(balance-%s) where user_name=%s and pin=%s and acc_no=%s")
                        ad=((amount*members),user_name,pin,acc_no)
                        cur1.execute(s1,ad)
                        print("successfully paid")
                        mydb1.commit()
                        cur=mydb.cursor()
                        s2=("update user_book set payment_status='paid' where email=%s or phone_number=%s")
                        ad2=(email,phone_number)
                        cur.execute(s2,ad2)
                        mydb.commit()
                    pay_amount()
                except:
                    print(" pin or username or account number is wrong")
            else:
                print("give correct option!!!")     
        else:
                print("please select valid option")
    else:
        print("seats not available look for another bus!!!")
else:
    print("select valid option")





                

        








        