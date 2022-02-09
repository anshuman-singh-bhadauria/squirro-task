import sqlite3  

con = sqlite3.connect("database.db")  
print("Database opened successfully")  
con.execute("drop table documents")  
print("Table dropped successfully")  
con.close()   
