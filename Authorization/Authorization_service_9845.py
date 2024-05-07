#TODO
import base64
import hashlib
import hmac
import time
import requests
import json  # Importing json for handling JSON body data

class Authorization:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def generate_signed_request(self, method, path, data=None):
        nonce = int(time.time() * 1000)  # Fixed syntax for multiplying time by 1000
        message = str(nonce) + method.upper() + path
        if data is not None:
            message += json.dumps(data)
        signature = hmac.new(base64.b64decode(self.api_secret), message.encode('utf-8'), hashlib.sha256).digest()
        signature = base64.b64encode(signature).decode('utf-8')  # Decoding for header compatibility
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'API-Key': self.api_key,
            'API-Signature': signature,
            'API-Nonce': str(nonce),  # Ensuring nonce is a string for headers
            'Content-Type': 'application/json'
        }
        return headers

    def make_request(self, method, path, data=None):
        headers = self.generate_signed_request(method, path, data)
        url = 'https://api.example.com' + path
        if method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers, json=data)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, headers=headers)
        elif method.upper() == 'PUT':
            response = requests.put(url, headers=headers, json=data)
        else:
            raise ValueError("Unsupported HTTP method")
        return response.json()

# Example usage
authorization = Authorization('YOUR_API_KEY', 'YOUR_API_SECRET')
response = authorization.make_request('GET', '/users/me')
print(response)
