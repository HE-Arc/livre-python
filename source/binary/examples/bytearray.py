"""Module d'exemple d'instanciation un bytearray."""


# Crée un bytearray à partir d'un objet bytes.
msg = bytearray(b"exemple")
# Crée un  bytearray à partir d'une chaine de caractères.
msg = bytearray("exemple", "utf-8")
# Crée un  bytearray à partir d'une liste d'entiers entre 0 et 255.
msg = bytearray([94, 91, 101, 125, 111, 35, 120, 101, 115, 101, 200])

# hexadécimal.
0xff  # sortie 255.
# binaire.
0b100  # sortie 4.

# autres possibilitées.
"{:x}".format(int.from_bytes("exemple".encode("utf-8"), byteorder="big"))
# sortie '6578656d706c65'.

# 65 est la lettre 'e' en hexadécimal.
f"{ord('e'):x}"  # sortie '65'.
