import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDL7qj_ZLu-kWaSMOUC6YxEnOh5YyLB_9k')

x = gmaps.place('ChIJdZOLiiMR2jERxPWrUs9peIg', session_token=None, fields=None, language=None, reviews_no_translations=False, reviews_sort='most_relevant')
print(x)