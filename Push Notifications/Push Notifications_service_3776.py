#TODO
import requests
import json

class PushNotificationService:
 def __init__(self, api_key, auth_token, app_id):
 self.api_key = api_key
 self.auth_token = auth_token
 self.app_id = app_id

 def send_notification(self, title, message, recipients):
 headers = {
 'Authorization': f'Bearer {self.auth_token}',
 'Content-Type': 'application/json; charset=utf-8'
 }
 data = {
 'app_id': self.app_id,
 'included_segments': ['All'],
 'contents': {'en': message},
 'headings': {'en': title},
 'filters': [{'field': 'tag', 'key': 'User_id', 'relation': 'in', 'value': recipients}]
 }
 response = requests.post(f'https://onesignal.com/api/v1/notifications', headers=headers, data=json.dumps(data))
 if response.status_code == 200:
 print('Notification sent successfully')
 else:
 print('Error sending notification')

if __name__ == '__main__':
 api_key = 'YOUR_ONESIGNAL_API_KEY'
 auth_token = 'YOUR_ONESIGNAL_AUTH_TOKEN'
 app_id = 'YOUR_ONESIGNAL_APP_ID'
 service = PushNotificationService(api_key, auth_token, app_id)
 service.send_notification('Hello', 'This is a test notification', ['USER_ID_1', 'USER_ID_2'])
