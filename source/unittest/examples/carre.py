"""Exemple simple de test unitaire sur une fonction carré."""

import unittest


# func:carré
def carré(x):
    """Élève au carré."""
    return x**2

# endfunc:carrée


# class:TestCase
class CarreTestCase(unittest.TestCase):
    """Classe testeur pour la fonction carrée."""

    test_values = ((2, 4), (0, 0), (-2, 4))

    def test_carré(self):
        """Teste les valeurs références."""
        for value, expected in self.test_values:
            self.assertEqual(expected, carré(value))

# endclass:TestCase


# main
if __name__ == '__main__':
    unittest.main()

# endmain
