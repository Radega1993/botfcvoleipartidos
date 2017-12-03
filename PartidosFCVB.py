#-*

import telebot # Importamos las librería

TOKEN = '495586156:AAGkSobt7tgtYaS6ug2-BdIfUgCgntnwvzY' # Ponemos nuestro Token generado con el @BotFather

tb = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
tb_update = Updater(tb.TOKEN)
def start(bot, update, pass_chat_data=True):
	update.message.chat_id
	tb.send_message(chat_id=update.message.chat_id, 'Hola mundo!') # Ejemplo tb.send_message('109556849', 'Hola mundo!')

start_handler = commandHandler('start', start)

dispatcher = tb.dispatcher

dispatcher.add_handler(start_handler)

tb.start_polling()
tb.idle()

while True:
	pass