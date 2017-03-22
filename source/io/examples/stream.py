"""Exemple de lecture et écriture avec io."""

try:
    with open('input.txt', 'r') as inputStream:
        with open('output.txt', 'w') as os:
            os.write(inputStream.read(10))
except PermissionError:
    print("PermissionError")
except OSError:
    print("OSError/IOError")
