.. _random-tutorial:

==========
``random``
==========

Par Christophe Hirschi [#email]_

Introduction
============

:py:mod:`random` est un module Python regroupant plusieurs fonctions
permettant de travailler avec des valeurs aléatoires. La distribution des
nombres aléatoires est réalisée par le générateur de nombres pseudo-aléatoires
`Mersenne Twister`_, l'un des générateurs les plus testés et utilisés dans le
monde informatique.

.. warning::
    Il est préférable d'éviter l'utilisation de :py:mod:`random` lors d'applications
    de sécurité ou de cryptographie et d'utiliser le module :py:mod:`secrets` à
    la place.

Module ``random``
=================

Exemples
========

Avant toutes choses, il convient d'importer le module au projet :

.. code-block:: python3

    >>> import random

Nombres à virgules
------------------

La fonction basique :py:func:`random.random` retourne un chiffre à virgule dans
l'intervalle compris entre 0 et 1 non-compris :math:`[0.0; 1.0[` :

.. code-block:: python3

    >>> random.random()
    0.6982933392406706

Il est possible de spécifier un intervalle avec la fonction
:py:func:`uniform(a,b) <random.uniform()>` qui retourne un chiffre à virgule dans l'intervalle
compris entre *a* et *b* non-compris :math:`[a; b[` :

.. code-block:: python3

    >>> random.uniform(4.5, 7.5)
    5.292029100094782

Nombres entiers
---------------

Si l'on souhaite travailler avec des nombres entiers, il faut utiliser la
fonction :py:func:`random.randrange()`. Cette fonction retourne un nombre entier entre
0 et *a* non-compris [0; a[ :

.. code-block:: python3

    >>> random.randrange(15)
    8

Il est également possible de spécifier le commencement de l'intervalle avec
:py:func:`random.randrange()` ce qui correspond à l'intervalle [a; b[ et d'ajouter
un pas d'une certaine valeur avec :py:func:`random.randrange()` où *s* est le pas
dans l'intervalle :

.. code-block:: python3

    >>> random.randrange(10, 12)
    10

    >>> random.randrange(4, 8, 2) #Retourne un nombre paire
    6

Séquences
---------

La fonction :py:func:`random.choice()` retourne un élément de la séquence *seq* à
condition que celle-ci ne soit pas vide :

.. code-block:: python3

    >>> random.choice(['dede', 'toto', 'lulu'])
    'lulu'

    >>> random.choice([4, 7, 11, 18])
    18

Il existe aussi la fonction :py:func:`random.shuffle()` qui mélange les éléments
de la séquence *seq* :

.. code-block:: python3

    >>> names = ['dede', 'toto', 'lulu']
    >>> random.shuffle(names)
    >>> names
    ['lulu', 'toto', 'dede']

    >>> numbers = [4, 7, 11, 18]
    >>> random.shuffle(numbers)
    >>> numbers
    [4, 11, 18, 7]

La fonction :py:func:`random.sample()` permet de retourner une liste de *k*
éléments de la séquence *seq* aléatoirement :

.. code-block:: python3

    >>> random.sample(['dede', 'toto', 'lulu', 'momo', 'baba'], 3)
    ['momo', 'dede', 'baba']

    >>> random.sample([10, 20, 30, 40, 50, 60], 4)
    [10, 30, 60, 50]

Conclusion
==========

:py:mod:`random` permet bien plus d'utilisations que la simple attribution d'une
valeur dans un intervalle donné. Toutes ses fonctionnalités n'ont pu être
traitées ici (car certaines sont exotiques et/ou très spécifiques) et si vous
êtes désireux d'en connaitre encore un peu plus sur son sujet, visitez la
documentation officielle python3 de :py:mod:`random`.

.. [#email] <christophe.hirschi@he-arc.ch>

.. Bibliographie

.. _Mersenne Twister: https://fr.wikipedia.org/wiki/Mersenne_Twister
