import telebot
from telebot import types
import sqlite3  # Import SQL module

bot = telebot.TeleBot('6175521547:AAHPf26Kd4zWMf5w59QZ7iqnQ8Nyk_g1w3M')


# Begin register from /start command
@bot.message_handler(commands=['start'])
def start(message):
    connection = sqlite3.connect('data.sql')  # Makes SQL file
    cursor = connection.cursor()  # For manage table
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, '
                   'name varchar(50),'
                   'pass varchar(50))')  # Making Table with fields
    connection.commit()  # Necessary step
    cursor.close()  # Stop manage table
    connection.close()  # Close table

    bot.send_message(message.chat.id, 'You begin registration\n input your name:')
    bot.register_next_step_handler(message, user_name)  # Method to make what do next


# Function to Input the name
def user_name(message):
    global name
    name = message.text.strip()  # Method strip() to remove spaces in begin an end
    bot.send_message(message.chat.id, 'Input password: ')
    bot.register_next_step_handler(message, user_password)


# Function to input the password
def user_password(message):
    password = message.text.strip()
    connection = sqlite3.connect('data.sql')  # Turn to table
    cursor = connection.cursor()  # Make manage cursor again

    cursor.execute("INSERT INTO users (name, pass) VALUES('%s', '%s')" % (name, password))  # Input data in table
    connection.commit()  # Necessary
    cursor.close()
    connection.close()

    # Making button to see users list
    buttons = types.InlineKeyboardMarkup()
    buttons.add(types.InlineKeyboardButton('Users list', callback_data='users'))
    bot.send_message(message.chat.id, 'User is registered', reply_markup=buttons)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    connection = sqlite3.connect('data.sql')  # To turn to table
    cursor = connection.cursor()  # To manage table

    cursor.execute('SELECT * FROM users')  # Extract users from table
    users = cursor.fetchall()  # Put users in variable

    # Providing users in comfortable view
    info = ''
    for elem in users:
        info += f'User name: {elem[1]}, Password: {elem[2]}\n'

    # Closing table
    cursor.close()
    connection.close()

    bot.send_message(call.message.chat.id, info)  # Providing users list in chat message


bot.polling(non_stop=True)
