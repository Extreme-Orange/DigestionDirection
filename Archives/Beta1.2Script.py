import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDL7qj_ZLu-kWaSMOUC6YxEnOh5YyLB_9k')

# Defining Things
Distances = list()
count1 = 0
total_dist1 = 0
total_dist2 = 0
total_dist3 = 0
total_dist4 = 0
total_dist5 = 0
total_dist6 = 0
winner = 1000000000000000000000000000000
AllLocations = dict()

# Place ID Bank
AllLocations['kent ridge mrt'] = "place_id:ChIJ_9hQHswb2jERDyOL3-rPBxg"
AllLocations['tkk mrt'] = "place_id:ChIJg1WsVaQb2jERE33zorzUq9g"
AllLocations['serangoon mrt'] = "place_id:ChIJMSKsChcX2jERPC0Poz3FmWg"
AllLocations['bedok mrt'] = "place_id:ChIJa39INRYj2jERxbk9IQPVo8I"
bishan_mrt = "place_id:ChIJ07MziFwX2jERAm3KTMyWP9o"
holland_village_mrt = "place_id:ChIJ1yBe2Hsb2jER8wHVEW0wXW0"
paya_lebar_mrt = "place_id:ChIJn9toHfIZ2jERUP7cso2BKYs"
bugis_mrt = "place_id:ChIJv7v_qp0Z2jER41auJd1oiSg"
orchard_mrt = "place_id:ChIJrU6OUTwZ2jERcVW6QTfiJqo"
kallang_mrt = "place_id:ChIJsx29uk8Z2jERmPP-HR07M9U"


# Running Google API
Matrix = gmaps.distance_matrix([bishan_mrt, holland_village_mrt, paya_lebar_mrt, bugis_mrt, orchard_mrt, kallang_mrt], [AllLocations[str.lower(input("First Location: "))], AllLocations[str.lower(input("Second Location: "))]], mode="transit", language=None, avoid=None, units=None, departure_time=None, arrival_time=None, transit_mode=["bus", "rail"], transit_routing_preference=None, traffic_model=None, region=None)


# Tuple of all middle locations
MiddleLocations = ('Bishan MRT', 'Holland Village MRT', 'Paya Lebar MRT', 'Bugis', 'Orchard MRT', 'Kallang MRT')

# Extracts distances, adds relevant pairs, then puts the sum into a tuple
for L1 in Matrix['rows']:
    for L2 in L1['elements']:
        if count1 == 0:
            total_dist1 = total_dist1 + L2['distance']['value']
            count1 = count1 + 1
        elif count1 == 1:
            total_dist1 = total_dist1 + L2['distance']['value']
            Distances.append(total_dist1)
            count1 = count1 + 1
        elif count1 == 2:
            total_dist2 = total_dist2 + L2['distance']['value']
            count1 = count1 + 1
        elif count1 == 3:
            total_dist2 = total_dist2 + L2['distance']['value']
            Distances.append(total_dist2)
            count1 = count1 + 1
        elif count1 == 4:
            total_dist3 = total_dist3 + L2['distance']['value']
            count1 = count1 + 1
        elif count1 == 5:
            total_dist3 = total_dist3 + L2['distance']['value']
            Distances.append(total_dist3)
            count1 = count1 + 1
        elif count1 == 6:
            total_dist4 = total_dist4 + L2['distance']['value']
            count1 = count1 + 1
        elif count1 == 7:
            total_dist4 = total_dist4 + L2['distance']['value']
            Distances.append(total_dist4)
            count1 = count1 + 1
        elif count1 == 8:
            total_dist5 = total_dist5 + L2['distance']['value']
            count1 = count1 + 1
        elif count1 == 9:
            total_dist5 = total_dist5 + L2['distance']['value']
            Distances.append(total_dist5)
            count1 = count1 + 1
        elif count1 == 10:
            total_dist6 = total_dist6 + L2['distance']['value']
            count1 = count1 + 1
        elif count1 == 11:
            total_dist6 = total_dist6 + L2['distance']['value']
            Distances.append(total_dist6)
            count1 = count1 + 1


# Inserts middle locations as dictionary values
Main = dict(zip(Distances, MiddleLocations))


# Compares the total distances and prints the winning middle location
for d, l in Main.items():
    if d < winner:
        winner = d
    else:
        continue
print(f"You should go to {Main[winner]}")