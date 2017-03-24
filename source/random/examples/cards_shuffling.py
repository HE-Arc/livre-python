"""Exemple d'attribution de cartes."""

import random

# Préparation des cartes.
valeur = ["Deux", "Trois", "Quatre", "Cinq", "Six", "Sept",
          "Huit", "Neuf", "Dix", "Valet", "Dame", "Roi", "As"]
enseigne = ["Coeur", "Pique", "Carreau", "Trèfle"]

# Préparation du jeu de cartes (52 cartes).
jeu = []
for e in enseigne:
    for v in valeur:
        carte = v + " de " + e
        jeu.append(carte)

# Mélange du jeu de cartes.
random.shuffle(jeu)

# Création de la main du joueur (5 cartes).
main = jeu[:5]

# Affichage de la main du joueur.
print("Main du joueur :")
for c in main:
    print("- " + c)
