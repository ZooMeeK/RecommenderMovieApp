import sqlite3
from logs.logs import Logs

l = Logs()

class SQLiteCore:

    def __init__(self):
        pass
        
            
    def create_connection(self):
        self.connection = sqlite3.connect(self.db_location)
        self.cursor = self.connection.cursor()
        
        l.write_logs('Create connection')

    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        
        l.write_logs('Close connection')
    
    
    def select(self, query):
        self.create_connection()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.close_connection()
        return result
   

    def update(self, query):
        self.create_connection()
        self.cursor.execute(query)
        self.connection.commit()
        self.close_connection() 
    
    
    def insert(self, query):
        self.create_connection()
        self.cursor.execute(query)
        self.connection.commit()
        self.close_connection()