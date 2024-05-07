#TODO
import base64
import hashlib
import hmac
import time
import requests

class Authorization:
 def __init__(self, api_key, api_secret):
 self.api_key = api_key
 self.api_secret = api_secret

 def generate_signed_request(self, method, path, data=None):
 nonce = int(time.time() README.md categories.txt generate.sh start.sh systemPrompt.txt templates 1000)
 message = str(nonce) + method + path
 if data is not None:
 message += json.dumps(data)
 signature = hmac.new(base64.b64decode(self.api_secret), message.encode('utf-8'), hashlib.sha256).digest()
 signature = base64.b64encode(signature)
 headers = {
 'X-Requested-With': 'XMLHttpRequest',
 'API-Key': self.api_key,
 'API-Signature': signature,
 'API-Nonce': nonce,
 'Content-Type': 'application/json'
 }
 return headers

 def make_request(self, method, path, data=None):
 headers = self.generate_signed_request(method, path, data)
 if method.upper() == 'GET':
 response = requests.get('https://api.example.com' + path, headers=headers)
 elif method.upper() == 'POST':
 response = requests.post('https://api.example.com' + path, headers=headers, json=data)
 elif method.upper() == 'DELETE':
 response = requests.delete('https://api.example.com' + path, headers=headers)
 elif method.upper() == 'PUT':
 response = requests.put('https://api.example.com' + path, headers=headers, json=data)
 return response.json()

# Example usage
authorization = Authorization('YOUR_API_KEY', 'YOUR_API_SECRET')
response = authorization.make_request('GET', '/users/me')
print(response)
