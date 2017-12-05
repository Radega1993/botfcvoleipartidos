# -*- coding: utf-8 -*-

# import libraries
import telebot
from telebot import types

import urllib2
from bs4 import BeautifulSoup

# token from the librari
TOKEN = ''

tb = telebot.TeleBot(TOKEN) 

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Bienvenido, espero poder ser de mucha ayuda!")

@tb.message_handler(commands=['hola'])
def comando_hola(mensaje):
    chat_id = mensaje.chat.id
    tb.send_message(chat_id, 'Hola compañero')

@tb.message_handler(commands=['chao'])
def comando_chao(mensaje):
    chat_id = mensaje.chat.id
    tb.send_message(chat_id, 'Adios colega')

tb.polling(none_stop = True)
