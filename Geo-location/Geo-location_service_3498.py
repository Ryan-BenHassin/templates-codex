import requests
import json

def get_geo_location(ip_address, api_key):
 response = requests.get(f'http://api.ipapi.com/api/{ip_address}?access_key={api_key}')
 data = response.json()
 return data

def main():
 ip_address = input("Enter IP Address: ")
 api_key = "YOUR_API_KEY_HERE"
 geo_location = get_geo_location(ip_address, api_key)
 print("Country: ", geo_location['country_name'])
 print("Region: ", geo_location['region'])
 print("City: ", geo_location['city'])
 print("Latitude: ", geo_location['latitude'])
 print("Longitude: ", geo_location['longitude'])

if __name__ == "__main__":
 main()
