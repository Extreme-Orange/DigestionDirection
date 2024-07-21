import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDL7qj_ZLu-kWaSMOUC6YxEnOh5YyLB_9k')

kent_ridge_mrt = "place_id:ChIJ_9hQHswb2jERDyOL3-rPBxg"
tkk_mrt = "place_id:ChIJg1WsVaQb2jERE33zorzUq9g"
serangoon_mrt = "place_id:ChIJMSKsChcX2jERPC0Poz3FmWg"
bedok_mrt = "place_id:ChIJa39INRYj2jERxbk9IQPVo8I"
bishan_mrt = "place_id:ChIJ07MziFwX2jERAm3KTMyWP9o"
holland_village_mrt = "place_id:ChIJ1yBe2Hsb2jER8wHVEW0wXW0"
paya_lebar_mrt = "place_id:ChIJn9toHfIZ2jERUP7cso2BKYs"
bugis_mrt = "place_id:ChIJv7v_qp0Z2jER41auJd1oiSg"
orchard_mrt = "place_id:ChIJrU6OUTwZ2jERcVW6QTfiJqo"
kalland_mrt = "place_id:ChIJsx29uk8Z2jERmPP-HR07M9U"

Matrix = gmaps.distance_matrix([holland_village_mrt, bugis_mrt], [kent_ridge_mrt, tkk_mrt], mode="transit", language=None, avoid=None, units=None, departure_time=None, arrival_time=None, transit_mode=["bus", "rail"], transit_routing_preference=None, traffic_model=None, region=None)
print(Matrix)

# The path to any distance value is: PossibleLocations['rows'][1]['elements'][1]['distance']['value']). First number represents origin location, second number represents destination location.

for L1 in Matrix['rows']:
    for L2 in L1['elements']:
        print(L2['distance']['value'])