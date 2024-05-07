import json
import requests

class ReportingService:
 def __init__(self, api_key, api_secret):
 self.api_key = api_key
 self.api_secret = api_secret

 def get_reports(self, start_date, end_date, metrics):
 headers = {
 'X-API-KEY': self.api_key,
 'X-API-SECRET': self.api_secret
 }
 data = {
 'start_date': start_date,
 'end_date': end_date,
 'metrics': metrics
 }
 response = requests.post('https://reporting-service.com/reports', headers=headers, json=data)
 return response.json()

 def get_report(self, report_id):
 headers = {
 'X-API-KEY': self.api_key,
 'X-API-SECRET': self.api_secret
 }
 response = requests.get(f'https://reporting-service.com/reports/{report_id}', headers=headers)
 return response.json()

 def generate_report(self, report_name, metrics):
 headers = {
 'X-API-KEY': self.api_key,
 'X-API-SECRET': self.api_secret
 }
 data = {
 'report_name': report_name,
 'metrics': metrics
 }
 response = requests.post('https://reporting-service.com/reports/generate', headers=headers, json=data)
 return response.json()

api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
reporting_service = ReportingService(api_key, api_secret)

# Example usage
start_date = '2022-01-01'
end_date = '2022-01-31'
metrics = ['impressions', 'clicks', 'conversions']
report_id = 'REPORT_ID'

reports = reporting_service.get_reports(start_date, end_date, metrics)
report = reporting_service.get_report(report_id)
new_report = reporting_service.generate_report('My Report', metrics)

print(reports)
print(report)
print(new_report)
