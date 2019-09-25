# -*- coding: utf-8 -*-

# import libraries
import telebot
from telebot import types
#imports de las webs
from resources.getInfo import get_info

# token from the librari
TOKEN = 'token'

tb = telebot.TeleBot(TOKEN)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Escola", callback_data="cb_escola"),
               InlineKeyboardButton("Infantil", callback_data="cb_infantil"),
               InlineKeyboardButton("Cadet", callback_data="cb_cadet"),
               InlineKeyboardButton("Juvenil", callback_data="cb_juvenil"),
               InlineKeyboardButton("Senior", callback_data="cb_senior"),
               InlineKeyboardButton("Master", callback_data="cb_master"))
    return markup

def escola_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Benjamí", callback_data="cb_benjami"),
               InlineKeyboardButton("Alevi Negre", callback_data="cb_anegre"),
               InlineKeyboardButton("Alevi Verd", callback_data="cb_averd"),
               InlineKeyboardButton("Alevi Blanc", callback_data="cb_ablanc"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_escola":
        bot.send_message(message.chat.id, "Escull equip?", reply_markup=escola_markup())
        #bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Answer is No")

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Escull categoria?", reply_markup=gen_markup())

bot.polling(none_stop=True)
