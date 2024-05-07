#TODO
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Replace with your own credentials
SERVICE_ACCOUNT_FILE = 'path/to/service_account_key.json'
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
VIEW_ID = 'your_view_id'

def initialize_analyticsreporting():
 credentials = service_account.Credentials.from_service_account_file(
 SERVICE_ACCOUNT_FILE, SCOPES)
 analytics = build('analyticsreporting', 'v4', credentials=credentials)
 return analytics

def get_report(analytics, view_id):
 body = {
 'reportRequests': [{
 'viewId': view_id,
 'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
 'metrics': [{'expression': 'ga:sessions'}],
 'dimensions': [{'name': 'ga:country'}]
 }]
 }
 response = analytics.reports().batchGet(body=body).execute()
 return response

def print_response(response):
 for report in response.get('reports', []):
 columnHeader = report.get('columnHeader', {})
 dimensionHeaders = columnHeader.get('dimensions', [])
 metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
 rows = report.get('data', {}).get('rows', [])

 for row in rows:
 dimensions = row.get('dimensions', [])
 dateRangeValues = row.get('metrics', [])

 for header, dimension in zip(dimensionHeaders, dimensions):
 print(f'{header.name}: {dimension}')

 for i, values in enumerate(dateRangeValues):
 for metricHeader, value in zip(metricHeaders, values.get('values', [])):
 print(f'{metricHeader.getName()}: {value}')

def main():
 analytics = initialize_analyticsreporting()
 response = get_report(analytics, VIEW_ID)
 print_response(response)

if __name__ == '__main__':
 main()
