"""Exemple d'utilisation des classes Garage et Voiture."""

from garage import Garage
from voiture import Voiture

# Création des voitures.
v1 = Voiture('BMW', 'Noir')
v2 = Voiture('Subaru', 'Bleu')
v3 = Voiture('Dacia', 'Rouge')

# On place les voitures dans un garage ainsi qu'un nombre.
g = Garage(v1, v2, v3)

# On affiche le garage.
g.afficher()
