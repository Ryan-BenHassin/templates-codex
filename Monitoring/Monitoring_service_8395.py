import requests
import time
import json

class MonitoringService:
 def __init__(self, api_key, api_secret, base_url):
 self.api_key = api_key
 self.api_secret = api_secret
 self.base_url = base_url

 def get_system_status(self):
 headers = {
 'X-API-KEY': self.api_key,
 'X-API-SECRET': self.api_secret
 }
 response = requests.get(self.base_url + '/system/status', headers=headers)
 return response.json()

 def get_component_status(self, component_id):
 headers = {
 'X-API-KEY': self.api_key,
 'X-API-SECRET': self.api_secret
 }
 response = requests.get(self.base_url + '/components/' + component_id, headers=headers)
 return response.json()

 def get_incident_history(self):
 headers = {
 'X-API-KEY': self.api_key,
 'X-API-SECRET': self.api_secret
 }
 response = requests.get(self.base_url + '/incidents', headers=headers)
 return response.json()

 def get_maintenance_schedules(self):
 headers = {
 'X-API-KEY': self.api_key,
 'X-API-SECRET': self.api_secret
 }
 response = requests.get(self.base_url + '/maintenance', headers=headers)
 return response.json()

 def get_planned_maintenance(self):
 headers = {
 'X-API-KEY': self.api_key,
 'X-API-SECRET': self.api_secret
 }
 response = requests.get(self.base_url + '/maintenance/planned', headers=headers)
 return response.json()

 def get_unplanned_maintenance(self):
 headers = {
 'X-API-KEY': self.api_key,
 'X-API-SECRET': self.api_secret
 }
 response = requests.get(self.base_url + '/maintenance/unplanned', headers=headers)
 return response.json()

 def get_outage_history(self):
 headers = {
 'X-API-KEY': self.api_key,
 'X-API-SECRET': self.api_secret
 }
 response = requests.get(self.base_url + '/outages', headers=headers)
 return response.json()

 def get_outage_details(self, outage_id):
 headers = {
 'X-API-KEY': self.api_key,
 'X-API-SECRET': self.api_secret
 }
 response = requests.get(self.base_url + '/outages/' + outage_id, headers=headers)
 return response.json()

 def monitor(self):
 while True:
 system_status = self.get_system_status()
 print('System Status:', system_status['status'])
 component_statuses = {}
 for component in system_status['components']:
 component_id = component['id']
 component_status = self.get_component_status(component_id)
 component_statuses[component_id] = component_status
 print('Component', component_id, 'Status:', component_status['status'])
 time.sleep(60)

def main():
 api_key = 'YOUR_API_KEY'
 api_secret = 'YOUR_API_SECRET'
 base_url = 'https://your-maintenance-page.com/api'
 monitoring_service = MonitoringService(api_key, api_secret, base_url)
 monitoring_service.monitor()

if __name__ == '__main__':
 main()
