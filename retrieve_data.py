import sqlite3
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

#Lists all customer data
Cust_Details = cursor.execute('select * from Customers')
print("Customers Details:")
for cust in Cust_Details:
    print(cust)

#Lists customer and acc details
Cust_Acc = cursor.execute('select A.acc_id, C.name, A.cust_id, A.acc_type, A.balance from Customers C,Accounts A Where C.cust_id = A.cust_id')
print("Customers Account Details:")
for acc in Cust_Acc:
    print(acc)

#Lists all transactions
transactions = cursor.execute('select * from Transactions')
print("All Transactions Details:")
for trans in transactions:
    print(trans)

cursor.close()
conn.close()