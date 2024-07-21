import requests

url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJIQ4seGoa2jERoXJVVkJefFs&fields=name%2Cgeometry&key=AIzaSyDL7qj_ZLu-kWaSMOUC6YxEnOh5YyLB_9k"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)