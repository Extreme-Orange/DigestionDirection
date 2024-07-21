import requests

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=1.310912%2C103.7951937&radius=200&type=restaurant&key=AIzaSyDL7qj_ZLu-kWaSMOUC6YxEnOh5YyLB_9k"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)