import sqlite3  

con = sqlite3.connect("database.db")  
print("Database opened successfully")  
con.execute("create table documents (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT NOT NULL)")  
print("Table created successfully")  
con.close()  
