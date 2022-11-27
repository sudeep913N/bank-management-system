import sqlite3
conn=sqlite3.connect("customer.db")
curs=conn.cursor()
curs.execute("""CREATE TABLE customers(name text,id int primary key,balance real)""")
conn.commit()
conn.close()
