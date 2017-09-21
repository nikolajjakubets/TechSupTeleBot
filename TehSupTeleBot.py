import telebot
import constants

bot = telebot.TeleBot(constants.token)

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "Бот технической поддержки хостинга")

bot.polling(none_stop=True, interval=0)