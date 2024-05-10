from flask import Flask, request, jsonify
import json

app = Flask(__name__)

webhooks = {}

@app.route('/webhooks', methods=['POST'])
def create_webhook():
    data = request.get_json()
    if not data:
        return 'Bad request', 400
    print("Received webhook creation data:")
    print(json.dumps(data, indent=4))  # Debugging output

    webhook_id = data.get('webhook_id')
    if not all(k in data for k in ['webhook_id', 'url', 'events']):
        return jsonify({'error': 'Missing required fields'}), 400
    if webhook_id in webhooks:
        return jsonify({'error': 'Webhook already exists'}), 409

    webhooks[webhook_id] = {'url': data['url'], 'events': data['events']}
    return jsonify({'webhook_id': webhook_id, 'status': 'created'}), 201

@app.route('/webhooks/<string:webhook_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_webhook(webhook_id):
    if request.method == 'GET':
        webhook = webhooks.get(webhook_id)
        if not webhook:
            return jsonify({'error': 'Webhook not found'}), 404
        return jsonify(webhook)

    elif request.method == 'PUT':
        webhook = webhooks.get(webhook_id)
        if not webhook:
            return jsonify({'error': 'Webhook not found'}), 404
        data = request.get_json()
        webhook['url'] = data.get('url', webhook['url'])
        webhook['events'] = data.get('events', webhook['events'])
        return jsonify({'webhook_id': webhook_id, 'status': 'updated'})

    elif request.method == 'DELETE':
        if webhook_id not in webhooks:
            return jsonify({'error': 'Webhook not found'}), 404
        del webhooks[webhook_id]
        return jsonify({'webhook_id': webhook_id, 'status': 'deleted'})

@app.route('/webhooks', methods=['GET'])
def get_webhooks():
    return jsonify(list(webhooks.keys()))

if __name__ == '__main__':
    app.run(debug=True)
