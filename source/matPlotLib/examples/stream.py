"""Lecture en streaming d'un gros document JSON."""

from urllib.request import urlopen

import ijson

f = urlopen('https://www.reddit.com/.json')
items = ijson.items(f, 'data.children')
for item in items:
    print(item)
