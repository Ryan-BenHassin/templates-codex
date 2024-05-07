#TODO
from flask import Flask, request, jsonify

app = Flask(__name__)

subscriptions = {}

@app.route('/subscriptions', methods=['POST'])
def create_subscription():
 data = request.get_json()
 subscriber_id = data['subscriber_id']
 subscription_id = data['subscription_id']
 subscriptions[subscription_id] = subscriber_id
 return jsonify({'subscription_id': subscription_id, 'ubscriber_id': subscriber_id})

@app.route('/subscriptions/<subscription_id>', methods=['GET'])
def get_subscription(subscription_id):
 if subscription_id in subscriptions:
 return jsonify({'subscription_id': subscription_id, 'ubscriber_id': subscriptions[subscription_id]})
 else:
 return jsonify({'error': 'Subscription not found'}), 404

@app.route('/subscriptions/<subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
 if subscription_id in subscriptions:
 del subscriptions[subscription_id]
 return jsonify({'message': 'Subscription deleted'})
 else:
 return jsonify({'error': 'Subscription not found'}), 404

if __name__ == '__main__':
 app.run(debug=True)
