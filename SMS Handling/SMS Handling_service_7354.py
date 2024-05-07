import requests
import json

class SMSHandler:
 def __init__(self, api_key, api_secret, from_number, to_number):
 self.api_key = api_key
 self.api_secret = api_secret
 self.from_number = from_number
 self.to_number = to_number

 def send_sms(self, message):
 auth = (self.api_key, self.api_secret)
 headers = {'Content-Type': 'application/x-www-form-urlencoded'}
 data = {'from': self.from_number, 'to': self.to_number, 'text': message}
 response = requests.post('https://api.nexmo.com/sm/pp/v1_msgs', auth=auth, headers=headers, data=data)
 if response.status_code == 200:
 return True
 else:
 return False

# usage
sms_handler = SMSHandler('YOUR_API_KEY', 'YOUR_API_SECRET', 'YOUR_FROM_NUMBER', 'YOUR_TO_NUMBER')
sms_handler.send_sms('Hello from Python!')
