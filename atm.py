#load user info
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kvsp",
    database="atm_machine"
    
)
state="true"

try:
   def admindetails():
        user_name=input("enter your user name").lower()
        passwords=input("enter your password").lower()
        cur=mydb.cursor()
        sq=("select * from admin_login where user_name=%sand passwords=%s")
        ad1=(user_name,passwords)
        cur.execute(sq,ad1)
        res=cur.fetchone()
        for i in res:
            print(i)
        print("login successfully")
   admindetails()
except:
   state='false'
option=['insert','delete','update','view']
if(state=="true"):
    print("welcome")
    
    opt=input("enter your option")
    if(opt=='view'):
        def view_user():
          cur=mydb.cursor()
          cur.execute("select * from users_verify")
          res1=cur.fetchall()
          for i in res1:
             print(i)
        view_user()
    elif(opt=='insert'):
        print("welcome")
        def inser_userdet():
            cur1=mydb.cursor()
            s=("insert into user_info(user_name,acc_no,pin,balance)values(%s,%s,%s,%s)")
            val=[('aadhi','acc105',2516,200),
                ('kani','acc106',7777,500),
                 ('anitha','acc107',2525,2000),
                ('padma','acc108',2929,3000)]
            cur1.executemany(s,val)
            mydb.commit()
        inser_userdet()



        






