"""Classe voiture."""


class Voiture():
    """Des voitures à mettre dans un garage."""

    def __init__(self, marque, couleur):
        """Construit une voiture."""
        self.marque = marque
        self.couleur = couleur

    def afficher(self):
        """Afficher les attributs de la voiture."""
        print(self.marque + ", " + self.couleur)
