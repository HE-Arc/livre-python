.. _csv-tutorial:

======================
         CSV
======================

.. image:: ../_static/csv.png
	:align: right
	:alt: CSV logo

Par Axel Rieben [#email]_

Introduction
============

CSV est un format ouvert très populaire d'importation et d'exporation de données tel que des feuilles de calcul. Les données d'un fichier .csv sont sous forme textuelles séparées par des virgules d'où son nom "Comma Separeted Values".

Exemple d'un fichier .csv [#wikipedia]_ :

.. code-block:: text

	"Robert;"Dupont";"rue du Verger, 12"
	"Michel";"Durand";" av. de la Ferme, 89"
	"Michel ""Michele""";"Durand";" av. de la Ferme, 89"
	"Michel;Michele";"Durand";"av. de la Ferme, 89"

Représentation tabulaire :

.. csv-table::
	:widths: 15, 10, 30

  "Robert","Dupont","rue du Verger, 12"
	"Michel","Durand","av. de la Ferme, 89"
	"Michel ""Michele""","Durand","av. de la Ferme, 89"
	"Michel;Michele","Durand","av. de la Ferme, 89"

Il existe des différences de format parmis les applications utilisant CSV puisqu'il n'a pas été standardisé. Les guillemet peuvent par exemple être omis et les points virgules remplacé par des virgules. Toutefois, la RFC 41802 [#rfc]_ décrit la forme la plus courante.

Module [#doc]_
==============

Le module :py:mod:`csv` python implémente des classes permettant de facilement lire et écrire des fichiers au format CSV. Pour tout les exemples qui suivent il ne faudra pas oublié d'importer ce module avec :

.. literalinclude:: examples.py
       :start-after: func:import
       :end-before: endfunc:import

Lecture
*******

L'exemple ci-dessous illustre la lecture d'un fichier CSV nommé "data.csv". Dans un premier temps, le fichier est ouvert en mode lecture de texte 'rt'. Ensuite, on peut voir que la fonction :py:func:`~csv.reader` est utiliser afin d'obtenir un objet sur lequel il est possible d'itérer. Enfin, une boucle affiche chaque ligne du fichier.

.. literalinclude:: examples.py
	:start-after: func:read
	:end-before: endfunc:read

Il est possible de ne lire qu'une plusieurs colonnes en utilisant l'opérateur [].

.. literalinclude:: examples.py
      :start-after: func:readcol
              :end-before: endfunc:readcol

Il est à noté qu'il est recommandé d'utiliser des fichier CSV encodé en UTF-8 pour éviter tout bug inopiné.

Ecriture
********

L'exemple ci-dessous illustre l'écriture d'un fichier CSV nommé "write.csv"

.. literalinclude:: examples.py
	:start-after: func:write
	:end-before: endfunc:write

Dialectes
*********



Références
==========

.. [#email] <axel.rieben@he-arc.ch>
.. [#logo] https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Text-csv-text.svg/262px-Text-csv-text.svg.png
.. [#wikipedia] https://fr.wikipedia.org/wiki/Comma-separated_values
.. [#rfc] https://tools.ietf.org/html/rfc4180
.. [#doc] https://docs.python.org/3.6/library/csv.html#module-csv
.. [#chicoree] http://www.chicoree.fr/w/Fichiers_CSV_en_Python
