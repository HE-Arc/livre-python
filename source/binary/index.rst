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

.. code-block:: python 

	msg = bytes('exemple', encoding = 'utf-8')
	#où mais l'encodage par défaut sera utilisé.
	msg = b"exemple" 

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

Cast bytes <-> string

.. code-block:: python

	#Cast string en bytes
	my_str = "exemple"
	bytes = str.encode(my_str)

	#Cast bytes en string
	my_decoded_str = str.decode(bytes)
	type(my_decoded_str) # ensure it is string representation
	
Cast Int <-> Bytes

.. code-block:: python

	i = 16

	#Crée 1 byte avec un int 16.
	#Attention à utiliser le bon encodage (little ou big endian)
	#vérifiez avec sys.byteorder
	single_byte = i.to_bytes(1, byteorder='big', signed=True) 
	print(single_byte)

	# Crée un bytes avec une liste de int (0-255)
	# sortie: b'\xff\xfe\xfd\xfc
	bytes_from_list = bytes([255, 254, 253, 252])

	# Print out binary string (e.g. 0b10110)
	print(bin(22))
	
	# Bytes à Integer
	# Crée un int avec un bytes (non signé par défaut)
	i = int.from_bytes(some_bytes, byteorder='big')

	# Crée un int signé
	i = int.from_bytes(b'\x00\x0F', byteorder='big', signed=True)

	# Utilise une liste d'entiers comme source pour le cast
	i = int.from_bytes([255, 0, 0, 0], byteorder='big')
	
Lecture d'un fichier

.. code-block:: python

	with open("test_file.dat", "rb") as binary_file:
    # Lit tout le fichier
    data = binary_file.read()
    print(data)

    # Lit N bytes depuis une certaine position
    binary_file.seek(0)
    couple_bytes = binary_file.read(2)
    print(couple_bytes)

`Un tableau résumant les opérations standards sur les bytes se trouve sur la documentation officielle <https://docs.python.org/3.1/library/stdtypes.html>`_.

BytesArray
----------

Le type bytearray est un tableau de byte et contient donc un objet bytes dans chaque clé.
Il n'y a donc pas de différence un bytarray est une collection de byte.

Instanciation
~~~~~~~~~~~~~

bytearray([initializer[, encoding]])

exemple

.. code-block:: python

	#crée un bytearray à partir d'un objet bytes  
	msg = bytearray(b"exemple") 
	#rée un  bytearray à partir d'une chaine de caractères
	msg = bytearray("exemple", "utf-8")  
	#Crée un  bytearray à partir d'une liste d'entiers entre 0 et 255  
	msg = bytearray([94, 91, 101, 125, 111, 35, 120, 101, 115, 101, 200])  
	
	#hexadécimal
	0xff  #sortie 255
	#binaire
	0b100  #sortie 4
	
	# autres possibilitées
	"{:x}".format(int.from_bytes("exemple".encode("utf-8"), byteorder="big"))                                     
	#sortie '6578656d706c65'
	# 65 est la lettre 'e' en hexadécimal.
	f"{ord('e'):x}"  #sortie '65'
	
Accès
~~~~~

Accède la première valeur à la clé 0 donc b'exemple' dans l'exemple ci-dessus.

.. code-block:: python

	msg[0]
	
Opérations
~~~~~~~~~~

En plus des opérations, ci-dessous voir les opérations de bytes ci-dessus.

.. code-block:: python

	# Cast bytes à bytearray
	mutable_bytes = bytearray(b'\x00\x0F')

	# Cast bytearray à bytes
	immutable_bytes = bytes(mutable_bytes)

	
MemoryView
----------

Une memoryView est un objet permettant d'utiliser des buffers afin de pouvoir les manipuler comme tout autre objet Python.

Instanciation
~~~~~~~~~~~~~

.. code-block:: python 

	# Crée une memoryview à partir d'un objet byte.
	mv = memoryview(b'exemple')

Opérations
~~~~~~~~~~

.. code-block:: python 

	# retourne les données comme string de bytes.
	# sortie: b'abc'.
	mv = memoryview(b"abc")
	mv.tobytes()
	
	# retourne les données en hexadécimale.
	# sortie: '616263'.
	mv = memoryview(b"abc")
	mv.hex()

	# retourne les données en une lsite d'élements.
	# sortie: [97, 98, 99].
	memoryview(b'abc').tolist()
	
	# relacher le buffer.
	mv.release()
	
`Plus d'opérations ici <https://docs.python.org/3.1/library/stdtypes.html>`_.
	
Exemple d'utilisation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python 

	mybuf = ... # un grand buffer de bytes
	mv_mybuf = memoryview(mybuf) # une memoryview de mybuf
	func(mv_mybuf[:len(mv_mybuf)//2])
	# passe la première moitié de mybuf dans func comme une "sous-view" créé par le découpage de la memoryview
	# Aucune copie n'est faite ici!

Avec bytearray:

.. code-block:: python 

	>>> buf = bytearray(b'abcdefgh')
	>>> mv = memoryview(buf)
	>>> mv[4:6] = b'ZA'
	>>> buf
	bytearray(b'abcdZAgh')

	
Struct
------

Un struct permet de convertir des structures C en valeurs de Python représenté sous forme d'objets bytes.

Exemple d'utilisation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python 

	#packing et unpacking de trois entiers
	from struct import *
	pack('hhl', 1, 2, 3)
	#sortie : '\x00\x01\x00\x02\x00\x00\x00\x03'
	unpack('hhl', '\x00\x01\x00\x02\x00\x00\x00\x03')
	#sortie : (1, 2, 3)

	#On peut assigner des noms aux champs.
	record = 'raymond   \x32\x12\x08\x01\x08'
	name, serialnum, school, gradelevel = unpack('<10sHHb', record)
	from collections import namedtuple
	Student = namedtuple('Student', 'name serialnum school gradelevel')
	Student._make(unpack('<10sHHb', record))
	Student(name='raymond   ', serialnum=4658, school=264, gradelevel=8)

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

`<https://docs.python.org/2/library/struct.html>`_

`<http://stackoverflow.com/questions/35988/c-like-structures-in-python>`_


Schnaebele Marc 2017
