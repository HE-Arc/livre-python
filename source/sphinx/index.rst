Sphinx
======

Par Guillaume Noguera [#gn]_

Introduction
------------

:py:mod:`sphinx` `(site officiel) <http://www.sphinx-doc.org/>`_ est un générateur de documentation python libre (Licence `BSD <https://en.wikipedia.org/wiki/BSD_licenses>`_).
Sphinx se charge de convertir un ensemble de sources `reSt <http://docutils.sourceforge.net/rst.html>`_ vers différents formats (LaTeX, PDF, Epub), en produisant les indices et références internes automatiquement.
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


    ..py:function::whatShouldIEat(hangoverLevel, politicalViews[])

       Ignores parameters and returns humus.

    .. py:function:: enumerate(sequence[, start=0])

       Return an iterator that yields tuples of an index and an item of the
       *sequence*. (And so on.)
   
Le résultat : 

.. py:function:: whatShouldIEat(hangoverLevel, politicalViews[])

   Ignores parameters and always returns humus.

.. py:function:: enumerate(sequence[, start=0])

   Return an iterator that yields tuples of an index and an item of the
   *sequence*. (And so on.)
  
Après une fonction documentée, il est possible de créer une référence vers cette dernière::

    La fonction :py:func:`enumerate` peut être utilisée pour ...

Le résultat : 

La fonction :py:func:`enumerate` peut être utilisée pour ...

Il est à noter que la recherche générée par sphinx renvoie également aux définitions de fonctions. 
Un référencement systématique me semble être une bonne pratique. La navigation est plus fluide et on évite ainsi des ctrl-f inutiles :)

.. highlight:: none

>>>>>>>>>>>>>>>>>>>


Autodoc
-------

Sphinx permet de générer la doc d'un module python ainsi que celle des classes le composant à partir des docstrings - *valides* - contenus dans sa source.
La façon la plus simple est d'inclure l'extension sphinx.ext.autodoc lors de l'utilisation de sphinx-quickstart (desactivé par défaut)::
	
    ..
    Please indicate if you want to use one of the following Sphinx extensions:
    > autodoc: automatically insert docstrings from modules (y/n) [n]: y
    ..

Sinon, on peut intégrer l'extension dans le fichier conf.py::

    extensions = ['sphinx.ext.autodoc']

Ensuite, si le module n'est pas inclus dans les variables d'environnement de python, il est possible de rajouter son chemin dans le fichier conf.py.
Les 3 lignes suivantes sont présentes par défaut dans ce dernier::

    # import os
    # import sys
    # sys.path.insert(0, os.path.abspath('.'))

.. highlight:: python

