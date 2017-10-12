from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image
import requests
from io import BytesIO
import subprocess
import time
import threading

def start(bot, update):
    update.message.reply_text('Helou Friendo!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def help(bot, update):
    update.message.reply_text('Feed me pictures ')

def handle():
    filename = './tmp.png'
    p = subprocess.Popen('lp -o media=Custom.48x200mm -o fit-to-page -o position=top -d ZJ-58 '+ filename, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    retval = p.wait()
    print(retval)

def sent_picture(bot, update):
    print('hei')

    photo_file = bot.get_file(update.message.photo[-1].file_id)
    print('hooo')
    response = requests.get(photo_file['file_path'])
    print('ameisin')
    im = Image.open(BytesIO(response.content))
    print('pic')
    basewidth = 384
    if im.size[0] > im.size[1]:
        im = im.rotate(-90, expand = True)

    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    im = im.resize((basewidth,hsize), Image.ANTIALIAS)

    im = im.convert('1')
    print('saving')
    filename = './tmp.png'
    im.save(filename)

    t = threading.Thread(target=handle)
    t.start()
    
    #print('printing')
    #p = Popen('lp -o media=Custom.48x200mm -o fit-to-page -o position=top -d ZJ-58 '+ filename, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #retval = p.wait()
    #print(retval)

    bio = BytesIO()
    bio.name = 'image.png'
    im.save(bio, 'PNG')
    bio.seek(0)
    bot.send_photo(chat_id=update.message.chat_id,
                   photo=bio)


updater = Updater('420789625:AAEpAt-Alcygxvi7kiTad1yUSDe6LCALgq4')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, sent_picture))

updater.start_polling()
updater.idle()
