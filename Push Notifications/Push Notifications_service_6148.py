#TODO
import requests
import json

class PushNotification:
    def __init__(self, api_key, auth_secret, app_id, api_url="https://onesignal.com/api/v1"):
        self.api_key = api_key
        self.auth_secret = auth_secret
        self.app_id = app_id
        self.api_url = api_url

    def send_notification(self, message, heading, notification_title, users):
        headers = {
            "Authorization": f"Basic {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "app_id": self.app_id,
            "included_segments": ["All"],
            "data": {"foo": "bar"},
            "contents": {"en": message},
            "headings": {"en": heading},
            "title": {"en": notification_title},
            "filters": [{"field": "tag", "key": "User_ID", "relation": "=", "value": users}]
        }
        response = requests.post(f"{self.api_url}/notifications", headers=headers, data=json.dumps(payload))
        return response.json()

api_key = "YOUR_API_KEY"
auth_secret = "YOUR_AUTH_SECRET"
app_id = "YOUR_APP_ID"
users = ["user1", "user2", "user3"]

pn = PushNotification(api_key, auth_secret, app_id)
response = pn.send_notification("Hello, this is a notification!", "This is a notification", "Notification Title", users)
print(response)