import telebot
import constants

bot = telebot.TeleBot(constants.token)

adminchatid = 0

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "Бот технической поддержки хостинга")

@bot.message_handler(commands=['IAmAdmin'])
def handle_text(message):
    bot.send_message(message.chat.id, "Пользователь отмечен как администратор")
    adminchatid = message.chat.id
    bot.send_message(message.chat.id, adminchatid)



bot.polling(none_stop=True, interval=0)