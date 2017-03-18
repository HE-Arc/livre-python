.. _itertools-tutorial:

======================
  itertools-tutorial
======================

Par Johnny Da Costa <johnny.dacosta@he-arc.ch>



Introduction
------------

Les :py:mod:`itertools` sont des outils puissant pour itérer dans les listes/tableaux de manière
efficace et intelligente. Elles nous simplifient la vie par exemple si l'on veut appliquer une opération
sur chaque élément de notre tableau. On peut aussi très facilement concaténer deux, trois ou n liste avec une simple
fonction :py:func:`count() <itertools.count()>` ou par exemple créer un filtre sur nos tableau avec :py:func:`compress<itertools.compress>`. 


Iterateur infini
----------------

function :py:func:`count(start=0, step=1) <itertools.count>`

Fonction count est un iterateur infini il prend comme paramètre
un début et le step (par défault c'est 1).

.. literalinclude:: use_itertools.py
   :start-after: # COUNT_BEGIN
   :end-before: # COUNT_END


Iterateur avec fin
-------------------

function :py:func:`Chain() <itertools.chain>`
*********************************************
Chain permet de concaténer des listes ensembles en lui passant en paramètre
les listes que vous voulez concatener.

Par exemple : 

.. code-block:: pycon

>>> a = [1, 2, 3, 4, 5, 6, 7]
>>> b = ["Johnny", "David", "Mike", "Bali", "Noami"]
>>> c = ["c", "h", "b", "s", "z"]
>>> for i in chain(a, b, c):
      print(i)
1
2
3
4
5
6
7
Johnny
David
Mike
Bali
Noami
c
h
b
s
z

Une façon plus élégante d'afficher une liste est d'utiliser 
la fonction list qui va nous retourner une liste(captain obvious) qui vous
suffira de print.

>>> print(list(chain(a, b, c)))
[1, 2, 3, 4, 5, 6, 7, 'Johnny', 'David', 'Mike', 'Bali', 'Noami', 'c', 'h', 'b', 's', 'z']
>>> print(list(chain(a[:1], b[:1], c[:1])))
[1, 'Johnny', 'c']
>>> print(list(chain(a[0:2], b[0:2], c[0:2]))
[1, 2, 'Johnny', 'David', 'c', 'h']
 
function :py:func:`Compress() <itertools.compress>`
***************************************************
Par fois il est intéressant de récuperer seulement une partie des données dans notre tableau et grace à la 
méthode compress ou peut lui appliquer un filtre. 

Par exemple un filtre bnaire. les bits à 1(=true) renvoi l'élément se situant à la même position
et 0(=false) ne renvoi pas le valeur. 


.. code-block:: pycon

>>> ListeName = ["Johnny", "Toto", "Tata", "Roger", "Steve"]
>>> filter_binaire = [1, 0, 1, 0, 1]
>>> b = list(compress(a, filter_binaire)) # on récupere sous forme de liste
>>> print(b)
[1, 3, 5]
 
   
function :py:func:`filterfalse() <itertools.filterfalse>`
**************************************************************************************************
Dans la même idée que la fonction compress filter/filterfalse sont des fonctions qui vont
vous permettre de filtre vos tableaux. La puissance des filters c'est que l'on puisse utiliser
des lambdas (function anonyme que l'on peut passer directement en paramêtre d'une fonction).

Exemple : 

- création d'un filtre pair et impair.
- paire = on va utiliser filter car il nous retourne la valeur si la condition est 0(=false).
- impaire = on va utiliser le :py:func:`filterfalse() <itertools.filterfalse>` qui fait la même chose mais qui renvoie la valeur si la condition est différet de 0.

.. code-block:: pycon

>>> listeNumber = [1, 2, 3, 5, 6]
>>> listeNumberOdds = list(filter(lambda x: x % 2, listeNumber)) 
>>> listeNumberEvens = list(filterfalse(lambda x: x % 2, listeNumber))  # 
>>> print(listeNumberOdds)
[0, 2, 4]
>>> print(listeNumberEvens)
[1, 3, 5]

function map()
*****************************************
La function map() nous permet d'appliquer une opération
sur chaque élément du tableau. Pour cela la fonction prend en paramètre une fonction
callback ou un lambda.

Exemple :
  - mettre au cube chaque élément de notre tableau
  
.. code-block:: pycon  
 
>>> listeNumber = [1, 2, 3, 4]
>>> def cube(x):
    """Renvoi notre x à la puissance 3."""
    return x**3
>>> listeNumberCube = list(map(cube, listeNumber))
>>> print(listeNumber)
[1, 2, 3, 4]
>>> print(listeNumberCube)
[1, 8, 27, 64]
>>> listeNumberCubeV2 = list(map(lambda x: x**3, listeNumber)) # syntaxe avec un lambda (en une ligne pas mal non ?)
>>> print(listeNumberCubeV2)
[1, 8, 27, 64]
   
   
function :py:func:`dropwhile() <itertools.dropwhile>`
*****************************************************

.. code-block:: pycon   

>>> dropwhile = list(dropwhile(lambda x: x < 5, [1, 4, 23, 2, 42, 23, 2]))
>>> print(dropwhile)[23, 2, 42, 23, 2]
   
function :py:func:`takewhile() <itertools.takewhile>`
*****************************************************

.. code-block:: pycon   

>>> takewhile = list(takewhile(lambda x: x < 5, [1, 4, 54, 23, 2, 42, 23, 2]))
>>> print(takewhile)
[1, 4]
