#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals  # Te perimte usar caracteres
from builtins import (ascii, bytes, chr, dict, filter, hex, input,
                      int, map, next, oct, open, pow, range, round,
                      str, super, zip)

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters, RegexHandler, ConversationHandler)
import logging
import web
import random

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection
db = web.database(
    dbn='mysql',
    host='localhost',
    db='horoscopo_lnpr',
    user='horoscopo',
    pw='horoscopo.2019',
    port=3306,
)

# Samm17_bot
token = '762779940:AAEQofnp6ylhdj79Y-VOkfUfLDrIixqk-N8'

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.


def start(bot, update):
    username = update.message.from_user.username
    update.message.reply_text(
        'Hola {} usa estos comandos:\n/info llave #Informacion_bot\n/signo nombre_signo\nPuedes consultar tu signo para saber lo que te depara el futuro\n  \
        '.format(username))


def help(bot, update):
    username = update.message.from_user.username
    update.message.reply_text(
        'Hola {} .\nBienvenido al HoroscoBot\n/info para poder conocer los comandos.'.format(username))


def search(bot, update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        nombre_signo = text[1]  # cast para convertir str a int
        print "Send info to {}".format(username)
        print "Key search {}".format(nombre_signo)
        result = db.select('horoscopos', where='nombre_signo=$nombre_signo', vars=locals())[0]

        nombre_signo = result.nombre_signo #Asignar cada campo de la consulta a una variable
        descripcion_signo = result.descripcion_signo

        nombre = nombre_signo.encode("utf-8") #Pasar el tipo de dato Unicode a encode
        descripcion = descripcion_signo.encode("utf-8")
        respuesta = "Signo: " + nombre + "\n" + \
                    "                       Descripcion\n" + descripcion
        #response = "Sending Info " + str(result[0]) + ", " + str(result[1]) + ", " + str(result[2])
        #print response
        update.message.reply_text('Hola {}\nEste es el HOROSCOPO que buscas:\n{}'.format(username, respuesta))
        
        #Imagen
        chat_id = update.message.chat_id
        bot.send_photo(chat_id=chat_id, photo=open("static/images/{}".format(result.ruta_img_signo), 'rb'))

    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('La llave {} es incorreta'.format(nombre_signo))


def signo(bot, update):
    search(bot, update)


def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user
    print update.message.from_user.username

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    try:
        print 'HoroscoBot init token'

        updater = Updater(token)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        print 'HoroscoBot'

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("signo", signo))

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'HoroscoBot ready'
        updater.idle()
    except Exception as e:
        print "Error 100: ", e.message


if __name__ == '__main__':
    main()


#Esta parte permite la codigficacion y decodificacion de los tipos de datos para evitar errores en la concatenacion.
'''
# Convert Unicode to plain Python string: "encode"
unicodestring = u"Hello world"
utf8string = unicodestring.encode("utf-8")
asciistring = unicodestring.encode("ascii")
isostring = unicodestring.encode("ISO-8859-1")
utf16string = unicodestring.encode("utf-16")

# Convert plain Python string to Unicode: "decode"
plainstring1 = unicode(utf8string, "utf-8")
plainstring2 = unicode(asciistring, "ascii")
plainstring3 = unicode(isostring, "ISO-8859-1")
plainstring4 = unicode(utf16string, "utf-16")

assert plainstring1==plainstring2==plainstring3==plainstring4
'''