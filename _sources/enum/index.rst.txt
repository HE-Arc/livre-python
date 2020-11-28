.. _enum-tutorial:

``enum``
========

Par Axel Bento da Silva [#abds]_

Introduction
------------


Définition
^^^^^^^^^^

L'enumération est un liste de noms symboliques lié à des valeurs constantes, on peu donc avec l'enumération remplacé des valeurs entières peu parlantes par des nom plus logiques.

Le principale attrait de l'enumération est donc d'écrire du code plus lisible et humain.

En python le 'enum.py' est un module qui contient 4 classes d'enumération différentes : Enum, IntEnum, Flag, intFlag, il contient en plus quelques fonctionnalités supplémentaires tel que le auto ou le unique
que nous allons voir.

Utilisation
-----------

Il faut faire attention à ce pourquoi on l'utilise, une enumération n'est nécessaire que pour représenté un objet très simple ou l'état d'un objet plus complexe.


Un mauvais exemple
^^^^^^^^^^^^^^^^^^

Un mauvais exmple d'utilisation est par exemple celui de créer un py:mod:`enum` pour représenter des animaux :

.. code-block:: python

    from enum import Enum

    class Animal(Enum):
        Dog = 0
        Cat = 1
        Bird = 2



Un animal est un objet bien trop complexe qui se définit par plein d'attributs (son nom, son poids, sa taille, etc...), il est donc bien plus censé de créer une classe animal à part,
qui pourra d'ailleurs implémenter des méthodes telle que manger(), dormir(), etc... et dans ce cas on pourrais envisager d'ajouter un attribut
enumérer pour définir l'espèces.

Un bon exemple
^^^^^^^^^^^^^^

Un bon exemple d'utilisation est celui du feu vert, on peu représenté l'état d'un feu rouge par une simple variable entière qui varie de 0 à 2, mais cela nécéssite qu'on garde
en tête quel chiffre correpond à quoi, etc...
Il suffit donc de remplacer cette variable entirère par une enumération de ce type :

.. code-block:: pycon

    >>> class StateLight(Enum):
            RED = 0
            ORANGE = 1
            GREEN = 2

Dans cette exemple ci-dessus, bien que les états soit plus parlant, le fait d'utiliser des valeurs numériques peu poser des problèmes dans la suite du programme, par exemple si
le feu est actuellement à l'état ORANGE, et que nous voulons afficher la valeur de ce feu c'est la valeur 1 qui apparaîtra :

.. code-block:: pycon

    >>>light = StateLight['ORANGE']
    >>>light.name
    'ORANGE'
    >>>light.value
    1

Pour contrer ce problème il suffit de remplacer les valeurs numériques par des string plus parlant :

.. code-block:: pycon

    >>> class StateLight(Enum)
            RED = "Rouge"
            ORANGE = "Orange"
            GREEN = "Vert"

    >>>light = StateLight['RED']
    >>>light.name
    'RED'
    >>>light.value
    'rouge'

Exemple concret
^^^^^^^^^^^^^^^

Comme exemple concret nous avons de nombreux librairies de différents language qui propose une enumération de couleurs de base (Color.Red, Color.Blue, etc...).
Donc plutôt que de devoir connaître tous les codes hexadécimaux des couleurs, le programmeur peu utilier leurs noms :

:ref:`color-named_colors`

Attribut du module
------------------

Auto
^^^^

Auto renvoie des valeurs automatiques pour les enums, par defaut dans un Enum classique Auto renvoie la position
de son élément dans l'enumération :

.. code-block:: pycon

    >>> from enum import Enum, auto
    >>> class Number(Enum):
    ...     ONE = auto()
    ...     TWO = auto()
    ...     THREE = auto()

    >>> Number.ONE
    <Number.ONE: 1>
    >>> Number.TWO
    <Number.TWO: 2>
    >>> Number.THREE
    <Number.THREE: 3>

La fonction utilisé par auto() est _generate_next_value_(), qui peut être re-écrite pour par exemple renvoyer le nom de l'élément comme ceci :

.. code-block:: pycon

    >>> class AutoName(Enum):
    ...     def _generate_next_value_(name, start, count, last_values):
    ...         return name

    >>> class CarBrand(AutoName):
    ...     AUDI = auto()
    ...     TOYOTA = auto()
    ...     OPEL = auto()
    ...     BMW = auto()

    >>> list(CarBrand)
    [<CarBrand.AUDI: 'AUDI'>, <CarBrand.TOYOTA: 'TOYOTA'>, <CarBrand.OPEL: 'OPEL'>, <CarBrand.BMW: 'BMW'>]

Unique()
^^^^^^^^

Unique va renvoyer une erreur si deux éléments d'une enumération ont la même valeur.

.. code-block:: pycon

    >>> from enum import Enum, unique
    >>> @unique
    class Mistake(Enum):
        ONE = 1
        TWO = 2
        THREE = 2

Retournera une erreur !


Enum
^^^^

:py:class:`~enum.Enum` est la classe de base pour la création d'enumération. On peu définir ces enumérations de différentes façon.

.. code-block:: pycon

    >>> from enum import Enum
    >>> class StateLight(Enum):
            RED = 1
            ORANGE = 2
            GREEN = 3

est égal à :

.. code-block:: pycon

    >>> StateLight = Enum('Light', 'RED ORANGE GREEN')
    >>> List(StateLight)
    [<Light.RED: 1>, <Light.ORANGE: 2>, <Light.GREEN: 3>,]


IntEnum
^^^^^^^

IntEnum dérive de :py:class:`int`, il permet de donnée des valeurs entière aux enumération, mais surout de pouvoir les comparé avec des int, par extension il peut donc faire des comparaisons entre
deux enumération de type IntEnum.


.. code-block:: pycon

    >>> from enum import IntEnum
    >>> class Color(IntEnum):
        RED = 1
        GREEN = 2

    >>> class Request(IntEnum):
        POST = 1
        GET = 2

    >>> Color == 1
        False
    >>> Color.RED == 1
        True
    >>> Color.RED == Request.POST
        True


Attention les intEnum ne peuvent pas être comparé à des Enum normales même si le valeurs de l'Enum sont numériques.

IntFlag
^^^^^^^

IntFlag est également basé sur int, mais il permet d'utiliser des opérations sur les bits comme le et logique.

.. code-block:: pycon

    >>> from enum import IntFlag
    >>> class Perm(IntFlag):
        X = 1
        W = 2
        R = 4

    >>> Perm.W | 2
        <Perm.W: 2>

Vous pouvez également utiliser ces opérations entre deux IntFlag différent, cela retournera toujours un IntFlag.

.. code-block:: pycon

    >>> Perm.W | Perm.R
        <Perm.R|W: 6>

    >>> Perm.W & Perm.X
        <Perm.0: 0>

A partir de la vous pouvez convertir le retour dans d'autres type.

.. code-block:: pycon

    >>> bool(Perm.W & Perm.X)
        False

    >>> int(Perm.W | Perm.R)
        6


Flag
^^^^

Comme IntFlag les Flags peuvent être combinés avec des opérations logiques, sans être des valeurs numériques.
Bien que les valeurs puissent être donné manuellement il est conseillé d'utiliser le paramètre auto(), qui donne
automatiquement des valeurs.

..
    auto() n'est certainement pas un paramètre.
    Quelle différence avec IntFlag alors??

.. code-block:: pycon

    >>> from enum import Flag
    >>> class Color(Flag):
       RED = auto()
       BLUE = auto()
       GREEN = auto()

    >>> Color.RED
      <Color.RED: 1>
    >>> Color.BLUE
      <Color.BLUE: 2>
    >>> Color.GREEN
      <Color.GREEN: 4>

Il est également possible donner des valeurs qui sont des retours d'opération d'autres Flag.

.. code-block:: pycon

   >>> class Color(Flag):
   ...    RED = auto()
   ...    BLUE = auto()
   ...    GREEN = auto()
    ...   WHITE = RED | BLUE | GREEN

    >>> Color.WHITE
    <Color.WHITE: 7>

.. et ça vous surprend?

Conclusion
------------

L'enumération est, bien que non obligatoire, une bonne pratique en programmation, elle simplifie la compréhension du code,  notament lorsque l'on travaille en groupe.
Et bien qu'elle ne soit que peu utilisé aujourd'hui il important de l'avoir testé un jour pour un dévellopeur, par exemple en python qui donne avec son module :py:mod:`enum`, plusieurs
outils intéressant.

    *Actually, Python enums are pretty OK*

    -- Karol Kuczmarski


.. [#abds] <axel.bentodasilva@he-arc.ch>

Bibliographie
---------------

Sam&Max :
<http://sametmax.com/les-enums-en-python/>

Karol Kuczmarski :
<http://xion.io/post/code/python-enums-are-ok.html>
