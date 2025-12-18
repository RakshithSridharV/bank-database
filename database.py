import sqlite3
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

#Customers
cursor.execute('create table if not exist Customers(cust_id integer primary key, name text not null , address text, email text unique )')
#Accounts
cursor.execute('create table if not exist Accounts(acc_id integer primary key, cust_id integer, acc_type text, balance real, foreign key (cust_id) references Customers(cust_id))')
#Transactions
cursor.execute('create table if not exist Transactions(trans_id integer primary key, acc_id integer, tran_type text, amount real, date date, foreign key(acc_id) references Accounts(acc_id))')

conn.commit()

cursor.close()
conn.close()