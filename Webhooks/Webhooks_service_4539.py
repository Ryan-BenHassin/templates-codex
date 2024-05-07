from flask import Flask, request, jsonify
app = Flask(__name__)

webhooks = {}

@app.route('/webhooks', methods=['POST'])
def create_webhook():
 data = request.get_json()
 webhook_id = data.get('id')
 if webhook_id in webhooks:
 return jsonify({'error': 'Webhook already exists'}), 400
 url = data.get('url')
 event = data.get('event')
 if not url or not event:
 return jsonify({'error': 'Invalid request'}), 400
 webhooks[webhook_id] = {'url': url, 'event': event}
 return jsonify({'id': webhook_id}), 201

@app.route('/webhooks', methods=['GET'])
def get_webhooks():
 return jsonify(webhooks)

@app.route('/webhooks/<webhook_id>', methods=['GET'])
def get_webhook(webhook_id):
 if webhook_id not in webhooks:
 return jsonify({'error': 'Webhook not found'}), 404
 return jsonify(webhooks[webhook_id])

@app.route('/webhooks/<webhook_id>', methods=['DELETE'])
def delete_webhook(webhook_id):
 if webhook_id not in webhooks:
 return jsonify({'error': 'Webhook not found'}), 404
 del webhooks[webhook_id]
 return '', 204

if __name__ == '__main__':
 app.run(debug=True)
