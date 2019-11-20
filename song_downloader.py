from __future__ import unicode_literals
from telegram.ext import Updater, CommandHandler
import logging
import youtube_dl
import os

updater=Updater(token='931539659:AAHWXmg0zDUrr6mX1GxUAnsslEOeFg6Zyk8',use_context=True)
dispatcher=updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update,context) :
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is a work of Huraken")
def dl(update, context):
    p=update.message.text
    p = p.strip('\n')
    ydl_opts = {
            'outtmpl':'music/%(title)s.%(ext)s',
            'format': 'bestaudio/best', 
                   'format': 'bestaudio/best',
               'postprocessors': [{
               'key': 'FFmpegExtractAudio',
               'preferredcodec': 'mp3',
               'preferredquality': '320',
             }],
                }
    context.bot.send_message(chat_id=update.effective_chat.id, text='Downloading Song...')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([str(p)])
    
    list=os.listdir('music')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Uploading Song...')
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('music/'+list[0], 'rb'))
    os.system("rm -rf music")

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, dl)
dispatcher.add_handler(echo_handler)

start_handler=CommandHandler('start',start)
dispatcher.add_handler(start_handler)
updater.start_polling()
