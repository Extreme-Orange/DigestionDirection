import telebot
from telebot import TeleBot, types, custom_filters
from telebot.custom_filters import TextFilter, TextMatchFilter, IsReplyFilter
import googlemaps
from datetime import datetime


# APIs
gmaps = googlemaps.Client(key='AIzaSyDL7qj_ZLu-kWaSMOUC6YxEnOh5YyLB_9k')
bot = telebot.TeleBot("6147055066:AAFvMRD41FTtRdF8q6v8jaqqSJmSPWsh5P8")


# Defining Things
Distances = list()
AllLocations = dict()
user_inputs = dict()
PossibleLocations = {'kent ridge mrt', 'serangoon mrt', 'bedok mrt', 'tkk mrt'}
MiddleLocations = ('Bishan MRT', 'Holland Village MRT', 'Paya Lebar MRT', 'Bugis MRT', 'Orchard MRT', 'Kallang MRT')


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


# Welcome Message
@bot.message_handler(commands=['start'])
def welcome_message(message):
      bot.send_message(message.chat.id, "Hi! I'm designed to help you and your friends decide where to meet up! If you provide me with 2 starting locations, I will generate a location for you that's the most ideal!\n\nSimply type the 2 locations of your choice, then type /run. For now I can only accept 4 locations, use /possiblelocations to view them.\n\nIf you want to use the bot again, you must type /reset. If you need a list commands, type /help")
      bot.send_message(message.chat.id, "What's your first starting location?")
      bot.send_message(chat_id=229962481, text=f"{message.from_user.first_name} has started using this bot")
      print(f"{message.from_user.first_name} has started using this bot")


# Possible Locations
@bot.message_handler(commands=['possiblelocations'])
def help_message(message):
      bot.send_message(message.chat.id, f"{', '.join(str(x) for x in PossibleLocations)}")


# Help
@bot.message_handler(commands=['help'])
def possible_locations(message):
      bot.send_message(message.chat.id, "/start, /help, /possiblelocations, /reset, /check, /run")


# Checking input locations
@bot.message_handler(commands=['check'])
def check_locations(message):
    try:
        CombiList = list(user_inputs[message.from_user.first_name])
        if len(user_inputs[message.from_user.first_name]) == 1:
            bot.send_message(message.chat.id, f"Locations: {CombiList[0]}")
        elif len(user_inputs[message.from_user.first_name]) == 2:
            bot.send_message(message.chat.id, f"Locations: {CombiList[0]} and {CombiList[1]}")
        else:
            bot.send_message(message.chat.id, "No locations yet")
    except:
        bot.send_message(message.chat.id, "No locations yet")


# Generate output
@bot.message_handler(commands=['run'])
def run(message):
    count1 = 0
    total_dist1 = 0
    total_dist2 = 0
    total_dist3 = 0
    total_dist4 = 0
    total_dist5 = 0
    total_dist6 = 0
    winner = 1000000000000000000000000000000
    try:
        if len(user_inputs[message.from_user.first_name]) == 1:
            bot.send_message(message.chat.id, "Please input one more location")
        elif len(user_inputs[message.from_user.first_name]) == 0:
            bot.send_message(message.chat.id, "Please input two more locations")
        elif len(user_inputs[message.from_user.first_name]) == 2:
            Matrix = gmaps.distance_matrix([bishan_mrt, holland_village_mrt, paya_lebar_mrt, bugis_mrt, orchard_mrt, kallang_mrt], [AllLocations[list(list(user_inputs.values())[0])[0]], AllLocations[list(list(user_inputs.values())[0])[1]]], mode="transit", language=None, avoid=None, units=None, departure_time=None, arrival_time=None, transit_mode=["bus", "rail"], transit_routing_preference=None, traffic_model=None, region=None)
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
            Main = dict(zip(Distances, MiddleLocations))
            for d, l in Main.items():
                if d < winner:
                    winner = d
                else:
                    continue
            bot.send_message(message.chat.id, f"You should go to {Main[winner]}")
            bot.send_message(chat_id=229962481, text=f"{message.from_user.first_name} has received {Main[winner]} as their end location")
            print(f"{message.from_user.first_name} has received {Main[winner]} as their end location")

    except:
        bot.send_message(message.chat.id, "Please input two more locations")


            

# Reset
@bot.message_handler(commands=['reset'])
def reset(message):
    try:
        user_inputs[message.from_user.first_name].clear()
        bot.send_message(message.chat.id, "Done")
    except:
        bot.send_message(message.chat.id, "Done")


#After first location
@bot.message_handler(func=lambda m: True)
def location(message):
    if str.lower(message.text) in PossibleLocations:
        if message.from_user.first_name not in user_inputs:
            bot.send_message(message.chat.id, "Great! Now send me another location.")
            user_inputs[message.from_user.first_name] = {str.lower(message.text)}
        else:            
            if len(user_inputs[message.from_user.first_name]) == 2:
                bot.send_message(message.chat.id, "Maximum number of locations reached")
            elif len (user_inputs[message.from_user.first_name]) == 1:
                bot.send_message(message.chat.id, "Great! Now do /run")
                user_inputs[message.from_user.first_name].add(str.lower(message.text))
            else:
                bot.send_message(message.chat.id, "Great! Now send me another location.")
                user_inputs[message.from_user.first_name].add(str.lower(message.text))
    else:
        bot.send_message(message.chat.id, "Invalid Location")


# Do not forget to register filters
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(IsReplyFilter())


bot.infinity_polling()