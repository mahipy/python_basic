import mysql.connector

conn = mysql.connector.connect(user='admin', password='admin123',
                               host='python-db-b1.ck3etxnc3ebl.us-east-1.rds.amazonaws.com',
                               database='pythondb', port=3306)
# create a cursor obj
cursor = conn.cursor()
# create/init a query
query_string = "CREATE TABLE student(Name VARCHAR(255),Roll_no int)"
# execute query
# inside cursor object we have a method called execute will accept one parameter
cursor.execute(query_string);
print(conn)
conn.close()
