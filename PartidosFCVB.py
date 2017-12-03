import telebot # Importamos las librería

TOKEN = '495586156:AAGkSobt7tgtYaS6ug2-BdIfUgCgntnwvzY' # Ponemos nuestro Token generado con el @BotFather

tb = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API

tb.send_message(1, 'Hola mundo!') # Ejemplo tb.send_message('109556849', 'Hola mundo!')