import telebot as tb

bot = tb.TeleBot('6285684879:AAFLk5uIxpIE9E105RIjGXCZkS-ZBKLWeRg')

# First question
def ask_or_tell():
    keyboard = tb.types.InlineKeyboardMarkup()
    key_ask_for_a_bus = tb.types.InlineKeyboardButton(text ='Посмотреть автобусы')
    keyboard.add(key_ask_for_a_bus)
    key_tell_about_the_bus = tb.types.InlineKeyboardButton(text='Сообщить об автобусе')
    keyboard.add(key_tell_about_the_bus)
