#TODO
import requests
import json

class ThirdPartyIntegration:
 def __init__(self, api_key, api_secret):
 self.api_key = api_key
 self.api_secret = api_secret
 self.base_url = "https://api.thirdparty.com/v1"

 def send_request(self, endpoint, data, method):
 headers = {
 "Authorization": f"Bearer {self.api_key}",
 "Content-Type": "application/json"
 }
 response = requests.request(method, f"{self.base_url}/{endpoint}", headers=headers, json=data)
 return response.json()

 def get_user_data(self, user_id):
 return self.send_request(f"users/{user_id}", {}, "GET")

 def create_order(self, order_data):
 return self.send_request("orders", order_data, "POST")

 def send_notification(self, notification_data):
 return self.send_request("notifications", notification_data, "POST")

# Usage
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
tpi = ThirdPartyIntegration(api_key, api_secret)
user_data = tpi.get_user_data("12345")
print(user_data)
order_response = tpi.create_order({"item": "Widget", "quantity": 2})
print(order_response)
notification_response = tpi.send_notification({"message": "Hello, world!"})
print(notification_response)
