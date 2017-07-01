.. _json-tutorial:

``json``
========

.. image:: ../_static/json.png
   :align: right
   :alt: JSON logo

Par Yoan Blanc [#yb]_

Introduction
------------

JSON_ (*JavaScript Object Notation*) est un format simple, compact qui a, au
fil des ans, remplacé XML comme format d'échange préféré. Standardisé au sein
de l'*ECMA-404* :cite:`bray2014javascript`  il est supporté par l'énorme
majorité des langages de programmation.

JSON_ comporte six types : chaîne de caractères, nombre, objet, tableau,
booléen (``true``, ``false``) et ``null``.

.. code-block:: json

    {
        "clé": "valeur",
        "age": 20,
        "pi": 314.59e-2,
        "tableau": [1, 2, 3, ["x", "y"]],
        "objet": {
            "clé": "autre valeur",
            "booléen": false
        },
        "rien": null
    }

Il serait possible de lire directement cette structure de donnée en Python si
les valeurs booléennes et la valeur vide n'étaient pas écrites différemment :
``True``, ``False`` et ``None``.

Le module :py:mod:`json` est des plus simples à utiliser. Il est présenté par
le fameux Kenneith Reitz dans `Hitchhiker's Guide To Python
<http://docs.python-guide.org/en/latest/scenarios/json/>`_.

Exemple
-------

L'API du module :py:mod:`json` est similaire à celle utilisée par
:py:mod:`marshal` et :py:mod:`pickle` qui permettent de sérialiser des objets
Python.

:py:func:`~json.load`:
    charge un fichier JSON;
:py:func:`~json.loads`:
    charge une chaîne de caractères;
:py:func:`~json.dump`:
    écrit en JSON dans fichier;
:py:func:`~json.dumps`:
    écrit en JSON dans une chaîne de caractères.

.. code-block:: pycon

    >>> import json

    >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    '["foo", {"bar": ["baz", null, 1.0, 2]}]'

    >>> json.dumps("€")
    '"\\u20ac"'

    >>> json.loads('[1, 2, "Hello"]')
    [1, 2, 'Hello']

Un exemple travaillant avec un fichier externe. Un point très important est
que JSON est toujours encodé en UTF-8.

.. literalinclude:: ./examples/test.json
   :caption: test.json

.. literalinclude:: ./examples/example.py

Résultat :

.. literalinclude:: ./examples/test.out.json
   :caption: test.out.json


Validation
----------

:py:mod:`jsonschema` permet de valider un document JSON selon un modèle.
consultez la documentation de `JSON Schema`_ pour en savoir plus.

.. literalinclude:: ./examples/schema.json
   :caption: schema.json

.. literalinclude:: ./examples/validation.py

Formats binaires
----------------

Un document JSON est un fichier texte, qui consomme plus de place qu'une
représentation binaire. Python offre un format de sérialisation en binaire
nommé :py:mod:`pickle`, comme il est possible d'utiliser des bibliothèques
externes telles que :py:mod:`msgpack`, ou `Apache Thrift`_.

Pickle
^^^^^^

:py:mod:`pickle` est le format utilisé par :ref:`multiprocessing-tutorial`
pour échanger des données entre différents processus Python. C'est un format
qui est pratique mais non intéropérable avec d'autres langages, voire même
d'autres versions de Python.

.. literalinclude:: ./examples/pickle.pycon
   :language: pycon

Ce format n'est pas recommandé pour de multiples raisons. La documentation du
module informe que lire du ``pikle`` revient à faire un ``eval``. Ben
Frederickson :cite:`fred2014` mentionne notamment la lenteur et la taille du
``pickle``.

MessagePack
^^^^^^^^^^^

En alternative à ``pickle``, `MessagePack`_ permet de réduire efficacement
l'espace nécessaire au stockage et à l'échange de tels documents. En Python,
c'est le module :py:mod:`msgpack`.

.. literalinclude:: ./examples/msg.pycon
   :language: pycon

Notez que cette petite différence n'est plus forcément intéressante si le
contenu est compressé à l'aide de :py:mod:`gzip`.

.. literalinclude:: ./examples/gzip.pycon
   :language: pycon

Parfois, le mieux est l'ennemi du bien.

Streaming
---------

Autre inconvénient majeur vis-à-vis du format XML est qu'il n'est pas aisé de
lire un document au fur et à mesure qu'il est reçu, en *streaming*. En XML, on
utilise une API nommée :abbr:`SAX (Simple API for XML)`. :py:mod:`json` propose
un modèle demandant de charger l'entier d'un document en mémoire. Comme avec
DOM en XML. Ce problème se résoud à l'aide de `YAJL`_ et du module `ijson`_.

.. literalinclude:: ./examples/stream.py
   :linenos:

Conclusion
----------

JSON est un format de fichier à connaître, comprendre et savoir utiliser. Dans
sa version basique, voire même dans sa version riche nommée `JSON-LD`_ utilisée
par de nombreuses API. Si vous devez consommer des données JSON externe, il
n'est que vivement recommandé d'ajouter un schéma afin d'offrir un message
d'erreur adéquat en cas de non respect du document espéré. Et des solutions
existent afin de contourner des problèmes de fichiers inutilement volumineux ou
devant être chargés complétement en mémoire avoir de pouvoir être lus.

    *JSON c'est bon, mangez-en!*

    -- Anonymous


.. [#yb] <yoan.blanc@he-arc.ch>

.. _JSON: http://json.org/
.. _JSON Schema: http://json-schema.org/
.. _JSON-LD: http://json-ld.org/
.. _MessagePack: http://msgpack.org/
.. _YAJL: http://lloyd.github.io/yajl/
.. _ijson: https://pypi.python.org/pypi/ijson/
.. _Apache Thrift: http://thrift.apache.org/

.. bibliography:: refs.bib
