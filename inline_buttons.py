import telebot
from telebot import types
import random


bot = telebot.TeleBot('6175521547:AAHPf26Kd4zWMf5w59QZ7iqnQ8Nyk_g1w3M')


# Replying to /start with buttons
@bot.message_handler(commands=['start'])
def inline_buttons(message):
    inline_keyboard = types.InlineKeyboardMarkup()  # Class object to do buttons
    butt_1 = types.InlineKeyboardButton('To open GOOGLE', url='https://google.com')
    butt_2 = types.InlineKeyboardButton('To write a random number', callback_data='random')
    inline_keyboard.row(butt_1, butt_2)
    bot.send_message(message.chat.id, 'Press the button', reply_markup=inline_keyboard)


# Replying on a photo with buttons
@bot.message_handler(content_types=['photo'])
def get_picture(message):
    bot.reply_to(message, 'Spicy photo!')
    button = types.InlineKeyboardMarkup()
    button.add(types.InlineKeyboardButton('Delete the picture', callback_data='delete'))
    button.add(types.InlineKeyboardButton('Edit text', callback_data='edit'))
    bot.send_message(message.chat.id, 'Click the button', reply_markup=button)


# Function manage buttons
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id-2)
    elif callback.data == 'edit':
        bot.edit_message_text('Fantastic photo!', callback.message.chat.id, callback.message.message_id-1)
    elif callback.data == 'random':
        random_number = random.randint(0, 100)
        bot.send_message(callback.message.chat.id, str(random_number))


bot.infinity_polling()
