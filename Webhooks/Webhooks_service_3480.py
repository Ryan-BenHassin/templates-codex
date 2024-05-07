from flask import Flask, request, jsonify
app = Flask(__name__)

webhooks = {}

@app.route('/webhooks', methods=['POST'])
def create_webhook():
 data = request.get_json()
 webhook_id = data['webhook_id']
 url = data['url']
 events = data['events']
 webhooks[webhook_id] = {'url': url, 'events': events}
 return jsonify({'webhook_id': webhook_id, 'tatus': 'created'})

@app.route('/webhooks/<string:webhook_id>', methods=['GET'])
def get_webhook(webhook_id):
 webhook = webhooks.get(webhook_id)
 if webhook:
 return jsonify({'webhook_id': webhook_id, 'url': webhook['url'], 'events': webhook['events']})
 else:
 return jsonify({'error': 'webhook not found'}), 404

@app.route('/webhooks/<string:webhook_id>', methods=['PUT'])
def update_webhook(webhook_id):
 webhook = webhooks.get(webhook_id)
 if webhook:
 data = request.get_json()
 webhook['url'] = data.get('url', webhook['url'])
 webhook['events'] = data.get('events', webhook['events'])
 return jsonify({'webhook_id': webhook_id, 'tatus': 'updated'})
 else:
 return jsonify({'error': 'webhook not found'}), 404

@app.route('/webhooks/<string:webhook_id>', methods=['DELETE'])
def delete_webhook(webhook_id):
 if webhook_id in webhooks:
 del webhooks[webhook_id]
 return jsonify({'webhook_id': webhook_id, 'tatus': 'deleted'})
 else:
 return jsonify({'error': 'webhook not found'}), 404

@app.route('/webhooks', methods=['GET'])
def get_webhooks():
 return jsonify(list(webhooks.keys()))

if __name__ == '__main__':
 app.run(debug=True)
