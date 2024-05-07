#TODO
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# replace with your database connection
conn = "YOUR_DB_CONNECTION"

@app.route('/report', methods=['GET'])
def generate_report():
 data = pd.read_sql_table("YOUR_TABLE_NAME", conn)
 return jsonify(data.to_dict(orient='records'))

@app.route('/REPORT/aggregate', methods=['GET'])
def generate_aggregate_report():
 data = pd.read_sql_table("YOUR_TABLE_NAME", conn)
 aggregate_data = data.groupby("YOUR_COLUMN_NAME").size().to_dict()
 return jsonify(aggregate_data)

if __name__ == '__main__':
 app.run(debug=True)
