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

Accède la première valeur à la clé 0 donc b'e' dans l'exemple ci-dessus.

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

	# Crée un bytes avec une liste dev int (0-255)
	bytes_from_list = bytes([255, 254, 253, 252])

	# Crée un byte avec un int en base 2
	one_byte = int('11110000', 2)
	print(one_byte)

	# Print out binary string (e.g. 0b010010)
	print(bin(22))
	
	#Bytes à Integer
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

Opérations standard
	
.. image:: ./img/bytes_operation.jpg
   :align: right
   :alt: operations bytes
     
.. image:: ./img/bytes_notes.jpg
   :align: right
   :alt: notes bytes
   
   
BytesArray
----------

Le type bytearray est un tableau de byte et contient donc un objet bytes dans chaque clé.

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
	
Accès
~~~~~

Accède la première valeur à la clé 0 donc b'exemple' dans l'exemple ci-dessus.

.. code-block:: python

	msg[0]
	
Opérations
~~~~~~~~~~

En plus des opérations ci-dessous voir les opérations de bytes ci-dessus.

.. code-block:: python
	# Cast bytes à bytearray
	mutable_bytes = bytearray(b'\x00\x0F')

	# Cast bytearray à bytes
	immutable_bytes = bytes(mutable_bytes)

	
MemoryView
----------

Une memoryView est un objet qui sert d'API pour utiliser des buffers (C objet) afin de pouvoir le manipuler comme tout autre objet.

Instanciation
~~~~~~~~~~~~~

.. code-block:: python 

	#Crée une memoryview à partir de l'objet qui définit le nouveau buffer.
	PyObject *PyMemoryView_FromObject(PyObject *obj)

	#Crée une memoryview et wrappe le buffer en structure view.
	#La memoryview détient le buffer qui sera désalloué automatiquement lors de la destruction de l'objet.
	PyObject *PyMemoryView_FromBuffer(Py_buffer *view)

	#Crée une memoryview d'une partie mémoire contiguë.
	#Si dans la mémoire l'objet est stocké de manière contiguë, le pointeur pointe sur cette zone mémoire
	#sinon une copie est faite.
	PyObject *PyMemoryView_GetContiguous(PyObject *obj, int buffertype, char order)

Opérations
~~~~~~~~~~

.. code-block:: python 

	#Retourne true si l'objet obj est une memoryview.
	int PyMemoryView_Check(PyObject *obj)
	
	#Retourne un pointer sur buffer wrapper par l'objet donné.
	Py_buffer *PyMemoryView_GET_BUFFER(PyObject *obj)
	
Exemple d'utilisation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python 

	mybuf = ... # un grand buffer de bytes
	mv_mybuf = memoryview(mybuf) # une memoryview de mybuf
	func(mv_mybuf[:len(mv_mybuf)//2])
	# passe la première moitié de mybuf dans func comme une "sous-view" crée par le découpage de la memoryview
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

struct permet de convertir des structures C en valeurs de python représenté sous forme d'objets bytes.

Instanciation
~~~~~~~~~~~~~

.. code-block:: python 

	#Crée une memoryview à partir de l'objet qui définit le nouveau buffer.
	PyObject *PyMemoryView_FromObject(PyObject *obj)

	#Crée une memoryview et wrappe le buffer en structure view.
	#La memoryview détient le buffer et il sera désalloué automatiquement lors de la destruction de l'objet.
	PyObject *PyMemoryView_FromBuffer(Py_buffer *view)

	#Crée une memoryview d'une partie mémoire contiguë.
	#Si dans la mémoire l'objet est stocké de manière contiguë, le pointeur pointe sur cette 
	#zone mémoire sinon une copie est faite.
	PyObject *PyMemoryView_GetContiguous(PyObject *obj, int buffertype, char order)

Opérations
~~~~~~~~~~

.. image:: ./img/struct_operation.jpg
   :align: right
   :alt: operations struct
	
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

	
Sources
-------

Bytes / Bytearray:

`<https://docs.python.org/3.1/library/stdtypes.html>`_.
`<http://docs.python-guide.org/en/latest/scenarios/json/>`_.
`<http://stackoverflow.com/questions/16678363/python-3-how-do-i-declare-an-empty-bytes-variable>`_.
`<http://stackoverflow.com/questions/19511440/add-b-prefix-to-python-variable>`_.
`<http://www.devdungeon.com/content/working-binary-data-python>`_.
`<http://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3>`_.


Memoryview:

`<https://docs.python.org/3/c-api/memoryview.html>`_.
`<https://docs.python.org/2/c-api/buffer.html>`_.
`<http://stackoverflow.com/questions/6736771/buffers-and-memoryview-objects-explained-for-the-non-c-programmer>`_.

Struct:

`<https://docs.python.org/2/library/struct.html>`_.
`<http://stackoverflow.com/questions/35988/c-like-structures-in-python>`_.


Schnaebele Marc 2017