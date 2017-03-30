"""Lecture en streaming d'un gros document JSON."""

from pprint import pprint
from urllib.request import urlopen

import ijson

f = urlopen('https://www.reddit.com/.json')

# data.children représente le chemin dans le fichier
# dont les éléments nous intéressent.
for child in ijson.items(f, 'data.children'):
    pprint(child)
