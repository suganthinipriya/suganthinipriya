#******************ATM***********************#
from logging.config import valid_ident
from multiprocessing.sharedctypes import Value
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="kvsp",
    database="atm_machine"    
)
print("##############welcome###########")
print("*****save your precious time uisng digitally transfering money*****")
#login verification
state="true"
try:
   def hai():
    print("insert your card")
    user_insert_card=input("insert your card if inserted click inserted or nor:") 
    if(user_insert_card=='inserted'):
       
       acc_no=input(("enter your account number:").lower()).strip()
       pin=int(input("enter your pin only four digit:"))
       cur=mydb.cursor()
       s="select * from user_info where acc_no=%s and pin=%s"
       val=(acc_no,pin)
       cur.execute(s,val)
       res=cur.fetchone()
       for i in res:
          print(i)
       print("logged in")
    
   hai()
except:
    state="wrong"
if(state=='true'):
    print("************************welcome**************************")
    print("please select your account:").lower()
    op1=['savings','current']
    option1=input("enter your account type:").lower()
    op=['deposit','withdraw','transfer','changepin','current_withdraw','current_transfer','viewbalance']
    print(op)
    opt=input(("enter your op").lower()).strip()
#depositing money
    if(opt=='deposit'and (option1=='savings' or option1=='current') ):
        def dept():
            acc_no=input("enter your account number like accXXX:")
            pin=int(input("enter your pin only 4 digit:"))
            amount=int(input("enter amount:"))
            cur=mydb.cursor()
            s=("update user_info set balance=(balance+%s) where acc_no=%s and pin=%s")
            val=(amount,acc_no,pin)
            cur.execute(s,val)
            mydb.commit()
            print("deposited")
        dept()
#withdraw money
    elif(opt=='withdraw'and option1=='savings'):
        def withd():
            acc_no=input("enter you account number like accXXX:")
            pin=int(input("enter your pin to proceed:"))
            amount=int(input("enter your amount to transfer:"))
            cur=mydb.cursor()
            s=("update user_info set balance=(balance-%s) where acc_no=%s and pin=%s and balance>%s")
            val=(amount,acc_no,pin,amount)
            cur.execute(s,val)
            mydb.commit()
            print("withdrawed")
        withd()
#transfer money to another account
    elif(opt=='transfer' and option1=='savings'):
        def transfer():
            acc_no=input("enter you account number like accXXX:")
            pin=int(input("enter your pin to proceed:"))
            acc_no2=input("enter account number you want to transfer:")
            amount=int(input("enter your amount to transfer:"))
            cur=mydb.cursor()
            s=("update user_info set balance=(balance-%s) where acc_no=%s and pin=%s and balance>%s")
            val=(amount,acc_no,pin,amount)
            cur.execute(s,val)
            mydb.commit()
            cur2=mydb.cursor()
            sq=("update user_info set balance=(balance+%s) where acc_no=%s")
            val1=((amount),acc_no2)
            cur2.execute(sq,val1)
            mydb.commit()
        transfer()
#change pin
    elif(opt=='changepin'and (option1=='savings'or option1=='current')):
        def change_pin():
            acc_no=input("enter your account number:")
            pin=int(input("enter your old pin:"))
            new_pin=int(input("enter your new pin only4 digit number:"))
            if(pin!=new_pin):
                cur=mydb.cursor()
                s=("update user_info set pin=%s where  acc_no=%s and pin=%s")
                val=(new_pin,acc_no,pin)
                cur.execute(s,val)
                mydb.commit()
                print("successfully updated")
            else:
                print("your password is same or incorrect")
        change_pin()
#withdraw money using current account
    elif(opt=='current_withdraw' and (option1=="current")):
        def curr_with():
            acc_no=input("enter your account number accXXX:")
            pin=int(input("enter your pin:"))
            amount=int(input("enter your amount to withdraw:"))
            cur=mydb.cursor()
            s=("update user_info set balance=(balance-%s) where pin=%s and acc_no=%s")
            val=(amount,pin,acc_no)
            cur.execute(s,val)
            mydb.commit()
            print("you can withdraw your amount.{}",amount)
        curr_with()
#transfer money  using curret account
    elif(opt=="current_transfer" and(option1=="current")):
        def trans_cur():
            acc_no=input("enter your account number:")
            pin=int(input("enter your pin:"))
            acc_no2=input("enter account number you want to transfer:")
            amount=int(input("enter your amount to transfer:"))
            cur=mydb.cursor()
            s=("update user_info set balance=(balance-%s) where acc_no=%s and pin=%s")
            val=(amount,acc_no,pin)
            cur.execute(s,val)
            mydb.commit()
            print("your amount is transfered successfully")
            cur1=mydb.cursor()
            s=("update user_info set balance=balance+%s where acc_no=%s")
            val=(amount,acc_no2)
            cur1.execute(s,val)
            mydb.commit()
        trans_cur()
#view your balance
    elif(opt=="viewbalance" and (option1=='savings' or option1=='current')):
        def view():
            acc_no=input("enter your account number:")
            pin=int(input("enter your 4 digit pin:"))
            cur=mydb.cursor()
            s=("select user_name,balance from user_info where acc_no=%s and pin=%s")
            val=(acc_no,pin)
            cur.execute(s,val)
            res=cur.fetchone()
            print(" your account balance is:")
            for i in res:
                print(i)
        view()
    else:
        print("some input is wrong give correct information!!!!")
else:
    print("your login information is wrong!!!")