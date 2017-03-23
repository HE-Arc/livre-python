.. _abc-tutorial:

``Abstract Base Class``
=======================

Par Sylvain Renaud <sylvain.renaud@he-arc.ch>

Introduction
------------
Les classes abstraites sont comme des classes standard, avec la particulatrité qu'on ne pourra pas créer d'objets de ces classes.

Les classes abstraites doivent être spécifiées. Les classes qui spécifient notre classe abstraite pourront elles être instanciées.

Lors de la spécialisation, la classe dérivée aura toutes les méthodes de la classe mère (notre classe abstraite).

Ce mécanisme est utile pour généraliser un objet.
.. Par exemple tout le monde sait à quoi ressemble une Porsche (c'est un terme précis), on peut donc instancier. Mais si l'on demande de représenter un véhicule (terme englobant), tout le monde a une idée différente du terme. La classe véhicule serait donc abstraite et la classe Porsche dérive de Véhicule.
Exemple de classe abstraite : Shape (forme en français)

.. image:: ./abstract_class_shape.jpg
   :align: center
   :alt: Abstract class Shape

La classe abstraite ``Shape`` possède la méthode ``calculateArea()``.
Nous savons qu'une forme géométrique possède une aire.
Mais nous ne savons pas comment la calculer sans connaître la forme.
C'est pourquoi il est nécessaire de créer des classes qui dérives de Shape.
Par exemple un rectange possède une aire calculable par ``hauteur*largeur``.
Idem pour d'autres formes géométriques qui ont leurs propre manière de calculer leur aire.

Grâce au polymorphisme, nous pouvons par exemple créer des listes de ``Shape``.
Dans ces listes il y aura des rectangles, triangles, etc.
Si nous demandons à chaque élément de la liste de calculer son aire, il l'a calculera grâce à sa propre formule.
De plus, nous sommes certains que chaque élément de la liste possède la méthode ``calculateArea()`` puisqu'il est une ``Shape``.


Exemple
-------
Nous voulons donc pouvoir faire cela.

.. code-block:: python

   for shape in listeShape:
      print(shape.calculateArea())

Pour cela, il faut une classe abstraite Shape qui contienne la méthode abstraite ``calculateArea()``.

.. code-block:: python

   class Shape(metaclass=abc.ABCMeta):
      """Shape est une classe abstraite."""

      # Méthode abstraite car les formes ont différentes manière de calculer leur aire.
      @abc.abstractmethod
      def calculateArea():
         """Calcul l'aire. Méthode abstraite."""
         pass

Ensuite, on créé une classe ``Rectange`` qui implémente (hérite de) ``Shape``.

.. code-block:: python

   class Rectangle(Shape):
      """Rectangle hérite de Shape."""

      def __init__(self, hauteur, largeur):
           """Initialisation des attributs."""
           self.hauteur = hauteur
           self.largeur = largeur

      def calculateArea(self):
           """Calcul l'aire d'un rectangle."""
           return self.hauteur * self.largeur

Ici on impémente la méthode ``calculateArea()`` avec la méthode de calcul ``largeur * hauteur``.
Si on oublie d'implémenter les méthodes abstraites dans une classe sensée implémenter une classe abstraite, une erreur se produit :
``TypeError: Can't instantiate abstract class Rectangle with abstract methods calculateArea``

En revanche on peut tout à fait, dans la classe abstraite implémenter complètement une méthode.
Les enfants hériteront alors de cette méthode. Il suffit de ne pas la marquer comme ``@abstractmethod``.

Ensuite faisons une autre classe, ``Triangle``, qui implémente ``Shape``. Elle aura le même prototype que
``Rectangle`` mais la méthode ``calculateArea()`` calculera l'aire différement.

.. code-block:: python

    class Triangle(Shape):
        """Triangle hérite de Shape."""

        def __init__(self, hauteur, base):
            """Initialisation des attributs."""
            self.hauteur = hauteur
            self.base = base

        def calculateArea(self):
            """Calcul l'aire d'un triangle."""
            return self.hauteur * self.base / 2

Nous pouvons ensuite créer une liste de Rectangle et de Triangle puis calculer l'aire de chacun d'entre
eux en une instruction, comme présenté avant.



Création d'une structure de données
-----------------------------------
Les classes abstraites peuvent également être utilisées pour créer sa propre structure de données.
En implémentant par exemple ``collections.abc.Sequence``, nous devrons redéfinir quelques méthodes qui
permettront d'utiliser notre classe comme une liste. Nous pouvons par des assertions vérifier les
éléments de cette liste pour qu'ils soient tous du même type.

Je propose comme exemple une classe ``Garage`` qui contient une liste de ``Voiture``.

.. code-block:: python

   class Garage(Sequence):
   """Classe iterable."""

      def __init__(self, *voitures):
         """Constructeur."""

         for v in voitures:
            if isinstance(v, Voiture):
               pass
            else:
               raise TypeError('La liste ne contient pas que des Voiture.')

         self.voitures = voitures

      def __getitem__(self, index):
         """ Trouve la voiture à l'index 'index'"""
         return self.voitures.__getitem__(index)

      def __len__(self):
         """Retourne le nombre de voitures"""
         return self.voitures.__len__()

      def afficher(self):
         for v in self.voitures :
            v.afficher()


De même que l'exemple précédent, on aimerait afficher toutes les voitures d'un garage. Mais en appelant simplement
une méthode du garage:

.. code-block:: python

   # Création des voitures.
   v1 = Voiture('BMW', 'Noir')
   v2 = Voiture('Subaru', 'Bleu')
   v3 = Voiture('Dacia', 'Rouge')

   # On place les voitures dans un garage.
   g = Garage(v1, v2, v3)

   # On affiche le garage (toutes les voitures qu'il contient)
   g.afficher()

La classe ``Garage`` implémente la classe abstraite ``collections.abc.Sequence``. Tout comme les ``list``.
On peut donc accéder à une voiture du garage par son index, obtenir le nombre de voiture du garage et d'autres
méthodes semblables à l'utilisation d'une ``list``.

.. code-block:: pycon

   >>> g.__getitem__(0).afficher()
   BMW, Noir
   >>> g.__len__()
   3
