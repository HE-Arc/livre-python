.. _dunder-tutorial:

=======
Dunders
=======

Introduction
============

Le mot dunder est un raccourci de Double UNDERscore et représente toutes les méthodes de python qui commencent et finissent par un double underscore (par ex. __init__()).

Les dunders sont des méthodes très puissantes et régulièrement utilisées en python. Ce sont des méthodes universelles que toute classe possède (un peu à l'image de la class Object dans Java).
Cependant, dans python, les dunders ne sont rarement appelés directement.

Par exemple :

.. code-block:: python3

      toto = new MyClass()


fera appel aux méthodes __new__() et __init__() même si ces méthodes n'ont pas été surchargées.

Les dunders ont des méthodes raccourci qui vont directements les appelés (autre raison pour laquelle on utilise régulièrement les dunders sans s'en rendre compte) :

.. code-block:: python3

      toto = 4+5


fera appel au dunder __add__()

Ou bien :

.. code-block:: python3

    str("I'm a text")


fera appel au dunder __str__()

La grande puissance des dunders est leur universalité. En effet, python a été programmé de manière à ce qu'une opération soit toujours relié au même dunder.

Par exemple, dans beaucoup de langages, si on veut connaitre la taille d'un truc, il faut d'abord savoir de quoi on parle (un tableau, une liste, un string etc.) avant de faire appel à la méthode appropriée. Dans python, on utilise toujours le dunder __len__() :


.. literalinclude:: someclass.py


Une autre grande utilisation des dunders consiste à les surcharger de manière à les personalisé.

De plus, par convention, on déclare une méthode privée comme étant un dunder :

.. code-block:: python3

      def __myPrivateMethod__(self, other):
          return none;


Exemples
========


.. literalinclude:: someclass.py


.. literalinclude:: main.py


Différence entre str et repr :
------------------------------

Les deux servent à afficher l'objets mais pas de la même manière :
  str se veut d'être lisible, il donne les informations qu'un utilisateur veut savoir et non le programme. Elle est ambigu et permet donc facilement le cast.

  repr se veut au contraire non ambigu. Il doit représenter l'objet tel qu'il est réellement.

De base, quand on chercher à afficher unn objet, à moins que la méthode str soit redéfinie, c'est la méhtode repr qui sera appelée.

.. code-block:: python3

        print(str(3)==str("3")) # return True car str est ambigu
        print(repr(3)==repr("3")) # return False car non-ambigu (Int != String)


Idéalement, il faudrait toujours redéfinir la méthode repr et redefinir str uniquement si on a besoin de la ambiguïté.

Conclusion
==========

Il existe beaucoup de dunders. Il faut puiser dans la doc afin de connaitre ceux dont on a l'usage et savoir quand ils sont utilisés.
Ce sont de puissants outils de Python qui permettent de facilement spécialiser le comportement d'un objet.

Bibliographie
=============

The Python Data model, extrait de Fluent Python
http://sametmax.com/le-guide-ultime-et-definitif-sur-la-programmation-orientee-objet-en-python-a-lusage-des-debutants-qui-sont-rassures-par-les-textes-detailles-qui-prennent-le-temps-de-tout-expliquer-partie-6/
http://www.diveintopython3.net/special-method-names.html

Par Marc Friedli
