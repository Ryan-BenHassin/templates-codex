import requests
import json

class ShippingService:
 def __init__(self, api_key, api_secret):
 self.api_key = api_key
 self.api_secret = api_secret

 def get_shipping_rates(self, origin, destination, package):
 url = "https://shipping-api.com/rates"
 auth = (self.api_key, self.api_secret)
 data = {
 "origin": origin,
 "destination": destination,
 "package": package
 }
 response = requests.post(url, auth=auth, json=data)
 return response.json()

 def schedule_delivery(self, shipment_id, pickup_date, delivery_date):
 url = f"https://shipping-api.com/shipments/{shipment_id}/schedule"
 auth = (self.api_key, self.api_secret)
 data = {
 "pickup_date": pickup_date,
 "delivery_date": delivery_date
 }
 response = requests.patch(url, auth=auth, json=data)
 return response.json()

 def track_shipment(self, shipment_id):
 url = f"https://shipping-api.com/shipments/{shipment_id}/track"
 auth = (self.api_key, self.api_secret)
 response = requests.get(url, auth=auth)
 return response.json()

api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
shipping_service = ShippingService(api_key, api_secret)

origin = {"address": "123 Main St", "city": "Anytown", "state": "CA", "zip": "12345"}
destination = {"address": "456 Elm St", "city": "Othertown", "state": "NY", "zip": "67890"}
package = {"weight": 10, "length": 10, "width": 10, "height": 10}

rates = shipping_service.get_shipping_rates(origin, destination, package)
print(rates)

shipment_id = "YOUR_SHIPMENT_ID"
pickup_date = "2023-03-01"
delivery_date = "2023-03-05"
schedule_response = shipping_service.schedule_delivery(shipment_id, pickup_date, delivery_date)
print(schedule_response)

tracking_response = shipping_service.track_shipment(shipment_id)
print(tracking_response)
