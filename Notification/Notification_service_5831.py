#TODO
import requests
import json

class NotificationService:
 def __init__(self, api_key, api_secret, base_url):
 self.api_key = api_key
 self.api_secret = api_secret
 self.base_url = base_url

 def send_notification(self, title, message, recipients):
 auth = (self.api_key, self.api_secret)
 headers = {'Content-type': 'application/json'}
 data = {'title': title, 'message': message, 'recipients': recipients}
 response = requests.post(self.base_url + '/notifications', auth=auth, headers=headers, data=json.dumps(data))
 return response.json()

notification_service = NotificationService('YOUR_API_KEY', 'YOUR_API_SECRET', 'https://example.com/api')
print(notification_service.send_notification('Hello', 'This is a test message', ['user1@example.com', 'user2@example.com']))
