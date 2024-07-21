import requests

url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=restaurant&inputtype=textquery&locationbias=circle%3A500%401.310912%2C103.7951937&fields=name&key=AIzaSyDL7qj_ZLu-kWaSMOUC6YxEnOh5YyLB_9k"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)