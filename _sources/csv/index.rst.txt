.. _csv-tutorial:

=======
``csv``
=======

.. image:: ../_static/csv.png
    :align: right
    :alt: CSV logo

Par Axel Rieben [#email]_


Introduction
============

CSV est un format ouvert très populaire d'importation et d'exportation de données tel que des feuilles de calcul. Les données d'un fichier ``.csv`` sont sous forme textuelles séparées par des virgules d'où son nom *Comma Separeted Values*.

Exemple d'un fichier .csv [#wikipedia]_ :

.. code-block:: text

    "Robert;"Dupont";"rue du Verger, 12"
    "Michel";"Durand";" av. de la Ferme, 89"
    "Michel ""Michele""";"Durand";" av. de la Ferme, 89"
    "Michel;Michele";"Durand";"av. de la Ferme, 89"

Représentation tabulaire :

.. csv-table::

    "Robert","Dupont","rue du Verger, 12"
    "Michel","Durand","av. de la Ferme, 89"
    "Michel ""Michele""","Durand","av. de la Ferme, 89"
    "Michel;Michele","Durand","av. de la Ferme, 89"

Il existe des différences de format parmi les applications utilisant CSV puisqu'il n'a pas été standardisé. Les guillemets peuvent par exemple être omis et les points virgules remplacé par des virgules. Toutefois, la RFC 41802 [#rfc]_ décrit la forme la plus courante.

Exemples
========

Le module :py:mod:`csv` python implémente des classes permettant de facilement lire et écrire des fichiers au format CSV.

Lecture
*******

L'exemple ci-dessous illustre la lecture d'un fichier CSV nommé "data.csv". Dans un premier temps, le fichier est ouvert. Ensuite, on peut voir que la fonction :py:func:`~csv.reader` est utilisé afin d'obtenir un objet sur lequel il est possible d'itérer. Enfin, une boucle affiche chaque ligne du fichier.

.. literalinclude:: examples.py
    :start-after: func:read
    :end-before: endfunc:read

Il est possible de ne lire qu'une ou plusieurs colonnes en utilisant l'opérateur ``[]``.

.. car ``row`` est une séquence, rien d'exceptionnel à celà.

.. literalinclude:: examples.py
    :start-after: func:readcol
    :end-before: endfunc:readcol

Il est commun de spécifier des entêtes au dessus de chaque colonne, comme sur l'exemple de fichier CSV ci-dessous avec les entêtes FirstColumn et SecondColumn. [#stack]_

.. code-block:: text

    FirstColumn,SecondColumn
    asdf,1234
    qwer,5678

Pour les ignorer lors de la lecture, il suffit de passer la première ligne avec la fonction :py:func:`next()` :

.. à quoi sert None?

.. literalinclude:: examples.py
    :start-after: func:readskip
    :end-before: endfunc:readskip

Ou alors en utilisant un :py:class:`~csv.DictReader`, qui permettra de lire chaque colonne en spécifiant son entête plutôt que son index numérique :

.. literalinclude:: examples.py
    :start-after: func:readdict
    :end-before: endfunc:readdict

Il est à noter qu'il est recommandé d'utiliser des fichier CSV encodé en UTF-8 pour éviter tout bogue inopiné.

Écriture
********

L'exemple ci-dessous illustre l'écriture d'un fichier CSV nommé "write.csv". Comme pour la lecture, il faut tout d'abord ouvrir le fichier. Ensuite la fonction, :py:func:`~csv.writer` retourne un objet qui va convertir au format CSV les données qu'on lui donne. Il suffit donc de passer celles-ci à la fonction :py:meth:`~csv.csvwriter.writerow()`.

.. literalinclude:: examples.py
    :start-after: func:write
    :end-before: endfunc:write

Le résultat du code ci-dessus sera un fichier ``write.csv`` placé au même endroit que le script Python et contenant :

.. code-block:: text

    abc,def,ghi
    123,456,789

Suivant le système d'exploitation et l'éditeur de texte utilisé, il est possible de voir apparaître des lignes vides entre chaque ligne de données. Ceci est dû au fait que le délimiteur de fin de ligne par défaut utilisé par :py:func:`~csv.writer` est ``\r\n``.

Dialectes [#chicoree]_
**********************

Comme précisé dans l'introduction, CSV manque de standardisation. Les logiciels francophones auront tendance à utiliser des points virgules comme séparateur, et des guillemets comme caractère de délimitation de chaine. Ainsi, il n'y aura pas besoin d'échapper les caractères apostrophe et il n'y aura pas de confusion avec la virgule d'un chiffre ou d'une phrase. D'un autre côté, le standard défini par la RFC est l'utilisation de l'apostrophe et de la virgule. Pour complexifier le tout, chacun peut plus ou moins définir son propre format.

Pour pallier à ces différents de formatage :py:mod:`csv` à créer les dialectes. Un dialecte permet de spécifier chacun des paramètres du formatage. Ils peuvent être spécifié soit directement lors de l'utilisation des fonctions :py:func:`~csv.reader` et :py:func:`~csv.writer` :

.. literalinclude:: examples.py
    :start-after: func:readdialect
    :end-before: endfunc:readdialect

Soit en utilisant une classe qui redéfini tous les attributs :

.. literalinclude:: examples.py
    :start-after: func:readdialectclass
    :end-before: endfunc:readdialectclass

Voici un tableau qui renseigne sur chacun des attributs :

================  =================  ===============================================================================
Attribut          Valeur par défaut  Signification
================  =================  ===============================================================================
delimiter         ``,``              Séparateur de champ
quotechar         ``"``              Délimiteur pour les chaînes
quoting           ``QUOTE_MINIMAL``  Contrôle l'adjonction de guillemets autour des données
doublequote       ``True``           Doubler les quotechar qui se trouvent dans les données
escapechar        ``None``           Caractère d'échappement pour protéger les caractères spéciaux dans les données
lineterminator    ``\r\n``           Séquence de caractères utilisée à la fin de chaque enregistrement (la fonction :py:func:`~csv.reader` ignore cet attribut et est configuré pour détecter automatiquement \\n ou \\r comme séquence de fin de ligne)
skipinitialspace  ``False``          Ignorer les espaces entre le délimiteur de chaîne et les données
================  =================  ===============================================================================


Conclusion
==========

:py:mod:`csv` est un module très pratique lorsqu'il s'agit de stocker ou de rechercher des données dans un fichier. Il est aussi facile d'utilisation et ne nécessite que quelques lignes de code pour être opérationnel. Un point négatif cependant, est que le format manque de standardisation, ce qui peut être problématique pour le partage d'informations entre plusieurs applications. Il n'est non plus pas adapté aux stockages d'informations en masse ayant de fortes dépendances entre elles. Là, une base de données serait plus judicieuse. Enfin, pour terminer, beaucoup d'autre fonctionnalités du module n'ont pas pu être exposé dans cette courte page d'information. Il est donc recommandé de suivre les liens listés ci-dessous pour plus de détails.

Références
==========

.. [#email] <axel.rieben@he-arc.ch>
.. [#logo] https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Text-csv-text.svg/262px-Text-csv-text.svg.png
.. [#wikipedia] https://fr.wikipedia.org/wiki/Comma-separated_values
.. [#rfc] https://tools.ietf.org/html/rfc4180
.. [#doc] https://docs.python.org/3.6/library/csv.html#module-csv
.. [#stack] http://stackoverflow.com/questions/14257373/skip-the-headers-when-editing-a-csv-file-using-python
.. [#chicoree] http://www.chicoree.fr/w/Fichiers_CSV_en_Python
