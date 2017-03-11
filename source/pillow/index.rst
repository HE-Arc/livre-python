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
successeur du projet PIL_ (*Python Imagin Library*). Elle est conçu
de manière à offrir un accès rapide au données contenues dans une image, et offre
un support pour différents formats de fichiers tel que PPM, PNG, JPEG, GIF,
TIFF et BMP.

Domaines d'utilisations
-----------------------

Pillow_ peut être utilisé pour différents types d'activités, tel que:

**Archivage d'images**:
  Création de miniatures, conversion d'images d'un format de fichier à un autre, ...
**Affichage d'images**:
  Création et affichage d'images via le module :py:mod:`ImageTK` ou :py:mod:`ImageWin` sous Windows. Ouverture d'une image dans un utilitaire externe via la méthode :py:meth:`show`.
**traitement d'images**:
  Offre un support pour quelques fonctions de bases tel que le filtrage, la convolution ou encore la conversion d'espaces couleurs. Il est également possible de redimensionner et d'appliquer des tranformations géométriques à l'image (rotation, ...).




.. [#qv] <quentin.vaucher@he-arc.ch>

.. _Pillow: https://python-pillow.org/
.. _PIL: https://en.wikipedia.org/wiki/Python_Imaging_Library
