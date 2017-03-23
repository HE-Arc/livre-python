.. _math-tutorial:

======================
    Math/Fractions
======================

.. image:: img/logo.png
   :align: right
   :alt: Fraction

Par Gabriel Griesser [#gg]_

=================
    Introduction
=================
Le principe du module *MATH* est d'effectuer diverses opérations mathématiques avec Python. 
Dans ce chapitre, nous verrons les nombres et les fractions en Python en utilisant ce module.

Les nombres entiers sont relativement simple a utiliser en Python. 
Ce langage devine facilement si un nombre est entier ou pas grâce à la virgule (ou point décimal dans *Python*).
Si le nombre ne possède pas de virgule, Python le reconnait comme un nombre entier.

Les résultats des opérations comme les fractions ne seront affichés correctement que si le résultat est décimal,
par exemple :``1/5 + 1/2 = 7/10``  sera affiché correctement.
Si le résultat n'est pas décimal, l'égalité ne pourra pas s'écrire sous forme décimale, 
par exemple : ``1/2 + 1/3 = 5/6`` sera affiché sour la forme ``0.83333333333333``

Pour effectuer des calculs exacts avec des fractions, on importe le module :py:mod:`fractions` 
afin de transformer Python en un langage de programmation spécialisé dans les fractions.

==============
    Nombres 
==============
Avant tout, il faut savoir que les nombres sont déclarés comme des variables en Python, et que le type de ces dernières
sont reconnu à l'initialisation de la variable.
Python comporte cinq catégories de nombres :

 * `int` pour les nombres entiers.
 * `long` pour les grands entiers.
 * `fraction` pour les fractions (quotients d'entiers par des entiers).
 * `decimal` et `float` pour les réels (ou *nombres décimaux*).
 * `complex` pour les nombres complexes.

Exemples
--------
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
Ici, *a* est la racine carrée de 100, la commande ``a.is_integer()`` 
renvoi ``true`` si le nombre est un *int*, ``false`` sinon.
*b* est la puissance cubique de *a*, c'est à dire 1'000.
Les puissances peuvent aussi s'écrire en dédoublant l'astérisque de la multiplication.
Dans cet exemple, comme aucune des variables ne possède de virgule, Python les reconnait comme des *int*.

.. code-block:: pycon

	>>> from math import *
	>>> a=sqrt(100)
	>>> print(a)
	10.0
	>>> print(a.is_integer())
	True
	>>>	b=pow(a,3)
	>>>	print(b.is_integer())
	True
	>>> print(b)
	1000.0
	
Les opération comme l'addition, la soustraction et la multiplication sont également faciles et rapides à utiliser.
Notons que pour ce genre d'opération, Python ne demande pas l'importation du module *MATH* car ce sont des opérations
standards.

.. code-block:: pycon

	>>> a=5
	>>> b=-8
	>>> print(a+b)
	-3
	>>> print(a-b)
	13
	>>> print(a*b)
	-40
	
La division se présente sous deux formes : `Le quotient euclidien` qui est un entier, et le `quotient exact`
qui est une fraction, donc un réel pour Python.
Pour choisir quelle forme utiliser, il suffit de dédoubler le *slash* de la division. 
Ici, le premier *print* affichera ``1.5`` alors que le dédoublement du *slash* changera la réponse en ``1``.
	
.. code-block:: pycon

	>>> a=3
	>>> b=2	
	>>> print(a/b)
	1.5
	>>> print(a//b)
	1

En Python, la priorité des opérations s'effectue comme en algère. On effectue dans l'ordre
1. Les parenthèses
2. Les fonctions (racines, puissances)
3. Les multiplications et divisions
3. Les additions et soustractions.


==========
Complexes
==========
Pour utiliser les nombres complexes en *Python*, il suffit d'écrite ``complex(x,y)``.
Rappelons que les physiciens  notant *j* le nombre complexe dont le carré vaut -1, *Python* suit ce choix.


.. code-block:: pycon

	>>> z=complex(4,3)
	>>> print(z)
	(4+3j)
	
Opérations
----------
Les quatre opérations se notent respectivement +, -, * et /, et donnent toujours un complexe, 
même si celui-ci est réel (exemple de la soustraction ci-dessous) :

.. code-block:: pycon

	>>> a=complex(2,3)
	>>> z=complex(4,3)
	>>> print(a+z)
	(6+6j)
	>>> print(a-z)
	(-2+0j)
	>>> print(a*z)
	(-1+18j)
	>>> print(a/z)
	(0.68+0.24j)
	
Propriétés
----------
Les parties réelle et imaginaire d'un complexe sont des propriétés de l'objet :

.. code-block:: pycon

	>>> z=complex(4,3)
	>>> print(z.real)
	4.0
	>>> print(z.imag)
	3.0

Pour le conjugé, c'est la propriétés ``conjugate()`` que nous appelerons :

.. code-block:: pycon

	>>> z=complex(4,3)
	>>> print(z.conjugate())
	(4-3j)
	
Le module et l'arguments, qui sont 2 notions biens propres aux nombres complexes, peuvent être 
obtenus avec ``abs()`` et ``phase()`` 
**ATTENTION**, pour la propriété *phase()*, il faut importer le module :py:mod:`cmath` 

.. code-block:: pycon

	>>> from cmath import *
	>>> z=complex(4,3)
	>>> print(abs(z))
	5.0
	>>> print(phase(z))
	0.6435011087932

Si on intègre le tout en un fichier, voilà ce que ça donne :

.. literalinclude:: ./examples/Complexes.py
	
==========
Fractions
==========
L'écriture de nombres non entiers sous forme de fractions est un concept fondamental des mathématiques.
Chaque fois que le dénominateur n'est pas une puissance de  10, on utilise une écriture fractionnaire.
Par exemple : Si l'on souhaite afficher ``9 heures 17``, cela correspond à ``9 + 17/60 = 493/60``;
Encore ici, lorsque qu'on exprime une attente sous forme de quart d'heure, cela correspond à une fraction.
Par exemple : J'ai attendu trois quarts-d'heure, je peux l'écrite aussi ``J'ai attendu 3/4 d'heure``;

Vous l'avez compris, l'utilisation des fractions se fait quotidiennement. Pour exprimer une telle forme
en *Python*, il faut importer le module :py:mod:`fractions`

Exemple
-------
Voici quelques exemples simples mais efficaces de l'utilisation de ce module.
Pour rentrer la fraction n/d dans *Python*, on utilise le module *fractions*.
Si on rentre 0 comme dénominateur, la fraction ne se crée pas et on a un message d'erreur :
Comme une fraction est un quotient, on ne peut pas diviser par 0.

.. code-block:: pycon

	>>> from fractions import Fraction
	>>> a=Fraction(24,10)
	>>> print(a)
	12/5
	
Une fois la fraction calculée, on peut afficher son numérateur et son dénominateur avec ``a.numerator`` et ``a.denominator``.
Bien entendu, le numérateur de ``24/10`` n'est pas 24, ce dernier est réduit. On obtiendra donc 12.

.. code-block:: pycon

	>>> from fractions import Fraction
	>>> a=Fraction(24,10)
	>>> print(a.numerator)
	12
	>>> print(a.denominator)
	5
	
Pour obtenir le résultat de la fraction en nombre réel, nous pouvons additionner *a* à 0.0 

.. code-block:: pycon
	
	>>> from fractions import Fraction
	>>> a=Fraction(24,10)
	>>> print(a+0.0)
	2.4

Cette méthode n'étant vraiment pas jolie, on préfère ajouter ``float()`` à l'affichage comme cela

.. code-block:: pycon
	
	>>> from fractions import Fraction
	>>> a=Fraction(24,10)
	>>> print(float(a))
	2.4
		

Opérations
----------
Les opérations sur les fractions se notent comme avec des nombres, mais le résultat sortant est en général une fraction.
Les opérations unaires (de bases) se font comme si l'on manipulait des nombres. *Python* les reconnaîtra néanmoins comme 
des fractions.

- Addition

La somme de deux fractions est une fraction :

.. code-block:: pycon
	
	>>> from fractions import Fraction
	>>> a=Fraction(23,42)
	>>> b=Fraction(34,13)
	>>> print(a+b)
	
	
- Soustraction
	
La différence de deux fractions est également une fraction :
	
.. code-block:: pycon
	
	>>> from fractions import Fraction
	>>> a=Fraction(23,42)
	>>> b=Fraction(34,13)
	>>> print(a-b)
	-1129/546
	
- Multiplication
	
Le produit de deux fractions est également une fraction :
	
.. code-block:: pycon
	
	>>> from fractions import Fraction
	>>> a=Fraction(23,42)
	>>> b=Fraction(34,13)
	>>> print(a*b)
	391/273	
		
- Division
	
Le quotient de deux fractions est également une fraction, pour autant que la 2ème fractions ne soit pas nulle :
Il est également possible d'afficher le reste euclidien avec le pourcent %. Ce reste est une fraction.
	
.. code-block:: pycon
	
	>>> from fractions import Fraction
	>>> a=Fraction(23,42)
	>>> b=Fraction(34,13)
	>>> print(a/b)
	299/1428
	>>> print(a%b)
	23/42
	
- Puissance

L'exposant d'une fraction est une fraction, pour autant que l'exposant est un entier :
	
.. code-block:: pycon
	
	>>> from fractions import Fraction
	>>> a=Fraction(23,42)
	>>> print(a**3)
	12167/74088
	>>> print(a**(-3))
	74088/12167
	
Si l'exposant est un réel, le résultat sera un réel :

.. code-block:: pycon
	
	>>> from fractions import Fraction
	>>> a=Fraction(23,42)
	>>> print(a**0.6);
	0.6967662840791479
	
- Opposé

L'opposé d'une fraction s'obtient en la faisant précéder du signe - :

.. code-block:: pycon
	
	>>> from fractions import Fraction
	>>> a=Fraction(23,42)
	>>> print(-a)
	-23/42
	
	
- Inverse

L'inverse d'une fraction s'obtient en la divisant par 1 :

.. code-block:: pycon
	
	>>> from fractions import Fraction
	>>> a=Fraction(23,42)
	>>> print(1/a)
	42/23

	
Voici le code résumé de toutes ces opérations en python :

.. literalinclude:: ./examples/Fraction.py
	
	
================
    Algorithmes
================
Le module :py:mod:`fractions` permet également la création de la suite de `Farey
<http://fr.wikipedia.org/wiki/Suite_de_Farey>`_.

En important le module :py:mod:`fractions` de Python, il est facile de créer une suite de Farey :

.. literalinclude:: ./examples/Farey.py

	
Fractions égyptiennes
---------------------
.. image:: img/egyptien.png
   :align: right
   :alt: Egyptien
	
Une `fraction égyptienne <http://fr.wikipedia.org/wiki/Suite_de_Farey>`_ est une somme de fractions unitaires.
C'est-à-dire de fractions qui ont des numérateurs égaux à un et des dénominateurs entiers positifs, 
avec ces dénominateurs tous différents.
De ce fait, **toute fraction peut s'écrire comme une somme de fractions égyptiennes**.
Dans l'exemple ci-dessous, l'algorithme fournit une liste de fractions, toutes de numérateur 1, dont la somme
est une fraction donnée *f*.

.. literalinclude:: ./examples/Farey.py


Dans cet exemple, le dénominateur d'une fraction égyptienne est choisi (en entier) et est plus grand
que l'inverse de la fraction *f* (pour que l'algorithme converge). Attention si l'inverse de *f* est entier,
on ne doit pas ajouter 1 car la suite serait infinie. On utilise alors la fonctoin ``ceil``. Donc

 - Il faut importer le module *math* qui contient la fonction ceil.
 - L'objet ``ceil(1/f)`` n'est plus un entier mais un réel (par conséquent, il ne peut plus être le dénominateur d'une fraction, donc erreur de *Python*). On convertit alors ce réel en entier (avec le *int*).

Comme *Python* ne possède pas de boucle *do..while*, il faut ajouter la dernière fraction égyptienne à la liste, 
pour que celle-ci soit complète.


================
   Conclusion
================

Le calcul mathématique peut largement se faire en *Python*. À savoir que ce dernier reconnaît automatiquement
le type de la variable selon si cette dernière possède une virgule ou pas. Il est aisé de demander à *Python*
de nous indiquer le type d'une variable. Toutes les opérations mathématiques sur les nombres se font à l'affichage.
Au moment du ``print()``, on spécifie quelques paramètres afin d'avoir la sortie voulue.
*Python* reconnaît et manipule également les nombres complexes. Il suffit de rentrer ``complex()`` afin 
d'utiliser ces derniers. Bien entendu, toutes les manipulations propres aux nombres complexes 
(réel, imaginaire, module, argument) sont possibles.
En important le module :py:mod:`fractions` , il est facile d'effectuer nos manipulations en utilisant des 
fractions. Les opérations sur les fractions se font comme pour les nombres, au moment de l'impression.



.. [#gg] <gabriel.griesser@he-arc.ch>

Bibliographie
-------------

 - Nombres : <https://fr.wikibooks.org/wiki/Math%C3%A9matiques_avec_Python_et_Ruby/Nombres_en_Python>`
 - Nombres opérations : <https://fr.wikibooks.org/wiki/Math%C3%A9matiques_avec_Python_et_Ruby/Nombres_entiers_en_Python>`
 - Nombres complexes : <https://fr.wikibooks.org/wiki/Math%C3%A9matiques_avec_Python_et_Ruby/Nombres_complexes_en_Python>`
 - Fractions : <https://fr.wikibooks.org/wiki/Math%C3%A9matiques_avec_Python_et_Ruby/Fractions_en_Python>`
	