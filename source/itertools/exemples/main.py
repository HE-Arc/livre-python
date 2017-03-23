"""Exemple principale."""

import os
from itertools import chain, cycle


# function_pairs_begin
def pairs(lst):
    """Pairs("abc") --> [(a,b), (b,c), (c,a)]."""
    i = cycle(lst)
    next(i)
    return list(zip(lst, i))


def getDistance(p):
    """Retourne la distance entre chaque pairs."""
    return list(chain(p[i][1]-p[i][0] for i in range(len(p))))
# function_pairs_end


# sortie_begin
chemin = [5, 3, 23, 223]
steps = pairs(chemin)
print(steps)
distances = getDistance(steps)
print(distances)
distance = sum(distances)
print(distance)
# sortie_end

# parcours_de_fichier_begin
for element in os.listdir('./'):
    if os.path.isdir(element):
        print("'%s' un dossier" % element)
    else:
        print("'%s' est un fichier" % element)
# parcours_de_fichier_end
