"""Exemple de validation d'un fichier JSON avec JSON Schema."""

import json

from jsonschema import validate

filename = "test.json"
schema = "schema.json"

with open(schema, encoding="utf-8") as fp:
    sch = json.load(fp)

with open(filename, encoding="utf-8") as fp:
    data = json.load(fp)

validate(data, schema)
