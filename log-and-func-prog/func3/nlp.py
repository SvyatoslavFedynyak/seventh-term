import telegram.ext as tg
import apiai
import json

def startCommand(bot, update,):
    bot.send_message(chat_id=update.message.chat_id, text='Hello bro, say smth!')

def textMessage(bot, update):
    with open('setting.non-git.json', 'r') as file:
        load_sett = json.load(file)
    request = apiai.ApiAI(load_sett['dialogflow-api-key']).text_request()
    request.lang = "en"
    request.session_id = 'nlpBro'
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Sorry, what?')

with open('setting.non-git.json', 'r') as file:
    load_sett = json.load(file)

updater = tg.Updater(token=load_sett['bot-api-token'])
dispatcher = updater.dispatcher

start_command_handler = tg.CommandHandler('start', startCommand)
text_message_handler = tg.MessageHandler(tg.Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()