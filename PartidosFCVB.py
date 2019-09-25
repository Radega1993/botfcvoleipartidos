# -*- coding: utf-8 -*-

# import libraries
import telebot
from telebot import types
#imports de las webs
from resources.getInfo import get_info
from partidosinfantilA import *
from partidosinfantilB import *
from partidoscadeteA import *
from partidoscadeteB import *
from partidosjuveA import *
from partidosjuveB import *
from partidossenior import *

# token from the librari
TOKEN = 'token'

tb = telebot.TeleBot(TOKEN)

@tb.message_handler(commands=['start'])
def send_welcome(message):
	tb.reply_to(message, "Bienvenido, espero poder ser de mucha ayuda!")

@tb.message_handler(commands=['hola'])
def comando_hola(mensaje):
	chat_id = mensaje.chat.id
	tb.send_message(chat_id, 'Hola compañero')

@tb.message_handler(commands=['adios'])
def comando_adios(mensaje):
	chat_id = mensaje.chat.id
	tb.send_message(chat_id, 'Adios compañero')

@tb.message_handler(commands=['jornadainfantila'])
def comando_jornadainfantila(mensaje):
	chat_id = mensaje.chat.id
	jornada = jornadaInfantilA()
	tb.send_message(chat_id, jornada)

@tb.message_handler(commands=['jornadainfantilb'])
def comando_jornadainfantilb(mensaje):
	chat_id = mensaje.chat.id
	jornada = jornadaInfantilB()
	tb.send_message(chat_id, jornada)

@tb.message_handler(commands=['jornadacadetea'])
def comando_jornadacadetea(mensaje):
	chat_id = mensaje.chat.id
	jornada = jornadaCadeteA()
	tb.send_message(chat_id, jornada)

@tb.message_handler(commands=['jornadacadeteb'])
def comando_jornadacadeteb(mensaje):
	chat_id = mensaje.chat.id
	jornada = jornadaCadeteB()
	tb.send_message(chat_id, jornada)

@tb.message_handler(commands=['jornadajuvenila'])
def comando_jornadajuvenila(mensaje):
	chat_id = mensaje.chat.id
	jornada = jornadaJuveA()
	tb.send_message(chat_id, jornada)

@tb.message_handler(commands=['jornadajuvenilb'])
def comando_jornadajuvenilb(mensaje):
	chat_id = mensaje.chat.id
	jornada = jornadaJuveB()
	tb.send_message(chat_id, jornada)

@tb.message_handler(commands=['jornadasenior'])
def comando_jornadasenior(mensaje):
	chat_id = mensaje.chat.id
	jornada = jornadaSenior()
	tb.send_message(chat_id, jornada)


#https://github.com/eternnoir/pyTelegramBotAPI#general-use-of-the-api

# Using the ReplyKeyboardMarkup class
# It's constructor can take the following optional arguments:
# - resize_keyboard: True/False (default False)
# - one_time_keyboard: True/False (default False)
# - selective: True/False (default False)
# - row_width: integer (default 3)
# row_width is used in combination with the add() function.
# It defines how many buttons are fit on each row before continuing on the next row.
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('a')
itembtn2 = types.KeyboardButton('v')
itembtn3 = types.KeyboardButton('d')
markup.add(itembtn1, itembtn2, itembtn3)
tb.send_message(chat_id, "Choose one letter:", reply_markup=markup)

# or add KeyboardButton one row at a time:
markup = types.ReplyKeyboardMarkup()
itembtnesc = types.KeyboardButton('Escola')
itembtninf = types.KeyboardButton('infantil')
itembtncad = types.KeyboardButton('Cadet')
itembtnjuv = types.KeyboardButton('juvenil')
itembtnsen = types.KeyboardButton('senior')
itembtnmas = types.KeyboardButton('Master')
markup.row(itembtnesc, itembtninf)
markup.row(itembtncad, itembtnjuv)
markup.row(itembtnsen, itembtnmas)
tb.send_message(chat_id, "Escull un equip:", reply_markup=markup)



tb.polling(none_stop = True)
