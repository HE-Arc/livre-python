"""Exemple d'attribution de cartes."""

import random

# Préparation des cartes.
valeurs = ["Deux", "Trois", "Quatre", "Cinq", "Six", "Sept",
          "Huit", "Neuf", "Dix", "Valet", "Dame", "Roi", "As"]
enseignes = ["Coeur", "Pique", "Carreau", "Trèfle"]

# Préparation du jeu de cartes (52 cartes).
jeu = []
for enseigne in enseignes:
    for valeur in valeurs:
        carte = valeur + " de " + enseigne
        jeu.append(carte)

# Mélange du jeu de cartes.
random.shuffle(jeu)

# Création de la main du joueur (5 cartes).
main = jeu[:5]

# Affichage de la main du joueur.
print("Main du joueur :")
for c in main:
    print("- " + c)
