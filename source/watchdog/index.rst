.. _watchdog-tutorial:

========
WatchDog
========

Par Paul Jeanbourquin [#pj]_

Introduction
------------

Watchdog est une librairie permettant l'utilisation d'événemement du système de f
ichier (création de fichier, modification, ...).

Cette librairie peut-être utilisée pour la mise en place d'un scanner de fichier dynamique
(exemple Scanner multimédia)
ou pour la mise en place d'un système d'audit des événements sur les fichiers.

Fonctionnement
--------------

Pour intercepter les événements il faut créer un class qui va contenir les fonctions par événements.

Un exemple d'une classe pour un système d'audit :

.. code-block:: python3

  from watchdog.events import FileSystemEventHandler

  class AuditHandler(FileSystemEventHandler):
    def on_modified(self, event):
      print("Le fichier %s a été modifié" % event.src_path)
    def on_created(self,event):
      print("Le fichier %s a été créé" % event.src_path)
    def on_deleted(self,event):
      print("Le fichier %s a été supprimé" % event.src_path)

Liste d'événements interceptable :

============  =============================================
      Nom                      Déclanchement
============  =============================================
on_modified   Modification d'un fichier / dossier
on_created    Création d'un fichier / dossier
on_deleted    Suppression d'un fichier / dossier
on_moved      Déplacement / renomage d'un fichier / dossier
on_any_event  Dans tous le cas au-dessus
============  =============================================

La classs doit, ensuite, être liée à un observateur.
C'est ici que nous spécifierons le dossier qui devra être observer.

.. code-block:: python3

  observer = Observer() # Création de l'observeur
  observer.schedule(eventHandler.AuditHandler(), path='U:', recursive=True) # Création du lien
  observer.start() # Démarrage de l'observateur

Dans ce cas l'observateur surveille le dossier "U:" de manière recursive.

Un observateur étant lancer dans un thread sépraré, il faut bloquer l'éxecution du script.
Mais, nous aimerions aussi pouvoir fermer le script par interuption du clavier.
La fermeture de l'observateur doit aussi être douce. Pour ce faire nous utiliserons le code ci-dessous.

.. code-block:: python3

  import time

  try:
    while True: # Boucle infinie bloquant l'execution du script
        time.sleep(1) # petite attente d'une millisecondes
  except KeyboardInterrupt: # Prise en charge de l'interuption par le clavier
        observer.stop() # Arret de l'observateur
        observer.join() # Attend que l'observateur se soit bien fermer

Exemple
-------

Todo

Contenu
----------

ToDo

Conclusion
----------

ToDo


.. [#pj] <paul.jeanbourquin@he-arc.ch>

.. Bibliographie (ceci est un commentaire)
