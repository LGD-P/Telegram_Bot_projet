from info import RESULTAT_REFLET
from nasa_img import RESULTAT_NASA
from citation import RESULTAT_CITATION

import telegram.ext

# nom du bot : ...


with open("Token.txt", "r") as f:
    TOKEN = f.read()


# Connexion du bot à Télégram grace au TOKEN


updater = telegram.ext.Updater(TOKEN, use_context=True)

disp = updater.dispatcher

# définition des fonctions messages renvoyés par les différentes commandes


def start(update, context):
    update.message.reply_text("Hey Dude !")


def help(update, context):
    update.message.reply_text("""
    /start => launch welcome message.
    /Nasa => get the Nasa info.
    /citation => get a quote 
    /reflet => get last news from reflet info
    """)


def call_nasa(update, context):
    update.message.reply_text(RESULTAT_NASA)


def call_citation(update, context):
    update.message.reply_text(RESULTAT_CITATION)


def call_reflet_info(update, context):
    update.message.reply_text(RESULTAT_REFLET)

# définition des commandes pour appeler les fonctions


disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("NASA", call_nasa))
disp.add_handler(telegram.ext.CommandHandler("citation", call_citation))
disp.add_handler(telegram.ext.CommandHandler("reflet", call_reflet_info))


# Sert à lancer le bot
updater.start_polling()

# Pour arrêter le bot proprement avec CTRL+C
updater.idle()
