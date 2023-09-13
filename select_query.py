import sqlite3
conn=sqlite3.connect("usama_database.db")
data=conn.execute("SELECT * FROM STUDENTS")
for n in data:
    print(n)