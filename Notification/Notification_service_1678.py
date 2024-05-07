#TODO
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from twilio.rest import Client

app = Flask(__name__)
api = Api(app)

# Replace with your Twilio accountSid and authToken
account_sid = "your_account_sid"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

class Notification(Resource):
    def post(self):
        data = request.get_json()
        to_number = data['to_number']
        message = data['message']
        message = client.messages.create(
            from_='your_twilio_number',
            to=to_number,
            body=message
        )
        return jsonify({'message': 'Notification sent successfully'})

api.add_resource(Notification, '/notification')

if __name__ == '__main__':
    app.run(debug=True)