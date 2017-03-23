"""Exemple de création de réduite de Farey."""

from fractions import Fraction


def Farey(a, b):
    """Définition fonction de création de la suite de Farey."""
    n = a.numerator + b.numerator
    d = a.denominator + b.denominator
    return Fraction(n, d)


a = Fraction(4, 5)
b = Fraction(2, 13)

print(Farey(a, b))
