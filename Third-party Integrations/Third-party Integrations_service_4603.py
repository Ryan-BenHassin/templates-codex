#TODO
import requests
import json

class ThirdPartyIntegrations:
 def __init__(self, api_key, api_secret, api_url):
 self.api_key = api_key
 self.api_secret = api_secret
 self.api_url = api_url

 def send_request(self, endpoint, payload=None):
 headers = {
 'Authorization': f'Bearer {self.api_key}',
 'Content-Type': 'application/json'
 }
 if payload:
 response = requests.post(f'{self.api_url}/{endpoint}', headers=headers, json=payload)
 else:
 response = requests.get(f'{self.api_url}/{endpoint}', headers=headers)
 return response.json()

 def get_integration_list(self):
 return self.send_request('integrations')

 def create_integration(self, name, description, callback_url):
 payload = {
 'name': name,
 'description': description,
 'callback_url': callback_url
 }
 return self.send_request('integrations', payload)

 def delete_integration(self, integration_id):
 return self.send_request(f'integrations/{integration_id}', method='DELETE')

api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
api_url = 'https://api.example.com'

integration_service = ThirdPartyIntegrations(api_key, api_secret, api_url)

# Example usage
print(integration_service.get_integration_list())
print(integration_service.create_integration('My Integration', 'This is a test integration', 'https://example.com/callback'))
print(integration_service.delete_integration('integration_id'))
