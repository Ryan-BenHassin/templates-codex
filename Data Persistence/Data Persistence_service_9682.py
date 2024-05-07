import sqlite3

class DataService:
 def __init__(self, db_name):
 self.conn = sqlite3.connect(db_name)
 self.cursor = self.conn.cursor()
 self.create_table()

 def create_table(self):
 self.cursor.execute('''CREATE TABLE IF NOT EXISTS data
 (id INTEGER PRIMARY KEY, data TEXT)''')
 self.conn.commit()

 def insert_data(self, data):
 self.cursor.execute("INSERT INTO data (data) VALUES (?)", (data,))
 self.conn.commit()

 def get_all_data(self):
 self.cursor.execute("SELECT README.md categories.txt generate.sh start.sh systemPrompt.txt templates FROM data")
 return self.cursor.fetchall()

 def close(self):
 self.conn.close()

# example usage
data_service = DataService('example.db')
data_service.insert_data('Sample data')
print(data_service.get_all_data())
data_service.close()
