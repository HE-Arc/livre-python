Pygame
======

.. image:: logo_pygame.png
   :align: right
   :alt: Pygame logo

Par Dany Chea [#dc]_

Introduction
------------

Pygame est un module qui offre des outils permettant de créer des jeux.
Le module est lui-même subdivisé en plusieurs sous-modules, ce qui permet de ne pas appeler des modules
qui serait inutiles.
On se contentera ici de présenter les bases de l'utilisation de Pygame, ainsi que le fonctionnement de certains sous-modules.

Liste des sous-modules de Pygame:

- :py:meth: `pygame.camera`
- :py:meth: `pygame.cdrom`
- :py:meth: `pygame.cursors`
- :py:meth: `pygame.display`
- :py:meth: `pygame.draw`
- :py:meth: `pygame.event`
- :py:meth: `pygame.examples`
- :py:meth: `pygame.font`
- :py:meth: `pygame.freetype`
- :py:meth: `pygame.gfxdraw`
- :py:meth: `pygame.image`
- :py:meth: `pygame.joystick`
- :py:meth: `pygame.key`
- :py:meth: `pygame.locals`
- :py:meth: `pygame.mask`
- :py:meth: `pygame.math`
- :py:meth: `pygame.midi`
- :py:meth: `pygame.mixer`
- :py:meth: `pygame.mixer.music`
- :py:meth: `pygame.mouse`
- :py:meth: `pygame.pixelcopy`
- :py:meth: `pygame.scrap`
- :py:meth: `pygame.sndarray`
- :py:meth: `pygame.sprite`
- :py:meth: `pygame.surfarray`
- :py:meth: `pygame.tests`
- :py:meth: `pygame.time`
- :py:meth: `pygame.transform`
- :py:meth: `pygame.version`

Squelette d'un code
-------------------
.. literalinclude:: exemple/skeleton.py

On peut voir ici que la création d'une fenêtre, indépendamment du jeu que l'on veut créer, passe par 5 étapes:
 -initialisation du module
 -appel des modules nécessaire
 -l'affichage
 -la boucle infinie
 -la fin

l'initialisation:
-----------------
Afin de pouvoir utiliser le module Pygame, il va falloir d'abord l'importer, puis l'initier de la manière suivante:

.. literalinclude:: exemple/skeleton.py
  :start-after: # begin_init
  :end-before: # end_init


le chargement des constantes
----------------------------
pygame contient une quantité de variable prédéfinies, qui se trouvent dans le module pygame.locals.
Pour les utiliser, on peut les importer de la manière suivante, afin d'éviter de réécrire à chaque fois pygame.CONSTANTE:

.. code-block:: python
  from pygame.locals import *

création de la fenêtre
----------------------
.. literalinclude:: exemple/test1.py


affichage: la notion de surface
-----------------------
tout doux

la boucle infinie
-----------------
Un jeu doit tourner continuellement, jusqu'au moment où l'on décide de fermer l'application, auquel cas on envoie le signal d'extinction.
pour se faire, on crée une boucle infinie, et on va attendre des instructions, comme des touches appuyées.


Conclusion
----------
Pygame est un mo

.. [#dc] <dany.chea@he-arc.ch>
