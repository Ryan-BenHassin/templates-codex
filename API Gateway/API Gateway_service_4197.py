#TODO
from flask import Flask, jsonify, request
from flask_api import API
app = Flask(__name__)
api = API(app)

api_key = "YOUR_API_KEY"
secret_key = "YOUR_SECRET_KEY"

@app.route('/api/gateway', methods=['POST'])
def gateway():
 if request.json['api_key'] == api_key and request.json['secret_key'] == secret_key:
 return jsonify({"status": "authorized"})
 else:
 return jsonify({"status": "unauthorized"}), 401

@app.route('/api/gateway', methods=['GET'])
def health_check():
 return jsonify({"status": "ok"})

if __name__ == '__main__':
 app.run(debug=True)
