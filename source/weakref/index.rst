.. _weakref-tutorial:

Weakref
=======

Par Anthony gillioz [#ya]_

Introductions
-------------
**Weakref** est un module de python qui permet au programmeur de créer des réference faibles sur des objets. Une référence faible sur un objet ne va pas garder cet objet en vie, si les seuls références sur cet object est une weakref,
le garbage collector est alors libre de détruire l'objet référencé. Ce qui ne pourai pas être faisable avec des références forte.

Référence (forte)
"""""""""""""""""

En python, tous les objets, dans tous les cas sont accèdé par références. Les références sont des pointeurs sur des objets, ils vont pointer à l'endroit ou se trouve l'objet en mémoire.
Il y a aussi un compteur de référence qui va s'incrémenté à chaque fois qu'une référence est créée sur un objet, et c'est seulement quand ce compteur est à zéro que l'objet va être détruit par le garbage collector.

Référence faible
""""""""""""""""

.. warning::
    Tous les objects ne supporte pas les weakref. Par exemple les list et les dict ne supporte pas directement les weakref mais peuvent le faire si l'on les sous classe. Pour plus d'information sur les objets supporter `Weakref support`_

Garbage collector
"""""""""""""""""

Exemple d'utilisation
---------------------

Dans cet exemple nous allons montrer l'utilité que peut avoir l'utilisation des weakref. Prenons la classe trivial ci-dessous:

.. code-block:: python3

    class ExampleWeakref(object):
     def __init__(self):
      print 'created'

     def __destroy__(self):
      print 'destroy'

Et que nous executons le code ci-dessous, avec des références fortes sur les objets créer. Il faut que les deux références sur l'objet sois détruite pour que le garbage collector libère la mémoire de l'objet.

.. code-block:: python3

    >>> a = ExampleWeakref()
    created
    >>> b = a
    >>> del a
    >>> del b
    destroyed

Alors que si nous n'avions qu'une seul référence forte sur l'objet et une faible comme dans l'exemple ci-dessous. La supression ce fait directement après la destruction de la référence forte. Grace à cela nous pouvons savoir exactement quand l'espace mémoire sera libéré.

.. code-block:: python3

    >>> a = ExampleWeakref()
    created
    >>> b = weakref.ref(a)
    >>> del a
    destroyed

Exemple n°2
-----------

L'utilité des weakref n'est pas des plus optimal dans cet exemple basic. Nous allons donc maintenant rajouter une méthode à notre class. Ce qui va nous permettre d'experimenter les références cyclique (c'est un objet qui a dans ces propriété une référence au même type que lui).

.. code-block:: python3

    class ExampleWeakref(object):
     def __init__(self):
	 self.obj = None
	  print 'created'
	 ...
     def store(self,obj)
	 self.obj = obj

Maintenant si nous tentons de faire des références cyclique sur notre objet. Les destructeurs de nos objets a et b ne sont jamais appelé

.. code-block:: python3

    >>> a = ExampleWeakref()
    created
    >>> b = ExampleWeakref()
    created
    >>> a.store(b)
    >>> b.store(a)
    >>> del a
    >>> del b

Conclusion
----------


.. [#ya] <anthony.gillioz@he-arc.ch>

.. Bibliographie

.. _Weakref support: https://docs.python.org/3/extending/newtypes.html#weakref-support
