.. _builtins-tutorial:

========
Builtins
========

Par Adrien Ferreira Mendes [#afm]_

Introduction
============

L'interpréteur Python contient des fonctions et classes *"embarquées"* qui sont disponibles dans n'importe quel section d'un script. Cette section du livre va donc présenter ces différentes classes et fonctions avec une brève explication et des exemples pour rendre leur compréhension et utilisation plus claire.

Dans une première partie se trouvera la présentation des différentes classes puis une deuxième partie traitera des fonctions qui font aussi parties des "builtins". Il a été choisit de décrire le plus de fonctions possible par ordre alphabétique pour atteindre le maximum de sept pages. Cette section est beaucoup inspirée de la documentation officielle en anglais des "builtins" de python: :ref:`built-in-funcs`.

Les classes
===========

.. _bool:

------------------
*class* bool([x])
------------------
Retourne une valeur booléenne entre ``True`` ou ``False``. Si ``x`` est faux ou est omis, retourne False. Sinon la classe retourne vrai. Cette classe hérite de la classe :ref:`int <int>` , elle ne peut pas être héritée et ces seules instances sont ``True`` ou ``False``.

.. il aurait été intéressant de montrer quoi est True et quoi est False. en fonction de `x`.

.. _bytearray:

---------------------------------------------------
*class* bytearray(*[source[, encoding], errors]]]*)
---------------------------------------------------
Retourne un nouveau tableau de :ref:`bytes <bytes>`. Cette classe est une suite mutable d'entier, elle contient les méthodes de bases des séquences mutables mais aussi la plupart des méthodes de la classe :ref:`bytes <bytes>`.

le paramètre source permet d'initialiser le tableau de manière différente:

* si c'est un *string*, il faut aussi donner les paramètres *encoding* et optionnellement  *errors*. bytearray() convertira le string en :ref:`bytes <bytes>` en utilisant str.encode().

* si c'est un entier, le tableau aura la taille de l'entier et sera initialisé avec des bytes null.

* Si c'est un objet qui implémente l'interface *buffer*, un buffer en lecture sera utilisé pour initialiser le tableau de :ref:`bytes <bytes>`.

* Si c'est un iterable, il faut absolument que cela soit un iterable d'entier  qui doivent tous être compris entre 0 <= x < 256. Les entiers seront utilisés comme contenu initial du tableau.

Sans argument, un tableau de taille 0 sera créé.

.. _bytes:

-----------------------------------------------
*class* bytes(*[source[, encoding[, errors]]]*)
-----------------------------------------------
Retourne un nouveau objet Byte qui est une séquence immuable d'entier compris entre 0 <= x < 256. bytes est une version immuable de :ref:`bytearray <bytearray>`.

.. _method:

--------------------------
*class* method(*fonction*)
--------------------------
Retourne une méthode de classe pour la fonction passée en paramètre.

.. _complex:

---------------------------------
*class* complex(*[real[, imag]]*)
---------------------------------
Retourne un nombre complexe avec la valeur *Réelle + imaginairex1j* ou convertit une chaine de caractères en nombre complexe.

Si le premier paramètre est un string, il sera interprété comme un nombre complexe et il ne faut pas ajouter de deuxième argument. Le deuxième paramètre ne devrait jamais être un string.

**Note :** Lors d'une conversion d'une chaine de caractère, elle ne doit pas contenir d'espace autour du + ou - central. Par exemple, le nombre complexe *'4+3j'* est correct, en revanche *'4 + 3j'* ne l'est pas.

.. _float:

------------------
*class* float([x])
------------------
Retourne un nombre flottant à partir de la chaine de caractères ou du nombre passé en argument.

Si l'argument est un string il doit contenir un nombre décimal précédé d'un + ou d'un -.

Si aucun argument n'est passé, le nombre 0.0 sera retourné.

.. _frozenset:

-------------------------------
*class* frozenset(*[iterable]*)
-------------------------------
Retourne un nouvel objet *frozenset*, avec en option des éléments de *iterable*.

