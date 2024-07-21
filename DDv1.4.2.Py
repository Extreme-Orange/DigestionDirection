import telebot
from telebot import TeleBot, types, custom_filters
from telebot.custom_filters import TextFilter, TextMatchFilter, IsReplyFilter
import googlemaps
from datetime import datetime


# APIs
gmaps = googlemaps.Client(key='AIzaSyDL7qj_ZLu-kWaSMOUC6YxEnOh5YyLB_9k')
bot = telebot.TeleBot("6147055066:AAFvMRD41FTtRdF8q6v8jaqqSJmSPWsh5P8")


# Defining Things
user_inputs = dict()
IDBank = {'Bishan MRT': 'place_id:ChIJ07MziFwX2jERAm3KTMyWP9o', 'Holland Village MRT': 'place_id:ChIJ1yBe2Hsb2jER8wHVEW0wXW0', 'Paya Lebar MRT': 'place_id:ChIJn9toHfIZ2jERUP7cso2BKYs', 'Bugis MRT': 'place_id:ChIJv7v_qp0Z2jER41auJd1oiSg', 'Orchard MRT': 'place_id:ChIJrU6OUTwZ2jERcVW6QTfiJqo', 'Beauty World MRT': 'place_id:ChIJU30G19ER2jERvfCb3mAcTFs', 'Clementi MRT': 'place_id:ChIJ59bEne0b2jERsbyVF889jkw', 'Geylang Bahru MRT': 'place_id:ChIJy4FlF5AZ2jERJF0GzsbPHdY', 'Newton MRT': 'place_id:ChIJYVk78I0Z2jERLLW9yTTDVHU', 'Harbourfront MRT': 'place_id:ChIJlXwdqs0b2jERnqiRG2DrUXU', 'Buona Vista MRT': 'place_id:ChIJ7e11tPob2jERasVPYICVQAc', 'Jurong East MRT': 'place_id:ChIJOZnDVoYR2jERxNKBNlvzs-g', 'Yishun MRT': 'place_id:ChIJ2wgK6OgV2jERVRIeiIfHVBI', 'Stadium MRT': 'place_id:ChIJt__YxmYZ2jERKih8lynJnUY', 'Marina Bay MRT': 'place_id:ChIJYxQaT1IZ2jERLnIZbZPDh3Q', 'Tanjong Pagar MRT': 'place_id:ChIJ8Rzth_kZ2jER0zzZJ9BgiUY', 'Clarke Quay MRT': 'place_id:ChIJG7Ehmh4Z2jERnKMfkjCawZE', 'City Hall MRT': 'place_id:ChIJR_ZtkaYZ2jERV9J2Cytl6ZM', 'King Albert Park MRT': 'place_id:ChIJx9iN1_YR2jERdqKVXCRKsJQ', 'Hillview MRT': 'place_id:ChIJ34lP7agR2jERrxCtkRz3y-4', 'Great World MRT': 'place_id:ChIJAeN00WAZ2jERRJuNySfxAXg', 'Little India MRT': 'place_id:ChIJo3WI6o0Z2jERpTdJzN1gGyI', 'Yio Chu Kang MRT': 'place_id:ChIJV4P8oOoW2jERpehfmVXX7ek', 'Upper Thomson MRT': 'place_id:ChIJe_9PgNMX2jERwEClesEv90w', 'Springleaf MRT': 'place_id:ChIJ50aywSsR2jERTO5bXvV_qcg'}

# Welcome Message
@bot.message_handler(commands=['start'])
def welcome_message(message):
      bot.send_message(message.chat.id, "Hi! I'm designed to help you and your friends decide where to meet up! If you provide me with 2-4 starting locations, I will generate the top 3 MRT locations that are the most ideal!\n\nSimply send me the locations of your choice (I will autocomplete based on your text), then type /run\n\nIf you want to use the bot again, you must type /reset. If you need a list commands, type /help")
      bot.send_message(message.chat.id, "What's your first starting location?")
      bot.send_message(chat_id=229962481, text=f"{message.from_user.first_name} has started using this bot")
      print(f"{message.from_user.first_name} has started using this bot")


# Help
@bot.message_handler(commands=['help'])
def possible_locations(message):
      bot.send_message(message.chat.id, "/start, /help, /reset, /run")


