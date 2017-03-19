.. _itertools-tutorial:

=============
``itertools``
=============

Par Johnny Da Costa [#jd]_



Introduction
------------
Le module itertools de Python nous propose un bon nombre de générateurs prêts à l'emploi. Qu'est-ce qu'un générateur ou un itérateur ? Pour comprendre ça, nous allons utiliser un exemple très simple. Imaginer que vous avez une liste et que vous voulez l'afficher. La première chose qui nous vient en tête est d'utiliser une boucle.

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
- itertools.filter : créer un itérateur qui va filtrer les éléments qui sont itérable et nous retourner seulement ceux qui réponde vrai à notre prédicat. :py:func:`itertools.filterfalse` fait l'opération inverse.

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
