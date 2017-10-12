from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image
import requests
from io import StringIO

basewidth = 384

im = Image.open("image")

if im.size[0] > im.size[1]:
    im = im.rotate(-90, expand = True)

wpercent = (basewidth/float(im.size[0]))
hsize = int((float(im.size[1])*float(wpercent)))
im = im.resize((basewidth,hsize), Image.ANTIALIAS)

im = im.convert('1')
im.show()
