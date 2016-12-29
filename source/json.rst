JSON
====

.. image:: image/json.gif
   :align: right
   :alt: JSON logo

Par Yoan Blanc (<yoan.blanc@he-arc.ch>)

Introduction
------------

JSON_ ou *JavaScript Object Notation* est un format simple, compact qui a, au
fil des ans, remplacé XML comme format d'échange préféré. Standardisé au sein
de l'`ECMA-404`_ il est supporté par l'énorme majorité des langages de
programmations.

JSON comporte six types : chaines de caractères, nombre, objet, tableau,
booléen (``true``, ``false``) et ``null``.

.. code-block:: json
    :linenos:

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
les booléens et la valeur vide n'étaient pas écrites différemment : ``True``,
``False`` et ``None``.

Le module :py:mod:`json` est des plus simples à utilisé. Il est présenté par
Kenneith Reitz dans `Hitchiker's Guide To Python
<http://docs.python-guide.org/en/latest/scenarios/json/>`_.

Exemple
-------

L'API du module :py:mod:`json` est similaire à celle utilisée par
:py:mod:`marshal` et :py:mod:`pickle` qui permettent de sérialiser des objets
Python.

- :py:meth:`json.load` charge un fichier JSON;
- :py:meth:`json.loads` charge une chaine de caractères;
- :py:meth:`json.dump` écrit en JSON dans fichier;
- :py:meth:`json.dumps` écrit en JSON dans une chaine de caractères.

.. code-block:: python3
   :linenos:

    import json

    print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
    ["foo", {"bar": ["baz", null, 1.0, 2]}]

    print(json.dumps("🐍"))
    "\\ud83d\\udc0d"

    print(json.loads('[1, 2, "Hello"]'))
    [1, 2, 'Hello']

Un exemple travaillant avec un fichier externe. Un point très important est
que JSON est toujours encodé en UTF-8.

.. literalinclude:: example/json/test.json
   :linenos:

.. literalinclude:: example/json/example.py
   :linenos:

Validation
----------

:py:mod:`jsonschema` permet de valider un document JSON selon un modèle.
consultez la documentation de `JSON Schema`_ pour en savoir plus.

.. literalinclude:: example/json/schema.json
   :linenos:

.. literalinclude:: example/json/validation.py
   :linenos:

Conclusion
----------

JSON est un format de fichier à connaitre, comprendre et savoir utiliser. Dans
sa version basique, voire même dans sa version riche nommée `JSON-LD`_ utilisée
par de nombreuses API. Si vous devez consommer des données JSON externe, il
n'est que vivement recommandé d'ajouter un schéma afin d'offrir un message
d'erreur adéquate en cas d'erreur avant que votre application ne casse.

    *JSON c'est bon, mangez-en!*

    -- Anonymous

.. Bibliographie

.. _JSON: http://json.org/
.. _JSON Schema: http://json-schema.org/
.. _JSON-LD: http://json-ld.org/
.. _ECMA-404: http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf
