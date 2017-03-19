.. _itertools-tutorial:

=============
``itertools``
=============

Par Johnny Da Costa [#jd]_

Introduction
------------
Le module itertools de Python nous propose un bon nombre de générateurs prêts à l'emploi. Qu'est-ce qu'un générateur ou un itérateur ? Pour comprendre ça, nous allons utiliser un exemple très simple. Imaginez que vous avez une liste et que vous voulez l'afficher. La première chose qui nous vient en tête est d'utiliser une boucle.

.. code-block:: pycon

>>> liste = ["I", "do" "love", "programming", "in", "python"]
>>> for i in liste:
    print(i)
I
do
love
programming
in
python

Derrière cette boucle **for** se cache enfet un itérateur. C'est un objet qui va être chargé de parcourir un objet conteneur, dans  notre cas notre liste. Quand Python va tomber sur la ligne **for i in liste:**, il va appeler l'itérateur de notre liste pour pouvoir la parcourir. L'itérateur se crée dans la méthode **__iter__** de notre objet liste dans notre cas. Et lui va nous retourner notre itérateur pour pouvoir parcourir notre petit liste.

A chaque itération python va appeler la méthode **__next__** de notre liste pour itérer à l'élément suivant ou s'arrêter avec l'execption **StopIteration** si le parcours à fini de parcour la liste.

Voici un autre exemple mais avec une chaine string.

.. code-block:: pycon

>>> chaine = "Python"
>>> iterateur = iter(chaine) # va nous retourner un itérateur sur notre chaine
>>> print(next(iterateur)) # va nous afficher la première lettre de notre string
P
>>> for i in chaine: # va parcourir tous les caractère un à un
    print(i)
P
y
t
h
o
n

Quand au générateurs, ce sont des outils puissants pour créer et manipuler des itérateurs ce qui permet de créer des choses complexe avec très peu de code.


Itérateurs offert par Python
----------------------------
Python nous offres des :py:mod:`itertools` qui sont des itérateurs qui nous permette d'itérer sur nous objets. Voici une petit liste non-exaustif de ce que nous propose se module : 

- :py:func:`itertools.count` : crée un itérateur qui va nous retourner des valeurs espacé de par 1 défault. Attention boucle inifni.
- :py:func:`itertools.repeat` : va nous répeter les éléments n fois.
- :py:func:`itertools.chain` : permet de concaténer des listes, chaine de caractère, etc...
- :py:func:`itertools.filterfalse` : créer un itérateur qui va filtrer les éléments qui sont itérable et nous retourner seulement ceux qui réponde faux à notre prédicat
- todo : mettre encore deux trois itertools...

La liste est encore longue et le but ici n'est pas de voir chaque :py:mod:`itertools` mais de comprendre le concept d'iterateur. Rien de mieux que pour comprendre ce que sont les itérateur que de créer le notre.

Nos itertools perso
-------------------
Nous allons ici créer une classe qui va nous retourner un itérateur qui va parcouir un liste de la fin jusqu'au début.

Exemple inspiré de la documentation de pyhton : https://docs.python.org/3/tutorial/classes.html#iterators.

- Première étape nous allons créer notre class qui va nous retourner un itérateur

.. literalinclude:: ./exemples/tools.py
   :start-after: # iterateur_perso_begin
   :end-before: # iterateur_perso_end

- Deuxième étape remplacer l'itérateur de l'objet liste par le notre.

.. literalinclude:: ./exemples/tools.py
   :start-after: # revlist_begin
   :end-before: # revlist_end
   
- troisième étape utiliser notre itertools perso!

.. code-block:: pycon

>>> liste = revList(list(islice(count(), 0, 10)))
>>> for i in liste:
    print(i)
9
8
7
...

Exemple
-------
Essayons maintenant de résoudre un problème avec les itertools que Pythons nous offre. Imaginons que nous avons une liste de point qui formerai un chemin dont on aimerai connaitre la distance.

Objectif :
.. code-block:: pycon

>>> chemin = [A, B, C]
>>> ...
>>> pairs = [(A, B), (B, C), (C, A)]
>>> ...
>>> distances = [len(B - A), len(C - B), len(A - C)]
>>> distance = sum(distances)

Voici nos fonctions : 

.. literalinclude:: ./exemples/main.py
   :start-after: # function_pairs_begin
   :end-before: # function_pairs_end

Sortie : 
.. code-block:: pycon

>>> chemin = [5, 3, 23, 223]
>>> steps = pairs(chemin)
>>> print(steps)
[(5, 3), (3, 23), (23, 223), (223, 5)]
>>> distances = getDistance(steps)
>>> print(distances)
[-2, 20, 200, -218]
>>> distance = sum(distances)
>>> print(distance)
0

:py:func:`itertools.cycle` va nous créer un itérateur qui va retourner les élélments en faisant à chaque fois une copie. Quand la boucle est terminé il va retourner les éléments qui la sauvé.
Dans notre cas il va décaler notre liste et rajouter le première élément qu'il a enregistré à la fin. Ensuite il nous suffit de lui appliquer la fonction :py:func:`zip` qui va nous "zipper" tous ça en pair.



Conclusion
----------

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


.. [#jd] <johnny.dacosta@he-arc.ch>

todo : déclarer les sources...
