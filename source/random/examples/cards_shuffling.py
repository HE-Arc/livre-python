"""Exemple d'attribution de cartes."""

import random

# Préparation des cartes.
valeurs = ["Deux", "Trois", "Quatre", "Cinq", "Six", "Sept",
          "Huit", "Neuf", "Dix", "Valet", "Dame", "Roi", "As"]
enseignes = ["Coeur", "Pique", "Carreau", "Trèfle"]

# Préparation du jeu de cartes (52 cartes).
jeu_de_cartes = []

for enseigne in enseignes:
    for valeur in valeurs:
        nouvelle_carte = valeur + " de " + enseigne
        jeu_de_cartes.append(nouvelle_carte)

# Mélange du jeu de cartes.
random.shuffle(jeu_de_cartes)

# Création de la main du joueur (5 cartes).
main = jeu_de_cartes[:5]

# Affichage de la main du joueur.
print("Main du joueur :")
for carte in main:
    print("- " + carte)
