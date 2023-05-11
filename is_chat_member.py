import telebot
from telebot import types


bot = telebot.TeleBot('6175521547:AAHPf26Kd4zWMf5w59QZ7iqnQ8Nyk_g1w3M')


#  Making a button that lets check memberships
@bot.message_handler()
def checking_membership(message):
    if message.text == '/start':
        button = types.ReplyKeyboardMarkup()
        btn = types.KeyboardButton('Check my memberships')
        button.row(btn)
        bot.send_message(message.chat.id, 'Press the button', reply_markup=button)
        bot.register_next_step_handler(message, pressed_button)


# Checking memberships of any user to certain channel
def pressed_button(message):
    if message.text == 'Check my memberships':
        chat_id = -1001979969925
        member_id = message.from_user.id
        member_checking = bot.get_chat_member(chat_id, member_id)  # Checking memberships
        if member_checking.status == 'member':
            bot.send_message(message.chat.id, 'You are member')
        else:
            bot.send_message(message.chat.id, "You aren't member")


bot.polling(non_stop=True)