# Generate output
@bot.message_handler(commands=['run'])
def run(message):
        distances = list()
        distance_sums = list()
        MiddleLocations = list()
        if len(user_inputs[message.from_user.first_name]) == 0:
            bot.send_message(message.chat.id, "Please input two more locations")
        elif len(user_inputs[message.from_user.first_name]) == 1:
            bot.send_message(message.chat.id, "Please input one more location")
        elif len(user_inputs[message.from_user.first_name]) == 2:
            try:
                for x, y in IDBank.items():
                    MiddleLocations.append(y)
                Matrix = gmaps.distance_matrix([MiddleLocations[z] for z in range(0, len(MiddleLocations))], [f"place_id:{list(user_inputs[message.from_user.first_name])[0]}", f"place_id:{list(user_inputs[message.from_user.first_name])[1]}"], mode="transit", language=None, avoid=None, units=None, departure_time=None, arrival_time=None, transit_mode=["bus", "rail"], transit_routing_preference=None, traffic_model=None, region=None)
                for L1 in Matrix['rows']:
                    for L2 in L1['elements']:
                        distances.append(L2['distance']['value'])
                for i in range(0, len(distances), 2):
                    pair_sum = distances[i] + distances[i+1]
                    distance_sums.append(pair_sum)
                Main = dict(zip(distance_sums, tuple(IDBank.keys())))
                bot.send_message(message.chat.id, f"Here are your Top 3 best options:\n1. {sorted(Main.items())[0][1]}\n2. {sorted(Main.items())[1][1]}\n3. {sorted(Main.items())[2][1]}")
                bot.send_message(chat_id=229962481, text=f"{message.from_user.first_name} has received\n1. {sorted(Main.items())[0][1]}\n2. {sorted(Main.items())[1][1]}\n3. {sorted(Main.items())[2][1]}\nas their end locations")
                print(f"{message.from_user.first_name} has received\n1. {sorted(Main.items())[0][1]}\n2. {sorted(Main.items())[1][1]}\n3. {sorted(Main.items())[2][1]}\nas their end locations")
            except:
                bot.send_message(message.chat.id, "Unexpected Error. Try again but with different but similar locations")
                bot.send_message(chat_id=229962481, text=f"Error encountered by {message.from_user.first_name}")
                print(f"Error encountered by {message.from_user.first_name}")
        elif len(user_inputs[message.from_user.first_name]) == 3:
            try:
                for x, y in IDBank.items():
                    MiddleLocations.append(y)
                Matrix = gmaps.distance_matrix([MiddleLocations[z] for z in range(0, len(MiddleLocations))], [f"place_id:{list(user_inputs[message.from_user.first_name])[0]}", f"place_id:{list(user_inputs[message.from_user.first_name])[1]}", f"place_id:{list(user_inputs[message.from_user.first_name])[2]}"], mode="transit", language=None, avoid=None, units=None, departure_time=None, arrival_time=None, transit_mode=["bus", "rail"], transit_routing_preference=None, traffic_model=None, region=None)
                for L1 in Matrix['rows']:
                    for L2 in L1['elements']:
                        distances.append(L2['distance']['value'])
                for i in range(0, len(distances), 3):
                    pair_sum = distances[i] + distances[i+1] + distances[i+2]
                    distance_sums.append(pair_sum)
                Main = dict(zip(distance_sums, tuple(IDBank.keys())))
                bot.send_message(message.chat.id, f"Here are your Top 3 best options:\n1. {sorted(Main.items())[0][1]}\n2. {sorted(Main.items())[1][1]}\n3. {sorted(Main.items())[2][1]}")
                bot.send_message(chat_id=229962481, text=f"{message.from_user.first_name} has received\n1. {sorted(Main.items())[0][1]}\n2. {sorted(Main.items())[1][1]}\n3. {sorted(Main.items())[2][1]}\nas their end locations")
                print(f"{message.from_user.first_name} has received\n1. {sorted(Main.items())[0][1]}\n2. {sorted(Main.items())[1][1]}\n3. {sorted(Main.items())[2][1]}\nas their end locations")
            except:
                bot.send_message(message.chat.id, "Unexpected Error. Try again but with different but similar locations")
                bot.send_message(chat_id=229962481, text=f"Error encountered by {message.from_user.first_name}")
                print(f"Error encountered by {message.from_user.first_name}")
        elif len(user_inputs[message.from_user.first_name]) == 4:
            try:
                for x, y in IDBank.items():
                    MiddleLocations.append(y)
                Matrix = gmaps.distance_matrix([MiddleLocations[z] for z in range(0, len(MiddleLocations))], [f"place_id:{list(user_inputs[message.from_user.first_name])[0]}", f"place_id:{list(user_inputs[message.from_user.first_name])[1]}", f"place_id:{list(user_inputs[message.from_user.first_name])[2]}", f"place_id:{list(user_inputs[message.from_user.first_name])[3]}"], mode="transit", language=None, avoid=None, units=None, departure_time=None, arrival_time=None, transit_mode=["bus", "rail"], transit_routing_preference=None, traffic_model=None, region=None)
                for L1 in Matrix['rows']:
                    for L2 in L1['elements']:
                        distances.append(L2['distance']['value'])
                for i in range(0, len(distances), 4):
                    pair_sum = distances[i] + distances[i+1] + distances[i+2] + distances[i+3]
                    distance_sums.append(pair_sum)
                Main = dict(zip(distance_sums, tuple(IDBank.keys())))
                bot.send_message(message.chat.id, f"Here are your Top 3 best options:\n1. {sorted(Main.items())[0][1]}\n2. {sorted(Main.items())[1][1]}\n3. {sorted(Main.items())[2][1]}")
                bot.send_message(chat_id=229962481, text=f"{message.from_user.first_name} has received\n1. {sorted(Main.items())[0][1]}\n2. {sorted(Main.items())[1][1]}\n3. {sorted(Main.items())[2][1]}\nas their end locations")
                print(f"{message.from_user.first_name} has received\n1. {sorted(Main.items())[0][1]}\n2. {sorted(Main.items())[1][1]}\n3. {sorted(Main.items())[2][1]}\nas their end locations")
            except:
                bot.send_message(message.chat.id, "Unexpected Error. Try again but with different but similar location")
                bot.send_message(chat_id=229962481, text=f"Error encountered by {message.from_user.first_name}")
                print(f"Error encountered by {message.from_user.first_name}")


