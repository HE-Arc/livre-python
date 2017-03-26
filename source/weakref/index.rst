.. _weakref-tutorial:

``weakref``
===========

Par Anthony Gillioz [#ag]_

Introduction
------------

:py:mod:`weakref` est un module de python qui permet au programmeur de créer des réference faibles sur des objets.
Une référence faible sur un objet ne va pas garder cet objet en vie, si les seuls références sur cet object est une weakref,
le garbage collector est alors libre de détruire l'objet référencé. Ce qui ne pourai pas être faisable avec des références forte.

Référence (forte)
"""""""""""""""""

En Python, tous les objets, dans tous les cas sont accédé par références. Les références sont des pointeurs sur des objets,
ils vont pointer à l'endroit où se trouve l'objet en mémoire.
Il y a aussi un compteur de référence qui va s'incrémenté à chaque fois qu'une référence est créée sur un objet,
et c'est seulement quand ce compteur est à zéro que l'objet va être détruit par le garbage collector.

Référence faible
""""""""""""""""

Les références failbes (weakref) permettent de créer des références sur des objets sans augmenté le compteur du garbage collector.
Le module :py:mod:`weakref` permet de créer et utilisé les weak références sur les objets. Une des principal utilité de ce module est pour les caches et le mapping de gros objet en mémoire.

:py:class:`~weakref.ref`:
    Retourne une weak référence de l'objet;
:py:func:`~weakref.proxy`:
    Retourne une weak référence de l'objet, mais génère une erreur si l'objet qui essaie d'être atteint n'exite pas;

.. warning::
    Tous les objects ne supporte pas les weakref. Par exemple les ``list`` et les ``dict`` ne supporte pas directement les weakref
    mais peuvent le faire si l'on les sous classe. Pour plus d'information sur les objets supportés.
    Voir: :ref:`weakref-support`.

Ramasse miettes
"""""""""""""""

En Python, l'allocation et la libération de la mémoire se font automatiquement. Le programmeur n'a pas besoin d'allouer ou de supprimer la mémoire allouée comme en C ou en C++.
La principale stratégie de Python pour libérer la mémoire est de se baser sur le système de comptage des références. À chaque fois qu'un référence est créer le compteur de l'objet
s'incrémente et a chaque fois que la référence est supprimé le compteur est décrémenté. C'est seulement quand le compteur est à zéro que la mémoire est libérée.

Le module :py:mod:`gc` permet d'interagir avec le ramasse-miettes.

Exemple d'utilisation
---------------------

Dans cet exemple nous allons montrer l'utilité que peut avoir l'utilisation des weakref. Prenons la classe trivial ci-dessous:

.. literalinclude:: ./examples/example1.py
   :language: python

Et que nous executons le code ci-dessous, avec des références fortes sur les objets créés. Il faut que les deux références sur
l'objet sois détruite pour que le *garbage collector* libère la mémoire de l'objet.

.. literalinclude:: ./examples/exampleStrongRef.pycon
   :language: pycon

Alors que si nous n'avions qu'une seul référence forte sur l'objet et une faible comme dans l'exemple ci-dessous. La supression
ce fait directement après la destruction de la référence forte. Grace à cela nous pouvons savoir exactement quand l'espace mémoire sera libéré.

.. literalinclude:: ./examples/exampleWeakRef.pycon
   :language: pycon

.. warning::

    ``del`` supprime la référence et n'est pas un appel direct à ``__destroy__``.

Référence circulaire
--------------------

L'utilité des *weakref* n'est pas des plus optimal dans l'exemple présenté ci-dessus. Nous allons donc maintenant rajouter une méthode à notre class.
Ce qui va nous permettre d'experimenter les références cyclique (c'est un objet qui a dans ces propriétés une référence au même type que lui).

.. Cette explication est confuse.


.. literalinclude:: ./examples/example2.py
   :language: python

Maintenant si nous tentons de faire des références cyclique sur notre objet. Que a a une référence sur b et que b a une référence sur a.
Au moment ou l'on veut détruire nos objets, les destructeurs de nos objets a et b ne sont jamais appelé et vont exister tant que l'interpréteur n'est pas quitté.

.. literalinclude:: ./examples/exampleStrongRef2.pycon
   :language: pycon

La solution a ce problème est de stocker des références faibles.

.. literalinclude:: ./examples/example2Sol.py
   :language: python

Conclusion
----------

Le module :py:mod:`weakref` est obligatoire pour les applications on l'on a besoin de savoir exactement ce qui ce passe en mémoire si notre mémoire est limité.
*weakref* est un module puissant, les exemples présentés sur cette page sont très basiques et sont destinés a comprendre le module sans rentrer en profondeur dans les détails.
Pour approfondir vos connaissances sur se sujet vous pouvez vous rendre sur la doc officiel : :py:mod:`weakref`.

    *Les robots n’ont ni choix à faire ni décisions à prendre.*

    -- Travis fan club


.. [#ag] <anthony.gillioz@he-arc.ch>
