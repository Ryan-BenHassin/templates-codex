#TODO
import yfinance as yf
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

def initialize_analyticsreporting():
    SERVICE_ACCOUNT_FILE = 'path_to_service_account_key.json'
    SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, SCOPES)
    analytics = build('analyticsreporting', 'v4', credentials=credentials)
    return analytics

def get_report(analytics):
    response = analytics.reports().batchGet(
        body={
            'reportRequests': [
                {
                    'viewId': 'your_view_id',
                    'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                    'metrics': [{'expression': 'ga:sessions'}],
                    'dimensions': [{'name': 'ga:browser'}]
                }
            ]
        }).execute()

    for report in response.get('reports', []):
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
        rows = report.get('data', {}).get('rows', [])

        for row in rows:
            dimensions = row.get('dimensions', [])
            dateRangeValues = row.get('metrics', [])

            for header, dimension in zip(dimensionHeaders, dimensions):
                print(f"{header.name}: {dimension}")

            for i, values in enumerate(dateRangeValues):
                print(f"Date range: {i}")
                for metricHeader, value in zip(metricHeaders, values.get('values')):
                    print(f"{metricHeader.get('name')}: {value}")

def main():
    analytics = initialize_analyticsreporting()
    get_report(analytics)

if __name__ == '__main__':
    main()