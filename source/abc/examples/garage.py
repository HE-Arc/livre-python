"""Classe garage."""


from collections.abc import Sequence
from voiture import Voiture


class Garage(Sequence):
    """Classe iterable."""

    def __init__(self, *voitures):
        """Constructeur."""
        for v in voitures:
            if isinstance(v, Voiture):
                pass
            else:
                raise TypeError(f"{v!r} n'est pas une voiture.")

        self.voitures = voitures

    def __getitem__(self, index):
        """Trouve la voiture à l'index 'index'."""
        return self.voitures[index]

    def __len__(self):
        """Retourne le nombre de voitures."""
        return len(self.voitures)

    def afficher(self):
        """Affiche toutes les voitures du garage."""
        for v in self.voitures:
            v.afficher()
