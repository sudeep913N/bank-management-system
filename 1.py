import sqlite3
import copy
loop=1
def newacc():
    try:
        conn=sqlite3.connect("customer.db")
        curs=conn.cursor()
        query="insert into customers values(?,?,?)"
        name=input("Enter your name:")
        idno=int(input("Enter your id no:"))
        balance=0
        curs.execute(query,[name,acno,balance])
        conn.commit()
        print("Account created succesfully")
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
def addmny():
    print("Enter your idno :")
    x=int(input())
    print("Enter the money to add")
    y=int(input())
    lis=[]
    try:
        conn=sqlite3.connect("customer.db")
        curs=conn.cursor()
        select_query = "SELECT balance from customers where id = ?"
        curs.execute(select_query, (x,))
        conn.commit()
        rem=curs.fetchone()
        for i in rem:
            res=i
            lis.append(i)
        bal=lis[0]+y
        query1='''UPDATE customers SET balance=? WHERE id =?'''
        curs.execute(query1,[bal,x])
        conn.commit()
        print("Ammount added")
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
def widr():
    conn=sqlite3.connect("customer.db")
    curs=conn.cursor()
    print("Enter your idno:")
    p=int(input())
    print("Enter the money you want:")
    o=int(input())
    try:
        select_query = "SELECT balance from customers where id = ?"
        curs.execute(select_query, (p,))
        conn.commit()
        rem=curs.fetchone()
        lis=[]
        for i in rem:
            res=i
            lis.append(res)
        if lis[0]<o:
            print("Not enough money")
        else:
            bal1=lis[0]-o
            bal=int(bal1)
            query1="update customers set balance=?  where id =?"
            curs.execute(query1,[bal,p])
            conn.commit()
            print("Amount debited ")
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
def balch():
    x=int(input("Enter your id :"))
    try:
        conn=sqlite3.connect("customer.db")
        curs=conn.cursor()
        select_query = "SELECT balance from customers where id = ?"
        curs.execute(select_query, (x,))
        conn.commit()
        rem=curs.fetchone()
        lis=[]
        for i in rem:
            res=i
            lis.append(res)
        print("Your balance is :",lis[0])
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
def show():
    try:
        conn=sqlite3.connect("customer.db")
        curs=conn.cursor()
        for row in curs.execute('SELECT * FROM customers;'):
            print(row)
    except Exception as ex:
        print(ex)
    finally:
        conn.close()
while(loop==1):
    d=int(input("1.Create new account\n2.add money\n3.withdraw money\n4.check balance\n"))
    if d==1:
        newacc()
    elif d==2:
        addmny()
    elif d==3:
        widr()
    elif d==4:
        balch()
    else:
        print("choose correct option")
    r=int(input("1.exit\n2.again"))
    if r==1:
        loop=2
    else:
        pass
    
    
    

    

