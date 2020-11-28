.. _random-tutorial:

==========
``random``
==========

.. image:: ./img/dice.png
    :scale: 45%
    :align: right
    :alt: Dice logo
    :target: http://silabs.se/media/1060/dice-2x.png

Par Christophe Hirschi [#email]_

Introduction
============

:py:mod:`random` est un module Python regroupant plusieurs fonctions
permettant de travailler avec des valeurs aléatoires.

La distribution des nombres aléatoires est réalisée par le générateur de nombres
pseudo-aléatoires `Mersenne Twister`_, l'un des générateurs les plus testés et
utilisés dans le monde informatique.

Module ``random``
=================

Le module comprend plusieurs fonctions travaillant chacune avec un type défini
de variables. Ces fonctions peuvent être séparées en trois groupes :

- Celles qui travaillent avec des nombres entiers
- Celles qui travaillent avec des nombres réels
- Celles qui travaillent avec des séquences (par exemple des listes).

Les fonctions de nombres entiers telles que :py:func:`random.randint` et
:py:func:`random.randrange` permettent de sélectionner arbitrairement une valeur
entière dans un intervalle donné.

Les fonctions de nombres réels, en plus de sélectionner des valeurs dans un
intervalle (avec les fonctions :py:func:`random.random` et
:py:func:`random.uniform` par exemple), permettent aussi de réaliser des
distributions gaussienne, exponentielles et logarithmiques.

Les fonctions de séquences permettent de manipuler des éléments dans une liste
donnée. Elles peuvent sélectionner un élément de la liste aléatoirement
(:py:func:`random.choice`), altérer l'ordre des éléments dans la liste elle-même
(:py:func:`random.shuffle`) ou encore retourner un nombre d'éléments aléatoires
d'une liste (:py:func:`random.sample`).

.. warning::
    Il est préférable d'éviter l'utilisation de :py:mod:`random` pour des
    applications liées à la cryptographie ou la sécurité en général (génération
    de mots de passe, authentification de compte, etc.) et de préférer le
    module :ref:`secrets-tutorial` à la place.

*Seeding*
=========

Comme spécifiés dans l'introduction, les nombres générés par :py:mod:`random`
sont de nature pseudo-aléatoire, c'est-à-dire qu'une *graine*, *seed* en
anglais, génère la suite de nombres. Dans le cas de :py:mod:`random`, la période
des *graines* est suffisamment élevée pour éviter de tomber sur les mêmes
numéros lors d'un usage commun. Cependant, il peut être utile dans certains cas
de répéter la même suite aléatoire de nombres. Pour cela, il est possible
d'indiquer à :py:mod:`random` la graine que l'on souhaite utiliser avec la
fonction :py:func:`random.seed` qui reçoit un nombre en argument, la *graine*.

.. literalinclude:: ./examples/random_seeding.py
   :linenos:

Résultats :

.. code-block:: console

    $ python random_seeding.py
    0.13436424411240122
    0.8474337369372327
    0.763774618976614

    $ python random_seeding.py
    0.13436424411240122
    0.8474337369372327
    0.763774618976614

Exemples
========

Avant toutes choses, il convient d'importer le module au projet :

.. code-block:: pycon

    >>> import random

Nombres réels
-------------

:py:func:`random.random` est la fonction la plus basique du module. Elle
retourne un nombre à virgule dans l'intervalle compris entre 0 et 1 non-compris
:math:`[0; 1[` :

.. code-block:: pycon

    >>> random.random()
    0.6982933392406706

:py:func:`random.uniform` permet de spécifier un intervalle. La fonction accepte
deux nombres comme arguments, *a* et *b*. Elle retourne un nombre à virgule
dans l'intervalle compris entre *a* et *b* non-compris :math:`[a; b[` :

.. code-block:: pycon

    >>> random.uniform(4.5, 7.5)
    5.292029100094782

Nombres entiers
---------------

Si l'on souhaite travailler avec des nombres entiers, il faut utiliser les
fonctions suivantes :

:py:func:`random.randint` accepte deux nombre comme arguments, *a* et *b*, et
retourne un nombre entier de l'intervalle compris entre *a* et *b*
:math:`[a;b]` :

.. code-block:: pycon

    >>> random.randint(2, 9)
    8

.. note::

    C'est la seule fonction qui prend en compte la valeur limite supérieur de
    l'intervalle dans son exécution.

:py:func:`random.randrange` accepte un nombre comme argument, *a*. Cette
fonction retourne un nombre entier compris entre 0 et *a* non-compris
:math:`[0; a[` :

.. code-block:: pycon

    >>> random.randrange(15)
    8

Elle accepte aussi deux nombres comme arguments, *a* et *b*.
Il est ainsi possible de spécifier le commencement de l'intervalle, ce qui
correspond à l'intervalle :math:`[a; b[` :

.. code-block:: pycon

    >>> random.randrange(10, 12)
    10

Il est possible d'ajouter un nombre en troisième argument pour indiquer
un pas dans l'intervalle :

.. code-block:: pycon

    >>> random.randrange(4, 8, 2) # Retourne un nombre paire.
    6

Séquences
---------

Il est possible d'utiliser certaines fonctions du module sur des listes
d'éléments :

:py:func:`random.choice` accepte une séquence comme argument, *seq*. Elle
retourne un élément de la séquence *seq* à condition que celle-ci ne soit pas
vide :

.. code-block:: pycon

    >>> random.choice(['dede', 'toto', 'lulu'])
    'lulu'

    >>> random.choice([4, 7, 11, 18])
    18

:py:func:`random.shuffle` accepte une séquence en argument, *seq*, et permet de
mélanger les éléments de la séquence *seq* :

.. code-block:: pycon

    >>> names = ['dede', 'toto', 'lulu']
    >>> random.shuffle(names)
    >>> names
    ['lulu', 'toto', 'dede']

    >>> numbers = [4, 7, 11, 18]
    >>> random.shuffle(numbers)
    >>> numbers
    [4, 11, 18, 7]

:py:func:`random.sample` prend en compte une séquence *seq* comme premier
argument et un nombre *k* en second argument. Elle permet de retourner une liste
de *k* éléments de la séquence *seq* aléatoirement :

.. code-block:: pycon

    >>> random.sample(['dede', 'toto', 'lulu', 'momo', 'bibi'], 3)
    ['momo', 'dede', 'bibi']

    >>> random.sample([10, 20, 30, 40, 50, 60], 4)
    [10, 30, 60, 50]

Exemple concret
---------------

L'exemple ci-dessous utilise la fonction :py:func:`random.shuffle` pour mélanger
un jeu de 52 cartes.

Dans un premier temps, les cartes sont créées et ajoutées une à une dans une
liste de cartes appelée *jeu*. Cette liste est ensuite mélangée, puis les 5
premières cartes du jeu mélangé sont attribuées au joueur.

.. literalinclude:: ./examples/cards_shuffling.py
   :linenos:

Résultats :

.. code-block:: console

    $ python cards_shuffling.py
    Main du joueur :
    - Valet de Pique
    - Dix de Trèfle
    - Dix de Carreau
    - Roi de Carreau
    - Trois de Coeur

    $ python cards_shuffling.py
    Main du joueur :
    - Dame de Coeur
    - Six de Coeur
    - As de Carreau
    - Deux de Trèfle
    - Sept de Carreau

Conclusion
==========

:py:mod:`random` permet bien plus d'utilisations que la simple attribution d'une
valeur dans un intervalle donné. Toutes ses fonctionnalités n'ont pu être
traitées ici (car certaines sont exotiques et/ou très spécifiques) et si vous
êtes désireux d'en connaitre encore un peu plus sur son sujet, visitez la
documentation officielle Python3 de :py:mod:`random`.

.. [#email] <christophe.hirschi@he-arc.ch>

.. Bibliographie

.. _Mersenne Twister: https://fr.wikipedia.org/wiki/Mersenne_Twister
