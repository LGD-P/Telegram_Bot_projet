# <span style="color:  #3b43ee  ">Création d'un BOT TELEGRAM :</span>

Ce sript fonctionne sous Python 3 ==><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width=50 align=center>

**Le but de ce script est de créer un bot avec trois fonctions principales:**

<span style="color:  #3b43ee  ">1.</span>Récupérer l'image du jour du site de la nasa

<span style="color:  #3b43ee  ">2.</span> Récupérer une citation chaque jour différente

<span style="color:  #3b43ee  ">3.</span> Récupérer le dernier article de presse sur le site Reflet Info

---

<span style ="color:  #ee0101  ">Note:</span>

_Bien entendu le bot ne fonctionne dans l'application Telegram, que si le script est en cours d'exécution_

_Un token nécessaire au fonctionnement du bot. Le mien n'est pas fourni dans le script. Si vous souhaitez créer votre propre bot, il vous faudra donc obtenir votre propre token._

_Une fois obtenu il vous suffira de créer un fichier ***"Token.text"*** dans le dossier où s'exécute le script, et y coller votre token à l'intérieur._

### <span style ="color:  #ee0101  ">Pour obtenir un token:</span>

<span style="color:  #3b43ee  ">1.</span>Ouvrez télégram sur votre os

<span style="color:  #3b43ee  ">2.</span> Dans chat recherchez **"Botfather"** certifié : <img src="Botfather.png" width=50 align=center>

<span style="color:  #3b43ee  ">3.</span> Ouvrez la conversation entrer la commande <span style="color:  #46ee1c  ">/start</span>

<span style="color:  #3b43ee  ">4.</span> Puis la commande : <span style="color:  #46ee1c  ">/newbot </span>

<span style="color:  #3b43ee  ">5.</span> Vous devez alors choisir un nom d'utilisateur, vous pourrez ainsi retrouver votre bot.

<span style="color:  #3b43ee  ">6.</span> Vous n'avez plus qu'a récupérer votre Token et créer le fichier évoqué plus haut.

---

## <span style="color:  #ee0101 ">Liste des commandes à exécuter pour lancer le programme:</span>

_Pré-requis: se placer depuis le terminal dans le dossier où l'on exécute le script:_

Avant toute chose on clone le répository git:

> <span style="color:  #46ee1c  ">git clone https://github.com/LGD-P/Telegram_Bot_projet.git</span>

On créer l'environnement virutel:

> <span style="color:  #46ee1c  ">python3 -m venv env</span>

Puis on lance l'installation des modules nécessaires au fonctionnement du script:

> <span style="color:  #46ee1c  ">pip install -r requirements.txt</span>

Une fois les modules installés on active l'environnement virutel:

> <span style="color:  #46ee1c  ">source env/Scripts/Activate</span>

Il n'y a plus qu'à exécuter le script:

> <span style="color:  #46ee1c  ">python bot.py</span>

Voilà le script tourne vous pouvez interroger votre bot !
