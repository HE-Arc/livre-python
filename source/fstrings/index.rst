.. _fstrings-tutorial:

=========
f-strings
=========

Par Thibaut Piquerez [#tp]_

------------
Introduction
------------

Depuis Python 3.6, f-strings (:pep:`498`) permet d'insérer des expressions dans des chaines de caractères en utilisant une syntaxe minimale. Ces expressions servent à insérer des variables dans les chaines de caractères et de les mettre en forme.

--------------
Fonctionnement
--------------

Pour utiliser f-strings il suffit de mettre un f devant la chaine de caractères et pour insérer la valeur d'une variable dans la chaine il suffit de mettre la variable entre accolade. Si il n'y a pas de variable a substituer il n'est pas nécessaire de mettre le ``f`` devant.

.. code-block:: pycon

    >>> name = 'Paul'
    >>> age = 23

    >>> print(f'Votre nom est un {name} et vous avez {age} ans')
    Votre nom est un Paul et vous avez 23 ans

f-strings prend également en compte les fonctions ce qui signigfie que les fonctions qui se trouvent dans la chaine de caractères sont exécutées et le résultat est affiché.

-----------
Échappement
-----------
Certains cractères ne peuvent pas être afficher tel quel il est nécessaire de les échapper.

Pour les accolade ``{}`` il faut en mettre deux à la suite :

.. code-block:: pycon

    >>> nombre = 34
    >>> print(f'Le nombre est {{{nombre}}}')

    Le nombre est {34}

Pour afficher des apostrophes, il y a trois solutions:

    Mettre la chaine entre guillemets :

    .. code-block:: pycon

        >>> print("ma chaine de caractères avec des 'apostrophes' ")

        ma chaine de caractères avec des 'apostrophes'

    Mettre la chaine entre 3 apostrophes :

    .. code-block:: pycon

        >>> print('''ma chaine de caractères avec des 'apostrophes' ''')

        ma chaine de caractères avec des 'apostrophes'

    Mettre des backslash avant les apostrophes :

    .. code-block:: pycon

        >>> print('ma chaine de caractères avec une \'apostrophe ')

        ma chaine de caractères avec des 'apostrophes

-------------
Raw f-strings
-------------

Un string convertit automatiquement les échappements avec des backslashs comme par exemple : ``\n`` , ``\"``, ``\t``, etc. Donc si on ne veut pas que python interprète ces échappements il faut utiliser les raw string en ecrivant ``r`` avant la chaine de caractères et si on veut utiliser des raw f-strings il faut mettre ``fr``.

.. code-block:: pycon

    >>> print('ma \n phrase')
    ma
     phrase

    >>> print(r'ma \n phrase')
    ma \n phrase

---------------------
Options de formattage
---------------------

f-strings implémente également une manière de mettre en forme les nombres.

Voici la syntaxe pour utiliser le formattage (voir :ref:`formatspec`):

.. code-block:: pycon

    f ' <texte> { <expression/variable> : <format> } <texte> ... '

Le format se trouve sous cette forme pour les nombres à virgule::

    [alignement][signe][largeur][groupage][.précision][type]

- alignement : détermine ou le nombre est aligné dans sa zone
    - '>'    aligne à droite
    - '<'    aligne à gauche
    - '^'    centré
    - '='    aligne le signe à gauche et le nombre à droite
- signe    : détermine l'affichage du signe
    - '+'     indique que le signe + doit être affiché ainsi que le -
    - '-'   indique que le signe - doit être affiché (par defaut)
    - ' '      n'affiche pas le + mais insére un espace à la place
- largeur : détermine la place qui doit être réservée pour l'affichage du nombre
- groupage : détermine le symbole de séparation tous les 3 chiffres
    - '_'
    - ','
- précision : détermine le nombre de chiffres après la virgule
- type : détermine le mode d'affichage
    - 'e' ou 'E'     notation scientifique
    - 'f' ou 'F'    affichage classique

Exemple :

.. code-block:: pycon

    >>> nombre = 357568.12312
    >>> nombre2 = 568.568768
    >>> nombre3 = -34.3432
    >>> nombre4 = 23
    >>> print(f'{nombre : >+20_.4f} {nombre2 : >+20_.4f}')
    >>> print(f'{nombre3 : >+20_.4f} {nombre4 : >+20_.4f}')

    +357_568.1231            +568.5688
         -34.3432             +23.0000

.. ce code mériterait d'utiliser une boucle.

C'est très pratique pour faire des tableaux de nombre.

Il existe aussi des option de formattage pour les entiers il suffit simplement de mettre une lettre pour le format:

- 'b'            : affiche en binaire
- 'c'             : affiche le caractère correspondant au code unicode
- 'd'            : affiche en decimal (par defaut)
- 'o'            : affiche en octal
- 'x' ou 'X'    : affiche en hexa

Exemple :

.. code-block:: pycon

    >>> chmod = 0o644
    >>> f'{chmod:016b}'
    '0000110100100'

.. un peu maigre comme exemple.

----------
Conclusion
----------

Avantage de f-strings:

- variable introduit directement dans les chaines de caractères
- concaténation des chaines de caractères sans '+'
- formattage simplifié des nombres
- alignement du texte simplifié
- temps d'execution plus court

f-strings est un complément très utile aux string classiques en simplifiant la manière d'utiliser des chaines de caractères. Le code à taper est plus simple et également plus court et qui dit moins de code dit moins d'erreurs.

.. [#tp] <thibaut.piquerez@he-arc.ch>
