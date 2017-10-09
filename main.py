from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('Helou Friendo!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def help(bot, update):
    update.message.reply_text('Feed me pictures ')

updater = Updater('KEY')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
updater.idle()