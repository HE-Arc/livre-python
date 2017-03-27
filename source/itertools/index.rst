.. _itertools-tutorial:

=============
``itertools``
=============

.. image:: ./img/toolsbox.png
    :scale: 40%
    :align: right
    :alt: lock logo
    :target: https://www.iconfinder.com/icons/286688/tool_kit_toolbox_tools_icon#size=512

Par Johnny Da Costa [#jd]_

Introduction
------------
Le module itertools de Python nous propose un bon nombre de générateurs prêts à l'emploi. Qu'est-ce qu'un générateur ou un itérateur ? Que permettent les itérateurs. Pour comprendre ça, nous allons utiliser un exemple très simple. Imaginez que vous avez une liste et que vous voulez l'afficher. La première chose qui nous vient à l'esprit est d'utiliser une boucle.

.. code-block:: pycon

    >>> liste = ["I", "do" "love", "programming", "in", "python"]
    >>> for i in liste:
    ...     print(i)
    I
    do
    love
    programming
    in
    python

Derrière cette boucle **for** se cache enfet un itérateur. C'est un objet qui va être chargé de parcourir un objet conteneur, dans  notre cas notre liste. Quand Python va tomber sur la ligne **for i in liste:**, il va appeler l'itérateur de notre liste pour pouvoir la parcourir. L'itérateur se crée dans la méthode **__iter__** de notre objet liste dans notre cas. Et va nous retourner notre itérateur pour pouvoir parcourir notre petite liste.

A chaque itération python va appeler la méthode **__next__** de notre liste pour itérer à l'élément suivant ou s'arrêter avec l'exception **StopIteration** si le parcours est fini.

Voici un autre exemple mais avec une chaine caractère.

.. code-block:: pycon

    >>> chaine = "Python"
    >>> iterateur = iter(chaine) # va nous retourner un itérateur sur notre chaine
    >>> print(next(iterateur)) # va nous afficher la première lettre de notre string
    P
    >>> for i in iterateur: # va parcourir tous les caractères un à un
    ...     print(i)
    y
    t
    h
    o
    n

On voit que le **P** à déjà été consommé lors de l'appel à la fonction **next(iterateur)**

Itérateurs offerts par Python
-----------------------------
Python nous offres des :py:mod:`itertools` qui sont des itérateurs qui nous permette d'itérer sur nous objets. Voici une petit liste non-exaustif de ce que nous propose se module : 

- :py:func:`~itertools.count` : crée un itérateur qui va nous retourner des valeurs espacé de par 1 défault. Attention boucle inifni.
- :py:func:`~itertools.repeat` : va nous répeter les éléments n fois.
- :py:func:`~itertools.chain` : permet de concaténer des listes, chaine de caractère, etc...
- :py:func:`~itertools.filterfalse` : créer un itérateur qui va filtrer les éléments qui sont itérable et nous retourner seulement ceux qui réponde faux à notre prédicat

La liste est encore longue et le but ici n'est pas de voir chaque :py:mod:`itertools` mais de comprendre le concept d'itérateur. Rien de mieux que pour comprendre ce que sont les itérateur que de créer le notre.

Nos :py:mod:`itertools` perso
-----------------------------
Nous allons ici créer une classe qui va nous retourner un itérateur qui va parcouir un liste de la fin jusqu'au début.

Exemple inspiré de la documentation Python : :ref:`tut-iterators`.

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

    >>> liste = revList(islice(count(), 0, 10))
    >>> for i in liste:
    ...     print(i)
    9
    8
    ...

.. Parfois c'est la même classe qui est la fois l'itérateur et l'itérable. Une
   classes devrait commencer par une majuscule.

Les générateurs
---------------
Les générateurs et les itérateurs sont intimement liés. Pour faire simple, un générateur est une fonction construite à l'aide
du mot clef **yield**. Mais contrairement aux fonctions habituelles, elle n'a pas de **return**, mais un ou plusieurs **yield**. Mais à quoi servent-ils ? Ce sont en fait des objets **itérable**, c'est à dire qu'ils vont à chaque passage nous renvoyé différentes valeurs. Pour les récupérer soit une boucle classique **for ... in ... :** ou bien la méthode **next**.

Un petit exemple simple :

.. code-block:: pycon

    >>> def say_hello(name):
    ...     yield "Bienvenue, "
    ...     yield                # return none
    ...     yield name
    >>> for in say_hello("Johnny"):
    ...     print(i)
    "Bienvenue,"
    None
    "Johnny"

Exemple de générateur **fibonacci**
-------------------------------------

D'après l'exemple de `zeste de savoir`_

.. code-block:: pycon

    >>> def fibonacci(n, a=0, b=1):
    ...     for _ in range(n):
    ...         yield a
    ...         a, b = b, a + b

    >>> list(fibonacci(10))
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    >>> list(fibonacci(5, 6, 7))
    [6, 7, 13, 20, 33]

Exemple d'utilisations d':py:mod:`itertools`
--------------------------------------------

Essayons maintenant de résoudre un problème avec les itertools que Python nous offre. Imaginons que nous avons une liste de points qui formerait un chemin dont on aimerait connaitre la distance.

Objectif :

.. code-block:: pycon

    >>> chemin = [A, B, C]
    >>> pairs = [(A, B), (B, C), (C, A)]

    >>> distances = [len(B - A), len(C - B), len(A - C)]
    >>> distance = sum(distances)

Voici nos fonctions :

.. literalinclude:: ./exemples/main.py
   :start-after: # function_pairs_begin
   :end-before: # function_pairs_end

.. todo::

    ``chain`` ne fait rien. ::

        def distances(p):
            return (a - b for a, b in p)

Sortie :

.. code-block:: pycon

    >>> chemin = [5, 3, 23, 223]
    >>> steps = pairs(chemin)
    >>> print(steps)
    [(5, 3), (3, 23), (23, 223), (223, 5)]
    >>> distances = getDistance(steps)
    >>> distances
    [-2, 20, 200, -218]
    >>> sum(distances)
    0

Un peu de *design pattern*
--------------------------

Tout le monde utilise ce modèle de conception sans même le connaître vraiment. Imaginez le cas on nous voudrions itérer sur un répertoire pour obtenir son contenu ou appliquer un traitement sur chacun des fichiers. Sans  l'approche itérateur,  ils nous faudraient recupérer un flux sur le dossier courant est utiliser un **while** pour parcourir tout notre arborescence et vérifier le type (fichier ou dossier ?) et ensuite afficher. Mais imaginons que notre problème change et que nous ne devons plus itérer sur un répertoire mais sur un autre type de structure... Et on est repartie pour réecrire du code fastidueux et compliqué.

Avec l'utilisation d'itérateur notre programme devient tout de suite plus robuste et plus élégant. Un gros avantage avec ce pattern est que si notre structure change, il nous suffit d'adapter son comportement sur cette objet (`décorateur`_) pour lui indiquer comment itérer sur cette objet. Grâce à ça, nous cachons la compléxité de parcours à notre client qui ne se rend même pas compte de ce qui se passent réelement. 

Mais en Python ce patron de conception est complétement intégré au language. Ce qui nous simplifie grandement la vie!

Voici un `exemple`_ de parcours du contenu d'un répertoire.

.. code-block:: pycon

    >>> for element in os.listdir('./'):
    ...     if os.path.isdir(element):
    ...         print(f"'{element}' un dossier")
    ...     else:
    ...         print(f"'{element}' est un fichier")

Conclusion
----------

:py:mod:`itertools` est un module permettant de faire des choses simpas avec cet objet qu'est l'itérateur. Ils sont tellement utile et important que Python a dédié un module pour les opérations d'itération qui sont les itertools. L'itérateur apporte un niveau d'abstraction (couche de code en plus pour réaliser une action.) L'avantage est que l'itérateur est un objet qui coûte `peu en utilisation mémoire`_. La syntaxe est peu plus élégante car on va masquer au client la complexité de notre code. Les itérateurs nous permettent d'itérer sur toute sorte de structure de données, ce qui rend notre code plus robuste et reutilisable.


.. [#jd] <johnny.dacosta@he-arc.ch>

.. _zeste de savoir: https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/5-generators/
.. _peu en utilisation mémoire : http://apprendre-python.com/page-iterateurs-iterator-generateur-generator-python
.. _itérateur : https://fr.wikipedia.org/wiki/Itérateur
.. _décorateur : https://fr.wikipedia.org/wiki/D%C3%A9corateur_(patron_de_conception)
.. _exemple : http://sametmax.com/appliquer-un-traitement-a-tous-les-fichiers-dun-dossier-en-python/
