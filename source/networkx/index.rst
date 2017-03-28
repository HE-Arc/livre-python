.. _networkX-tutorial:

``networkX``
============

Par Deni Gahlinger [#dg]_

Introduction
------------

:py:mod:´NetworkX´_ est une librairie Python qui permet d'instancier des graphes composés de noeuds
et de ponts, ou liens. Grâce à cette librairie, la manipulation de ces graphes est simplifiée

Un graphe, c'est un ensemble d'objet ou noeud pouvant être reliés par des ponts. Il existe plusieurs
opérations et calculs sur les graphes. les graphes que NetworkX permet d'instancier peuvent
contenir comme noeud nimporte quel objet hashable.

Nous allons donc voir premièrement un exemple d'instanciation de noeuds,
ensuite découvrire les différentes sortes de graphes ainsi que les opérations sur elles,
et finalement comprendre les différents types d'affichages de graphes.

Instanciation
-------------

Voici un exemple d'instanciation d'un graphe simple avec NetworkX.
Comme NetworkX prend nimporte quel objet hashable comme noeud, l'exemple prendra
des int.

.. literalinclude:: ./examples/instanciation.py

Opération sur des graphes
-------------------------

NetworkX permet différentes opérations sur les graphes. En voici un exemple :

.. literalinclude:: ./examples/OperationGraphes.py

Dessin d'un graphe
------------------

NetworkX n'est pas fait spécialement pour dessiner un graphe.

.. literalinclude:: ./examples/Dessin.py

Conclusion
----------

On peut voir que NetwokX est une librairie assez simple à utiliser dans les bases, mais est assez complète
Cette librairie est vraiment utile pour différentes problématique touchant les graphes et la théories des graphes
comme le voyageur de commerce. Certains problèmes mathématiques dans ce domaine peuvent avoir une
grande complexité (complexité non polynomiale).

L'existance d'une librairie comme NetworkX permet de manipuler des graphes de façon simple et offre plusieurs
options utile pour une utilisation assez large dans le domaine des graphes. 


.. [#dg] <deni.gahlinger@he-arc.ch>

.. Bibliographie

.. _NetworkX: https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html