# Debug
@bot.message_handler(commands=['debug'])
def debug(message):
    print()

# Reset
@bot.message_handler(commands=['reset'])
def reset(message):
    try:
        user_inputs[message.from_user.first_name].clear()
        bot.send_message(message.chat.id, "Done")
    except:
        bot.send_message(message.chat.id, "No existing input")


#After first location
@bot.message_handler(func=lambda m: True)
def location(message):
    try:
        Search = gmaps.places_autocomplete(f"{message.text}", session_token=None, offset=None, origin=None, location=None, radius=None, language=None, types=None, components={'country': ['SG']}, strict_bounds=False)
        if message.from_user.first_name not in user_inputs:
            bot.send_message(message.chat.id, f"First Location: {Search[0]['description']}\n\nNow send me another location!")
            user_inputs[message.from_user.first_name] = {Search[0]['place_id']}
        else:            
            if len(user_inputs[message.from_user.first_name]) == 4:
                bot.send_message(message.chat.id, "Maximum number of locations reached. Use /reset to input new locations.")
            elif len (user_inputs[message.from_user.first_name]) == 3:
                bot.send_message(message.chat.id, f"Fourth Location: {Search[0]['description']}\n\nNow do /run")
                user_inputs[message.from_user.first_name].add(f"{Search[0]['place_id']}")
            elif len (user_inputs[message.from_user.first_name]) == 2:
                bot.send_message(message.chat.id, f"Third Location: {Search[0]['description']}\n\nNow send me another location or do /run")
                user_inputs[message.from_user.first_name].add(f"{Search[0]['place_id']}")
            elif len (user_inputs[message.from_user.first_name]) == 1:
                bot.send_message(message.chat.id, f"Second Location: {Search[0]['description']}\n\nNow send me another location or do /run")
                user_inputs[message.from_user.first_name].add(f"{Search[0]['place_id']}")
            else:
                bot.send_message(message.chat.id, f"First Location: {Search[0]['description']}\n\nNow send me another location!")
                user_inputs[message.from_user.first_name].add(f"{Search[0]['place_id']}")
    except:
        bot.send_message(message.chat.id, "Error, Invalid Location. More details might help.")
        bot.send_message(chat_id=229962481, text=f"Invalid Location encountered by {message.from_user.first_name}")
        print(f"Invalid Location encountered by {message.from_user.first_name}")


# Do not forget to register filters
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(IsReplyFilter())


bot.infinity_polling()