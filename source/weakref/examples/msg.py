"""Sérialisation de document JSON en binaire avec MessagePack."""

import json

import msgpack

document = {"title": "HE-Arc!", "values": [1000, 2000, 3000]}

# 32 bytes
print(len(msgpack.packb(document)))

# 50 bytes
print(len(json.dumps(document)))
