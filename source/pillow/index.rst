.. _pillow-tutorial:

======================
Python Imaging Library
======================

par Quentin Vaucher.
=======

Pillow
======

.. image:: ../_static/pillow.png
   :align: right
   :alt: Pillow logo

Par Quentin Vaucher [#qv]_

Introduction
------------

Pillow_ est une bibliothèque de traitement d'image, qui est un fork et
successeur du projet PIL_ (*Python Imaging Library*). Elle est conçu
de manière à offrir un accès rapide au données contenues dans une image, et offre
un support pour différents formats de fichiers tel que PPM, PNG, JPEG, GIF,
TIFF et BMP.

Pillow_ dispose de capacités de traitement d'images relativement puissantes, et
a pour but d'offrir une solide base à toute application générale de traitement d'image.

Domaines d'utilisations
-----------------------

La bibliothèque de fonctions peut être utilisée pour différents types d'activités, tel que:

**Archivage d'images**:
  Création de miniatures, conversion d'images d'un format de fichier à un autre, ...
**Affichage d'images**:
  Création et affichage d'images via le module :py:mod:`ImageTK`, ou :py:mod:`ImageWin` sous Windows. Ouverture d'une image dans un utilitaire externe via la méthode :py:meth:`show`.
**Traitement d'images**:
  Offre un support pour quelques fonctions de bases tel que le filtrage, la convolution ou encore la conversion d'espaces couleurs. Il est également possible de redimensionner et d'appliquer des tranformations géométriques à l'image (rotation, ...).


Examples
--------

Le premier example ci-dessous permet dans un premier temps de se familiariser avec le fonctionnement de base de Pillow_, puis, une fois les bases acquises, un deuxième example plus technique met en évidence la puissance de la bibliothèque.

Example basique
'''''''''''''''

L'example suivant aborde de manière simple quelques notions de bases de Pillow_. Une image en couleur au format *.png* est récupérée et convertie en nuances de gris. Le résultat s'affiche puis est sauvegardé au format *.jpeg*.

- :py:meth:`Image.open` charge une image en mémoire;
- :py:meth:`Image.convert` change le mode_ de l'image;
- :py:meth:`Image.show` ouvre l'image dans un outil externe;
- :py:meth:`Image.save` sauvegarde l'image dans le format spécifié.

.. literalinclude:: ./examples/example.py

Example technique
'''''''''''''''''


.. [#qv] <quentin.vaucher@he-arc.ch>

.. _Pillow: https://python-pillow.org/
.. _PIL: https://en.wikipedia.org/wiki/Python_Imaging_Library
.. _mode: https://pillow.readthedocs.io/en/4.0.x/handbook/concepts.html#modes
