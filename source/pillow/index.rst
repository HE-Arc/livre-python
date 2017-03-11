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
  :linenos:

Example technique
'''''''''''''''''

Dans cet example, le logo de la librairie Pillow_ subit divers modification afin de mettre en partique quelques fonctions de la bibliothèque. Le logo est d'abord flouté, puis retourner afin d'inverser la position de chaque python. On parcourt ensuite chaque pixel, puis on colorie l'arrière-plan en étudiant les attributs de chaque pixels (couleurs et position).

.. literalinclude:: ./examples/example2.py
  :linenos:

Le résultat obtenu est le suivant:

.. image:: ../_static/logoFiltre.png
   :align: center
   :alt: Cercle Trigonométrique

Méthodes de dessin
------------------

Pillow_ fournit également des outils de base pour le graphisme 2D. Toutes ces fonctions sont regroupées dans le module :py:mod:`ImageDraw`. Il est possible de dessiner divers formes géométriques, ainsi que du texte, dans le but de créer ou retoucher des images. l'exemple suivant met en évidence quelques unes des fonctionnalités disponibles.

- :py:meth:`Image.new` crée une image avec la taille et la couleur spécifiée;
- :py:meth:`ImageDraw.Draw` crée un objet qui peut être utilisé pour dessinier sur l'image;
- :py:meth:`Draw.line` dessine une ligne entre les points donnés, avec la couleur choisie;
- :py:meth:`Draw.ellipse` dessine une ellipse à l'intérieur du rectangle donné;
- :py:meth:`Draw.text` dessine du texte à l'endroit choisi.

.. literalinclude:: ./examples/drawing.py
  :linenos:

Le résultat obtenu est le suivant:

.. image:: ../_static/cercleTrigo.png
   :align: center
   :alt: Cercle Trigonométrique

Utilisation au sein du binding PyQt
-----------------------------------

Pillow_ fournit le module :py:mod:`ImageQt` afin de créer des Qimage directement utilisables par le binding PyQt. En effet, le module dispose d'une classe du même nom qui est une sous-calsse de QtGui.QImage. Il est donc possible de passer l'objet directement à l'API PyQt.


.. [#qv] <quentin.vaucher@he-arc.ch>

.. _Pillow: https://python-pillow.org/
.. _PIL: http://www.pythonware.com/products/pil/
.. _mode: https://pillow.readthedocs.io/en/4.0.x/handbook/concepts.html#modes
