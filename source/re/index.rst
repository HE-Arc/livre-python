.. _re-tutorial:

Expressions régulières (``re``)
===============================

Par Julien Feuillade [#jf]_

Introduction
------------

Les expressions régulières sont utilisées dans pratiquement tous les langages. C'est un puissant outil qui permet de vérifier si le contenu d'une variable a la forme de ce que l'on attend.
Ils permettent aussi de modifier ou de supprimer tous les éléments indésirables dans une variable.

Les bases de la syntaxe
-----------------------

Une des premières choses à réaliser dans la conception d'une expression régulière, c'est de définir le motif (pattern en anglais).

Pour construire ces motifs, vous avez besoin de créer une structure formée de caractères littéraux, puis de symboles qui sont définis en tant que méta caractères et délimiteurs et qui seront utilisés séparément ou en combinaison à l'intérieur d'un même groupement ou d'une classe.

On utilisera différents types de syntaxe comme :

::

    ^     Marque le début de la chaine, la ligne.
    $     Marque la fin d'une chaine, la ligne.
    .     N'importe quel caractère.
    *     0, 1 ou plusieurs occurrences.
    +     1 ou plusieurs occurrences.
    ?     0 ou 1 occurrence.
    |     Alternative - ou reconnaît l'un ou l'autre.
    [ ]   Tous les caractères énumérés dans la classe.
    [^ ]  Tous les caractères sauf ceux énumérés.
    ( )   Utilisée pour limiter la portée d'un masque ou de l'alternative.

Ainsi que de groupes de caractères :

::

    \w      Les lettres (w pour word).
    \d      Les chiffres (d pour digit).
    \s      Les espaces (s pour spaces).
    [A-Z]   Les majuscules.
    [abd;_] Les lettres a, b, et d, le point-virgule (;), et l’underscore (_).

Prenons un exemple :

::

    k|\d{2} : la lettre k, ou bien deux chiffres.
    BRA{,10} : on attend à ce que le segment BRA ne soit pas présent du tout ou présent jusqu'à 10 fois consécutives.

.. todo:: Pourquoi ne pas utiliser une liste de définition comme la documentation officielle?

La bibliothèque ``re``
----------------------

Afin de mettre les différentes expressions en place, la bibliothèque :py:mod:`re` nous est proposé avec ces différentes fonctions qui permettra essentiellement de rechercher / modifier / supprimer des expressions.

re.match()
----------

La fonction :py:func:`~re.match()` va permettre de vérifier la correspondance avec la chaîne de caractères.

::

    re.match(pattern, string)

- ``pattern`` est l'expression à faire correspondre.
- ``string`` est la chaîne d'origine.

.. code:: pycon

    >>> import re
    >>> re.match(r"B(.)?NJO(.)?R", "BONJOUR")
    <_sre.SRE_Match object; span=(0, 7), match='BONJOUR'>

re.search()
-----------

Afin de rechercher une expression, on utilisera la fonction :py:func:`~re.search()` :

::

    re.search(pattern, string)

- ``pattern`` est l'expression à rechercher.
- ``string`` est la chaîne d'origine.

.. code:: pycon

    >>> import re
    >>> line = "Cats are smarter than dogs";
    >>> searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
    >>> if searchObj:
    ...     print("searchObj.group() : ", searchObj.group())
    ...     print("searchObj.group(1) : ", searchObj.group(1))
    ...     print("searchObj.group(2) : ", searchObj.group(2))
    ... else:
    ...     print("Nothing found!!")
    ...
    searchObj.group() :  Cats are smarter than dogs
    searchObj.group(1) :  Cats
    searchObj.group(2) :  smarter

re.split()
----------

La fonction :py:func:`~re.split()` va permettre de découper une chaîne ``string`` selon un pattern.

::

    re.split(pattern, string, maxsplit)

- ``pattern`` est l'expression avec lequelle on séparera.
- ``string`` est la chaîne d'origine.
- ``maxsplit`` est le nombre de séparations faite au maximum.

.. code:: pycon

    >>> import re
    >>> line = 'Je Suis; Le, Gars,Qui,      Joue'

    >>> re.split(r'[;,\s]\s*', line)
    ['Je', 'Suis', 'Le', 'Gars', 'Qui', 'Joue']

    >>> re.split(r'[;,\s]\s*', line, maxsplit=1)
    ['Je', 'Suis; Le, Gars,Qui,      Joue']

re.sub()
--------

Afin de remplacer des données, on peut passer par la fonction :py:func:`~re.sub()` :

::

    re.sub(pattern, replace, string)

- ``pattern`` est l'expression à rechercher.
- ``replace`` est le remplacent de cette expression.
- ``string`` est la chaîne d'origine.

.. code:: pycon

    >>> import re
    >>> phone = "2004-959-559"
    >>> num = re.sub(r'#.*$', "", phone) # Suppresion des guillemets
    >>> print("Phone Num : ", num)
    Phone Num :  2004-959-559

    >>> num = re.sub(r'\D', "", phone) # Suppresion de tout sauf les digits
    >>> print( "Phone Num : ", num)
    Phone Num :  2004959559

.. sub peut recevoir une fonction comme second argument.

re.compile()
------------

Si, dans votre programme, vous utilisez plusieurs fois les mêmes expressions régulières, il peut être utile de les compiler. La bibliothèque :py:mod:`re` propose en effet de conserver votre expression régulière sous la forme d'un objet que vous pouvez stocker dans votre programme. On utilisera ainsi la fonction :py:func:`~re.compile()` :

.. pourquoi?

::

    re.compile(pattern)

- ``pattern`` est l'expression à compiler.

.. code:: pycon

    >>> import re
    >>> batRegex = re.compile(r'Bat(wo)?man')
    >>> mo1 = batRegex.search('The Adventures of Batman')
    >>> mo1.group()
    'Batman'

    >>> mo2 = batRegex.search('The Adventures of Batwoman')
    >>> mo2.group()
    'Batwoman'

Conclusion
----------

Avec cette documentation vous pouvez avoir une bonne idée de ce qu'est une expression régulière, de comment la construire et de comment l'utiliser. Ne nous leurrons cependant pas, l'apprentissage n'est pas aussi facile, il faut les apprivoiser, « jouer » avec elles, mais le jeu en vaut la chandelle.

.. [#jf] <julien.feuillade@he-arc.ch>

.. Bibliographie (ceci est un commentaire)

.. https://www.tutorialspoint.com/python/python_reg_expressions.htm
.. http://apprendre-python.com/page-expressions-regulieres-regular-python
.. https://regexone.com/references/python
.. http://www.python-course.eu/re_advanced.php
.. https://www.analyticsvidhya.com/blog/2015/06/regular-expression-python/
