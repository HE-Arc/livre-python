.. _dunder-tutorial:

=======
Dunders
=======

Introduction
============

Le mot dunder est un raccourci de Double UNDERscore et représente toutes les méthodes de python qui commencent et finissent par un double underscore (par ex. __init__()).

Les dunders sont des méthodes très puissantes et régulièrement utilisées en python. Ce sont des méthodes universelles que toute classe possède (un peu à l'image de la class Object dans Java).
Cependant, dans python, les dunders ne sont rarement appelés directement.

Par exemple :

.. code-block:: python3

      toto = new MyClass()


fera appel aux méthodes __new__() et __init__() même si ces méthodes n'ont pas été surchargées.

Les dunders ont des méthodes raccourci qui vont directements les appelés (autre raison pour laquelle on utilise régulièrement les dunders sans s'en rendre compte) :

.. code-block:: python3

      toto = 4+5


fera appel au dunder __add__()

Ou bien :

.. code-block:: python3

    str("I'm a text")


fera appel au dunder __str__()

La grande puissance des dunders est leur universalité. En effet, python a été programmé de manière à ce qu'une opération soit toujours relié au même dunder.

Par exemple, dans beaucoup de langages, si on veut connaitre la taille d'un truc, il faut d'abord savoir de quoi on parle (un tableau, une liste, un string etc.) avant de faire appel à la méthode appropriée. Dans python, on utilise toujours le dunder __len__() :

.. code-block:: python3

      class SomeClass(object) :
          grammar ={
              1 : "Some string",
              2 : "Another string",
              3 : 42,
              4 : True
          }

          def __init__(self, name) :
              self.name=name

      sc = SomeClass("Totoro")
      print (len(sc.name)) #affiche la taille du string (6)
      print (len(sc.grammar)) #affiche le nombre d'éléments


Une autre grande utilisation des dunders consiste à les surcharger de manière à les personalisé.

De plus, par convention, on déclare une méthode privée comme étant un dunder :

.. code-block:: python3

      def __myPrivateMethod__(self, other):
          return none;


Exemples
========

.. code-block:: python3

      from math import hypot

      class Vector:
          def __init__(self, x=0, y=0):
              self.x = x
              self.y = y

          def __repr__(self):
              return 'Vecteur(%r, %r)' % (self.x, self.y)

          def __abs__(self):
               return hypot(self.x, self.y)

          def __add__(self, other):
              #Overide de l'opérateur +
              x = self.x + other.x
              y = self.y + other.y
              return Vector(x, y)

          def __mul__(self, scalar):
              return Vector(self.x * scalar, self.y * scalar)

          def __truediv__(self, other):
              raise TypeError("On ne peut pas diviser un vecteur !")

      vect = Vector(4,7)
      print(repr(vect)+" a pour norme "+str(abs(vect))) #Vecteur(4,7) a pour norme 8.0622
      vect = vect*2 #Vecteur(8,14)
      vect+=Vector(2,5)  #Vecteur(10,19)
      vect/=5 #lève une exception


.. code-block:: python3

      class Main(object):

      def __init__(self, *args):
        self.cartes = args

      def ajouter(self, carte):
        obj2 = list(self.cartes) #Converti en liste
        obj2.append(carte)
        self.cartes = tuple(obj2)

      def __str__(self):
        return str(u'; '.join(self.cartes).encode('utf8'))

      def __len__(self):
        return len(self.cartes)


      def __getitem__(self, key):
        #Est appelé quand on fait objet[index] ou objet[key].
        return self.cartes[key]

      def __iter__(self):
        #Est appelé quand on fait un iter(objet). La valeur retournée doit être un iterateur.
        return iter(self.cartes)


      def __reversed__(self):
        #Est appelé quand on fait reversed(objt)
        return reversed(self.cartes)


      def __contains__(self, item):
        #Est appelé quand "in objet"
        return item in self.cartes

      main = Main('1Coeur', '7Pique')
      print(str(main))

      main.ajouter('AsCoeur')

      for carte in main: # parce qu'on a défini __iter__ !
      print (carte)

      print (main[0]) # 1Coeur

      print ('3Coeur' in main) # False

      print (len(main))# 3


Différence entre str et repr :

.. code-block:: python3

        print(str(3)==str("3")) # return True car str est ambigu
        print(repr(3)==repr("3")) # return False car non-ambigu (Int != String)


Conclusion
==========

Il existe un nombre incalculable de dunders. Il faut puiser dans la doc afin de connaitre ceux dont on a l'usage et savoir quand ils sont utilisés.
Ce sont de puissants outils de Python qui permettent de facilement spécialiser le comportement d'un objet.

Bibliographie
=============

The Python Data model, extrait de Fluent Python
http://sametmax.com/le-guide-ultime-et-definitif-sur-la-programmation-orientee-objet-en-python-a-lusage-des-debutants-qui-sont-rassures-par-les-textes-detailles-qui-prennent-le-temps-de-tout-expliquer-partie-6/
http://www.diveintopython3.net/special-method-names.html

Par Marc Friedli
