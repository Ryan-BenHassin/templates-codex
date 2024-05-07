#TODO
import requests
import json
import datetime

class Analytics:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api.example.com/analytics"

    def get_users(self):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(f"{self.base_url}/users", headers=headers)
        return response.json()

    def get_user_details(self, user_id):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(f"{self.base_url}/users/{user_id}", headers=headers)
        return response.json()

    def track_event(self, user_id, event_name, event_data):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "user_id": user_id,
            "event_name": event_name,
            "event_data": event_data,
            "timestamp": datetime.datetime.now().isoformat()
        }
        response = requests.post(f"{self.base_url}/events", headers=headers, json=data)
        return response.json()

    def get_events(self, user_id):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(f"{self.base_url}/users/{user_id}/events", headers=headers)
        return response.json()

analytics = Analytics("YOUR_API_KEY", "YOUR_API_SECRET")

# Example usage:
users = analytics.get_users()
print(users)

user_details = analytics.get_user_details(1)
print(user_details)

event_response = analytics.track_event(1, "button_clicked", {"button_name": "Click me"})
print(event_response)

events = analytics.get_events(1)
print(events)