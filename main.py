import telebot as tb
from telebot import types
import webbrowser
bot = tb.TeleBot('6175521547:AAHPf26Kd4zWMf5w59QZ7iqnQ8Nyk_g1w3M')


# Sending picture
@bot.message_handler(content_types=['photo'])
def get_picture(message):
    bot.reply_to(message, 'It is so beautiful!')



# First question
@bot.message_handler(commands=['start'])
def ask_or_tell(message):
    first_question = types.InlineKeyboardMarkup()
    first_question.add(types.InlineKeyboardButton('Look at going buses', callback_data='bus_list'))
    first_question.add(types.InlineKeyboardButton('Tell about the certain bus', callback_data='tell_about_bus'))
    bot.reply_to(message, 'Select what you wanna do', reply_markup=first_question)

@bot.callback_query_handler(func=lambda callback: True)
def buses(callback):
    buses_list = types.InlineKeyboardMarkup()
    bus_80 = types.InlineKeyboardButton('80', callback_data='80')
    bus_90 = types.InlineKeyboardButton('90', callback_data='90')
    if callback.data == 'bus_list':
        buses_list.row(bus_80, bus_90)
        bot.reply_to(callback.message, 'Select the bus\nwhich you wanna look at', reply_markup=buses_list)
    elif callback.data == 'tell_about_bus':
        buses_list.row(bus_80, bus_90)
        bot.reply_to(callback.message, 'Select the bus\nwhich you wanna tell about', reply_markup=buses_list)
# following website
@bot.message_handler(commands=['vk'])
def site(message):
    webbrowser.open('https://vk.com/thorsher')


@bot.message_handler()
def saying_hi(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(non_stop=True)
