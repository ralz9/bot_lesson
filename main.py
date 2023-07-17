import telebot
import random 
from my_token import token


bot = telebot.TeleBot(token)

keybord = telebot.types.ReplyKeyboardMarkup()
butn1 = telebot.types.KeyboardButton('Играть ')
butn2 = telebot.types.KeyboardButton('нет') 
keybord.add(butn1,butn2)


@bot.message_handler(commands=['start'])
def start_messege(message):
#  bot.reply_to(message, "Howdy, how are you doing?")
    bot.send_sticker(message.chat.id , 'CAACAgIAAxkBAAI2t2S1PAOOTk0dC9JojvVeHj--56K1AAJtAQACIjeOBCXzuBTCmqbyLwQ')
    msg = bot.send_message(message.chat.id, f'привет {message.chat.first_name} начнем игру?', reply_markup=keybord)
    bot.register_next_step_handler(msg, check_answer)


def check_answer(message):
    if message.text == 'Играть':
        bot.send_message(message.chat.id, ' окей, вот правила: нужно угадать число от 1 до 10 за три попытки ')
        random_number = random.randint(1,10)
        start_game(message, 3 , random_number)
    else:
        bot.send_message(message.chat.id, 'ну и ладно')
    

def start_game(message , attempts , random_number): 
    msg = bot.send_message(message.chat.id, 'Введите число ')
    bot.register_next_step_handler(msg , check_number , attempts - 1 , random_number)


def check_number(message , attemps , random_number):
    if message.text == str(random_number):
        bot.send_message(message.chat.id, 'вы победили ')
        bot.send_photo(message.chat.id , 'https://blog.ipleaders.in/wp-content/uploads/2020/08/winner-1-696x463-1-1.jpg')
    elif attemps == 0:
        bot.send_message(message.chat.id, f' Извините но у вас закончились попытки. Числа было  - {random_number} ')
    else:
        bot.send_message(message.chat.id , f'попробуйте еще раз , у вас осталось {attemps} попыток ')
        start_game(message , attemps, random_number)



bot.polling()
