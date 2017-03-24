"""Exemple de lecture et écriture avec io."""

with open('input.txt', 'r') as inputStream:
    with open('output.txt', 'w') as os:
        os.write(inputStream.read(10))
