.. _`binary-tutorial`:

``bytes`` / ``bytearray`` / ``memoryview``, ``struct``
======================================================

Par Marc Schnaebele [#ms]_

``bytes``
---------

Le type :py:class:`bytes` fait partie des types dits de séquence. Il permet de traiter les chaines d'octets.

Instanciation
~~~~~~~~~~~~~

syntaxe

bytes([initializer[, encoding]])

exemple

.. literalinclude:: ./examples/byte_inst.py

Affichage
~~~~~~~~~

Le ``b`` est affiché pour bien préciser que c'est une chaine de type bytes.

.. code-block:: python

    b'exemple'

Accès
~~~~~

Accède à la première valeur à la clé 0 donc b'e' dans l'exemple ci-dessus.

.. code-block:: python

    msg[0]

opérations
~~~~~~~~~~

Cast bytes <--> str

.. literalinclude:: ./examples/cast_bytes_string.py

.. en pratique, on utilise le fait que `str` est un objet.

Cast int <--> bytes

.. literalinclude:: ./examples/cast_bytes_int.py

Un tableau résumant les opérations standards sur les bytes se trouve sur la documentation officielle des :ref:`Built-in Types<python:typebytes>`.

``bytearray``
-------------

Le type :py:class:`bytearray` est un tableau de ``bytes`` et contient donc un objet bytes dans chaque clé.
Il n'y a donc pas de différence un ``bytarray`` est une collection de ``bytes``.

Instanciation
~~~~~~~~~~~~~

bytearray([initializer[, encoding]])

exemple

.. literalinclude:: ./examples/bytearray.py

Accès
~~~~~

Accède la première valeur à l'emplacement donc ``b'exemple'`` dans l'exemple ci-dessus.

.. code-block:: python

    msg[0]

Opérations
~~~~~~~~~~

En plus des opérations, ci-dessous voir les opérations de bytes ci-dessus.

.. literalinclude:: ./examples/bytearray_cast.py

``memoryview``
--------------

Une :py:class:`memoryview` est un objet permettant d'utiliser des buffers afin de pouvoir les manipuler comme tout autre objet Python.

.. Ceci ne veut rien dire, pourtant tout est dans le titre.

Instanciation
~~~~~~~~~~~~~

.. literalinclude:: ./examples/memoryview_inst.py

Opérations
~~~~~~~~~~

.. literalinclude:: ./examples/memoryview_op.py

Plus d'opérations sur les memoryview dans la documentation des :ref:`Built-in Types <python:typememoryview>`.

Exemple d'utilisation
~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ./examples/memoryview_ex_python.py

Avec bytearray:

.. literalinclude:: ./examples/memoryview_ex_bytearray.py

``struct``
----------

Un :py:mod:`struct` permet de convertir des structures C en valeurs Python représenté sous forme d'objets bytes. Ceux-ci sont utilisés pour manipuler des données binaire depuis des fichiers, le réseau ou d'autres sources.

Exemple d'utilisation
~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ./examples/struct.py

Plus d'informations sur les methodes et caractéristiques des :py:mod:`struct`. se trouve sur la documentation officielle.
	
Sources
-------

:py:class:`bytes` / :py:class:`bytearray`

:ref:`Built-in Types <python:bltin-types>`.

`<http://stackoverflow.com/questions/16678363/python-3-how-do-i-declare-an-empty-bytes-variable>`_

`<http://stackoverflow.com/questions/19511440/add-b-prefix-to-python-variable>`_

`<http://www.devdungeon.com/content/working-binary-data-python>`_

`<http://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3>`_

:py:class:`memoryview`

`<https://docs.python.org/3/library/stdtypes.html?highlight=memoryview#memoryview>`_

`<http://stackoverflow.com/questions/6736771/buffers-and-memoryview-objects-explained-for-the-non-c-programmer>`_

:py:mod:`struct`

`<https://docs.python.org/3.6/library/struct.html#module-struct>`_

`<https://docs.python.org/2/library/struct.html>`_

`<http://stackoverflow.com/questions/35988/c-like-structures-in-python>`_

.. [#ms] <marc.schnebele@he-arc.ch>