.. _int:

-------------------------
*class* int(*x=0*)
-------------------------
*class* int(*x,base=10*)
-------------------------
Retourne un objet entier  construit grâce à un nombre ou à une chaine de caractères passés en paramètre. Retourne 0 si aucun argument n'est spécifié. Si x n'est pas un entier, il doit impérativement être soit une chaine de caractères, des bytes ou un tableau de bytes. La chaine de caractères peut optionnellement être précédée par un + ou un -.

.. _object:

--------------
*class* object
--------------
Retourne un nouvel objet dépourvu de fonctionnalité. C'est une base à toute les classes. Cette classe contient toutes les méthodes communes à toute les classes Python. Le constructeur de la classe  n'accepte aucun argument.

Les fonctions
==============

.. _abs:

---------
abs(*nb*)
---------
Retourne la valeur absolue d'un nombre. L'argument nb peut être un entier, un nombre flottant ou un nombre complexe. Dans le cas d'un nombre complexe, la fonction renvoie le module du nombre.

.. _all:

---------------
all(*iterable*)
---------------
Retourne vrai si tout les éléments de l'iterable sont vrai ou si  il est vide.

Voici l'algorithme de all:

.. code-block:: pycon

   >>> def all(iterable)
          for element in iterable
             if not element:
                return False
          return True

.. todo:: exemple cassé.

.. _any:

---------
any(it)
---------
Retourne vrai si un des éléments de la table
est vrai. Retourne faux si l'itérable est vide.

.. code-block:: pycon

   >>> def all(iterable)
          for element in iterable
             if  element:
                return True
          return False

.. todo:: exemple cassé.

.. _ascii:

--------------
ascii(*objet*)
--------------
Retourne un string qui contient une représentation affichable d'un objet mais échappe tout les caractères non-ASCII. Cette fonction renvoie un string similaire à celui renvoyé par repr() en Python 2.

.. _bin:

---------
bin(*nb*)
---------
Convertit un entier en binaire. Si nb n'est pas un objet :ref:`int <int>` Python, il doit définir une méthode ``__index__()``  qui retourne un entier


.. _callable:

-----------------
callable(*objet*)
-----------------
Retourne vrai si l'objet passé en argument est "callable", faux sinon. Si cette fonction retourne vrai, il est quand même possible qu'un call échoue. En revanche si elle retourne faux, il est certain qu'un call n'aboutira jamais.

.. _chr:

---------
chr(*i*)
---------
Retourne la lettre correspondant dont l'unicode correspond à l'entier passé en paramètre. par exemple chr(98) retourna la lettre 'b'. Cette fonction fait l'inverse de ord(),


.. _compile:

--------------------------------------------------------------------------
compile(*source, filename, mode, flags=0, dont_inherit=False,optimize=-1*)
--------------------------------------------------------------------------
Compile la source en code ou en un objet AST. Un objet "code" peut être exécuté par exec() ou eval(). La source peut être une chaine de caractères, un byte string ou un objet AST.

L'argument *filename* doit faire référence au fichier qui contient le code à compiler.

Le mode spécifie avec quelle fonction il est possible d’exécuter le code. *Exec* si la source contient beaucoup de code, *eval* si la source ne contient qu'une seule expression et *single* si la source ne contient qu'une seule expression interactive.

.. _delattr:

-----------------------
delattr(*object, name*)
-----------------------
L'argument de cette fonction est un objet et le nom de l'un de ces attributs, la fonction va supprimer l'attribut spécifié si l'objet la lui permet.


.. _dir:

---------------
dir(*[object]*)
---------------
Sans argument, la fonction retourne la liste des noms dans le contexte actuel. Avec un argument, elle essaie de retourner la liste valide des attributs de l'objet.

Si l'objet possède une méthode _dir_(), cette méthode sera appelée et devra retourner la liste des attributs. Ceci permet aux objets qui implémente _getattr_() ou _getattribute_() de choisir la façon dont la fonction dir() agira sur leurs attributs

