import telebot
import webbrowser

#  Initialisation our bot
bot = telebot.TeleBot('6175521547:AAHPf26Kd4zWMf5w59QZ7iqnQ8Nyk_g1w3M')


#  open weblink
@bot.message_handler(commands=['website'])
def website(message):
    webbrowser.open('https://google.com')


# replying to message
@bot.message_handler()
def info(message):
    if message.text.lower() == 'id':
        bot.reply_to(message, f'Your ID:{message.from_user.id}')
    elif message.text.lower() == '/start':
        main(message)


# replying to commands with info about user
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hello! {message.from_user.first_name} {message.from_user.last_name}')


# Replying with format text
@bot.message_handler(commands=['text'])
def format_text(message):
    bot.send_message(message.chat.id, '<b>Format</b> <em><u>text</u></em>', parse_mode='html')


bot.polling(non_stop=True)  # Or bot.infinity_polling()
