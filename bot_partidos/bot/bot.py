from resources.geturl import get_url

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



@bot.callback_query_handler(lambda query: query.data == "sdss")
def print_data(bot, update):
    query = update.callback_query
    bot.send_message(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=get_url(),
                          reply_markup=telegram.ReplyKeyboardRemove())
