import telebot
from telebot import TeleBot, types, custom_filters
from telebot.custom_filters import TextFilter, TextMatchFilter, IsReplyFilter

bot = telebot.TeleBot("6147055066:AAFvMRD41FTtRdF8q6v8jaqqSJmSPWsh5P8")


# Starting and Ending Location Dictionary
CheatSheet = dict()
CheatSheet['holland village'] = {'nus', 'tkk'}
CheatSheet['bugis'] = {'nus', 'bedok'}
CheatSheet['orchard'] = {'nus', 'serangoon'}
CheatSheet['bishan'] = {'tkk', 'serangoon'}
CheatSheet['paya lebar'] = {'bedok', 'serangoon'}
CheatSheet['kallang'] = {'bedok', 'tkk'}


# Defining the databases
user_inputs = dict()
PossibleLocations = {'nus', 'serangoon', 'bedok', 'tkk'}


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
    try:
        if len(user_inputs[message.from_user.first_name]) == 1:
            bot.send_message(message.chat.id, "Please input one more location")
        elif len(user_inputs[message.from_user.first_name]) == 0:
            bot.send_message(message.chat.id, "Please input two more locations")
        else:
            for end, start in CheatSheet.items():
                if user_inputs[message.from_user.first_name] == start:
                    bot.send_message(message.chat.id, f"You should go to {end}")
                    bot.send_message(chat_id=229962481, text=f"{message.from_user.first_name} has received {end} as their end location")
                    print(f"{message.from_user.first_name} has received {end} as their end location")
                    break
                else:
                    continue
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