Binaire
=======

Bytes
-----
Le type bytes fait partie des types dits de séquence. Il permet de traiter les chaines d'octets.

Instanciation
~~~~~~~~~~~~~
syntaxe

bytes([initializer[, encoding]])

exemple

.. literalinclude:: ./examples/byte_inst.py

Affichage
~~~~~~~~~

Le b est affiché pour bien préciser que c'est une chaine de type bytes.

.. code-block:: python

	b'exemple'


Accès
~~~~~

Accède à la première valeur à la clé 0 donc b'e' dans l'exemple ci-dessus.

.. code-block:: python

	msg[0]


opérations
~~~~~~~~~~

Cast bytes <--> string

.. literalinclude:: ./examples/cast_bytes_string.py
	
Cast Int <--> Bytes

.. literalinclude:: ./examples/cast_bytes_int.py
	
Lecture d'un fichier

.. literalinclude:: ./examples/lecture_fichier.py

`Un tableau résumant les opérations standards sur les bytes se trouve sur la documentation officielle <https://docs.python.org/3.1/library/stdtypes.html>`_.

BytesArray
----------

Le type bytearray est un tableau de byte et contient donc un objet bytes dans chaque clé.
Il n'y a donc pas de différence un bytarray est une collection de byte.

Instanciation
~~~~~~~~~~~~~

bytearray([initializer[, encoding]])

exemple

.. literalinclude:: ./examples/bytearray.py
	
Accès
~~~~~

Accède la première valeur à la clé 0 donc b'exemple' dans l'exemple ci-dessus.

.. code-block:: python

	msg[0]
	
Opérations
~~~~~~~~~~

En plus des opérations, ci-dessous voir les opérations de bytes ci-dessus.

.. literalinclude:: ./examples/bytearray_cast.py

	
MemoryView
----------

Une memoryView est un objet permettant d'utiliser des buffers afin de pouvoir les manipuler comme tout autre objet Python.

Instanciation
~~~~~~~~~~~~~

.. literalinclude:: ./examples/memoryview_inst.py

Opérations
~~~~~~~~~~

.. literalinclude:: ./examples/memoryview_op.py
	
`Plus d'opérations ici <https://docs.python.org/3.1/library/stdtypes.html>`_.
	
Exemple d'utilisation
~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ./examples/memoryview_ex_python.py

Avec bytearray:

.. literalinclude:: ./examples/memoryview_ex_bytearray.py

	
Struct
------

Un struct permet de convertir des structures C en valeurs de Python représenté sous forme d'objets bytes.

Exemple d'utilisation
~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ./examples/struct.py

Opérations
~~~~~~~~~~

`Un tableau résumant les opérations standards sur les structures se trouve sur la documentation officielle <https://docs.python.org/3.6/library/struct.html#module-struct>`_.

	
Sources
-------

bytes / bytearray

`<https://docs.python.org/3.1/library/stdtypes.html>`_

`<http://docs.python-guide.org/en/latest/scenarios/json/>`_

`<http://stackoverflow.com/questions/16678363/python-3-how-do-i-declare-an-empty-bytes-variable>`_

`<http://stackoverflow.com/questions/19511440/add-b-prefix-to-python-variable>`_

`<http://www.devdungeon.com/content/working-binary-data-python>`_

`<http://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3>`_


memoryview

`<https://docs.python.org/3/library/stdtypes.html?highlight=memoryview#memoryview>`_

`<http://stackoverflow.com/questions/6736771/buffers-and-memoryview-objects-explained-for-the-non-c-programmer>`_

:py:mod:`struct`

`<https://docs.python.org/3.6/library/struct.html#module-struct>`_

`<https://docs.python.org/2/library/struct.html>`_

`<http://stackoverflow.com/questions/35988/c-like-structures-in-python>`_


Schnaebele Marc 2017
