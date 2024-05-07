#TODO
import sqlite3

class DataService:
 def __init__(self, db_name):
 self.conn = sqlite3.connect(db_name)
 self.cursor = self.conn.cursor()

 def create_table(self, table_name, columns):
 query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
 self.cursor.execute(query)
 self.conn.commit()

 def insert_data(self, table_name, data):
 columns = ', '.join(data.keys())
 placeholders = ':' + ', :'.join(data.keys())
 query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
 self.cursor.execute(query, data)
 self.conn.commit()

 def retrieve_data(self, table_name, condition):
 query = f"SELECT README.md categories.txt generate.sh start.sh systemPrompt.txt templates FROM {table_name} WHERE {condition}"
 self.cursor.execute(query)
 return self.cursor.fetchall()

 def update_data(self, table_name, data, condition):
 sets = ', '.join(f"{column} = :{column}" for column in data.keys())
 query = f"UPDATE {table_name} SET {sets} WHERE {condition}"
 self.cursor.execute(query, data)
 self.conn.commit()

 def delete_data(self, table_name, condition):
 query = f"DELETE FROM {table_name} WHERE {condition}"
 self.cursor.execute(query)
 self.conn.commit()

 def close_connection(self):
 self.conn.close()
