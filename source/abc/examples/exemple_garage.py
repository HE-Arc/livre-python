"""Exemple de classe abstraite avec un garage contenant des voitures."""

from collections.abc import Sequence

class Voiture():
    """Des voitures à mettre dans un garage."""
    def __init__(self, marque, couleur):
        """Construits une voiture."""
        self.marque = marque
        self.couleur = couleur

    def afficher(self):
        """Afficher les attributs de la voiture."""
        print(self.marque + ", " + self.couleur)

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
        """ Trouve la voiture à l'index 'index'"""
        return self.voitures[index]

    def __len__(self):
        """Retourne le nombre de voitures"""
        return len(self.voitures)

    def afficher(self):
        """Affiche toutes les voitures du garage."""
        for v in self.voitures :
            v.afficher()

# Création des voitures.
v1 = Voiture('BMW', 'Noir')
v2 = Voiture('Subaru', 'Bleu')
v3 = Voiture('Dacia', 'Rouge')

# On place les voitures dans un garage ainsi qu'un nombre.
g = Garage(v1, v2, v3)

# On affiche le garage.
g.afficher()
