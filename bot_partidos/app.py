# -*- coding: utf-8 -*-

# import libraries
from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot, ReplyKeyboardRemove
import telegram
#imports de las webs
from resources.getInfo import get_info
from resources.getUrl import get_url, get_all_data
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


############################ PRINT FUNCTIONS ###################################

def print_data_alen(bot, update):
    equipo = 'alen'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text="Sense dades encara",
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_alev(bot, update):
    equipo = 'alev'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text="Sense dades encara",
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_infn(bot, update):
    equipo = 'infn'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_infv(bot, update):
    equipo = 'infv'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_infb(bot, update):
    equipo = 'infb'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_infr(bot, update):
    equipo = 'infr'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_cadn(bot, update):
    equipo = 'cadn'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_cadv(bot, update):
    equipo = 'cadv'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_cadb(bot, update):
    equipo = 'cadb'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_juvn(bot, update):
    equipo = 'juvn'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_juvv(bot, update):
    equipo = 'juvv'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_juvb(bot, update):
    equipo = 'juvb'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_sen(bot, update):
    equipo = 'sen'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_vet(bot, update):
    equipo = 'vet'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
                          reply_markup=telegram.ReplyKeyboardRemove())

def print_data_mas(bot, update):
    equipo = 'mas'
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(equipo),
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

def tots_els_partits(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                        action = telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id, text=get_all_data())

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

######################### PRINT DATA ###########################################

    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_alen,
                                                            pattern='cb_alen'))
    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_alev,
                                                        pattern='cb_alev'))

    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_infn,
                                                            pattern='cb_infn'))
    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_infv,
                                                            pattern='cb_infv'))
    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_infb,
                                                        pattern='cb_infb'))
    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_infr,
                                                            pattern='cb_infr'))

    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_cadn,
                                                            pattern='cb_cadn'))
    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_cadv,
                                                        pattern='cb_cadv'))
    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_cadb,
                                                            pattern='cb_cadb'))

    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_juvn,
                                                            pattern='cb_juvn'))
    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_juvv,
                                                        pattern='cb_juvv'))
    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_juvb,
                                                            pattern='cb_juvb'))

    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_sen,
                                                            pattern='cb_sen'))

    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_vet,
                                                        pattern='cb_vet'))
    updater.dispatcher.add_handler(CallbackQueryHandler(print_data_mas,
                                                            pattern='cb_mas'))

    updater.dispatcher.add_handler(CommandHandler('tots_els_partits', tots_els_partits))


    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
