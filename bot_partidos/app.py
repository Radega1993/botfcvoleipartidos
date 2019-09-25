# -*- coding: utf-8 -*-

# import libraries
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot
#imports de las webs
from resources.getInfo import get_info
from config.auth import get_token
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger('listaasistencia_bot')


############################### Bot ############################################
def start(bot, update):
  update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

def main_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def escola_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=equip_menu_message(),
                        reply_markup=escola_menu_keyboard())

def infantil_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=equip_menu_message(),
                        reply_markup=infantil_menu_keyboard())

def cadet_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=equip_menu_message(),
                        reply_markup=cadet_menu_keyboard())

def juvenil_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=equip_menu_message(),
                        reply_markup=juvenil_menu_keyboard())

def senior_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=equip_menu_message(),
                        reply_markup=senior_menu_keyboard())

def master_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=equip_menu_message(),
                        reply_markup=master_menu_keyboard())


############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton("Escola", callback_data="cb_escola")],
             [InlineKeyboardButton("Infantil", callback_data="cb_infantil")],
             [InlineKeyboardButton("Cadet", callback_data="cb_cadet")],
             [InlineKeyboardButton("Juvenil", callback_data="cb_juvenil")],
             [InlineKeyboardButton("Senior", callback_data="cb_senior")],
             [InlineKeyboardButton("Master", callback_data="cb_master")]]
  return InlineKeyboardMarkup(keyboard)

def escola_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def infantil_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def cadet_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Cadet Negre', callback_data='cb_cadn')],
              [InlineKeyboardButton('Cadet Verd', callback_data='cb_cadv')],
              [InlineKeyboardButton('Cadet blanc', callback_data='cb_cadb')]
              [InlineKeyboardButton('Main Menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def juvenil_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Juvenil Negre', callback_data='cb_juvn')],
                [InlineKeyboardButton('Juvenil Verd', callback_data='cb_juvv')],
                [InlineKeyboardButton('Juvenil blanc', callback_data='cb_juvb')],
                [InlineKeyboardButton('Main Menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

def senior_menu_keyboard():
    keyboard = [[InlineKeyboardButton('femení', callback_data='m2_1')]
                [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

def master_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
                [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
                [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


############################# Messages #########################################
def main_menu_message():
  return 'Escull categoria?'

def equip_menu_message():
  return 'Escull equip?"'


############################# Handlers #########################################
token = get_token()
updater = Updater(token, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(escola_menu, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(infantil_menu, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(cadet_menu, pattern='m3'))
updater.dispatcher.add_handler(CallbackQueryHandler(juvenil_menu, pattern='m4'))
updater.dispatcher.add_handler(CallbackQueryHandler(senior_menu, pattern='m5'))
updater.dispatcher.add_handler(CallbackQueryHandler(master_menu, pattern='m6'))

def error(bot, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', bot, update.error)


# log all errors
updater.dispatcher.add_error_handler(error)

updater.start_polling()
# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()
