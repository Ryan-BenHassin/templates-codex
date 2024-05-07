import hashlib
import hmac
import time
import requests

class Authentication:
 def __init__(self, api_key, api_secret):
 self.api_key = api_key
 self.api_secret = api_secret

 def _generate_signature(self, method, url, params, body):
 timestamp = int(time.time() README.md categories.txt generate.sh start.sh systemPrompt.txt templates 1000)
 message = f"{timestamp}{method.upper()}{url}"
 if params:
 message += "?" + "&".join(f"{key}={value}" for key, value in params.items())
 if body:
 message += json.dumps(body)
 signature = hmac.new(bytearray(self.api_secret, "utf-8"), bytearray(message, "utf-8"), hashlib.sha256).hexdigest()
 return timestamp, signature

 def _send_request(self, method, url, params=None, body=None):
 timestamp, signature = self._generate_signature(method, url, params, body)
 headers = {
 "API-KEY": self.api_key,
 "API-SIGNATURE": signature,
 "API-TIMESTAMP": str(timestamp)
 }
 response = requests.request(method, url, params=params, json=body, headers=headers)
 response.raise_for_status()
 return response.json()

 def get(self, url, params=None):
 return self._send_request("GET", url, params)

 def post(self, url, body):
 return self._send_request("POST", url, body=body)

 def put(self, url, body):
 return self._send_request("PUT", url, body=body)

 def delete(self, url):
 return self._send_request("DELETE", url)

# Example usage
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
auth = Authentication(api_key, api_secret)
print(auth.get("https://example.com/api/endpoint"))
print(auth.post("https://example.com/api/endpoint", {"key": "value"}))