.. _divmod:

-------------
divmod(*a,b*)
-------------
Prends les deux nombres non-complexes passés en paramètre et retourne leurs quotients et le reste.

.. _enumerate:

-----------------------------
enumerate(*iterable,start=0*)
-----------------------------
Retourne un objet *enumerate*, le paramètre *iterable* doit être un iterateur ou un objet qui supporte l'itération. La méthode _next_() retournée par enumerate est composée de deux éléments, un index et la valeur de l'index.

.. code-block:: pycon

   >>> saison = ['Eté', 'Printemps','Automne','Hiver']
   >>> list(enumerate(saison))
   [(0,'Eté'),(1,'Printemps'),(2,'Automne'),(3,'Hiver')]


.. _eval:

---------------------------------------------
eval(*expression, globals=None, locals=None*)
---------------------------------------------
Les arguments sont un string et des *globals* ou *locals* en option. Si spécifié, *globals* doit être un dictionnaire. Si spécifié, *locals* est un objet de mapping.

L'expression passée en argument est convertit et évaluée comme une expression Python.

.. _exec:

------------------------------------
exec(*object[, globals[, locals]]*)
------------------------------------
l'attribut object doit être soit une chaine de caractères soit un objet. Si c'est une chaine de caractères, elle sera convertie en expressions Python. si c'est un objet, le code qu'il contient sera simplement exécuté. 

.. _filter:

---------------------------
filter(*fontion, iterable*)
---------------------------
Construit un itérateur grâce à *iterable* pour lequel chaque itération de fonction retourne vrai.



.. _format:

------------------------------
format(*value[, format_spec]*)
------------------------------
Transforme *value* en une version *formatée*, contrôlée par *format_spec*.

.. _getattr:

