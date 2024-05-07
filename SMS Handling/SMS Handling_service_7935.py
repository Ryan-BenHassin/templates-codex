import requests

class SmsHandler:
 def __init__(self, api_key, api_secret, sender_id):
 self.api_key = api_key
 self.api_secret = api_secret
 self.sender_id = sender_id

 def send_sms(self, recipient, message):
 auth = (self.api_key, self.api_secret)
 data = {
 "from": self.sender_id,
 "to": recipient,
 "text": message
 }
 response = requests.post("https://api.sms.service.com/messages", auth=auth, json=data)
 if response.status_code == 202:
 return True
 else:
 return False

# usage
sms_handler = SmsHandler("YOUR_API_KEY", "YOUR_API_SECRET", "YOUR_SENDER_ID")
if sms_handler.send_sms("RECIPIENT_PHONE_NUMBER", "Hello!"):
 print("SMS sent successfully")
else:
 print("Failed to send SMS")
