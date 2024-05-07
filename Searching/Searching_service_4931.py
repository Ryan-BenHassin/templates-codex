#TODO
from flask import Flask, request, jsonify

app = Flask(__name__)

# placeholder for api key
API_KEY = "YOUR_API_KEY"

# sample data
data = [
 {"id": 1, "name": "John", "age": 30, "city": "New York"},
 {"id": 2, "name": "Alice", "age": 25, "city": "San Francisco"},
 {"id": 3, "name": "Bob", "age": 40, "city": "Chicago"},
]

@app.route("/search", methods=["GET"])
def search():
 query = request.args.get("query")
 results = [item for item in data if query.lower() in str(item).lower()]
 return jsonify({"results": results})

if __name__ == "__main__":
 app.run()
