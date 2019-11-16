from telegram.ext import Updater, CommandHandler
import logging
updater=Updater(token='931539659:AAHWXmg0zDUrr6mX1GxUAnsslEOeFg6Zyk8',use_context=True)
dispatcher=updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update,context) :
    context.bot.send_message(chat_id=update.effective_chat.id, text="hello world")

start_handler=CommandHandler('start',start)
dispatcher.add_handler(start_handler)
updater.start_polling()