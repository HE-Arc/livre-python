.. _pillow-tutorial:

================================
Python Imaging Library (``PIL``)
================================

.. image:: ../_static/pillow.png
   :align: right
   :alt: Pillow logo

Par Quentin Vaucher. [#qv]_

Introduction
------------

Pillow_ est une bibliothèque de traitement d'image, qui est un fork et
successeur du projet PIL_ (*Python Imaging Library*). Elle est conçue
de manière à offrir un accès rapide aux données contenues dans une image, et offre
un support pour différents formats de fichiers tels que PPM, PNG, JPEG, GIF,
TIFF et BMP.

Pillow_ dispose de capacités de traitement d'images relativement puissantes, et
a pour but d'offrir une solide base à toute application générale de traitement d'images.

Domaines d'utilisations
-----------------------

La bibliothèque de fonctions peut être utilisée pour différents types d'activités, telles que:

**Archivage d'images**:
  Création de miniatures, conversion d'images d'un format de fichier à un autre, ...
**Affichage d'images**:
  Création et affichage d'images via le module :py:mod:`PIL.ImageTk`, ou :py:mod:`PIL.ImageWin` sous Windows. Ouverture d'une image dans un utilitaire externe via la méthode :py:meth:`PIL.Image.Image.show`.
**Traitement d'images**:
  Offre un support pour quelques fonctions de bases telles que le filtrage, la convolution ou encore la conversion d'espaces couleurs. Il est également possible de redimensionner et d'appliquer des transformations géométriques à l'image (rotation, ...).


Concepts
--------

La bibliothèque utilise le principe d'images matricielles (par opposition aux images vectorielles), c'est-à-dire que chaque élément de la matrice représente un point avec une couleur associée (= un pixel). Pillow_ utilise également les :ref:`concepts des bandes <concept-bands>` et de :ref:`modes <concept-modes>` décrits ci-dessous:

**Bandes**:
  Les images sont constituées de bandes de données (une ou plusieurs, pour autant que celles-ci aient toute les mêmes dimensions et profondeurs). Un exemple commun de bandes est celles sous la forme RGBA, qui sépare les informations sur le rouge, le vert, le bleu et la transparence. Il est ainsi possible de réaliser différentes actions qui agissent que sur une seule bande. Finalement, du point de vue des pixels, on peut dire qu'ils disposent tous d'une valeur par bande.
**Modes**:
  Ils définissent le type et la profondeur des pixels d'une image. Parmi les modes les plus connus, on peut notamment citer RGB et RGBA, qui représentent les pixels sur respectivement 3x8 bits et 4x8 bits.

Exemples
--------

Le premier exemple ci-dessous permet dans un premier temps de se familiariser avec le fonctionnement de base de Pillow_, puis une fois les bases acquises, un deuxième exemple plus technique met en évidence la puissance de la bibliothèque.

Exemple basique
'''''''''''''''

L'exemple suivant aborde de manière simple quelques notions de bases de Pillow_. Une image en couleur au format *.png* est récupérée et convertie en nuances de gris. Le résultat s'affiche puis est sauvegardé au format *.jpeg*.

- :py:func:`~PIL.Image.open` charge une image en mémoire;
- :py:meth:`Image.convert() <PIL.Image.Image.convert>` change le mode de l'image. ``L`` représente :math:`256` nuances de gris (voir :ref:`modes <concept-modes>`).
- :py:meth:`Image.show() <PIL.Image.Image.show>` ouvre l'image dans un outil externe;
- :py:meth:`Image.save() <PIL.Image.Image.save>` sauvegarde l'image dans le format spécifié.

.. literalinclude:: ./examples/example.py
  :linenos:

Le résultat obtenu est le suivant:

.. image:: ../_static/gray-pillow.jpeg
  :align: center
  :alt: Logo de Pillow en nuances de gris

Exemple technique
'''''''''''''''''

Dans cet exemple, le logo de la bibliothèque Pillow_ subit diverses modifications afin de mettre en pratique quelques fonctions de la bibliothèque. Le logo est d'abord flouté à l'aide d'un filtre, puis transposé afin d'inverser la position de chaque python. On parcourt ensuite tous les pixels, puis on colorie l'arrière-plan en étudiant les attributs de chacun d'eux (couleurs et position).

- :py:meth:`PIL.Image.Image.filter` filtre l'image;
- :py:meth:`PIL.Image.Image.transpose` retourne l'image;
- :py:meth:`PIL.Image.Image.getpixel` récupère les attributs du pixel à la position donnée;
- :py:meth:`PIL.Image.Image.putpixel` modifie  les attributs du pixel à la position donnée.

.. literalinclude:: ./examples/example2.py
  :linenos:

Le résultat obtenu est le suivant:

.. image:: ../_static/logoFiltre.png
   :align: center
   :alt: Cercle Trigonométrique

Manipulation des bandes
-----------------------

Pillow_ utilise le :ref:`concept des bandes de données<concept-bands>`, qu'il est possible de traiter séparément. L'exemple suivant illustre cette notion, en inversant l'ordre des bandes R, G et B.

- :py:meth:`PIL.Image.Image.split` retourne un tuple contenant toutes les bandes de l'image;
- :py:func:`PIL.Image.merge` fusionne un ensemble d'images monobande en une image multibandes.

.. literalinclude:: ./examples/bandes.py
  :linenos:

Le résultat obtenu est le suivant:

.. image:: ../_static/logoBandes.png
  :align: center
  :alt: Suppression du rouge dans le logo de Pillow


Méthodes de dessin
------------------

Pillow_ fournit également des outils de base pour le graphisme 2D. Toutes ces fonctions sont regroupées dans le module :py:mod:`PIL.ImageDraw`. Il est possible de dessiner diverses formes géométriques, ainsi que du texte, dans le but de créer ou retoucher des images. L'exemple suivant met en évidence quelques-unes des fonctionnalités disponibles.

- :py:func:`PIL.Image.new` crée une image avec la taille et la couleur spécifiée;
- ``PIL.ImageDraw.Draw`` crée un objet qui peut être utilisé pour dessiner sur l'image;
- ``PIL.ImageDraw.Draw.line`` dessine une ligne entre les points donnés, avec la couleur choisie;
- ``PIL.ImageDraw.Draw.ellipse`` dessine une ellipse à l'intérieur du rectangle donné;
- ``PIL.ImageDraw.Draw.text`` dessine du texte à l'endroit choisi.

.. literalinclude:: ./examples/drawing.py
  :linenos:

Le résultat obtenu est le suivant:

.. image:: ../_static/cercleTrigo.png
   :align: center
   :alt: Cercle Trigonométrique

Utilisation au sein du binding PyQt
-----------------------------------

Pillow_ fournit le module :py:mod:`PIL.ImageQt` afin de créer des Qimage directement utilisables par le binding PyQt. En effet, le module dispose d'une classe du même nom qui est une sous-classe de QtGui.QImage. Il est donc possible de passer l'objet directement à l'API PyQt. On peut donc utiliser la puissance de Pillow_ pour réaliser du traitement d'images au sein d'un logiciel graphique utilisant le Framework Qt.

Le code suivant illustre un telle utilisation, permettant à l'utilisateur de visualiser une image, de la tourner et de la flouter. Le traitement de l'image est réalisé à l'aide de Pillow_, tandis que l'interface utilisateur utilise l'api PyQt. La fonction ``initUI()`` n'est pas présentée car elle ne sert qu'à mettre en place les différents composants visuels.

.. literalinclude:: ./examples/pyqt.py
  :lines: 1-54, 80-
  :linenos:

Le résultat obtenu est le suivant:

.. image:: ../_static/pyqt.png
  :align: center
  :alt: Application PyQt avec traitement d'images réalisé par Pillow

Conclusion
----------

Pillow_ est une bibliothèque relativement complète qui offre la possibilité de manipuler des images avec une grande simplicité. Elle dispose d'une large palette de fonctions qui touche à différents domaines allant du filtrage au graphisme, en passant par la manipulation de pixels.

La bibliothèque se positionne donc plutôt comme une bibliothèque à vocation généraliste dans le domaine du traitement d'images, et ne se démarque donc dans aucun domaine spécifique.

Pour conclure, les quelques exemples abordés dans cet article offrent un bon aperçu du fonctionnement de Pillow_, mais ne couvrent en aucun cas toutes ses possibilités. Pour une liste plus exhaustive et plus détaillée, la `documentation officielle`_ semble être la candidate idéale.

.. [#qv] <quentin.vaucher@he-arc.ch>

.. Bibliographie

.. _Pillow: https://python-pillow.org/
.. _PIL: http://www.pythonware.com/products/pil/
.. _documentation officielle: https://pillow.readthedocs.io/en/latest/
