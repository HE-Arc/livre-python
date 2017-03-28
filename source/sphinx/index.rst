.. _sphinx-tutorial:

==========
``Sphinx``
==========

Introduction
------------

`Sphinx <http://www.sphinx-doc.org/>`_ est un générateur de documentation python libre (Licence `BSD <https://en.wikipedia.org/wiki/BSD_licenses>`_).
Sphinx se charge de convertir un ensemble de sources `reSt <http://docutils.sourceforge.net/rst.html>`_ vers différents formats (LateX, PDF, Epub), en produisant les indices et références internes automatiquement.
Il est également capable de générer une version html de la documentation pour une consultation directe et facile.
On peut noter que sphinx se concentre sur une documentation écrite "à la main", plutôt que sur une documentation auto-générée.
On peut donc considérer grossièrement Sphinx comme un programme qui prends des fichiers reST et les convertit en html.

Pré-réquis 
----------
Python 2.7 ou Python 3.4 est impératif au fonctionnement de Sphinx.
La librairie `Pygments <http://pygments.org>`_  peut-être installée si une colorisation syntaxique est nécessaire.


Installation et rapide mise en pratique
---------------------------------------

L'installation de sphinx se fait avec PyPI::

	pip install Sphinx
	
Ensuite, il peut être intéressant d'appeler la commande sphinx-quickstart pour générer automatiquement l'arborescence utilisée par Sphinx, ainsi
que les fichiers conf.py et index.rst (configuration par défaut de sphinx-quickstart).

Structure des fichiers
----------------------

Le fichier index.rst placé à l'origine du dossier source, appelé *master document*, agit principalement comme une page d'accueil et contient la table des matières.
Le toctree (*table of contents tree*) est une fonctionnalité ajoutée à reSt par Sphinx et permet de connecter plusieurs fichiers à l'intérieur d'un document::
	
	.. toctree::
	:maxdepth: 1

	bar.rst
	foo.rst
	sphinx/index.rst
	...

Il est également possible de changer le titre à afficher en haut de page au lieu du nom de fichier grâce à la notation suivante::
	
	..toctree::
	:maxdepth: 1

	A mindblowing theory about narwhals <heapq/whichsurpriseyouforsure.rst>

On peut aussi choisir d'utiliser une liste ordonnée::
	
	..toctree::
	:numbered: 

Documentation d'un objet
------------------------

La syntaxe pour documenter une fonction est la suivante::

    .. py:function:: enumerate(sequence[, start=0])

       Return an iterator that yields tuples of an index and an item of the
       *sequence*. (And so on.)
   
Le résultat : 

.. py:function:: enumerate(sequence[, start=0])

   Return an iterator that yields tuples of an index and an item of the
   *sequence*. (And so on.)
  

Après une fonction documentée, il est possible de créer une référence vers cette dernière::

    The :py:func:`enumerate` function can be used for ...

Le résultat : 

The :py:func:`enumerate` function can be used for ...

Un référencement systématique me semble être une bonne pratique. La navigation est plus fluide et on évite ainsi des ctrl-f inutiles :)  
