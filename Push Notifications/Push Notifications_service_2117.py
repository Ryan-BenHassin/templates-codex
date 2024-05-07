import requests
import json

class PushNotificationService:
 def __init__(self, api_key, api_secret, proxy=None):
 self.api_key = api_key
 self.api_secret = api_secret
 self.proxy = proxy

 def send_notification(self, title, message, tokens):
 headers = {
 'Content-Type': 'application/json',
 'Authorization': f'Basic {self.api_key}',
 }

 data = {
 'title': title,
 'message': message,
 'tokens': tokens
 }

 response = requests.post(
 f'https://push-notification-service.com/api/push',
 headers=headers,
 data=json.dumps(data),
 proxies=self.proxy
 )

 if response.status_code == 200:
 return True
 else:
 return False

# usage
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
service = PushNotificationService(api_key, api_secret)
title = 'Test Notification'
message = 'This is a test notification'
tokens = ['token1', 'token2', 'token3']

if service.send_notification(title, message, tokens):
 print('Notification sent successfully')
else:
 print('Failed to send notification')
