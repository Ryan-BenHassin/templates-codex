import requests
import json

class AuthService:
 def __init__(self, client_id, client_secret, username, password):
 self.client_id = client_id
 self.client_secret = client_secret
 self.username = username
 self.password = password

 def get_token(self):
 auth = (self.client_id, self.client_secret)
 data = {'grant_type': 'password', 'username': self.username, 'password': self.password}
 response = requests.post('https://your_auth_server.com/token', auth=auth, data=data)
 if response.status_code == 200:
 return response.json()['access_token']
 else:
 return None

 def get_authorized_request(self, url, method='GET', data=None):
 token = self.get_token()
 if token:
 headers = {'Authorization': 'Bearer ' + token}
 if method.upper() == 'GET':
 response = requests.get(url, headers=headers)
 elif method.upper() == 'POST':
 response = requests.post(url, headers=headers, json=data)
 return response
 else:
 return None

# usage
client_id = 'your_client_id'
client_secret = 'your_client_secret'
username = 'your_username'
password = 'your_password'

auth_service = AuthService(client_id, client_secret, username, password)
response = auth_service.get_authorized_request('https://your_request_url.com/api/data')
print(response.json())
