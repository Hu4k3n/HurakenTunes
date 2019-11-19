from __future__ import unicode_literals
from telegram.ext import Updater, CommandHandler
import logging
import youtube_dl

updater=Updater(token='931539659:AAHWXmg0zDUrr6mX1GxUAnsslEOeFg6Zyk8',use_context=True)
dispatcher=updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update,context) :
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is a work of Huraken")
def echo(update, context):
    p=update.message.text
    #context.bot.send_message(chat_id=update.effective_chat.id, text=p)
    #p = stdin.readline()
    p = p.strip('\n')
	#p='https://www.youtube.com/watch?v=aJOTlE1K90k'
    ydl_opts = {
            'format': 'bestaudio/best', 
                   'format': 'bestaudio/best',
               'postprocessors': [{
               'key': 'FFmpegExtractAudio',
               'preferredcodec': 'mp3',
               'preferredquality': '320',
             }],
                }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([str(p)])
    

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

start_handler=CommandHandler('start',start)
dispatcher.add_handler(start_handler)
updater.start_polling()