Il est donc possible de les décommenter, le chemin étant évidemment à adapter (L'option de mettre un chemin en dur comme en sale étant évidemment disponible à votre désarroi et pour mon grand bonheur)::

    import os
    import sys
    sys.path.insert(0,"C:\\Users\\Guillaume\\Desktop\\FlappyBird\\flappy")

.. highlight:: rest

Finalement, la documentation se fait en ajoutant les modules, classes et fonctions désirées dans notre fichier reST::

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

.. highlight:: none

Néanmoins, cette méthode comporte un soucis évident : on doit quand même inclure tous les modules et classes manuellement, et ça c'est tout pourri.
Heureusement, un utilisateur a créé un script remédiant à ce soucis : il s'agit d'apidoc. 

APIDoc
~~~~~~

APIDoc est un outil venant avec sphinx. Sa fonction est d'extraire la documentation d'un projet entier, générant ainsi les fichiers \*.rst pour chaque module.
apidoc peut-être invoqué ainsi::

    sphinx-apidoc [options] -o <destination> <source> [chemins ...]

Des informations suplémentaires sur son utilisation peuvent être trouvées `à cette adresse <http://sphinx.pocoo.org/man/sphinx-apidoc.html>`_. 


>>>>>>>>>>>>>>>>>>>


Domaines
--------

.. highlight:: rest

Au départ, sphinx a été conçu comme un outil dédié au language python. Après quelques temps, l'intéret grandissant pour cet outil a poussé le développement de sphinx vers un support multi-language. Il est donc possible aujourd'hui de documenter des projets C, C++ ou Javascript avec sphinx. 

On peut remarquer que dans la définition de la fonction :py:func:`enumerate`, on utilise la notation **.. py:** function: . Ce même préfixe .. py: corresponds justement à un domaine sphinx.
Ces domaines sont en fait une collection de directives reST qui évitent les conflits de noms si le document redigé corresponds à un projet utilisant une multitude de languages, par exemple. 

Ainsi, le domaine C est representé par la notation **.. c:**, son équivalent C++ est **.. cpp:**. Javascript se verra malicieusement attribué le tag **.. js:**.

Quelques exemples (`source <http://www.sphinx-doc.org/en/stable/domains.html>`_)::

    .. c:function:: PyObject* PyType_GenericAlloc(PyTypeObject *type, Py_ssize_t nitems)
    .. c:member:: PyObject* PyTypeObject.tp_bases
    .. js:function:: $.getJSON(href, callback[, errback])

       :param string href: An URI to the location of the resource.
       :param callback: Gets called with the object.
       :param errback:
           Gets called in case the request fails. And a lot of other
           text so we need multiple lines.
       :throws SomeError: For whatever reason in that case.
       :returns: Something.

> > > 

.. c:function:: PyObject* PyType_GenericAlloc(PyTypeObject *type, Py_ssize_t nitems)
.. c:member:: PyObject* PyTypeObject.tp_bases
.. js:function:: $.getJSON(href, callback[, errback])

   :param string href: An URI to the location of the resource.
   :param callback: Gets called with the object.
   :param errback:
       Gets called in case the request fails. And a lot of other
       text so we need multiple lines.
   :throws SomeError: For whatever reason in that case.
   :returns: Something.

(On appréciera la traduction baguette automatique de sphinx \\[T]/ )

à noter que les extensions :function::, :member::, etc. sont liées au language qu'elles couvrent. 
Ainsi, pour le C++, nous avons accès à ::

   .. cpp:class::
   .. cpp:member::
   .. cpp:function::
   .. cpp:enum::
   .. cpp:var::
   .. cpp:type::

La liste est longue et le mieux est de vous inviter à consuler la `page de référence <http://www.sphinx-doc.org/en/stable/domains.html>`_ prévue à cet effet. 

.. highlight:: none

>>>>>>>>>>>>>>>>>>>


Les thèmes
----------

.. highlight:: python

Comme pour un content manager tel que Wordpress ou Drupal, Sphinx utilise un système de thème pour déterminer l'aspect visuel du build (html uniquement).

Sphinx vient avec quelques thèmes pré-intallés : classic (semblable à la doc officielle python), alabaster (le thème actuellement utilisé pour ce livre python), sphinxdoc (thème utilisé pour le site officiel de sphinx) ... la liste exhaustive est `disponible ici <http://www.sphinx-doc.org/en/stable/theming.html#builtin-themes>`_ .
Si l'on désire utiliser un des thèmes pre-installés, il suffit de modifier la ligne suivante dans le fichier conf.py::

    html_theme = "classic"
    html_theme_options = {
        "rightsidebar": "true",
        "relbarbgcolor": "black"
    }  

.. highlight:: none

(On peut remarquer que des options sont disponibles, afficher ou non la barre latérale par exemple. Les options sont liées au thème utilisé)

La manipulation est sensiblement la même pour un thème tiers, en admettant que l'on ait inclus le thème concerné dans un repértoire accessible par sphinx et indiquer son chemin ("html_theme_path = ["."]") dans conf.py. Les thèmes tiers statiques peuvent venir sous deux formes différentes : un dossier composé de sous-fichiers et d'un fichier theme.py, ou un dossier compressé (.zip). La forme que prennent ces derniers ne change néanmoins pas la démarche pour les activer.


>>>>>>>>>>>>>>>>>>>


Conclusion
----------

J'aurais pû couvrir bien des notions sur Sphinx et ai essayé d'en couvrir l'essentiel. Il s'agit d'un outil utile qui fera gagner un temps considérable: Après un build html, on peut simplement déposer la documentation sur un serveur. De plus, il est adapté pour un travail en équipe grâce à son aspect "modulaire" (plusieurs indexes séparés, un par librairie dans le cas de notre travail sur ce livre python). Enfin, sa capacité à produire de multiples formats de fichiers à partir du markup reST 

J'encourage donc mes éventuels lecteurs à s'y intéresser, quand bien même il faudra se débattre un peu avec son fonctionnement de prime abord. Le retour sur investissement peut valoir le coup. 

.. image:: img/o.png
   :alt: sphinx
   :align: center

.. [#gn] <guillaume.noguera@he-arc.ch> ou <guillaume.noguera@gmail.com> pour les trucs moins corpo

Après une fonction documentée, il est possible de créer une référence vers cette dernière::

    The :py:func:`enumerate` function can be used for ...

Le résultat : 

The :py:func:`enumerate` function can be used for ...

Il est à noter que la recherche générée par sphinx renvoie également aux définitions de fonctions. 
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
~~~~~~

APIDoc est un outil venant avec sphinx. Sa fonction est d'extraire la documentation d'un projet entier, générant ainsi les fichiers \*.rst pour chaque module.
apidoc peut-être invoqué ainsi::

    sphinx-apidoc [options] -o <destination> <source> [chemins ...]

Des informations suplémentaires sur son utilisation peuvent être trouvées `à cette adresse <http://sphinx.pocoo.org/man/sphinx-apidoc.html>`_. 

Le fichier de configuration
---------------------------

Le fichier conf.py, présent à la racine de notre dossier, permet de paramétrer un grand nombre de paramètres.

Configuration générale
~~~~~~~~~~~~~~~~~~~~~~

**extensions** ::
    
    import sys, os
    sys.path.append(os.path.abspath('sphinxext'))
    extensions = {'extensionname', '..'}

utilisé pour indiquer à sphinx quels extensions (autodoc, par exemple) utiliser. A noter que comme pour les modules à documenter avec autodoc, il faudra ajouter les extensions au sys.path si ces dernières ne y sont pas déjà.

**source_suffix**

Définit l'extension à utiliser; sphinx ne prendra pas en compte les fichiers ne comportant pas cette extension. 
Par défaut, le suffixe utilisé est ".rst".

**master_doc**

Indique le nom du master toctree.

**exclude_patterns** 

Un .gitignore, mais pour les sphinxes

Information sur le projet
~~~~~~~~~~~~~~~~~~~~~~~~~

**project, copyright, author, version, release** 

Les informations sur le projet, plutôt éloquent

**language**

Utilisé par sphinx pour la traduction automatique de certain termes

Options pour la sortie html
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**html_theme, html_theme_options**

Comme expliqué dans la section thème, on indique ici le thème à utiliser. 
On peut également donner une séquence d'éléments à html_theme_options afin d'ajuster le thème aux besoins.

**html_static_path** 

On peut indiquer ici un répértoire statique dont les fichiers doivent passer en priorité sur les builtins (par ex, les stylesheets)

>>>>>>>>>>>>>>>>

La quantité de paramètres à disposition dans le fichier conf.py est grande et il serait difficile de tout citer sans exploser la limite des 7 pages de cette documentation. Il existe notamment des paramètres propres à tous les formats d'exportation : ePub, LaTeX, pdf .. Tous sont spécifiques et peuvent être retrouvés à cette `adresse <http://www.sphinx-doc.org/en/stable/config.html>`_.

Domaines
--------

Au départ, sphinx a été conçu comme un outil dédié au language python. Après quelques temps, l'intéret grandissant pour cet outil a poussé le développement de sphinx vers un support multi-language. Il est donc possible aujourd'hui de documenter des projets C, C++ ou Javascript avec sphinx. 

On peut remarquer que dans la définition de la fonction :py:func:`enumerate`, on utilise la notation **.. py:** function: . Ce même préfixe .. py: corresponds justement à un domaine sphinx.
Ces domaines sont en fait une collection de directives reST qui évitent les conflits de noms si le document redigé corresponds à un projet utilisant une multitude de languages, par exemple. 

Ainsi, le domaine C est representé par la notation **.. c:**, son équivalent C++ est **.. cpp:**. 

Quelques exemples::

    .. c:function:: PyObject* PyType_GenericAlloc(PyTypeObject *type, Py_ssize_t nitems)
    .. c:member:: PyObject* PyTypeObject.tp_bases
    .. js:function:: $.getJSON(href, callback[, errback])

       :param string href: An URI to the location of the resource.
       :param callback: Gets called with the object.
       :param errback:
           Gets called in case the request fails. And a lot of other
           text so we need multiple lines.
       :throws SomeError: For whatever reason in that case.
       :returns: Something.

> > > 

.. c:function:: PyObject* PyType_GenericAlloc(PyTypeObject *type, Py_ssize_t nitems)
.. c:member:: PyObject* PyTypeObject.tp_bases
.. js:function:: $.getJSON(href, callback[, errback])

   :param string href: An URI to the location of the resource.
   :param callback: Gets called with the object.
   :param errback:
       Gets called in case the request fails. And a lot of other
       text so we need multiple lines.
   :throws SomeError: For whatever reason in that case.
   :returns: Something.

(On appréciera la traduction baguette automatique de sphinx \\[T]/ )

à noter que les extensions :function::, :member::, etc. sont liées au language qu'elles couvrent. 
Ainsi, pour le C++, nous avons accès à ::

   .. cpp:class::
   .. cpp:member::
   .. cpp:function::
   .. cpp:enum::
   .. cpp:var::
   .. cpp:type::

La liste est longue et le mieux est de vous inviter à consuler la `page de référence <http://www.sphinx-doc.org/en/stable/domains.html>`_ prévue à cet effet. 

Les thèmes
----------

Comme pour un content manager tel que Wordpress ou Drupal, Sphinx utilise un système de thème pour déterminer l'aspect visuel du build (html uniquement).

Sphinx vient avec quelques thèmes pré-intallés : classic (semblable à la doc officielle python), alabaster (le thème actuellement utilisé pour ce livre python), sphinxdoc (thème utilisé pour le site officiel de sphinx) ... la liste exhaustive est `disponible ici <http://www.sphinx-doc.org/en/stable/theming.html#builtin-themes>`_ .
Si l'on désire utiliser un des thèmes pre-installés, il suffit de modifier la ligne suivante dans le fichier conf.py::

    html_theme = "classic"
    html_theme_options = {
        "rightsidebar": "true",
        "relbarbgcolor": "black"
    }  

(On peut remarquer que des options sont disponibles, afficher ou non la barre latérale par exemple. Les options sont liées au thème utilisé)

La manipulation est sensiblement la même pour un thème tiers, en admettant que l'on ait inclus le thème concerné dans un repértoire accessible par sphinx et indiquer son chemin ("html_theme_path = ["."]") dans conf.py. Les thèmes tiers statiques peuvent venir sous deux formes différentes : un dossier composé de sous-fichiers et d'un fichier theme.py, ou un dossier compressé (.zip). La forme que prennent ces derniers ne change néanmoins pas la démarche pour les activer.


Conclusion
----------

J'aurais pû couvrir bien des notions sur Sphinx et ai essayé d'en couvrir l'essentiel. Il s'agit d'un outil utile qui fera gagner un temps considérable: Après un build html, on peut simplement déposer la documentation sur un serveur. De plus, il est adapté pour un travail en équipe grâce à son aspect "modulaire" (plusieurs indexes séparés, un par librairie dans le cas de notre travail sur ce livre python). Enfin, sa capacité à produire de multiples formats de fichiers à partir du markup reST 

J'encourage donc mes éventuels lecteurs à s'y intéresser, quand bien même il faudra se débattre un peu avec son fonctionnement de prime abord. Le retour sur investissement peut valoir le coup. 

.. image:: img/o.png
   :alt: sphinx
   :align: center

.. [#gn] <guillaume.noguera@he-arc.ch> ou <guillaume.noguera@gmail.com> pour les trucs moins corpo

