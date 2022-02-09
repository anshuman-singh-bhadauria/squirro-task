import sqlite3

class DB:
    def __init__(self, name):
        self.name = name

    def insert(self, document):
        try:
            with sqlite3.connect(self.name) as con:  
                cur = con.cursor()
                cur.execute("INSERT INTO documents (content) VALUES (?)", (document,))   
                con.commit()  
                print("Success")   
                return cur.lastrowid 
        except Exception as e:
            con.rollback()
            print(e)
            print("Consider running init.py")
        finally:
            con.close()
            print("DB Closed")

    def fetch(self, document_id):
        try:
            with sqlite3.connect(self.name) as con:  
                cur = con.cursor()
                cur.execute("SELECT content FROM documents WHERE (id) = (?)", (str(document_id),))
                document=cur.fetchall()[0][0]   
                con.commit()  
                return document 
        except Exception as e:
            con.rollback()
            print(e)
        finally:
            con.close()
            print("DB Closed")

    def show_table(self, table_name="documents",limit=5):
        try:
            with sqlite3.connect(self.name) as con:  
                cur = con.cursor()
                sql="SELECT * FROM "+table_name+" LIMIT "+str(limit)
                cur.execute(sql)
                print(cur.fetchall())
        except Exception as e:
            con.rollback()
            print(e)
        finally:       
            con.close()

if __name__=="__main__":
    database=DB("database.db")
    content='Some text content'
    database.insert(content)
    database.fetch(6)
