# -*- coding: utf-8 -*-

# import libraries
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot, ReplyKeyboardRemove
#import telegram
#imports de las webs
#from resources.getInfo import get_info
from resources.geturl import get_url
from config.auth import get_token
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


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

def print_data(bot, update):
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(),
                          reply_markup=telegram.ReplyKeyboardRemove())


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
  keyboard = [[InlineKeyboardButton('Aleví Negre', callback_data='cb_alen')],
              [InlineKeyboardButton('Aleví Verd', callback_data='cb_alev')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def infantil_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Infantil Negre', callback_data='cb_infn')],
              [InlineKeyboardButton('Infantil Verd', callback_data='cb_infv')],
              [InlineKeyboardButton('Infantil Blanc', callback_data='cb_infb')],
              [InlineKeyboardButton('Infantil Vermell', callback_data='cb_infr')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def cadet_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Cadet Negre', callback_data='cb_cadn')],
              [InlineKeyboardButton('Cadet Verd', callback_data='cb_cadv')],
              [InlineKeyboardButton('Cadet Blanc', callback_data='cb_cadb')],
              [InlineKeyboardButton('Main Menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def juvenil_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Juvenil Negre', callback_data='cb_juvn')],
                [InlineKeyboardButton('Juvenil Verd', callback_data='cb_juvv')],
                [InlineKeyboardButton('Juvenil Blanc', callback_data='cb_juvb')],
                [InlineKeyboardButton('Main Menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

def senior_menu_keyboard():
    keyboard = [[InlineKeyboardButton('femení', callback_data='cb_sen')],
                [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

def master_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Veterans', callback_data='cb_vet')],
                [InlineKeyboardButton('Masters', callback_data='cb_mas')],
                [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


############################# Messages #########################################
def main_menu_message():
  return 'Escull categoria?'

def equip_menu_message():
  return 'Escull equip?"'

############################# Handlers #########################################
def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    token = get_token()
    updater = Updater(token)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu,
                                                            pattern='main'))
    updater.dispatcher.add_handler(CallbackQueryHandler(escola_menu,
                                                            pattern='cb_escola'))
    updater.dispatcher.add_handler(CallbackQueryHandler(infantil_menu,
                                                            pattern='cb_infantil'))
    updater.dispatcher.add_handler(CallbackQueryHandler(cadet_menu,
                                                            pattern='cb_cadet'))
    updater.dispatcher.add_handler(CallbackQueryHandler(juvenil_menu,
                                                            pattern='cb_juvenil'))
    updater.dispatcher.add_handler(CallbackQueryHandler(senior_menu,
                                                            pattern='cb_senior'))
    updater.dispatcher.add_handler(CallbackQueryHandler(master_menu,
                                                            pattern='cb_master'))

    updater.dispatcher.add_handler(CallbackQueryHandler(print_data,
                                                            pattern='cb_cadv'))


    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
