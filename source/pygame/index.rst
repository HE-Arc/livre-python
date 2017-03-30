.. _pygame-tutorial:

==========
``pygame``
==========

.. image:: logo_pygame.png
   :align: right
   :alt: Pygame logo

Par Dany Chea [#dc]_

Introduction
============

Pygame est un module qui offre des outils permettant de créer des jeux.
Le module est lui-même subdivisé en plusieurs sous-modules, ce qui permet de ne pas appeler des modules qui seraient inutiles.
On se contentera ici de présenter les bases de l’utilisation de Pygame, ainsi que le fonctionnement de certains sous-modules.

Liste des sous-modules de Pygame:

+------------------+------------------+-------------------+-------------------+
| `pygame.camera`  | `pygame.cdrom`   | `pygame.cursors`  | `pygame.display`  |
+------------------+------------------+-------------------+-------------------+
| `pygame.draw`    | `pygame.event`   | `pygame.examples` | `pygame.font`     |
+------------------+------------------+-------------------+-------------------+
| `pygame.freetype`| `pygame.gfxdraw` | `pygame.image`    | `pygame.joystick` |
+------------------+------------------+-------------------+-------------------+
| `pygame.key`     | `pygame.locals`  | `pygame.mask`     | `pygame.math`     |
+------------------+------------------+-------------------+-------------------+
| `pygame.midi`    | `pygame.mixer`   | `pygame.mouse`    | `pygame.pixelcopy`|
+------------------+------------------+-------------------+-------------------+
| `pygame.scrap`   | `pygame.sndarray`| `pygame.sprite`   | `pygame.surfarray`|
+------------------+------------------+-------------------+-------------------+
| `pygame.test`    | `pygame.time`    | `pygame.transform`| `pygame.version`  |
+------------------+------------------+-------------------+-------------------+

.. À quoi ça sert?

Indépendemment du jeu que l’on veut créer, sa réalisation passe nécessairement par cinq étapes:

#. Initialisation de pygame
#. Appel des modules nécessaires
#. L’affichage
#. Boucle infinie
#. Fermeture du programme

Initialisation
--------------

Afin de pouvoir utiliser le module Pygame, il va falloir d'abord l'importer, puis l'initier de la manière suivante:

.. code-block:: pycon

    >>> import pygame
    >>> pygame.init()


``pygame.locals``
^^^^^^^^^^^^^^^^^

pygame contient une quantité de constantes prédéfinies, qui sont chargées dans le namespace pygame, lors de l’importation de celui-ci. Ainsi, lorsque l’on veut utiliser une des constantes, il faut à chaque fois l’appeler en préfixant pygame. suivi du nom de la constante. Afin d’éviter ce préfixe, on peut faire une importation des constantes depuis :py:mod:`pygame.locals`, comme ci-dessous:

.. code-block:: python

    >>> from pygame.locals import *

Appel des fonctions utiles
--------------------------

C’est dans cette partie que l’on va initialiser la fenêtre, ainsi que tout les éléments dont on aura besoin.

par exemple, pour afficher une fenêtre:

.. code-block:: pycon

    >>> fenetre = pygame.display.set_mode((200, 200))

Dans cet exemple, on appelle la fonction :py:func:`~pygame.display.set_mode` du module display. Ce que l’on obtient en retour, c’est un objet de la classe Surface qui est défini par Pygame.

Résultat:

.. image:: exemple/firstWindow.PNG

La boucle infinie
-----------------

Si on se contentait d’exécuter le code ci-dessus, on n’obtiendrait le résultat que pendant une fraction de seconde, car au moment où le code a fini de s’exécuter, il se termine. Il faut donc créer une boucle infinie, de laquelle on peut sortir au moyen d’une action de l’utilisateur.

Exemple de fenêtre simple
-------------------------

Cet exemple provient de :ref:`makegames-2`.

.. literalinclude:: exemple/simpleWindow.py


Exemples
========

Petit lecteur audio simple
^^^^^^^^^^^^^^^^^^^^^^^^^^
Cet exemple provient du `tutoriel OpenClassrooms`_
.. literalinclude:: exemple/mixerEx.py

Dans cet exemple, plusieurs modules sont utilisés, notamment: pygame.mixer, qui est utilisé pour la gestion de sons, pygame.event, qui est utilisé pour la gestion des touches au clavier, pygame.draw, pour dessiner les boutons et pygame.mouse, pour récupérer les coordonnées de la souris.
Ici, on a créé un petit lecteur audio. Lorsque l'on appuie sur play/stop, le son de lance/s'arrête.
pour créer les boutons, on a utilisé la fonction de dessin de pygame.draw.
pour l'illumination des boutons au passage de la souris, il faut récupérer la position de la souris, et la comparer avec la zone dans laquelle est dessinée le rectangle.

résultat:

.. image:: exemple/LecteurAudio.PNG

Affichage simple d'images
-------------------------

.. literalinclude:: exemple/loadBg.py

Dans cet exemple, on commence par charger une image. Cette image n’étant pas forcément dans un format supporté par pygame, la fonction pygame.convert est utilisée afin de s’assurer que l’image pourra s’afficher correctement.

.. convert est également une méthode. Et c'est dommage d'être resizable et de ne
   rien faire avec ça.

.. code-block:: pycon

  >>> fond = pygame.image.load("background.jpg").convert()

Enfin, on peut afficher l’image en la “collant” sur la fenêtre de base, avec la fonction blit().

.. code-block:: pycon

  >>> fenetre.blit(fond,(0,0))

Il est a noter que la fonction blit prend en paramètre une Surface, donc l’objet à afficher, ainsi que la position, en sachant que la coordonnée (0,0) est en haut à gauche de la fenêtre.

.. blit est une méthode j'imagine.

Conclusion
==========

*pygame* est un module très complet, qui nous permet de réaliser des jeux avec une certaine rapidité. Les quelques méthodes présentées ici ne sont qu’une infime partie des méthodes que propose pygame. Afin d’en avoir une liste exhaustive, il est recommandé d’aller consulter la documentation officielle de :py:mod:`pygame`,


.. [#dc] <dany.chea@he-arc.ch>

.. _tutoriel OpenClassrooms: https://openclassrooms.com/courses/interface-graphique-pygame-pour-python/le-son-5
