.. _fstrings-tutorial:

=========
f-strings
=========

Ecrit par : Thibaut Piquerez

------------
Introduction
------------
f-strings permet d'insérer des expressions dans des chaines de caractères en utilisant une syntaxe minimale.

--------------
Fonctionnement
--------------
Pour utiliser f-strings il suffit de mettre un f devant la chaine de caractères et pour insérer la valeur d'une variable dans la chaine il suffit de mettre la variable entre accolade.

.. code-block:: pycon

	>>> name = 'Paul'
	>>> age = 23
	>>> print(f'Votre nom est un {name} et vous avez {age} ans')
	
	Votre nom est un Paul et vous avez 23 ans
	
-----------	
Echappement
-----------
Certain cractères ne peuvent pas être afficher tel quel il est nécaissaire de les échapper.

Pour les accolade {} il faut en mettre 2 a la suite:

.. code-block:: pycon

	>>> nombre = 34
	>>> print(f'Le nombre est {{{nombre}}}')
	
	Le nombre est {34}
	
Pour afficher des apostrophes il y a trois solutions:

	Mettre la chaine entre guillemets :
	
	.. code-block:: pycon
	
		>>> print(f"ma chaine de caractères avec des 'apostrophes' ")
		
		ma chaine de caractères avec des 'apostrophes' 
		
	Mettre la chaine entre 3 apostrophes :
	
	.. code-block:: pycon
	
		>>> print(f'''ma chaine de caractères avec des 'apostrophes' ''')
		
		ma chaine de caractères avec des 'apostrophes' 

	Mettre des backslash avant les apostrophes :

	.. code-block:: pycon
	
		>>> print(f'''ma chaine de caractères avec une \'apostrophe ''')
		
		ma chaine de caractères avec des 'apostrophes

-------------		
raw f-strings		
-------------
	
Un f-strings converti automatiquement les échapements avec des backslash comme par exemple : '\\n' , '\\"' , "\\'" , '\\xhh' , '\\uxxxx' , '\\Uxxxxxxxx'. Donc si on ne veut pas que python interprète ces échappements il faut utiliser les raw f-string en ecrivant fr avant la chaine de caractères et non f.

.. code-block:: pycon

		>>> print(f'ma \n phrase')
		
		ma 
		 phrase

		>>> print(fr'ma \n phrase')
		
		ma \n phrase

		
	
	

