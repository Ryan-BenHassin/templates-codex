#TODO
import requests
import json

def get_geo_location(ip_address, api_key):
 url = f"http://api.ipstack.com/{ip_address}?access_key={api_key}&output=json&legacy=1"
 response = requests.get(url)
 data = response.json()
 return data

def main():
 ip_address = input("Enter IP address: ")
 api_key = "YOUR_API_KEY_HERE"
 geo_data = get_geo_location(ip_address, api_key)
 print("IP Address: ", geo_data['ip'])
 print("Country: ", geo_data['country_name'])
 print("Region: ", geo_data['region_name'])
 print("City: ", geo_data['city'])
 print("Latitude: ", geo_data['latitude'])
 print("Longitude: ", geo_data['longitude'])

if __name__ == "__main__":
 main()
