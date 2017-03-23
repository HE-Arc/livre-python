.. re-tutorial:

Expression régulière (re)
=========================

Par Julien Feuillade

Introduction
------------

Les expressions régulières sont utilisées dans pratiquement tous les langages. C'est un puissant outil qui permet de vérifier si le contenu d'une variable a la forme de ce que l'on attend.
Ils permettent aussi de modifier ou de supprimer tous les éléments indésirables dans une variable.

Les bases de la syntaxe
-----------------------

Une des premières choses à réaliser dans la conception d'une expression régulière, c'est de définir le motif (pattern en anglais)

Pour construire ces motifs, vous avez besoin de créer une structure formée de caractères littéraux, puis de symboles qui sont définis en tant que méta caractères et délimiteurs et qui seront utilisés séparément ou en combinaison à l'intérieur d'un même groupement ou d'une classe.

On utilisera différents types de syntaxe comme :

::

	^		Marque le début de la chaine, la ligne...
	$		Marque la fin d'une chaine, ligne...
	.	    N'importe quel caractère
	*		0, 1 ou plusieurs occurrences
	+		1 ou plusieurs occurrences
	?		0 ou 1 occurrence
	|		Alternative - ou reconnaît l'un ou l'autre
	[ ]		Tous les caractères énumérés dans la classe
	[^ ]	Tous les caractères sauf ceux énumérés
	( )		Utilisée pour limiter la portée d'un masque ou de l'alternative

Ainsi que de groupes de caractères :

::

	\w 		Les lettres (w pour word)
	\d 	 	Les chiffres (d pour digit)
	\s 		Les espaces (s pour spaces)
	[A-Z] 	Les majuscules
	[abd;_] Les lettres a, b, et d, le point-virgule (;), et l’underscore (_)

Prenons un exemple :

::

	k|\d{2} : la lettre k, ou bien deux chiffres
	BRA{,10} : on attend à ce que le segment BRA ne soit pas présent du tout ou présent jusqu'à 10 fois consécutives.

La bibliothèque re
------------------

Afin de mettre les différentes expressions en place, la bibliothèque ``re`` nous est proposé avec ces différentes fonctions qui permettra essentiellement de rechercher / modifier / supprimer des expressions. Pour cela :

.. code:: python

    import re

re.match()
----------

La fonction "match()" va permettre de vérifier la correspondance avec la chaîne de caractère.

.. code:: python

	re.match(pattern, string)

- Pattern est l'expression à faire correspondre
- String est la chaîne d'origine

.. code:: python

	print re.match(r"B(.)?NJO(.)?R", "BONJOUR")

.. code:: python
  
	# true
	<_sre.SRE_Match object at 0x7f61685fc690>

	# false
	None

re.search()
-----------

Afin de rechercher une expression, on utilisera la fonction "search()" :

.. code:: python

	re.search(pattern, string)

- Pattern est l'expression à rechercher
- String est la chaîne d'origine 

.. code:: python

	import re

	line = "Cats are smarter than dogs";

	searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

	if searchObj:
	   print "searchObj.group() : ", searchObj.group()
	   print "searchObj.group(1) : ", searchObj.group(1)
	   print "searchObj.group(2) : ", searchObj.group(2)
	else:
	   print "Nothing found!!"

Sortie :

.. code:: python

	matchObj.group() :  Cats are smarter than dogs
	matchObj.group(1) :  Cats
	matchObj.group(2) :  smarter

re.split()
----------

.. code:: python

	re.split(pattern, string, [maxsplit=0])

- Pattern est l'expression avec lequelle on séparera
- String est la chaîne d'origine
- Maxsplit est le nombre de séparations faite au maximum

.. code:: python

	import re
        
	# Without maxsplit
	sep = re.split("-","+91-011-2711-1111")
	print spe

	# With maxsplit
	sep = re.split("-","+91-011-2711-1111", maxsplit=1)
	print spe

La sortie :

.. code:: python

	# Without maxsplit
	['+91', '011', '2711', '1111']

	# With maxsplit
	['+91', '011-2711-1111']

re.sub()
--------

Afin de remplacer des données, on peut passer par la fonction "sub()" :

.. code:: python

	re.sub(pattern, replace, string)

- Pattern est l'expression à rechercher
- Replace est le remplacent de cette expression
- String est la chaîne d'origine

.. code:: python

	import re

	phone = "2004-959-559"
        
    # Suppresion des guillemets
	num = re.sub(r'#.*$', "", phone)
	print "Phone Num : ", num
	
	# Suppresion de tout sauf les digits
	num = re.sub(r'\D', "", phone)    
	print "Phone Num : ", num

La sortie :

.. code:: python

	Phone Num :  2004-959-559
	Phone Num :  2004959559

re.compile()
------------

Si, dans votre programme, vous utilisez plusieurs fois les mêmes expressions régulières, il peut être utile de les compiler. Le module re propose en effet de conserver votre expression régulière sous la forme d'un objet que vous pouvez stocker dans votre programme.

.. code:: python

	re.compile(pattern)

- Pattern est l'expression à compiler

.. code:: python

	import re

	name_check = re.compile(r"[^A-Za-zs.]")

	name = raw_input ("Please, enter your name: ")

	while name_check.search(name):
		print "Please enter your name correctly!"
		name = raw_input ("Please, enter your name: ")
	print "Welcome !"

La sortie :

.. code:: python

	Please, enter your name:  12
	Please enter your name correctly!

	Please, enter your name:  Julien
	Welcome !

Conclusion
----------

Avec cette documentation vous pouvez avoir une bonne idée de ce qu'est une expression régulière, de comment la construire et de comment l'utiliser. Ne nous leurrons cependant pas, l'apprentissage n'est pas aussi facile, il faut les apprivoiser, « jouer » avec elles, mais le jeu en vaut la chandelle.

.. <julien.feuillade@he-arc.ch>

.. Bibliographie (ceci est un commentaire)

.. https://www.tutorialspoint.com/python/python_reg_expressions.htm
.. http://apprendre-python.com/page-expressions-regulieres-regular-python
.. https://regexone.com/references/python
.. http://www.python-course.eu/re_advanced.php
.. https://www.analyticsvidhya.com/blog/2015/06/regular-expression-python/