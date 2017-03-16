=======
.. _Invoke-tutorial:

INVOKE
======
Par Jonathan Guerne

Introduction
------------
l'utilié de Invoke est de pouvoir très simplement lancer des tâches que vous
aurez déjà préparé au par avant et qui exécuteront par exemple des lignes de
commande.

Installation
------------
pour pouvoir utiliser les commandes propres à la librairie Invoke il faut d'abord
s'assurer de l'avoir installée dans son environnememt python.
Comme d'habitude on utilise pip pour installer des librairies externe.

::

  $ pip install invoke 
On va ensuite mettre en place un fichier nommé ``tasks.py``.
