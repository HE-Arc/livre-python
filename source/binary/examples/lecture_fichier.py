"""Module d'exemple d'une lecture de fichier."""


with open("test_file.dat", "rb") as binary_file:
    # Lit tout le fichier.
    data = binary_file.read()
print(data)


# Lit N bytes depuis une certaine position.
binary_file.seek(0)
couple_bytes = binary_file.read(2)
print(couple_bytes)
