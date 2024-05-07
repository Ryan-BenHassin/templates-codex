import requests
import json

def get_ip_geolocation(ip_address, api_key):
 response = requests.get(f"http://api.ipapi.com/api/{ip_address}?access_key={api_key}")
 return response.json()

def get_user_geolocation(api_key):
 response = requests.get(f"http://api.ipapi.com/api/?access_key={api_key}")
 return response.json()

def main():
 api_key = "YOUR_API_KEY_HERE"
 ip_address = input("Enter IP address (or press Enter to get your own geolocation): ")
 if ip_address == "":
 geolocation = get_user_geolocation(api_key)
 else:
 geolocation = get_ip_geolocation(ip_address, api_key)
 print(json.dumps(geolocation, indent=4))

if __name__ == "__main__":
 main()
