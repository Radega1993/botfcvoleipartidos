#-*

import telebot # Importamos las librería

TOKEN = '495586156:AAGkSobt7tgtYaS6ug2-BdIfUgCgntnwvzY' # Ponemos nuestro Token generado con el @BotFather

tb = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
tb_update = Updater(tb.TOKEN)


@tb.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@tb.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()

while True:
	pass