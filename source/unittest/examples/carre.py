"""Exemple simple de test unitaire sur une fonction carre."""

import unittest


# func:carre
def carre(x):
    """Élève au carre."""
    return x ** 2


# endfunc:carre


# class:TestCase
class CarreTestCase(unittest.TestCase):
    """Classe testeur pour la fonction carre."""

    test_values = ((2, 4), (0, 0), (-2, 4))

    def test_carre(self):
        """Teste les valeurs références."""
        for value, expected in self.test_values:
            self.assertEqual(expected, carre(value))


# endclass:TestCase

# class:CarreTestCaseFail
class CarreTestCaseFail(unittest.TestCase):
    """Mauvaise classe testeur pour la fonction carre."""

    def test_assert_fail(self):
        """Affichage d'un message d'erreur personnalisé."""
        value = 2
        self.assertEqual(2, carre(value), "Message d'erreur personnalisé")


# endclass:CarreTestCaseFail

# main
if __name__ == '__main__':
    unittest.main()

# endmain
