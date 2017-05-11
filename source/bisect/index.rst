.. _bisect-tutorial:

``bisect``
==========

Par Yoan Blanc [#yb]_

:py:mod:`bisect` est un tout petit module permettant de travailler avec des listes triées. Son nom provient de l'algorithme utilisé nommé *recherche dichotomique* (`Wikipedia`_) ou parfois *bissection* (en anglais notamment).

Introduction
------------

Comme le cite l'article de _pymotw sur le suject, :py:mod:`bisect` est un petite module avec deux fonctionnalités simples.

- Trouver la position pour insérer un élément dans une liste triée : :py:func:`~bisect.bisect`
- Insérer un élément dans la liste triée : :py:func:`~bisect.insort`

Par défaut, ces deux opérations travaillent à *droite*. C'est-à-dire que la recherche fournit le dernier élément trouvé en cas de doublons, et que l'ajout se fait à la suite de la liste.

.. literalinclude:: ./examples/bisect.pycon

Afin de travailler à gauche, et insérer au début d'une série, il faut travailler avec les alternatives :py:func:`~bisect.bisect_left` et :py:func:`~bisect.insort_left`.

.. literalinclude:: ./examples/bisect_left.pycon

.. note::

    :py:func:`~bisect.bisect_right` est un alias pour :py:func:`~bisect.bisect`, tout comme :py:func:`~bisect.insort_right` et :py:func:`~bisect.insort`.

Exemple
-------

L'exemple ci-dessous utilise le module :py:mod:`collections.abc` (voir :ref:`abc-tutorial`, et :ref:`unittest-tutorial`) pour composer une collection restant triée en toute circonstance. Comme expliqué précédemment, l'intérêt par rapport à effectuer des tris à intervalle régulier est la complexité qui reste base.

.. literalinclude:: ./examples/sortedcollection.py
   :start-after: # start
   :end-before: # end
   :linenos:

Ce module est inspiré d'un article sur ActiveState_ (datant de 2010) adapté pour Python 3.

Alternatives
------------

:py:mod:`heapq` est un module implémantant une liste de priorité, nommé tas ou *heap* en anglais permettant de, à moindre coût, obtenir la valeur la plus petite (par défaut), d'une liste de valeur.

Conclusion
----------

Quel que soit le besoin, il n'est jamais conseillé de retrier une liste régulièrement. :py:mod:`bisect` et :py:mod:`heapq` offrent de bons outils pour pâlier au coût d'un tri complet.

.. [#yb] <yoan.blanc@he-arc.ch>

.. bibliographie

.. _pymotw: https://pymotw.com/3/bisect/
.. _Wikipedia: https://fr.wikipedia.org/wiki/Recherche_dichotomique
.. _ActiveState: https://code.activestate.com/recipes/577197-sortedcollection/
