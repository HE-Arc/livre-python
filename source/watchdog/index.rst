.. _watchdog-tutorial:

========
WatchDog
========

Par Paul Jeanbourquin [#pj]_

Introduction
------------

Watchdog est une librairie permettant l'utilisation d'événemement du système de f
ichier (création de fichier, modification, ...).

Cette librairie peut-être utilisée (par exemple) pour la mise en place d'un scanner de fichier dynamique
(exemple Scanner multimédia)
ou pour la mise en place d'un système d'audit des événements sur les fichiers.
Dans le cadre de cet article, notre fils rouge sera la création d'un programme d'audit
des événements émis par les fichiers de musiques.

Fonctionnement
--------------

Traitement de l'événement
=========================

Pour intercepter les événements il faut créer une classe qui va contenir les fonctions par événements.

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

================  =============================================
      Nom                      Déclanchement
================  =============================================
``on_modified``   Modification d'un fichier / dossier
``on_created``    Création d'un fichier / dossier
``on_deleted``    Suppression d'un fichier / dossier
``on_moved``      Déplacement / renomage d'un fichier / dossier
``on_any_event``  Dans tous les cas ci-dessus
================  =============================================

L'objet ``event`` est une instance de la classe :py:class:`watchdog.events.FileSystemEvent`.
Cette classe est dérivée pour chaque type d'événement. Elle contient les attributs suivant :

=================   ===========================================================
Attribut            Description
=================   ===========================================================
``event_type``      Le type d'événement en string
``is_directory``    Boolean signalant si l'événement s'applique à un dossier
``src_path``        Chemin du fichier ayant lancé l'événement
``dest_path``       Fichier de destination (Uniquement lors d'un ``on_moved``)
=================   ===========================================================

Interception de l'événement
===========================

La classe doit, ensuite, être liée à un observateur.
C'est ici que nous spécifierons le dossier qui devra être observer.

.. code-block:: python3

  import eventhandler
  from watchdog.observers import Observer

  observer = Observer() # Création de l'observeur
  observer.schedule(eventhandler.AuditHandler(), path='U:', recursive=True) # Création du lien
  observer.start() # Démarrage de l'observateur

Dans ce cas, l'observateur surveille le dossier ``"U:"`` de manière recursive.

Bloquer le script
=================

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

Filtrage
============

Il est possible de filtrer les fichiers sur lesquelles les events sont interceptés,
ce qui est utile si l'on souhaite (par exemple) traiter que certain type de fichiers (par ex. les .mp3).

Pour ce faire, il faut utiliser une autre classe de base pour la classe de traitement.
Deux classes dérivant de :py:class:`watchdog.events.FileSystemEventHandler` sont fournies (liste dans le tableau ci-dessous).

===============================   ===========================================
Nom                               Utilisation
===============================   ===========================================
``FileSystemEventHandler``        Handler de base (sans filtre)
``PatternMatchingEventHandler``   Handler utilisant un pattern pour filtrer
``RegexMatchingEventHandler``     Handler utilisant un regex pour filtrer
===============================   ===========================================

L'utilisation de la version avec les patterns étant la même que celle avec les regexes,
nous utiliserons la version patterns dans la suite.
Par exemple si l'on souhaite reprendre le code du programme d'audit fait plus haut mais,
qui s'occupe que des fichiers de musique (.mp3, .flac, .wav).

.. code-block:: python3

  from watchdog.events import PatternMatchingEventHandler

  class AuditHandlerMusic(PatternMatchingEventHandler):
      def on_modified(self, event):
          print("Le fichier %s a été modifié" % event.src_path)
      def on_created(self,event):
          print("Le fichier %s a été créé" % event.src_path)
      def on_deleted(self,event):
          print("Le fichier %s a été supprimé" % event.src_path)

La classe de traitement ne change quasiment pas la seule différence est le changement de la classe de base.
La principale différence ce trouvera au moment de l'instantation de l'objet.

.. code-block:: python3

  import eventhandler
  from watchdog.observers import Observer

  observer = Observer()
  handler = eventhandler.AuditHandlerMusic(patterns=["*.mp3", "*.wav", "*.flac"])
  observer.schedule(handler, path='U:', recursive=True)
  observer.start()

Ici nous avons instancier l'objet avant de le passer en arguments à la fonction.
Nous spécifions aussi un 1er arguement du constructeur
qui se trouve dans ce cas être les patterns à traités.

Les autres arguments possible sont dans l'ordre :

========================================  ====================  ================================================================================
Noms                                      Default               Utilisation
========================================  ====================  ================================================================================
``patterns``/``regexes``                  ``None``/``[".*"]``   Spécifie les patterns (respectivement regexes) à traiter
``ignore_patterns`` / ``ignore_regexes``  ``None``/``[]``       Spécifie les patterns (respectivement regexes) à ignorer
``ignore_directories``                    ``False``             Si mit à ``True`` ignore les dossiers
``case_sensitive``                        ``False``             Si mit à ``True`` rend le patterns (respectivement regex) sensible à la casse
========================================  ====================  ================================================================================

Conclusion
----------

En conclusion, la bibliothèque watchdog permet d'utiliser des événements, en provenance du système de fichiers, d'une manière facile et efficace.
Watchdog permet aussi de filtrer les fichiers / dossiers émetant un événement.
Cette bibliothèque permet aussi une grande réusabilité du code grâce, entre autre, à l'utilisation de classe pour le traitement des événements.

.. [#pj] <paul.jeanbourquin@he-arc.ch>

Bibliographie
-------------

* watchdog documentation : http://pythonhosted.org/watchdog/
* Tutoriel d'utilisation de watchdog : http://sametmax.com/reagir-a-un-changement-sur-un-fichier-avec-watchdog/
