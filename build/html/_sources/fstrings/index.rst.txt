.. _fstrings-tutorial:

=========
f-strings
=========

Écrit par : Thibaut Piquerez

------------
Introduction
------------
f-strings permet d'insérer des expressions dans des chaines de caractères en utilisant une syntaxe minimale.

--------------
Fonctionnement
--------------
Pour utiliser f-strings il suffit de mettre un f devant la chaine de caractères et pour insérer la valeur d'une variable dans la chaine il suffit de mettre la variable entre accolade. Si il n'y a pas de variable a substituer il n'est pas nécessaire de mettre le ``f`` devant.

.. code-block:: pycon

	>>> name = 'Paul'
	>>> age = 23
	>>> print(f'Votre nom est un {name} et vous avez {age} ans')
	
	Votre nom est un Paul et vous avez 23 ans
	
-----------	
Echappement
-----------
Certains cractères ne peuvent pas être afficher tel quel il est nécessaire de les échapper.

Pour les accolade ``{}`` il faut en mettre deux à la suite :

.. code-block:: pycon

	>>> nombre = 34
	>>> print(f'Le nombre est {{{nombre}}}')
	
	Le nombre est {34}
	
Pour afficher des apostrophes, il y a trois solutions:

	Mettre la chaine entre guillemets :
	
	.. code-block:: pycon
	
		>>> print("ma chaine de caractères avec des 'apostrophes' ")
		
		ma chaine de caractères avec des 'apostrophes' 
		
	Mettre la chaine entre 3 apostrophes :
	
	.. code-block:: pycon
	
		>>> print('''ma chaine de caractères avec des 'apostrophes' ''')
		
		ma chaine de caractères avec des 'apostrophes' 

	Mettre des backslash avant les apostrophes :

	.. code-block:: pycon
	
		>>> print('ma chaine de caractères avec une \'apostrophe ')
		
		ma chaine de caractères avec des 'apostrophes

-------------		
raw f-strings		
-------------
	
Un string convertit automatiquement les échappements avec des backslashs comme par exemple : ``\n`` , ``\"``, ``\t``, etc. Donc si on ne veut pas que python interprète ces échappements il faut utiliser les raw string en ecrivant ``r`` avant la chaine de caractères et si on veut utiliser des raw f-strings il faut mettre ``fr``.

.. code-block:: pycon

		>>> print('ma \n phrase')
		
		ma 
		 phrase

		>>> print(r'ma \n phrase')
		
		ma \n phrase

		
	
	

