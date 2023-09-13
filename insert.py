import sqlite3
conn=sqlite3.connect("usama_database.db")
ins=('''
    insert into students (st_id,st_name,st_class,st_email)VALUES("3455","hassan ali ","10th","hassanali402@gmail.com")
    ''')
conn.execute(ins)
conn.commit()
conn.close