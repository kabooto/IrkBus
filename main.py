import telebot as tb
from telebot import types
import webbrowser
bot = tb.TeleBot('6175521547:AAHPf26Kd4zWMf5w59QZ7iqnQ8Nyk_g1w3M')
chat_id = -1001979969925
member_id = 5514024912
result = bot.get_chat_member(chat_id, member_id)
print(result)
print(type(result))


# Sending picture
@bot.message_handler(content_types=['photo'])
def get_picture(message):
    bot.reply_to(message, 'It is so beautiful!')



# First question
@bot.message_handler(commands=['start'])
def ask_or_tell(message):
    first_question = types.ReplyKeyboardMarkup()
    first_question.row(types.InlineKeyboardButton('Check my subscribe'))
    first_question.row(types.InlineKeyboardButton('Look at going buses'))
    first_question.add(types.InlineKeyboardButton('Tell about the certain bus'))
    bot.send_message(message.chat.id, 'Select what you wanna do', reply_markup=first_question)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Look at going buses':
        bot.send_message(message.chat.id, 'Wait a second')
    elif message.text == 'Tell about the certain bus':
        bot.send_message(message.chat.id, 'Select the bus')
    elif message.text == 'Check my subscribe':
        if result.status == 'member':
            bot.send_message(message.chat.id, 'Lucky you')
        else:bot.send_message(message.chat.id, 'Subscribe to keep going')


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
    elif message.text.lower() == 'inf':
        bot.send_message(message.chat.id, message)


bot.polling(non_stop=True)
