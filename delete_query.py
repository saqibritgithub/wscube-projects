import sqlite3
conn=sqlite3.connect("usama_database.db")
st_id=input("enter the student id:")
conn.execute("DELETE FROM students where st_id="+ st_id)
conn.commit()
conn.close()