import telegram.ext as tg

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello bro, say smth!')

def textMessage(bot, update):
    response = 'I\'ve got your point: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)

updater = tg.Updater(token="915791277:AAGgFRiZ8Oo6oli6lZfTax-3fT8dTZi4V0M")
dispatcher = updater.dispatcher

start_command_handler = tg.CommandHandler('start', startCommand)
text_message_handler = tg.MessageHandler(tg.Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()