"""Exemple d'attribution de cartes."""

import random

# Préparation des cartes.
valeurs = [
    "Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf", "Dix",
    "Valet", "Dame", "Roi", "As"
]
enseignes = ["Cœur", "Pique", "Carreau", "Trèfle"]

# Préparation du jeu de cartes (52 cartes).
jeu_de_cartes = [f"{v} de {e}" for v in valeurs for e in enseignes]

# Mélange du jeu de cartes.
random.shuffle(jeu_de_cartes)

# Création de la main du joueur (5 cartes).
main = jeu_de_cartes[:5]

# Affichage de la main du joueur.
print("Main du joueur :")
for carte in main:
    print("- " + carte)
