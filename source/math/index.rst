======================
    Math/Fractions
======================

.. image:: img/logo.png
   :align: right
   :alt: Fraction

Par Gabriel Griesser

Introduction
------------

Le principe du module *MATH* est d'effectuer diverses opérations mathématiques avec Python. 
Dans ce chapitre, nous verrons les nombres et les fractions en Python en utilisant ce module.

Les nombres entiers sont relativement simple a utiliser en Python. 
Ce langage devine facilement si un nombre est entier ou pas grâce à la virgule (ou point décimal dans *Python*).
Si le nombre ne possède pas de virgule, Python le reconnait comme un nombre entier.

Les résultats des opérations comme les fractions ne seront affichés correctement que si le résultat est décimal,
par exemple :``1/5 + 1/2 = 7/10``  sera affiché correctement.
Si le résultat n'est pas décimal, l'égalité ne pourra pas s'écrire sous forme décimale, 
par exemple : ``1/2 + 1/3 = 5/6`` sera affiché sour la forme ``0.83333333333333``

Pour effectuer des calculs exacts avec des fractions, on importe le module fractions.py 
afin de transformer Python en un langage de programmation spécialisé dans les fractions.


Nombres
-------
Avant tout, il faut savoir que les nombres sont déclarés comme des variables en Python, et que le type de ces dernières
sont reconnu à l'initialisation de la variable.
Python comporte cinq catégories de nombres :

- :py:meth:`int` pour les nombres entiers.
- :py:meth:`long` pour les grands entiers.
- :py:meth:`fraction` pour les fractions (quotients d'entiers par des entiers).
- :py:meth:`decimal` et `float` pour les réels (ou *nombres décimaux*).
- :py:meth:`complex` pour les nombres complexes.


Voici un exemple tout simple pour commencer.

.. code-block:: pycon

	>>> a=3
	>>> print(type(a))
	<class 'int'>
	>>> b=3.14
	>>> print(type(b))
	<class 'float'>
	>>> c=int(b)
	>>> print(c)
	3
	
On remarquera que Python reconnait *a* comme un entier,  *b* comme un nombre décimal, 
et *c* qui peut être entier même s'il est obtenu à partir de *b*.
*c* sera converti en entier grâce à *int()* qui s'occupera de faire la conversion d'un nombre décimal en un entier.
Ici, *c* vaut 3.

On peut également utiliser diverses fonctions de la librairie *MATH* comme les `racines` ou les `puissances`.
Ici, *a* est la racine carrée de 100, la commande *a.is_integer()* 
renvoi ``true`` si le nombre est un *int*, ``false`` sinon.
*b* est la puissance cubique de *a*, c'est à dire 1'000.
Les puissances peuvent aussi s'écrire en dédoublant l'astérisque de la multiplication.
Dans cet exemple, comme aucune des variables ne possède de virgule, Python les reconnait comme des *int*.

.. code-block:: python3

	from math import *
	a=sqrt(100)
	print(a)
	print(a.is_integer())
	b=pow(a,3)
	print(b.is_integer())
	print(b)
	
Les opération comme l'addition, la soustraction et la multiplication sont également faciles et rapides à utiliser.
Notons que pour ce genre d'opération, Python ne demande pas l'importation du module *MATH* car ce sont des opérations
standards.

.. code-block:: python3

	a=5
	b=-8
	
	print(a+b)
	print(a-b)
	print(a*b)
	
La division se présente sous deux formes : `Le quotient euclidien` qui est un entier, et le `quotient exact`
qui est une fraction, donc un réel pour Python.
Pour choisir quelle forme utiliser, il suffit de dédoubler le *slash* de la division. 
Ici, le premier *print* affichera ``1.5`` alors que le dédoublement du *slash* changera la réponse en ``1``.
	
.. code-block:: python3

	a=3
	b=2
	
	print(a/b)
	print(a//b)

En Python, la priorité des opérations s'effectue comme en algère. On effectue dans l'ordre
1. Les parenthèses
2. Les fonctions (racines, puissances)
3. Les multiplications et divisions
3. Les additions et soustractions.


Fractions
-------

Exemple
-------
Voici un exemple simple mais efficace de l'utilisation de ce module, pour rentrer la fraction n/d dans *Python*, on utilise le module Fraction


.. code-block:: python3
	from fractions import *
	a=Fraction(24,10)
	print(a)
	