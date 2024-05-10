import unittest
from flask import Flask, request, jsonify

# Setup the Flask app
app = Flask(__name__)

webhooks = {}

@app.route('/webhooks', methods=['POST'])
def create_webhook():
    data = request.get_json()
    if not all(key in data for key in ['webhook_id', 'url', 'events']):
        return jsonify({'error': 'Missing required fields'}), 400
    webhook_id = data['webhook_id']
    if webhook_id in webhooks:
        return jsonify({'error': 'Webhook already exists'}), 409
    webhooks[webhook_id] = {'url': data['url'], 'events': data['events']}
    return jsonify({'webhook_id': webhook_id, 'status': 'created'}), 201

@app.route('/webhooks/<string:webhook_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_webhook(webhook_id):
    if request.method == 'GET':
        webhook = webhooks.get(webhook_id)
        if webhook:
            return jsonify({'webhook_id': webhook_id, 'url': webhook['url'], 'events': webhook['events']})
        return jsonify({'error': 'Webhook not found'}), 404

    elif request.method == 'PUT':
        webhook = webhooks.get(webhook_id)
        if webhook:
            data = request.get_json()
            webhook['url'] = data.get('url', webhook['url'])
            webhook['events'] = data.get('events', webhook['events'])
            return jsonify({'webhook_id': webhook_id, 'status': 'updated'})
        return jsonify({'error': 'Webhook not found'}), 404

    elif request.method == 'DELETE':
        if webhook_id in webhooks:
            del webhooks[webhook_id]
            return jsonify({'webhook_id': webhook_id, 'status': 'deleted'})
        return jsonify({'error': 'Webhook not found'}), 404

@app.route('/webhooks', methods=['GET'])
def get_webhooks():
    return jsonify(list(webhooks.keys()))

# Test class
class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the Flask test client and initialize webhooks dict
        self.app = app.test_client()
        self.app.testing = True
        global webhooks
        webhooks = {}  # Reset the state before each test

    def test_create_webhook(self):
        # Test creating a new webhook successfully
        response = self.app.post('/webhooks', json={
            'webhook_id': '1',
            'url': 'http://example.com',
            'events': ['create', 'update']
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('created', response.get_json()['status'])

    def test_create_webhook_with_missing_fields(self):
        # Test error handling for missing fields
        response = self.app.post('/webhooks', json={
            'webhook_id': '2'  # Missing 'url' and 'events'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing required fields', response.get_json()['error'])

    def test_get_webhook_not_found(self):
        # Test getting a non-existent webhook
        response = self.app.get('/webhooks/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Webhook not found', response.get_json()['error'])

    def test_get_webhook(self):
        # Prepare a webhook and test getting it
        self.app.post('/webhooks', json={
            'webhook_id': '1',
            'url': 'http://example.com',
            'events': ['create', 'update']
        })
        response = self.app.get('/webhooks/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['webhook_id'], '1')

    def test_update_webhook(self):
        # Prepare a webhook and test updating it
        self.app.post('/webhooks', json={
            'webhook_id': '1',
            'url': 'http://example.com',
            'events': ['create', 'update']
        })
        response = self.app.put('/webhooks/1', json={
            'url': 'http://newexample.com',
            'events': ['delete']
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('updated', response.get_json()['status'])

    def test_delete_webhook(self):
        # Prepare a webhook and test deleting it
        self.app.post('/webhooks', json={
            'webhook_id': '1',
            'url': 'http://example.com',
            'events': ['create', 'update']
        })
        response = self.app.delete('/webhooks/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('deleted', response.get_json()['status'])

    def test_get_webhooks(self):
        # Test getting all webhooks
        response = self.app.get('/webhooks')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    

if __name__ == '__main__':
    unittest.main()
