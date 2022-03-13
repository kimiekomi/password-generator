import sqlite3

class Database:
    def __init__(self, database):
        self.connect = sqlite3.connect(database)
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, website_name, password)")
        self.connect.commit() 

    def fetch(self):
        self.cursor.execute("SELECT * FROM passwords")
        rows = self.cursor.fetchall()
            
        return rows

    def add(self, website_name, password):
        self.cursor.execute("INSERT INTO addresses VALUES (NULL, ?, ?)", (website_name, password))
        self.connect.commit()

    def remove(self, id):
        self.cursor.execute("DELETE FROM passwords WHERE id=?", (id,))
        self.connect.commit()

    def update(self, id, website_name, password):
        self.cursor.execute("UPDATE passwords SET website_name=?, password=? WHERE id=?", (website_name, password, id))
        self.connect.commit()

    def delete_all(self):
        self.cursor.execute("DELETE FROM passwords")
        self.connect.commit()

    def __del__(self):
        self.connect.close()


database = Database("password_tree.db")