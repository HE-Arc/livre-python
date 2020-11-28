.. _matplotlib-tutorial:


==============
``matplotlib``
==============

Par Florian Fasmeyer [#ff]_

.. image:: ./sources/matplotlib.png
    :alt: matPlotLib membranePlot


Introduction
------------

matplotlib_ est une bibliothèque Python capable de produire des graphes de qualité.
matplotlib_ peut être utilisé dans des scripts Python, le shell Python et IPython_,
le notebook Jupyter_, des serveurs d'application web et dans quatre outils d'interface graphique.


.. image:: ./sources/surface3d_frontpage.png
   :alt: matPlotLib membranePlot

.. image:: ./sources/contour_frontpage.png
   :alt: matPlotLib contourPlot


.. image:: ./sources/membrane_frontpage.png
   :alt: matPlotLib membranePlot

.. image:: ./sources/histogram_frontpage.png
   :alt: matPlotLib histogramPlot

Matplotlib essai de rendre les tâches simples 'simples' et de rendre possible les choses compliqués.
Vous pouvez générer des graphes, histogrames, des spectres_ de puissance (lié à la transformée de Fourier),
des graphiques à bares, des graphiques d'erreur, des nuages de dispersion_, etc... en quelques lignes de code.

Pour des graphiques simples, le module :py:mod:`matplotlib.pyplot` fournit une
interface comme MATLAB spécialement adaptée avec IPython_.

Exemple
-------

Matplotlib_ est généralement utilisé avec :py:mod:`numpy`, permettant l'usage
de fonctions utiles comme :py:func:`~numpy.arange` qui dans notre cas est
utilisé pour la création de valeures à intervals réguliers de 0 à 5.

Matplotlib_ dispose de plus d'une centaine d'exemples (:ref:`examples-index`)
pour tous les cas possibles et imaginables.

Il vous est conseilé de vous rendre sur le site officiel et de jeter un  œil à la galerie_.

Cas simple
^^^^^^^^^^

.. image:: ./sources/exempleImportant.png
   :alt: matPlotLib exemple2

.. literalinclude:: code/simple.py

Cas pratique de statistique
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ./sources/example.png
   :alt: matPlotLib exemple1

.. literalinclude:: code/casPratique.py


Cas particulier avec toolkits pour la 3D
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ./sources/matplotlib-3d-graph-wire_frame-tutorial.png
   :alt: matPlotLib exemple3D

.. literalinclude:: code/exemple3d.py


How to
------

Liste non exhaustive expliquant comment utiliser matplotlib.
Le but est d'expliquer simplement des conceptes sur lesquels
vous risquez autrement de perdre du temps.

N'hésitez pas à visiter la page de :ref:`pyplot-tutorial` sur le site officiel
si vous comprenez l'anglais ou le code_.

Conseil, regardez les fonctions suivantes en détail

- plot(\*args, \*\*kwargs)
- triplot(\*args, \*\*kwargs)
- bar(left, height, width=0.8, bottom=None, hold=None, data=None, \*\*kwargs)
- hist(x, bins=None, ..., \*\*kwargs)
- boxplot(x, notch=None, ...)

.. todo::

    Il manque les liens *intersphinx*.

Graphique simple
^^^^^^^^^^^^^^^^

Le :py:func:`~matplotlib.pyplot.plot` est la fonction la plus importante de
`matplotlib`_ (on se demande pourquoi), pour cette raison il vous est
recommandé de regarder la doc :py:mod:`matplotlib.pyplot` en détail.

.. image:: ./sources/simplesimple.png
   :alt: matPlotLib ro

.. literalinclude:: code/simpleNoNumpy.py


Lignes, points, tirets
^^^^^^^^^^^^^^^^^^^^^^

.. image:: ./sources/ro.png
   :alt: matPlotLib ro

Pour changer l'affichage de ligne à points ou traitillé, il suffit d'ajouter
un argument au moment de plot! Voir :py:func:`~matplotlib.pyplot.plot`.

.. literalinclude:: code/ro.py

Axes et axes mineurs
^^^^^^^^^^^^^^^^^^^^

.. image:: ./sources/axe.png
   :alt: matPlotLib axes

Pour modifier les axes l'on a besoin d'un objet que subplot retourne, d'où
l'étrange ``subplot(111)``.

Vous remarquerez l'axe mineur, qui s'affiche tous les :math:`0.1` ticks.

Dans cet exemple l'on ne touche qu'à 'x'. 'y' est en mode par défaut, il se met
directement à la bonne position. Notez bien qu rien ne vous empèche de faire
des échelles étranges ou logarithmiques_. Voir :py:mod:`numpy`.

.. literalinclude:: code/axe.py


Afficher plusieurs graphes
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ./sources/AEGXG.png
   :alt: matPlotLib subplot

.. literalinclude:: code/sub.py


Vous pouvez aussi produire des assemblements asymétriques:

.. image:: ./sources/subPlot.png
   :alt: matPlotLib subPlot2 printscreen Florian Fasmeyer 22.03.2017

.. literalinclude:: code/sub2.py


Conclusion
----------

Matplotlib est une bibliothèque extraordinaire permettant de gagner beaucoup de
temps dans les applications nécessitant un affichage de données sous forme de
graphiques.

Crédits
-------

    Matplotlib_ est un projet par John Hunter (1968 - 2012) qui à l'aide de
    nombreux contributeurs, ont donné une quantité incommensurable de travail
    dans la production de ce software. Dans le cas ou Matplotlib contribue à un
    projet menant à des publications scientifiques, il vous est prié de faire
    reconnaitre ce travail en le citant dans votre projet. Vous pouvez utiliser
    cette citation_ prête à l'usage.

Sources
-------
- Matplotlib_.org
- PythonProgramming_.net
- StackOverflow.com subPlot_

.. Bibliographie

.. _matplotlib: http://matplotlib.org/
.. _IPython: https://ipython.org/
.. _Jupyter: http://jupyter.org/
.. _galerie: http://matplotlib.org/gallery.html
.. _spectres: https://fr.wikipedia.org/wiki/Densit%C3%A9_spectrale_de_puissance
.. _dispersion: http://spss.espaceweb.usherbrooke.ca/media/images/Site%20v17/nuage1.jpg
.. _citation: http://matplotlib.org/2.0.0/citing.html
.. _PythonProgramming: https://pythonprogramming.net/conclusion-matplotlib-tutorial/
.. _subPlot: http://stackoverflow.com/questions/3584805/in-matplotlib-what-does-the-argument-mean-in-fig-add-subplot111
.. _logarithmiques: https://www.ilemaths.net/img/forum_img/0416/forum_416807_1.JPG
.. _code: https://2.bp.blogspot.com/-2mxHUrtNNQI/VvCP1V94pNI/AAAAAAAAEqw/h9IWBjCeMowykzM8uXWWoOb3BymaZNTIQ/s1600/matrix-600x400.jpg

.. [#ff] <florian.fasmeyer@he-arc.ch>
