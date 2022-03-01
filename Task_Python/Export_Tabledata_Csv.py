# import libraries
import mysql.connector
import pandas as pd


# create connection
conn = mysql.connector.Connect(host="python-db-b1.ck3etxnc3ebl.us-east-1.rds.amazonaws.com", database="pythondb", user="admin", password="admin123", port=3306)

# run sql query
sql_query = pd.read_sql_query('''select * from m_employees''',conn)

# write the dataframe to a csv file
df = pd.DataFrame(sql_query)
df.to_csv(r'E:\Python_Course\emp_data.csv', index=False)
