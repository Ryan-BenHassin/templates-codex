#TODO
import sqlite3

class DataService:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, fields):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{field} TEXT' for field in fields])})"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(query, data)
        self.conn.commit()

    def select_data(self, table_name, conditions=None):
        query = f"SELECT * FROM {table_name}"
        if conditions:
            query += " WHERE " + " AND ".join([f"{key} =?" for key in conditions.keys()])
        self.cursor.execute(query, list(conditions.values()) if conditions else [])
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()

# Usage
db_file = 'y_database.db'
table_name = 'y_table'
fields = ['id', 'name', 'age']
data_service = DataService(db_file)
data_service.create_table(table_name, fields)
data_service.insert_data(table_name, ['1', 'John Doe', '30'])
print(data_service.select_data(table_name, {'age': '30'}))
data_service.close_connection()