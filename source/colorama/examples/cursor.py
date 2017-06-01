"""Déplacement du curseur."""

from colorama import deinit, init

init()

# ici on définit notre style
print('\033[33;42;1m')

# deplacement du curseur à l'aide de n lignes
print('\033[3B'+'3 lignes plus bas')

# deplacement du curseur à l'aide de n lignes
print('\033[20C'+'20 caractères plus loin')

# deplacement du curseur à l'aide de coordonnées
print('\033[15;10f'+'Selon coordonées')

deinit()
