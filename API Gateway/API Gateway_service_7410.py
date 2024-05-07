#TODO
from flask import Flask, request, jsonify
import os
import logging

app = Flask(__name__)

# placeholder for API key
API_KEY = 'YOUR_API_KEY'

# logging configuration
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

@app.before_request
def check_api_key():
   if request.headers.get('API-Key') != API_KEY:
       return jsonify({'error': 'Invalid API Key'}), 401

@app.route('/', methods=['GET'])
def index():
   return jsonify({'message': 'Welcome to API Gateway'})

if __name__ == '__main__':
   app.run(debug=True)