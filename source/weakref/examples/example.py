"""Exemple de lecture et d'écriture depuis et vers un fichier JSON."""

import json

filename = "test.json"

with open(filename, "r", encoding="utf-8") as fp:
    data = json.load(fp)

data["counter"] += 1

with open(filename, "w", encoding="utf-8") as fp:
    json.dump(data, fp, sort_keys=True, indent=4)
