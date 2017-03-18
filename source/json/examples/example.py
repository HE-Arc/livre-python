"""Exemple de lecture et d'écriture depuis et vers un fichier JSON."""

import json

entrée = "test.json"
sortie = "test.out.json"

with open(entrée, "r", encoding="utf-8") as fp:
    données = json.load(fp)

données["counter"] += 1

with open(sortie, "w", encoding="utf-8") as fp:
    json.dump(données, fp, sort_keys=True, indent=4)