---------------------------------
getattr(*object, name[, default*]
---------------------------------
Retourne la valeur de l'attribut de l'objet passé en paramètre. Si *name* correspond au nom d'un des attributs de l'objet cela revient au même que d'appeler l'objet. Exemple : getattr(x, 'foobar') est égal à x.foobar.

.. _globals:

---------
globals()
---------
Retourne un dictionnaire représentant la table symbolique actuelle.

.. _hasattr:

-----------------------
hasattr(*object, name*)
-----------------------
Les arguments sont un objet et une chaine de caractères. Si la chaine de caractères correspond à un des attributs de l'objet, la fonction retourne vrai, faux sinon. Cette méthode est implémentée en utilisant la fonction getattr(object, name) et d'observer si elle soulève une exception AttributeError ou non.

.. _hash:

--------------
hash(*object*)
--------------
Retourne la valeur hashée de l'objet. Ces valeurs hashés sont des entiers. Elles sont utilisées pour comparer des clés de dictionnaire efficacement.

.. _help:

----------------
help(*[object]*)
----------------
Invoque l'aide de base de Python. Si aucun argument n'est passé, la page de base de l'aide
sera affichée. Si l'argument est une chaine de caractères, alors la méthode va chercher si elle correspond au nom d'un module, si oui elle affiche la page d'aide en question.

.. _hex:

---------
hex(*x*)
---------
Convertit un nombre entier en une chaine hexadécimale préfixée par "0x" par exemple:

.. code-block:: pycon

   >>> hex(255)
   '0xff'
   >>> hex(-42)
   '0x2a'

Si l'entier n'est pas un entier Python, il doit définir une méthode ``__index__()`` qui retourne un entier.

.. _id:

------------
id(*object*)
------------
Retourne "l'identité" d'un objet. Cette identité est un entier qui est garanti d'être unique et constant pendant toute la vie de l'*object*.

.. input:

----------------
input(*[prompt*)
----------------
Permet d'ajouter du texte supplémentaire à une chaine de caractères avant l'affichage.

Exemple: 

.. code-block:: pycon

   >>> str = input('J'aime')
   J'aime le chocolat au lait!
   >>> s
   le chocolat au lait!

.. todo:: Cet exemple est cassé.

.. _isinstance:

--------------------------------
isinstance(*object, classinfo*)
--------------------------------
Retourne vrai si l'objet passé en paramètre est un objet appartenant à la classe spécifiée dans *classinfo*. Si *classinfo* est composé de plusieurs classes, object doit au moins appartenir à une des classes pour que la fonction retourne vrai, retourne faux sinon.

.. _iter:

---------------------------
iter(*object[, sentinel]*)
---------------------------
Retourne un objet *iterator*. Le premier argument est interprété très différemment selon si le deuxième argument est présent ou non. Sans deuxième argument, *object* doit être une collection d'objet qui supporte le protocole d'itération. Si le deuxième argument est présent, alors *object* doit être un objet appelable.

.. _len:

---------
len(s)
---------
Retourne la taille (le nombre d'attributs) d'un objet. L'argument s peut être une séquence comme un string, des bytes ou une liste. Il peut aussi être une collection comme un dictionnaire ou un set.

.. très imprécis. http://lucumr.pocoo.org/2011/7/9/python-and-pola/

.. _locals:

---------
locals()
---------
Mets à jour et retourne le dictionnaire qui représente la table de symbole courante  

.. _map:

------------------------------
map(*function, iterable, ...*)
------------------------------
Retourne un itérateur qui applique *function* à tout les objets contenu dans *iterable*.

.. _max:

-----------------------------
max(*arg1, arg2, args[,key]*)
-----------------------------
Retourne le plus grand objet d'un itérable composé de tout les objets de *arg1* et de *arg2*

.. _memoryview:

-----------------
memoryview(*obj*)
-----------------

Retourne une "memory view" d'un objet créé à partir de *obj* passé en argument.

.. memoryview est une classe, cette fonction est un constructeur.

.. _min:

-----------------------------
min(*arg1, arg2, args[,key]*)
-----------------------------

Retourne le plus petit objet d'un itérable composé de tout les objets de *arg1* et de *arg2*

.. _next:

---------------------------
next(*iterator[, default]*)
---------------------------
Donne le prochain item d'*iterator* en appelant sa fonction ``__next_()``.



.. _oct:

---------
oct(*x*)
---------
Convertit un entier en octale. Si x n'est pas un entier Python il doit avoir définit une méthode ``__index__()`` qui retourne un entier.

.. _open:

-----------------------------------------------------------------------------------------------------------------
open(*file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None*)
-----------------------------------------------------------------------------------------------------------------
Ouvre un fichier et retourne le *file object* correspondant. Si le fichier ne peut pas être ouvert, une erreur OSError est levée.

*file* doit être le chemin du fichier en absolu ou en relatif.

mode est un paramètre qui permet de déterminer le mode d'ouverture du fichier. Par défaut le mode 'r' est choisi. Ce qui signifie que le fichier est ouvert en lecture. Un autre mode commun est 'w' pour passer en mode écriture.

* **'r'** - Ouvert en lecture
* **'w'** - Ouvert en écriture
* **'x'** - Ouvert en création, échoue si le fichier existe déjà
* **'b'** - Mode binaire
* **'t'** - Mode texte (par défaut)
* **'+'** - Ouvre un fichier disque en écriture et lecture

Voir: :ref:`io-tutorial`

Conclusion
==========

Malheureusement, ce document ne contient pas une liste exhaustive de toutes les classes et fonctions inclue dans l’interpréteur Python. En effet, la limite de page pour chaque article ne permettait pas de toutes les décrire de façon complète.

Pour conclure, les fonctions et classes présentées dans cette section font parties des plus basiques et les plus utilisées des commandes. La plupart du temps, nous les utilisons sans trop réfléchir à leur implémentation ou bien même sans savoir tout les possibilités quelles détiennent. En effet il est parfois intéressant de regarder la documentation pour pouvoir exploiter le plein potentiel de certaines classes ou fonctions.

.. [#afm] <adrien.ferreiramendes@he-arc.ch>
