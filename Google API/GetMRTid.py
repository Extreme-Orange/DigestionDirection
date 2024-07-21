import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDL7qj_ZLu-kWaSMOUC6YxEnOh5YyLB_9k')


Names = list()
id = list()

x = gmaps.places(query='MRT Station', location=[1.352083 , 103.819836], radius=25000, language=None, min_price=None, max_price=None, open_now=False, type=None, region=None, page_token='AUjq9jn4cMRvRC23iWOZ1rxb7VhEFfzeiU__yLq9Ikv-dbLN87xPUKhNKTo2w86M9UP3fC32e92QPs-ZlocmiWfdzEsmhO63CzAO7uXIy3AOPD429WoWcL96eYUc6eiGDGpH92pWRacLSBwv5XAPjW-7ItQNHRVCHtJianKoCEdG4JnTorDvKDsQrGhgwY0LwhWlzC-KShRGGANKykrVvwWVi-L1pnV-EbQxOGcep-kgDtGxNZJZJXRCjE2Fm2reNQefuLODCflV4z2L8R4sYX8C0MF7H_Y-DkBruDZ_ATdz01OjT5-6zmpJeBx1MX7pPydBpuuTvQDiMiFR_Aqu0qWsBX5xaX2JWV_Mf7CywDaajnGhUzZ2jHwpXS2twjkiB3oj_MDqJgQaHVZIC3hVRqbqyfJC1l4LqU42wenByStDm0yh0kbx2hqqX-p5Splq0fGyJtmxJR_47wN-La3sjI4PzHf3bDaatQ0uzk7zPOuXE06j-vr5xF1SOQjZsIlIR6jN2YRnvQevqN7c_T7itxrGKyfwy0TLNDM6f8RR1jEZY70XhoTAklNUfPln-vuw_eWR1dYTCkSBw7eZKQ7mEd7MhCrZK4PZStWJq2Ohysy8sdg-TrPI8Z8Q27xGQ8VKl9I5nEbrPLxrbSbSYfT4a1pcSZzESQ')

for place in x['results']:
    Names.append(place['name'])
    id.append(place['place_id'])

PlaceBank = dict(zip(Names, id))

print(x)