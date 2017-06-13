.. _weakref-tutorial:

``weakref``
===========

Par Anthony Gillioz [#ag]_

Introduction
------------

:py:mod:`weakref` est un module de python qui permet au programmeur de créer des réference faibles sur des objets.
Une référence faible sur un objet ne va pas garder cet objet en vie, si les seuls références sur cet object est une weakref,
le garbage collector est alors libre de détruire l'objet référencé. Ce qui ne pourai pas être faisable avec des références forte.

:py:mod:`gc` est un module qui met à disposition du programmeur une interface pour gérer manuellement le ramasse miette. Il permet entre autres,
de désactiver ou de forcer la collection des ressources, ainsi que d'atteindre les objets que le collecteur a trouvés mais ne peut pas libérer.

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
Ce qui va nous permettre d'expérimenter les références circulaires. Ce type de références arrive quand deux objets se référencent mutuellement,
ce qui va augmenter leurs compteurs de référence. Et au moment où l'on n'utilise plus ces objets, le ramasse-miettes ne va pas pouvoir supprimer
les supprimer vu que leur compteur n'est pas à zéro.

.. literalinclude:: ./examples/example2.py
   :language: python

Maintenant si nous tentons de faire des références cyclique sur notre objet. Que a a une référence sur b et que b a une référence sur a.
Au moment ou l'on veut détruire nos objets, les destructeurs de nos objets a et b ne sont jamais appelé et vont exister tant que l'interpréteur n'est pas quitté.

.. literalinclude:: ./examples/exampleStrongRef2.pycon
   :language: pycon

La solution à ce problème est de stocker des références faibles sur nos objets, ce qui va permettre au ramasse-miettes de supprimer les objets qui sont coincés dans
une référence cyclique (Le ramasse-miette de python est capable de détecter et supprimer directement des références cycliques).

.. literalinclude:: ./examples/example2Sol.py
   :language: python

Module :py:mod:`gc`
-------------------

Le module gc, comme expliqué dans l'introduction permet de gérer manuellement le ramasse-miettes. Dans cette section, je présente les principals fonction du module :py:mod:`gc`.

Le ramasse-miettes tiens à jour 3 listes de génération de collections (threshold0, threshold1, threshold2), ces listes permettant de mettre les objets dans la bonne
liste en fonction du nombre de collection auquel ils ont survécu.
Les nouveaux objets sont placé dans la liste de génération 0 (threshold0). Quand la première libération de la mémoire a lieu, et que des objets ont survécu,
ils passent alors dans la liste de génération 1 (threshold1). À ce moment là, s'ils survivent de-nouveau au ramasse-miettes, alors ils passent dans la dernière liste de génération 2
(threshold2).
L'utilité de ces listes est que plus l'objet est dans une liste de génération élevée, plus il se passera de temps avant que le ramasse-miettes revienne pour le collecter.


:py:func:`~gc.disable`:
    Permet d'activer le ramasse-miettes.

:py:func:`~gc.disable`:
    Permet de désactiver le ramasse-miettes.

:py:func:`~gc.collect`:
    Permet de forcer l'utilisation du ramasse-miettes.

:py:func:`~gc.garbage`:
    Retourne la liste des objets qui ne sont plus référencés mais qui ne peuvent pas être libéré.

:py:func:`~gc.set_threshold`:
    Permet de changer le temps des différentes

:py:func:`~gc.count`
    Retourne le nombre d'objet dans chaque liste de génération


Conclusion
----------

Le module :py:mod:`weakref` est obligatoire pour les applications on l'on a besoin de savoir exactement ce qui ce passe en mémoire si notre mémoire est limité.
*weakref* est un module puissant, les exemples présentés sur cette page sont très basiques et sont destinés a comprendre le module sans rentrer en profondeur dans les détails.
Pour approfondir vos connaissances sur se sujet vous pouvez vous rendre sur la doc officiel : :py:mod:`weakref`.

Le module :py:mod:`gc` est un module complémentaire au module :py:mod:`weakref`, il permet d'avoir une plus grande maîtrise de ce qui ce passe en mémoire.

    *Les robots n’ont ni choix à faire ni décisions à prendre.*

    -- Travis fan club


.. [#ag] <anthony.gillioz@he-arc.ch>
