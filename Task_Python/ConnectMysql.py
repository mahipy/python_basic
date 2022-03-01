import mysql.connector
try:
    con = mysql.connector.connect(host="python-db-b1.ck3etxnc3ebl.us-east-1.rds.amazonaws.com", database="pythondb", user="admin", password="admin123", port=3306)
    cursor = con.cursor()
    cursor.execute("create table m_employees(Eno int(5) primary key,Ename varchar(10),Esal double(10,2),Eaddr varchar(10))")
    print("Table created")

    sql_query = "insert into m_employees(Eno, Ename, Esal, Eaddr) VALUES(%s,%s,%s,%s)"
    records = [(100, 'sachin', 10000, 'Mumbai'), (200, 'dhoni', 20000, 'Ranchi'), (300, 'kohli', 30000, 'Delhi')]
    cursor.executemany(sql_query, records)
    con.commit()
    print("Records Inserted Successfully..")

    cursor.execute("select * from m_employees")
    data = cursor.fetchall()
    print("data from db", data)
    for row in data:
        print("Employee number:", row[0])
        print("Emp name:", row[1])
        print("Emp sal:", row[2])
        print("Emp addr:", row[3])
        print()
        print()
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
    print("there is a problem with sql :", e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
