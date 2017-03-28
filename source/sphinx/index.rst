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

Autodoc
-------

Sphinx permet de générer la doc d'un module python ainsi que celle des classes le composant à partir des docstrings - *valides* - contenus dans sa source.
La façon la plus simple est d'inclure l'extension sphinx.ext.autodoc lors de l'utilisation de sphinx-quickstart (desactivé par défaut)::
	
    ..
    Please indicate if you want to use one of the following Sphinx extensions:
    > autodoc: automatically insert docstrings from modules (y/n) [n]: y
    ..

Ensuite, si le module n'est pas inclus dans les variables d'environnement de python, il est possible de rajouter son chemin dans le fichier conf.py.
Les 3 lignes suivantes sont présentes par défaut dans ce dernier::

    # import os
    # import sys
    # sys.path.insert(0, os.path.abspath('.'))

Il est donc possible de les décommenter, le chemin étant évidemment à adapter (L'option de mettre un chemin en dur comme en sale étant évidemment disponible à mon grand bonheur)::

    import os
    import sys
    sys.path.insert(0,"C:\\Users\\Guillaume\\Desktop\\FlappyBird\\flappy")

Finalement, la documentation se fait en invoquant::

    Contents:
 
    .. toctree::
       :maxdepth: 2
 
    .. automodule:: Flappy
 
    .. autoclass:: Bird
        :members:
    
    .. autoclass:: Pipe
        :members:

Ainsi, lors de la compilation avec sphinx-build, Sphinx extraira les docstrings des classes concernées, générant ainsi une doc automatique.
Nous nous retrouvons donc avec une chatoyante doc : 

.. image:: img/flappydoc.png
   :alt: a fine doc
   :align: center

Néanmoins, cette méthode comporte un soucis évident : on doit quand même inclure tous les modules et classes manuellement, et ça c'est tout pourri.
Heureusement, un utilisateur a créé un script remédiant à ce soucis : il s'agit d'apidoc. 

APIDoc
------

APIDoc est un outil venant avec sphinx. Sa fonction est d'extraire la documentation d'un projet entier, générant ainsi les fichiers \*.rst pour chaque module.
apidoc peut-être invoqué ainsi::

    sphinx-apidoc [options] -o <destination> <source> [chemins ...]

Des informations suplémentaires sur son utilisation peuvent être trouvées `à cette adresse <http://sphinx.pocoo.org/man/sphinx-apidoc.html>`_. 

Syntaxe spécifique à Sphinx
---------------------------

*todo*

Domaines
--------

*todo*

Le fichier de configuration
---------------------------

*todo*

Les thèmes
----------

*todo*

Configuration pour LaTeX
------------------------

*todo*

Conclusion
----------

*todo*


