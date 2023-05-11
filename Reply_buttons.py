import telebot
from telebot import types

bot = telebot.TeleBot('6175521547:AAHPf26Kd4zWMf5w59QZ7iqnQ8Nyk_g1w3M')


@bot.message_handler(commands=['start'])
def start(message):
    reply_keyboard = types.ReplyKeyboardMarkup()
    btn_1 = types.KeyboardButton('Button one')
    btn_2 = types.KeyboardButton('Button two')
    btn_3 = types.KeyboardButton('Send the pic')
    reply_keyboard.row(btn_1)
    reply_keyboard.row(btn_2, btn_3)
    bot.send_message(message.chat.id, 'Press the button', reply_markup=reply_keyboard)
    bot.register_next_step_handler(message, pressed_button)


def pressed_button(message):
    if message.text == 'Button one':
        bot.send_message(message.chat.id, 'You pressed button one')
        start(message)
    elif message.text == 'Button two':
        bot.send_message(message.chat.id, 'You pressed button two')
        start(message)
    elif message.text == 'Send the pic':
        bot.send_message(message.chat.id, 'Here it is:')
        with open('me.jpeg') as file:
            bot.send_photo(message.chat.id, file)
        start(message)


bot.polling(non_stop=True)
