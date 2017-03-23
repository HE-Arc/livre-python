"""Exemple de classe abstraite."""

import abc


class Shape(metaclass=abc.ABCMeta):
    """Shape est une classe abstraite."""

    # Méthode abstraite car les formes ont
    # différentes manière de calculer leur aire.
    @abc.abstractmethod
    def calculateArea():
        """Calcul l'aire. Méthode abstraite."""

    # Méthode pas abstraite car elle est la même pour toute les formes.
    def about(self):
        """Affiche un "a propos" de la classe."""
        print('Exemple de classe abstraite.')


class Rectangle(Shape):
    """Rectangle hérite de Shape."""

    def __init__(self, hauteur, largeur):
        """Initialisation des attributs."""
        self.hauteur = hauteur
        self.largeur = largeur

    def calculateArea(self):
        """Calcul l'aire d'un rectangle."""
        return self.hauteur * self.largeur


class Triangle(Shape):
    """Triangle hérite de Shape."""

    def __init__(self, hauteur, base):
        """Initialisation des attributs."""
        self.hauteur = hauteur
        self.base = base

    def calculateArea(self):
        """Calcul l'aire d'un triangle."""
        return self.hauteur * self.base / 2


# Shape.register(Rectangle)
# Shape.register(Triangle)

rec = Rectangle(5, 6)
tri = Triangle(5, 6)
rec2 = Rectangle(2, 2)
listeShape = [rec, rec2, tri]

# On peut parcourir les formes et calculer leur aire.
for shape in listeShape:
    print(shape.calculateArea())

rec.about()
