import requests
import json

class ShippingService:
 def __init__(self, api_key, api_secret):
 self.api_key = api_key
 self.api_secret = api_secret

 def get_shipping_rates(self, from_zip, to_zip, weight, length, width, height):
 url = "https://api.shipping.com/rates"
 headers = {
 "Authorization": f"Bearer {self.api_key}",
 "Content-Type": "application/json"
 }
 data = {
 "from_zip": from_zip,
 "to_zip": to_zip,
 "weight": weight,
 "length": length,
 "width": width,
 "height": height
 }
 response = requests.post(url, headers=headers, json=data)
 return response.json()

 def create_shipment(self, from_address, to_address, weight, length, width, height):
 url = "https://api.shipping.com/shipments"
 headers = {
 "Authorization": f"Bearer {self.api_key}",
 "Content-Type": "application/json"
 }
 data = {
 "from_address": from_address,
 "to_address": to_address,
 "weight": weight,
 "length": length,
 "width": width,
 "height": height
 }
 response = requests.post(url, headers=headers, json=data)
 return response.json()

 def track_shipment(self, tracking_number):
 url = f"https://api.shipping.com/shipments/{tracking_number}"
 headers = {
 "Authorization": f"Bearer {self.api_key}"
 }
 response = requests.get(url, headers=headers)
 return response.json()

# Example usage:
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
shipping_service = ShippingService(api_key, api_secret)

from_zip = "10001"
to_zip = "20001"
weight = 1
length = 10
width = 10
height = 10

rates = shipping_service.get_shipping_rates(from_zip, to_zip, weight, length, width, height)
print("Shipping Rates:", rates)

from_address = {
 "name": "John Doe",
 "address1": "123 Main St",
 "city": "New York",
 "state": "NY",
 "zip": from_zip
}
to_address = {
 "name": "Jane Doe",
 "address1": "456 Main St",
 "city": "Los Angeles",
 "state": "CA",
 "zip": to_zip
}
shipment = shipping_service.create_shipment(from_address, to_address, weight, length, width, height)
print("Shipment:", shipment)

tracking_number = shipment["tracking_number"]
tracking_info = shipping_service.track_shipment(tracking_number)
print("Tracking Info:", tracking_info)
