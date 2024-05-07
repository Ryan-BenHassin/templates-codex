#TODO
import flask
import json
from flask import request

app = flask.Flask(__name__)

@app.route('/webhooks', methods=['POST'])
def handle_webhook():
 data = request.get_json()
 if data:
 print("Received webhook data:")
 print(json.dumps(data, indent=4))
 return 'Webhook received successfully', 200
 else:
 return 'Bad request', 400

if __name__ == '__main__':
 app.run(debug=True)
