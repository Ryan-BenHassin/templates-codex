#TODO
import requests
import json

class DataService:
 def __init__(self, api_key):
 self.api_key = api_key
 self.base_url = "https://api.data.gov"

 def get_data(self, dataset, params):
 url = f"{self.base_url}/{dataset}"
 headers = {"Authorization": f"Bearer {self.api_key}"}
 response = requests.get(url, headers=headers, params=params)
 return response.json()

 def get_datasets(self):
 url = f"{self.base_url}/datasets"
 headers = {"Authorization": f"Bearer {self.api_key}"}
 response = requests.get(url, headers=headers)
 return response.json()

api_key = "YOUR_API_KEY_HERE"
data_service = DataService(api_key)

# Example usage:
datasets = data_service.get_datasets()
print(json.dumps(datasets, indent=4))

params = {"year": "2020", "category": "Agriculture"}
data = data_service.get_data("commodity-pilot-programs", params)
print(json.dumps(data, indent=4))
