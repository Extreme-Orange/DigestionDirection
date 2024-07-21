import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDL7qj_ZLu-kWaSMOUC6YxEnOh5YyLB_9k')

IDBank = {'Bishan MRT': 'place_id:ChIJ07MziFwX2jERAm3KTMyWP9o', 'Holland Village MRT': 'place_id:ChIJ1yBe2Hsb2jER8wHVEW0wXW0', 'Paya Lebar MRT': 'place_id:ChIJn9toHfIZ2jERUP7cso2BKYs', 'Bugis MRT': 'place_id:ChIJv7v_qp0Z2jER41auJd1oiSg', 'Orchard MRT': 'place_id:ChIJrU6OUTwZ2jERcVW6QTfiJqo', 'Kallang MRT': 'place_id:ChIJsx29uk8Z2jERmPP-HR07M9U', 'Botanic Gardens MRT': 'place_id:ChIJlVLQgy4b2jER0sESh7WlGhs', 'Beauty World MRT': 'place_id:ChIJU30G19ER2jERvfCb3mAcTFs', 'Clementi MRT': 'place_id:ChIJ59bEne0b2jERsbyVF889jkw', 'Geylang Bahru MRT': 'place_id:ChIJy4FlF5AZ2jERJF0GzsbPHdY', 'Newton MRT': 'place_id:ChIJYVk78I0Z2jERLLW9yTTDVHU', 'Harbourfront MRT': 'place_id:ChIJlXwdqs0b2jERnqiRG2DrUXU', 'Buona Vista MRT': 'place_id:ChIJ7e11tPob2jERasVPYICVQAc', 'Jurong East MRT': 'place_id:ChIJOZnDVoYR2jERxNKBNlvzs-g', 'Yishun MRT': 'place_id:ChIJ2wgK6OgV2jERVRIeiIfHVBI', 'Punggol MRT': 'place_id:ChIJx5Q8JZcV2jEREKHBj2RZKOw', 'Stadium MRT': 'place_id:ChIJt__YxmYZ2jERKih8lynJnUY', 'Marina Bay MRT': 'place_id:ChIJYxQaT1IZ2jERLnIZbZPDh3Q', 'Tanjong Pagar MRT': 'place_id:ChIJ8Rzth_kZ2jER0zzZJ9BgiUY', 'Dhoby Ghaut MRT': 'place_id:ChIJkSzRliQZ2jERpcrSSCY7kMM', 'Clarke Quay MRT': 'place_id:ChIJG7Ehmh4Z2jERnKMfkjCawZE', 'City Hall MRT': 'place_id:ChIJR_ZtkaYZ2jERV9J2Cytl6ZM', 'Pasir Ris MRT': 'place_id:ChIJc1a6Akg92jERNgnLXSsjS5s', 'King Albert Park MRT': 'place_id:ChIJx9iN1_YR2jERdqKVXCRKsJQ', 'Hillview MRT': 'place_id:ChIJ34lP7agR2jERrxCtkRz3y-4', 'Great World MRT': 'place_id:ChIJAeN00WAZ2jERRJuNySfxAXg', 'Little India MRT': 'place_id:ChIJo3WI6o0Z2jERpTdJzN1gGyI', 'Novena MRT': 'place_id:ChIJBxjqcBsZ2jERIrw1JbXLHsM', 'Yio Chu Kang MRT': 'place_id:ChIJV4P8oOoW2jERpehfmVXX7ek', 'Sengkang MRT': 'place_id:ChIJO3gfb2wW2jERWnKswyGepDY', 'Sembawang MRT': 'place_id:ChIJG56OlqQT2jERc5j3ppIVMmU', 'Woodlands MRT': 'place_id:ChIJ3VBWhqET2jERzGBRueNKWGk', 'Upper Thomson MRT': 'place_id:ChIJe_9PgNMX2jERwEClesEv90w', 'Springleaf MRT': 'place_id:ChIJ50aywSsR2jERTO5bXvV_qcg', 'Tiong Bahru MRT': 'place_id:ChIJh5-QyX4Z2jER6AS12kg9wwM'}

while True:
    x = input('Location: ')
    if x == 'break':
        break
    else:
        Search = gmaps.places_autocomplete_query(x, offset=None, location=[1.352083 , 103.819836], radius=25000, language=None)
        print(Search[0]['description'], Search[0]['place_id'])
        IDBank[x] = 'place_id:' + Search[0]['place_id']

print(IDBank)