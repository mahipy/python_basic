# pip install mysql-connector-python==8.0.17 # for mysql perticular version
# pip uninstall mysql-connector-python

import mysql.connector

conn = mysql.connector.connect(user='admin', password='admin123',
                               host='python-db-b1.ck3etxnc3ebl.us-east-1.rds.amazonaws.com',
                               database='pythondb', port=3306)
# create a cursor obj
cursor = conn.cursor()
# create/init a query
# query_string = "CREATE TABLE student(Name VARCHAR(255),Roll_no int)"
query_string = "insert into student(Name,Roll_no) values(%s,%s)"
#1 val = ('Ram', '1234') # for single row insert value
val = [('surya', '3452'), ('kasi', '7845'), ('naga', '1624'), ('chandu', '6248')]
# execute query
# inside cursor object we have a method called execute will accept one parameter
#1 cursor.execute(query_string, val); # To execute single query
cursor.executemany(query_string, val); # To execute multiple queries
conn.commit()
print(conn)
conn.close()
